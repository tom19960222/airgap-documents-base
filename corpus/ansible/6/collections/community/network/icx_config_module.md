---
collection: ansible
version: "6"
title: "community.network.icx_config module – Manage configuration sections of Ruckus ICX 7000 series switches"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/icx_config_module.html
fetched_at: 2026-07-27T17:18:41+00:00
---
# community.network.icx_config module – Manage configuration sections of Ruckus ICX 7000 series switches

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
> To use it in a playbook, specify: `community.network.icx_config`.

- [Synopsis](icx_config_module.md#synopsis)
- [Parameters](icx_config_module.md#parameters)
- [Notes](icx_config_module.md#notes)
- [Examples](icx_config_module.md#examples)
- [Return Values](icx_config_module.md#return-values)

## [Synopsis](icx_config_module.md#id1)

- Ruckus ICX configurations use a simple block indent file syntax for segmenting configuration into sections. This module provides an implementation for working with ICX configuration sections in a deterministic way.

## [Parameters](icx_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **after**  list / elements=string | The ordered set of commands to append to the end of the command stack if a change needs to be made. Just like with *before* this allows the playbook designer to append a set of commands to be executed after the command set. |
| **backup**  boolean | This argument will cause the module to create a full backup of the current `running-config` from the remote device before any changes are made. The backup file is written to the `backup` folder in the playbook root directory or role root directory, if playbook is part of an ansible role. If the directory does not exist, it is created.  Choices:   - `false` ← (default) - `true` |
| **before**  list / elements=string | The ordered set of commands to push on to the command stack if a change needs to be made. This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system. |
| **defaults**  boolean | This argument specifies whether or not to collect all defaults when getting the remote device running config. When enabled, the module will get the current config by issuing the command `show running-config all`.  Choices:   - `false` ← (default) - `true` |
| **diff_against**  string | When using the `ansible-playbook --diff` command line argument the module can generate diffs against different sources.  When this option is configure as *startup*, the module will return the diff of the running-config against the configuration.  When this option is configured as *intended*, the module will return the diff of the running-config against the configuration provided in the `intended_config` argument.  When this option is configured as *running*, the module will return the before and after diff of the running-config with respect to any changes made to the device configuration.  Choices:   - `"running"` - `"startup"` - `"intended"` |
| **diff_ignore_lines**  list / elements=string | Use this argument to specify one or more lines that should be ignored during the diff. This is used for lines in the configuration that are automatically updated by the system. This argument takes a list of regular expressions or exact line matches. |
| **intended_config**  string | The `intended_config` provides the master configuration that the node should conform to and is used to check the final running-config against. This argument will not modify any settings on the remote device and is strictly used to check the compliance of the current device’s configuration against. When specifying this argument, the task should also modify the `diff_against` value and set it to *intended*. |
| **lines**  aliases: commands  list / elements=string | The ordered set of commands that should be configured in the section. The commands must be the exact same commands as found in the device running-config. Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser. |
| **match**  string | Instructs the module on the way to perform the matching of the set of commands against the current device config. If match is set to *line*, commands are matched line by line. If match is set to *strict*, command lines are matched with respect to position. If match is set to *exact*, command lines must be an equal match. Finally, if match is set to *none*, the module will not attempt to compare the source configuration with the running configuration on the remote device.  Choices:   - `"line"` ← (default) - `"strict"` - `"exact"` - `"none"` |
| **multiline_delimiter**  string | This argument is used when pushing a multiline configuration element to the ICX device. It specifies the character to use as the delimiting character. This only applies to the configuration action.  Default: `"@"` |
| **parents**  list / elements=string | The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against. If the parents argument is omitted, the commands are checked against the set of top level or global commands. |
| **replace**  string | Instructs the module on the way to perform the configuration on the device. If the replace argument is set to *line* then the modified lines are pushed to the device in configuration mode. If the replace argument is set to *block* then the entire command block is pushed to the device in configuration mode if any line is not correct.  Choices:   - `"line"` ← (default) - `"block"` |
| **running_config**  aliases: config  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *running_config* argument allows the implementer to pass in the configuration to use as the base config for comparison. |
| **save_when**  string | When changes are made to the device running-configuration, the changes are not copied to non-volatile storage by default. Using this argument will change that before. If the argument is set to *always*, then the running-config will always be copied to the start-up configuration and the *modified* flag will always be set to True. If the argument is set to *modified*, then the running-config will only be copied to the start-up configuration if it has changed since the last save to configuration. If the argument is set to *never*, the running-config will never be copied to the configuration. If the argument is set to *changed*, then the running-config will only be copied to the configuration if the task has made a change.  Choices:   - `"always"` - `"never"` ← (default) - `"modified"` - `"changed"` |
| **src**  string | Specifies the source path to the file that contains the configuration or configuration template to load. The path to the source file can either be the full path on the Ansible control host or a relative path from the playbook or role root directory. This argument is mutually exclusive with *lines*, *parents*. |

## [Notes](icx_config_module.md#id3)

> **Note:**
>
> - Tested against ICX 10.1.
> - For information on using ICX platform, see [the ICX OS Platform Options guide](user_guide/platform_icx.md).

## [Examples](icx_config_module.md#id4)

```yaml+jinja
- name: Configure top level configuration
  community.network.icx_config:
    lines: hostname {{ inventory_hostname }}

- name: Configure interface settings
  community.network.icx_config:
    lines:
      - port-name test string
      - ip address 172.31.1.1 255.255.255.0
    parents: interface ethernet 1/1/2

- name: Configure ip helpers on multiple interfaces
  community.network.icx_config:
    lines:
      - ip helper-address 172.26.1.10
      - ip helper-address 172.26.3.8
    parents: "{{ item }}"
  with_items:
    - interface ethernet 1/1/2
    - interface ethernet 1/1/3

- name: Load new acl into device
  community.network.icx_config:
    lines:
      - permit ip host 192.0.2.1 any log
      - permit ip host 192.0.2.2 any log
      - permit ip host 192.0.2.3 any log
      - permit ip host 192.0.2.4 any log
    parents: ip access-list extended test
    before: no ip access-list extended test
    match: exact

- name: Check the running-config against master config
  community.network.icx_config:
    diff_against: intended
    intended_config: "{{ lookup('file', 'master.cfg') }}"

- name: Check the configuration against the running-config
  community.network.icx_config:
    diff_against: startup
    diff_ignore_lines:
      - ntp clock .*

- name: For idempotency, use full-form commands
  community.network.icx_config:
    lines:
      # - en
      - enable
    # parents: int eth1/0/11
    parents: interface ethernet 1/1/2

# Set boot image based on comparison to a group_var (version) and the version
# that is returned from the `icx_facts` module
- name: SETTING BOOT IMAGE
  community.network.icx_config:
    lines:
      - no boot system
      - boot system flash bootflash:{{new_image}}
    host: "{{ inventory_hostname }}"
  when: ansible_net_version != version

- name: Render template onto an ICX device
  community.network.icx_config:
    backup: yes
    src: "{{ lookup('file', 'config.j2') }}"
```

## [Return Values](icx_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  Returned: when backup is yes  Sample: `"/playbooks/ansible/backup/icx_config.2016-07-16@22:28:34"` |
| **commands**  list / elements=string | The set of commands that will be pushed to the remote device  Returned: always  Sample: `["hostname foo", "router ospf 1", "router-id 192.0.2.1"]` |
| **updates**  list / elements=string | The set of commands that will be pushed to the remote device  Returned: always  Sample: `["hostname foo", "router ospf 1", "router-id 192.0.2.1"]` |

### Authors

- Ruckus Wireless (@Commscope)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
