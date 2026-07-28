---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_imish_config module – Manage BIG-IP advanced routing configuration sections"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_imish_config_module.html
fetched_at: 2026-07-27T17:27:00+00:00
---
# f5networks.f5_modules.bigip_imish_config module – Manage BIG-IP advanced routing configuration sections

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_imish_config`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_imish_config_module.md#synopsis)
- [Parameters](bigip_imish_config_module.md#parameters)
- [Notes](bigip_imish_config_module.md#notes)
- [Examples](bigip_imish_config_module.md#examples)
- [Return Values](bigip_imish_config_module.md#return-values)

## [Synopsis](bigip_imish_config_module.md#id1)

- This module provides an implementation for working with advanced routing configuration sections in a deterministic way.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](bigip_imish_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **after**  list / elements=string | The ordered set of commands to append to the end of the command stack if a change needs to be made.  Just like with *before*, this allows the playbook designer to append a set of commands to be executed after the command set. |
| **allow_duplicates**  boolean  added in f5networks.f5_modules 1.2.0 | Allows duplicate commands to be sent to the device. This is to accommodate scenarios where address families are configured.  Only used with the `lines` parameter.  Choices:   - `false` ← (default) - `true` |
| **backup**  boolean | This argument will cause the module to create a full backup of the current `running-config` from the remote device before any changes are made.  The backup file is written to the `backup` folder in the playbook root directory or role root directory, if playbook is part of an Ansible role. If the directory does not exist, it is created.  Choices:   - `false` ← (default) - `true` |
| **backup_options**  dictionary | This is a dict object containing configurable options related to backup file path. The value of this option is read-only when `backup` is set to *yes*. If `backup` is set to *no*, this option will be silently ignored. |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist, it will be first created and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given, a *backup* directory will be created in the current working directory and backup configuration will be copied in `filename` within the *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the filename is not given, it will be generated based on the hostname, current time and date in the format defined by <hostname>_config.<current-date>@<current-time> |
| **before**  list / elements=string | The ordered set of commands to push onto the command stack if a change needs to be made.  This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes, without affecting how the set of commands are matched against the system. |
| **diff_against**  string | When using the `ansible-playbook --diff` command line argument, the module can generate diffs against different sources.  When this option is configured as *startup*, the module will return the diff of the running-config against the startup-config.  When this option is configured as *intended*, the module will return the diff of the running-config against the configuration provided in the `intended_config` argument.  When this option is configured as *running*, the module will return the before and after diff of the running-config with respect to any changes made to the device configuration.  Choices:   - `"startup"` ← (default) - `"intended"` - `"running"` |
| **diff_ignore_lines**  list / elements=string | Use this argument to specify one or more lines that should be ignored during the diff.  This is used for lines in the configuration that are automatically updated by the system.  This argument takes a list of regular expressions or exact line matches. |
| **intended_config**  string | The `intended_config` provides the master configuration the node should conform to and is used to check the final running-config against.  This argument will not modify any settings on the remote device and is strictly used to check the compliance of the current device’s configuration against.  When specifying this argument, the task should also modify the `diff_against` value and set it to *intended*. |
| **lines**  aliases: commands  list / elements=string | The ordered set of commands that should be configured in the section.  The commands must be the exact same as those found in the device running-config.  Be sure to note the configuration command syntax, as some commands are automatically modified by the device config parser. |
| **match**  string | Instructs the module on the way to perform the matching of the set of commands against the current device config.  If match is set to *line*, commands are matched line by line.  If match is set to *strict*, command lines are matched with respect to position.  If match is set to *exact*, command lines must be an equal match.  Finally, if match is set to *none*, the module will not attempt to compare the source configuration with the running configuration on the remote device.  Choices:   - `"line"` ← (default) - `"strict"` - `"exact"` - `"none"` |
| **parents**  list / elements=string | The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against.  If the `parents` argument is omitted, the commands are checked against the set of top level or global commands. |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **replace**  string | Instructs the module on the way to perform the configuration on the device.  If the replace argument is set to *line*, the modified lines are pushed to the device in configuration mode.  If the replace argument is set to *block*, the entire command block is pushed to the device in configuration mode if any line is not correct.  Choices:   - `"line"` ← (default) - `"block"` |
| **route_domain**  string | Route domain on which to manage the BGP configuration.  Default: `"0"` |
| **running_config**  aliases: config  string | By default, the module will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source.  There are times when you do not want to have the task get the current running-config for every task in a playbook.  The *running_config* argument allows the implementer to pass in the configuration to use as the base config for comparison. |
| **save_when**  string | When changes are made to the device running-configuration, the changes are not copied to non-volatile storage by default.  If the argument is set to *always*, the running-config will always be copied to the startup-config and the *modified* flag will always be set to `True`.  If the argument is set to *modified*, the running-config will only be copied to the startup-config if it has changed since the last save to startup-config.  If the argument is set to *never*, the running-config will never be copied to the startup-config.  If the argument is set to *changed*, the running-config will only be copied to the startup-config if the task has made a change.  Choices:   - `"always"` - `"never"` ← (default) - `"modified"` - `"changed"` |
| **src**  path | The *src* argument provides a path to the configuration file to load into the remote system.  The path can either be a full system path to the configuration file if the value starts with /, or relative to the root of the implemented role or playbook.  This argument is mutually exclusive with the *lines* and *parents* arguments. |

## [Notes](bigip_imish_config_module.md#id3)

> **Note:**
>
> - Abbreviated commands are NOT idempotent
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_imish_config_module.md#id4)

```yaml+jinja
- name: configure top level configuration and save it
  bigip_imish_config:
    lines: bfd slow-timer 2000
    save_when: modified
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: diff the running-config against a provided config
  bigip_imish_config:
    diff_against: intended
    intended_config: "{{ lookup('file', 'master.cfg') }}"
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Add config to a parent block
  bigip_imish_config:
    lines:
      - bgp graceful-restart restart-time 120
      - redistribute kernel route-map rhi
      - neighbor 10.10.10.11 remote-as 65000
      - neighbor 10.10.10.11 fall-over bfd
      - neighbor 10.10.10.11 remote-as 65000
      - neighbor 10.10.10.11 fall-over bfd
    parents: router bgp 64664
    match: exact
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Remove an existing acl before writing it
  bigip_imish_config:
    lines:
      - access-list 10 permit 20.20.20.20
      - access-list 10 permit 20.20.20.21
      - access-list 10 deny any
    before: no access-list 10
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: for idempotency, use full-form commands
  bigip_imish_config:
    lines:
      # - desc My interface
      - description My Interface
    # parents: int ANYCAST-P2P-2
    parents: interface ANYCAST-P2P-2
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: configurable backup path
  bigip_imish_config:
    lines: bfd slow-timer 2000
    backup: yes
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
    backup_options:
      filename: backup.cfg
      dir_path: /home/user
  delegate_to: localhost
```

## [Return Values](bigip_imish_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file.  Returned: when backup is yes  Sample: `"/playbooks/ansible/backup/bigip_imish_config.2016-07-16@22:28:34"` |
| **commands**  list / elements=string | The set of commands that will be pushed to the remote device.  Returned: always  Sample: `["interface ANYCAST-P2P-2", "neighbor 20.20.20.21 remote-as 65000", "neighbor 20.20.20.21 fall-over bfd"]` |
| **updates**  list / elements=string | The set of commands that will be pushed to the remote device.  Returned: always  Sample: `["interface ANYCAST-P2P-2", "neighbor 20.20.20.21 remote-as 65000", "neighbor 20.20.20.21 fall-over bfd"]` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
