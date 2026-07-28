---
collection: ansible
version: "8"
title: "check_point.mgmt.checkpoint httpapi – HttpApi Plugin for Checkpoint devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/checkpoint_httpapi.html
fetched_at: 2026-07-28T01:05:35+00:00
---
# check_point.mgmt.checkpoint httpapi – HttpApi Plugin for Checkpoint devices

> **Note:**
>
> This httpapi plugin is part of the [check_point.mgmt collection](https://galaxy.ansible.com/ui/repo/published/check_point/mgmt/) (version 5.1.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.checkpoint`.

New in check_point.mgmt 2.8.0

- [Synopsis](checkpoint_httpapi.md#synopsis)
- [Parameters](checkpoint_httpapi.md#parameters)

## [Synopsis](checkpoint_httpapi.md#id1)

- This HttpApi plugin provides methods to connect to Checkpoint devices over a HTTP(S)-based api.

## [Parameters](checkpoint_httpapi.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Login with api-key instead of user & password  **Configuration:**   - Variable: ansible_api_key |
| **cloud_mgmt_id**  string | The Cloud Management ID  **Configuration:**   - Variable: ansible_cloud_mgmt_id |
| **domain**  string | Specifies the domain of the Check Point device  **Configuration:**   - Variable: ansible_checkpoint_domain |

### Authors

- Ansible Networking Team (@rcarrillocruz)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
