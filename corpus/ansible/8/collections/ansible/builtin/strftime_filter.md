---
collection: ansible
version: "8"
title: "ansible.builtin.strftime filter – date formating"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/strftime_filter.html
fetched_at: 2026-07-28T01:08:18+00:00
---
# ansible.builtin.strftime filter – date formating

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `strftime`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.strftime` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](strftime_filter.md#synopsis)
- [Input](strftime_filter.md#input)
- [Positional parameters](strftime_filter.md#positional-parameters)
- [Notes](strftime_filter.md#notes)
- [Examples](strftime_filter.md#examples)
- [Return Value](strftime_filter.md#return-value)

## [Synopsis](strftime_filter.md#id1)

- Using Python’s `strftime` function, take a data formating string and a date/time to create a formated date.

## [Input](strftime_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.strftime`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A formating string following `stftime` conventions.  See [the Python documentation](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) for a reference. |

## [Positional parameters](strftime_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.strftime(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **second**  integer | Datetime in seconds from `epoch` to format, if not supplied `gmttime/localtime` will be used. |
| **utc**  boolean | Whether time supplied is in UTC.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](strftime_filter.md#id4)

> **Note:**
>
> - This is a passthrough to Python’s `stftime`, for a complete set of formatting options go to <https://strftime.org/>.

## [Examples](strftime_filter.md#id5)

```yaml+jinja
# for a complete set of features go to  https://strftime.org/

# Display year-month-day
{{ '%Y-%m-%d' | strftime }}
# => "2021-03-19"

# Display hour:min:sec
{{ '%H:%M:%S' | strftime }}
# => "21:51:04"

# Use ansible_date_time.epoch fact
{{ '%Y-%m-%d %H:%M:%S' | strftime(ansible_date_time.epoch) }}
# => "2021-03-19 21:54:09"

# Use arbitrary epoch value
{{ '%Y-%m-%d' | strftime(0) }}          # => 1970-01-01
{{ '%Y-%m-%d' | strftime(1441357287) }} # => 2015-09-04

# complex examples
vars:
  date1: '2022-11-15T03:23:13.686956868Z'
  date2: '2021-12-15T16:06:24.400087Z'
  date_short: '{{ date1|regex_replace("([^.]+)(\.\d{6})(\d*)(.+)", "\1\2\4") }}' #shorten microseconds
  iso8601format: '%Y-%m-%dT%H:%M:%S.%fZ'
  date_diff_isoed: '{{ (date1|to_datetime(isoformat) - date2|to_datetime(isoformat)).total_seconds() }}'
```

## [Return Value](strftime_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  string | A formatted date/time string.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
