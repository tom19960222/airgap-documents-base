---
collection: ansible
version: "8"
title: "community.general.nictagadm module – Manage nic tags on SmartOS systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/nictagadm_module.html
fetched_at: 2026-07-28T01:48:08+00:00
---
# community.general.nictagadm module – Manage nic tags on SmartOS systems

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
> To use it in a playbook, specify: `community.general.nictagadm`.

- [Synopsis](nictagadm_module.md#synopsis)
- [Parameters](nictagadm_module.md#parameters)
- [Attributes](nictagadm_module.md#attributes)
- [Examples](nictagadm_module.md#examples)
- [Return Values](nictagadm_module.md#return-values)

## [Synopsis](nictagadm_module.md#id1)

- Create or delete nic tags on SmartOS systems.

Aliases: cloud.smartos.nictagadm

## [Parameters](nictagadm_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **etherstub**  boolean | Specifies that the nic tag will be attached to a created `etherstub`.  Parameter `etherstub` is mutually exclusive with both `mtu`, and `mac`.  **Choices:**   - `false` ← (default) - `true` |
| **force**  boolean | When `state=absent` this switch will use the `-f` parameter and delete the nic tag regardless of existing VMs.  **Choices:**   - `false` ← (default) - `true` |
| **mac**  string | Specifies the `mac` address to attach the nic tag to when not creating an `etherstub`.  Parameters `mac` and `etherstub` are mutually exclusive. |
| **mtu**  integer | Specifies the size of the `mtu` of the desired nic tag.  Parameters `mtu` and `etherstub` are mutually exclusive. |
| **name**  string / required | Name of the nic tag. |
| **state**  string | Create or delete a SmartOS nic tag.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Attributes](nictagadm_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](nictagadm_module.md#id4)

```yaml+jinja
- name: Create 'storage0' on '00:1b:21:a3:f5:4d'
  community.general.nictagadm:
    name: storage0
    mac: 00:1b:21:a3:f5:4d
    mtu: 9000
    state: present

- name: Remove 'storage0' nic tag
  community.general.nictagadm:
    name: storage0
    state: absent
```

## [Return Values](nictagadm_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **etherstub**  boolean | specifies if the nic tag will create and attach to an etherstub.  **Returned:** always  **Sample:** `false` |
| **force**  boolean | Shows if -f was used during the deletion of a nic tag  **Returned:** always  **Sample:** `false` |
| **mac**  string | MAC Address that the nic tag was attached to.  **Returned:** always  **Sample:** `"00:1b:21:a3:f5:4d"` |
| **mtu**  integer | specifies which MTU size was passed during the nictagadm add command. mtu and etherstub are mutually exclusive.  **Returned:** always  **Sample:** `1500` |
| **name**  string | nic tag name  **Returned:** always  **Sample:** `"storage0"` |
| **state**  string | state of the target  **Returned:** always  **Sample:** `"present"` |

### Authors

- Bruce Smith (@SmithX10)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
