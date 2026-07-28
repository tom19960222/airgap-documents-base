---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr netconf – Use iosxr netconf plugin to run netconf commands on Cisco IOSXR platform"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_netconf.html
fetched_at: 2026-07-28T01:27:02+00:00
---
# cisco.iosxr.iosxr netconf – Use iosxr netconf plugin to run netconf commands on Cisco IOSXR platform

> **Note:**
>
> This netconf plugin is part of the [cisco.iosxr collection](https://galaxy.ansible.com/ui/repo/published/cisco/iosxr/) (version 5.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_netconf.md#synopsis)
- [Parameters](iosxr_netconf.md#parameters)

## [Synopsis](iosxr_netconf.md#id1)

- This iosxr plugin provides low level abstraction apis for sending and receiving netconf commands from Cisco iosxr network devices.

## [Parameters](iosxr_netconf.md#id2)

| Parameter | Comments |
| --- | --- |
| **ncclient_device_handler**  string | Specifies the ncclient device handler name for Cisco iosxr network os. To identify the ncclient device handler name refer ncclient library documentation.  **Default:** `"iosxr"` |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
