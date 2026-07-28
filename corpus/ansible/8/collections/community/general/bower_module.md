---
collection: ansible
version: "8"
title: "community.general.bower module – Manage bower packages with bower"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/bower_module.html
fetched_at: 2026-07-28T01:44:51+00:00
---
# community.general.bower module – Manage bower packages with bower

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.bower`.

- [Synopsis](bower_module.md#synopsis)
- [Parameters](bower_module.md#parameters)
- [Attributes](bower_module.md#attributes)
- [Examples](bower_module.md#examples)

## [Synopsis](bower_module.md#id1)

- Manage bower packages with bower

Aliases: packaging.language.bower

## [Parameters](bower_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string | The name of a bower package to install |
| **offline**  boolean | Install packages from local cache, if the packages were installed before  **Choices:**   - `false` ← (default) - `true` |
| **path**  path / required | The base path where to install the bower packages |
| **production**  boolean | Install with –production flag  **Choices:**   - `false` ← (default) - `true` |
| **relative_execpath**  path | Relative path to bower executable from install path |
| **state**  string | The state of the bower package  **Choices:**   - `"present"` ← (default) - `"absent"` - `"latest"` |
| **version**  string | The version to be installed |

## [Attributes](bower_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](bower_module.md#id4)

```yaml+jinja
- name: Install "bootstrap" bower package.
  community.general.bower:
    name: bootstrap

- name: Install "bootstrap" bower package on version 3.1.1.
  community.general.bower:
    name: bootstrap
    version: '3.1.1'

- name: Remove the "bootstrap" bower package.
  community.general.bower:
    name: bootstrap
    state: absent

- name: Install packages based on bower.json.
  community.general.bower:
    path: /app/location

- name: Update packages based on bower.json to their latest version.
  community.general.bower:
    path: /app/location
    state: latest

# install bower locally and run from there
- npm:
    path: /app/location
    name: bower
    global: false
- community.general.bower:
    path: /app/location
    relative_execpath: node_modules/.bin
```

### Authors

- Michael Warkentin (@mwarkentin)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
