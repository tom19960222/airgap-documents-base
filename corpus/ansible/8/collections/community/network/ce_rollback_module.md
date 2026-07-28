---
collection: ansible
version: "8"
title: "community.network.ce_rollback module – Set a checkpoint or rollback to a checkpoint on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_rollback_module.html
fetched_at: 2026-07-28T01:55:49+00:00
---
# community.network.ce_rollback module – Set a checkpoint or rollback to a checkpoint on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_rollback`.

- [Synopsis](ce_rollback_module.md#synopsis)
- [Parameters](ce_rollback_module.md#parameters)
- [Notes](ce_rollback_module.md#notes)
- [Examples](ce_rollback_module.md#examples)
- [Return Values](ce_rollback_module.md#return-values)

## [Synopsis](ce_rollback_module.md#id1)

- This module offers the ability to set a configuration checkpoint file or rollback to a configuration checkpoint file on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_rollback

## [Parameters](ce_rollback_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string / required | The operation of configuration rollback.  **Choices:**   - `"rollback"` - `"clear"` - `"set"` - `"display"` - `"commit"` |
| **commit_id**  string | Specifies the label of the configuration rollback point to which system configurations are expected to roll back. The value is an integer that the system generates automatically. |
| **filename**  string | Specifies a configuration file for configuration rollback. The value is a string of 5 to 64 case-sensitive characters in the format of \*.zip, \*.cfg, or \*.dat, spaces not supported. |
| **label**  string | Specifies a user label for a configuration rollback point. The value is a string of 1 to 256 case-sensitive ASCII characters, spaces not supported. The value must start with a letter and cannot be presented in a single hyphen (-). |
| **last**  string | Specifies the number of configuration rollback points. The value is an integer that ranges from 1 to 80. |
| **oldest**  string | Specifies the number of configuration rollback points. The value is an integer that ranges from 1 to 80. |

## [Notes](ce_rollback_module.md#id3)

> **Note:**
>
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_rollback_module.md#id4)

```yaml+jinja
- name: Rollback module test
  hosts: cloudengine
  connection: local
  gather_facts: false
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

- name: Ensure commit_id is exist, and specifies the label of the configuration rollback point to
        which system configurations are expected to roll back.
  community.network.ce_rollback:
    commit_id: 1000000748
    action: rollback
    provider: "{{ cli }}"
```

## [Return Values](ce_rollback_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  **Returned:** always  **Sample:** `{"commitId": "1000000748", "userLabel": "abc"}` |
| **existing**  dictionary | k/v pairs of existing rollback  **Returned:** sometimes  **Sample:** `{"commitId": "1000000748", "userLabel": "abc"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** sometimes  **Sample:** `{"action": "rollback", "commit_id": "1000000748"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["rollback configuration to file a.cfg", "set configuration commit 1000000783 label ddd", "clear configuration commit 1000000783 label", "display configuration commit list"]` |

### Authors

- Li Yanfeng (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
