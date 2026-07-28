---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_vrf module – Manage the VRF definitions on Juniper JUNOS devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_vrf_module.html
fetched_at: 2026-07-28T02:40:01+00:00
---
# junipernetworks.junos.junos_vrf module – Manage the VRF definitions on Juniper JUNOS devices

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos/) (version 5.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_vrf_module.md#ansible-collections-junipernetworks-junos-junos-vrf-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_vrf`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_vrf_module.md#synopsis)
- [Requirements](junos_vrf_module.md#requirements)
- [Parameters](junos_vrf_module.md#parameters)
- [Notes](junos_vrf_module.md#notes)
- [Examples](junos_vrf_module.md#examples)
- [Return Values](junos_vrf_module.md#return-values)

## [Synopsis](junos_vrf_module.md#id1)

- This module provides declarative management of VRF definitions on Juniper JUNOS devices. It allows playbooks to manage individual or the entire VRF collection.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: vrf

## [Requirements](junos_vrf_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.5.2)

## [Parameters](junos_vrf_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | Specifies whether or not the configuration is active or deactivated  **Choices:**   - `false` - `true` ← (default) |
| **aggregate**  list / elements=dictionary | The set of VRF definition objects to be configured on the remote JUNOS device. Ths list entries can either be the VRF name or a hash of VRF definitions and attributes. This argument is mutually exclusive with the `name` argument. |
| **active**  boolean | Specifies whether or not the configuration is active or deactivated  **Choices:**   - `false` - `true` |
| **description**  string | Provides a short description of the VRF definition in the current active configuration. The VRF definition value accepts alphanumeric characters used to provide additional information about the VRF. |
| **interfaces**  list / elements=string | Identifies the set of interfaces that should be configured in the VRF. Interfaces must be routed interfaces in order to be placed into a VRF. |
| **name**  string / required | The name of the VRF definition to be managed on the remote IOS device. The VRF definition name is an ASCII string name used to uniquely identify the VRF. This argument is mutually exclusive with the `aggregate` argument |
| **rd**  list / elements=string | The router-distinguisher value uniquely identifies the VRF to routing processes on the remote IOS system. The RD value takes the form of `A:B` where `A` and `B` are both numeric values. |
| **state**  string | Configures the state of the VRF definition as it relates to the device operational configuration. When set to *present*, the VRF should be configured in the device active configuration and when set to *absent* the VRF should not be in the device active configuration  **Choices:**   - `"present"` - `"absent"` |
| **table_label**  boolean | Causes JUNOS to allocate a VPN label per VRF rather than per VPN FEC. This allows for forwarding of traffic to directly connected subnets, COS Egress filtering etc.  **Choices:**   - `false` - `true` |
| **target**  list / elements=string | It configures VRF target community configuration. The target value takes the form of `target:A:B` where `A` and `B` are both numeric values. |
| **description**  string | Provides a short description of the VRF definition in the current active configuration. The VRF definition value accepts alphanumeric characters used to provide additional information about the VRF. |
| **interfaces**  list / elements=string | Identifies the set of interfaces that should be configured in the VRF. Interfaces must be routed interfaces in order to be placed into a VRF. |
| **name**  string | The name of the VRF definition to be managed on the remote IOS device. The VRF definition name is an ASCII string name used to uniquely identify the VRF. This argument is mutually exclusive with the `aggregate` argument |
| **rd**  list / elements=string | The router-distinguisher value uniquely identifies the VRF to routing processes on the remote IOS system. The RD value takes the form of `A:B` where `A` and `B` are both numeric values. |
| **state**  string | Configures the state of the VRF definition as it relates to the device operational configuration. When set to *present*, the VRF should be configured in the device active configuration and when set to *absent* the VRF should not be in the device active configuration  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **table_label**  boolean | Causes JUNOS to allocate a VPN label per VRF rather than per VPN FEC. This allows for forwarding of traffic to directly connected subnets, COS Egress filtering etc.  **Choices:**   - `false` - `true` ← (default) |
| **target**  list / elements=string | It configures VRF target community configuration. The target value takes the form of `target:A:B` where `A` and `B` are both numeric values. |

## [Notes](junos_vrf_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
> - Recommended connection is `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - This module also works with `local` connections for legacy playbooks.
> - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Juniper network devices see <https://www.ansible.com/ansible-juniper>.

## [Examples](junos_vrf_module.md#id5)

```yaml+jinja
- name: Configure vrf configuration
  junipernetworks.junos.junos_vrf:
    name: test-1
    description: test-vrf-1
    interfaces:
      - ge-0/0/3
      - ge-0/0/2
    rd: 192.0.2.1:10
    target: target:65514:113
    state: present

- name: Remove vrf configuration
  junipernetworks.junos.junos_vrf:
    name: test-1
    description: test-vrf-1
    interfaces:
      - ge-0/0/3
      - ge-0/0/2
    rd: 192.0.2.1:10
    target: target:65514:113
    state: absent

- name: Deactivate vrf configuration
  junipernetworks.junos.junos_vrf:
    name: test-1
    description: test-vrf-1
    interfaces:
      - ge-0/0/3
      - ge-0/0/2
    rd: 192.0.2.1:10
    target: target:65514:113
    active: false

- name: Activate vrf configuration
  junipernetworks.junos.junos_vrf:
    name: test-1
    description: test-vrf-1
    interfaces:
      - ge-0/0/3
      - ge-0/0/2
    rd: 192.0.2.1:10
    target: target:65514:113
    active: true

- name: Create vrf using aggregate
  junipernetworks.junos.junos_vrf:
    aggregate:
      - name: test-1
        description: test-vrf-1
        interfaces:
          - ge-0/0/3 - ge-0/0/2
        rd: 192.0.2.1:10
        target: target:65514:113
      - name: test-2
        description: test-vrf-2
        interfaces:
          - ge-0/0/4
          - ge-0/0/5
        rd: 192.0.2.2:10
        target: target:65515:114
  state: present
```

## [Return Values](junos_vrf_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff.prepared**  string | Configuration difference before and after applying change.  **Returned:** when configuration is changed and diff option is enabled.  **Sample:** `"[edit routing-instances] +   test-1 { +       description test-vrf-1; +       instance-type vrf; +       interface ge-0/0/2.0; +       interface ge-0/0/3.0; +       route-distinguisher 192.0.2.1:10; +       vrf-target target:65514:113; +   }\n"` |

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
