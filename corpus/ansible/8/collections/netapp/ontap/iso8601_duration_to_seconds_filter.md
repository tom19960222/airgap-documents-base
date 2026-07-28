---
collection: ansible
version: "8"
title: "netapp.ontap.iso8601_duration_to_seconds filter – Decode a ISO 8601 duration string as seconds"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/iso8601_duration_to_seconds_filter.html
fetched_at: 2026-07-28T02:43:45+00:00
---
# netapp.ontap.iso8601_duration_to_seconds filter – Decode a ISO 8601 duration string as seconds

> **Note:**
>
> This filter plugin is part of the [netapp.ontap collection](https://galaxy.ansible.com/ui/repo/published/netapp/ontap/) (version 22.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
>
> To use it in a playbook, specify: `netapp.ontap.iso8601_duration_to_seconds`.

New in netapp.ontap 21.24.0

- [Synopsis](iso8601_duration_to_seconds_filter.md#synopsis)
- [Input](iso8601_duration_to_seconds_filter.md#input)
- [Notes](iso8601_duration_to_seconds_filter.md#notes)
- [Examples](iso8601_duration_to_seconds_filter.md#examples)
- [Return Value](iso8601_duration_to_seconds_filter.md#return-value)

## [Synopsis](iso8601_duration_to_seconds_filter.md#id1)

- Decode a ISO 8601 duration string as seconds

## [Input](iso8601_duration_to_seconds_filter.md#id2)

This describes the input of the filter, the value before `| netapp.ontap.iso8601_duration_to_seconds`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A string to decode |

## [Notes](iso8601_duration_to_seconds_filter.md#id3)

> **Note:**
>
> - requires isodate and datetime python modules.
> - set filter_plugins path to <installation_path>/ansible_collections/netapp/ontap/plugins/filter in ansible.cfg.
> - documentation can be generated locally using a version of ansible-doc (2.14) that supports ‘-t filter’
> - ansible-doc -t filter netapp.ontap.iso8601_duration_to_seconds

## [Examples](iso8601_duration_to_seconds_filter.md#id4)

```yaml+jinja
# Decode a string
duration_in_seconds: "{{ 'P689DT13H57M44S' | netapp.ontap.iso8601_duration_to_seconds }}"

# Decode 'iso_duration' variable
duration_in_seconds: "{{ iso_duration | netapp.ontap.iso8601_duration_to_seconds }}"
```

## [Return Value](iso8601_duration_to_seconds_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  float | A float representing the number of seconds. The fractional part may represent milliseconds.  **Returned:** success |

### Authors

- NetApp Ansible Team (@carchi8py)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
