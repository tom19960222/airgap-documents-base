---
collection: ansible
version: "6"
title: "community.network.edgeos_config module – Manage EdgeOS configuration on remote device"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/edgeos_config_module.html
fetched_at: 2026-07-27T17:18:25+00:00
---
# community.network.edgeos_config module – Manage EdgeOS configuration on remote device

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
> To use it in a playbook, specify: `community.network.edgeos_config`.

- [Synopsis](edgeos_config_module.md#synopsis)
- [Parameters](edgeos_config_module.md#parameters)
- [Notes](edgeos_config_module.md#notes)
- [Examples](edgeos_config_module.md#examples)
- [Return Values](edgeos_config_module.md#return-values)

## [Synopsis](edgeos_config_module.md#id1)

- This module provides configuration file management of EdgeOS devices. It provides arguments for managing both the configuration file and state of the active configuration. All configuration statements are based on `set` and `delete` commands in the device configuration.
- This is a network module and requires the `connection: network_cli` in order to work properly.
- For more information please see the [Network Guide](getting_started/index.md).

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](edgeos_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backup**  boolean | The `backup` argument will backup the current device’s active configuration to the Ansible control host prior to making any changes. If the `backup_options` value is not given, the backup file will be located in the backup folder in the playbook root directory or role root directory if the playbook is part of an ansible role. If the directory does not exist, it is created.  Choices:   - `false` ← (default) - `true` |
| **backup_options**  dictionary | This is a dict object containing configurable options related to backup file path. The value of this option is read only when `backup` is set to *yes*, if `backup` is set to *no* this option will be silently ignored. |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist it will be first created and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given in that case a *backup* directory will be created in the current working directory and backup configuration will be copied in `filename` within *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the filename is not given it will be generated based on the hostname, current time and date in format defined by <hostname>_config.<current-date>@<current-time> |
| **comment**  string | Allows a commit description to be specified to be included when the configuration is committed. If the configuration is not changed or committed, this argument is ignored.  Default: `"configured by edgeos_config"` |
| **config**  string | The `config` argument specifies the base configuration to use to compare against the desired configuration. If this value is not specified, the module will automatically retrieve the current active configuration from the remote device. |
| **lines**  list / elements=string | The ordered set of configuration lines to be managed and compared with the existing configuration on the remote device. |
| **match**  string | The `match` argument controls the method used to match against the current active configuration. By default, the desired config is matched against the active config and the deltas are loaded. If the `match` argument is set to `none` the active configuration is ignored and the configuration is always loaded.  Choices:   - `"line"` ← (default) - `"none"` |
| **save**  boolean | The `save` argument controls whether or not changes made to the active configuration are saved to disk. This is independent of committing the config. When set to `True`, the active configuration is saved.  Choices:   - `false` ← (default) - `true` |
| **src**  string | The `src` argument specifies the path to the source config file to load. The source config file can either be in bracket format or set format. The source file can include Jinja2 template variables. |

## [Notes](edgeos_config_module.md#id3)

> **Note:**
>
> - Tested against EdgeOS 1.9.7
> - Setting `ANSIBLE_PERSISTENT_COMMAND_TIMEOUT` to 30 is recommended since the save command can take longer than the default of 10 seconds on some EdgeOS hardware.

## [Examples](edgeos_config_module.md#id4)

```yaml+jinja
- name: Configure the remote device
  community.network.edgeos_config:
    lines:
      - set system host-name {{ inventory_hostname }}
      - set service lldp
      - delete service dhcp-server

- name: Backup and load from file
  community.network.edgeos_config:
    src: edgeos.cfg
    backup: yes

- name: Configurable backup path
  community.network.edgeos_config:
    src: edgeos.cfg
    backup: yes
    backup_options:
      filename: backup.cfg
      dir_path: /home/user
```

## [Return Values](edgeos_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  Returned: when backup is yes  Sample: `"/playbooks/ansible/backup/edgeos_config.2016-07-16@22:28:34"` |
| **commands**  list / elements=string | The list of configuration commands sent to the device  Returned: always  Sample: `["...", "..."]` |

### Authors

- Nathaniel Case (@Qalthos)
- Sam Doran (@samdoran)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
