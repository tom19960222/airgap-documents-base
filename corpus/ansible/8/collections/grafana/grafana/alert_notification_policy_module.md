---
collection: ansible
version: "8"
title: "grafana.grafana.alert_notification_policy module – Manage Alerting Policies points in Grafana"
source_url: https://docs.ansible.com/projects/ansible/8/collections/grafana/grafana/alert_notification_policy_module.html
fetched_at: 2026-07-28T02:33:48+00:00
---
# grafana.grafana.alert_notification_policy module – Manage Alerting Policies points in Grafana

> **Note:**
>
> This module is part of the [grafana.grafana collection](https://galaxy.ansible.com/ui/repo/published/grafana/grafana/) (version 2.2.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install grafana.grafana`.
> You need further requirements to be able to use this module,
> see [Requirements](alert_notification_policy_module.md#ansible-collections-grafana-grafana-alert-notification-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `grafana.grafana.alert_notification_policy`.

New in grafana.grafana 0.0.1

- [Synopsis](alert_notification_policy_module.md#synopsis)
- [Requirements](alert_notification_policy_module.md#requirements)
- [Parameters](alert_notification_policy_module.md#parameters)
- [Notes](alert_notification_policy_module.md#notes)
- [Examples](alert_notification_policy_module.md#examples)
- [Return Values](alert_notification_policy_module.md#return-values)

## [Synopsis](alert_notification_policy_module.md#id1)

- Set the notification policy tree using Ansible.

## [Requirements](alert_notification_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 1.0.0

## [Parameters](alert_notification_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **Continue**  boolean | Continue matching subsequent sibling nodes if set to `true`.  **Choices:**   - `false` ← (default) - `true` |
| **grafana_api_key**  string / required | Grafana API Key used to authenticate with Grafana. |
| **grafana_url**  string / required | URL of the Grafana instance. |
| **groupByStr**  list / elements=string | List of string.  Group alerts when you receive a notification based on labels. If empty it will be inherited from the parent policy.  **Default:** `[]` |
| **groupInterval**  string | Sets the wait time to send a batch of new alerts for that group after the first notification was sent. Inherited from the parent policy if empty.  **Default:** `"5m"` |
| **groupWait**  string | Sets the wait time until the initial notification is sent for a new group created by an incoming alert. Inherited from the parent policy if empty.  **Default:** `"30s"` |
| **muteTimeIntervals**  list / elements=string | List of string.  Sets the mute timing for the notfification policy.  **Default:** `[]` |
| **objectMatchers**  list / elements=dictionary | Matchers is a slice of Matchers that is sortable, implements Stringer, and provides a Matches method to match a LabelSet.  **Default:** `[]` |
| **repeatInterval**  string | Sets the waiting time to resend an alert after they have successfully been sent.  **Default:** `"4h"` |
| **rootPolicyReceiver**  string | Sets the name of the contact point to be set as the default receiver.  **Default:** `"grafana-default-email"` |
| **routes**  list / elements=dictionary / required | List of objects  Sets the Route that contains definitions of how to handle alerts. |

## [Notes](alert_notification_policy_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](alert_notification_policy_module.md#id5)

```yaml+jinja
- name: Set Notification policy tree
  grafana.grafana.alert_notification_policy:
    grafana_url: "{{ grafana_url }}"
    grafana_api_key: "{{ grafana_api_key }}"
    routes: [
      {
        receiver: myReceiver,
        object_matchers: [["env", "=", "Production"]],
      }
    ]

- name: Set nested Notification policies
  grafana.grafana.alert_notification_policy:
    routes: [
      {
        receiver: myReceiver,
        object_matchers: [["env", "=", "Production"],["team", "=", "ops"]],
        routes: [
          {
            receiver: myReceiver2,
            object_matchers: [["region", "=", "eu"]],
          }
        ]
      },
      {
        receiver: myReceiver3,
        object_matchers: [["env", "=", "Staging"]]
      }
    ]
    grafana_url: "{{ grafana_url }}"
    grafana_api_key: "{{ grafana_api_key }}"
```

## [Return Values](alert_notification_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  dictionary | Dict object containing Notification tree information.  **Returned:** On success |
| **group_interval**  string | The waiting time to send a batch of new alerts for that group after the first notification was sent. This is of the parent policy.  **Returned:** on success  **Sample:** `"5m"` |
| **group_wait**  string | The waiting time until the initial notification is sent for a new group created by an incoming alert. This is of the parent policy.  **Returned:** on success  **Sample:** `"30s"` |
| **receiver**  string | The name of the default contact point.  **Returned:** state is present and on success  **Sample:** `"grafana-default-email"` |
| **repeat_interval**  string | The waiting time to resend an alert after they have successfully been sent. This is of the parent policy  **Returned:** on success  **Sample:** `"4h"` |
| **routes**  list / elements=string | The entire notification tree returned as a list.  **Returned:** on success  **Sample:** `[{"object_matchers": [["env", "=", "Production"]], "receiver": "grafana-default-email"}]` |

### Authors

- Ishan Jain (@ishanjainn)

### Collection links

- [Issue Tracker](https://github.com/grafana/grafana-ansible-collection/issues)
- [Repository (Sources)](https://github.com/grafana/grafana-ansible-collection)
