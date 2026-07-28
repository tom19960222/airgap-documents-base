---
collection: ansible
version: "8"
title: "sensu.sensu_go.package_name filter – Format package name"
source_url: https://docs.ansible.com/projects/ansible/8/collections/sensu/sensu_go/package_name_filter.html
fetched_at: 2026-07-28T02:53:42+00:00
---
# sensu.sensu_go.package_name filter – Format package name

> **Note:**
>
> This filter plugin is part of the [sensu.sensu_go collection](https://galaxy.ansible.com/ui/repo/published/sensu/sensu_go/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install sensu.sensu_go`.
>
> To use it in a playbook, specify: `sensu.sensu_go.package_name`.

New in sensu.sensu_go 1.13.2

- [Synopsis](package_name_filter.md#synopsis)
- [Input](package_name_filter.md#input)
- [Keyword parameters](package_name_filter.md#keyword-parameters)
- [Examples](package_name_filter.md#examples)
- [Return Value](package_name_filter.md#return-value)

## [Synopsis](package_name_filter.md#id1)

- Package name format function.
- The return value is a string respresenting package name and build version.

## [Input](package_name_filter.md#id2)

This describes the input of the filter, the value before `| sensu.sensu_go.package_name`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | Package type.  **Choices:**   - `"apt"` - `"yum"` |

## [Keyword parameters](package_name_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | sensu.sensu_go.package_name(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **build**  string / required | Package build. |
| **name**  string / required | Package name. |
| **version**  string / required | Package version. |

## [Examples](package_name_filter.md#id4)

```yaml+jinja
- name: Install apt component
  apt:
    name: "{{ 'apt' | sensu.sensu_go.package_name(name, version, build) }}"

- name: Install yum component
  yum:
    name: "{{ 'yum' | sensu.sensu_go.package_name(name, version, build) }}"
```

## [Return Value](package_name_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | Package name, version and build as a formatted string.  **Returned:** success |

### Authors

- Tadej Borovsak (@tadeboro)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
- [Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
