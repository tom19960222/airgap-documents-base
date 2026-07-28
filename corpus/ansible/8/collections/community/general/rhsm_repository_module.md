---
collection: ansible
version: "8"
title: "community.general.rhsm_repository module – Manage RHSM repositories using the subscription-manager command"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/rhsm_repository_module.html
fetched_at: 2026-07-28T01:50:00+00:00
---
# community.general.rhsm_repository module – Manage RHSM repositories using the subscription-manager command

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
> see [Requirements](rhsm_repository_module.md#ansible-collections-community-general-rhsm-repository-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rhsm_repository`.

- [Synopsis](rhsm_repository_module.md#synopsis)
- [Requirements](rhsm_repository_module.md#requirements)
- [Parameters](rhsm_repository_module.md#parameters)
- [Attributes](rhsm_repository_module.md#attributes)
- [Notes](rhsm_repository_module.md#notes)
- [Examples](rhsm_repository_module.md#examples)
- [Return Values](rhsm_repository_module.md#return-values)

## [Synopsis](rhsm_repository_module.md#id1)

- Manage (Enable/Disable) RHSM repositories to the Red Hat Subscription Management entitlement platform using the `subscription-manager` command.

Aliases: packaging.os.rhsm_repository

## [Requirements](rhsm_repository_module.md#id2)

The below requirements are needed on the host that executes this module.

- subscription-manager

## [Parameters](rhsm_repository_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  list / elements=string / required | The ID of repositories to enable.  To operate on several repositories this can accept a comma separated list or a YAML list. |
| **purge**  boolean | Disable all currently enabled repositories that are not not specified in `name`. Only set this to `true` if passing in a list of repositories to the `name` field. Using this with `loop` will most likely not have the desired result.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | If state is equal to present or disabled, indicates the desired repository state.  Please note that `present` and `absent` are deprecated, and will be  removed in community.general 10.0.0; please use `enabled` and `disabled` instead.  **Choices:**   - `"present"` - `"enabled"` ← (default) - `"absent"` - `"disabled"` |

## [Attributes](rhsm_repository_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](rhsm_repository_module.md#id5)

> **Note:**
>
> - In order to manage RHSM repositories the system must be already registered to RHSM manually or using the Ansible [community.general.redhat_subscription](redhat_subscription_module.md#ansible-collections-community-general-redhat-subscription-module) module.
> - It is possible to interact with `subscription-manager` only as root, so root permissions are required to successfully run this module.

## [Examples](rhsm_repository_module.md#id6)

```yaml+jinja
- name: Enable a RHSM repository
  community.general.rhsm_repository:
    name: rhel-7-server-rpms

- name: Disable all RHSM repositories
  community.general.rhsm_repository:
    name: '*'
    state: disabled

- name: Enable all repositories starting with rhel-6-server
  community.general.rhsm_repository:
    name: rhel-6-server*
    state: enabled

- name: Disable all repositories except rhel-7-server-rpms
  community.general.rhsm_repository:
    name: rhel-7-server-rpms
    purge: true
```

## [Return Values](rhsm_repository_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **repositories**  list / elements=string | The list of RHSM repositories with their states.  When this module is used to change the repository states, this list contains the updated states after the changes.  **Returned:** success |

### Authors

- Giovanni Sciortino (@giovannisciortino)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
