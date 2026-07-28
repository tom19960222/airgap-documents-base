---
collection: ansible
version: "6"
title: "community.network.sros_config module – Manage Nokia SR OS device configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/sros_config_module.html
fetched_at: 2026-07-27T17:19:47+00:00
---
# community.network.sros_config module – Manage Nokia SR OS device configuration

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.sros_config`.

- [Synopsis](sros_config_module.md#synopsis)
- [Parameters](sros_config_module.md#parameters)
- [Notes](sros_config_module.md#notes)
- [Examples](sros_config_module.md#examples)
- [Return Values](sros_config_module.md#return-values)

## [Synopsis](sros_config_module.md#id1)

- Nokia SR OS configurations use a simple block indent file syntax for segmenting configuration into sections. This module provides an implementation for working with SR OS configuration sections in a deterministic way.

## [Parameters](sros_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **after**  string | The ordered set of commands to append to the end of the command stack if a change needs to be made. Just like with *before* this allows the playbook designer to append a set of commands to be executed after the command set. |
| **backup**  boolean | This argument will cause the module to create a full backup of the current `running-config` from the remote device before any changes are made. If the `backup_options` value is not given, the backup file is written to the `backup` folder in the playbook root directory. If the directory does not exist, it is created.  Choices:   - `false` ← (default) - `true` |
| **backup_options**  dictionary | This is a dict object containing configurable options related to backup file path. The value of this option is read only when `backup` is set to *yes*, if `backup` is set to *no* this option will be silently ignored. |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist it will be first created and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given in that case a *backup* directory will be created in the current working directory and backup configuration will be copied in `filename` within *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the filename is not given it will be generated based on the hostname, current time and date in format defined by <hostname>_config.<current-date>@<current-time> |
| **before**  string | The ordered set of commands to push on to the command stack if a change needs to be made. This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system. |
| **config**  string | The `config` argument allows the playbook designer to supply the base configuration to be used to validate configuration changes necessary. If this argument is provided, the module will not download the running-config from the remote node. |
| **defaults**  aliases: detail  boolean | This argument specifies whether or not to collect all defaults when getting the remote device running config. When enabled, the module will get the current config by issuing the command `admin display-config detail`.  Choices:   - `false` ← (default) - `true` |
| **force**  boolean | The force argument instructs the module to not consider the current devices running-config. When set to true, this will cause the module to push the contents of *src* into the device without first checking if already configured.  Note this argument should be considered deprecated. To achieve the equivalent, set the `match=none` which is idempotent. This argument will be removed in a future release.  Choices:   - `false` - `true` |
| **lines**  aliases: commands  string | The ordered set of commands that should be configured in the section. The commands must be the exact same commands as found in the device running-config. Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser. The *lines* argument only supports current context lines. See EXAMPLES |
| **match**  string | Instructs the module on the way to perform the matching of the set of commands against the current device config. If match is set to *line*, commands are matched line by line. If match is set to *none*, the module will not attempt to compare the source configuration with the running configuration on the remote device.  Choices:   - `"line"` ← (default) - `"none"` |
| **parents**  string | The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against. If the parents argument is omitted, the commands are checked against the set of top level or global commands. |
| **replace**  string | Instructs the module on the way to perform the configuration on the device. If the replace argument is set to *line* then the modified lines are pushed to the device in configuration mode. If the replace argument is set to *block* then the entire command block is pushed to the device in configuration mode if any line is not correct.  Choices:   - `"line"` ← (default) - `"block"` |
| **save**  boolean | The `save` argument instructs the module to save the running- config to the startup-config at the conclusion of the module running. If check mode is specified, this argument is ignored.  Choices:   - `false` ← (default) - `true` |
| **src**  string | Specifies the source path to the file that contains the configuration or configuration template to load. The path to the source file can either be the full path on the Ansible control host or a relative path from the playbook or role root directory. This argument is mutually exclusive with *lines*, *parents*. |

## [Notes](sros_config_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage Nokia SR OS Network devices see <https://www.ansible.com/ansible-nokia>.

## [Examples](sros_config_module.md#id4)

```yaml+jinja
---
- name: Enable rollback location
  community.network.sros_config:
    lines: configure system rollback rollback-location "cf3:/ansible"

- name: Set system name to {{ inventory_hostname }} using one line
  community.network.sros_config:
    lines:
        - configure system name "{{ inventory_hostname }}"

- name: Set system name to {{ inventory_hostname }} using parents
  community.network.sros_config:
    lines:
        - 'name "{{ inventory_hostname }}"'
    parents:
        - configure
        - system
    backup: yes

- name: Load config from file
  community.network.sros_config:
      src: "{{ inventory_hostname }}.cfg"
      save: yes

- name: Invalid use of lines
  community.network.sros_config:
    lines:
      - service
      -     vpls 1000 customer foo 1 create
      -         description "invalid lines example"

- name: Valid use of lines
  community.network.sros_config:
    lines:
      - description "invalid lines example"
    parents:
      - service
      - vpls 1000 customer foo 1 create

- name: Configurable backup path
  community.network.sros_config:
    backup: yes
    backup_options:
      filename: backup.cfg
      dir_path: /home/user
```

## [Return Values](sros_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  Returned: when backup is yes  Sample: `"/playbooks/ansible/backup/sros_config.2016-07-16@22:28:34"` |
| **commands**  list / elements=string | The set of commands that will be pushed to the remote device  Returned: always  Sample: `["config system name \"sros01\""]` |
| **updates**  list / elements=string | The set of commands that will be pushed to the remote device  Returned: always  Sample: `["config system name \"sros01\""]` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
