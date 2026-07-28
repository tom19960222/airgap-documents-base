---
collection: ansible
version: "6"
title: "ansible.netcommon.cli_config module – Push text based configuration to network devices over network_cli"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/cli_config_module.html
fetched_at: 2026-07-27T16:44:26+00:00
---
# ansible.netcommon.cli_config module – Push text based configuration to network devices over network_cli

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.cli_config`.

New in ansible.netcommon 1.0.0

- [Synopsis](cli_config_module.md#synopsis)
- [Parameters](cli_config_module.md#parameters)
- [Notes](cli_config_module.md#notes)
- [Examples](cli_config_module.md#examples)
- [Return Values](cli_config_module.md#return-values)

## [Synopsis](cli_config_module.md#id1)

- This module provides platform agnostic way of pushing text based configuration to network devices over network_cli connection plugin.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](cli_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backup**  boolean | This argument will cause the module to create a full backup of the current running config from the remote device before any changes are made. If the `backup_options` value is not given, the backup file is written to the `backup` folder in the playbook root directory or role root directory, if playbook is part of an ansible role. If the directory does not exist, it is created.  Choices:   - `false` ← (default) - `true` |
| **backup_options**  dictionary | This is a dict object containing configurable options related to backup file path. The value of this option is read only when `backup` is set to *yes*, if `backup` is set to *no* this option will be silently ignored. |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist it will be first created and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given in that case a *backup* directory will be created in the current working directory and backup configuration will be copied in `filename` within *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the filename is not given it will be generated based on the hostname, current time and date in format defined by <hostname>_config.<current-date>@<current-time> |
| **commit**  boolean | The `commit` argument instructs the module to push the configuration to the device. This is mapped to module check mode.  Choices:   - `false` - `true` |
| **commit_comment**  string | The `commit_comment` argument specifies a text string to be used when committing the configuration. If the `commit` argument is set to False, this argument is silently ignored. This argument is only valid for the platforms that support commit operation with comment. |
| **config**  string | The config to be pushed to the network device. This argument is mutually exclusive with `rollback` and either one of the option should be given as input. To ensure idempotency and correct diff the configuration lines should be similar to how they appear if present in the running configuration on device including the indentation. |
| **defaults**  boolean | The *defaults* argument will influence how the running-config is collected from the device. When the value is set to true, the command used to collect the running-config is append with the all keyword. When the value is set to false, the command is issued without the all keyword.  Choices:   - `false` ← (default) - `true` |
| **diff_ignore_lines**  list / elements=string | Use this argument to specify one or more lines that should be ignored during the diff. This is used for lines in the configuration that are automatically updated by the system. This argument takes a list of regular expressions or exact line matches. Note that this parameter will be ignored if the platform has onbox diff support. |
| **diff_match**  string | Instructs the module on the way to perform the matching of the set of commands against the current device config. If `diff_match` is set to *line*, commands are matched line by line. If `diff_match` is set to *strict*, command lines are matched with respect to position. If `diff_match` is set to *exact*, command lines must be an equal match. Finally, if `diff_match` is set to *none*, the module will not attempt to compare the source configuration with the running configuration on the remote device. Note that this parameter will be ignored if the platform has onbox diff support.  Choices:   - `"line"` - `"strict"` - `"exact"` - `"none"` |
| **diff_replace**  string | Instructs the module on the way to perform the configuration on the device. If the `diff_replace` argument is set to *line* then the modified lines are pushed to the device in configuration mode. If the argument is set to *block* then the entire command block is pushed to the device in configuration mode if any line is not correct. Note that this parameter will be ignored if the platform has onbox diff support.  Choices:   - `"line"` - `"block"` - `"config"` |
| **multiline_delimiter**  string | This argument is used when pushing a multiline configuration element to the device. It specifies the character to use as the delimiting character. This only applies to the configuration action. |
| **replace**  string | If the `replace` argument is set to `yes`, it will replace the entire running-config of the device with the `config` argument value. For devices that support replacing running configuration from file on device like NXOS/JUNOS, the `replace` argument takes path to the file on the device that will be used for replacing the entire running-config. The value of `config` option should be *None* for such devices. Nexus 9K devices only support replace. Use *net_put* or *nxos_file_copy* in case of NXOS module to copy the flat file to remote device and then use set the fullpath to this argument. |
| **rollback**  integer | The `rollback` argument instructs the module to rollback the current configuration to the identifier specified in the argument. If the specified rollback identifier does not exist on the remote device, the module will fail. To rollback to the most recent commit, set the `rollback` argument to 0. This option is mutually exclusive with `config`. |

## [Notes](cli_config_module.md#id3)

> **Note:**
>
> - The commands will be returned only for platforms that do not support onbox diff. The `--diff` option with the playbook will return the difference in configuration for devices that has support for onbox diff
> - To ensure idempotency and correct diff the configuration lines in the relevant module options should be similar to how they appear if present in the running configuration on device including the indentation.
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](cli_config_module.md#id4)

```yaml+jinja
- name: configure device with config
  ansible.netcommon.cli_config:
    config: "{{ lookup('template', 'basic/config.j2') }}"

- name: multiline config
  ansible.netcommon.cli_config:
    config: |
      hostname foo
      feature nxapi

- name: configure device with config with defaults enabled
  ansible.netcommon.cli_config:
    config: "{{ lookup('template', 'basic/config.j2') }}"
    defaults: yes

- name: Use diff_match
  ansible.netcommon.cli_config:
    config: "{{ lookup('file', 'interface_config') }}"
    diff_match: none

- name: nxos replace config
  ansible.netcommon.cli_config:
    replace: bootflash:nxoscfg

- name: junos replace config
  ansible.netcommon.cli_config:
    replace: /var/home/ansible/junos01.cfg

- name: commit with comment
  ansible.netcommon.cli_config:
    config: set system host-name foo
    commit_comment: this is a test

- name: configurable backup path
  ansible.netcommon.cli_config:
    config: "{{ lookup('template', 'basic/config.j2') }}"
    backup: yes
    backup_options:
      filename: backup.cfg
      dir_path: /home/user
```

## [Return Values](cli_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  Returned: when backup is yes  Sample: `"/playbooks/ansible/backup/hostname_config.2016-07-16@22:28:34"` |
| **commands**  list / elements=string | The set of commands that will be pushed to the remote device  Returned: When *supports_generated_diff=True* and *supports_onbox_diff=False* in the platform’s cliconf plugin  Sample: `["interface Loopback999", "no shutdown"]` |
| **diff**  string | The diff generated on the device when the commands were applied  Returned: When *supports_onbox_diff=True* in the platform’s cliconf plugin  Sample: `"--- system:/running-config\n+++ session:/ansible_1599745461-session-config\n@@ -4,7 +4,7 @@\n !\n transceiver qsfp default-mode 4x10G\n !\n-hostname veos\n+hostname veos3\n !\n spanning-tree mode mstp"` |

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
