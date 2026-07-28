---
collection: ansible
version: "6"
title: "splunk.es.splunk_adaptive_response_notable_events module – Manage Adaptive Responses notable events resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/splunk/es/splunk_adaptive_response_notable_events_module.html
fetched_at: 2026-07-28T00:19:59+00:00
---
# splunk.es.splunk_adaptive_response_notable_events module – Manage Adaptive Responses notable events resource module

> **Note:**
>
> This module is part of the [splunk.es collection](https://galaxy.ansible.com/splunk/es) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install splunk.es`.
>
> To use it in a playbook, specify: `splunk.es.splunk_adaptive_response_notable_events`.

New in splunk.es 2.1.0

- [Synopsis](splunk_adaptive_response_notable_events_module.md#synopsis)
- [Parameters](splunk_adaptive_response_notable_events_module.md#parameters)
- [Examples](splunk_adaptive_response_notable_events_module.md#examples)
- [Return Values](splunk_adaptive_response_notable_events_module.md#return-values)

## [Synopsis](splunk_adaptive_response_notable_events_module.md#id1)

- This module allows for creation, deletion, and modification of Splunk Enterprise Security Notable Event Adaptive Responses that are associated with a correlation search
- Tested against Splunk Enterprise Server 8.2.3

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](splunk_adaptive_response_notable_events_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Configure file and directory monitoring on the system |
| **correlation_search_name**  string / required | Name of correlation search to associate this notable event adaptive response with |
| **default_owner**  string | Default owner of the notable event, if unset it will default to Splunk System Defaults |
| **default_status**  string | Default status of the notable event, if unset it will default to Splunk System Defaults  Choices:   - `"unassigned"` - `"new"` - `"in progress"` - `"pending"` - `"resolved"` - `"closed"` |
| **description**  string | Description of the notable event, this will populate the description field for the web console |
| **drilldown_earliest_offset**  string | Set the amount of time before the triggering event to search for related events. For example, 2h. Use ‘$info_min_time$’ to set the drill-down time to match the earliest time of the search  Default: `"$info_min_time$"` |
| **drilldown_latest_offset**  string | Set the amount of time after the triggering event to search for related events. For example, 1m. Use ‘$info_max_time$’ to set the drill-down time to match the latest time of the search  Default: `"$info_max_time$"` |
| **drilldown_name**  string | Name for drill down search, Supports variable substitution with fields from the matching event. |
| **drilldown_search**  string | Drill down search, Supports variable substitution with fields from the matching event. |
| **extract_artifacts**  dictionary | Assets and identities to be extracted |
| **asset**  list / elements=string | list of assets to extract, select any one or many of the available choices  defaults to all available choices  Choices:   - `"src"` - `"dest"` - `"dvc"` - `"orig_host"` |
| **file**  list / elements=string | list of files to extract |
| **identity**  list / elements=string | list of identity fields to extract, select any one or many of the available choices  defaults to ‘user’ and ‘src_user’  Choices:   - `"user"` - `"src_user"` - `"src_user_id"` - `"user_id"` - `"src_user_role"` - `"user_role"` - `"vendor_account"` |
| **url**  list / elements=string | list of URLs to extract |
| **investigation_profiles**  list / elements=string | Investigation profile to associate the notable event with. |
| **name**  string | Name of notable event |
| **next_steps**  list / elements=string | List of adaptive responses that should be run next  Describe next steps and response actions that an analyst could take to address this threat. |
| **recommended_actions**  list / elements=string | List of adaptive responses that are recommended to be run next  Identifying Recommended Adaptive Responses will highlight those actions for the analyst when looking at the list of response actions available, making it easier to find them among the longer list of available actions. |
| **security_domain**  string | Splunk Security Domain  Choices:   - `"access"` - `"endpoint"` - `"network"` - `"threat"` ← (default) - `"identity"` - `"audit"` |
| **severity**  string | Severity rating  Choices:   - `"informational"` - `"low"` - `"medium"` - `"high"` ← (default) - `"critical"` - `"unknown"` |
| **running_config**  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *running_config* argument allows the implementer to pass in the configuration to use as the base config for comparison. This value of this option should be the output received from device by executing command. |
| **state**  string | The state the configuration should be left in  Choices:   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"gathered"` |

## [Examples](splunk_adaptive_response_notable_events_module.md#id3)

```yaml+jinja
# Using gathered
# --------------

- name: Gather adaptive response notable events config
  splunk.es.splunk_adaptive_response_notable_events:
    config:
      - correlation_search_name: Ansible Test
      - correlation_search_name: Ansible Test 2
    state: gathered

# RUN output:
# -----------

# "gathered": [
#     {
#         "correlation_search_name": "Ansible Test",
#         "description": "test notable event",
#         "drilldown_earliest_offset": "$info_min_time$",
#         "drilldown_latest_offset": "$info_max_time$",
#         "drilldown_name": "test_drill_name",
#         "drilldown_search": "test_drill",
#         "extract_artifacts": {
#             "asset": [
#                 "src",
#                 "dest",
#                 "dvc",
#                 "orig_host"
#             ],
#             "identity": [
#                 "src_user",
#                 "user",
#                 "src_user_id",
#                 "src_user_role",
#                 "user_id",
#                 "user_role",
#                 "vendor_account"
#             ]
#         },
#         "investigation_profiles": [
#             "test profile 1",
#             "test profile 2",
#             "test profile 3"
#         ],
#         "next_steps": [
#             "makestreams",
#             "nbtstat",
#             "nslookup"
#         ],
#         "name": "ansible_test_notable",
#         "recommended_actions": [
#             "email",
#             "logevent",
#             "makestreams",
#             "nbtstat"
#         ],
#         "security_domain": "threat",
#         "severity": "high"
#     },
#     { } # there is no configuration associated with "/var"
# ]

# Using merged
# ------------

- name: Example to add config
  splunk.es.splunk_adaptive_response_notable_events:
    config:
      - correlation_search_name: Ansible Test
        description: test notable event
        drilldown_earliest_offset: $info_min_time$
        drilldown_latest_offset: $info_max_time$
        extract_artifacts:
            asset:
              - src
              - dest
            identity:
              - src_user
              - user
              - src_user_id
        next_steps:
        - makestreams
        name: ansible_test_notable
        recommended_actions:
        - email
        - logevent
        security_domain: threat
        severity: high
    state: merged

# RUN output:
# -----------

# "after": [
#     {
#         "correlation_search_name": "Ansible Test",
#         "description": "test notable event",
#         "drilldown_earliest_offset": "$info_min_time$",
#         "drilldown_latest_offset": "$info_max_time$",
#         "drilldown_name": "test_drill_name",
#         "drilldown_search": "test_drill",
#         "extract_artifacts": {
#             "asset": [
#                 "src",
#                 "dest",
#                 "dvc",
#                 "orig_host"
#             ],
#             "identity": [
#                 "src_user",
#                 "user",
#                 "src_user_id",
#                 "src_user_role",
#                 "user_id",
#                 "user_role",
#                 "vendor_account"
#             ]
#         },
#         "investigation_profiles": [
#             "test profile 1",
#             "test profile 2",
#             "test profile 3"
#         ],
#         "next_steps": [
#             "makestreams",
#             "nbtstat",
#             "nslookup"
#         ],
#         "name": "ansible_test_notable",
#         "recommended_actions": [
#             "email",
#             "logevent",
#             "makestreams",
#             "nbtstat"
#         ],
#         "security_domain": "threat",
#         "severity": "high"
#     }
# ],
# "before": [],

# Using replaced
# --------------

- name: Example to Replace the config
  splunk.es.splunk_adaptive_response_notable_events:
    config:
      - correlation_search_name: Ansible Test
        description: test notable event
        drilldown_earliest_offset: $info_min_time$
        drilldown_latest_offset: $info_max_time$
        extract_artifacts:
            asset:
              - src
              - dest
            identity:
              - src_user
              - user
              - src_user_id
        next_steps:
        - makestreams
        name: ansible_test_notable
        recommended_actions:
        - email
        - logevent
        security_domain: threat
        severity: high
    state: replaced

# RUN output:
# -----------

# "after": [
#     {
#         "correlation_search_name": "Ansible Test",
#         "description": "test notable event",
#         "drilldown_earliest_offset": "$info_min_time$",
#         "drilldown_latest_offset": "$info_max_time$",
#         "extract_artifacts": {
#             "asset": [
#                 "src",
#                 "dest"
#             ],
#             "identity": [
#                 "src_user",
#                 "user",
#                 "src_user_id"
#             ]
#         },
#         "next_steps": [
#             "makestreams"
#         ],
#         "name": "ansible_test_notable",
#         "recommended_actions": [
#             "email",
#             "logevent"
#         ],
#         "security_domain": "threat",
#         "severity": "high"
#     }
# ],
# "before": [
#     {
#         "correlation_search_name": "Ansible Test",
#         "description": "test notable event",
#         "drilldown_earliest_offset": "$info_min_time$",
#         "drilldown_latest_offset": "$info_max_time$",
#         "drilldown_name": "test_drill_name",
#         "drilldown_search": "test_drill",
#         "extract_artifacts": {
#             "asset": [
#                 "src",
#                 "dest",
#                 "dvc",
#                 "orig_host"
#             ],
#             "identity": [
#                 "src_user",
#                 "user",
#                 "src_user_id",
#                 "src_user_role",
#                 "user_id",
#                 "user_role",
#                 "vendor_account"
#             ]
#         },
#         "investigation_profiles": [
#             "test profile 1",
#             "test profile 2",
#             "test profile 3"
#         ],
#         "next_steps": [
#             "makestreams",
#             "nbtstat",
#             "nslookup"
#         ],
#         "name": "ansible_test_notable",
#         "recommended_actions": [
#             "email",
#             "logevent",
#             "makestreams",
#             "nbtstat"
#         ],
#         "security_domain": "threat",
#         "severity": "high"
#     }
# ],

# USING DELETED
# -------------

- name: Example to remove the config
  splunk.es.splunk_adaptive_response_notable_events:
    config:
      - correlation_search_name: Ansible Test
    state: deleted

# RUN output:
# -----------

# "after": [],
# "before": [
#     {
#         "correlation_search_name": "Ansible Test",
#         "description": "test notable event",
#         "drilldown_earliest_offset": "$info_min_time$",
#         "drilldown_latest_offset": "$info_max_time$",
#         "drilldown_name": "test_drill_name",
#         "drilldown_search": "test_drill",
#         "extract_artifacts": {
#             "asset": [
#                 "src",
#                 "dest",
#                 "dvc",
#                 "orig_host"
#             ],
#             "identity": [
#                 "src_user",
#                 "user",
#                 "src_user_id",
#                 "src_user_role",
#                 "user_id",
#                 "user_role",
#                 "vendor_account"
#             ]
#         },
#         "investigation_profiles": [
#             "test profile 1",
#             "test profile 2",
#             "test profile 3"
#         ],
#         "next_steps": [
#             "makestreams",
#             "nbtstat",
#             "nslookup"
#         ],
#         "name": "ansible_test_notable",
#         "recommended_actions": [
#             "email",
#             "logevent",
#             "makestreams",
#             "nbtstat"
#         ],
#         "security_domain": "threat",
#         "severity": "high"
#     }
# ]
```

## [Return Values](splunk_adaptive_response_notable_events_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |
| **gathered**  dictionary | Facts about the network resource gathered from the remote device as structured data.  Returned: when state is *gathered*  Sample: `"This output will always be in the same format as the module argspec.\n"` |

### Authors

- Ansible Security Automation Team (@pranav-bhatt) <<https://github.com/ansible-security>>

### Collection links

[Issue Tracker](https://github.com/ansible-collections/splunk.es/issues)
[Repository (Sources)](https://github.com/ansible-collections/splunk.es)
