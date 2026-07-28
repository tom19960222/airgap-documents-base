---
collection: ansible
version: "6"
title: "cisco.asa.asa_config module – Manage configuration sections on Cisco ASA devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/asa/asa_config_module.html
fetched_at: 2026-07-27T16:50:47+00:00
---
# cisco.asa.asa_config module – Manage configuration sections on Cisco ASA devices

> **Note:**
>
> This module is part of the [cisco.asa collection](https://galaxy.ansible.com/cisco/asa) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.asa`.
>
> To use it in a playbook, specify: `cisco.asa.asa_config`.

New in cisco.asa 1.0.0

- [Synopsis](asa_config_module.md#synopsis)
- [Parameters](asa_config_module.md#parameters)
- [Notes](asa_config_module.md#notes)
- [Examples](asa_config_module.md#examples)
- [Return Values](asa_config_module.md#return-values)

## [Synopsis](asa_config_module.md#id1)

- Cisco ASA configurations use a simple block indent file syntax for segmenting configuration into sections. This module provides an implementation for working with ASA configuration sections in a deterministic way.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](asa_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **after**  list / elements=string | The ordered set of commands to append to the end of the command stack if a change needs to be made. Just like with *before* this allows the playbook designer to append a set of commands to be executed after the command set. |
| **authorize**  boolean | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli` and `become: yes`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` - `true` |
| **backup**  boolean | This argument will cause the module to create a full backup of the current `running-config` from the remote device before any changes are made. If the `backup_options` value is not given, the backup file is written to the `backup` folder in the playbook root directory. If the directory does not exist, it is created.  Choices:   - `false` ← (default) - `true` |
| **backup_options**  dictionary | This is a dict object containing configurable options related to backup file path. The value of this option is read only when `backup` is set to *yes*, if `backup` is set to *no* this option will be silently ignored. |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist it will be first created and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given in that case a *backup* directory will be created in the current working directory and backup configuration will be copied in `filename` within *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the filename is not given it will be generated based on the hostname, current time and date in format defined by <hostname>_config.<current-date>@<current-time> |
| **before**  list / elements=string | The ordered set of commands to push on to the command stack if a change needs to be made. This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system. |
| **config**  string | The `config` argument allows the playbook designer to supply the base configuration to be used to validate configuration changes necessary. If this argument is provided, the module will not download the running-config from the remote node. |
| **context**  string | Specifies which context to target if you are running in the ASA in multiple context mode. Defaults to the current context you login to. |
| **defaults**  boolean | This argument specifies whether or not to collect all defaults when getting the remote device running config. When enabled, the module will get the current config by issuing the command `show running-config all`.  Choices:   - `false` ← (default) - `true` |
| **lines**  aliases: commands  list / elements=string | The ordered set of commands that should be configured in the section. The commands must be the exact same commands as found in the device running-config. Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser. |
| **match**  string | Instructs the module on the way to perform the matching of the set of commands against the current device config. If match is set to *line*, commands are matched line by line. If match is set to *strict*, command lines are matched with respect to position. If match is set to *exact*, command lines must be an equal match. Finally, if match is set to *none*, the module will not attempt to compare the source configuration with the running configuration on the remote device.  Choices:   - `"line"` ← (default) - `"strict"` - `"exact"` - `"none"` |
| **parents**  list / elements=string | The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against. If the parents argument is omitted, the commands are checked against the set of top level or global commands. |
| **passwords**  boolean | This argument specifies to include passwords in the config when retrieving the running-config from the remote device. This includes passwords related to VPN endpoints. This argument is mutually exclusive with *defaults*.  Choices:   - `false` - `true` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies idle timeout in seconds for the connection, in seconds. Useful if the console freezes before continuing. For example when saving configurations. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **replace**  string | Instructs the module on the way to perform the configuration on the device. If the replace argument is set to *line* then the modified lines are pushed to the device in configuration mode. If the replace argument is set to *block* then the entire command block is pushed to the device in configuration mode if any line is not correct  Choices:   - `"line"` ← (default) - `"block"` |
| **save**  boolean | The `save` argument instructs the module to save the running- config to the startup-config at the conclusion of the module running. If check mode is specified, this argument is ignored.  Choices:   - `false` ← (default) - `true` |
| **save_when**  string  added in cisco.asa 1.1.0 | When changes are made to the device running-configuration, the changes are not copied to non-volatile storage by default. Using this argument will change that before. If the argument is set to *always*, then the running-config will always be copied to the startup-config and the *modified* flag will always be set to True. If the argument is set to *modified*, then the running-config will only be copied to the startup-config if it has changed since the last save to startup-config. If the argument is set to *never*, the running-config will never be copied to the startup-config. If the argument is set to *changed*, then the running-config will only be copied to the startup-config if the task has made a change. *changed* was added in Ansible 2.5.  Choices:   - `"always"` - `"never"` ← (default) - `"modified"` - `"changed"` |
| **src**  path | Specifies the source path to the file that contains the configuration or configuration template to load. The path to the source file can either be the full path on the Ansible control host or a relative path from the playbook or role root directory. This argument is mutually exclusive with *lines*, *parents*. |

## [Notes](asa_config_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](asa_config_module.md#id4)

```yaml+jinja
- cisco.asa.asa_config:
    lines:
    - network-object host 10.80.30.18
    - network-object host 10.80.30.19
    - network-object host 10.80.30.20
    parents: [object-group network OG-MONITORED-SERVERS]
    provider: '{{ cli }}'

- cisco.asa.asa_config:
    host: '{{ inventory_hostname }}'
    lines:
    - message-length maximum client auto
    - message-length maximum 512
    match: line
    parents: [policy-map type inspect dns PM-DNS, parameters]
    authorize: yes
    auth_pass: cisco
    username: admin
    password: cisco
    context: ansible

- cisco.asa.asa_config:
    lines:
    - ikev1 pre-shared-key MyS3cretVPNK3y
    parents: tunnel-group 1.1.1.1 ipsec-attributes
    passwords: yes
    provider: '{{ cli }}'

- name: attach ASA acl on interface vlan13/nameif cloud13
  cisco.asa.asa_config:
    lines:
    - access-group cloud-acl_access_in in interface cloud13
    provider: '{{ cli }}'

- name: configure ASA (>=9.2) default BGP
  cisco.asa.asa_config:
    lines:
    - bgp log-neighbor-changes
    - bgp bestpath compare-routerid
    provider: '{{ cli }}'
    parents:
    - router bgp 65002
  register: bgp
  when: bgp_default_config is defined
- name: configure ASA (>=9.2) BGP neighbor in default/single context mode
  cisco.asa.asa_config:
    lines:
    - bgp router-id {{ bgp_router_id }}
    - neighbor {{ bgp_neighbor_ip }} remote-as {{ bgp_neighbor_as }}
    - neighbor {{ bgp_neighbor_ip }} description {{ bgp_neighbor_name }}
    provider: '{{ cli }}'
    parents:
    - router bgp 65002
    - address-family ipv4 unicast
  register: bgp
  when: bgp_neighbor_as is defined
- name: configure ASA interface with standby
  cisco.asa.asa_config:
    lines:
    - description my cloud interface
    - nameif cloud13
    - security-level 50
    - ip address 192.168.13.1 255.255.255.0 standby 192.168.13.2
    provider: '{{ cli }}'
    parents: [interface Vlan13]
  register: interface
- name: Show changes to interface from task above
  debug:
    var: interface

- name: configurable backup path
  cisco.asa.asa_config:
    lines:
    - access-group cloud-acl_access_in in interface cloud13
    provider: '{{ cli }}'
    backup: yes
    backup_options:
      filename: backup.cfg
      dir_path: /home/user

- name: save running to startup when modified
  cisco.asa.asa_config:
    save_when: modified
```

## [Return Values](asa_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  Returned: when backup is yes  Sample: `"/playbooks/ansible/backup/asa_config.2016-07-16@22:28:34"` |
| **updates**  list / elements=string | The set of commands that will be pushed to the remote device  Returned: always  Sample: `["...", "..."]` |

### Authors

- Peter Sprygada (@privateip), Patrick Ogenstad (@ogenstad)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.asa/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.asa)
