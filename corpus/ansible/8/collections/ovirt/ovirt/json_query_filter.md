---
collection: ansible
version: "8"
title: "ovirt.ovirt.json_query filter – Copy of community.general.json_query"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/json_query_filter.html
fetched_at: 2026-07-28T02:50:24+00:00
---
# ovirt.ovirt.json_query filter – Copy of community.general.json_query

> **Note:**
>
> This filter plugin is part of the [ovirt.ovirt collection](https://galaxy.ansible.com/ui/repo/published/ovirt/ovirt/) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ovirt.ovirt`.
>
> To use it in a playbook, specify: `ovirt.ovirt.json_query`.

- [Synopsis](json_query_filter.md#synopsis)
- [Input](json_query_filter.md#input)
- [Examples](json_query_filter.md#examples)
- [Return Value](json_query_filter.md#return-value)

## [Synopsis](json_query_filter.md#id1)

- Copy of community.general.json_query used internally in the collection to ease RPM packaging, so we don’t need to package/release/support the whole community.general collection for RHV customers
- The original can be found at link <https://github.com/ansible-collections/community.general/blob/main/plugins/filter/json_query.py>

## [Input](json_query_filter.md#id2)

This describes the input of the filter, the value before `| ovirt.ovirt.json_query`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | Value to be converted |

## [Examples](json_query_filter.md#id3)

```yaml+jinja
Query data using jmespath query language ( http://jmespath.org ). Example:
- ansible.builtin.debug: msg="{{ instance | json_query(tagged_instances[*].block_device_mapping.*.volume_id') }}"
```

## [Return Value](json_query_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | query  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
