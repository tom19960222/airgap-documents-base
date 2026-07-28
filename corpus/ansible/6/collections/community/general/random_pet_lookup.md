---
collection: ansible
version: "6"
title: "community.general.random_pet lookup – Generates random pet names"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/random_pet_lookup.html
fetched_at: 2026-07-27T17:15:10+00:00
---
# community.general.random_pet lookup – Generates random pet names

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](random_pet_lookup.md#ansible-collections-community-general-random-pet-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.random_pet`.

New in community.general 3.1.0

- [Synopsis](random_pet_lookup.md#synopsis)
- [Requirements](random_pet_lookup.md#requirements)
- [Keyword parameters](random_pet_lookup.md#keyword-parameters)
- [Examples](random_pet_lookup.md#examples)
- [Return Value](random_pet_lookup.md#return-value)

## [Synopsis](random_pet_lookup.md#id1)

- Generates random pet names that can be used as unique identifiers for the resources.

## [Requirements](random_pet_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- petname <https://github.com/dustinkirkland/python-petname>

## [Keyword parameters](random_pet_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.random_pet', key1=value1, key2=value2, ...)` and `query('community.general.random_pet', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **length**  integer | The maximal length of every component of the pet name.  Values below 3 will be set to 3 by petname.  Default: `6` |
| **prefix**  string | A string to prefix with the name. |
| **separator**  string | The character to separate words in the pet name.  Default: `"-"` |
| **words**  integer | The number of words in the pet name.  Default: `2` |

## [Examples](random_pet_lookup.md#id4)

```yaml+jinja
- name: Generate pet name
  ansible.builtin.debug:
    var: lookup('community.general.random_pet')
  # Example result: 'loving-raptor'

- name: Generate pet name with 3 words
  ansible.builtin.debug:
    var: lookup('community.general.random_pet', words=3)
  # Example result: 'fully-fresh-macaw'

- name: Generate pet name with separator
  ansible.builtin.debug:
    var: lookup('community.general.random_pet', separator="_")
  # Example result: 'causal_snipe'

- name: Generate pet name with length
  ansible.builtin.debug:
    var: lookup('community.general.random_pet', length=7)
  # Example result: 'natural-peacock'
```

## [Return Value](random_pet_lookup.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | A one-element list containing a random pet name  Returned: success |

### Authors

- Abhijeet Kasurde (@Akasurde)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
