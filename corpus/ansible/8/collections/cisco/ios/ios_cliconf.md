---
collection: ansible
version: "8"
title: "cisco.ios.ios cliconf – Use ios cliconf to run command on Cisco IOS platform"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_cliconf.html
fetched_at: 2026-07-28T01:26:32+00:00
---
# cisco.ios.ios cliconf – Use ios cliconf to run command on Cisco IOS platform

> **Note:**
>
> This cliconf plugin is part of the [cisco.ios collection](https://galaxy.ansible.com/ui/repo/published/cisco/ios/) (version 4.6.1).
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
- [Examples](ios_cliconf.md#examples)

## [Synopsis](ios_cliconf.md#id1)

- This ios plugin provides low level abstraction apis for sending and receiving CLI commands from Cisco IOS network devices.

## [Parameters](ios_cliconf.md#id2)

| Parameter | Comments |
| --- | --- |
| **commit_confirm_immediate**  boolean | Enable or disable commit confirm mode.  Confirms the configuration pushed after a custom/ default timeout.(default 1 minute).  For custom timeout configuration set commit_confirm_timeout value.  On commit_confirm_immediate default value for commit_confirm_timeout is considered 1 minute when variable in not explicitly declared.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - Environment variable: [`ANSIBLE_IOS_COMMIT_CONFIRM_IMMEDIATE`](../../environment_variables.md#envvar-ANSIBLE_IOS_COMMIT_CONFIRM_IMMEDIATE) - Variable: ansible_ios_commit_confirm_immediate |
| **commit_confirm_timeout**  integer | Commits the configuration on a trial basis for the time specified in minutes.  Using commit_confirm_timeout without specifying commit_confirm_immediate would need an explicit `configure confirm` using the ios_command module to confirm/commit the changes made.  Refer to example for a use case demonstration.  **Configuration:**   - Environment variable: [`ANSIBLE_IOS_COMMIT_CONFIRM_TIMEOUT`](../../environment_variables.md#envvar-ANSIBLE_IOS_COMMIT_CONFIRM_TIMEOUT) - Variable: ansible_ios_commit_confirm_timeout |
| **config_commands**  list / elements=string  *added in cisco.ios 2.0.0* | Specifies a list of commands that can make configuration changes to the target device.  When `ansible_network_single_user_mode` is enabled, if a command sent to the device is present in this list, the existing cache is invalidated.  **Default:** `[]`  **Configuration:**   - Variable: ansible_ios_config_commands |

## [Examples](ios_cliconf.md#id3)

```yaml+jinja
# NOTE - IOS waits for a `configure confirm` when the configure terminal
# command executed is `configure terminal revert timer <timeout>` within the timeout
# period for the configuration to commit successfully, else a rollback
# happens.

# Use commit confirm with timeout and confirm the commit explicitly

- name: Example commit confirmed
  vars:
    ansible_ios_commit_confirm_timeout: 1
  tasks:
    - name: "Commit confirmed with timeout"
      cisco.ios.ios_hostname:
        state: merged
        config:
          hostname: R1

    - name: "Confirm the Commit"
      cisco.ios.ios_command:
        commands:
          - configure confirm

# Commands fired
# - configure terminal revert timer 1 (cliconf specific)
# - hostname R1 (from hostname resource module)
# - configure confirm (from ios_command module)

# Use commit confirm with timeout and confirm the commit via cliconf

- name: Example commit confirmed
  vars:
    ansible_ios_commit_confirm_immediate: True
    ansible_ios_commit_confirm_timeout: 3
  tasks:
    - name: "Commit confirmed with timeout"
      cisco.ios.ios_hostname:
        state: merged
        config:
          hostname: R1

# Commands fired
# - configure terminal revert timer 3 (cliconf specific)
# - hostname R1 (from hostname resource module)
# - configure confirm (cliconf specific)

# Use commit confirm via cliconf using default timeout

- name: Example commit confirmed
  vars:
    ansible_ios_commit_confirm_immediate: True
  tasks:
    - name: "Commit confirmed with timeout"
      cisco.ios.ios_hostname:
        state: merged
        config:
          hostname: R1

# Commands fired
# - configure terminal revert timer 1 (cliconf specific with default timeout)
# - hostname R1 (from hostname resource module)
# - configure confirm (cliconf specific)
```

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
