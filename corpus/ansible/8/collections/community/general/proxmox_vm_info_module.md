---
collection: ansible
version: "8"
title: "community.general.proxmox_vm_info module – Retrieve information about one or more Proxmox VE virtual machines"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/proxmox_vm_info_module.html
fetched_at: 2026-07-28T01:49:25+00:00
---
# community.general.proxmox_vm_info module – Retrieve information about one or more Proxmox VE virtual machines

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
> see [Requirements](proxmox_vm_info_module.md#ansible-collections-community-general-proxmox-vm-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.proxmox_vm_info`.

New in community.general 7.2.0

- [Synopsis](proxmox_vm_info_module.md#synopsis)
- [Requirements](proxmox_vm_info_module.md#requirements)
- [Parameters](proxmox_vm_info_module.md#parameters)
- [Attributes](proxmox_vm_info_module.md#attributes)
- [Examples](proxmox_vm_info_module.md#examples)
- [Return Values](proxmox_vm_info_module.md#return-values)

## [Synopsis](proxmox_vm_info_module.md#id1)

- Retrieve information about one or more Proxmox VE virtual machines.

## [Requirements](proxmox_vm_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- proxmoxer
- requests

## [Parameters](proxmox_vm_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_host**  string / required | Specify the target host of the Proxmox VE cluster. |
| **api_password**  string | Specify the password to authenticate with.  You can use [`PROXMOX_PASSWORD`](../../environment_variables.md#envvar-PROXMOX_PASSWORD) environment variable. |
| **api_token_id**  string  *added in community.general 1.3.0* | Specify the token ID.  Requires `proxmoxer>=1.1.0` to work. |
| **api_token_secret**  string  *added in community.general 1.3.0* | Specify the token secret.  Requires `proxmoxer>=1.1.0` to work. |
| **api_user**  string / required | Specify the user to authenticate with. |
| **name**  string | Restrict results to a specific virtual machine(s) by using their name.  If VM(s) with the specified name do not exist in a cluster then the resulting list will be empty. |
| **node**  string | Restrict results to a specific Proxmox VE node. |
| **type**  string | Restrict results to a specific virtual machine(s) type.  **Choices:**   - `"all"` ← (default) - `"qemu"` - `"lxc"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` ← (default) - `true` |
| **vmid**  integer | Restrict results to a specific virtual machine by using its ID.  If VM with the specified vmid does not exist in a cluster then resulting list will be empty. |

## [Attributes](proxmox_vm_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](proxmox_vm_info_module.md#id5)

```yaml+jinja
- name: List all existing virtual machines on node
  community.general.proxmox_vm_info:
    api_host: proxmoxhost
    api_user: root@pam
    api_token_id: '{{ token_id | default(omit) }}'
    api_token_secret: '{{ token_secret | default(omit) }}'
    node: node01

- name: List all QEMU virtual machines on node
  community.general.proxmox_vm_info:
    api_host: proxmoxhost
    api_user: root@pam
    api_password: '{{ password | default(omit) }}'
    node: node01
    type: qemu

- name: Retrieve information about specific VM by ID
  community.general.proxmox_vm_info:
    api_host: proxmoxhost
    api_user: root@pam
    api_password: '{{ password | default(omit) }}'
    node: node01
    type: qemu
    vmid: 101

- name: Retrieve information about specific VM by name
  community.general.proxmox_vm_info:
    api_host: proxmoxhost
    api_user: root@pam
    api_password: '{{ password | default(omit) }}'
    node: node01
    type: lxc
    name: lxc05.home.arpa
```

## [Return Values](proxmox_vm_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **proxmox_vms**  list / elements=dictionary | List of virtual machines.  **Returned:** on success  **Sample:** `[{"cpu": 0.258944410905281, "cpus": 1, "disk": 0, "diskread": 0, "diskwrite": 0, "id": "qemu/100", "maxcpu": 1, "maxdisk": 34359738368, "maxmem": 4294967296, "mem": 35158379, "name": "pxe.home.arpa", "netin": 99715803, "netout": 14237835, "node": "pve", "pid": 1947197, "status": "running", "template": false, "type": "qemu", "uptime": 135530, "vmid": 100}, {"cpu": 0, "cpus": 1, "disk": 0, "diskread": 0, "diskwrite": 0, "id": "qemu/101", "maxcpu": 1, "maxdisk": 0, "maxmem": 536870912, "mem": 0, "name": "test1", "netin": 0, "netout": 0, "node": "pve", "status": "stopped", "template": false, "type": "qemu", "uptime": 0, "vmid": 101}]` |

### Authors

- Sergei Antipov (@UnderGreen) <greendayonfire at gmail dot com>

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
