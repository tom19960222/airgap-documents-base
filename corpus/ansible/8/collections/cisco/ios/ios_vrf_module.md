---
collection: ansible
version: "8"
title: "cisco.ios.ios_vrf module – Module to configure VRF definitions."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_vrf_module.html
fetched_at: 2026-07-28T01:26:31+00:00
---
# cisco.ios.ios_vrf module – Module to configure VRF definitions.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/ui/repo/published/cisco/ios/) (version 4.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_vrf`.

New in cisco.ios 1.0.0

- [Synopsis](ios_vrf_module.md#synopsis)
- [Parameters](ios_vrf_module.md#parameters)
- [Notes](ios_vrf_module.md#notes)
- [Examples](ios_vrf_module.md#examples)
- [Return Values](ios_vrf_module.md#return-values)

## [Synopsis](ios_vrf_module.md#id1)

- This module provides declarative management of VRF definitions on Cisco IOS devices. It allows playbooks to manage individual or the entire VRF collection. It also supports purging VRF definitions from the configuration that are not explicitly defined.

Aliases: vrf

## [Parameters](ios_vrf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **associated_interfaces**  list / elements=string | This is a intent option and checks the operational state of the for given vrf `name` for associated interfaces. If the value in the `associated_interfaces` does not match with the operational state of vrf interfaces on device it will result in failure. |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device.  **Default:** `10` |
| **description**  string | Provides a short description of the VRF definition in the current active configuration. The VRF definition value accepts alphanumeric characters used to provide additional information about the VRF. |
| **interfaces**  list / elements=string | Identifies the set of interfaces that should be configured in the VRF. Interfaces must be routed interfaces in order to be placed into a VRF. |
| **name**  string | The name of the VRF definition to be managed on the remote IOS device. The VRF definition name is an ASCII string name used to uniquely identify the VRF. This argument is mutually exclusive with the `vrfs` argument |
| **purge**  boolean | Instructs the module to consider the VRF definition absolute. It will remove any previously configured VRFs on the device.  **Choices:**   - `false` ← (default) - `true` |
| **rd**  string | The router-distinguisher value uniquely identifies the VRF to routing processes on the remote IOS system. The RD value takes the form of `A:B` where `A` and `B` are both numeric values. |
| **route_both**  list / elements=string | Adds an export and import list of extended route target communities to the VRF. |
| **route_both_ipv4**  list / elements=string | Adds an export and import list of extended route target communities in address-family configuration submode to the VRF. |
| **route_both_ipv6**  list / elements=string | Adds an export and import list of extended route target communities in address-family configuration submode to the VRF. |
| **route_export**  list / elements=string | Adds an export list of extended route target communities to the VRF. |
| **route_export_ipv4**  list / elements=string | Adds an export list of extended route target communities in address-family configuration submode to the VRF. |
| **route_export_ipv6**  list / elements=string | Adds an export list of extended route target communities in address-family configuration submode to the VRF. |
| **route_import**  list / elements=string | Adds an import list of extended route target communities to the VRF. |
| **route_import_ipv4**  list / elements=string | Adds an import list of extended route target communities in address-family configuration submode to the VRF. |
| **route_import_ipv6**  list / elements=string | Adds an import list of extended route target communities in address-family configuration submode to the VRF. |
| **state**  string | Configures the state of the VRF definition as it relates to the device operational configuration. When set to *present*, the VRF should be configured in the device active configuration and when set to *absent* the VRF should not be in the device active configuration  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vrfs**  list / elements=any | The set of VRF definition objects to be configured on the remote IOS device. Ths list entries can either be the VRF name or a hash of VRF definitions and attributes. This argument is mutually exclusive with the `name` argument. |

## [Notes](ios_vrf_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](ios_vrf_module.md#id4)

```yaml+jinja
- name: Configure a vrf named management
  cisco.ios.ios_vrf:
    name: management
    description: oob mgmt vrf
    interfaces:
      - Management1

- name: Remove a vrf named test
  cisco.ios.ios_vrf:
    name: test
    state: absent

- name: Configure set of VRFs and purge any others
  cisco.ios.ios_vrf:
    vrfs:
      - red
      - blue
      - green
    purge: true

- name: Creates a list of import RTs for the VRF with the same parameters
  cisco.ios.ios_vrf:
    name: test_import
    rd: 1:100
    route_import:
      - 1:100
      - 3:100

- name:
    Creates a list of import RTs in address-family configuration submode for the
    VRF with the same parameters
  cisco.ios.ios_vrf:
    name: test_import_ipv4
    rd: 1:100
    route_import_ipv4:
      - 1:100
      - 3:100

- name:
    Creates a list of import RTs in address-family configuration submode for the
    VRF with the same parameters
  cisco.ios.ios_vrf:
    name: test_import_ipv6
    rd: 1:100
    route_import_ipv6:
      - 1:100
      - 3:100

- name: Creates a list of export RTs for the VRF with the same parameters
  cisco.ios.ios_vrf:
    name: test_export
    rd: 1:100
    route_export:
      - 1:100
      - 3:100

- name:
    Creates a list of export RTs in address-family configuration submode for the
    VRF with the same parameters
  cisco.ios.ios_vrf:
    name: test_export_ipv4
    rd: 1:100
    route_export_ipv4:
      - 1:100
      - 3:100

- name:
    Creates a list of export RTs in address-family configuration submode for the
    VRF with the same parameters
  cisco.ios.ios_vrf:
    name: test_export_ipv6
    rd: 1:100
    route_export_ipv6:
      - 1:100
      - 3:100

- name:
    Creates a list of import and export route targets for the VRF with the same
    parameters
  cisco.ios.ios_vrf:
    name: test_both
    rd: 1:100
    route_both:
      - 1:100
      - 3:100

- name:
    Creates a list of import and export route targets in address-family configuration
    submode for the VRF with the same parameters
  cisco.ios.ios_vrf:
    name: test_both_ipv4
    rd: 1:100
    route_both_ipv4:
      - 1:100
      - 3:100

- name:
    Creates a list of import and export route targets in address-family configuration
    submode for the VRF with the same parameters
  cisco.ios.ios_vrf:
    name: test_both_ipv6
    rd: 1:100
    route_both_ipv6:
      - 1:100
      - 3:100
```

## [Return Values](ios_vrf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["vrf definition ansible", "description management vrf", {"rd": "1:100"}]` |
| **delta**  string | The time elapsed to perform all operations  **Returned:** always  **Sample:** `"0:00:10.469466"` |
| **end**  string | The time the job ended  **Returned:** always  **Sample:** `"2016-11-16 10:38:25.595612"` |
| **start**  string | The time the job started  **Returned:** always  **Sample:** `"2016-11-16 10:38:15.126146"` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
