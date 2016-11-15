## Steps to release a new version

- Change version in setup.py and troposphere/\_\_init\_\_.py
- Update CHANGELOG.md with changes made since last release
- Create a signed tag: ```git tag --sign -m "Release 1.1.1" 1.1.1```
- Create PyPI release: ```python setup.py sdist upload --sign```
- Push commits: ```git push```
- Push tag: ```git push --tags```
- Update github release page: https://github.com/cloudtools/troposphere/releases
