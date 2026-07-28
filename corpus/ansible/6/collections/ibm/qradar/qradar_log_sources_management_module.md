---
collection: ansible
version: "6"
title: "ibm.qradar.qradar_log_sources_management module – Qradar Log Sources Management resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ibm/qradar/qradar_log_sources_management_module.html
fetched_at: 2026-07-27T17:50:16+00:00
---
# ibm.qradar.qradar_log_sources_management module – Qradar Log Sources Management resource module

> **Note:**
>
> This module is part of the [ibm.qradar collection](https://galaxy.ansible.com/ibm/qradar) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.qradar`.
>
> To use it in a playbook, specify: `ibm.qradar.qradar_log_sources_management`.

New in ibm.qradar 2.1.0

- [Synopsis](qradar_log_sources_management_module.md#synopsis)
- [Parameters](qradar_log_sources_management_module.md#parameters)
- [Examples](qradar_log_sources_management_module.md#examples)
- [Return Values](qradar_log_sources_management_module.md#return-values)

## [Synopsis](qradar_log_sources_management_module.md#id1)

- This module allows for addition, deletion, or modification of Log Sources in QRadar

## [Parameters](qradar_log_sources_management_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of Qradar Log Sources options |
| **average_eps**  integer | The average events per second (EPS) rate of the log source over the last 60 seconds. |
| **coalesce_events**  boolean | If events collected by this log source are coalesced based on common properties, the condition is set to ‘true’. If each individual event is stored, then the condition is set to ‘false’.  Choices:   - `false` - `true` |
| **description**  string | Description of log source |
| **enabled**  boolean | If the log source is enabled, the condition is set to ‘true’; otherwise, the condition is set to ‘false’.  Choices:   - `false` - `true` |
| **gateway**  boolean | If the log source is configured as a gateway, the condition is set to ‘true’; otherwise, the condition is set to ‘false’. A gateway log source is a stand-alone protocol configuration. The log source receives no events itself, and serves as a host for a protocol configuration that retrieves event data to feed other log sources. It acts as a “gateway” for events from multiple systems to enter the event pipeline.  Choices:   - `false` - `true` |
| **group_ids**  list / elements=string | The set of log source group IDs this log source is a member of. Each ID must correspond to an existing log source group. |
| **identifier**  string | Log Source Identifier (Typically IP Address or Hostname of log source) |
| **internal**  boolean | If the log source is internal (when the log source type is defined as internal), the condition is set to ‘true’.  Choices:   - `false` - `true` |
| **language_id**  integer | The language of the events that are being processed by this log source. Must correspond to an existing log source language. Individual log source types can support only a subset of all available log source languages, as indicated by the supported_language_ids field of the log source type structure |
| **name**  string | Name of Log Source |
| **protocol_parameters**  list / elements=dictionary | The set of protocol parameters  If not provided module will set the protocol parameters by itself  Note, parameter will come to use mostly in case when facts are gathered and fired with some modifications to params or in case of round trip scenarios. |
| **id**  integer | The ID of the protocol type. |
| **name**  string | The unique name of the protocol type. |
| **value**  string | The allowed protocol value. |
| **protocol_type_id**  integer | Type of protocol by id, as defined in QRadar Log Source Types Documentation |
| **requires_deploy**  boolean | Set to ‘true’ if you need to deploy changes to enable the log source for use; otherwise, set to ‘false’ if the log source is already active.  Choices:   - `false` - `true` |
| **status**  dictionary | The status of the log source. |
| **last_updated**  integer | last_updated |
| **messages**  string | last_updated |
| **status**  string | last_updated |
| **store_event_payload**  boolean | If the payloads of events that are collected by this log source are stored, the condition is set to ‘true’. If only the normalized event records are stored, then the condition is set to ‘false’.  Choices:   - `false` - `true` |
| **target_event_collector_id**  integer | The ID of the event collector where the log source sends its data. The ID must correspond to an existing event collector. |
| **type_id**  integer | The type of the log source. Must correspond to an existing log source type. |
| **type_name**  string | Type of resource by name |
| **state**  string | The state the configuration should be left in  The state *gathered* will get the module API configuration from the device and transform it into structured data in the format as per the module argspec and the value is returned in the *gathered* key within the result.  Choices:   - `"merged"` - `"replaced"` - `"gathered"` - `"deleted"` |

## [Examples](qradar_log_sources_management_module.md#id3)

```yaml+jinja
# Using MERGED state
# -------------------

- name: Add Snort n Apache log sources to IBM QRadar
  ibm.qradar.qradar_log_sources_management:
    config:
      - name: "Snort logs"
        type_name: "Snort Open Source IDS"
        description: "Snort IDS remote logs from rsyslog"
        identifier: "192.0.2.1"
      - name: "Apache HTTP Server logs"
        type_name: "Apache HTTP Server"
        description: "Apache HTTP Server remote logs from rsyslog"
        identifier: "198.51.100.1"
    state: merged

# RUN output:
# -----------

#   qradar_log_sources_management:
#     after:
#     - auto_discovered: false
#       average_eps: 0
#       coalesce_events: true
#       creation_date: 1654727311444
#       credibility: 5
#       description: Snort IDS remote logs from rsyslog
#       enabled: true
#       gateway: false
#       group_ids:
#       - 0
#       id: 181
#       internal: false
#       language_id: 1
#       last_event_time: 0
#       log_source_extension_id: null
#       modified_date: 1654727311444
#       name: Snort logs
#       protocol_parameters:
#       - id: 1
#         name: incomingPayloadEncoding
#         value: UTF-8
#       - id: 0
#         name: identifier
#         value: 192.0.2.1
#       protocol_type_id: 0
#       requires_deploy: true
#       status:
#         last_updated: 0
#         messages: null
#         status: NA
#       store_event_payload: true
#       target_event_collector_id: 7
#       type_id: 2
#       wincollect_external_destination_ids: null
#       wincollect_internal_destination_id: null
#     - auto_discovered: false
#       average_eps: 0
#       coalesce_events: true
#       creation_date: 1654727311462
#       credibility: 5
#       description: Apache HTTP Server remote logs from rsyslog
#       enabled: true
#       gateway: false
#       group_ids:
#       - 0
#       id: 182
#       internal: false
#       language_id: 1
#       last_event_time: 0
#       log_source_extension_id: null
#       modified_date: 1654727311462
#       name: Apache HTTP Server logs
#       protocol_parameters:
#       - id: 1
#         name: incomingPayloadEncoding
#         value: UTF-8
#       - id: 0
#         name: identifier
#         value: 198.51.100.1
#       protocol_type_id: 0
#       requires_deploy: true
#       status:
#         last_updated: 0
#         messages: null
#         status: NA
#       store_event_payload: true
#       target_event_collector_id: 7
#       type_id: 10
#       wincollect_external_destination_ids: null
#       wincollect_internal_destination_id: null
#     before: []

# Using REPLACED state
# --------------------

- name: Replace existing Log sources to IBM QRadar
  ibm.qradar.qradar_log_sources_management:
    state: replaced
    config:
      - name: "Apache HTTP Server logs"
        type_name: "Apache HTTP Server"
        description: "REPLACED Apache HTTP Server remote logs from rsyslog"
        identifier:  "192.0.2.1"

# RUN output:
# -----------

#   qradar_log_sources_management:
#     after:
#     - auto_discovered: false
#       average_eps: 0
#       coalesce_events: true
#       creation_date: 1654727944017
#       credibility: 5
#       description: REPLACED Apache HTTP Server remote logs from rsyslog
#       enabled: true
#       gateway: false
#       group_ids:
#       - 0
#       id: 183
#       internal: false
#       language_id: 1
#       last_event_time: 0
#       log_source_extension_id: null
#       modified_date: 1654727944017
#       name: Apache HTTP Server logs
#       protocol_parameters:
#       - id: 1
#         name: incomingPayloadEncoding
#         value: UTF-8
#       - id: 0
#         name: identifier
#         value: 192.0.2.1
#       protocol_type_id: 0
#       requires_deploy: true
#       status:
#         last_updated: 0
#         messages: null
#         status: NA
#       store_event_payload: true
#       target_event_collector_id: 7
#       type_id: 10
#       wincollect_external_destination_ids: null
#       wincollect_internal_destination_id: null
#     before:
#     - auto_discovered: false
#       average_eps: 0
#       coalesce_events: true
#       creation_date: 1654727311462
#       credibility: 5
#       description: Apache HTTP Server remote logs from rsyslog
#       enabled: true
#       gateway: false
#       group_ids:
#       - 0
#       id: 182
#       internal: false
#       language_id: 1
#       last_event_time: 0
#       log_source_extension_id: null
#       modified_date: 1654727311462
#       name: Apache HTTP Server logs
#       protocol_parameters:
#       - name: identifier
#         value: 198.51.100.1
#       - name: incomingPayloadEncoding
#         value: UTF-8
#       protocol_type_id: 0
#       requires_deploy: true
#       status:
#         last_updated: 0
#         messages: null
#         status: NA
#       store_event_payload: true
#       target_event_collector_id: 7
#       type_id: 10
#       wincollect_external_destination_ids: null
#       wincollect_internal_destination_id: null

# Using GATHERED state
# --------------------

- name: Gather Snort n Apache log source from IBM QRadar
  ibm.qradar.qradar_log_sources_management:
    config:
      - name: "Snort logs"
      - name: "Apache HTTP Server logs"
    state: gathered

# RUN output:
# -----------

# gathered:
#   - auto_discovered: false
#     average_eps: 0
#     coalesce_events: true
#     creation_date: 1654727311444
#     credibility: 5
#     description: Snort IDS remote logs from rsyslog
#     enabled: true
#     gateway: false
#     group_ids:
#     - 0
#     id: 181
#     internal: false
#     language_id: 1
#     last_event_time: 0
#     log_source_extension_id: null
#     modified_date: 1654728103340
#     name: Snort logs
#     protocol_parameters:
#     - id: 0
#       name: identifier
#       value: 192.0.2.1
#     - id: 1
#       name: incomingPayloadEncoding
#       value: UTF-8
#     protocol_type_id: 0
#     requires_deploy: true
#     status:
#       last_updated: 0
#       messages: null
#       status: NA
#     store_event_payload: true
#     target_event_collector_id: 7
#     type_id: 2
#     wincollect_external_destination_ids: null
#     wincollect_internal_destination_id: null
#   - auto_discovered: false
#     average_eps: 0
#     coalesce_events: true
#     creation_date: 1654727944017
#     credibility: 5
#     description: Apache HTTP Server remote logs from rsyslog
#     enabled: true
#     gateway: false
#     group_ids:
#     - 0
#     id: 183
#     internal: false
#     language_id: 1
#     last_event_time: 0
#     log_source_extension_id: null
#     modified_date: 1654728103353
#     name: Apache HTTP Server logs
#     protocol_parameters:
#     - id: 0
#       name: identifier
#       value: 192.0.2.1
#     - id: 1
#       name: incomingPayloadEncoding
#       value: UTF-8
#     protocol_type_id: 0
#     requires_deploy: true
#     status:
#       last_updated: 0
#       messages: null
#       status: NA
#     store_event_payload: true
#     target_event_collector_id: 7
#     type_id: 10
#     wincollect_external_destination_ids: null
#     wincollect_internal_destination_id: null

- name: TO Gather ALL log sources from IBM QRadar
  tags: gather_log_all
  ibm.qradar.qradar_log_sources_management:
    state: gathered

# Using DELETED state
# -------------------

- name: Delete Snort n Apache log source from IBM QRadar
  ibm.qradar.qradar_log_sources_management:
    config:
      - name: "Snort logs"
      - name: "Apache HTTP Server logs"
    state: deleted

# RUN output:
# -----------

#   qradar_log_sources_management:
#     after: []
#     before:
#     - auto_discovered: false
#       average_eps: 0
#       coalesce_events: true
#       creation_date: 1654727311444
#       credibility: 5
#       description: Snort IDS remote logs from rsyslog
#       enabled: true
#       gateway: false
#       group_ids:
#       - 0
#       id: 181
#       internal: false
#       language_id: 1
#       last_event_time: 0
#       log_source_extension_id: null
#       modified_date: 1654728103340
#       name: Snort logs
#       protocol_parameters:
#       - id: 0
#         name: identifier
#         value: 192.0.2.1
#       - id: 1
#         name: incomingPayloadEncoding
#         value: UTF-8
#       protocol_type_id: 0
#       requires_deploy: true
#       status:
#         last_updated: 0
#         messages: null
#         status: NA
#       store_event_payload: true
#       target_event_collector_id: 7
#       type_id: 2
#       wincollect_external_destination_ids: null
#       wincollect_internal_destination_id: null
#     - auto_discovered: false
#       average_eps: 0
#       coalesce_events: true
#       creation_date: 1654727944017
#       credibility: 5
#       description: Apache HTTP Server remote logs from rsyslog
#       enabled: true
#       gateway: false
#       group_ids:
#       - 0
#       id: 183
#       internal: false
#       language_id: 1
#       last_event_time: 0
#       log_source_extension_id: null
#       modified_date: 1654728103353
#       name: Apache HTTP Server logs
#       protocol_parameters:
#       - id: 0
#         name: identifier
#         value: 192.0.2.1
#       - id: 1
#         name: incomingPayloadEncoding
#         value: UTF-8
#       protocol_type_id: 0
#       requires_deploy: true
#       status:
#         last_updated: 0
#         messages: null
#         status: NA
#       store_event_payload: true
#       target_event_collector_id: 7
#       type_id: 10
#       wincollect_external_destination_ids: null
#       wincollect_internal_destination_id: null
```

## [Return Values](qradar_log_sources_management_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |

### Authors

- Ansible Security Automation Team (@justjais) <<https://github.com/ansible-security>>

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ibm.qradar/issues)
[Repository (Sources)](https://github.com/ansible-collections/ibm.qradar)
