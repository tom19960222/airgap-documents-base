---
collection: ansible
version: "8"
title: "ansible.builtin.to_datetime filter – Get datetime from string"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/to_datetime_filter.html
fetched_at: 2026-07-28T01:08:21+00:00
---
# ansible.builtin.to_datetime filter – Get `datetime` from string

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `to_datetime`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.to_datetime` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](to_datetime_filter.md#synopsis)
- [Input](to_datetime_filter.md#input)
- [Keyword parameters](to_datetime_filter.md#keyword-parameters)
- [Notes](to_datetime_filter.md#notes)
- [Examples](to_datetime_filter.md#examples)
- [Return Value](to_datetime_filter.md#return-value)

## [Synopsis](to_datetime_filter.md#id1)

- Using the input string attempt to create a matching Python `datetime` object.

## [Input](to_datetime_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.to_datetime`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A string containing date time information. |

## [Keyword parameters](to_datetime_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.to_datetime(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **format**  string | `strformat` formatted string that describes the expected format of the input string. |

## [Notes](to_datetime_filter.md#id4)

> **Note:**
>
> - For a full list of format codes for working with Python date format strings, see [the Python documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).

## [Examples](to_datetime_filter.md#id5)

```yaml+jinja
# Get total amount of seconds between two dates. Default date format is %Y-%m-%d %H:%M:%S but you can pass your own format
secsdiff: '{{ (("2016-08-14 20:00:12" | to_datetime) - ("2015-12-25" | to_datetime("%Y-%m-%d"))).total_seconds()  }}'

# Get remaining seconds after delta has been calculated. NOTE: This does NOT convert years, days, hours, and so on to seconds. For that, use total_seconds()
{{ (("2016-08-14 20:00:12" | to_datetime) - ("2016-08-14 18:00:00" | to_datetime)).seconds  }}
# This expression evaluates to "12" and not "132". Delta is 2 hours, 12 seconds

# get amount of days between two dates. This returns only number of days and discards remaining hours, minutes, and seconds
{{ (("2016-08-14 20:00:12" | to_datetime) - ("2015-12-25" | to_datetime('%Y-%m-%d'))).days  }}
```

## [Return Value](to_datetime_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  any | `datetime` object from the represented value.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
