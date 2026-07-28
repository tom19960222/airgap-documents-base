---
collection: ansible
version: "8"
title: "microsoft.ad.as_guid filter – Converts an LDAP value to a GUID string"
source_url: https://docs.ansible.com/projects/ansible/8/collections/microsoft/ad/as_guid_filter.html
fetched_at: 2026-07-28T02:40:56+00:00
---
# microsoft.ad.as_guid filter – Converts an LDAP value to a GUID string

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
> To use it in a playbook, specify: `microsoft.ad.as_guid`.

New in microsoft.ad 1.1.0

- [Synopsis](as_guid_filter.md#synopsis)
- [Input](as_guid_filter.md#input)
- [See Also](as_guid_filter.md#see-also)
- [Examples](as_guid_filter.md#examples)
- [Return Value](as_guid_filter.md#return-value)

## [Synopsis](as_guid_filter.md#id1)

- Converts an LDAP string or raw value to a guid string.
- Should be used with the `microsoft.ad.ldap` plugin to convert attribute values to a guid string.

## [Input](as_guid_filter.md#id2)

This describes the input of the filter, the value before `| microsoft.ad.as_guid`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | The LDAP attribute bytes or string value representing a GUID stored in LDAP.  If using a string as input, it must be a base64 string representing the GUIDs bytes. |

## [See Also](as_guid_filter.md#id3)

> **See also:**
>
> [microsoft.ad.as_datetime](as_datetime_filter.md#ansible-collections-microsoft-ad-as-datetime-filter)
> :   microsoft.ad.as_datetime filter
>
> [microsoft.ad.as_sid](as_sid_filter.md#ansible-collections-microsoft-ad-as-sid-filter)
> :   microsoft.ad.as_sid filter
>
> [microsoft.ad.ldap](ldap_inventory.md#ansible-collections-microsoft-ad-ldap-inventory)
> :   microsoft.ad.ldap inventory

## [Examples](as_guid_filter.md#id4)

```yaml+jinja
# This is an example used in the microsoft.ad.ldap plugin

attributes:
  objectGuid: raw | microsoft.ad.as_guid
```

## [Return Value](as_guid_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | The guid string value(s).  **Returned:** success |

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
