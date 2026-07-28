---
collection: ansible
version: "6"
title: "cisco.ios.ios_config module – Module to manage configuration sections."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_config_module.html
fetched_at: 2026-07-27T16:55:10+00:00
---
# cisco.ios.ios_config module – Module to manage configuration sections.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/cisco/ios) (version 3.3.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_config`.

New in cisco.ios 1.0.0

- [Synopsis](ios_config_module.md#synopsis)
- [Parameters](ios_config_module.md#parameters)
- [Notes](ios_config_module.md#notes)
- [Examples](ios_config_module.md#examples)
- [Return Values](ios_config_module.md#return-values)

## [Synopsis](ios_config_module.md#id1)

- Cisco IOS configurations use a simple block indent file syntax for segmenting configuration into sections. This module provides an implementation for working with IOS configuration sections in a deterministic way.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](ios_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **after**  list / elements=string | The ordered set of commands to append to the end of the command stack if a change needs to be made. Just like with *before* this allows the playbook designer to append a set of commands to be executed after the command set. |
| **backup**  boolean | This argument will cause the module to create a full backup of the current `running-config` from the remote device before any changes are made. If the `backup_options` value is not given, the backup file is written to the `backup` folder in the playbook root directory or role root directory, if playbook is part of an ansible role. If the directory does not exist, it is created.  Choices:   - `false` ← (default) - `true` |
| **backup_options**  dictionary | This is a dict object containing configurable options related to backup file path. The value of this option is read only when `backup` is set to *yes*, if `backup` is set to *no* this option will be silently ignored. |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist it will be first created and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given in that case a *backup* directory will be created in the current working directory and backup configuration will be copied in `filename` within *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the filename is not given it will be generated based on the hostname, current time and date in format defined by <hostname>_config.<current-date>@<current-time> |
| **before**  list / elements=string | The ordered set of commands to push on to the command stack if a change needs to be made. This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system. |
| **defaults**  boolean | This argument specifies whether or not to collect all defaults when getting the remote device running config. When enabled, the module will get the current config by issuing the command `show running-config all`.  Choices:   - `false` ← (default) - `true` |
| **diff_against**  string | When using the `ansible-playbook --diff` command line argument the module can generate diffs against different sources.  When this option is configure as *startup*, the module will return the diff of the running-config against the startup-config.  When this option is configured as *intended*, the module will return the diff of the running-config against the configuration provided in the `intended_config` argument.  When this option is configured as *running*, the module will return the before and after diff of the running-config with respect to any changes made to the device configuration.  Choices:   - `"running"` - `"startup"` - `"intended"` |
| **diff_ignore_lines**  list / elements=string | Use this argument to specify one or more lines that should be ignored during the diff. This is used for lines in the configuration that are automatically updated by the system. This argument takes a list of regular expressions or exact line matches. |
| **intended_config**  string | The `intended_config` provides the master configuration that the node should conform to and is used to check the final running-config against. This argument will not modify any settings on the remote device and is strictly used to check the compliance of the current device’s configuration against. When specifying this argument, the task should also modify the `diff_against` value and set it to *intended*. The configuration lines for this value should be similar to how it will appear if present in the running-configuration of the device including the indentation to ensure correct diff. |
| **lines**  aliases: commands  list / elements=string | The ordered set of commands that should be configured in the section. The commands must be the exact same commands as found in the device running-config to ensure idempotency and correct diff. Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser. |
| **match**  string | Instructs the module on the way to perform the matching of the set of commands against the current device config. If match is set to *line*, commands are matched line by line. If match is set to *strict*, command lines are matched with respect to position. If match is set to *exact*, command lines must be an equal match. Finally, if match is set to *none*, the module will not attempt to compare the source configuration with the running configuration on the remote device.  Choices:   - `"line"` ← (default) - `"strict"` - `"exact"` - `"none"` |
| **multiline_delimiter**  string | This argument is used when pushing a multiline configuration element to the IOS device. It specifies the character to use as the delimiting character. This only applies to the configuration action.  Default: `"@"` |
| **parents**  list / elements=string | The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against. If the parents argument is omitted, the commands are checked against the set of top level or global commands. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>.   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **replace**  string | Instructs the module on the way to perform the configuration on the device. If the replace argument is set to *line* then the modified lines are pushed to the device in configuration mode. If the replace argument is set to *block* then the entire command block is pushed to the device in configuration mode if any line is not correct.  Choices:   - `"line"` ← (default) - `"block"` |
| **running_config**  aliases: config  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *running_config* argument allows the implementer to pass in the configuration to use as the base config for comparison. The configuration lines for this option should be similar to how it will appear if present in the running-configuration of the device including the indentation to ensure idempotency and correct diff. |
| **save_when**  string | When changes are made to the device running-configuration, the changes are not copied to non-volatile storage by default. Using this argument will change that before. If the argument is set to *always*, then the running-config will always be copied to the startup-config and the *modified* flag will always be set to True. If the argument is set to *modified*, then the running-config will only be copied to the startup-config if it has changed since the last save to startup-config. If the argument is set to *never*, the running-config will never be copied to the startup-config. If the argument is set to *changed*, then the running-config will only be copied to the startup-config if the task has made a change. *changed* was added in Ansible 2.5.  Choices:   - `"always"` - `"never"` ← (default) - `"modified"` - `"changed"` |
| **src**  string | Specifies the source path to the file that contains the configuration or configuration template to load. The path to the source file can either be the full path on the Ansible control host or a relative path from the playbook or role root directory. This argument is mutually exclusive with *lines*, *parents*. The configuration lines in the source file should be similar to how it will appear if present in the running-configuration of the device including the indentation to ensure idempotency and correct diff. |

## [Notes](ios_config_module.md#id3)

> **Note:**
>
> - Tested against IOS 15.6
> - Abbreviated commands are NOT idempotent, see <https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-do-the-config-modules-always-return-changed-true-with-abbreviated-commands>
> - To ensure idempotency and correct diff the configuration lines in the relevant module options should be similar to how they appear if present in the running configuration on device including the indentation.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](ios_config_module.md#id4)

```yaml+jinja
- name: configure top level configuration
  cisco.ios.ios_config:
    lines: hostname {{ inventory_hostname }}

- name: configure interface settings
  cisco.ios.ios_config:
    lines:
    - description test interface
    - ip address 172.31.1.1 255.255.255.0
    parents: interface Ethernet1

- name: configure ip helpers on multiple interfaces
  cisco.ios.ios_config:
    lines:
    - ip helper-address 172.26.1.10
    - ip helper-address 172.26.3.8
    parents: '{{ item }}'
  with_items:
  - interface Ethernet1
  - interface Ethernet2
  - interface GigabitEthernet1

- name: configure policer in Scavenger class
  cisco.ios.ios_config:
    lines:
    - conform-action transmit
    - exceed-action drop
    parents:
    - policy-map Foo
    - class Scavenger
    - police cir 64000

- name: load new acl into device
  cisco.ios.ios_config:
    lines:
    - 10 permit ip host 192.0.2.1 any log
    - 20 permit ip host 192.0.2.2 any log
    - 30 permit ip host 192.0.2.3 any log
    - 40 permit ip host 192.0.2.4 any log
    - 50 permit ip host 192.0.2.5 any log
    parents: ip access-list extended test
    before: no ip access-list extended test
    match: exact

- name: check the running-config against master config
  cisco.ios.ios_config:
    diff_against: intended
    intended_config: "{{ lookup('file', 'master.cfg') }}"

- name: check the startup-config against the running-config
  cisco.ios.ios_config:
    diff_against: startup
    diff_ignore_lines:
    - ntp clock .*

- name: save running to startup when modified
  cisco.ios.ios_config:
    save_when: modified

- name: for idempotency, use full-form commands
  cisco.ios.ios_config:
    lines:
      # - shut
    - shutdown
    # parents: int gig1/0/11
    parents: interface GigabitEthernet1/0/11

# Set boot image based on comparison to a group_var (version) and the version
# that is returned from the `ios_facts` module
- name: SETTING BOOT IMAGE
  cisco.ios.ios_config:
    lines:
    - no boot system
    - boot system flash bootflash:{{new_image}}
    host: '{{ inventory_hostname }}'
  when: ansible_net_version != version
- name: render a Jinja2 template onto an IOS device
  cisco.ios.ios_config:
    backup: yes
    src: ios_template.j2

- name: configurable backup path
  cisco.ios.ios_config:
    src: ios_template.j2
    backup: yes
    backup_options:
      filename: backup.cfg
      dir_path: /home/user

# Example ios_template.j2
# ip access-list extended test
#  permit ip host 192.0.2.1 any log
#  permit ip host 192.0.2.2 any log
#  permit ip host 192.0.2.3 any log
#  permit ip host 192.0.2.4 any log
```

## [Return Values](ios_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  Returned: when backup is yes  Sample: `"/playbooks/ansible/backup/ios_config.2016-07-16@22:28:34"` |
| **commands**  list / elements=string | The set of commands that will be pushed to the remote device  Returned: always  Sample: `["hostname foo", "router ospf 1", "router-id 192.0.2.1"]` |
| **date**  string | The date extracted from the backup file name  Returned: when backup is yes  Sample: `"2016-07-16"` |
| **filename**  string | The name of the backup file  Returned: when backup is yes and filename is not specified in backup options  Sample: `"ios_config.2016-07-16@22:28:34"` |
| **shortname**  string | The full path to the backup file excluding the timestamp  Returned: when backup is yes and filename is not specified in backup options  Sample: `"/playbooks/ansible/backup/ios_config"` |
| **time**  string | The time extracted from the backup file name  Returned: when backup is yes  Sample: `"22:28:34"` |
| **updates**  list / elements=string | The set of commands that will be pushed to the remote device  Returned: always  Sample: `["hostname foo", "router ospf 1", "router-id 192.0.2.1"]` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
