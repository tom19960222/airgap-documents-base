---
collection: ansible
version: "8"
title: "community.general.random_mac filter – Generate a random MAC address"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/random_mac_filter.html
fetched_at: 2026-07-28T01:52:22+00:00
---
# community.general.random_mac filter – Generate a random MAC address

> **Note:**
>
> This filter plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.random_mac`.

- [Synopsis](random_mac_filter.md#synopsis)
- [Input](random_mac_filter.md#input)
- [Keyword parameters](random_mac_filter.md#keyword-parameters)
- [Examples](random_mac_filter.md#examples)
- [Return Value](random_mac_filter.md#return-value)

## [Synopsis](random_mac_filter.md#id1)

- Generates random networking interfaces MAC addresses for a given prefix.

## [Input](random_mac_filter.md#id2)

This describes the input of the filter, the value before `| community.general.random_mac`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A string prefix to use as a basis for the random MAC generated. |

## [Keyword parameters](random_mac_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | community.general.random_mac(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **seed**  string | A randomization seed to initialize the process, used to get repeatable results.  If no seed is provided, a system random source such as `/dev/urandom` is used. |

## [Examples](random_mac_filter.md#id4)

```yaml+jinja
- name: Random MAC given a prefix
  ansible.builtin.debug:
    msg: "{{ '52:54:00' | community.general.random_mac }}"
    # => '52:54:00:ef:1c:03'

- name: With a seed
  ansible.builtin.debug:
    msg: "{{ '52:54:00' | community.general.random_mac(seed=inventory_hostname) }}"
```

## [Return Value](random_mac_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | The generated MAC.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
