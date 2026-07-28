---
collection: ansible
version: "6"
title: "community.general.pagerduty_alert module – Trigger, acknowledge or resolve PagerDuty incidents"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/pagerduty_alert_module.html
fetched_at: 2026-07-27T17:11:46+00:00
---
# community.general.pagerduty_alert module – Trigger, acknowledge or resolve PagerDuty incidents

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](pagerduty_alert_module.md#ansible-collections-community-general-pagerduty-alert-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.pagerduty_alert`.

- [Synopsis](pagerduty_alert_module.md#synopsis)
- [Requirements](pagerduty_alert_module.md#requirements)
- [Parameters](pagerduty_alert_module.md#parameters)
- [Examples](pagerduty_alert_module.md#examples)

## [Synopsis](pagerduty_alert_module.md#id1)

- This module will let you trigger, acknowledge or resolve a PagerDuty incident by sending events

## [Requirements](pagerduty_alert_module.md#id2)

The below requirements are needed on the host that executes this module.

- PagerDuty API access

## [Parameters](pagerduty_alert_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | The pagerduty API key (readonly access), generated on the pagerduty site. |
| **client**  string | The name of the monitoring client that is triggering this event. |
| **client_url**  string | The URL of the monitoring client that is triggering this event. |
| **desc**  string | For `triggered` *state* - Required. Short description of the problem that led to this trigger. This field (or a truncated version) will be used when generating phone calls, SMS messages and alert emails. It will also appear on the incidents tables in the PagerDuty UI. The maximum length is 1024 characters.  For `acknowledged` or `resolved` *state* - Text that will appear in the incident’s log associated with this event.  Default: `"Created via Ansible"` |
| **incident_key**  string | Identifies the incident to which this *state* should be applied.  For `triggered` *state* - If there’s no open (i.e. unresolved) incident with this key, a new one will be created. If there’s already an open incident with a matching key, this event will be appended to that incident’s log. The event key provides an easy way to “de-dup” problem reports.  For `acknowledged` or `resolved` *state* - This should be the incident_key you received back when the incident was first opened by a trigger event. Acknowledge events referencing resolved or nonexistent incidents will be discarded. |
| **integration_key**  string | The GUID of one of your “Generic API” services.  This is the “integration key” listed on a “Integrations” tab of PagerDuty service. |
| **name**  string | PagerDuty unique subdomain. Obsolete. It is not used with PagerDuty REST v2 API. |
| **service_id**  string / required | ID of PagerDuty service when incidents will be triggered, acknowledged or resolved. |
| **service_key**  string | The GUID of one of your “Generic API” services. Obsolete. Please use *integration_key*. |
| **state**  string / required | Type of event to be sent.  Choices:   - `"triggered"` - `"acknowledged"` - `"resolved"` |

## [Examples](pagerduty_alert_module.md#id4)

```yaml+jinja
- name: Trigger an incident with just the basic options
  community.general.pagerduty_alert:
    name: companyabc
    integration_key: xxx
    api_key: yourapikey
    service_id: PDservice
    state: triggered
    desc: problem that led to this trigger

- name: Trigger an incident with more options
  community.general.pagerduty_alert:
    integration_key: xxx
    api_key: yourapikey
    service_id: PDservice
    state: triggered
    desc: problem that led to this trigger
    incident_key: somekey
    client: Sample Monitoring Service
    client_url: http://service.example.com

- name: Acknowledge an incident based on incident_key
  community.general.pagerduty_alert:
    integration_key: xxx
    api_key: yourapikey
    service_id: PDservice
    state: acknowledged
    incident_key: somekey
    desc: "some text for incident's log"

- name: Resolve an incident based on incident_key
  community.general.pagerduty_alert:
    integration_key: xxx
    api_key: yourapikey
    service_id: PDservice
    state: resolved
    incident_key: somekey
    desc: "some text for incident's log"
```

### Authors

- Amanpreet Singh (@ApsOps)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
