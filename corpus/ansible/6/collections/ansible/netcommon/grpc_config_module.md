---
collection: ansible
version: "6"
title: "ansible.netcommon.grpc_config module – Fetch configuration/state data from gRPC enabled target hosts."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/grpc_config_module.html
fetched_at: 2026-07-27T16:44:27+00:00
---
# ansible.netcommon.grpc_config module – Fetch configuration/state data from gRPC enabled target hosts.

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
> You need further requirements to be able to use this module,
> see [Requirements](grpc_config_module.md#ansible-collections-ansible-netcommon-grpc-config-module-requirements) for details.
>
> To use it in a playbook, specify: `ansible.netcommon.grpc_config`.

New in ansible.netcommon 3.1.0

- [Synopsis](grpc_config_module.md#synopsis)
- [Requirements](grpc_config_module.md#requirements)
- [Parameters](grpc_config_module.md#parameters)
- [Notes](grpc_config_module.md#notes)
- [Examples](grpc_config_module.md#examples)
- [Return Values](grpc_config_module.md#return-values)

## [Synopsis](grpc_config_module.md#id1)

- gRPC is a high performance, open-source universal RPC framework.
- This module allows the user to append configs to an existing configuration in a gRPC enabled devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](grpc_config_module.md#id2)

The below requirements are needed on the host that executes this module.

- grpcio
- protobuf

## [Parameters](grpc_config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **backup**  boolean | This argument will cause the module to create a full backup of the current `running-config` from the remote device before any changes are made. If the `backup_options` value is not given, the backup file is written to the `backup` folder in the playbook root directory or role root directory, if playbook is part of an ansible role. If the directory does not exist, it is created.  Choices:   - `false` ← (default) - `true` |
| **backup_options**  dictionary | This is a dict object containing configurable options related to backup file path. The value of this option is read only when `backup` is set to *yes*, if `backup` is set to *no* this option will be silently ignored. |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist it will be first created and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given in that case a *backup* directory will be created in the current working directory and backup configuration will be copied in `filename` within *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the filename is not given it will be generated based on the hostname, current time and date in format defined by <hostname>_config.<current-date>@<current-time> |
| **config**  string | This option specifies the string which acts as a filter to restrict the portions of the data to be retrieved from the target host device. If this option is not specified the entire configuration or state data is returned in response provided it is supported by target host. |
| **state**  string | action to be performed |

## [Notes](grpc_config_module.md#id4)

> **Note:**
>
> - This module requires the gRPC system service be enabled on the target host being managed.
> - This module supports the use of connection=connection=ansible.netcommon.grpc
> - This module requires the value of ‘ansible_network_os’ or ‘grpc_type’ configuration option (refer ansible.netcommon.grpc connection plugin documentation) be defined as an inventory variable.
> - Tested against iosxrv 9k version 6.1.2.

## [Examples](grpc_config_module.md#id5)

```yaml+jinja
- name: Merge static route config
  ansible.netcommon.grpc_config:
    config:
      Cisco-IOS-XR-ip-static-cfg:router-static:
        default-vrf:
          address-family:
            vrfipv4:
              vrf-unicast:
                vrf-prefixes:
                  vrf-prefix:
                    - prefix: "1.2.3.6"
                      prefix-length: 32
                      vrf-route:
                        vrf-next-hop-table:
                          vrf-next-hop-next-hop-address:
                            - next-hop-address: "10.0.2.2"

    state: merged

- name: Merge bgp config
  ansible.netcommon.grpc_config:
    config: "{{ lookup('file', 'bgp.json')  }}"
    state: merged

- name: Find diff
  diff: True
  ansible.netcommon.grpc_config:
    config: "{{ lookup('file', 'bgp_start.yml')  }}"
    state: merged

- name: Backup running config
  ansible.netcommon.grpc_config:
     backup: yes
```

## [Return Values](grpc_config_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  Returned: when backup is yes  Sample: `"/playbooks/ansible/backup/config.2022-07-16@22:28:34"` |
| **diff**  dictionary | If –diff option in enabled while running, the before and after configuration change are returned as part of before and after key.  Returned: when diff is enabled |
| **stdout**  string | The raw string containing response object received from the gRPC server.  Returned: error mesage, when failure happens. empty , when the operation is successful  Sample: `"..."` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  Returned: always apart from low-level errors (such as action plugin)  Sample: `["...", "..."]` |

### Authors

- Gomathi Selvi S (@GomathiselviS)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
