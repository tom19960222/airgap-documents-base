---
collection: ansible
version: "8"
title: "arista.eos.eos httpapi – Use eAPI to run command on eos platform"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_httpapi.html
fetched_at: 2026-07-28T01:05:33+00:00
---
# arista.eos.eos httpapi – Use eAPI to run command on eos platform

> **Note:**
>
> This httpapi plugin is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos`.

New in arista.eos 1.0.0

- [Synopsis](eos_httpapi.md#synopsis)
- [Parameters](eos_httpapi.md#parameters)

## [Synopsis](eos_httpapi.md#id1)

- This eos plugin provides low level abstraction api’s for sending and receiving CLI commands with eos network devices.

## [Parameters](eos_httpapi.md#id2)

| Parameter | Comments |
| --- | --- |
| **eos_use_sessions**  boolean | Specifies if sessions should be used on remote host or not  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - Environment variable: [`ANSIBLE_EOS_USE_SESSIONS`](../../environment_variables.md#envvar-ANSIBLE_EOS_USE_SESSIONS) - Variable: ansible_eos_use_sessions |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
