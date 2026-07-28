---
collection: ansible
version: "6"
title: "dellemc.enterprise_sonic.sonic_config module – Manages configuration sections on devices running Enterprise SONiC"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/enterprise_sonic/sonic_config_module.html
fetched_at: 2026-07-27T17:24:52+00:00
---
# dellemc.enterprise_sonic.sonic_config module – Manages configuration sections on devices running Enterprise SONiC

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/dellemc/enterprise_sonic) (version 1.1.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_config`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_config_module.md#synopsis)
- [Parameters](sonic_config_module.md#parameters)
- [Notes](sonic_config_module.md#notes)
- [Examples](sonic_config_module.md#examples)
- [Return Values](sonic_config_module.md#return-values)

## [Synopsis](sonic_config_module.md#id1)

- Manages configuration sections of Enterprise SONiC Distribution by Dell Technologies. SONiC configurations use a simple block indent file syntax for segmenting configuration into sections. This module provides an implementation for working with SONiC configuration sections in a deterministic way.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **after**  list / elements=string | The ordered set of commands to append to the end of the command stack if a change needs to be made. Just like with *before*, this allows the playbook designer to append a set of commands to be executed after the command set. |
| **backup**  boolean | This argument causes the module to create a full backup of the current `running-configuration` from the remote device before any changes are made. If the `backup_options` value is not given, the backup file is written to the `backup` folder in the playbook root directory. If the directory does not exist, it is created.  Choices:   - `false` ← (default) - `true` |
| **backup_options**  dictionary | This is a dictionary object containing configurable options related to backup file path. The value of this option is read only when `backup` is set to *yes*, if `backup` is set to *no* this option is ignored. |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file is stored. If the directory does not exist it is first created, and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given, an *backup* directory is created in the current working directory and backup configuration is copied in `filename` within the *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the filename is not given, it is generated based on the hostname, current time, and date in the format defined by <hostname>_config.<current-date>@<current-time>. |
| **before**  list / elements=string | The ordered set of commands to push on to the command stack if a change needs to be made. This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system. |
| **config**  string | The module, by default, connects to the remote device and retrieves the current running-configuration to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-configuration for every task in a playbook. The *config* argument allows the implementer to pass in the configuration to use as the base configuration for comparison. |
| **lines**  aliases: commands  list / elements=string | The ordered set of commands that should be configured in the section. The commands must be the exact same commands as found in the device running-configuration. Be sure to note the configuration command syntax as some commands are automatically modified by the device configuration parser. This argument is mutually exclusive with *src*. |
| **match**  string | Instructs the module on the way to perform the matching of the set of commands against the current device configuration. If match is set to *line*, commands are matched line by line. If match is set to *strict*, command lines are matched with respect to position. If match is set to *exact*, command lines must be an equal match. If match is set to *none*, the module does not attempt to compare the source configuration with the running-configuration on the remote device.  Choices:   - `"line"` ← (default) - `"strict"` - `"exact"` - `"none"` |
| **parents**  list / elements=string | The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against. If the parents argument is omitted, the commands are checked against the set of top level or global commands. |
| **replace**  string | Instructs the module how to perform a configuration on the device. If the replace argument is set to *line*, then the modified lines are pushed to the device in configuration mode. If the replace argument is set to *block*, then the entire command block is pushed to the device in configuration mode if any line is not correct.  Choices:   - `"line"` ← (default) - `"block"` |
| **save**  boolean | The `save` argument instructs the module to save the running- configuration to the startup-configuration at the conclusion of the module running. If check mode is specified, this argument is ignored.  Choices:   - `false` ← (default) - `true` |
| **src**  path | Specifies the source path to the file that contains the configuration or configuration template to load. The path to the source file can either be the full path on the Ansible control host, or a relative path from the playbook or role root directory. This argument is mutually exclusive with *lines*. |
| **update**  string | The *update* argument controls how the configuration statements are processed on the remote device. Valid choices for the *update* argument are *merge* and *check*. When you set this argument to *merge*, the configuration changes merge with the current device running-configuration. When you set this argument to *check*, the configuration updates are determined but not configured on the remote device.  Choices:   - `"merge"` ← (default) - `"check"` |

## [Notes](sonic_config_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_config_module.md#id4)

```yaml+jinja
- dellemc.enterprise_sonic.sonic_config:
    lines: ['username {{ user_name }} password {{ user_password }} role {{ user_role }}']

- dellemc.enterprise_sonic.sonic_config:
    lines:
      - description 'SONiC'
    parents: ['interface Eth1/10']

- dellemc.enterprise_sonic.sonic_config:
    lines:
      - seq 2 permit udp any any
      - seq 3 deny icmp any any
    parents: ['ip access-list test']
    before: ['no ip access-list test']
```

## [Return Values](sonic_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The set of commands that is pushed to the remote device.  Returned: always  Sample: `["username foo password foo role admin", "router bgp 1", "router-id 1.1.1.1"]` |
| **saved**  boolean | Returns whether the configuration is saved to the startup configuration or not.  Returned: When not check_mode.  Sample: `true` |
| **updates**  list / elements=string | The set of commands that is pushed to the remote device.  Returned: always  Sample: `["username foo password foo role admin", "router bgp 1", "router-id 1.1.1.1"]` |

### Authors

- Abirami N (@abirami-n)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
