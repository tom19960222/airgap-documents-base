---
collection: ansible
version: "6"
title: "ansible.builtin.sequence lookup – generate a list based on a number sequence"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/sequence_lookup.html
fetched_at: 2026-07-27T16:44:23+00:00
---
# ansible.builtin.sequence lookup – generate a list based on a number sequence

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `sequence` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](sequence_lookup.md#synopsis)
- [Keyword parameters](sequence_lookup.md#keyword-parameters)
- [Examples](sequence_lookup.md#examples)
- [Return Value](sequence_lookup.md#return-value)

## [Synopsis](sequence_lookup.md#id1)

- generates a sequence of items. You can specify a start value, an end value, an optional “stride” value that specifies the number of steps to increment the sequence, and an optional printf-style format string.
- Arguments can be specified as key=value pair strings or as a shortcut form of the arguments string is also accepted: [start-]end[/stride][:format].
- Numerical values can be specified in decimal, hexadecimal (0x3f8) or octal (0600).
- Starting at version 1.9.2, negative strides are allowed.
- Generated items are strings. Use Jinja2 filters to convert items to preferred type, e.g. `{{ 1 + item|int }}`.
- See also Jinja2 `range` filter as an alternative.

## [Keyword parameters](sequence_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('ansible.builtin.sequence', key1=value1, key2=value2, ...)` and `query('ansible.builtin.sequence', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **count**  integer | number of elements in the sequence, this is not to be used with end  Default: `0` |
| **end**  integer | number at which to end the sequence, dont use this with count  Default: `0` |
| **format**  string | return a string with the generated number formatted in |
| **start**  integer | number at which to start the sequence  Default: `0` |
| **stride**  integer | increments between sequence numbers, the default is 1 unless the end is less than the start, then it is -1. |

## [Examples](sequence_lookup.md#id3)

```yaml+jinja
- name: create some test users
  ansible.builtin.user:
    name: "{{ item }}"
    state: present
    groups: "evens"
  with_sequence: start=0 end=32 format=testuser%02x

- name: create a series of directories with even numbers for some reason
  ansible.builtin.file:
    dest: "/var/stuff/{{ item }}"
    state: directory
  with_sequence: start=4 end=16 stride=2

- name: a simpler way to use the sequence plugin create 4 groups
  ansible.builtin.group:
    name: "group{{ item }}"
    state: present
  with_sequence: count=4

- name: the final countdown
  ansible.builtin.debug:
    msg: "{{item}} seconds to detonation"
  with_sequence: start=10 end=0 stride=-1

- name: Use of variable
  ansible.builtin.debug:
    msg: "{{ item }}"
  with_sequence: start=1 end="{{ end_at }}"
  vars:
    - end_at: 10
```

## [Return Value](sequence_lookup.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | A list containing generated sequence of items  Returned: success |

### Authors

- Jayson Vantuyl

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
