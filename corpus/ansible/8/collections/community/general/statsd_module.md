---
collection: ansible
version: "8"
title: "community.general.statsd module – Send metrics to StatsD"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/statsd_module.html
fetched_at: 2026-07-28T01:50:48+00:00
---
# community.general.statsd module – Send metrics to StatsD

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](statsd_module.md#ansible-collections-community-general-statsd-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.statsd`.

New in community.general 2.1.0

- [Synopsis](statsd_module.md#synopsis)
- [Requirements](statsd_module.md#requirements)
- [Parameters](statsd_module.md#parameters)
- [Attributes](statsd_module.md#attributes)
- [Examples](statsd_module.md#examples)

## [Synopsis](statsd_module.md#id1)

- The `statsd` module sends metrics to StatsD.
- For more information, see <https://statsd-metrics.readthedocs.io/en/latest/>.
- Supported metric types are `counter` and `gauge`. Currently unupported metric types are `timer`, `set`, and `gaugedelta`.

Aliases: monitoring.statsd

## [Requirements](statsd_module.md#id2)

The below requirements are needed on the host that executes this module.

- statsd

## [Parameters](statsd_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **delta**  boolean | If the metric is of type `gauge`, change the value by `delta`.  **Choices:**   - `false` ← (default) - `true` |
| **host**  string | StatsD host (hostname or IP) to send metrics to.  **Default:** `"localhost"` |
| **metric**  string / required | The name of the metric. |
| **metric_prefix**  string | The prefix to add to the metric.  **Default:** `""` |
| **metric_type**  string / required | The type of metric.  **Choices:**   - `"counter"` - `"gauge"` |
| **port**  integer | The port on `host` which StatsD is listening on.  **Default:** `8125` |
| **protocol**  string | The transport protocol to send metrics over.  **Choices:**   - `"udp"` ← (default) - `"tcp"` |
| **state**  string | State of the check, only `present` makes sense.  **Choices:**   - `"present"` ← (default) |
| **timeout**  float | Sender timeout, only applicable if `protocol` is `tcp`.  **Default:** `1.0` |
| **value**  integer / required | The value of the metric. |

## [Attributes](statsd_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](statsd_module.md#id5)

```yaml+jinja
- name: Increment the metric my_counter by 1
  community.general.statsd:
    host: localhost
    port: 9125
    protocol: tcp
    metric: my_counter
    metric_type: counter
    value: 1

- name: Set the gauge my_gauge to 7
  community.general.statsd:
    host: localhost
    port: 9125
    protocol: tcp
    metric: my_gauge
    metric_type: gauge
    value: 7
```

### Authors

- Mark Mercado (@mamercad)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
