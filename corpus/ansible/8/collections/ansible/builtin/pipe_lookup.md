---
collection: ansible
version: "8"
title: "ansible.builtin.pipe lookup – read output from a command"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/pipe_lookup.html
fetched_at: 2026-07-28T01:08:35+00:00
---
# ansible.builtin.pipe lookup – read output from a command

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `pipe`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.pipe` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](pipe_lookup.md#synopsis)
- [Terms](pipe_lookup.md#terms)
- [Notes](pipe_lookup.md#notes)
- [Examples](pipe_lookup.md#examples)
- [Return Value](pipe_lookup.md#return-value)

## [Synopsis](pipe_lookup.md#id1)

- Run a command and return the output.

## [Terms](pipe_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | command(s) to run. |

## [Notes](pipe_lookup.md#id3)

> **Note:**
>
> - Like all lookups this runs on the Ansible controller and is unaffected by other keywords, such as become, so if you need to different permissions you must change the command or run Ansible as another user.
> - Alternatively you can use a shell/command task that runs against localhost and registers the result.
> - Pipe lookup internally invokes Popen with shell=True (this is required and intentional). This type of invocation is considered a security issue if appropriate care is not taken to sanitize any user provided or variable input. It is strongly recommended to pass user input or variable input via quote filter before using with pipe lookup. See example section for this. Read more about this [Bandit B602 docs](https://bandit.readthedocs.io/en/latest/plugins/b602_subprocess_popen_with_shell_equals_true.html)

## [Examples](pipe_lookup.md#id4)

```yaml+jinja
- name: raw result of running date command
  ansible.builtin.debug:
    msg: "{{ lookup('ansible.builtin.pipe', 'date') }}"

- name: Always use quote filter to make sure your variables are safe to use with shell
  ansible.builtin.debug:
    msg: "{{ lookup('ansible.builtin.pipe', 'getent passwd ' + myuser | quote ) }}"
```

## [Return Value](pipe_lookup.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | stdout from command  **Returned:** success |

### Authors

- Daniel Hokka Zakrisson

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
