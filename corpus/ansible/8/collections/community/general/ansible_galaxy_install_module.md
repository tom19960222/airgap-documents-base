---
collection: ansible
version: "8"
title: "community.general.ansible_galaxy_install module – Install Ansible roles or collections using ansible-galaxy"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ansible_galaxy_install_module.html
fetched_at: 2026-07-28T01:44:38+00:00
---
# community.general.ansible_galaxy_install module – Install Ansible roles or collections using ansible-galaxy

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
> see [Requirements](ansible_galaxy_install_module.md#ansible-collections-community-general-ansible-galaxy-install-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ansible_galaxy_install`.

New in community.general 3.5.0

- [Synopsis](ansible_galaxy_install_module.md#synopsis)
- [Requirements](ansible_galaxy_install_module.md#requirements)
- [Parameters](ansible_galaxy_install_module.md#parameters)
- [Attributes](ansible_galaxy_install_module.md#attributes)
- [Notes](ansible_galaxy_install_module.md#notes)
- [Examples](ansible_galaxy_install_module.md#examples)
- [Return Values](ansible_galaxy_install_module.md#return-values)

## [Synopsis](ansible_galaxy_install_module.md#id1)

- This module allows the installation of Ansible collections or roles using `ansible-galaxy`.

Aliases: packaging.language.ansible_galaxy_install

## [Requirements](ansible_galaxy_install_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9, ansible-base 2.10, or ansible-core 2.11 or newer

## [Parameters](ansible_galaxy_install_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ack_ansible29**  boolean | Acknowledge using Ansible 2.9 with its limitations, and prevents the module from generating warnings about them.  This option is completely ignored if using a version of Ansible greater than `2.9.x`.  Note that this option will be removed without any further deprecation warning once support for Ansible 2.9 is removed from this module.  **Choices:**   - `false` ← (default) - `true` |
| **ack_min_ansiblecore211**  boolean | Acknowledge the module is deprecating support for Ansible 2.9 and ansible-base 2.10.  Support for those versions will be removed in community.general 8.0.0. At the same time, this option will be removed without any deprecation warning!  This option is completely ignored if using a version of ansible-core/ansible-base/Ansible greater than `2.11`.  For the sake of conciseness, setting this parameter to `true` implies `ack_ansible29=true`.  **Choices:**   - `false` ← (default) - `true` |
| **dest**  path | The path to the directory containing your collections or roles, according to the value of `type`.  Please notice that `ansible-galaxy` will not install collections with `type=both`, when `requirements_file` contains both roles and collections and `dest` is specified. |
| **force**  boolean | Force overwriting an existing role or collection.  Using `force=true` is mandatory when downgrading.  **Ansible 2.9 and 2.10**: Must be `true` to upgrade roles and collections.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | Name of the collection or role being installed.  Versions can be specified with `ansible-galaxy` usual formats. For example, the collection `community.docker:1.6.1` or the role `ansistrano.deploy,3.8.0`.  `name` and `requirements_file` are mutually exclusive. |
| **no_deps**  boolean  *added in community.general 4.5.0* | Refrain from installing dependencies.  **Choices:**   - `false` ← (default) - `true` |
| **requirements_file**  path | Path to a file containing a list of requirements to be installed.  It works for `type` equals to `collection` and `role`.  `name` and `requirements_file` are mutually exclusive.  **Ansible 2.9**: It can only be used to install either `type=role` or `type=collection`, but not both at the same run. |
| **type**  string / required | The type of installation performed by `ansible-galaxy`.  If `type=both`, then `requirements_file` must be passed and it may contain both roles and collections.  Note however that the opposite is not true: if using a `requirements_file`, then `type` can be any of the three choices.  **Ansible 2.9**: The option `both` will have the same effect as `role`.  **Choices:**   - `"collection"` - `"role"` - `"both"` |

## [Attributes](ansible_galaxy_install_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](ansible_galaxy_install_module.md#id5)

> **Note:**
>
> - **Ansible 2.9/2.10**: The `ansible-galaxy` command changed significantly between Ansible 2.9 and ansible-base 2.10 (later ansible-core 2.11). See comments in the parameters.
> - The module will try and run using the `C.UTF-8` locale. If that fails, it will try `en_US.UTF-8`. If that one also fails, the module will fail.

## [Examples](ansible_galaxy_install_module.md#id6)

```yaml+jinja
- name: Install collection community.network
  community.general.ansible_galaxy_install:
    type: collection
    name: community.network

- name: Install role at specific path
  community.general.ansible_galaxy_install:
    type: role
    name: ansistrano.deploy
    dest: /ansible/roles

- name: Install collections and roles together
  community.general.ansible_galaxy_install:
    type: both
    requirements_file: requirements.yml

- name: Force-install collection community.network at specific version
  community.general.ansible_galaxy_install:
    type: collection
    name: community.network:3.0.2
    force: true
```

## [Return Values](ansible_galaxy_install_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dest**  string | The value of the `dest` parameter.  **Returned:** always |
| **force**  boolean | The value of the `force` parameter.  **Returned:** always |
| **installed_collections**  dictionary | If `requirements_file` is specified instead, returns dictionary with all the collections installed per path.  If `name` is specified, returns that collection name and the version installed per path.  **Ansible 2.9**: Returns empty because `ansible-galaxy` has no `list` subcommand.  **Returned:** always when installing collections  **Sample:** `{"/custom/ansible/ansible_collections": {"community.general": "3.1.0"}, "/home/az/.ansible/collections/ansible_collections": {"community.docker": "1.6.0", "community.general": "3.0.2"}}` |
| **<path>**  dictionary | Collections and versions for that path  **Returned:** success |
| **installed_roles**  dictionary | If `requirements_file` is specified instead, returns dictionary with all the roles installed per path.  If `name` is specified, returns that role name and the version installed per path.  **Ansible 2.9**: Returns empty because `ansible-galaxy` has no `list` subcommand.  **Returned:** always when installing roles  **Sample:** `{"/custom/ansible/roles": {"ansistrano.deploy": "3.8.0"}, "/home/user42/.ansible/roles": {"ansistrano.deploy": "3.9.0", "baztian.xfce": "v0.0.3"}}` |
| **<path>**  dictionary | Roles and versions for that path.  **Returned:** success |
| **name**  string | The value of the `name` parameter.  **Returned:** always |
| **new_collections**  dictionary | New collections installed by this module.  **Returned:** success  **Sample:** `{"community.docker": "1.6.1", "community.general": "3.1.0"}` |
| **new_roles**  dictionary | New roles installed by this module.  **Returned:** success  **Sample:** `{"ansistrano.deploy": "3.8.0", "baztian.xfce": "v0.0.3"}` |
| **requirements_file**  string | The value of the `requirements_file` parameter.  **Returned:** always |
| **type**  string | The value of the `type` parameter.  **Returned:** always |

### Authors

- Alexei Znamensky (@russoz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
