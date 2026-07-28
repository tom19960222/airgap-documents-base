---
collection: ansible
version: "8"
title: "community.general.proxmox_nic module – Management of a NIC of a Qemu(KVM) VM in a Proxmox VE cluster"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/proxmox_nic_module.html
fetched_at: 2026-07-28T01:49:20+00:00
---
# community.general.proxmox_nic module – Management of a NIC of a Qemu(KVM) VM in a Proxmox VE cluster

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
> see [Requirements](proxmox_nic_module.md#ansible-collections-community-general-proxmox-nic-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.proxmox_nic`.

New in community.general 3.1.0

- [Synopsis](proxmox_nic_module.md#synopsis)
- [Requirements](proxmox_nic_module.md#requirements)
- [Parameters](proxmox_nic_module.md#parameters)
- [Attributes](proxmox_nic_module.md#attributes)
- [Examples](proxmox_nic_module.md#examples)
- [Return Values](proxmox_nic_module.md#return-values)

## [Synopsis](proxmox_nic_module.md#id1)

- Allows you to create/update/delete a NIC on Qemu(KVM) Virtual Machines in a Proxmox VE cluster.

Aliases: cloud.misc.proxmox_nic

## [Requirements](proxmox_nic_module.md#id2)

The below requirements are needed on the host that executes this module.

- proxmoxer
- requests

## [Parameters](proxmox_nic_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_host**  string / required | Specify the target host of the Proxmox VE cluster. |
| **api_password**  string | Specify the password to authenticate with.  You can use [`PROXMOX_PASSWORD`](../../environment_variables.md#envvar-PROXMOX_PASSWORD) environment variable. |
| **api_token_id**  string  *added in community.general 1.3.0* | Specify the token ID.  Requires `proxmoxer>=1.1.0` to work. |
| **api_token_secret**  string  *added in community.general 1.3.0* | Specify the token secret.  Requires `proxmoxer>=1.1.0` to work. |
| **api_user**  string / required | Specify the user to authenticate with. |
| **bridge**  string | Add this interface to the specified bridge device. The Proxmox VE default bridge is called `vmbr0`. |
| **firewall**  boolean | Whether this interface should be protected by the firewall.  **Choices:**   - `false` ← (default) - `true` |
| **interface**  string / required | Name of the interface, should be `net[n]` where `1 ≤ n ≤ 31`. |
| **link_down**  boolean | Whether this interface should be disconnected (like pulling the plug).  **Choices:**   - `false` ← (default) - `true` |
| **mac**  string | `XX:XX:XX:XX:XX:XX` should be a unique MAC address. This is automatically generated if not specified.  When not specified this module will keep the MAC address the same when changing an existing interface. |
| **model**  string | The NIC emulator model.  **Choices:**   - `"e1000"` - `"e1000-82540em"` - `"e1000-82544gc"` - `"e1000-82545em"` - `"i82551"` - `"i82557b"` - `"i82559er"` - `"ne2k_isa"` - `"ne2k_pci"` - `"pcnet"` - `"rtl8139"` - `"virtio"` ← (default) - `"vmxnet3"` |
| **mtu**  integer | Force MTU, for `virtio` model only, setting will be ignored otherwise.  Set to `1` to use the bridge MTU.  Value should be `1 ≤ n ≤ 65520`. |
| **name**  string | Specifies the VM name. Only used on the configuration web interface.  Required only for `state=present`. |
| **queues**  integer | Number of packet queues to be used on the device.  Value should be `0 ≤ n ≤ 16`. |
| **rate**  float | Rate limit in MBps (MegaBytes per second) as floating point number. |
| **state**  string | Indicates desired state of the NIC.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tag**  integer | VLAN tag to apply to packets on this interface.  Value should be `1 ≤ n ≤ 4094`. |
| **trunks**  list / elements=integer | List of VLAN trunks to pass through this interface. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` ← (default) - `true` |
| **vmid**  integer | Specifies the instance ID. |

## [Attributes](proxmox_nic_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](proxmox_nic_module.md#id5)

```yaml+jinja
- name: Create NIC net0 targeting the vm by name
  community.general.proxmox_nic:
    api_user: root@pam
    api_password: secret
    api_host: proxmoxhost
    name: my_vm
    interface: net0
    bridge: vmbr0
    tag: 3

- name: Create NIC net0 targeting the vm by id
  community.general.proxmox_nic:
    api_user: root@pam
    api_password: secret
    api_host: proxmoxhost
    vmid: 103
    interface: net0
    bridge: vmbr0
    mac: "12:34:56:C0:FF:EE"
    firewall: true

- name: Delete NIC net0 targeting the vm by name
  community.general.proxmox_nic:
    api_user: root@pam
    api_password: secret
    api_host: proxmoxhost
    name: my_vm
    interface: net0
    state: absent
```

## [Return Values](proxmox_nic_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | A short message  **Returned:** always  **Sample:** `"Nic net0 unchanged on VM with vmid 103"` |
| **vmid**  integer | The VM vmid.  **Returned:** success  **Sample:** `115` |

### Authors

- Lammert Hellinga (@Kogelvis)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
