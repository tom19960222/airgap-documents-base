---
collection: ansible
version: "6"
title: "arista.eos.eos cliconf – Use eos cliconf to run command on Arista EOS platform"
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_cliconf.html
fetched_at: 2026-07-27T16:45:21+00:00
---
# arista.eos.eos cliconf – Use eos cliconf to run command on Arista EOS platform

> **Note:**
>
> This cliconf plugin is part of the [arista.eos collection](https://galaxy.ansible.com/arista/eos) (version 5.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos`.

New in arista.eos 1.0.0

- [Synopsis](eos_cliconf.md#synopsis)
- [Parameters](eos_cliconf.md#parameters)

## [Synopsis](eos_cliconf.md#id1)

- This eos plugin provides low level abstraction apis for sending and receiving CLI commands from Arista EOS network devices.

## [Parameters](eos_cliconf.md#id2)

| Parameter | Comments |
| --- | --- |
| **config_commands**  list / elements=string  added in arista.eos 2.0.0 | Specifies a list of commands that can make configuration changes to the target device.  When `ansible_network_single_user_mode` is enabled, if a command sent to the device is present in this list, the existing cache is invalidated.  Default: `[]`  Configuration:   - Variable: ansible_eos_config_commands |
| **eos_use_sessions**  boolean | Specifies if sessions should be used on remote host or not  Choices:   - `false` - `true` ← (default)   Configuration:   - Environment variable: [`ANSIBLE_EOS_USE_SESSIONS`](../../environment_variables.md#envvar-ANSIBLE_EOS_USE_SESSIONS) - Variable: ansible_eos_use_sessions |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
