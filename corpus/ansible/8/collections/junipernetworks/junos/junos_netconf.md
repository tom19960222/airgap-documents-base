---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos netconf – Use junos netconf plugin to run netconf commands on Juniper JUNOS platform"
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_netconf.html
fetched_at: 2026-07-28T01:05:50+00:00
---
# junipernetworks.junos.junos netconf – Use junos netconf plugin to run netconf commands on Juniper JUNOS platform

> **Note:**
>
> This netconf plugin is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos/) (version 5.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_netconf.md#synopsis)
- [Parameters](junos_netconf.md#parameters)

## [Synopsis](junos_netconf.md#id1)

- This junos plugin provides low level abstraction apis for sending and receiving netconf commands from Juniper JUNOS network devices.

## [Parameters](junos_netconf.md#id2)

| Parameter | Comments |
| --- | --- |
| **ncclient_device_handler**  string | Specifies the ncclient device handler name for Juniper junos network os. To identify the ncclient device handler name refer ncclient library documentation.  **Default:** `"junos"` |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
