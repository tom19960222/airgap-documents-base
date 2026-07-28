---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr cliconf – Use iosxr cliconf to run command on Cisco IOS XR platform"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_cliconf.html
fetched_at: 2026-07-28T01:27:01+00:00
---
# cisco.iosxr.iosxr cliconf – Use iosxr cliconf to run command on Cisco IOS XR platform

> **Note:**
>
> This cliconf plugin is part of the [cisco.iosxr collection](https://galaxy.ansible.com/ui/repo/published/cisco/iosxr/) (version 5.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_cliconf.md#synopsis)
- [Parameters](iosxr_cliconf.md#parameters)
- [Notes](iosxr_cliconf.md#notes)
- [Examples](iosxr_cliconf.md#examples)

## [Synopsis](iosxr_cliconf.md#id1)

- This iosxr plugin provides low level abstraction apis for sending and receiving CLI commands from Cisco IOS XR network devices.

## [Parameters](iosxr_cliconf.md#id2)

| Parameter | Comments |
| --- | --- |
| **commit_comment**  string | Adds comment to commit confirmed..  **Configuration:**   - Environment variable: [`ANSIBLE_IOSXR_COMMIT_COMMENT`](../../environment_variables.md#envvar-ANSIBLE_IOSXR_COMMIT_COMMENT) - Variable: ansible_iosxr_commit_comment |
| **commit_confirmed**  boolean | enable or disable commit confirmed mode  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - Environment variable: [`ANSIBLE_IOSXR_COMMIT_CONFIRMED`](../../environment_variables.md#envvar-ANSIBLE_IOSXR_COMMIT_CONFIRMED) - Variable: ansible_iosxr_commit_confirmed |
| **commit_confirmed_timeout**  integer | Commits the configuration on a trial basis for the time specified in seconds or minutes.  **Configuration:**   - Environment variable: [`ANSIBLE_IOSXR_COMMIT_CONFIRMED_TIMEOUT`](../../environment_variables.md#envvar-ANSIBLE_IOSXR_COMMIT_CONFIRMED_TIMEOUT) - Variable: ansible_iosxr_commit_confirmed_timeout |
| **commit_label**  string | Adds label to commit confirmed.  **Configuration:**   - Environment variable: [`ANSIBLE_IOSXR_COMMIT_LABEL`](../../environment_variables.md#envvar-ANSIBLE_IOSXR_COMMIT_LABEL) - Variable: ansible_iosxr_commit_label |
| **config_commands**  list / elements=string  *added in cisco.iosxr 2.0.0* | Specifies a list of commands that can make configuration changes to the target device.  When `ansible_network_single_user_mode` is enabled, if a command sent to the device is present in this list, the existing cache is invalidated.  **Default:** `[]`  **Configuration:**   - Variable: ansible_iosxr_config_commands |
| **config_mode_exclusive**  boolean | enable or disable config mode exclusive  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - Environment variable: [`ANSIBLE_IOSXR_CONFIG_MODE_EXCLUSIVE`](../../environment_variables.md#envvar-ANSIBLE_IOSXR_CONFIG_MODE_EXCLUSIVE) - Variable: ansible_iosxr_config_mode_exclusive |

## [Notes](iosxr_cliconf.md#id3)

> **Note:**
>
> - IOSXR commit confirmed command varies with IOSXR version releases, commit_comment and commit_label may or may not be valid together as per the device version.

## [Examples](iosxr_cliconf.md#id4)

```yaml+jinja
# Use commit confirmed within a task with timeout, label and comment

- name: Commit confirmed with a task
  vars:
    ansible_iosxr_commit_confirmed: True
    ansible_iosxr_commit_confirmed_timeout: 50
    ansible_iosxr_commit_label: TestLabel
    ansible_iosxr_commit_comment: I am a test comment
  cisco.iosxr.iosxr_logging_global:
    state: merged
    config:
      buffered:
        severity: errors #alerts #informational
      correlator:
        buffer_size: 2024

# Commands (cliconf specific)
# ["commit confirmed 50 label TestLabel comment I am a test comment"]

# Use commit within a task with label

- name: Commit label with a task
  vars:
    ansible_iosxr_commit_label: lblTest
  cisco.iosxr.iosxr_hostname:
    state: merged
    config:
      hostname: R1

# Commands (cliconf specific)
# ["commit label lblt1"]

# Use commit confirm with timeout and confirm the commit

# NOTE - IOSXR waits for a `commit` when the command
# executed is `commit confirmed <timeout>` within the timeout
# period for the config to commit successfully, else a rollback
# happens.

- name: Example commit confirmed
  vars:
    ansible_iosxr_commit_confirmed: True
    ansible_iosxr_commit_confirmed_timeout: 60
  tasks:
    - name: "Commit confirmed with timeout"
      cisco.iosxr.iosxr_hostname:
        state: merged
        config:
          hostname: R1

    - name: "Confirm the Commit"
      cisco.iosxr.iosxr_command:
        commands:
          - commit

# Commands (cliconf specific)
# ["commit confirmed 60"]

# Use exclusive mode with a task

- name: Configure exclusive mode with a task
  vars:
    ansible_iosxr_config_mode_exclusive: True
  cisco.iosxr.iosxr_interfaces:
    state: merged
    config:
      - name: GigabitEthernet0/0/0/2
        description: Configured via Ansible
      - name: GigabitEthernet0/0/0/3
        description: Configured via Ansible

# Commands (cliconf specific)
# ["configure exclusive"]

# Use Replace option with commit confirmed

# NOTE - IOSXR waits for a `commit` when the command
# executed is `commit replace confirmed <timeout>` within the timeout
# period for the config to commit successfully, else a rollback
# happens.
# This option is supported by only iosxr_config module

- name: Example replace config with commit confirmed
  vars:
    ansible_iosxr_commit_confirmed: True
    ansible_iosxr_commit_confirmed_timeout: 60
  tasks:
    - name: "Replace config with Commit confirmed"
      cisco.iosxr.iosxr_config:
        src: 'replace_running_cfg_iosxr.txt'
        replace: config

    - name: "Confirm the Commit"
      cisco.iosxr.iosxr_command:
        commands:
          - commit
```

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
