---
collection: ansible
version: "8"
title: "ansible.builtin.random_choice lookup – return random element from list"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/random_choice_lookup.html
fetched_at: 2026-07-28T01:08:35+00:00
---
# ansible.builtin.random_choice lookup – return random element from list

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `random_choice`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.random_choice` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](random_choice_lookup.md#synopsis)
- [Examples](random_choice_lookup.md#examples)
- [Return Value](random_choice_lookup.md#return-value)

## [Synopsis](random_choice_lookup.md#id1)

- The ‘random_choice’ feature can be used to pick something at random. While it’s not a load balancer (there are modules for those), it can somewhat be used as a poor man’s load balancer in a MacGyver like situation.
- At a more basic level, they can be used to add chaos and excitement to otherwise predictable automation environments.

## [Examples](random_choice_lookup.md#id2)

```yaml+jinja
- name: Magic 8 ball for MUDs
  ansible.builtin.debug:
    msg: "{{ item }}"
  with_random_choice:
     - "go through the door"
     - "drink from the goblet"
     - "press the red button"
     - "do nothing"
```

## [Return Value](random_choice_lookup.md#id3)

| Key | Description |
| --- | --- |
| **Return value**  any | random item  **Returned:** success |

### Authors

- Michael DeHaan

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
