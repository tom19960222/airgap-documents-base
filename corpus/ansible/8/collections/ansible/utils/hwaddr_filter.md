---
collection: ansible
version: "8"
title: "ansible.utils.hwaddr filter – HWaddr / MAC address filters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/hwaddr_filter.html
fetched_at: 2026-07-28T01:09:46+00:00
---
# ansible.utils.hwaddr filter – HWaddr / MAC address filters

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
> To use it in a playbook, specify: `ansible.utils.hwaddr`.

New in ansible.utils 2.5.0

- [Synopsis](hwaddr_filter.md#synopsis)
- [Keyword parameters](hwaddr_filter.md#keyword-parameters)
- [Examples](hwaddr_filter.md#examples)
- [Return Value](hwaddr_filter.md#return-value)

## [Synopsis](hwaddr_filter.md#id1)

- This filter check if string is a HW/MAC address and filter it
- You can use the hwaddr() filter to check if a given string is a MAC address or convert it between various formats.

## [Keyword parameters](hwaddr_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.hwaddr(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **alias**  string | alias  **Default:** `"hwaddr"` |
| **query**  string | query string. Example. cisco,linux,unix etc  **Default:** `""` |
| **value**  string / required | HW/MAC address. |

## [Examples](hwaddr_filter.md#id3)

```yaml+jinja
#### examples
- name: Check if given string is a MAC address
  debug:
    msg: "{{ '1a:2b:3c:4d:5e:6f' | ansible.utils.hwaddr }}"

- name: Convert HW address to Cisco format
  debug:
    msg: "{{ '1a:2b:3c:4d:5e:6f' | ansible.utils.hwaddr('cisco') }}"

# TASK [Check if given string is a MAC address] ***************************************************************
# ok: [localhost] => {
#     "msg": "1a:2b:3c:4d:5e:6f"
# }
#
# TASK [Convert HW address to Cisco format] ******************************************************************
# ok: [localhost] => {
#     "msg": "1a2b.3c4d.5e6f"
# }
```

## [Return Value](hwaddr_filter.md#id4)

| Key | Description |
| --- | --- |
| **data**  string | mac/Hw address  **Returned:** success |

### Authors

- Ashwini Mhatre (@amhatre)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
