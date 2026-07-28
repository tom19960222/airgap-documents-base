---
collection: ansible
version: "6"
title: "splunk.es.splunk_correlation_searches module – Splunk Enterprise Security Correlation searches resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/splunk/es/splunk_correlation_searches_module.html
fetched_at: 2026-07-28T00:19:59+00:00
---
# splunk.es.splunk_correlation_searches module – Splunk Enterprise Security Correlation searches resource module

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
> To use it in a playbook, specify: `splunk.es.splunk_correlation_searches`.

New in splunk.es 2.1.0

- [Synopsis](splunk_correlation_searches_module.md#synopsis)
- [Parameters](splunk_correlation_searches_module.md#parameters)
- [Examples](splunk_correlation_searches_module.md#examples)
- [Return Values](splunk_correlation_searches_module.md#return-values)

## [Synopsis](splunk_correlation_searches_module.md#id1)

- This module allows for creation, deletion, and modification of Splunk Enterprise Security correlation searches
- Tested against Splunk Enterprise Server v8.2.3 with Splunk Enterprise Security v7.0.1 installed on it.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](splunk_correlation_searches_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Configure file and directory monitoring on the system |
| **annotations**  dictionary | Add context from industry standard cyber security mappings in Splunk Enterprise Security or custom annotations |
| **cis20**  list / elements=string | Specify CIS20 annotations |
| **custom**  list / elements=dictionary | Specify custom framework and custom annotations |
| **custom_annotations**  list / elements=string | Specify annotations associated with custom framework |
| **framework**  string | Specify annotation framework |
| **kill_chain_phases**  list / elements=string | Specify Kill 10 annotations |
| **mitre_attack**  list / elements=string | Specify MITRE ATTACK annotations |
| **nist**  list / elements=string | Specify NIST annotations |
| **app**  string | Splunk app to associate the correlation seach with  Default: `"SplunkEnterpriseSecuritySuite"` |
| **cron_schedule**  string | Enter a cron-style schedule.  For example `'*/5 * * * *'` (every 5 minutes) or `'0 21 * * *'` (every day at 9 PM).  Real-time searches use a default schedule of `'*/5 * * * *'`.  Default: `"*/5 * * * *"` |
| **description**  string | Description of the coorelation search, this will populate the description field for the web console |
| **disabled**  boolean | Disable correlation search  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | Name of correlation search |
| **schedule_priority**  string | Raise the scheduling priority of a report. Set to “Higher” to prioritize it above other searches of the same scheduling mode, or “Highest” to prioritize it above other searches regardless of mode. Use with discretion.  Choices:   - `"default"` ← (default) - `"higher"` - `"highest"` |
| **schedule_window**  string | Let report run at any time within a window that opens at its scheduled run time, to improve efficiency when there are many concurrently scheduled reports. The “auto” setting automatically determines the best window width for the report.  Default: `"0"` |
| **scheduling**  string | Controls the way the scheduler computes the next execution time of a scheduled search.  Learn more: <https://docs.splunk.com/Documentation/Splunk/7.2.3/Report/Configurethepriorityofscheduledreports#Real-time_scheduling_and_continuous_scheduling>  Choices:   - `"realtime"` ← (default) - `"continuous"` |
| **search**  string | SPL search string |
| **suppress_alerts**  boolean | To suppress alerts from this correlation search or not  Choices:   - `false` ← (default) - `true` |
| **throttle_fields_to_group_by**  list / elements=string | Type the fields to consider for matching events for throttling. |
| **throttle_window_duration**  string | How much time to ignore other events that match the field values specified in Fields to group by. |
| **time_earliest**  string | Earliest time using relative time modifiers.  Default: `"-24h"` |
| **time_latest**  string | Latest time using relative time modifiers.  Default: `"now"` |
| **trigger_alert**  string | Notable response actions and risk response actions are always triggered for each result. Choose whether the trigger is activated once or for each result.  Choices:   - `"once"` ← (default) - `"for each result"` |
| **trigger_alert_when**  string | Raise the scheduling priority of a report. Set to “Higher” to prioritize it above other searches of the same scheduling mode, or “Highest” to prioritize it above other searches regardless of mode. Use with discretion.  Choices:   - `"number of events"` ← (default) - `"number of results"` - `"number of hosts"` - `"number of sources"` |
| **trigger_alert_when_condition**  string | Conditional to pass to `trigger_alert_when`  Choices:   - `"greater than"` ← (default) - `"less than"` - `"equal to"` - `"not equal to"` - `"drops by"` - `"rises by"` |
| **trigger_alert_when_value**  string | Value to pass to `trigger_alert_when`  Default: `"10"` |
| **ui_dispatch_context**  string | Set an app to use for links such as the drill-down search in a notable event or links in an email adaptive response action. If None, uses the Application Context. |
| **running_config**  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *running_config* argument allows the implementer to pass in the configuration to use as the base config for comparison. This value of this option should be the output received from device by executing command. |
| **state**  string | The state the configuration should be left in  Choices:   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"gathered"` |

## [Examples](splunk_correlation_searches_module.md#id3)

```yaml+jinja
# Using gathered
# --------------

- name: Gather correlation searches config
  splunk.es.splunk_correlation_searches:
    config:
      - name: Ansible Test
      - name: Ansible Test 2
    state: gathered

# RUN output:
# -----------

# "gathered": [
#     {
#       "annotations": {
#           "cis20": [
#               "test1"
#           ],
#           "custom": [
#               {
#                   "custom_annotations": [
#                       "test5"
#                   ],
#                   "framework": "test_framework"
#               }
#           ],
#           "kill_chain_phases": [
#               "test3"
#           ],
#           "mitre_attack": [
#               "test2"
#           ],
#           "nist": [
#               "test4"
#           ]
#       },
#       "app": "DA-ESS-EndpointProtection",
#       "cron_schedule": "*/5 * * * *",
#       "description": "test description",
#       "disabled": false,
#       "name": "Ansible Test",
#       "schedule_priority": "default",
#       "schedule_window": "0",
#       "scheduling": "realtime",
#       "search": '| tstats summariesonly=true values("Authentication.tag") as "tag",dc("Authentication.user") as "user_count",dc("Authent'
#                 'ication.dest") as "dest_count",count from datamodel="Authentication"."Authentication" where nodename="Authentication.Fai'
#                 'led_Authentication" by "Authentication.app","Authentication.src" | rename "Authentication.app" as "app","Authenticatio'
#                 'n.src" as "src" | where "count">=6',
#       "suppress_alerts": false,
#       "throttle_fields_to_group_by": [
#           "test_field1"
#       ],
#       "throttle_window_duration": "5s",
#       "time_earliest": "-24h",
#       "time_latest": "now",
#       "trigger_alert": "once",
#       "trigger_alert_when": "number of events",
#       "trigger_alert_when_condition": "greater than",
#       "trigger_alert_when_value": "10",
#       "ui_dispatch_context": "SplunkEnterpriseSecuritySuite"
#     }
# ]

# Using merged
# ------------

- name: Merge and create new correlation searches configuration
  splunk.es.splunk_correlation_searches:
    config:
      - name: Ansible Test
        disabled: false
        description: test description
        app: DA-ESS-EndpointProtection
        annotations:
          cis20:
            - test1
          mitre_attack:
            - test2
          kill_chain_phases:
            - test3
          nist:
            - test4
          custom:
            - framework: test_framework
              custom_annotations:
                - test5
        ui_dispatch_context: SplunkEnterpriseSecuritySuite
        time_earliest: -24h
        time_latest: now
        cron_schedule: "*/5 * * * *"
        scheduling: realtime
        schedule_window: "0"
        schedule_priority: default
        trigger_alert: once
        trigger_alert_when: number of events
        trigger_alert_when_condition: greater than
        trigger_alert_when_value: "10"
        throttle_window_duration: 5s
        throttle_fields_to_group_by:
          - test_field1
        suppress_alerts: False
        search: >
                '| tstats summariesonly=true values("Authentication.tag") as "tag",dc("Authentication.user") as "user_count",dc("Authent'
                'ication.dest") as "dest_count",count from datamodel="Authentication"."Authentication" where nodename="Authentication.Fai'
                'led_Authentication" by "Authentication.app","Authentication.src" | rename "Authentication.app" as "app","Authenticatio'
                'n.src" as "src" | where "count">=6'
    state: merged

# RUN output:
# -----------

# "after": [
#     {
#       "annotations": {
#           "cis20": [
#               "test1"
#           ],
#           "custom": [
#               {
#                   "custom_annotations": [
#                       "test5"
#                   ],
#                   "framework": "test_framework"
#               }
#           ],
#           "kill_chain_phases": [
#               "test3"
#           ],
#           "mitre_attack": [
#               "test2"
#           ],
#           "nist": [
#               "test4"
#           ]
#       },
#       "app": "DA-ESS-EndpointProtection",
#       "cron_schedule": "*/5 * * * *",
#       "description": "test description",
#       "disabled": false,
#       "name": "Ansible Test",
#       "schedule_priority": "default",
#       "schedule_window": "0",
#       "scheduling": "realtime",
#       "search": '| tstats summariesonly=true values("Authentication.tag") as "tag",dc("Authentication.user") as "user_count",dc("Authent'
#                 'ication.dest") as "dest_count",count from datamodel="Authentication"."Authentication" where nodename="Authentication.Fai'
#                 'led_Authentication" by "Authentication.app","Authentication.src" | rename "Authentication.app" as "app","Authenticatio'
#                 'n.src" as "src" | where "count">=6',
#       "suppress_alerts": false,
#       "throttle_fields_to_group_by": [
#           "test_field1"
#       ],
#       "throttle_window_duration": "5s",
#       "time_earliest": "-24h",
#       "time_latest": "now",
#       "trigger_alert": "once",
#       "trigger_alert_when": "number of events",
#       "trigger_alert_when_condition": "greater than",
#       "trigger_alert_when_value": "10",
#       "ui_dispatch_context": "SplunkEnterpriseSecuritySuite"
#     },
# ],
# "before": [],

# Using replaced
# --------------

- name: Replace existing correlation searches configuration
  splunk.es.splunk_correlation_searches:
    state: replaced
    config:
      - name: Ansible Test
        disabled: false
        description: test description
        app: SplunkEnterpriseSecuritySuite
        annotations:
          cis20:
            - test1
            - test2
          mitre_attack:
            - test3
            - test4
          kill_chain_phases:
            - test5
            - test6
          nist:
            - test7
            - test8
          custom:
            - framework: test_framework2
              custom_annotations:
                - test9
                - test10
        ui_dispatch_context: SplunkEnterpriseSecuritySuite
        time_earliest: -24h
        time_latest: now
        cron_schedule: "*/5 * * * *"
        scheduling: continuous
        schedule_window: auto
        schedule_priority: default
        trigger_alert: once
        trigger_alert_when: number of events
        trigger_alert_when_condition: greater than
        trigger_alert_when_value: 10
        throttle_window_duration: 5s
        throttle_fields_to_group_by:
          - test_field1
          - test_field2
        suppress_alerts: True
        search: >
                '| tstats summariesonly=true values("Authentication.tag") as "tag",dc("Authentication.user") as "user_count",dc("Authent'
                'ication.dest") as "dest_count",count from datamodel="Authentication"."Authentication" where nodename="Authentication.Fai'
                'led_Authentication" by "Authentication.app","Authentication.src" | rename "Authentication.app" as "app","Authenticatio'
                'n.src" as "src" | where "count">=6'

# RUN output:
# -----------

# "after": [
#     {
#         "annotations": {
#             "cis20": [
#                 "test1",
#                 "test2"
#             ],
#             "custom": [
#                 {
#                     "custom_annotations": [
#                         "test9",
#                         "test10"
#                     ],
#                     "framework": "test_framework2"
#                 }
#             ],
#             "kill_chain_phases": [
#                 "test5",
#                 "test6"
#             ],
#             "mitre_attack": [
#                 "test3",
#                 "test4"
#             ],
#             "nist": [
#                 "test7",
#                 "test8"
#             ]
#         },
#         "app": "SplunkEnterpriseSecuritySuite",
#         "cron_schedule": "*/5 * * * *",
#         "description": "test description",
#         "disabled": false,
#         "name": "Ansible Test",
#         "schedule_priority": "default",
#         "schedule_window": "auto",
#         "scheduling": "continuous",
#         "search": '| tstats summariesonly=true values("Authentication.tag") as "tag",dc("Authentication.user") as "user_count",dc("Authent'
#                   'ication.dest") as "dest_count",count from datamodel="Authentication"."Authentication" where nodename="Authentication.Fai'
#                   'led_Authentication" by "Authentication.app","Authentication.src" | rename "Authentication.app" as "app","Authenticatio'
#                   'n.src" as "src" | where "count">=6',
#         "suppress_alerts": true,
#         "throttle_fields_to_group_by": [
#             "test_field1",
#             "test_field2"
#         ],
#         "throttle_window_duration": "5s",
#         "time_earliest": "-24h",
#         "time_latest": "now",
#         "trigger_alert": "once",
#         "trigger_alert_when": "number of events",
#         "trigger_alert_when_condition": "greater than",
#         "trigger_alert_when_value": "10",
#         "ui_dispatch_context": "SplunkEnterpriseSecuritySuite"
#     }
# ],
# "before": [
#     {
#         "annotations": {
#             "cis20": [
#                 "test1"
#             ],
#             "custom": [
#                 {
#                     "custom_annotations": [
#                         "test5"
#                     ],
#                     "framework": "test_framework"
#                 }
#             ],
#             "kill_chain_phases": [
#                 "test3"
#             ],
#             "mitre_attack": [
#                 "test2"
#             ],
#             "nist": [
#                 "test4"
#             ]
#         },
#         "app": "DA-ESS-EndpointProtection",
#         "cron_schedule": "*/5 * * * *",
#         "description": "test description",
#         "disabled": false,
#         "name": "Ansible Test",
#         "schedule_priority": "default",
#         "schedule_window": "0",
#         "scheduling": "realtime",
#         "search": '| tstats summariesonly=true values("Authentication.tag") as "tag",dc("Authentication.user") as "user_count",dc("Authent'
#                   'ication.dest") as "dest_count",count from datamodel="Authentication"."Authentication" where nodename="Authentication.Fai'
#                   'led_Authentication" by "Authentication.app","Authentication.src" | rename "Authentication.app" as "app","Authenticatio'
#                   'n.src" as "src" | where "count">=6',
#         "suppress_alerts": false,
#         "throttle_fields_to_group_by": [
#             "test_field1"
#         ],
#         "throttle_window_duration": "5s",
#         "time_earliest": "-24h",
#         "time_latest": "now",
#         "trigger_alert": "once",
#         "trigger_alert_when": "number of events",
#         "trigger_alert_when_condition": "greater than",
#         "trigger_alert_when_value": "10",
#         "ui_dispatch_context": "SplunkEnterpriseSecuritySuite"
#     }
# ]

# Using deleted
# -------------

- name: Example to delete the corelation search
  splunk.es.splunk_correlation_searches:
    config:
      - name: Ansible Test
    state: deleted

# RUN output:
# -----------

# "after": [],
# "before": [
#     {
#       "annotations": {
#           "cis20": [
#               "test1"
#           ],
#           "custom": [
#               {
#                   "custom_annotations": [
#                       "test5"
#                   ],
#                   "framework": "test_framework"
#               }
#           ],
#           "kill_chain_phases": [
#               "test3"
#           ],
#           "mitre_attack": [
#               "test2"
#           ],
#           "nist": [
#               "test4"
#           ]
#       },
#       "app": "DA-ESS-EndpointProtection",
#       "cron_schedule": "*/5 * * * *",
#       "description": "test description",
#       "disabled": false,
#       "name": "Ansible Test",
#       "schedule_priority": "default",
#       "schedule_window": "0",
#       "scheduling": "realtime",
#       "search": '| tstats summariesonly=true values("Authentication.tag") as "tag",dc("Authentication.user") as "user_count",dc("Authent'
#                 'ication.dest") as "dest_count",count from datamodel="Authentication"."Authentication" where nodename="Authentication.Fai'
#                 'led_Authentication" by "Authentication.app","Authentication.src" | rename "Authentication.app" as "app","Authenticatio'
#                 'n.src" as "src" | where "count">=6',
#       "suppress_alerts": false,
#       "throttle_fields_to_group_by": [
#           "test_field1"
#       ],
#       "throttle_window_duration": "5s",
#       "time_earliest": "-24h",
#       "time_latest": "now",
#       "trigger_alert": "once",
#       "trigger_alert_when": "number of events",
#       "trigger_alert_when_condition": "greater than",
#       "trigger_alert_when_value": "10",
#       "ui_dispatch_context": "SplunkEnterpriseSecuritySuite"
#     },
# ],
```

## [Return Values](splunk_correlation_searches_module.md#id4)

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
