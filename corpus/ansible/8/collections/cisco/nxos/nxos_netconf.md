---
collection: ansible
version: "8"
title: "cisco.nxos.nxos netconf – Use nxos netconf plugin to run netconf commands on Cisco NX-OS platform."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_netconf.html
fetched_at: 2026-07-28T01:39:30+00:00
---
# cisco.nxos.nxos netconf – Use nxos netconf plugin to run netconf commands on Cisco NX-OS platform.

> **Note:**
>
> This netconf plugin is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos`.

New in cisco.nxos 2.3.0

- [Synopsis](nxos_netconf.md#synopsis)
- [Parameters](nxos_netconf.md#parameters)

## [Synopsis](nxos_netconf.md#id1)

- This nxos plugin provides low level abstraction apis for sending and receiving netconf commands from Cisco NX-OS network devices.

## [Parameters](nxos_netconf.md#id2)

| Parameter | Comments |
| --- | --- |
| **ncclient_device_handler**  string | Specifies the ncclient device handler name for Cisco NX-OS network os. To identify the ncclient device handler name refer ncclient library documentation.  **Default:** `"nexus"` |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
