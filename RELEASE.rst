Releasing
=========

Steps to release a new version
------------------------------

- Update the version using ``poetry version [RULE|<version>]``
- Update CHANGELOG.md with changes made since last release
- Verify release installs on Python 3: ``make release-test``
- Create a signed tag: ``git tag --sign -m "Release 1.1.1" 1.1.1``
- Build the distribution: ``poetry build``
- Publish the release: ``poetry publish``
- Push commits: ``git push``
- Push tag: ``git push --tags``
- Update github release page: https://github.com/cloudtools/troposphere/releases


Helper to create CHANGELOG entries
----------------------------------

``git log --reverse --pretty=format:"%s" | tail -100 | sed 's/^/* /'``

Helper to list supported resources
----------------------------------

``grep -h 'resource_type = "AWS::' troposphere/* | sed 's/[ ]*resource_type = "'// | cut -f1-3 -d: | sort | uniq | sed 's/^/- /'``
