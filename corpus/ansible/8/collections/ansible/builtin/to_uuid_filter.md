---
collection: ansible
version: "8"
title: "ansible.builtin.to_uuid filter – namespaced UUID generator"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/to_uuid_filter.html
fetched_at: 2026-07-28T01:08:21+00:00
---
# ansible.builtin.to_uuid filter – namespaced UUID generator

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `to_uuid`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.to_uuid` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

New in Ansible 2.9

- [Synopsis](to_uuid_filter.md#synopsis)
- [Input](to_uuid_filter.md#input)
- [Positional parameters](to_uuid_filter.md#positional-parameters)
- [Examples](to_uuid_filter.md#examples)
- [Return Value](to_uuid_filter.md#return-value)

## [Synopsis](to_uuid_filter.md#id1)

- Use to generate namespeced Universal Unique ID.

## [Input](to_uuid_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.to_uuid`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | String to use as base fo the UUID. |

## [Positional parameters](to_uuid_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.to_uuid(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **namespace**  string | UUID namespace to use.  **Default:** `"361E6D51-FAEC-444A-9079-341386DA8E2E"` |

## [Examples](to_uuid_filter.md#id4)

```yaml+jinja
# To create a namespaced UUIDv5
uuid: "{{ string | to_uuid(namespace='11111111-2222-3333-4444-555555555555') }}"

# To create a namespaced UUIDv5 using the default Ansible namespace '361E6D51-FAEC-444A-9079-341386DA8E2E'
uuid: "{{ string | to_uuid }}"
```

## [Return Value](to_uuid_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | Generated UUID.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
