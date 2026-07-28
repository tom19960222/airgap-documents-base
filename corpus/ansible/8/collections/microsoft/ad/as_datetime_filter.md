---
collection: ansible
version: "8"
title: "microsoft.ad.as_datetime filter – Converts an LDAP value to a datetime string"
source_url: https://docs.ansible.com/projects/ansible/8/collections/microsoft/ad/as_datetime_filter.html
fetched_at: 2026-07-28T02:40:56+00:00
---
# microsoft.ad.as_datetime filter – Converts an LDAP value to a datetime string

> **Note:**
>
> This filter plugin is part of the [microsoft.ad collection](https://galaxy.ansible.com/ui/repo/published/microsoft/ad/) (version 1.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install microsoft.ad`.
>
> To use it in a playbook, specify: `microsoft.ad.as_datetime`.

New in microsoft.ad 1.1.0

- [Synopsis](as_datetime_filter.md#synopsis)
- [Input](as_datetime_filter.md#input)
- [Keyword parameters](as_datetime_filter.md#keyword-parameters)
- [See Also](as_datetime_filter.md#see-also)
- [Examples](as_datetime_filter.md#examples)
- [Return Value](as_datetime_filter.md#return-value)

## [Synopsis](as_datetime_filter.md#id1)

- Converts an LDAP integer or raw value to a datetime string.
- Should be used with the `microsoft.ad.ldap` plugin to convert attribute values to a datetime string.

## [Input](as_datetime_filter.md#id2)

This describes the input of the filter, the value before `| microsoft.ad.as_datetime`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | The LDAP attribute bytes or integer value representing a FILETIME integer stored in LDAP.  The resulting datetime will be set as a UTC datetime as that’s how the FILETIME value is stored in LDAP. |

## [Keyword parameters](as_datetime_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | microsoft.ad.as_datetime(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **format**  string | The string format to format the datetime object as.  Defaults to an ISO 8601 compatible string, for example `2023-02-06T07:39:09.195321+0000`.  **Default:** `"%Y-%m-%dT%H:%M:%S.%f%z"` |

## [See Also](as_datetime_filter.md#id4)

> **See also:**
>
> [microsoft.ad.as_guid](as_guid_filter.md#ansible-collections-microsoft-ad-as-guid-filter)
> :   microsoft.ad.as_guid filter
>
> [microsoft.ad.as_sid](as_sid_filter.md#ansible-collections-microsoft-ad-as-sid-filter)
> :   microsoft.ad.as_sid filter
>
> [microsoft.ad.ldap](ldap_inventory.md#ansible-collections-microsoft-ad-ldap-inventory)
> :   microsoft.ad.ldap inventory

## [Examples](as_datetime_filter.md#id5)

```yaml+jinja
# This is an example used in the microsoft.ad.ldap plugin

# Converting from the coerced value
attributes:
  pwdLastSet: this | microsoft.ad.as_datetime

# Converting from the raw bytes value
attributes:
  maxPwdAge: raw | microsoft.ad.as_datetime
```

## [Return Value](as_datetime_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  string | The datetime string value(s) formatted as per the *format* option.  **Returned:** success |

### Authors

- Jordan Borean (@jborean93)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/microsoft.ad/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/microsoft.ad)
- [Report an issue](https://github.com/ansible-collections/microsoft.ad/issues/new/choose)
- [Communication](index.md#communication-for-microsoft-ad)
