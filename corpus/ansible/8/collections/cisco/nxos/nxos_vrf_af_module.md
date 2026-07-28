---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_vrf_af module – Manages VRF AF."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_vrf_af_module.html
fetched_at: 2026-07-28T01:39:21+00:00
---
# cisco.nxos.nxos_vrf_af module – Manages VRF AF.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_vrf_af`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_vrf_af_module.md#synopsis)
- [Parameters](nxos_vrf_af_module.md#parameters)
- [Notes](nxos_vrf_af_module.md#notes)
- [Examples](nxos_vrf_af_module.md#examples)
- [Return Values](nxos_vrf_af_module.md#return-values)

## [Synopsis](nxos_vrf_af_module.md#id1)

- Manages VRF AF

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: vrf_af

## [Parameters](nxos_vrf_af_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **afi**  string / required | Address-Family Identifier (AFI).  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **route_target_both_auto_evpn**  boolean | Enable/Disable the EVPN route-target ‘auto’ setting for both import and export target communities.  **Choices:**   - `false` - `true` |
| **route_targets**  list / elements=dictionary | Specify the route-targets which should be imported and/or exported under the AF. This argument accepts a list of dicts that specify the route-target, the direction (import|export|both) and state of each route-target. Default direction is `direction=both`. See examples. |
| **direction**  string | Indicates the direction of the route-target (import|export|both)  **Choices:**   - `"import"` - `"export"` - `"both"` ← (default) |
| **rt**  string / required | Defines the route-target itself |
| **state**  string | Determines whether the route-target with the given direction should be present or not on the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **state**  string | Determines whether the config should be present or not on the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vrf**  string / required | Name of the VRF. |

## [Notes](nxos_vrf_af_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - Default, where supported, restores params default value.
> - In case of `state=absent` the address-family configuration will be absent. Therefore the options `route_target_both_auto_evpn` and `route_targets` are ignored.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_vrf_af_module.md#id4)

```yaml+jinja
- cisco.nxos.nxos_vrf_af:
    vrf: ntc
    afi: ipv4
    route_target_both_auto_evpn: true
    state: present

- cisco.nxos.nxos_vrf_af:
    vrf: ntc
    afi: ipv4
    route_targets:
    - rt: 65000:1000
      direction: import
    - rt: 65001:1000
      direction: import

- cisco.nxos.nxos_vrf_af:
    vrf: ntc
    afi: ipv4
    route_targets:
    - rt: 65000:1000
      direction: import
    - rt: 65001:1000
      state: absent

- cisco.nxos.nxos_vrf_af:
    vrf: ntc
    afi: ipv4
    route_targets:
    - rt: 65000:1000
      direction: export
    - rt: 65001:1000
      direction: export

- cisco.nxos.nxos_vrf_af:
    vrf: ntc
    afi: ipv4
    route_targets:
    - rt: 65000:1000
      direction: export
      state: absent

- cisco.nxos.nxos_vrf_af:
    vrf: ntc
    afi: ipv4
    route_targets:
    - rt: 65000:1000
      direction: both
      state: present
    - rt: 65001:1000
      direction: import
      state: present
    - rt: 65002:1000
      direction: both
      state: absent
```

## [Return Values](nxos_vrf_af_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["vrf context ntc", "address-family ipv4 unicast"]` |

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
