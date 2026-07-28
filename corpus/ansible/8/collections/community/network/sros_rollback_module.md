---
collection: ansible
version: "8"
title: "community.network.sros_rollback module – Configure Nokia SR OS rollback"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/sros_rollback_module.html
fetched_at: 2026-07-28T01:57:54+00:00
---
# community.network.sros_rollback module – Configure Nokia SR OS rollback

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.sros_rollback`.

- [Synopsis](sros_rollback_module.md#synopsis)
- [Parameters](sros_rollback_module.md#parameters)
- [Notes](sros_rollback_module.md#notes)
- [Examples](sros_rollback_module.md#examples)
- [Return Values](sros_rollback_module.md#return-values)

## [Synopsis](sros_rollback_module.md#id1)

- Configure the rollback feature on remote Nokia devices running the SR OS operating system. this module provides a stateful implementation for managing the configuration of the rollback feature

Aliases: network.sros.sros_rollback

## [Parameters](sros_rollback_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **local_max_checkpoints**  string | The *local_max_checkpoints* argument configures the maximum number of rollback files that can be saved on the devices local compact flash. Valid values for this argument are in the range of 1 to 50 |
| **remote_max_checkpoints**  string | The *remote_max_checkpoints* argument configures the maximum number of rollback files that can be transferred and saved to a remote location. Valid values for this argument are in the range of 1 to 50 |
| **rescue_location**  string | The *rescue_location* specifies the location of the rescue file. This argument supports any valid local or remote URL as specified in SR OS |
| **rollback_location**  string | The *rollback_location* specifies the location and filename of the rollback checkpoint files. This argument supports any valid local or remote URL as specified in SR OS |
| **state**  string | The *state* argument specifies the state of the configuration entries in the devices active configuration. When the state value is set to `true` the configuration is present in the devices active configuration. When the state value is set to `false` the configuration values are removed from the devices active configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](sros_rollback_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage Nokia SR OS Network devices see <https://www.ansible.com/ansible-nokia>.

## [Examples](sros_rollback_module.md#id4)

```yaml+jinja
---
- name: Configure rollback location
  community.network.sros_rollback:
    rollback_location: "cb3:/ansible"

- name: Remove all rollback configuration
  community.network.sros_rollback:
    state: absent
```

## [Return Values](sros_rollback_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **updates**  list / elements=string | The set of commands that will be pushed to the remote device  **Returned:** always  **Sample:** `["...", "..."]` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
