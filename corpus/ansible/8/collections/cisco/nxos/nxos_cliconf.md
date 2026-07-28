---
collection: ansible
version: "8"
title: "cisco.nxos.nxos cliconf – Use NX-OS cliconf to run commands on Cisco NX-OS platform"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_cliconf.html
fetched_at: 2026-07-28T01:39:28+00:00
---
# cisco.nxos.nxos cliconf – Use NX-OS cliconf to run commands on Cisco NX-OS platform

> **Note:**
>
> This cliconf plugin is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_cliconf.md#synopsis)
- [Parameters](nxos_cliconf.md#parameters)

## [Synopsis](nxos_cliconf.md#id1)

- This nxos plugin provides low level abstraction apis for sending and receiving CLI commands from Cisco NX-OS network devices.

## [Parameters](nxos_cliconf.md#id2)

| Parameter | Comments |
| --- | --- |
| **config_commands**  list / elements=string  *added in cisco.nxos 2.0.0* | Specifies a list of commands that can make configuration changes to the target device.  When `ansible_network_single_user_mode` is enabled, if a command sent to the device is present in this list, the existing cache is invalidated.  **Default:** `[]`  **Configuration:**   - Variable: ansible_nxos_config_commands |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
