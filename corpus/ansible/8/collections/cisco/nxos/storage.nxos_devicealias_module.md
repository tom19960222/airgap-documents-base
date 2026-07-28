---
collection: ansible
version: "8"
title: "cisco.nxos.storage.nxos_devicealias module – Configuration of device alias for Cisco NXOS MDS Switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/storage.nxos_devicealias_module.html
fetched_at: 2026-07-28T01:39:26+00:00
---
# cisco.nxos.storage.nxos_devicealias module – Configuration of device alias for Cisco NXOS MDS Switches.

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
> To use it in a playbook, specify: `cisco.nxos.storage.nxos_devicealias`.

New in cisco.nxos 1.0.0

- [Synopsis](storage.nxos_devicealias_module.md#synopsis)
- [Parameters](storage.nxos_devicealias_module.md#parameters)
- [Notes](storage.nxos_devicealias_module.md#notes)
- [Examples](storage.nxos_devicealias_module.md#examples)
- [Return Values](storage.nxos_devicealias_module.md#return-values)

## [Synopsis](storage.nxos_devicealias_module.md#id1)

- Configuration of device alias for Cisco MDS NXOS.

Aliases: nxos_devicealias

## [Parameters](storage.nxos_devicealias_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **da**  list / elements=dictionary | List of device-alias to be added or removed |
| **name**  string / required | Name of the device-alias to be added or removed |
| **pwwn**  string | pwwn to which the name needs to be associated with |
| **remove**  boolean | Removes the device-alias if set to True  **Choices:**   - `false` ← (default) - `true` |
| **distribute**  boolean | Enable/Disable device-alias distribution  **Choices:**   - `false` - `true` |
| **mode**  string | Mode of devices-alias, basic or enhanced  **Choices:**   - `"basic"` - `"enhanced"` |
| **rename**  list / elements=dictionary | List of device-alias to be renamed |
| **new_name**  string / required | New name of the device-alias |
| **old_name**  string / required | Old name of the device-alias that needs to be renamed |

## [Notes](storage.nxos_devicealias_module.md#id3)

> **Note:**
>
> - Tested against Cisco MDS NX-OS 8.4(1)

## [Examples](storage.nxos_devicealias_module.md#id4)

```yaml+jinja
- name: Test that device alias module works
  cisco.nxos.nxos_devicealias:
    da:
    - name: test1_add
      pwwn: 56:2:22:11:22:88:11:67
    - name: test2_add
      pwwn: 65:22:22:11:22:22:11:d
    - name: dev1
      remove: true
    - name: dev2
      remove: true
    distribute: true
    mode: enhanced
    rename:
    - new_name: bcd
      old_name: abc
    - new_name: bcd1
      old_name: abc1
```

## [Return Values](storage.nxos_devicealias_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["terminal dont-ask", "device-alias database", "device-alias name somename pwwn 10:00:00:00:89:a1:01:03", "device-alias name somename1 pwwn 10:00:00:00:89:a1:02:03", "device-alias commit", "no terminal dont-ask"]` |

### Authors

- Suhas Bharadwaj (@srbharadwaj)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
