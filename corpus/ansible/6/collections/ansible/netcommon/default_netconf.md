---
collection: ansible
version: "6"
title: "ansible.netcommon.default netconf – Use default netconf plugin to run standard netconf commands as per RFC"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/default_netconf.html
fetched_at: 2026-07-27T16:44:40+00:00
---
# ansible.netcommon.default netconf – Use default netconf plugin to run standard netconf commands as per RFC

> **Note:**
>
> This netconf plugin is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.default`.

New in ansible.netcommon 1.0.0

- [Synopsis](default_netconf.md#synopsis)
- [Parameters](default_netconf.md#parameters)

## [Synopsis](default_netconf.md#id1)

- This default plugin provides low level abstraction apis for sending and receiving netconf commands as per Netconf RFC specification.

## [Parameters](default_netconf.md#id2)

| Parameter | Comments |
| --- | --- |
| **ncclient_device_handler**  string | Specifies the ncclient device handler name for network os that support default netconf implementation as per Netconf RFC specification. To identify the ncclient device handler name refer ncclient library documentation.  Default: `"default"` |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
