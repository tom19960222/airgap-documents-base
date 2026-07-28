---
collection: ansible
version: "8"
title: "ansible.utils.nthhost filter – This filter returns the nth host within a network described by value."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/nthhost_filter.html
fetched_at: 2026-07-28T01:09:57+00:00
---
# ansible.utils.nthhost filter – This filter returns the nth host within a network described by value.

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
> To use it in a playbook, specify: `ansible.utils.nthhost`.

New in ansible.utils 2.5.0

- [Synopsis](nthhost_filter.md#synopsis)
- [Keyword parameters](nthhost_filter.md#keyword-parameters)
- [Examples](nthhost_filter.md#examples)
- [Return Value](nthhost_filter.md#return-value)

## [Synopsis](nthhost_filter.md#id1)

- This filter returns the nth host within a network described by value. To return the nth ip from a network, use the filter nthhost.
- Nthhost also supports a negative value.

## [Keyword parameters](nthhost_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.nthhost(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **query**  string | nth host |
| **value**  string / required | The network address or range to test against. |

## [Examples](nthhost_filter.md#id3)

```yaml+jinja
#### examples
- name: To return the nth ip from a network, use the filter nthhost.
  debug:
    msg: "{{ '10.0.0.0/8' | ansible.utils.nthhost(305)  }}"

- name: nthhost also supports a negative value.
  debug:
    msg: "{{ '10.0.0.0/8' | ansible.utils.nthhost(-1) }}"

# TASK [To return the nth ip from a network, use the filter nthhost.] *****************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_nthhost.yaml:7
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "10.0.1.49"
# }
#
# TASK [nthhost also supports a negative value.] **************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_nthhost.yaml:11
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "10.255.255.255"
# }
```

## [Return Value](nthhost_filter.md#id4)

| Key | Description |
| --- | --- |
| **data**  string | Returns nth host from network  **Returned:** success |

### Authors

- Ashwini Mhatre (@amhatre)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
