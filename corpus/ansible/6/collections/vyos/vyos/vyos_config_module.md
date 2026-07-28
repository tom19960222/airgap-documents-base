---
collection: ansible
version: "6"
title: "vyos.vyos.vyos_config module – Manage VyOS configuration on remote device"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vyos/vyos/vyos_config_module.html
fetched_at: 2026-07-27T16:42:58+00:00
---
# vyos.vyos.vyos_config module – Manage VyOS configuration on remote device

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/vyos/vyos) (version 3.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_config`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_config_module.md#synopsis)
- [Parameters](vyos_config_module.md#parameters)
- [Notes](vyos_config_module.md#notes)
- [Examples](vyos_config_module.md#examples)
- [Return Values](vyos_config_module.md#return-values)

## [Synopsis](vyos_config_module.md#id1)

- This module provides configuration file management of VyOS devices. It provides arguments for managing both the configuration file and state of the active configuration. All configuration statements are based on `set` and `delete` commands in the device configuration.

## [Parameters](vyos_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backup**  boolean | The `backup` argument will backup the current devices active configuration to the Ansible control host prior to making any changes. If the `backup_options` value is not given, the backup file will be located in the backup folder in the playbook root directory or role root directory, if playbook is part of an ansible role. If the directory does not exist, it is created.  Choices:   - `false` ← (default) - `true` |
| **backup_options**  dictionary | This is a dict object containing configurable options related to backup file path. The value of this option is read only when `backup` is set to *yes*, if `backup` is set to *no* this option will be silently ignored. |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist it will be first created and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given in that case a *backup* directory will be created in the current working directory and backup configuration will be copied in `filename` within *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the filename is not given it will be generated based on the hostname, current time and date in format defined by <hostname>_config.<current-date>@<current-time> |
| **comment**  string | Allows a commit description to be specified to be included when the configuration is committed. If the configuration is not changed or committed, this argument is ignored.  Default: `"configured by vyos_config"` |
| **config**  string | The `config` argument specifies the base configuration to use to compare against the desired configuration. If this value is not specified, the module will automatically retrieve the current active configuration from the remote device. The configuration lines in the option value should be similar to how it will appear if present in the running-configuration of the device including indentation to ensure idempotency and correct diff. |
| **lines**  list / elements=string | The ordered set of commands that should be configured in the section. The commands must be the exact same commands as found in the device running-config as found in the device running-config to ensure idempotency and correct diff. Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser. |
| **match**  string | The `match` argument controls the method used to match against the current active configuration. By default, the desired config is matched against the active config and the deltas are loaded. If the `match` argument is set to `none` the active configuration is ignored and the configuration is always loaded.  Choices:   - `"line"` ← (default) - `"none"` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **save**  boolean | The `save` argument controls whether or not changes made to the active configuration are saved to disk. This is independent of committing the config. When set to True, the active configuration is saved.  Choices:   - `false` ← (default) - `true` |
| **src**  path | The `src` argument specifies the path to the source config file to load. The source config file can either be in bracket format or set format. The source file can include Jinja2 template variables. The configuration lines in the source file should be similar to how it will appear if present in the running-configuration of the device including indentation to ensure idempotency and correct diff. |

## [Notes](vyos_config_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).
> - To ensure idempotency and correct diff the configuration lines in the relevant module options should be similar to how they appear if present in the running configuration on device including the indentation.
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](vyos_config_module.md#id4)

```yaml+jinja
- name: configure the remote device
  vyos.vyos.vyos_config:
    lines:
    - set system host-name {{ inventory_hostname }}
    - set service lldp
    - delete service dhcp-server

- name: backup and load from file
  vyos.vyos.vyos_config:
    src: vyos.cfg
    backup: yes

- name: render a Jinja2 template onto the VyOS router
  vyos.vyos.vyos_config:
    src: vyos_template.j2

- name: for idempotency, use full-form commands
  vyos.vyos.vyos_config:
    lines:
      # - set int eth eth2 description 'OUTSIDE'
    - set interface ethernet eth2 description 'OUTSIDE'

- name: configurable backup path
  vyos.vyos.vyos_config:
    backup: yes
    backup_options:
      filename: backup.cfg
      dir_path: /home/user
```

## [Return Values](vyos_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  Returned: when backup is yes  Sample: `"/playbooks/ansible/backup/vyos_config.2016-07-16@22:28:34"` |
| **commands**  list / elements=string | The list of configuration commands sent to the device  Returned: always  Sample: `["...", "..."]` |
| **date**  string | The date extracted from the backup file name  Returned: when backup is yes  Sample: `"2016-07-16"` |
| **filename**  string | The name of the backup file  Returned: when backup is yes and filename is not specified in backup options  Sample: `"vyos_config.2016-07-16@22:28:34"` |
| **filtered**  list / elements=string | The list of configuration commands removed to avoid a load failure  Returned: always  Sample: `["...", "..."]` |
| **shortname**  string | The full path to the backup file excluding the timestamp  Returned: when backup is yes and filename is not specified in backup options  Sample: `"/playbooks/ansible/backup/vyos_config"` |
| **time**  string | The time extracted from the backup file name  Returned: when backup is yes  Sample: `"22:28:34"` |

### Authors

- Nathaniel Case (@Qalthos)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
[Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
