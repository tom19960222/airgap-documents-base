---
collection: ansible
version: "8"
title: "dellemc.powerflex.powerflex_sdr role – Role to manage installation and uninstallation Powerflex SDR"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/powerflex/powerflex_sdr_role.html
fetched_at: 2026-07-28T02:05:18+00:00
---
# dellemc.powerflex.powerflex_sdr role – Role to manage installation and uninstallation Powerflex SDR

> **Note:**
>
> This role is part of the [dellemc.powerflex collection](https://galaxy.ansible.com/ui/repo/published/dellemc/powerflex/) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it use: `ansible-galaxy collection install dellemc.powerflex`.
>
> To use it in a playbook, specify: `dellemc.powerflex.powerflex_sdr`.

- [Entry point `main` – Role to manage installation and uninstallation Powerflex SDR](powerflex_sdr_role.md#entry-point-main-role-to-manage-installation-and-uninstallation-powerflex-sdr)

  - [Synopsis](powerflex_sdr_role.md#synopsis)
  - [Parameters](powerflex_sdr_role.md#parameters)

## [Entry point `main` – Role to manage installation and uninstallation Powerflex SDR](powerflex_sdr_role.md#id1)

### [Synopsis](powerflex_sdr_role.md#id2)

- Role to manage installation and uninstallation Powerflex SDR.

### [Parameters](powerflex_sdr_role.md#id3)

| Parameter | Comments |
| --- | --- |
| **powerflex_common_file_install_location**  path | Location of installation and rpm gpg files to be installed.  The required, compatible installation software package based on the operating system of the node.  The files can be downloaded from the Dell Product support page for PowerFlex software.  **Default:** `"/var/tmp"` |
| **powerflex_mdm_password**  string / required | Password for the Powerflex MDM. |
| **powerflex_protection_domain_name**  string | The name of the protection domain to which the SDR will be added. |
| **powerflex_sdr_repl_journal_capacity_max_ratio**  integer | Maximum capacity percentage to be allocated for journal capacity.  **Default:** `10` |
| **powerflex_sdr_state**  string | Specifies the state of SDR.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **powerflex_storage_pool_name**  string | The name of the storage pool to which the device will be added. |

#### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-powerflex/tree/1.9.0)
