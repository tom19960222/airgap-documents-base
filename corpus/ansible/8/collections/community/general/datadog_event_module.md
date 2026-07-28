---
collection: ansible
version: "8"
title: "community.general.datadog_event module – Posts events to Datadog  service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/datadog_event_module.html
fetched_at: 2026-07-28T01:45:18+00:00
---
# community.general.datadog_event module – Posts events to Datadog service

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
> To use it in a playbook, specify: `community.general.datadog_event`.

- [Synopsis](datadog_event_module.md#synopsis)
- [Parameters](datadog_event_module.md#parameters)
- [Attributes](datadog_event_module.md#attributes)
- [Examples](datadog_event_module.md#examples)

## [Synopsis](datadog_event_module.md#id1)

- Allows to post events to Datadog (www.datadoghq.com) service.
- Uses <http://docs.datadoghq.com/api/#events> API.

Aliases: monitoring.datadog.datadog_event

## [Parameters](datadog_event_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregation_key**  string | An arbitrary string to use for aggregation. |
| **alert_type**  string | Type of alert.  **Choices:**   - `"error"` - `"warning"` - `"info"` ← (default) - `"success"` |
| **api_host**  string  *added in community.general 3.3.0* | DataDog API endpoint URL. |
| **api_key**  string / required | Your DataDog API key. |
| **app_key**  string / required | Your DataDog app key. |
| **date_happened**  integer | POSIX timestamp of the event.  Default value is now. |
| **host**  string | Host name to associate with the event.  If not specified, it defaults to the remote system’s hostname. |
| **priority**  string | The priority of the event.  **Choices:**   - `"normal"` ← (default) - `"low"` |
| **tags**  list / elements=string | Comma separated list of tags to apply to the event. |
| **text**  string / required | The body of the event. |
| **title**  string / required | The event title. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](datadog_event_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](datadog_event_module.md#id4)

```yaml+jinja
- name: Post an event with low priority
  community.general.datadog_event:
    title: Testing from ansible
    text: Test
    priority: low
    api_key: 9775a026f1ca7d1c6c5af9d94d9595a4
    app_key: j4JyCYfefWHhgFgiZUqRm63AXHNZQyPGBfJtAzmN

- name: Post an event with several tags
  community.general.datadog_event:
    title: Testing from ansible
    text: Test
    api_key: 9775a026f1ca7d1c6c5af9d94d9595a4
    app_key: j4JyCYfefWHhgFgiZUqRm63AXHNZQyPGBfJtAzmN
    tags: 'aa,bb,#host:{{ inventory_hostname }}'

- name: Post an event with several tags to another endpoint
  community.general.datadog_event:
    title: Testing from ansible
    text: Test
    api_key: 9775a026f1ca7d1c6c5af9d94d9595a4
    app_key: j4JyCYfefWHhgFgiZUqRm63AXHNZQyPGBfJtAzmN
    api_host: 'https://example.datadoghq.eu'
    tags:
      - aa
      - b
      - '#host:{{ inventory_hostname }}'
```

### Authors

- Artūras ‘arturaz’ Šlajus (@arturaz)
- Naoya Nakazawa (@n0ts)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
