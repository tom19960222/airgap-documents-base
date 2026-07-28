---
collection: ansible
version: "6"
title: "ansible.builtin.lines lookup – read lines from command"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/lines_lookup.html
fetched_at: 2026-07-27T16:44:21+00:00
---
# ansible.builtin.lines lookup – read lines from command

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `lines` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](lines_lookup.md#synopsis)
- [Terms](lines_lookup.md#terms)
- [Notes](lines_lookup.md#notes)
- [Examples](lines_lookup.md#examples)
- [Return Value](lines_lookup.md#return-value)

## [Synopsis](lines_lookup.md#id1)

- Run one or more commands and split the output into lines, returning them as a list

## [Terms](lines_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | command(s) to run |

## [Notes](lines_lookup.md#id3)

> **Note:**
>
> - Like all lookups, this runs on the Ansible controller and is unaffected by other keywords such as ‘become’. If you need to use different permissions, you must change the command or run Ansible as another user.
> - Alternatively, you can use a shell/command task that runs against localhost and registers the result.

## [Examples](lines_lookup.md#id4)

```yaml+jinja
- name: We could read the file directly, but this shows output from command
  ansible.builtin.debug: msg="{{ item }} is an output line from running cat on /etc/motd"
  with_lines: cat /etc/motd

- name: More useful example of looping over a command result
  ansible.builtin.shell: "/usr/bin/frobnicate {{ item }}"
  with_lines:
    - "/usr/bin/frobnications_per_host --param {{ inventory_hostname }}"
```

## [Return Value](lines_lookup.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | lines of stdout from command  Returned: success |

### Authors

- Daniel Hokka Zakrisson

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
