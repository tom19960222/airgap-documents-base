---
collection: ansible
version: "8"
title: "ansible.utils.ip4_hex filter – This filter is designed to convert IPv4 address to Hexadecimal notation with optional delimiter."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/ip4_hex_filter.html
fetched_at: 2026-07-28T01:09:48+00:00
---
# ansible.utils.ip4_hex filter – This filter is designed to convert IPv4 address to Hexadecimal notation with optional delimiter.

> **Note:**
>
> This filter plugin is part of the [ansible.utils collection](https://galaxy.ansible.com/ui/repo/published/ansible/utils/) (version 2.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.utils`.
>
> To use it in a playbook, specify: `ansible.utils.ip4_hex`.

New in ansible.utils 2.5.0

- [Synopsis](ip4_hex_filter.md#synopsis)
- [Keyword parameters](ip4_hex_filter.md#keyword-parameters)
- [Examples](ip4_hex_filter.md#examples)
- [Return Value](ip4_hex_filter.md#return-value)

## [Synopsis](ip4_hex_filter.md#id1)

- This filter convert IPv4 address to Hexadecimal notation with optional delimiter

## [Keyword parameters](ip4_hex_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.ip4_hex(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **arg**  string / required | IPv4 address. |
| **delimiter**  string | You can provide a single argument to each ip4_hex() filter as delimiter.  **Default:** `""` |

## [Examples](ip4_hex_filter.md#id3)

```yaml+jinja
#### examples
# ip4_hex convert IPv4 address to Hexadecimal notation with optional delimiter
- debug:
    msg: "{{ '192.168.1.5' | ansible.utils.ip4_hex }}"

# ip4_hex with delimiter
- debug:
    msg: "{{ '192.168.1.5' | ansible.utils.ip4_hex(':') }}"

# TASK [debug] ************************************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_ip4_hex.yaml:7
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "c0a80105"
# }
#
# TASK [debug] ************************************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_ip4_hex.yaml:11
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "c0:a8:01:05"
# }
```

## [Return Value](ip4_hex_filter.md#id4)

| Key | Description |
| --- | --- |
| **data**  string | Returns IPv4 address to Hexadecimal notation.  **Returned:** success |

### Authors

- Ashwini Mhatre (@amhatre)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
