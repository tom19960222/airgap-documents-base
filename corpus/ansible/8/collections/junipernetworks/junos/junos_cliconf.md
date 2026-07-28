---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos cliconf – Use junos cliconf to run command on Juniper Junos OS platform"
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_cliconf.html
fetched_at: 2026-07-28T02:40:02+00:00
---
# junipernetworks.junos.junos cliconf – Use junos cliconf to run command on Juniper Junos OS platform

> **Note:**
>
> This cliconf plugin is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos/) (version 5.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_cliconf.md#synopsis)
- [Parameters](junos_cliconf.md#parameters)

## [Synopsis](junos_cliconf.md#id1)

- This junos plugin provides low level abstraction apis for sending and receiving CLI commands from Juniper Junos OS network devices.

## [Parameters](junos_cliconf.md#id2)

| Parameter | Comments |
| --- | --- |
| **config_commands**  list / elements=string  *added in junipernetworks.junos 2.0.0* | Specifies a list of commands that can make configuration changes to the target device.  When `ansible_network_single_user_mode` is enabled, if a command sent to the device is present in this list, the existing cache is invalidated.  **Default:** `[]`  **Configuration:**   - Variable: ansible_junos_config_commands |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
