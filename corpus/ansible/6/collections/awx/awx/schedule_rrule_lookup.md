---
collection: ansible
version: "6"
title: "awx.awx.schedule_rrule lookup – Generate an rrule string which can be used for Schedules"
source_url: https://docs.ansible.com/projects/ansible/6/collections/awx/awx/schedule_rrule_lookup.html
fetched_at: 2026-07-27T16:45:38+00:00
---
# awx.awx.schedule_rrule lookup – Generate an rrule string which can be used for Schedules

> **Note:**
>
> This lookup plugin is part of the [awx.awx collection](https://galaxy.ansible.com/awx/awx) (version 21.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](schedule_rrule_lookup.md#ansible-collections-awx-awx-schedule-rrule-lookup-requirements) for details.
>
> To use it in a playbook, specify: `awx.awx.schedule_rrule`.

- [Synopsis](schedule_rrule_lookup.md#synopsis)
- [Requirements](schedule_rrule_lookup.md#requirements)
- [Terms](schedule_rrule_lookup.md#terms)
- [Keyword parameters](schedule_rrule_lookup.md#keyword-parameters)
- [Notes](schedule_rrule_lookup.md#notes)
- [Examples](schedule_rrule_lookup.md#examples)
- [Return Value](schedule_rrule_lookup.md#return-value)

## [Synopsis](schedule_rrule_lookup.md#id1)

- Returns a string based on criteria which represents an rrule

## [Requirements](schedule_rrule_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- pytz
- python-dateutil >= 2.7.0

## [Terms](schedule_rrule_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | The frequency of the schedule  none - Run this schedule once  minute - Run this schedule every x minutes  hour - Run this schedule every x hours  day - Run this schedule every x days  week - Run this schedule weekly  month - Run this schedule monthly  Choices:   - `"none"` - `"minute"` - `"hour"` - `"day"` - `"week"` - `"month"` |

## [Keyword parameters](schedule_rrule_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('awx.awx.schedule_rrule', key1=value1, key2=value2, ...)` and `query('awx.awx.schedule_rrule', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **end_on**  string | How to end this schedule  If this is not defined, this schedule will never end  If this is a positive integer, this schedule will end after this number of occurences  If this is a date in the format YYYY-MM-DD [HH:MM:SS], this schedule ends after this date  Used for all types except none |
| **every**  integer | The repetition in months, weeks, days hours or minutes  Used for all types except none |
| **month_day_number**  integer | The day of the month this schedule will run on (0-31)  Used for month type schedules  Cannot be used with on_the parameter |
| **on_days**  string | The days to run this schedule on  A comma-separated list which can contain values sunday, monday, tuesday, wednesday, thursday, friday  Used for week type schedules |
| **on_the**  string | A description on when this schedule will run  Two strings separated by a space  First string is one of first, second, third, fourth, last  Second string is one of sunday, monday, tuesday, wednesday, thursday, friday  Used for month type schedules  Cannot be used with month_day_number parameters |
| **start_date**  string | The date to start the rule  Used for all frequencies  Format should be YYYY-MM-DD [HH:MM:SS] |
| **timezone**  string | The timezone to use for this rule  Used for all frequencies  Format should be as US/Eastern  Defaults to America/New_York |

## [Notes](schedule_rrule_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('awx.awx.schedule_rrule', term1, term2, key1=value1, key2=value2)` and `query('awx.awx.schedule_rrule', term1, term2, key1=value1, key2=value2)`

## [Examples](schedule_rrule_lookup.md#id6)

```yaml+jinja
- name: Create a string for a schedule
  debug:
    msg: "{{ query('awx.awx.schedule_rrule', 'none', start_date='1979-09-13 03:45:07') }}"
```

## [Return Value](schedule_rrule_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  string | String in the rrule format  Returned: success |

### Authors

- John Westcott IV (@john-westcott-iv)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
[Homepage](https://www.ansible.com/)
[Repository (Sources)](https://github.com/ansible/awx)
