---
collection: ansible
version: "8"
title: "ansible.utils.slaac filter – This filter returns the SLAAC address within a network for a given HW/MAC address."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/slaac_filter.html
fetched_at: 2026-07-28T01:10:01+00:00
---
# ansible.utils.slaac filter – This filter returns the SLAAC address within a network for a given HW/MAC address.

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
> To use it in a playbook, specify: `ansible.utils.slaac`.

New in ansible.utils 2.5.0

- [Synopsis](slaac_filter.md#synopsis)
- [Keyword parameters](slaac_filter.md#keyword-parameters)
- [Examples](slaac_filter.md#examples)
- [Return Value](slaac_filter.md#return-value)

## [Synopsis](slaac_filter.md#id1)

- This filter returns the SLAAC address within a network for a given HW/MAC address.
- The filter slaac() generates an IPv6 address for a given network and a MAC Address in Stateless Configuration.

## [Keyword parameters](slaac_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.slaac(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **query**  string | nth host |
| **value**  string / required | The network address or range to test against. |

## [Examples](slaac_filter.md#id3)

```yaml+jinja
#### examples
- name: The filter slaac() generates an IPv6 address for a given network and a MAC Address in Stateless Configuration.
  debug:
    msg: "{{ 'fdcf:1894:23b5:d38c:0000:0000:0000:0000' | slaac('c2:31:b3:83:bf:2b') }}"

# TASK [The filter slaac() generates an IPv6 address for a given network and a MAC Address in Stateless Configuration.] ***
# task path: /Users/amhatre/ansible-collections/playbooks/test_slaac.yaml:7
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "fdcf:1894:23b5:d38c:c031:b3ff:fe83:bf2b"
# }
```

## [Return Value](slaac_filter.md#id4)

| Key | Description |
| --- | --- |
| **data**  string | Returns the SLAAC address within a network for a given HW/MAC address.  **Returned:** success |

### Authors

- Ashwini Mhatre (@amhatre)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
