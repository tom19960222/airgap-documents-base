---
collection: ansible
version: "6"
title: "community.network.ftd httpapi – HttpApi Plugin for Cisco ASA Firepower device"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ftd_httpapi.html
fetched_at: 2026-07-27T17:20:05+00:00
---
# community.network.ftd httpapi – HttpApi Plugin for Cisco ASA Firepower device

> **Note:**
>
> This httpapi plugin is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ftd`.

- [Synopsis](ftd_httpapi.md#synopsis)
- [Parameters](ftd_httpapi.md#parameters)

## [Synopsis](ftd_httpapi.md#id1)

- This HttpApi plugin provides methods to connect to Cisco ASA firepower devices over a HTTP(S)-based api.

## [Parameters](ftd_httpapi.md#id2)

| Parameter | Comments |
| --- | --- |
| **spec_path**  string | Specifies the api spec path of the FTD device  Default: `"/apispec/ngfw.json"`  Configuration:   - Variable: ansible_httpapi_ftd_spec_path |
| **token_path**  string | Specifies the api token path of the FTD device  Configuration:   - Variable: ansible_httpapi_ftd_token_path |

### Authors

- Ansible Networking Team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
