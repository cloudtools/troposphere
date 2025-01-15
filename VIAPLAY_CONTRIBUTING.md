# More about this fork 

While we should always try to use the official version, in case that Troposphere is lagging behind, we can always bypass this fact and "force an update". Basically this means that we are updating the Cloudformation spec that Troposphere uses internally and regenerating its code so that we can use new features that are not yet supported by the open source version of Troposphere. 

### Create virtual environment and activate it

```
python3 -m venv --clear --upgrade-deps .venv
source .venv/bin/activate
pip3 install -r requirements-dev.txt
```

### Upgrade troposphere to the last Cloudformation spec available
```
make spec regen fix-black
```

### Run tests
```
make test
```

### Create release
```
make release-test
```

### Configuring Pypi for read/writea

~/.pypirc
```
[distutils]
index-servers =
  cloud-virtual
  cloud-local
[cloud-virtual]
repository: https://viaplay.jfrog.io/artifactory/api/pypi/cloud-virtual
username: carlos.mateos@viaplaygroup.com
password: <JFrog token>
[cloud-local]
repository: https://viaplay.jfrog.io/artifactory/api/pypi/cloud-local
username: carlos.mateos@viaplaygroup.com
password: <JFrog token>
```

~/.pip/pip.conf
```
[global]
index-url = https://carlos.mateos@viaplaygroup.com:<JFrog token>@viaplay.jfrog.io/artifactory/api/pypi/cloud-virtual/simple
```

### Create a new release artifact and upload it to JFrog

#### Install Twine (within the troposphere virtual environment)
1. brew install gpgme
2. pip3 install twine
3. gpg --gen-key

#### Relevant steps (copied from RELEASE.rst)
- Change version in troposphere/\_\_init\_\_.py
- Change version in docs/conf.py
- Update CHANGELOG.md with changes made since last release
- Verify release installs on Python 3: ``make release-test``
- Create a signed tag: ``git tag --sign -m "Release 1.1.1" 1.1.1``
- Build the distribution: python -m build --sdist --wheel .
- Use twine to check the release: twine check dist/troposphere-1.1.1*[.whl,.gz]

- Upload using Twine:

```
# TWINE_USER and TWINE_PASSWORD are defined in ~/.zshrc
# TWINE_USER is always your viaplaygroup email
# TWINE_PASSWORD is the token generated in JFrog (see the "Set me up" section in JFrog)

twine upload -r cloud-local -s dist/troposphere-1.1.1*[.whl,.gz] --config-file ~/.pypirc --verbose --username carlos.mateos@viaplaygroup.com --password $TWINE_PASSWORD
```

