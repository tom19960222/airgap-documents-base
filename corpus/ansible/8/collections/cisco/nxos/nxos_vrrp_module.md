---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_vrrp module – Manages VRRP configuration on NX-OS switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_vrrp_module.html
fetched_at: 2026-07-28T01:39:22+00:00
---
# cisco.nxos.nxos_vrrp module – Manages VRRP configuration on NX-OS switches.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_vrrp`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_vrrp_module.md#synopsis)
- [Parameters](nxos_vrrp_module.md#parameters)
- [Notes](nxos_vrrp_module.md#notes)
- [Examples](nxos_vrrp_module.md#examples)
- [Return Values](nxos_vrrp_module.md#return-values)

## [Synopsis](nxos_vrrp_module.md#id1)

- Manages VRRP configuration on NX-OS switches.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: vrrp

## [Parameters](nxos_vrrp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **admin_state**  string | Used to enable or disable the VRRP process.  **Choices:**   - `"shutdown"` ← (default) - `"no shutdown"` - `"default"` |
| **authentication**  string | Clear text authentication string or ‘default’ keyword |
| **group**  string / required | VRRP group number. |
| **interface**  string / required | Full name of interface that is being managed for VRRP. |
| **interval**  string | Time interval between advertisement or ‘default’ keyword |
| **preempt**  boolean | Enable/Disable preempt.  **Choices:**   - `false` - `true` |
| **priority**  string | VRRP priority or ‘default’ keyword |
| **state**  string | Specify desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vip**  string | VRRP virtual IP address or ‘default’ keyword |

## [Notes](nxos_vrrp_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - VRRP feature needs to be enabled first on the system.
> - SVIs must exist before using this module.
> - Interface must be a L3 port before using this module.
> - `state=absent` removes the VRRP group if it exists on the device.
> - VRRP cannot be configured on loopback interfaces.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_vrrp_module.md#id4)

```yaml+jinja
- name: Ensure vrrp group 100 and vip 10.1.100.1 is on vlan10
  cisco.nxos.nxos_vrrp:
    interface: vlan10
    group: 100
    vip: 10.1.100.1

- name: Ensure removal of the vrrp group config
  cisco.nxos.nxos_vrrp:
    interface: vlan10
    group: 100
    vip: 10.1.100.1
    state: absent

- name: Re-config with more params
  cisco.nxos.nxos_vrrp:
    interface: vlan10
    group: 100
    vip: 10.1.100.1
    preempt: false
    priority: 130
    authentication: AUTHKEY
```

## [Return Values](nxos_vrrp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["interface vlan10", "vrrp 150", "address 10.1.15.1", "authentication text testing", "no shutdown"]` |

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
