#!/usr/bin/env python3

from __future__ import annotations

import argparse
import glob
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parent.parent
CHANGELOG_PATH = REPO_ROOT / "CHANGELOG.rst"


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the troposphere release workflow."
    )
    parser.add_argument(
        "-n",
        "--dry-run",
        action="store_true",
        help="Skip git tag, git push, and twine commands.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    stage_parser = subparsers.add_parser(
        "stage", help="Prepare the release locally for review."
    )
    stage_parser.add_argument("version", help="Version to release, for example 4.10.2")

    subparsers.add_parser("rollback", help="Undo local staged release changes.")
    subparsers.add_parser("push", help="Create the tag and publish the release.")
    return parser.parse_args(argv)


def run(cmd: Sequence[str], *, skip: bool = False) -> None:
    rendered = " ".join(cmd)
    if skip:
        print(f"[dry-run] {rendered}")
        return

    print(f"+ {rendered}")
    subprocess.run(cmd, cwd=REPO_ROOT, check=True)


def capture(cmd: Sequence[str]) -> str:
    return subprocess.check_output(cmd, cwd=REPO_ROOT, text=True).strip()


def build_artifacts(version: str) -> list[str]:
    pattern = str(REPO_ROOT / "dist" / f"troposphere-{version}*")
    artifacts = sorted(glob.glob(pattern))
    if not artifacts:
        raise RuntimeError(f"No built artifacts found for version {version}")
    return [str(Path(path).relative_to(REPO_ROOT)) for path in artifacts]


def read_current_version() -> str:
    content = (REPO_ROOT / "troposphere" / "__init__.py").read_text()
    match = re.search(r'__version__ = "([^"]+)"', content)
    if not match:
        raise RuntimeError("Could not determine the current version")
    return match.group(1)


@dataclass(frozen=True)
class ReleaseFileChange:
    path: Path

    @property
    def release_path(self) -> str:
        return str(self.path.relative_to(REPO_ROOT))

    def apply(self, version: str) -> None:
        raise NotImplementedError

    def rollback(self) -> None:
        run(
            [
                "git",
                "restore",
                "--source=HEAD",
                "--staged",
                "--worktree",
                "--",
                self.release_path,
            ]
        )


@dataclass(frozen=True)
class VersionFileChange(ReleaseFileChange):
    pattern: str
    replacement: str

    def apply(self, version: str) -> None:
        original = self.path.read_text()
        updated, count = re.subn(
            self.pattern,
            self.replacement.format(version=version),
            original,
        )
        if count != 1:
            raise RuntimeError(f"Failed to update version in {self.path}")
        if updated != original:
            self.path.write_text(updated)
            print(f"Updated {self.release_path}")
        else:
            print(f"No change in {self.release_path}")


@dataclass(frozen=True)
class ChangelogChange(ReleaseFileChange):
    def find_last_release_ref(self) -> tuple[str, str]:
        history = capture(["git", "log", "--format=%H%x00%s%x00%D"])
        for line in history.splitlines():
            commit, subject, decorations = line.split("\x00", 2)

            for tag in re.findall(r"tag: ([^,]+)", decorations):
                if re.fullmatch(r"\d+\.\d+\.\d+", tag):
                    return commit, tag

            match = re.fullmatch(r"Release (\d+\.\d+\.\d+)", subject)
            if match:
                return commit, match.group(1)

        raise RuntimeError("Could not find a prior release tag or release commit")

    def messages(self, since_ref: str) -> list[str]:
        output = capture(
            ["git", "log", "--reverse", "--format=%s", f"{since_ref}..HEAD"]
        )
        messages = [line for line in output.splitlines() if line]
        if not messages:
            raise RuntimeError("No commits found since the last release")
        return messages

    def format_entry(self, version: str, messages: Sequence[str]) -> str:
        heading = f"{version} ({date.today().strftime('%Y*%m*%d')})"
        underline = "-" * len(heading)
        bullets = "\n".join(f"* {message}" for message in messages)
        return f"{heading}\n{underline}\n{bullets}\n\n"

    def entry(self, version: str) -> str:
        since_ref, since_version = self.find_last_release_ref()
        print(f"Generating changelog from commits after release {since_version}.")
        return self.format_entry(version, self.messages(since_ref))

    def print_entry(self, entry: str) -> None:
        print(f"Proposed {self.release_path} entry:\n")
        print(entry, end="")

    def confirm(self) -> bool:
        response = input("Apply this changelog entry and continue staging? [y/N]: ")
        return response.strip().lower() in {"y", "yes"}

    def apply(self, version: str) -> None:
        entry = self.entry(version)
        self.print_entry(entry)

        if not entry.endswith("\n\n"):
            raise RuntimeError("Generated changelog entry is malformed")

        if not self.confirm():
            print("Changelog not written. Exiting without staging changes.")
            raise SystemExit(0)

        original = self.path.read_text()
        self.path.write_text(entry + original)
        print(f"Updated {self.release_path}")


RELEASE_FILE_CHANGES: tuple[ReleaseFileChange, ...] = (
    ChangelogChange(CHANGELOG_PATH),
    VersionFileChange(
        REPO_ROOT / "troposphere" / "__init__.py",
        r'(__version__ = ")([^"]+)(")',
        r"\g<1>{version}\g<3>",
    ),
    VersionFileChange(
        REPO_ROOT / "docs" / "conf.py",
        r'(release = ")([^"]+)(")',
        r"\g<1>{version}\g<3>",
    ),
)


def release_file_changes() -> tuple[ReleaseFileChange, ...]:
    return RELEASE_FILE_CHANGES


def managed_paths() -> list[Path]:
    return [change.path for change in release_file_changes()]


def release_file_args() -> list[str]:
    return [change.release_path for change in release_file_changes()]


def staged_files() -> set[str]:
    output = capture(["git", "diff", "--cached", "--name-only"])
    return {line for line in output.splitlines() if line}


def check_staged_release_files(*, dry_run: bool) -> None:
    expected_files = set(release_file_args())
    staged = staged_files()

    if expected_files.issubset(staged):
        return

    missing = ", ".join(sorted(expected_files - staged))
    message = f"required release files are not staged: {missing}"
    if dry_run:
        print(f"Warning: {message}")
        return

    raise RuntimeError(f"Refusing to push release because {message}")


def stage_release(version: str, *, dry_run: bool) -> int:
    for change in release_file_changes():
        change.apply(version)

    run(["git", "add", *release_file_args()])
    run(["make", "release-test"])
    run(["python3", "-m", "build", "--sdist", "--wheel", "."])

    artifacts = build_artifacts(version)
    if dry_run:
        print("[dry-run] twine check " + " ".join(artifacts))
    else:
        run(["twine", "check", *artifacts])

    print("Release staged locally. Review the staged diff and commit before push.")
    return 0


def rollback_release() -> int:
    version = read_current_version()
    for change in release_file_changes():
        change.rollback()

    tags = capture(["git", "tag"]).splitlines()
    if version in tags:
        run(["git", "tag", "-d", version])

    print("Local release changes have been rolled back.")
    return 0


def push_release(*, dry_run: bool) -> int:
    version = read_current_version()
    check_staged_release_files(dry_run=dry_run)

    artifacts = build_artifacts(version)

    if dry_run:
        print(f'[dry-run] git commit -m "Release {version}"')
        print(f'[dry-run] git tag --sign -m "Release {version}" {version}')
        print("[dry-run] twine upload -s " + " ".join(artifacts))
        print("[dry-run] git push")
        print("[dry-run] git push --tags")
    else:
        run(["git", "commit", "-m", f"Release {version}"])
        run(["git", "tag", "--sign", "-m", f"Release {version}", version])
        run(["twine", "upload", "-s", *artifacts])
        run(["git", "push"])
        run(["git", "push", "--tags"])

    print("Release push phase complete. Update the GitHub release page manually.")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    if args.command == "stage":
        return stage_release(
            args.version,
            dry_run=args.dry_run,
        )
    if args.command == "rollback":
        return rollback_release()
    if args.command == "push":
        return push_release(dry_run=args.dry_run)
    raise RuntimeError(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"Command failed with exit code {exc.returncode}", file=sys.stderr)
        raise SystemExit(exc.returncode)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
