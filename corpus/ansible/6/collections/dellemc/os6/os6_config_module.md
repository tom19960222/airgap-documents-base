---
collection: ansible
version: "6"
title: "dellemc.os6.os6_config module – Manage Dell EMC OS6 configuration sections"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/os6/os6_config_module.html
fetched_at: 2026-07-27T17:26:05+00:00
---
# dellemc.os6.os6_config module – Manage Dell EMC OS6 configuration sections

> **Note:**
>
> This module is part of the [dellemc.os6 collection](https://galaxy.ansible.com/dellemc/os6) (version 1.0.7).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.os6`.
>
> To use it in a playbook, specify: `dellemc.os6.os6_config`.

- [Synopsis](os6_config_module.md#synopsis)
- [Parameters](os6_config_module.md#parameters)
- [Notes](os6_config_module.md#notes)
- [Examples](os6_config_module.md#examples)
- [Return Values](os6_config_module.md#return-values)

## [Synopsis](os6_config_module.md#id1)

- OS6 configurations use a simple block indent file syntax for segmenting configuration into sections. This module provides an implementation for working with OS6 configuration sections in a deterministic way.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](os6_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **after**  list / elements=string | The ordered set of commands to append to the end of the command stack if a change needs to be made. Just like with *before* this allows the playbook designer to append a set of commands to be executed after the command set. |
| **backup**  boolean | This argument will cause the module to create a full backup of the current `running-config` from the remote device before any changes are made. If the `backup_options` value is not given, the backup file is written to the `backup` folder in the playbook root directory. If the directory does not exist, it is created.  Choices:   - `false` ← (default) - `true` |
| **backup_options**  dictionary | This is a dict object containing configurable options related to backup file path. The value of this option is read only when `backup` is set to *yes*, if `backup` is set to *no* this option will be silently ignored. |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist it will be first created and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given in that case a *backup* directory will be created in the current working directory and backup configuration will be copied in `filename` within *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the the filename is not given it will be generated based on the hostname, current time and date in format defined by <hostname>_config.<current-date>@<current-time> |
| **before**  list / elements=string | The ordered set of commands to push on to the command stack if a change needs to be made. This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system. |
| **config**  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *config* argument allows the implementer to pass in the configuration to use as the base config for comparison. |
| **lines**  aliases: commands  list / elements=string | The ordered set of commands that should be configured in the section. The commands must be the exact same commands as found in the device running-config. Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser. This argument is mutually exclusive with *src*. |
| **match**  string | Instructs the module on the way to perform the matching of the set of commands against the current device config. If match is set to *line*, commands are matched line by line. If match is set to *strict*, command lines are matched with respect to position. If match is set to *exact*, command lines must be an equal match. Finally, if match is set to *none*, the module will not attempt to compare the source configuration with the running configuration on the remote device.  Choices:   - `"line"` ← (default) - `"strict"` - `"exact"` - `"none"` |
| **parents**  list / elements=string | The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against. If the parents argument is omitted, the commands are checked against the set of top level or global commands. |
| **provider**  dictionary | A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Password to authenticate the SSH session to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Path to an ssh key used to authenticate the SSH session to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies idle timeout (in seconds) for the connection. Useful if the console freezes before continuing. For example when saving configurations. |
| **username**  string | User to authenticate the SSH session to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **replace**  string | Instructs the module on the way to perform the configuration on the device. If the replace argument is set to *line* then the modified lines are pushed to the device in configuration mode. If the replace argument is set to *block* then the entire command block is pushed to the device in configuration mode if any line is not correct.  Choices:   - `"line"` ← (default) - `"block"` |
| **save**  boolean | The `save` argument instructs the module to save the running- config to the startup-config at the conclusion of the module running. If check mode is specified, this argument is ignored.  Choices:   - `false` ← (default) - `true` |
| **src**  path | Specifies the source path to the file that contains the configuration or configuration template to load. The path to the source file can either be the full path on the Ansible control host or a relative path from the playbook or role root directory. This argument is mutually exclusive with *lines*. |
| **update**  string | The *update* argument controls how the configuration statements are processed on the remote device. Valid choices for the *update* argument are *merge* and *check*. When you set this argument to *merge*, the configuration changes merge with the current device running configuration. When you set this argument to *check* the configuration updates are determined but not actually configured on the remote device.  Choices:   - `"merge"` ← (default) - `"check"` |

## [Notes](os6_config_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage Dell EMC Network devices see <https://www.ansible.com/ansible-dell-networking>.

## [Examples](os6_config_module.md#id4)

```yaml+jinja
- os6_config:
    lines: ['hostname {{ inventory_hostname }}']
- os6_config:
    lines:
      - 10 permit ip 1.1.1.1 any log
      - 20 permit ip 2.2.2.2 any log
      - 30 permit ip 3.3.3.3 any log
      - 40 permit ip 4.4.4.4 any log
      - 50 permit ip  5.5.5.5 any log
    parents: ['ip access-list test']
    before: ['no ip access-list test']
    match: exact
- os6_config:
    lines:
      - 10 permit ip 1.1.1.1 any log
      - 20 permit ip 2.2.2.2 any log
      - 30 permit ip 3.3.3.3 any log
      - 40 permit ip 4.4.4.4 any log
    parents: ['ip access-list test']
    before: ['no ip access-list test']
    replace: block
- os6_config:
    lines: ['hostname {{ inventory_hostname }}']
    backup: yes
    backup_options:
      filename: backup.cfg
      dir_path: /home/user
```

## [Return Values](os6_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  Returned: when backup is yes  Sample: `"/playbooks/ansible/backup/os6_config.2017-07-16@22:28:34"` |
| **commands**  list / elements=string | The set of commands that will be pushed to the remote device  Returned: always  Sample: `["interface Te1/0/1", "no shutdown", "exit"]` |
| **saved**  boolean | Returns whether the configuration is saved to the startup configuration or not.  Returned: When not check_mode.  Sample: `true` |
| **updates**  list / elements=string | The set of commands that will be pushed to the remote device.  Returned: always  Sample: `["interface Te1/0/1", "no shutdown", "exit"]` |

### Authors

- Abirami N (@abirami-n)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.os6/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.os6)
