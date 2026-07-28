---
collection: ansible
version: "8"
title: "ansible.builtin.ternary filter – Ternary operation filter"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/ternary_filter.html
fetched_at: 2026-07-28T01:08:20+00:00
---
# ansible.builtin.ternary filter – Ternary operation filter

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `ternary`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.ternary` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](ternary_filter.md#synopsis)
- [Input](ternary_filter.md#input)
- [Positional parameters](ternary_filter.md#positional-parameters)
- [Keyword parameters](ternary_filter.md#keyword-parameters)
- [Notes](ternary_filter.md#notes)
- [Examples](ternary_filter.md#examples)
- [Return Value](ternary_filter.md#return-value)

## [Synopsis](ternary_filter.md#id1)

- Return the first value if the input is `True`, the second if `False`.

## [Input](ternary_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.ternary`.

| Parameter | Comments |
| --- | --- |
| **Input**  boolean / required | A boolean expression, must evaluate to `True` or `False`.  **Choices:**   - `false` - `true` |

## [Positional parameters](ternary_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.ternary(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **true_val**  any / required | Value to return if the input is `True`. |
| **false_val**  any | Value to return if the input is `False`. |

## [Keyword parameters](ternary_filter.md#id4)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.ternary(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **none_val**  any  *added in Ansible 2.8* | Value to return if the input is `None`. If not set, `None` will be treated as `False`. |

## [Notes](ternary_filter.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `input | ansible.builtin.ternary(positional1, positional2, key1=value1, key2=value2)`
> - Vars as values are evaluated even when not returned. This is due to them being evaluated before being passed into the filter.

## [Examples](ternary_filter.md#id6)

```yaml+jinja
# set first 10 volumes rw, rest as dp
volume_mode: "{{ (item|int < 11)|ternary('rw', 'dp') }}"

# choose correct vpc subnet id, note that vars as values are evaluated even if not returned
vpc_subnet_id: "{{ (ec2_subnet_type == 'public') | ternary(ec2_vpc_public_subnet_id, ec2_vpc_private_subnet_id) }}"

- name: service-foo, use systemd module unless upstart is present, then use old service module
  service:
    state: restarted
    enabled: yes
    use: "{{ (ansible_service_mgr == 'upstart') | ternary('service', 'systemd') }}"
```

## [Return Value](ternary_filter.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  any | The value indicated by the input.  **Returned:** success |

### Authors

- Brian Coca (@bcoca)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
