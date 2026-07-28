---
collection: ansible
version: "8"
title: "cisco.nxos.storage.nxos_vsan module – Configuration of vsan for Cisco NXOS MDS Switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/storage.nxos_vsan_module.html
fetched_at: 2026-07-28T01:39:27+00:00
---
# cisco.nxos.storage.nxos_vsan module – Configuration of vsan for Cisco NXOS MDS Switches.

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
> To use it in a playbook, specify: `cisco.nxos.storage.nxos_vsan`.

New in cisco.nxos 1.0.0

- [Synopsis](storage.nxos_vsan_module.md#synopsis)
- [Parameters](storage.nxos_vsan_module.md#parameters)
- [Notes](storage.nxos_vsan_module.md#notes)
- [Examples](storage.nxos_vsan_module.md#examples)
- [Return Values](storage.nxos_vsan_module.md#return-values)

## [Synopsis](storage.nxos_vsan_module.md#id1)

- Configuration of vsan for Cisco MDS NXOS.

Aliases: nxos_vsan

## [Parameters](storage.nxos_vsan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **vsan**  list / elements=dictionary | List of vsan details to be added or removed |
| **id**  integer / required | Vsan id |
| **interface**  list / elements=string | List of vsan’s interfaces to be added |
| **name**  string | Name of the vsan |
| **remove**  boolean | Removes the vsan if True  **Choices:**   - `false` - `true` |
| **suspend**  boolean | suspend the vsan if True  **Choices:**   - `false` - `true` |

## [Notes](storage.nxos_vsan_module.md#id3)

> **Note:**
>
> - Tested against Cisco MDS NX-OS 8.4(1)

## [Examples](storage.nxos_vsan_module.md#id4)

```yaml+jinja
- name: Test that vsan module works
  cisco.nxos.nxos_vsan:
    vsan:
    - id: 922
      interface:
      - fc1/1
      - fc1/2
      - port-channel 1
      name: vsan-SAN-A
      remove: false
      suspend: false
    - id: 923
      interface:
      - fc1/11
      - fc1/21
      - port-channel 2
      name: vsan-SAN-B
      remove: false
      suspend: true
    - id: 1923
      name: vsan-SAN-Old
      remove: true
```

## [Return Values](storage.nxos_vsan_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["terminal dont-ask", "vsan database", "vsan 922 interface fc1/40", "vsan 922 interface port-channel 155", "no terminal dont-ask"]` |

### Authors

- Suhas Bharadwaj (@srbharadwaj)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
