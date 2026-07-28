---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_rpm module – Install patch or feature rpms on Cisco NX-OS devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_rpm_module.html
fetched_at: 2026-07-28T01:39:07+00:00
---
# cisco.nxos.nxos_rpm module – Install patch or feature rpms on Cisco NX-OS devices.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_rpm`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_rpm_module.md#synopsis)
- [Parameters](nxos_rpm_module.md#parameters)
- [Notes](nxos_rpm_module.md#notes)
- [Examples](nxos_rpm_module.md#examples)
- [Return Values](nxos_rpm_module.md#return-values)

## [Synopsis](nxos_rpm_module.md#id1)

- Install software maintenance upgrade (smu) RPMS and 3rd party RPMS on Cisco NX-OS devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: rpm

## [Parameters](nxos_rpm_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of RPM/patch definitions. |
| **file_system**  string | The remote file system of the device. If omitted, devices that support a file_system parameter will use their default values. |
| **pkg**  string / required | Name of the RPM package. |
| **state**  string | If the state is present, the rpm will be installed, If the state is absent, it will be removed.  **Choices:**   - `"present"` - `"absent"` |
| **file_system**  string | The remote file system of the device. If omitted, devices that support a file_system parameter will use their default values.  **Default:** `"bootflash"` |
| **pkg**  string | Name of the RPM package. |
| **state**  string | If the state is present, the rpm will be installed, If the state is absent, it will be removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](nxos_rpm_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.0(3)I2(5), 7.0(3)I4(6), 7.0(3)I5(3), 7.0(3)I6(1), 7.0(3)I7(3)
> - Unsupported for Cisco MDS
> - For patches, the minimum platform version needed is 7.0(3)I2(5)
> - For feature rpms, the minimum platform version needed is 7.0(3)I6(1)
> - The module manages the entire RPM lifecycle (Add, activate, commit, deactivate, remove)
> - For reload patches, this module is NOT idempotent until the patch is committed.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_rpm_module.md#id4)

```yaml+jinja
- cisco.nxos.nxos_rpm:
    pkg: nxos.sample-n9k_ALL-1.0.0-7.0.3.I7.3.lib32_n9000.rpm
```

## [Return Values](nxos_rpm_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["install add bootflash:nxos.sample-n9k_ALL-1.0.0-7.0.3.I7.3.lib32_n9000.rpm forced", "install activate nxos.sample-n9k_ALL-1.0.0-7.0.3.I7.3.lib32_n9000 forced", "install commit nxos.sample-n9k_ALL-1.0.0-7.0.3.I7.3.lib32_n9000"]` |

### Authors

- Sai Chintalapudi (@saichint)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
