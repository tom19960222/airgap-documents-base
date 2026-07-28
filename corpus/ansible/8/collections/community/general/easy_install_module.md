---
collection: ansible
version: "8"
title: "community.general.easy_install module – Installs Python libraries"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/easy_install_module.html
fetched_at: 2026-07-28T01:45:28+00:00
---
# community.general.easy_install module – Installs Python libraries

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](easy_install_module.md#ansible-collections-community-general-easy-install-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.easy_install`.

- [Synopsis](easy_install_module.md#synopsis)
- [Requirements](easy_install_module.md#requirements)
- [Parameters](easy_install_module.md#parameters)
- [Attributes](easy_install_module.md#attributes)
- [Notes](easy_install_module.md#notes)
- [Examples](easy_install_module.md#examples)

## [Synopsis](easy_install_module.md#id1)

- Installs Python libraries, optionally in a `virtualenv`

Aliases: packaging.language.easy_install

## [Requirements](easy_install_module.md#id2)

The below requirements are needed on the host that executes this module.

- virtualenv

## [Parameters](easy_install_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **executable**  string | The explicit executable or a pathname to the executable to be used to run easy_install for a specific version of Python installed in the system. For example `easy_install-3.3`, if there are both Python 2.7 and 3.3 installations in the system and you want to run easy_install for the Python 3.3 installation.  **Default:** `"easy_install"` |
| **name**  string / required | A Python library name. |
| **state**  string | The desired state of the library. `latest` ensures that the latest version is installed.  **Choices:**   - `"present"` ← (default) - `"latest"` |
| **virtualenv**  string | An optional `virtualenv` directory path to install into. If the `virtualenv` does not exist, it is created automatically. |
| **virtualenv_command**  string | The command to create the virtual environment with. For example `pyvenv`, `virtualenv`, `virtualenv2`.  **Default:** `"virtualenv"` |
| **virtualenv_site_packages**  boolean | Whether the virtual environment will inherit packages from the global site-packages directory. Note that if this setting is changed on an already existing virtual environment it will not have any effect, the environment must be deleted and newly created.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](easy_install_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](easy_install_module.md#id5)

> **Note:**
>
> - Please note that the `easy_install` module can only install Python libraries. Thus this module is not able to remove libraries. It is generally recommended to use the [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module) module which you can first install using [community.general.easy_install](easy_install_module.md#ansible-collections-community-general-easy-install-module).
> - Also note that `virtualenv` must be installed on the remote host if the `virtualenv` parameter is specified.

## [Examples](easy_install_module.md#id6)

```yaml+jinja
- name: Install or update pip
  community.general.easy_install:
    name: pip
    state: latest

- name: Install Bottle into the specified virtualenv
  community.general.easy_install:
    name: bottle
    virtualenv: /webapps/myapp/venv
```

### Authors

- Matt Wright (@mattupstate)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
