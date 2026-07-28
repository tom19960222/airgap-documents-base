---
collection: ansible
version: "8"
title: "hpe.nimble.hpe_nimble_network module – Manage the HPE Nimble Storage network configuration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/hpe/nimble/hpe_nimble_network_module.html
fetched_at: 2026-07-28T02:34:23+00:00
---
# hpe.nimble.hpe_nimble_network module – Manage the HPE Nimble Storage network configuration

> **Note:**
>
> This module is part of the [hpe.nimble collection](https://galaxy.ansible.com/ui/repo/published/hpe/nimble/) (version 1.1.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hpe.nimble`.
> You need further requirements to be able to use this module,
> see [Requirements](hpe_nimble_network_module.md#ansible-collections-hpe-nimble-hpe-nimble-network-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_network`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_network_module.md#synopsis)
- [Requirements](hpe_nimble_network_module.md#requirements)
- [Parameters](hpe_nimble_network_module.md#parameters)
- [Notes](hpe_nimble_network_module.md#notes)
- [Examples](hpe_nimble_network_module.md#examples)

## [Synopsis](hpe_nimble_network_module.md#id1)

- Manage the storage network configuration on the HPE Nimble Storage group.

## [Requirements](hpe_nimble_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **activate**  boolean | Activate a network configuration.  **Choices:**   - `false` - `true` |
| **array**  list / elements=dictionary | List of array network configs. |
| **change_name**  string | Change name of the existing network config. |
| **host**  string / required | HPE Nimble Storage IP address. |
| **ignore_validation_mask**  integer | Indicates whether to ignore the validation. |
| **iscsi_automatic_connection_method**  boolean | Whether automatic connection method is enabled. Enabling this means means redirecting connections from the specified iSCSI discovery IP address to the best data IP address based on connection counts.  **Choices:**   - `false` - `true` |
| **iscsi_connection_rebalancing**  boolean | Whether rebalancing is enabled. Enabling this means rebalancing iSCSI connections by periodically breaking existing connections that are out-of-balance, allowing the host to reconnect to a more appropriate data IP address.  **Choices:**   - `false` - `true` |
| **mgmt_ip**  string | Management IP address for the Group. Four numbers in the range (0,255) separated by periods. |
| **name**  string / required | Name of the network configuration. Use the name ‘draft’ when creating a draft configuration.  **Choices:**   - `"active"` - `"backup"` - `"draft"` |
| **password**  string / required | HPE Nimble Storage password. |
| **route**  list / elements=dictionary | List of static routes. |
| **secondary_mgmt_ip**  string | Secondary management IP address for the Group. Four numbers in the range [0,255] separated by periods. |
| **state**  string / required | The network config operation.  **Choices:**   - `"create"` - `"present"` - `"absent"` |
| **subnet**  list / elements=dictionary | List of subnet configs. |
| **username**  string / required | HPE Nimble Storage user name. |
| **validate**  boolean | Validate a network configuration.  **Choices:**   - `false` - `true` |

## [Notes](hpe_nimble_network_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_network_module.md#id5)

```yaml+jinja
# if state is create, then create network config, fails if it exist or cannot create
# if state is present, then create network config if not present ,else success
- name: Create network config
  hpe.nimble.hpe_nimble_network:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    route: "{{ route }}"
    subnet: "{{ subnet }}"
    array: "{{ array }}"
    iscsi_automatic_connection_method: true
    iscsi_connection_rebalancing: False
    mgmt_ip: "{{ mgmt_ip }}"
    state: "{{ state | default('present') }}"

- name: Delete network config
  hpe.nimble.hpe_nimble_network:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: "absent"

- name: Validate network config
  hpe.nimble.hpe_nimble_network:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: "present"
    ignore_validation_mask: 1
    validate: true

- name: Activate Network config
  hpe.nimble.hpe_nimble_network:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: "present"
    ignore_validation_mask: 1
    activate: true
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

- [Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
- [Homepage](http://hpe.com/storage/nimble)
- [Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
