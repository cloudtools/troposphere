#!/usr/bin/env python3

import pathlib
import re

resources = set()
resource_re = re.compile(r"(AWS|OS)::(?P<name>\w+)::\w+")
for path in sorted(pathlib.Path("troposphere").glob("*.py")):
    with open(path, "r") as f:
        for line in f.readlines():
            m = resource_re.search(line)
            if m:
                resources.add(m.group("name"))

print("# Currently supported AWS resource types")
print()
for r in sorted(resources):
    print(
        f"- [AWS::{r}](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/AWS_{r}.html)"
    )
