---
collection: ansible
version: "8"
title: "theforeman.foreman.cp_label filter – Convert strings to Candlepin labels"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/cp_label_filter.html
fetched_at: 2026-07-28T02:56:50+00:00
---
# theforeman.foreman.cp_label filter – Convert strings to Candlepin labels

> **Note:**
>
> This filter plugin is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
>
> To use it in a playbook, specify: `theforeman.foreman.cp_label`.

New in theforeman.foreman 0.1.0

- [Synopsis](cp_label_filter.md#synopsis)
- [Input](cp_label_filter.md#input)
- [Examples](cp_label_filter.md#examples)
- [Return Value](cp_label_filter.md#return-value)

## [Synopsis](cp_label_filter.md#id1)

- Converts an arbitrary string to a valid Candlepin label

## [Input](cp_label_filter.md#id2)

This describes the input of the filter, the value before `| theforeman.foreman.cp_label`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | String that should be converted |

## [Examples](cp_label_filter.md#id3)

```yaml+jinja
organization_label: "{{ 'Default Organization' | cp_label }}"
# => 'Default_Organization'
```

## [Return Value](cp_label_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | The converted Candlepin label  **Returned:** success |

### Authors

- Matthias Dellweg

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
