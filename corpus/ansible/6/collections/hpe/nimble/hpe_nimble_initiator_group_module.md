---
collection: ansible
version: "6"
title: "hpe.nimble.hpe_nimble_initiator_group module – Manage the HPE Nimble Storage initiator groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/hpe/nimble/hpe_nimble_initiator_group_module.html
fetched_at: 2026-07-27T17:50:02+00:00
---
# hpe.nimble.hpe_nimble_initiator_group module – Manage the HPE Nimble Storage initiator groups

> **Note:**
>
> This module is part of the [hpe.nimble collection](https://galaxy.ansible.com/hpe/nimble) (version 1.1.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hpe.nimble`.
> You need further requirements to be able to use this module,
> see [Requirements](hpe_nimble_initiator_group_module.md#ansible-collections-hpe-nimble-hpe-nimble-initiator-group-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_initiator_group`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_initiator_group_module.md#synopsis)
- [Requirements](hpe_nimble_initiator_group_module.md#requirements)
- [Parameters](hpe_nimble_initiator_group_module.md#parameters)
- [Notes](hpe_nimble_initiator_group_module.md#notes)
- [Examples](hpe_nimble_initiator_group_module.md#examples)

## [Synopsis](hpe_nimble_initiator_group_module.md#id1)

- Manage the HPE Nimble Storage initiator groups.

## [Requirements](hpe_nimble_initiator_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_initiator_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_protocol**  string | Initiator group access protocol.  Choices:   - `"iscsi"` - `"fc"` |
| **app_uuid**  string | Application identifier of initiator group. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed. |
| **change_name**  string | Change name of the existing initiator group. |
| **description**  string | Text description of initiator group. |
| **fc_initiators**  list / elements=dictionary | List of FC initiators. When create/update fc_initiators, WWPN is required. |
| **fc_tdz_ports**  list / elements=integer | List of target fibre channel ports with target driven zoning configured on this initiator group. |
| **host**  string / required | HPE Nimble Storage IP address. |
| **host_type**  string | Initiator group host type. Available options are auto and hpux. The default option is auto. This attribute will be applied to all the initiators in the initiator group. Initiators with different host OSes should not be kept in the same initiator group having a non-default host type attribute. |
| **iscsi_initiators**  list / elements=dictionary | List of iSCSI initiators. When create/update iscsi_initiators, either iqn or ip_address is always required with label. |
| **metadata**  dictionary | Key-value pairs that augment an initiator group’s attributes. List of key-value pairs. Keys must be unique and non-empty. |
| **name**  string / required | Name of the initiator group. |
| **password**  string / required | HPE Nimble Storage password. |
| **state**  string / required | The initiator group operation.  Choices:   - `"present"` - `"absent"` - `"create"` |
| **target_subnets**  list / elements=dictionary | List of target subnet labels. If specified, discovery and access to volumes will be restricted to the specified subnets. |
| **username**  string / required | HPE Nimble Storage user name. |

## [Notes](hpe_nimble_initiator_group_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_initiator_group_module.md#id5)

```yaml+jinja
# if state is create, then create ig. Fails if already present.
# if state is present, then create ig if not present. Succeeds if it already exists.
- name: Create an igroup
  hpe.nimble.hpe_nimble_initiator_group:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    access_protocol: "{{ access_protocol | default('iscsi')}}"
    name: "{{ name }}"
    iscsi_initiators: "{{ iscsi_initiators | default([])}}"  # list of dictionaries. Each entry in the dictionary has one initiator details.
    description: "{{ description | default(None) }}"
    state: "{{ state | default('present') }}"

- name: Delete igroup
  hpe.nimble.hpe_nimble_initiator_group:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    access_protocol: "{{ access_protocol | default('iscsi')}}"
    name: "{{ name }}"
    state: absent
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

[Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
[Homepage](http://hpe.com/storage/nimble)
[Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
