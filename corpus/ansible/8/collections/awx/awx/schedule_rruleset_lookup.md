---
collection: ansible
version: "8"
title: "awx.awx.schedule_rruleset lookup – Generate an rruleset string"
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/schedule_rruleset_lookup.html
fetched_at: 2026-07-28T01:05:33+00:00
---
# awx.awx.schedule_rruleset lookup – Generate an rruleset string

> **Note:**
>
> This lookup plugin is part of the [awx.awx collection](https://galaxy.ansible.com/ui/repo/published/awx/awx/) (version 22.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](schedule_rruleset_lookup.md#ansible-collections-awx-awx-schedule-rruleset-lookup-requirements) for details.
>
> To use it in a playbook, specify: `awx.awx.schedule_rruleset`.

- [Synopsis](schedule_rruleset_lookup.md#synopsis)
- [Requirements](schedule_rruleset_lookup.md#requirements)
- [Terms](schedule_rruleset_lookup.md#terms)
- [Keyword parameters](schedule_rruleset_lookup.md#keyword-parameters)
- [Notes](schedule_rruleset_lookup.md#notes)
- [Examples](schedule_rruleset_lookup.md#examples)
- [Return Value](schedule_rruleset_lookup.md#return-value)

## [Synopsis](schedule_rruleset_lookup.md#id1)

- Returns a string based on criteria which represents an rrule

## [Requirements](schedule_rruleset_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- pytz
- python-dateutil >= 2.7.0

## [Terms](schedule_rruleset_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | The start date of the ruleset  Used for all frequencies  Format should be YYYY-MM-DD [HH:MM:SS] |

## [Keyword parameters](schedule_rruleset_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('awx.awx.schedule_rruleset', key1=value1, key2=value2, ...)` and `query('awx.awx.schedule_rruleset', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **rules**  list / elements=dictionary / required | Array of rules in the rruleset |
| **byhour**  string | The hours to run this schedule on  A comma-separated list which can contain values 0-23 |
| **byminute**  string | The minutes to run this schedule on  A comma-separated list which can contain values 0-59 |
| **bymonth**  string | The months this schedule will run on  A comma-separated list which can contain values 0-12 |
| **bymonthday**  string | The day of the month this schedule will run on  A comma-separated list which can contain values 0-31 |
| **bysetpos**  string | Specify an occurrence number, corresponding to the nth occurrence of the rule inside the frequency period.  A comma-separated list of positions (first, second, third, forth or last) |
| **byweekday**  string | The days to run this schedule on  A comma-separated list which can contain values sunday, monday, tuesday, wednesday, thursday, friday |
| **byweekno**  string | The week numbers to run this schedule on  A comma-separated list which can contain values as described in ISO8601 |
| **byyearday**  string | The year day numbers to run this schedule on  A comma-separated list which can contain values 0-366 |
| **end_on**  string | How to end this schedule  If this is not defined, this schedule will never end  If this is a positive integer, this schedule will end after this number of occurrences  If this is a date in the format YYYY-MM-DD [HH:MM:SS], this schedule ends after this date  Used for all types except none |
| **frequency**  string / required | The frequency of the schedule  none - Run this schedule once  minute - Run this schedule every x minutes  hour - Run this schedule every x hours  day - Run this schedule every x days  week - Run this schedule weekly  month - Run this schedule monthly  **Choices:**   - `"none"` - `"minute"` - `"hour"` - `"day"` - `"week"` - `"month"` |
| **include**  boolean | If this rule should be included (RRULE) or excluded (EXRULE)  **Choices:**   - `false` - `true` ← (default) |
| **interval**  integer | The repetition in months, weeks, days hours or minutes  Used for all types except none |
| **timezone**  string | The timezone to use for this rule  Used for all frequencies  Format should be as US/Eastern  Defaults to America/New_York |

## [Notes](schedule_rruleset_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('awx.awx.schedule_rruleset', term1, term2, key1=value1, key2=value2)` and `query('awx.awx.schedule_rruleset', term1, term2, key1=value1, key2=value2)`

## [Examples](schedule_rruleset_lookup.md#id6)

```yaml+jinja
- name: Create a ruleset for everyday except Sundays
  set_fact:
    complex_rule: "{{ query(awx.awx.schedule_rruleset, '2022-04-30 10:30:45', rules=rrules, timezone='UTC' ) }}"
  vars:
    rrules:
      - frequency: 'day'
        interval: 1
      - frequency: 'day'
        interval: 1
        byweekday: 'sunday'
        include: False
```

## [Return Value](schedule_rruleset_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  string | String in the rrule format  **Returned:** success |

### Authors

- John Westcott IV (@john-westcott-iv)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
