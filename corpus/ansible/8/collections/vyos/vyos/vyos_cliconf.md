---
collection: ansible
version: "8"
title: "vyos.vyos.vyos cliconf – Use vyos cliconf to run command on VyOS platform"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_cliconf.html
fetched_at: 2026-07-28T01:06:03+00:00
---
# vyos.vyos.vyos cliconf – Use vyos cliconf to run command on VyOS platform

> **Note:**
>
> This cliconf plugin is part of the [vyos.vyos collection](https://galaxy.ansible.com/ui/repo/published/vyos/vyos/) (version 4.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_cliconf.md#synopsis)
- [Parameters](vyos_cliconf.md#parameters)

## [Synopsis](vyos_cliconf.md#id1)

- This vyos plugin provides low level abstraction apis for sending and receiving CLI commands from VyOS network devices.

## [Parameters](vyos_cliconf.md#id2)

| Parameter | Comments |
| --- | --- |
| **config_commands**  list / elements=string  *added in vyos.vyos 2.0.0* | Specifies a list of commands that can make configuration changes to the target device.  When `ansible_network_single_user_mode` is enabled, if a command sent to the device is present in this list, the existing cache is invalidated.  **Default:** `[]`  **Configuration:**   - Variable: ansible_vyos_config_commands |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
