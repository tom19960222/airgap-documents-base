---
collection: ansible
version: "6"
title: "community.general.apk module – Manages apk packages"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/apk_module.html
fetched_at: 2026-07-27T17:08:07+00:00
---
# community.general.apk module – Manages apk packages

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.apk`.

- [Synopsis](apk_module.md#synopsis)
- [Parameters](apk_module.md#parameters)
- [Notes](apk_module.md#notes)
- [Examples](apk_module.md#examples)
- [Return Values](apk_module.md#return-values)

## [Synopsis](apk_module.md#id1)

- Manages *apk* packages for Alpine Linux.

## [Parameters](apk_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **available**  boolean | During upgrade, reset versioned world dependencies and change logic to prefer replacing or downgrading packages (instead of holding them) if the currently installed package is no longer available from any repository.  Choices:   - `false` ← (default) - `true` |
| **name**  list / elements=string | A package name, like `foo`, or multiple packages, like `foo, bar`. |
| **no_cache**  boolean  added in community.general 1.0.0 | Do not use any local cache path.  Choices:   - `false` ← (default) - `true` |
| **repository**  list / elements=string | A package repository or multiple repositories. Unlike with the underlying apk command, this list will override the system repositories rather than supplement them. |
| **state**  string | Indicates the desired package(s) state.  `present` ensures the package(s) is/are present. `installed` can be used as an alias.  `absent` ensures the package(s) is/are absent. `removed` can be used as an alias.  `latest` ensures the package(s) is/are present and the latest version(s).  Choices:   - `"present"` ← (default) - `"absent"` - `"latest"` - `"installed"` - `"removed"` |
| **update_cache**  boolean | Update repository indexes. Can be run with other steps or on it’s own.  Choices:   - `false` ← (default) - `true` |
| **upgrade**  boolean | Upgrade all installed packages to their latest version.  Choices:   - `false` ← (default) - `true` |
| **world**  string  added in community.general 5.4.0 | Use a custom world file when checking for explicitly installed packages.  Default: `"/etc/apk/world"` |

## [Notes](apk_module.md#id3)

> **Note:**
>
> - *name* and *upgrade* are mutually exclusive.
> - When used with a `loop:` each package will be processed individually, it is much more efficient to pass the list directly to the *name* option.

## [Examples](apk_module.md#id4)

```yaml+jinja
- name: Update repositories and install foo package
  community.general.apk:
    name: foo
    update_cache: true

- name: Update repositories and install foo and bar packages
  community.general.apk:
    name: foo,bar
    update_cache: true

- name: Remove foo package
  community.general.apk:
    name: foo
    state: absent

- name: Remove foo and bar packages
  community.general.apk:
    name: foo,bar
    state: absent

- name: Install the package foo
  community.general.apk:
    name: foo
    state: present

- name: Install the packages foo and bar
  community.general.apk:
    name: foo,bar
    state: present

- name: Update repositories and update package foo to latest version
  community.general.apk:
    name: foo
    state: latest
    update_cache: true

- name: Update repositories and update packages foo and bar to latest versions
  community.general.apk:
    name: foo,bar
    state: latest
    update_cache: true

- name: Update all installed packages to the latest versions
  community.general.apk:
    upgrade: true

- name: Upgrade / replace / downgrade / uninstall all installed packages to the latest versions available
  community.general.apk:
    available: true
    upgrade: true

- name: Update repositories as a separate step
  community.general.apk:
    update_cache: true

- name: Install package from a specific repository
  community.general.apk:
    name: foo
    state: latest
    update_cache: true
    repository: http://dl-3.alpinelinux.org/alpine/edge/main

- name: Install package without using cache
  community.general.apk:
    name: foo
    state: latest
    no_cache: true

- name: Install package checking a custom world
  community.general.apk:
    name: foo
    state: latest
    world: /etc/apk/world.custom
```

## [Return Values](apk_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **packages**  list / elements=string | a list of packages that have been changed  Returned: when packages have changed  Sample: `["package", "other-package"]` |

### Authors

- Kevin Brebanov (@kbrebanov)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
