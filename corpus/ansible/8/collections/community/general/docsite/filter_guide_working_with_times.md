---
collection: ansible
version: "8"
title: "Working with times"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/docsite/filter_guide_working_with_times.html
fetched_at: 2026-07-28T03:00:44+00:00
---
# Working with times

The [community.general.to_time_unit filter](../to_time_unit_filter.md#ansible-collections-community-general-to-time-unit-filter) allows to convert times from a human-readable string to a unit. For example, `'4h 30min 12second' | community.general.to_time_unit('hour')` gives the number of hours that correspond to 4 hours, 30 minutes and 12 seconds.

There are shorthands to directly convert to various units, like [community.general.to_hours](../to_hours_filter.md#ansible-collections-community-general-to-hours-filter), [community.general.to_minutes](../to_minutes_filter.md#ansible-collections-community-general-to-minutes-filter), [community.general.to_seconds](../to_seconds_filter.md#ansible-collections-community-general-to-seconds-filter), and so on. The following table lists all units that can be used:

Units

| Unit name | Unit value in seconds | Unit strings for filter | Shorthand filter |
| --- | --- | --- | --- |
| Millisecond | 1/1000 second | `ms`, `millisecond`, `milliseconds`, `msec`, `msecs`, `msecond`, `mseconds` | [community.general.to_milliseconds](../to_milliseconds_filter.md#ansible-collections-community-general-to-milliseconds-filter) |
| Second | 1 second | `s`, `sec`, `secs`, `second`, `seconds` | [community.general.to_seconds](../to_seconds_filter.md#ansible-collections-community-general-to-seconds-filter) |
| Minute | 60 seconds | `m`, `min`, `mins`, `minute`, `minutes` | [community.general.to_minutes](../to_minutes_filter.md#ansible-collections-community-general-to-minutes-filter) |
| Hour | 60\*60 seconds | `h`, `hour`, `hours` | [community.general.to_hours](../to_hours_filter.md#ansible-collections-community-general-to-hours-filter) |
| Day | 24\*60\*60 seconds | `d`, `day`, `days` | [community.general.to_days](../to_days_filter.md#ansible-collections-community-general-to-days-filter) |
| Week | 7\*24\*60\*60 seconds | `w`, `week`, `weeks` | [community.general.to_weeks](../to_weeks_filter.md#ansible-collections-community-general-to-weeks-filter) |
| Month | 30\*24\*60\*60 seconds | `mo`, `month`, `months` | [community.general.to_months](../to_months_filter.md#ansible-collections-community-general-to-months-filter) |
| Year | 365\*24\*60\*60 seconds | `y`, `year`, `years` | [community.general.to_years](../to_years_filter.md#ansible-collections-community-general-to-years-filter) |

Note that months and years are using a simplified representation: a month is 30 days, and a year is 365 days. If you need different definitions of months or years, you can pass them as keyword arguments. For example, if you want a year to be 365.25 days, and a month to be 30.5 days, you can write `'11months 4' | community.general.to_years(year=365.25, month=30.5)`. These keyword arguments can be specified to [community.general.to_time_unit](../to_time_unit_filter.md#ansible-collections-community-general-to-time-unit-filter) and to all shorthand filters.

```yaml+jinja
- name: Convert string to seconds
  debug:
    msg: "{{ '30h 20m 10s 123ms' | community.general.to_time_unit('seconds') }}"

- name: Convert string to hours
  debug:
    msg: "{{ '30h 20m 10s 123ms' | community.general.to_hours }}"

- name: Convert string to years (using 365.25 days == 1 year)
  debug:
    msg: "{{ '400d 15h' | community.general.to_years(year=365.25) }}"
```

This produces:

```ansible-output
TASK [Convert string to seconds] **********************************************************
ok: [localhost] => {
    "msg": "109210.123"
}

TASK [Convert string to hours] ************************************************************
ok: [localhost] => {
    "msg": "30.336145277778"
}

TASK [Convert string to years (using 365.25 days == 1 year)] ******************************
ok: [localhost] => {
    "msg": "1.096851471595"
}
```
