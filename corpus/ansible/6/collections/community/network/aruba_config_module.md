---
collection: ansible
version: "6"
title: "community.network.aruba_config module – Manage Aruba configuration sections"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/aruba_config_module.html
fetched_at: 2026-07-27T17:16:25+00:00
---
# community.network.aruba_config module – Manage Aruba configuration sections

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
> To use it in a playbook, specify: `community.network.aruba_config`.

- [Synopsis](aruba_config_module.md#synopsis)
- [Parameters](aruba_config_module.md#parameters)
- [Examples](aruba_config_module.md#examples)
- [Return Values](aruba_config_module.md#return-values)

## [Synopsis](aruba_config_module.md#id1)

- Aruba configurations use a simple block indent file syntax for segmenting configuration into sections. This module provides an implementation for working with Aruba configuration sections in a deterministic way.

## [Parameters](aruba_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **after**  string | The ordered set of commands to append to the end of the command stack if a change needs to be made. Just like with *before* this allows the playbook designer to append a set of commands to be executed after the command set. |
| **backup**  boolean | This argument will cause the module to create a full backup of the current `running-config` from the remote device before any changes are made. If the `backup_options` value is not given, the backup file is written to the `backup` folder in the playbook root directory. If the directory does not exist, it is created.  Choices:   - `false` ← (default) - `true` |
| **backup_options**  dictionary | This is a dict object containing configurable options related to backup file path. The value of this option is read only when `backup` is set to *yes*, if `backup` is set to *no* this option will be silently ignored. |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist it will be first created and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given in that case a *backup* directory will be created in the current working directory and backup configuration will be copied in `filename` within *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the filename is not given it will be generated based on the hostname, current time and date in format defined by <hostname>_config.<current-date>@<current-time> |
| **before**  string | The ordered set of commands to push on to the command stack if a change needs to be made. This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system. |
| **diff_against**  string | When using the `ansible-playbook --diff` command line argument the module can generate diffs against different sources.  When this option is configure as *startup*, the module will return the diff of the running-config against the startup configuration.  When this option is configured as *intended*, the module will return the diff of the running-config against the configuration provided in the `intended_config` argument.  When this option is configured as *running*, the module will return the before and after diff of the running-config with respect to any changes made to the device configuration.  Choices:   - `"startup"` - `"intended"` - `"running"` |
| **diff_ignore_lines**  string | Use this argument to specify one or more lines that should be ignored during the diff. This is used for lines in the configuration that are automatically updated by the system. This argument takes a list of regular expressions or exact line matches. |
| **encrypt**  boolean | This allows an Aruba controller’s passwords and keys to be displayed in plain text when set to *false* or encrypted when set to *true*. If set to *false*, the setting will re-encrypt at the end of the module run. Backups are still encrypted even when set to *false*.  Choices:   - `false` - `true` ← (default) |
| **intended_config**  string | The `intended_config` provides the master configuration that the node should conform to and is used to check the final running-config against. This argument will not modify any settings on the remote device and is strictly used to check the compliance of the current device’s configuration against. When specifying this argument, the task should also modify the `diff_against` value and set it to *intended*. |
| **lines**  aliases: commands  string | The ordered set of commands that should be configured in the section. The commands must be the exact same commands as found in the device running-config. Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser. |
| **match**  string | Instructs the module on the way to perform the matching of the set of commands against the current device config. If match is set to *line*, commands are matched line by line. If match is set to *strict*, command lines are matched with respect to position. If match is set to *exact*, command lines must be an equal match. Finally, if match is set to *none*, the module will not attempt to compare the source configuration with the running configuration on the remote device.  Choices:   - `"line"` ← (default) - `"strict"` - `"exact"` - `"none"` |
| **parents**  string | The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against. If the parents argument is omitted, the commands are checked against the set of top level or global commands. |
| **replace**  string | Instructs the module on the way to perform the configuration on the device. If the replace argument is set to *line* then the modified lines are pushed to the device in configuration mode. If the replace argument is set to *block* then the entire command block is pushed to the device in configuration mode if any line is not correct.  Choices:   - `"line"` ← (default) - `"block"` |
| **running_config**  aliases: config  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *running_config* argument allows the implementer to pass in the configuration to use as the base config for comparison. |
| **save_when**  string | When changes are made to the device running-configuration, the changes are not copied to non-volatile storage by default. Using this argument will change that before. If the argument is set to *always*, then the running-config will always be copied to the startup configuration and the *modified* flag will always be set to True. If the argument is set to *modified*, then the running-config will only be copied to the startup configuration if it has changed since the last save to startup configuration. If the argument is set to *never*, the running-config will never be copied to the startup configuration. If the argument is set to *changed*, then the running-config will only be copied to the startup configuration if the task has made a change.  Choices:   - `"always"` - `"never"` ← (default) - `"modified"` - `"changed"` |
| **src**  string | Specifies the source path to the file that contains the configuration or configuration template to load. The path to the source file can either be the full path on the Ansible control host or a relative path from the playbook or role root directory. This argument is mutually exclusive with *lines*, *parents*. |

## [Examples](aruba_config_module.md#id3)

```yaml+jinja
- name: Configure top level configuration
  community.network.aruba_config:
    lines: hostname {{ inventory_hostname }}

- name: Diff the running-config against a provided config
  community.network.aruba_config:
    diff_against: intended
    intended_config: "{{ lookup('file', 'master.cfg') }}"

- name: Configure interface settings
  community.network.aruba_config:
    lines:
      - description test interface
      - ip access-group 1 in
    parents: interface gigabitethernet 0/0/0

- name: Load new acl into device
  community.network.aruba_config:
    lines:
      - permit host 10.10.10.10
      - ipv6 permit host fda9:97d6:32a3:3e59::3333
    parents: ip access-list standard 1
    before: no ip access-list standard 1
    match: exact

- name: Configurable backup path
  community.network.aruba_config:
    backup: yes
    lines: hostname {{ inventory_hostname }}
    backup_options:
      filename: backup.cfg
      dir_path: /home/user
```

## [Return Values](aruba_config_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  Returned: when backup is yes  Sample: `"/playbooks/ansible/backup/aruba_config.2016-07-16@22:28:34"` |
| **commands**  list / elements=string | The set of commands that will be pushed to the remote device  Returned: always  Sample: `["hostname foo", "vlan 1", "name default"]` |
| **updates**  list / elements=string | The set of commands that will be pushed to the remote device  Returned: always  Sample: `["hostname foo", "vlan 1", "name default"]` |

### Authors

- James Mighion (@jmighion)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
