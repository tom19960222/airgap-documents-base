---
collection: ansible
version: "6"
title: "cisco.ios.ios cliconf – Use ios cliconf to run command on Cisco IOS platform"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_cliconf.html
fetched_at: 2026-07-27T16:55:34+00:00
---
# cisco.ios.ios cliconf – Use ios cliconf to run command on Cisco IOS platform

> **Note:**
>
> This cliconf plugin is part of the [cisco.ios collection](https://galaxy.ansible.com/cisco/ios) (version 3.3.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios`.

New in cisco.ios 1.0.0

- [Synopsis](ios_cliconf.md#synopsis)
- [Parameters](ios_cliconf.md#parameters)

## [Synopsis](ios_cliconf.md#id1)

- This ios plugin provides low level abstraction apis for sending and receiving CLI commands from Cisco IOS network devices.

## [Parameters](ios_cliconf.md#id2)

| Parameter | Comments |
| --- | --- |
| **config_commands**  list / elements=string  added in cisco.ios 2.0.0 | Specifies a list of commands that can make configuration changes to the target device.  When `ansible_network_single_user_mode` is enabled, if a command sent to the device is present in this list, the existing cache is invalidated.  Default: `[]`  Configuration:   - Variable: ansible_ios_config_commands |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
