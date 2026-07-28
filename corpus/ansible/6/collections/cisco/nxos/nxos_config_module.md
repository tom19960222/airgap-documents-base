---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_config module – Manage Cisco NXOS configuration sections"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_config_module.html
fetched_at: 2026-07-27T17:01:44+00:00
---
# cisco.nxos.nxos_config module – Manage Cisco NXOS configuration sections

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/cisco/nxos) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_config`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_config_module.md#synopsis)
- [Parameters](nxos_config_module.md#parameters)
- [Notes](nxos_config_module.md#notes)
- [Examples](nxos_config_module.md#examples)
- [Return Values](nxos_config_module.md#return-values)

## [Synopsis](nxos_config_module.md#id1)

- Cisco NXOS configurations use a simple block indent file syntax for segmenting configuration into sections. This module provides an implementation for working with NXOS configuration sections in a deterministic way. This module works with either CLI or NXAPI transports.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **after**  list / elements=string | The ordered set of commands to append to the end of the command stack if a change needs to be made. Just like with *before* this allows the playbook designer to append a set of commands to be executed after the command set. |
| **backup**  boolean | This argument will cause the module to create a full backup of the current `running-config` from the remote device before any changes are made. If the `backup_options` value is not given, the backup file is written to the `backup` folder in the playbook root directory or role root directory, if playbook is part of an ansible role. If the directory does not exist, it is created.  Choices:   - `false` ← (default) - `true` |
| **backup_options**  dictionary | This is a dict object containing configurable options related to backup file path. The value of this option is read only when `backup` is set to *True*, if `backup` is set to *false* this option will be silently ignored. |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist it will be created and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given in that case a *backup* directory will be created in the current working directory and backup configuration will be copied in `filename` within *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the filename is not given it will be generated based on the hostname, current time and date in format defined by <hostname>_config.<current-date>@<current-time> |
| **before**  list / elements=string | The ordered set of commands to push on to the command stack if a change needs to be made. This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system. |
| **defaults**  boolean | The *defaults* argument will influence how the running-config is collected from the device. When the value is set to true, the command used to collect the running-config is append with the all keyword. When the value is set to false, the command is issued without the all keyword  Choices:   - `false` ← (default) - `true` |
| **diff_against**  string | When using the `ansible-playbook --diff` command line argument the module can generate diffs against different sources.  When this option is configure as *startup*, the module will return the diff of the running-config against the startup-config.  When this option is configured as *intended*, the module will return the diff of the running-config against the configuration provided in the `intended_config` argument.  When this option is configured as *running*, the module will return the before and after diff of the running-config with respect to any changes made to the device configuration.  Choices:   - `"startup"` - `"intended"` - `"running"` |
| **diff_ignore_lines**  list / elements=string | Use this argument to specify one or more lines that should be ignored during the diff. This is used for lines in the configuration that are automatically updated by the system. This argument takes a list of regular expressions or exact line matches. |
| **intended_config**  string | The `intended_config` provides the master configuration that the node should conform to and is used to check the final running-config against. This argument will not modify any settings on the remote device and is strictly used to check the compliance of the current device’s configuration against. When specifying this argument, the task should also modify the `diff_against` value and set it to *intended*. The configuration lines for this value should be similar to how it will appear if present in the running-configuration of the device including the indentation to ensure correct diff. |
| **lines**  aliases: commands  list / elements=string | The ordered set of commands that should be configured in the section. The commands must be the exact same commands as found in the device running-config to ensure idempotency and correct diff. Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser. |
| **match**  string | Instructs the module on the way to perform the matching of the set of commands against the current device config. If match is set to *line*, commands are matched line by line. If match is set to *strict*, command lines are matched with respect to position. If match is set to *exact*, command lines must be an equal match. Finally, if match is set to *none*, the module will not attempt to compare the source configuration with the running configuration on the remote device.  Choices:   - `"line"` ← (default) - `"strict"` - `"exact"` - `"none"` |
| **parents**  list / elements=string | The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against. If the parents argument is omitted, the commands are checked against the set of top level or global commands. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  Starting with Ansible 2.6 we recommend using `connection: httpapi` for NX-API.  This option will be removed in a release after 2022-06-01.  For more information please see the <https://docs.ansible.com/ansible/latest/network/user_guide/platform_nxos.html>.   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This is a common argument used for either *cli* or *nxapi* transports. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. This value applies to either *cli* or *nxapi*. The port value will default to the appropriate transport common port if none is provided in the task. (cli=22, http=80, https=443). |
| **ssh_keyfile**  string | Specifies the SSH key to use to authenticate the connection to the remote device. This argument is only used for the *cli* transport. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc). |
| **transport**  string | Configures the transport connection to use when connecting to the remote device. The transport argument supports connectivity to the device over cli (ssh) or nxapi.  Choices:   - `"cli"` ← (default) - `"nxapi"` |
| **use_proxy**  boolean | If `no`, the environment variables `http_proxy` and `https_proxy` will be ignored.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | Configures the *transport* to use SSL if set to `yes` only when the `transport=nxapi`, otherwise this value is ignored.  Choices:   - `false` ← (default) - `true` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates. If the transport argument is not nxapi, this value is ignored.  Choices:   - `false` ← (default) - `true` |
| **replace**  string | Instructs the module on the way to perform the configuration on the device. If the replace argument is set to *line* then the modified lines are pushed to the device in configuration mode. If the replace argument is set to *block* then the entire command block is pushed to the device in configuration mode if any line is not correct. replace *config* will only work for NX-OS versions that support `config replace`.  Choices:   - `"line"` ← (default) - `"block"` - `"config"` |
| **replace_src**  string | The *replace_src* argument provides path to the configuration file to load into the remote system. This argument is used to replace the entire config with a flat-file. This is used with argument *replace* with value *config*. This is mutually exclusive with the *lines* and *src* arguments. This argument will only work for NX-OS versions that support `config replace`. Use *nxos_file_copy* module to copy the flat file to remote device and then use the path with this argument. The configuration lines in the file should be similar to how it will appear if present in the running-configuration of the device including the indentation to ensure idempotency and correct diff. |
| **running_config**  aliases: config  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *running_config* argument allows the implementer to pass in the configuration to use as the base config for comparison. The configuration lines for this option should be similar to how it will appear if present in the running-configuration of the device including the indentation to ensure idempotency and correct diff. |
| **save_when**  string | When changes are made to the device running-configuration, the changes are not copied to non-volatile storage by default. Using this argument will change that before. If the argument is set to *always*, then the running-config will always be copied to the startup-config and the *modified* flag will always be set to True. If the argument is set to *modified*, then the running-config will only be copied to the startup-config if it has changed since the last save to startup-config. If the argument is set to *never*, the running-config will never be copied to the startup-config. If the argument is set to *changed*, then the running-config will only be copied to the startup-config if the task has made a change. *changed* was added in Ansible 2.6.  Choices:   - `"always"` - `"never"` ← (default) - `"modified"` - `"changed"` |
| **src**  path | The *src* argument provides a path to the configuration file to load into the remote system. The path can either be a full system path to the configuration file if the value starts with / or relative to the root of the implemented role or playbook. This argument is mutually exclusive with the *lines* and *parents* arguments. The configuration lines in the source file should be similar to how it will appear if present in the running-configuration of the device including indentation to ensure idempotency and correct diff. |

## [Notes](nxos_config_module.md#id3)

> **Note:**
>
> - Unsupported for Cisco MDS
> - Abbreviated commands are NOT idempotent, see <https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-do-the-config-modules-always-return-changed-true-with-abbreviated-commands>.
> - To ensure idempotency and correct diff the configuration lines in the relevant module options should be similar to how they appear if present in the running configuration on device including the indentation.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_config_module.md#id4)

```yaml+jinja
- name: configure top level configuration and save it
  cisco.nxos.nxos_config:
    lines: hostname {{ inventory_hostname }}
    save_when: modified

- name: diff the running-config against a provided config
  cisco.nxos.nxos_config:
    diff_against: intended
    intended_config: "{{ lookup('file', 'master.cfg') }}"

- cisco.nxos.nxos_config:
    lines:
    - 10 permit ip 192.0.2.1/32 any log
    - 20 permit ip 192.0.2.2/32 any log
    - 30 permit ip 192.0.2.3/32 any log
    - 40 permit ip 192.0.2.4/32 any log
    - 50 permit ip 192.0.2.5/32 any log
    parents: ip access-list test
    before: no ip access-list test
    match: exact

- cisco.nxos.nxos_config:
    lines:
    - 10 permit ip 192.0.2.1/32 any log
    - 20 permit ip 192.0.2.2/32 any log
    - 30 permit ip 192.0.2.3/32 any log
    - 40 permit ip 192.0.2.4/32 any log
    parents: ip access-list test
    before: no ip access-list test
    replace: block

- name: replace config with flat file
  cisco.nxos.nxos_config:
    replace_src: config.txt
    replace: config

- name: for idempotency, use full-form commands
  cisco.nxos.nxos_config:
    lines:
      # - shut
    - shutdown
    # parents: int eth1/1
    parents: interface Ethernet1/1

- name: configurable backup path
  cisco.nxos.nxos_config:
    backup: yes
    backup_options:
      filename: backup.cfg
      dir_path: /home/user
```

## [Return Values](nxos_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  Returned: when backup is yes  Sample: `"/playbooks/ansible/backup/nxos_config.2016-07-16@22:28:34"` |
| **commands**  list / elements=string | The set of commands that will be pushed to the remote device  Returned: always  Sample: `["hostname foo", "vlan 1", "name default"]` |
| **date**  string | The date extracted from the backup file name  Returned: when backup is yes  Sample: `"2016-07-16"` |
| **filename**  string | The name of the backup file  Returned: when backup is yes and filename is not specified in backup options  Sample: `"nxos_config.2016-07-16@22:28:34"` |
| **shortname**  string | The full path to the backup file excluding the timestamp  Returned: when backup is yes and filename is not specified in backup options  Sample: `"/playbooks/ansible/backup/nxos_config"` |
| **time**  string | The time extracted from the backup file name  Returned: when backup is yes  Sample: `"22:28:34"` |
| **updates**  list / elements=string | The set of commands that will be pushed to the remote device  Returned: always  Sample: `["hostname foo", "vlan 1", "name default"]` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
