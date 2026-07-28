---
collection: ansible
version: "8"
title: "Lookups"
source_url: https://docs.ansible.com/projects/ansible/8/playbook_guide/playbooks_lookups.html
fetched_at: 2026-07-28T00:59:53+00:00
---
# Lookups

Lookup plugins retrieve data from outside sources such as files, databases, key/value stores, APIs, and other services. Like all templating, lookups execute and are evaluated on the Ansible control machine. Ansible makes the data returned by a lookup plugin available using the standard templating system. Before Ansible 2.5, lookups were mostly used indirectly in `with_<lookup>` constructs for looping. Starting with Ansible 2.5, lookups are used more explicitly as part of Jinja2 expressions fed into the `loop` keyword.

## Using lookups in variables

You can populate variables using lookups. Ansible evaluates the value each time it is executed in a task (or template).

```yaml+jinja
vars:
  motd_value: "{{ lookup('file', '/etc/motd') }}"
tasks:
  - debug:
      msg: "motd value is {{ motd_value }}"
```

For more details and a list of lookup plugins in ansible-core, see [Working with plugins](../plugins/plugins.md#plugins-lookup). You may also find lookup plugins in collections. You can review a list of lookup plugins installed on your control machine with the command `ansible-doc -l -t lookup`.

> **See also:**
>
> [Working with playbooks](playbooks.md#working-with-playbooks)
> :   An introduction to playbooks
>
> [Conditionals](playbooks_conditionals.md#playbooks-conditionals)
> :   Conditional statements in playbooks
>
> [Using Variables](playbooks_variables.md#playbooks-variables)
> :   All about variables
>
> [Loops](playbooks_loops.md#playbooks-loops)
> :   Looping in playbooks
>
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the Google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
