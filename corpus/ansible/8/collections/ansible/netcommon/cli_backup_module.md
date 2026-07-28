---
collection: ansible
version: "8"
title: "ansible.netcommon.cli_backup module – Back up device configuration from network devices over network_cli"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/cli_backup_module.html
fetched_at: 2026-07-28T01:09:04+00:00
---
# ansible.netcommon.cli_backup module – Back up device configuration from network devices over network_cli

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ui/repo/published/ansible/netcommon/) (version 5.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.cli_backup`.

New in ansible.netcommon 4.2.0

- [Synopsis](cli_backup_module.md#synopsis)
- [Parameters](cli_backup_module.md#parameters)
- [Notes](cli_backup_module.md#notes)
- [Examples](cli_backup_module.md#examples)
- [Return Values](cli_backup_module.md#return-values)

## [Synopsis](cli_backup_module.md#id1)

- This module provides platform agnostic way of backing up text based configuration from network devices over network_cli connection plugin.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](cli_backup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **defaults**  boolean | The *defaults* argument will influence how the running-config is collected from the device. When the value is set to true, the command used to collect the running-config is append with the all keyword. When the value is set to false, the command is issued without the all keyword.  **Choices:**   - `false` ← (default) - `true` |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist it will be first created and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given in that case a *backup* directory will be created in the current working directory and backup configuration will be copied in `filename` within *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the filename is not given it will be generated based on the hostname, current time and date in format defined by <hostname>_config.<current-date>@<current-time> |

## [Notes](cli_backup_module.md#id3)

> **Note:**
>
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](cli_backup_module.md#id4)

```yaml+jinja
- name: configurable backup path
  ansible.netcommon.cli_backup:
    filename: backup.cfg
    dir_path: /home/user
```

## [Return Values](cli_backup_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  **Returned:** always  **Sample:** `"/playbooks/ansible/backup/hostname_config.2016-07-16@22:28:34"` |

### Authors

- Kate Case (@Qalthos)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
