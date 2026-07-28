---
collection: ansible
version: "8"
title: "ansible.netcommon.grpc_get module – Fetch configuration/state data from gRPC enabled target hosts."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/grpc_get_module.html
fetched_at: 2026-07-28T01:09:06+00:00
---
# ansible.netcommon.grpc_get module – Fetch configuration/state data from gRPC enabled target hosts.

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ui/repo/published/ansible/netcommon/) (version 5.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
> You need further requirements to be able to use this module,
> see [Requirements](grpc_get_module.md#ansible-collections-ansible-netcommon-grpc-get-module-requirements) for details.
>
> To use it in a playbook, specify: `ansible.netcommon.grpc_get`.

New in ansible.netcommon 3.1.0

- [Synopsis](grpc_get_module.md#synopsis)
- [Requirements](grpc_get_module.md#requirements)
- [Parameters](grpc_get_module.md#parameters)
- [Notes](grpc_get_module.md#notes)
- [Examples](grpc_get_module.md#examples)
- [Return Values](grpc_get_module.md#return-values)

## [Synopsis](grpc_get_module.md#id1)

- gRPC is a high performance, open-source universal RPC framework.
- This module allows the user to fetch configuration and state data from gRPC enabled devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](grpc_get_module.md#id2)

The below requirements are needed on the host that executes this module.

- grpcio
- protobuf

## [Parameters](grpc_get_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **command**  string | The option specifies the command to be executed on the target host and return the response in result. This option is supported if the gRPC target host supports executing CLI command over the gRPC connection. |
| **data_type**  string | The type of data that should be fetched from the target host. The value depends on the capability of the gRPC server running on target host. The values can be *config*, *oper* etc. based on what is supported by the gRPC server. By default it will return both configuration and operational state data in response. |
| **display**  string | Encoding scheme to use when serializing output from the device. The encoding scheme value depends on the capability of the gRPC server running on the target host. The values can be *json*, *text* etc. |
| **section**  aliases: filter  string | This option specifies the string which acts as a filter to restrict the portions of the data to be retrieved from the target host device. If this option is not specified the entire configuration or state data is returned in response provided it is supported by target host. |

## [Notes](grpc_get_module.md#id4)

> **Note:**
>
> - This module requires the gRPC system service be enabled on the target host being managed.
> - This module supports the use of connection=ansible.netcommon.grpc.
> - This module requires the value of ‘ansible_network_os or grpc_type’ configuration option (refer ansible.netcommon.grpc connection plugin documentation) be defined as an inventory variable.
> - Tested against iosxrv 9k version 6.1.2.

## [Examples](grpc_get_module.md#id5)

```yaml+jinja
- name: Get bgp configuration data
  grpc_get:
    section:
      Cisco-IOS-XR-ip-static-cfg:router-static:
        - null
- name: run cli command
  grpc_get:
    command: 'show version'
    display: text
```

## [Return Values](grpc_get_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  list / elements=string | A dictionary representing a JSON-formatted response, if the response is a valid json string  **Returned:** when the device response is valid JSON  **Sample:** `["[{\n    \"Cisco-IOS-XR-ip-static-cfg:router-static\": {\n        \"default-vrf\": {\n            \"address-family\": {\n                \"vrfipv4\": {\n                    \"vrf-unicast\": {\n                        \"vrf-prefixes\": {\n                            \"vrf-prefix\": [\n                                {\n                                    \"prefix\": \"0.0.0.0\"", "\n                                    \"prefix-length\": 0", "\n                                    \"vrf-route\": {\n                                        \"vrf-next-hop-table\": {\n                                            \"vrf-next-hop-interface-name-next-hop-address\": [\n                                                {\n                                                    \"interface-name\": \"MgmtEth0/RP0/CPU0/0\"", "\n                                                    \"next-hop-address\": \"10.0.2.2\"\n                                                }\n                                            ]\n                                        }\n                                    }\n                                }\n                            ]\n                        }\n                    }\n                }\n            }\n        }\n    }\n}]\n"]` |
| **stdout**  string | The raw string containing configuration or state data received from the gRPC server.  **Returned:** always apart from low-level errors (such as action plugin)  **Sample:** `"..."` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  **Returned:** always apart from low-level errors (such as action plugin)  **Sample:** `["...", "..."]` |

### Authors

- Ganesh Nalawade (@ganeshrn)
- Gomathi Selvi S (@GomathiselviS)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
