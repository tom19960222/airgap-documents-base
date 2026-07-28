---
collection: ansible
version: "8"
title: "community.general.stackdriver module – Send code deploy and annotation events to stackdriver"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/stackdriver_module.html
fetched_at: 2026-07-28T01:50:47+00:00
---
# community.general.stackdriver module – Send code deploy and annotation events to stackdriver

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.stackdriver`.

- [DEPRECATED](stackdriver_module.md#deprecated)
- [Synopsis](stackdriver_module.md#synopsis)
- [Parameters](stackdriver_module.md#parameters)
- [Attributes](stackdriver_module.md#attributes)
- [Examples](stackdriver_module.md#examples)
- [Status](stackdriver_module.md#status)

## [DEPRECATED](stackdriver_module.md#id1)

Removed in:
:   version 9.0.0

Why:
:   the endpoints this module relies on do not exist any more and do not resolve to IPs in DNS.

Alternative:
:   no known alternative at this point

## [Synopsis](stackdriver_module.md#id2)

- Send code deploy and annotation events to Stackdriver

Aliases: monitoring.stackdriver

## [Parameters](stackdriver_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **annotated_by**  string | The person or robot who the annotation should be attributed to.  **Default:** `"Ansible"` |
| **deployed_by**  string | The person or robot responsible for deploying the code  **Default:** `"Ansible"` |
| **deployed_to**  string | The environment code was deployed to. (ie: development, staging, production) |
| **event**  string / required | The type of event to send, either annotation or deploy  **Choices:**   - `"annotation"` - `"deploy"` |
| **event_epoch**  string | Unix timestamp of where the event should appear in the timeline, defaults to now. Be careful with this. |
| **instance_id**  string | id of an EC2 instance that this event should be attached to, which will limit the contexts where this event is shown |
| **key**  string / required | API key. |
| **level**  string | one of INFO/WARN/ERROR, defaults to INFO if not supplied. May affect display.  **Choices:**   - `"INFO"` ← (default) - `"WARN"` - `"ERROR"` |
| **msg**  string | The contents of the annotation message, in plain text. Limited to 256 characters. Required for annotation. |
| **repository**  string | The repository (or project) deployed |
| **revision_id**  string | The revision of the code that was deployed. Required for deploy events |

## [Attributes](stackdriver_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](stackdriver_module.md#id5)

```yaml+jinja
- name: Send a code deploy event to stackdriver
  community.general.stackdriver:
    key: AAAAAA
    event: deploy
    deployed_to: production
    deployed_by: leeroyjenkins
    repository: MyWebApp
    revision_id: abcd123

- name: Send an annotation event to stackdriver
  community.general.stackdriver:
    key: AAAAAA
    event: annotation
    msg: Greetings from Ansible
    annotated_by: leeroyjenkins
    level: WARN
    instance_id: i-abcd1234
```

## [Status](stackdriver_module.md#id6)

- This module will be removed in version 9.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](stackdriver_module.md#deprecated).

### Authors

- Ben Whaley (@bwhaley)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
