---
collection: ansible
version: "8"
title: "community.network.cnos_config module – Manage Lenovo CNOS configuration sections"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/cnos_config_module.html
fetched_at: 2026-07-28T01:56:09+00:00
---
# community.network.cnos_config module – Manage Lenovo CNOS configuration sections

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
> To use it in a playbook, specify: `community.network.cnos_config`.

- [Synopsis](cnos_config_module.md#synopsis)
- [Parameters](cnos_config_module.md#parameters)
- [Notes](cnos_config_module.md#notes)
- [Examples](cnos_config_module.md#examples)
- [Return Values](cnos_config_module.md#return-values)

## [Synopsis](cnos_config_module.md#id1)

- Lenovo CNOS configurations use a simple block indent file syntax for segmenting configuration into sections. This module provides an implementation for working with CNOS configuration sections in a deterministic way.

Aliases: network.cnos.cnos_config

## [Parameters](cnos_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **admin**  boolean | Enters into administration configuration mode for making config changes to the device.  **Choices:**   - `false` ← (default) - `true` |
| **after**  string | The ordered set of commands to append to the end of the command stack if a change needs to be made. Just like with *before* this allows the playbook designer to append a set of commands to be executed after the command set. |
| **backup**  boolean | This argument will cause the module to create a full backup of the current `running-config` from the remote device before any changes are made. If the `backup_options` value is not given, the backup file is written to the `backup` folder in the playbook root directory. If the directory does not exist, it is created.  **Choices:**   - `false` ← (default) - `true` |
| **backup_options**  dictionary | This is a dict object containing configurable options related to backup file path. The value of this option is read only when `backup` is set to *yes*, if `backup` is set to *no* this option will be silently ignored. |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist it will be first created and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given in that case a *backup* directory will be created in the current working directory and backup configuration will be copied in `filename` within *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the filename is not given it will be generated based on the hostname, current time and date in format defined by <hostname>_config.<current-date>@<current-time> |
| **before**  string | The ordered set of commands to push on to the command stack if a change needs to be made. This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system. |
| **comment**  string | Allows a commit description to be specified to be included when the configuration is committed. If the configuration is not changed or committed, this argument is ignored.  **Default:** `"configured by cnos_config"` |
| **config**  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *config* argument allows the implementer to pass in the configuration to use as the base config for comparison. |
| **lines**  aliases: commands  string | The ordered set of commands that should be configured in the section. The commands must be the exact same commands as found in the device running-config. Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser. |
| **match**  string | Instructs the module on the way to perform the matching of the set of commands against the current device config. If match is set to *line*, commands are matched line by line. If match is set to *strict*, command lines are matched with respect to position. If match is set to *exact*, command lines must be an equal match. Finally, if match is set to *none*, the module will not attempt to compare the source configuration with the running configuration on the remote device.  **Choices:**   - `"line"` ← (default) - `"strict"` - `"exact"` - `"none"` |
| **parents**  string | The ordered set of parents that uniquely identify the section the commands should be checked against. If the parents argument is omitted, the commands are checked against the set of top level or global commands. |
| **replace**  string | Instructs the module on the way to perform the configuration on the device. If the replace argument is set to *line* then the modified lines are pushed to the device in configuration mode. If the replace argument is set to *block* then the entire command block is pushed to the device in configuration mode if any line is not correct.  **Choices:**   - `"line"` ← (default) - `"block"` - `"config"` |
| **src**  string | Specifies the source path to the file that contains the configuration or configuration template to load. The path to the source file can either be the full path on the Ansible control host or a relative path from the playbook or role root directory. This argument is mutually exclusive with *lines*, *parents*. |

## [Notes](cnos_config_module.md#id3)

> **Note:**
>
> - Tested against CNOS 10.9.1

## [Examples](cnos_config_module.md#id4)

```yaml+jinja
Tasks: The following are examples of using the module cnos_config.
---
- name: Configure top level configuration
  community.network.cnos_config:
    "lines: hostname {{ inventory_hostname }}"

- name: Configure interface settings
  community.network.cnos_config:
    lines:
      - enable
      - ip ospf enable
    parents: interface ip 13

- name: Load a config from disk and replace the current config
  community.network.cnos_config:
    src: config.cfg
    backup: true

- name: Configurable backup path
  community.network.cnos_config:
    src: config.cfg
    backup: true
    backup_options:
      filename: backup.cfg
      dir_path: /home/user
```

## [Return Values](cnos_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  **Returned:** when backup is yes  **Sample:** `"/playbooks/ansible/backup/cnos01.2016-07-16@22:28:34"` |
| **updates**  list / elements=string | The set of commands that will be pushed to the remote device  **Returned:** Only when lines is specified.  **Sample:** `["...", "..."]` |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
