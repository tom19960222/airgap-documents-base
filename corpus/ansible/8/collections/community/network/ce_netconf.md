---
collection: ansible
version: "8"
title: "community.network.ce netconf – Use ce netconf plugin to run netconf commands on Huawei Cloudengine platform"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_netconf.html
fetched_at: 2026-07-28T01:58:13+00:00
---
# community.network.ce netconf – Use ce netconf plugin to run netconf commands on Huawei Cloudengine platform

> **Note:**
>
> This netconf plugin is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ce`.

- [Synopsis](ce_netconf.md#synopsis)
- [Parameters](ce_netconf.md#parameters)

## [Synopsis](ce_netconf.md#id1)

- This ce plugin provides low level abstraction apis for sending and receiving netconf commands from Huawei Cloudengine network devices.

## [Parameters](ce_netconf.md#id2)

| Parameter | Comments |
| --- | --- |
| **ncclient_device_handler**  string | Specifies the ncclient device handler name for Huawei Cloudengine. To identify the ncclient device handler name refer ncclient library documentation.  **Default:** `"huawei"` |

### Authors

- Unknown

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
