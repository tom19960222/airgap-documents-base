---
collection: ansible
version: "6"
title: "cisco.asa.asa cliconf – Use asa cliconf to run command on Cisco ASA platform"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/asa/asa_cliconf.html
fetched_at: 2026-07-27T16:50:50+00:00
---
# cisco.asa.asa cliconf – Use asa cliconf to run command on Cisco ASA platform

> **Note:**
>
> This cliconf plugin is part of the [cisco.asa collection](https://galaxy.ansible.com/cisco/asa) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.asa`.
>
> To use it in a playbook, specify: `cisco.asa.asa`.

New in cisco.asa 1.0.0

- [Synopsis](asa_cliconf.md#synopsis)
- [Parameters](asa_cliconf.md#parameters)

## [Synopsis](asa_cliconf.md#id1)

- This asa plugin provides low level abstraction apis for sending and receiving CLI commands from Cisco ASA network devices.

## [Parameters](asa_cliconf.md#id2)

| Parameter | Comments |
| --- | --- |
| **config_commands**  list / elements=string  added in cisco.asa 2.0.0 | Specifies a list of commands that can make configuration changes to the target device.  When `ansible_network_single_user_mode` is enabled, if a command sent to the device is present in this list, the existing cache is invalidated.  Default: `[]`  Configuration:   - Variable: ansible_asa_config_commands |

### Authors

- Ansible Security Team (@ansible-security)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.asa/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.asa)
