---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_telemetry module – TELEMETRY resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_telemetry_module.html
fetched_at: 2026-07-27T17:02:28+00:00
---
# cisco.nxos.nxos_telemetry module – TELEMETRY resource module

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
> To use it in a playbook, specify: `cisco.nxos.nxos_telemetry`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_telemetry_module.md#synopsis)
- [Parameters](nxos_telemetry_module.md#parameters)
- [Notes](nxos_telemetry_module.md#notes)
- [Examples](nxos_telemetry_module.md#examples)
- [Return Values](nxos_telemetry_module.md#return-values)

## [Synopsis](nxos_telemetry_module.md#id1)

- Manages Telemetry Monitoring Service (TMS) configuration

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_telemetry_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | The provided configuration |
| **certificate**  dictionary | Certificate SSL/TLS and hostname values.  Value must be a dict defining values for keys (key and hostname). |
| **hostname**  string | Certificate hostname |
| **key**  string | Certificate key |
| **compression**  string | Destination profile compression method.  Choices:   - `"gzip"` |
| **destination_groups**  list / elements=any | List of telemetry destination groups. |
| **destination**  dictionary | Group destination ipv4, port, protocol and encoding values.  Value must be a dict defining values for keys (ip, port, protocol, encoding). |
| **encoding**  string | Destination group encoding.  Choices:   - `"GPB"` - `"JSON"` |
| **ip**  string | Destination group IP address. |
| **port**  integer | Destination group port number. |
| **protocol**  string | Destination group protocol.  Choices:   - `"HTTP"` - `"TCP"` - `"UDP"` - `"gRPC"` |
| **id**  string | Destination group identifier.  Value must be an integer or string representing the destination group identifier. |
| **sensor_groups**  list / elements=any | List of telemetry sensor groups. |
| **data_source**  string | Telemetry data source.  Choices:   - `"NX-API"` - `"DME"` - `"YANG"` |
| **id**  string | Sensor group identifier.  Value must be a integer or a string representing the sensor group identifier. |
| **path**  dictionary | Telemetry sensor path.  Value must be a dict defining values for keys (name, depth, filter_condition, query_condition).  Mandatory Keys (name)  Optional Keys (depth, filter_condition, query_condition) |
| **depth**  string | Sensor group depth. |
| **filter_condition**  string | Sensor group filter condition. |
| **name**  string | Sensor group path name. |
| **query_condition**  string | Sensor group query condition. |
| **source_interface**  string | Destination profile source interface.  Valid value is a str representing the source interface name. |
| **subscriptions**  list / elements=any | List of telemetry subscriptions. |
| **destination_group**  string | Associated destination group. |
| **id**  string | Subscription identifier.  Value must be an integer or string representing the subscription identifier. |
| **sensor_group**  dictionary | Associated sensor group.  Value must be a dict defining values for keys (id, sample_interval). |
| **id**  string | Associated sensor group id. |
| **sample_interval**  integer | Associated sensor group id sample interval. |
| **vrf**  string | Destination profile vrf.  Valid value is a str representing the vrf name. |
| **state**  string | Final configuration state  Choices:   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"gathered"` |

## [Notes](nxos_telemetry_module.md#id3)

> **Note:**
>
> - Supported on N9k Version 7.0(3)I7(5) and later.
> - Unsupported for Cisco MDS

## [Examples](nxos_telemetry_module.md#id4)

```yaml+jinja
# Using deleted
# This action will delete all telemetry configuration on the device

- name: Delete Telemetry Configuration
  cisco.nxos.nxos_telemetry:
    state: deleted

# Using merged
# This action will merge telemetry configuration defined in the playbook with
# telemetry configuration that is already on the device.

- name: Merge Telemetry Configuration
  cisco.nxos.nxos_telemetry:
    config:
      certificate:
        key: /bootflash/server.key
        hostname: localhost
      compression: gzip
      source_interface: Ethernet1/1
      vrf: management
      destination_groups:
      - id: 2
        destination:
          ip: 192.168.0.2
          port: 50001
          protocol: gRPC
          encoding: GPB
      - id: 55
        destination:
          ip: 192.168.0.55
          port: 60001
          protocol: gRPC
          encoding: GPB
      sensor_groups:
      - id: 1
        data_source: NX-API
        path:
          name: '"show lldp neighbors detail"'
          depth: 0
      - id: 55
        data_source: DME
        path:
          name: sys/ch
          depth: unbounded
          filter_condition: ne(eqptFt.operSt,"ok")
      subscriptions:
      - id: 5
        destination_group: 55
        sensor_group:
          id: 1
          sample_interval: 1000
      - id: 6
        destination_group: 2
        sensor_group:
          id: 55
          sample_interval: 2000
    state: merged

# Using replaced
# This action will replace telemetry configuration on the device with the
# telemetry configuration defined in the playbook.

- name: Override Telemetry Configuration
  cisco.nxos.nxos_telemetry:
    config:
      certificate:
        key: /bootflash/server.key
        hostname: localhost
      compression: gzip
      source_interface: Ethernet1/1
      vrf: management
      destination_groups:
      - id: 2
        destination:
          ip: 192.168.0.2
          port: 50001
          protocol: gRPC
          encoding: GPB
      subscriptions:
      - id: 5
        destination_group: 55
    state: replaced
```

## [Return Values](nxos_telemetry_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The configuration as structured data after module completion.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration as structured data prior to module invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["command 1", "command 2", "command 3"]` |

### Authors

- Mike Wiebe (@mikewiebe)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
