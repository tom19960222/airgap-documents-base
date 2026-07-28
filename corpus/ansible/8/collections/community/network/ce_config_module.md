---
collection: ansible
version: "8"
title: "community.network.ce_config module – Manage Huawei CloudEngine configuration sections."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_config_module.html
fetched_at: 2026-07-28T01:55:20+00:00
---
# community.network.ce_config module – Manage Huawei CloudEngine configuration sections.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ce_config`.

- [Synopsis](ce_config_module.md#synopsis)
- [Parameters](ce_config_module.md#parameters)
- [Notes](ce_config_module.md#notes)
- [Examples](ce_config_module.md#examples)
- [Return Values](ce_config_module.md#return-values)

## [Synopsis](ce_config_module.md#id1)

- Huawei CloudEngine configurations use a simple block indent file syntax for segmenting configuration into sections. This module provides an implementation for working with CloudEngine configuration sections in a deterministic way. This module works with CLI transports.

Aliases: network.cloudengine.ce_config

## [Parameters](ce_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **after**  string | The ordered set of commands to append to the end of the command stack if a change needs to be made. Just like with *before* this allows the playbook designer to append a set of commands to be executed after the command set. |
| **backup**  boolean | This argument will cause the module to create a full backup of the current `current-configuration` from the remote device before any changes are made. If the `backup_options` value is not given, the backup file is written to the `backup` folder in the playbook root directory. If the directory does not exist, it is created.  **Choices:**   - `false` ← (default) - `true` |
| **backup_options**  dictionary | This is a dict object containing configurable options related to backup file path. The value of this option is read only when `backup` is set to *yes*, if `backup` is set to *no* this option will be silently ignored. |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist it will be first created and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given in that case a *backup* directory will be created in the current working directory and backup configuration will be copied in `filename` within *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the filename is not given it will be generated based on the hostname, current time and date in format defined by <hostname>_config.<current-date>@<current-time> |
| **before**  string | The ordered set of commands to push on to the command stack if a change needs to be made. This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system. |
| **config**  string | The module, by default, will connect to the remote device and retrieve the current current-configuration to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current-configuration for every task in a playbook. The *config* argument allows the implementer to pass in the configuration to use as the base config for comparison. |
| **defaults**  boolean | The *defaults* argument will influence how the current-configuration is collected from the device. When the value is set to true, the command used to collect the current-configuration is append with the all keyword. When the value is set to false, the command is issued without the all keyword.  **Choices:**   - `false` ← (default) - `true` |
| **lines**  string | The ordered set of commands that should be configured in the section. The commands must be the exact same commands as found in the device current-configuration. Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser. |
| **match**  string | Instructs the module on the way to perform the matching of the set of commands against the current device config. If match is set to *line*, commands are matched line by line. If match is set to *strict*, command lines are matched with respect to position. If match is set to *exact*, command lines must be an equal match. Finally, if match is set to *none*, the module will not attempt to compare the source configuration with the current-configuration on the remote device.  **Choices:**   - `"line"` ← (default) - `"strict"` - `"exact"` - `"none"` |
| **parents**  string | The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against. If the parents argument is omitted, the commands are checked against the set of top level or global commands. |
| **replace**  string | Instructs the module on the way to perform the configuration on the device. If the replace argument is set to *line* then the modified lines are pushed to the device in configuration mode. If the replace argument is set to *block* then the entire command block is pushed to the device in configuration mode if any line is not correct.  **Choices:**   - `"line"` ← (default) - `"block"` |
| **save**  boolean | The `save` argument instructs the module to save the current-configuration to saved-configuration. This operation is performed after any changes are made to the current running config. If no changes are made, the configuration is still saved to the startup config. This option will always cause the module to return changed.  **Choices:**   - `false` ← (default) - `true` |
| **src**  string | The *src* argument provides a path to the configuration file to load into the remote system. The path can either be a full system path to the configuration file if the value starts with / or relative to the root of the implemented role or playbook. This argument is mutually exclusive with the *lines* and *parents* arguments. |

## [Notes](ce_config_module.md#id3)

> **Note:**
>
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_config_module.md#id4)

```yaml+jinja
- name: CloudEngine config test
  hosts: cloudengine
  connection: local
  gather_facts: false

  tasks:
  - name: "Configure top level configuration and save it"
    community.network.ce_config:
      lines: sysname {{ inventory_hostname }}
      save: true

  - name: "Configure acl configuration and save it"
    community.network.ce_config:
      lines:
        - rule 10 permit source 1.1.1.1 32
        - rule 20 permit source 2.2.2.2 32
        - rule 30 permit source 3.3.3.3 32
        - rule 40 permit source 4.4.4.4 32
        - rule 50 permit source 5.5.5.5 32
      parents: acl 2000
      before: undo acl 2000
      match: exact

  - name: "Configure acl configuration and save it"
    community.network.ce_config:
      lines:
        - rule 10 permit source 1.1.1.1 32
        - rule 20 permit source 2.2.2.2 32
        - rule 30 permit source 3.3.3.3 32
        - rule 40 permit source 4.4.4.4 32
      parents: acl 2000
      before: undo acl 2000
      replace: block

  - name: Configurable backup path
    community.network.ce_config:
      lines: sysname {{ inventory_hostname }}
      backup: true
      backup_options:
        filename: backup.cfg
        dir_path: /home/user
```

## [Return Values](ce_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  **Returned:** when backup is yes  **Sample:** `"/playbooks/ansible/backup/ce_config.2016-07-16@22:28:34"` |
| **updates**  list / elements=string | The set of commands that will be pushed to the remote device  **Returned:** Only when lines is specified.  **Sample:** `["...", "..."]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
