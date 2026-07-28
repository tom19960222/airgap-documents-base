---
collection: ansible
version: "8"
title: "ansible.utils.reduce_on_network filter – This filter reduces a list of addresses to only the addresses that match a given network."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/reduce_on_network_filter.html
fetched_at: 2026-07-28T01:09:59+00:00
---
# ansible.utils.reduce_on_network filter – This filter reduces a list of addresses to only the addresses that match a given network.

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
> To use it in a playbook, specify: `ansible.utils.reduce_on_network`.

New in ansible.utils 2.5.0

- [Synopsis](reduce_on_network_filter.md#synopsis)
- [Keyword parameters](reduce_on_network_filter.md#keyword-parameters)
- [Examples](reduce_on_network_filter.md#examples)
- [Return Value](reduce_on_network_filter.md#return-value)

## [Synopsis](reduce_on_network_filter.md#id1)

- This filter reduces a list of addresses to only the addresses that match a given network.
- To check whether multiple addresses belong to a network, use the reduce_on_network filter.

## [Keyword parameters](reduce_on_network_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.reduce_on_network(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **network**  string | The network to validate against. |
| **value**  list / elements=string / required | the list of addresses to filter on. |

## [Examples](reduce_on_network_filter.md#id3)

```yaml+jinja
- name: To check whether multiple addresses belong to a network, use the reduce_on_network filter.
  debug:
    msg: "{{ ['192.168.0.34', '10.3.0.3', '192.168.2.34'] | ansible.utils.reduce_on_network( '192.168.0.0/24' ) }}"

# TASK [To check whether multiple addresses belong to a network, use the reduce_on_network filter.] ***********
# task path: /Users/amhatre/ansible-collections/playbooks/test_reduce_on_network.yaml:7
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": [
#         "192.168.0.34"
#     ]
# }
```

## [Return Value](reduce_on_network_filter.md#id4)

| Key | Description |
| --- | --- |
| **data**  boolean | Returns whether an address or a network passed as argument is in a network.  **Returned:** success |

### Authors

- Ashwini Mhatre (@amhatre)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
