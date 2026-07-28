---
collection: ansible
version: "8"
title: "community.general.to_weeks filter – Converte a duration string to weeks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/to_weeks_filter.html
fetched_at: 2026-07-28T01:52:27+00:00
---
# community.general.to_weeks filter – Converte a duration string to weeks

> **Note:**
>
> This filter plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.to_weeks`.

New in community.general 0.2.0

- [Synopsis](to_weeks_filter.md#synopsis)
- [Input](to_weeks_filter.md#input)
- [Keyword parameters](to_weeks_filter.md#keyword-parameters)
- [Examples](to_weeks_filter.md#examples)
- [Return Value](to_weeks_filter.md#return-value)

## [Synopsis](to_weeks_filter.md#id1)

- Parse a human readable time duration string and convert to weeks.

## [Input](to_weeks_filter.md#id2)

This describes the input of the filter, the value before `| community.general.to_weeks`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | The time string to convert.  Can use the units `y` and `year` for a year, `mo` and `month` for a month, `w` and `week` for a week, `d` and `day` for a day, `h` and `hour` for a hour, `m`, `min` and `minute` for minutes, `s`, `sec` and `second` for seconds, `ms`, `msec`, `msecond` and `millisecond` for milliseconds. The suffix `s` can be added to a unit as well, so `seconds` is the same as `second`.  Valid strings are space separated combinations of an integer with an optional minus sign and a unit.  Examples are `1h`, `-5m`, and `3h -5m 6s`. |

## [Keyword parameters](to_weeks_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | community.general.to_weeks(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **month**  float | Number of days per month.  **Default:** `30.0` |
| **year**  float | Number of days per year.  **Default:** `365.0` |

## [Examples](to_weeks_filter.md#id4)

```yaml+jinja
- name: Convert a duration into weeks
  ansible.builtin.debug:
    msg: "{{ '1y 7m 5d 30h' | community.general.to_weeks }}"
```

## [Return Value](to_weeks_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  float | Number of weeks.  **Returned:** success |

### Authors

- René Moser (@resmo)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
