---
collection: ansible
version: "8"
title: "ansible.utils.previous_nth_usable filter – This filter returns the previous nth usable ip within a network described by value."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/previous_nth_usable_filter.html
fetched_at: 2026-07-28T01:09:59+00:00
---
# ansible.utils.previous_nth_usable filter – This filter returns the previous nth usable ip within a network described by value.

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
> To use it in a playbook, specify: `ansible.utils.previous_nth_usable`.

New in ansible.utils 2.5.0

- [Synopsis](previous_nth_usable_filter.md#synopsis)
- [Keyword parameters](previous_nth_usable_filter.md#keyword-parameters)
- [Examples](previous_nth_usable_filter.md#examples)
- [Return Value](previous_nth_usable_filter.md#return-value)

## [Synopsis](previous_nth_usable_filter.md#id1)

- This filter returns the previous nth usable ip within a network described by value.
- Use previous_nth_usable to find the previous nth usable IP address in relation to another within a range

## [Keyword parameters](previous_nth_usable_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.previous_nth_usable(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **offset**  integer | index value  previous nth usable IP address |
| **value**  string / required | subnets or individual address input for previous_nth_usable plugin |

## [Examples](previous_nth_usable_filter.md#id3)

```yaml+jinja
#### examples
- name: previous_nth_usable returns the second usable IP address for the given IP range
  debug:
    msg: "{{ '192.168.122.10/24' | ansible.utils.previous_nth_usable(2) }}"

- name: If there is no usable address, it returns an empty string.
  debug:
    msg: "{{ '192.168.122.1/24' | ansible.utils.previous_nth_usable(2) }}"

# TASK [previous_nth_usable returns the second usable IP address for the given IP range] **************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_previous_nth_usable.yaml:9
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "192.168.122.8"
# }
#
# TASK [If there is no usable address, it returns an empty string.] *******************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_previous_nth_usable.yaml:14
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": ""
# }
```

## [Return Value](previous_nth_usable_filter.md#id4)

| Key | Description |
| --- | --- |
| **data**  string | Returns the previous nth usable ip within a network described by value.  **Returned:** success |

### Authors

- Ashwini Mhatre (@amhatre)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
