---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_config module – Module to manage configuration sections."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_config_module.html
fetched_at: 2026-07-28T01:26:40+00:00
---
# cisco.iosxr.iosxr_config module – Module to manage configuration sections.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/ui/repo/published/cisco/iosxr/) (version 5.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_config`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_config_module.md#synopsis)
- [Parameters](iosxr_config_module.md#parameters)
- [Notes](iosxr_config_module.md#notes)
- [Examples](iosxr_config_module.md#examples)
- [Return Values](iosxr_config_module.md#return-values)

## [Synopsis](iosxr_config_module.md#id1)

- Cisco IOS XR configurations use a simple block indent file syntax for segmenting configuration into sections. This module provides an implementation for working with IOS XR configuration sections in a deterministic way.

Aliases: config

## [Parameters](iosxr_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **admin**  boolean | Enters into administration configuration mode for making config changes to the device.  **Choices:**   - `false` ← (default) - `true` |
| **after**  list / elements=string | The ordered set of commands to append to the end of the command stack if a change needs to be made. Just like with *before* this allows the playbook designer to append a set of commands to be executed after the command set. |
| **backup**  boolean | This argument will cause the module to create a full backup of the current `running-config` from the remote device before any changes are made. If the `backup_options` value is not given, the backup file is written to the `backup` folder in the playbook root directory or role root directory, if playbook is part of an ansible role. If the directory does not exist, it is created.  **Choices:**   - `false` ← (default) - `true` |
| **backup_options**  dictionary | This is a dict object containing configurable options related to backup file path. The value of this option is read only when `backup` is set to *yes*, if `backup` is set to *no* this option will be silently ignored. |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist it will be first created and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given in that case a *backup* directory will be created in the current working directory and backup configuration will be copied in `filename` within *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the filename is not given it will be generated based on the hostname, current time and date in format defined by <hostname>_config.<current-date>@<current-time> |
| **before**  list / elements=string | The ordered set of commands to push on to the command stack if a change needs to be made. This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system. |
| **comment**  string | Allows a commit description to be specified to be included when the configuration is committed. If the configuration is not changed or committed, this argument is ignored.  **Default:** `"configured by iosxr_config"` |
| **config**  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *config* argument allows the implementer to pass in the configuration to use as the base config for comparison. The configuration lines for this option should be similar to how it will appear if present in the running-configuration of the device to ensure idempotency and correct diff. |
| **disable_default_comment**  boolean | disable default comment when set to True.  **Choices:**   - `false` ← (default) - `true` |
| **exclusive**  boolean | Enters into exclusive configuration mode that locks out all users from committing configuration changes until the exclusive session ends.  **Choices:**   - `false` ← (default) - `true` |
| **force**  boolean | The force argument instructs the module to not consider the current devices running-config. When set to true, this will cause the module to push the contents of *src* into the device without first checking if already configured.  Note this argument should be considered deprecated. To achieve the equivalent, set the `match=none` which is idempotent. This argument will be removed in a future release.  **Choices:**   - `false` ← (default) - `true` |
| **label**  string | Allows a commit label to be specified to be included when the configuration is committed. A valid label must begin with an alphabet and not exceed 30 characters, only alphabets, digits, hyphens and underscores are allowed. If the configuration is not changed or committed, this argument is ignored. |
| **lines**  aliases: commands  list / elements=string | The ordered set of commands that should be configured in the section. The commands must be the exact same commands as found in the device running-config as found in the device running-config to ensure idempotency and correct diff. Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser. |
| **match**  string | Instructs the module on the way to perform the matching of the set of commands against the current device config. If match is set to *line*, commands are matched line by line. If match is set to *strict*, command lines are matched with respect to position. If match is set to *exact*, command lines must be an equal match. Finally, if match is set to *none*, the module will not attempt to compare the source configuration with the running configuration on the remote device.  **Choices:**   - `"line"` ← (default) - `"strict"` - `"exact"` - `"none"` |
| **parents**  list / elements=string | The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against. If the parents argument is omitted, the commands are checked against the set of top level or global commands. |
| **replace**  string | Instructs the module on the way to perform the configuration on the device. If the replace argument is set to *line* then the modified lines are pushed to the device in configuration mode. If the replace argument is set to *block* then the entire command block is pushed to the device in configuration mode if any line is not correct.  **Choices:**   - `"line"` ← (default) - `"block"` - `"config"` |
| **src**  path | Specifies the source path to the file that contains the configuration or configuration template to load. The path to the source file can either be the full path on the Ansible control host or a relative path from the playbook or role root directory. This argument is mutually exclusive with *lines*, *parents*. The configuration lines in the source file should be similar to how it will appear if present in the running-configuration of the device to ensure idempotency and correct diff. |

## [Notes](iosxr_config_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_iosxr.html>
> - This module does not support `netconf` connection
> - Abbreviated commands are NOT idempotent, see <https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-do-the-config-modules-always-return-changed-true-with-abbreviated-commands>
> - Avoid service disrupting changes (viz. Management IP) from config replace.
> - Do not use `end` in the replace config file.
> - To ensure idempotency and correct diff the configuration lines in the relevant module options should be similar to how they appear if present in the running configuration on device including the indentation.
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](iosxr_config_module.md#id4)

```yaml+jinja
- name: configure top level configuration
  cisco.iosxr.iosxr_config:
    lines: hostname {{ inventory_hostname }}

- name: configure interface settings
  cisco.iosxr.iosxr_config:
    lines:
    - description test interface
    - ip address 172.31.1.1 255.255.255.0
    parents: interface GigabitEthernet0/0/0/0

- name: load a config from disk and replace the current config
  cisco.iosxr.iosxr_config:
    src: config.cfg
    replace: config
    backup: yes

- name: for idempotency, use full-form commands
  cisco.iosxr.iosxr_config:
    lines:
      # - shut
    - shutdown
    # parents: int g0/0/0/1
    parents: interface GigabitEthernet0/0/0/1

- name: configurable backup path
  cisco.iosxr.iosxr_config:
    src: config.cfg
    backup: yes
    backup_options:
      filename: backup.cfg
      dir_path: /home/user
```

## [Return Values](iosxr_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  **Returned:** when backup is yes  **Sample:** `"/playbooks/ansible/backup/iosxr01_config.2016-07-16@22:28:34"` |
| **commands**  list / elements=string | The set of commands that will be pushed to the remote device  **Returned:** If there are commands to run against the host  **Sample:** `["hostname foo", "router ospf 1", "router-id 1.1.1.1"]` |
| **date**  string | The date extracted from the backup file name  **Returned:** when backup is yes  **Sample:** `"2016-07-16"` |
| **filename**  string | The name of the backup file  **Returned:** when backup is yes and filename is not specified in backup options  **Sample:** `"iosxr01_config.2016-07-16@22:28:34"` |
| **shortname**  string | The full path to the backup file excluding the timestamp  **Returned:** when backup is yes and filename is not specified in backup options  **Sample:** `"/playbooks/ansible/backup/iosxr01_config"` |
| **time**  string | The time extracted from the backup file name  **Returned:** when backup is yes  **Sample:** `"22:28:34"` |

### Authors

- Ricardo Carrillo Cruz (@rcarrillocruz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
