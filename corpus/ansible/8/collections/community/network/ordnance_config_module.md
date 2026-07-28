---
collection: ansible
version: "8"
title: "community.network.ordnance_config module – Manage Ordnance configuration sections"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ordnance_config_module.html
fetched_at: 2026-07-28T01:57:17+00:00
---
# community.network.ordnance_config module – Manage Ordnance configuration sections

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ordnance_config`.

- [Synopsis](ordnance_config_module.md#synopsis)
- [Parameters](ordnance_config_module.md#parameters)
- [Examples](ordnance_config_module.md#examples)
- [Return Values](ordnance_config_module.md#return-values)

## [Synopsis](ordnance_config_module.md#id1)

- Ordnance router configurations use a simple block indent file syntax for segmenting configuration into sections. This module provides an implementation for working with these configuration sections in a deterministic way.

Aliases: network.ordnance.ordnance_config

## [Parameters](ordnance_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **after**  string | The ordered set of commands to append to the end of the command stack if a change needs to be made. Just like with *before* this allows the playbook designer to append a set of commands to be executed after the command set. |
| **backup**  boolean | This argument will cause the module to create a full backup of the current `running-config` from the remote device before any changes are made. The backup file is written to the `backup` folder in the playbook root directory. If the directory does not exist, it is created.  **Choices:**   - `false` ← (default) - `true` |
| **before**  string | The ordered set of commands to push on to the command stack if a change needs to be made. This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system. |
| **config**  string | The `config` argument allows the playbook designer to supply the base configuration to be used to validate configuration changes necessary. If this argument is provided, the module will not download the running-config from the remote node. |
| **defaults**  boolean | This argument specifies whether or not to collect all defaults when getting the remote device running config. When enabled, the module will get the current config by issuing the command `show running-config all`.  **Choices:**   - `false` ← (default) - `true` |
| **lines**  aliases: commands  string | The ordered set of commands that should be configured in the section. The commands must be the exact same commands as found in the device running-config. Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser. |
| **match**  string | Instructs the module on the way to perform the matching of the set of commands against the current device config. If match is set to *line*, commands are matched line by line. If match is set to *strict*, command lines are matched with respect to position. If match is set to *exact*, command lines must be an equal match. Finally, if match is set to *none*, the module will not attempt to compare the source configuration with the running configuration on the remote device.  **Choices:**   - `"line"` ← (default) - `"strict"` - `"exact"` - `"none"` |
| **multiline_delimiter**  string | This argument is used when pushing a multiline configuration element to the Ordnance router. It specifies the character to use as the delimiting character. This only applies to the configuration action  **Default:** `"@"` |
| **parents**  string | The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against. If the parents argument is omitted, the commands are checked against the set of top level or global commands. |
| **replace**  string | Instructs the module on the way to perform the configuration on the device. If the replace argument is set to *line* then the modified lines are pushed to the device in configuration mode. If the replace argument is set to *block* then the entire command block is pushed to the device in configuration mode if any line is not correct.  **Choices:**   - `"line"` ← (default) - `"block"` |
| **save**  boolean | The `save` argument instructs the module to save the running- config to the startup-config at the conclusion of the module running. If check mode is specified, this argument is ignored.  **Choices:**   - `false` ← (default) - `true` |
| **src**  string | Specifies the source path to the file that contains the configuration or configuration template to load. The path to the source file can either be the full path on the Ansible control host or a relative path from the playbook or role root directory. This argument is mutually exclusive with *lines*, *parents*. |

## [Examples](ordnance_config_module.md#id3)

```yaml+jinja
---
# Note: examples below use the following provider dict to handle
#       transport and authentication to the node.
vars:
  cli:
    host: "{{ inventory_hostname }}"
    username: RouterName
    password: password
    transport: cli

---
- name: Configure top level configuration
  community.network.ordnance_config:
    lines: hostname {{ inventory_hostname }}
    provider: "{{ cli }}"

- name: Configure interface settings
  community.network.ordnance_config:
    lines:
      - description test interface
      - ip address 172.31.1.1 255.255.255.0
    parents: interface Ethernet1
    provider: "{{ cli }}"

- name: Configure bgp router
  community.network.ordnance_config:
    lines:
      - neighbor 1.1.1.1 remote-as 1234
      - network 10.0.0.0/24
    parents: router bgp 65001
    provider: "{{ cli }}"
```

## [Return Values](ordnance_config_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  **Returned:** when backup is yes  **Sample:** `"/playbooks/ansible/backup/ordnance_config.2016-07-16@22:28:34"` |
| **updates**  list / elements=string | The set of commands that will be pushed to the remote device  **Returned:** Only when commands is specified.  **Sample:** `["...", "..."]` |

### Authors

- Alexander Turner (@alexanderturner)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
