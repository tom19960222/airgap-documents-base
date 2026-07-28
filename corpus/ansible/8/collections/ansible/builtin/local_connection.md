---
collection: ansible
version: "8"
title: "ansible.builtin.local connection – execute on controller"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/local_connection.html
fetched_at: 2026-07-28T01:05:16+00:00
---
# ansible.builtin.local connection – execute on controller

> **Note:**
>
> This connection plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `local`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.local` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same connection plugin name.

- [Synopsis](local_connection.md#synopsis)
- [Parameters](local_connection.md#parameters)
- [Notes](local_connection.md#notes)

## [Synopsis](local_connection.md#id1)

- This connection plugin allows ansible to execute tasks on the Ansible ‘controller’ instead of on a remote host.

Aliases: redirected_local

## [Parameters](local_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **pipelining**  boolean | Pipelining reduces the number of connection operations required to execute a module on the remote server, by executing many Ansible modules without actual file transfers.  This can result in a very significant performance improvement when enabled.  However this can conflict with privilege escalation (become). For example, when using sudo operations you must first disable ‘requiretty’ in the sudoers file for the target hosts, which is why this feature is disabled by default.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   pipelining = false   ```  ```YAML+Jinja   [connection]   pipelining = false   ``` - Environment variable: [`ANSIBLE_PIPELINING`](../../../reference_appendices/config.md#envvar-ANSIBLE_PIPELINING) - Variable: ansible_pipelining |

## [Notes](local_connection.md#id3)

> **Note:**
>
> - The remote user is ignored, the user with which the ansible CLI was executed is used instead.

### Authors

- ansible (@core)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
