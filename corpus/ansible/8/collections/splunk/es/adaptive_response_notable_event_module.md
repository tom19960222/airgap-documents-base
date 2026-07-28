---
collection: ansible
version: "8"
title: "splunk.es.adaptive_response_notable_event module – Manage Splunk Enterprise Security Notable Event Adaptive Responses"
source_url: https://docs.ansible.com/projects/ansible/8/collections/splunk/es/adaptive_response_notable_event_module.html
fetched_at: 2026-07-28T02:53:46+00:00
---
# splunk.es.adaptive_response_notable_event module – Manage Splunk Enterprise Security Notable Event Adaptive Responses

> **Note:**
>
> This module is part of the [splunk.es collection](https://galaxy.ansible.com/ui/repo/published/splunk/es/) (version 2.1.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install splunk.es`.
>
> To use it in a playbook, specify: `splunk.es.adaptive_response_notable_event`.

New in splunk.es 1.0.0

- [DEPRECATED](adaptive_response_notable_event_module.md#deprecated)
- [Synopsis](adaptive_response_notable_event_module.md#synopsis)
- [Parameters](adaptive_response_notable_event_module.md#parameters)
- [Examples](adaptive_response_notable_event_module.md#examples)
- [Status](adaptive_response_notable_event_module.md#status)

## [DEPRECATED](adaptive_response_notable_event_module.md#id1)

Removed in:
:   major release after 2024-09-01

Why:
:   Newer and updated modules released with more functionality.

Alternative:
:   splunk_adaptive_response_notable_events

## [Synopsis](adaptive_response_notable_event_module.md#id2)

- This module allows for creation, deletion, and modification of Splunk Enterprise Security Notable Event Adaptive Responses that are associated with a correlation search

Aliases: splunk_adaptive_response_notable_event

## [Parameters](adaptive_response_notable_event_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **asset_extraction**  list / elements=string | list of assets to extract, select any one or many of the available choices  defaults to all available choices  **Choices:**   - `"src"` ← (default) - `"dest"` ← (default) - `"dvc"` ← (default) - `"orig_host"` ← (default)   **Default:** `["src", "dest", "dvc", "orig_host"]` |
| **correlation_search_name**  string / required | Name of correlation search to associate this notable event adaptive response with |
| **default_owner**  string | Default owner of the notable event, if unset it will default to Splunk System Defaults |
| **default_status**  string | Default status of the notable event, if unset it will default to Splunk System Defaults  **Choices:**   - `"unassigned"` - `"new"` - `"in progress"` - `"pending"` - `"resolved"` - `"closed"` |
| **description**  string / required | Description of the notable event, this will populate the description field for the web console |
| **drill_down_earliest_offset**  string | Set the amount of time before the triggering event to search for related events. For example, 2h. Use “$info_min_time$” to set the drill-down time to match the earliest time of the search  **Default:** `"$info_min_time$"` |
| **drill_down_latest_offset**  string | Set the amount of time after the triggering event to search for related events. For example, 1m. Use “$info_max_time$” to set the drill-down time to match the latest time of the search  **Default:** `"$info_max_time$"` |
| **drill_down_name**  string | Name for drill down search, Supports variable substitution with fields from the matching event. |
| **drill_down_search**  string | Drill down search, Supports variable substitution with fields from the matching event. |
| **identity_extraction**  list / elements=string | list of identity fields to extract, select any one or many of the available choices  defaults to all available choices  **Choices:**   - `"user"` ← (default) - `"src_user"` ← (default)   **Default:** `["user", "src_user"]` |
| **investigation_profiles**  string | Investigation profile to assiciate the notable event with. |
| **name**  string / required | Name of notable event |
| **next_steps**  list / elements=string | List of adaptive responses that should be run next  Describe next steps and response actions that an analyst could take to address this threat.  **Default:** `[]` |
| **recommended_actions**  list / elements=string | List of adaptive responses that are recommended to be run next  Identifying Recommended Adaptive Responses will highlight those actions for the analyst when looking at the list of response actions available, making it easier to find them among the longer list of available actions.  **Default:** `[]` |
| **security_domain**  string | Splunk Security Domain  **Choices:**   - `"access"` - `"endpoint"` - `"network"` - `"threat"` ← (default) - `"identity"` - `"audit"` |
| **severity**  string | Severity rating  **Choices:**   - `"informational"` - `"low"` - `"medium"` - `"high"` ← (default) - `"critical"` - `"unknown"` |
| **state**  string / required | Add or remove a data source.  **Choices:**   - `"present"` - `"absent"` |

## [Examples](adaptive_response_notable_event_module.md#id4)

```yaml+jinja
- name: Example of using splunk.es.adaptive_response_notable_event module
  splunk.es.adaptive_response_notable_event:
    name: "Example notable event from Ansible"
    correlation_search_name: "Example Correlation Search From Ansible"
    description: "Example notable event from Ansible, description."
    state: "present"
    next_steps:
      - ping
      - nslookup
    recommended_actions:
      - script
      - ansiblesecurityautomation
```

## [Status](adaptive_response_notable_event_module.md#id5)

- This module will be removed in a major release after 2024-09-01.
  *[deprecated]*
- For more information see [DEPRECATED](adaptive_response_notable_event_module.md#deprecated).

### Authors

- Ansible Security Automation Team (@maxamillion) <<https://github.com/ansible-security>>

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/splunk.es/issues)
- [Repository (Sources)](https://github.com/ansible-collections/splunk.es)
