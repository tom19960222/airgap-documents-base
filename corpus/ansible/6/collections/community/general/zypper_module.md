---
collection: ansible
version: "6"
title: "community.general.zypper module – Manage packages on SUSE and openSUSE"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/zypper_module.html
fetched_at: 2026-07-27T17:14:14+00:00
---
# community.general.zypper module – Manage packages on SUSE and openSUSE

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](zypper_module.md#ansible-collections-community-general-zypper-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.zypper`.

- [Synopsis](zypper_module.md#synopsis)
- [Requirements](zypper_module.md#requirements)
- [Parameters](zypper_module.md#parameters)
- [Notes](zypper_module.md#notes)
- [Examples](zypper_module.md#examples)

## [Synopsis](zypper_module.md#id1)

- Manage packages on SUSE and openSUSE using the zypper and rpm tools.
- Also supports transactional updates, by running zypper inside `/sbin/transactional-update --continue --drop-if-no-change --quiet run`.

## [Requirements](zypper_module.md#id2)

The below requirements are needed on the host that executes this module.

- zypper >= 1.0 # included in openSUSE >= 11.1 or SUSE Linux Enterprise Server/Desktop >= 11.0
- python-xml
- rpm

## [Parameters](zypper_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_vendor_change**  boolean  added in community.general 0.2.0 | Adds `--allow_vendor_change` option to *zypper* dist-upgrade command.  Choices:   - `false` ← (default) - `true` |
| **clean_deps**  boolean  added in community.general 4.6.0 | Adds `--clean-deps` option to *zypper* remove command.  Choices:   - `false` ← (default) - `true` |
| **disable_gpg_check**  boolean | Whether to disable to GPG signature checking of the package signature being installed. Has an effect only if state is *present* or *latest*.  Choices:   - `false` ← (default) - `true` |
| **disable_recommends**  boolean | Corresponds to the `--no-recommends` option for *zypper*. Default behavior (`true`) modifies zypper’s default behavior; `false` does install recommended packages.  Choices:   - `false` - `true` ← (default) |
| **extra_args**  string | Add additional options to `zypper` command.  Options should be supplied in a single line as if given in the command line. |
| **extra_args_precommand**  string | Add additional global target options to `zypper`.  Options should be supplied in a single line as if given in the command line. |
| **force**  boolean | Adds `--force` option to *zypper*. Allows to downgrade packages and change vendor or architecture.  Choices:   - `false` ← (default) - `true` |
| **force_resolution**  boolean  added in community.general 0.2.0 | Adds `--force-resolution` option to *zypper*. Allows to (un)install packages with conflicting requirements (resolver will choose a solution).  Choices:   - `false` ← (default) - `true` |
| **name**  aliases: pkg  list / elements=string / required | Package name `name` or package specifier or a list of either.  Can include a version like `name=1.0`, `name>3.4` or `name<=2.7`. If a version is given, `oldpackage` is implied and zypper is allowed to update the package within the version range given.  You can also pass a url or a local path to a rpm file.  When using *state=latest*, this can be ‘\*’, which updates all installed packages. |
| **oldpackage**  boolean | Adds `--oldpackage` option to *zypper*. Allows to downgrade packages with less side-effects than force. This is implied as soon as a version is specified as part of the package name.  Choices:   - `false` ← (default) - `true` |
| **replacefiles**  boolean  added in community.general 0.2.0 | Adds `--replacefiles` option to *zypper* install/update command.  Choices:   - `false` ← (default) - `true` |
| **state**  string | `present` will make sure the package is installed. `latest` will make sure the latest version of the package is installed. `absent` will make sure the specified package is not installed. `dist-upgrade` will make sure the latest version of all installed packages from all enabled repositories is installed.  When using `dist-upgrade`, *name* should be `'*'`.  Choices:   - `"present"` ← (default) - `"latest"` - `"absent"` - `"dist-upgrade"` - `"installed"` - `"removed"` |
| **type**  string | The type of package to be operated on.  Choices:   - `"package"` ← (default) - `"patch"` - `"pattern"` - `"product"` - `"srcpackage"` - `"application"` |
| **update_cache**  aliases: refresh  boolean | Run the equivalent of `zypper refresh` before the operation. Disabled in check mode.  Choices:   - `false` ← (default) - `true` |

## [Notes](zypper_module.md#id4)

> **Note:**
>
> - When used with a `loop:` each package will be processed individually, it is much more efficient to pass the list directly to the *name* option.

## [Examples](zypper_module.md#id5)

```yaml+jinja
- name: Install nmap
  community.general.zypper:
    name: nmap
    state: present

- name: Install apache2 with recommended packages
  community.general.zypper:
    name: apache2
    state: present
    disable_recommends: false

- name: Apply a given patch
  community.general.zypper:
    name: openSUSE-2016-128
    state: present
    type: patch

- name: Remove the nmap package
  community.general.zypper:
    name: nmap
    state: absent

- name: Install the nginx rpm from a remote repo
  community.general.zypper:
    name: 'http://nginx.org/packages/sles/12/x86_64/RPMS/nginx-1.8.0-1.sles12.ngx.x86_64.rpm'
    state: present

- name: Install local rpm file
  community.general.zypper:
    name: /tmp/fancy-software.rpm
    state: present

- name: Update all packages
  community.general.zypper:
    name: '*'
    state: latest

- name: Apply all available patches
  community.general.zypper:
    name: '*'
    state: latest
    type: patch

- name: Perform a dist-upgrade with additional arguments
  community.general.zypper:
    name: '*'
    state: dist-upgrade
    allow_vendor_change: true
    extra_args: '--allow-arch-change'

- name: Perform a installaion of nmap with the install option replacefiles
  community.general.zypper:
    name: 'nmap'
    state: latest
    replacefiles: true

- name: Refresh repositories and update package openssl
  community.general.zypper:
    name: openssl
    state: present
    update_cache: true

- name: "Install specific version (possible comparisons: <, >, <=, >=, =)"
  community.general.zypper:
    name: 'docker>=1.10'
    state: present

- name: Wait 20 seconds to acquire the lock before failing
  community.general.zypper:
    name: mosh
    state: present
  environment:
    ZYPP_LOCK_TIMEOUT: 20
```

### Authors

- Patrick Callahan (@dirtyharrycallahan)
- Alexander Gubin (@alxgu)
- Thomas O’Donnell (@andytom)
- Robin Roth (@robinro)
- Andrii Radyk (@AnderEnder)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
