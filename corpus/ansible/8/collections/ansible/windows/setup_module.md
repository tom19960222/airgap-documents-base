---
collection: ansible
version: "8"
title: "ansible.windows.setup module – Gathers facts about remote hosts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/setup_module.html
fetched_at: 2026-07-28T01:10:26+00:00
---
# ansible.windows.setup module – Gathers facts about remote hosts

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ui/repo/published/ansible/windows/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.setup`.

- [Synopsis](setup_module.md#synopsis)
- [Parameters](setup_module.md#parameters)
- [Notes](setup_module.md#notes)
- [See Also](setup_module.md#see-also)
- [Examples](setup_module.md#examples)

## [Synopsis](setup_module.md#id1)

- This module is automatically called by playbooks to gather useful variables about remote hosts that can be used in playbooks. It can also be executed directly by `/usr/bin/ansible` to check what variables are available to a host. Ansible provides many *facts* about the system, automatically.

## [Parameters](setup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **_measure_subset**  boolean | For internal use  **Choices:**   - `false` ← (default) - `true` |
| **fact_path**  path | Path used for local ansible facts (`*.ps1` or `*.json`) - files in this dir will be run (if a ps1) or read (if a json) and their results be added to the return facts.  The returned fact will be named after the local file (without the extension suffix), e.g. `ansible_my_fact`. |
| **gather_subset**  list / elements=string | If supplied, restrict the additional facts collected to the given subset.  Can specify a list of values to specify a larger subset.  Values can also be used with an initial `!` to specify that that specific subset should not be collected.  To avoid collecting even the min subset, specify `!all,!min`.  To collect only specific facts, use `!all,!min`, and specify the particular fact subsets.  **Default:** `["all"]` |
| **gather_timeout**  integer | Set the default timeout in seconds for individual fact gathering.  **Default:** `10` |

## [Notes](setup_module.md#id3)

> **Note:**
>
> - More ansible facts will be added with successive releases. If *facter* is installed, variables from these programs will also be snapshotted into the JSON file for usage in templating. These variables are prefixed with `facter_` so it’s easy to tell their source. All variables are bubbled up to the caller.
> - Some facts may be unavailable if running under a limited account.
> - For more information about delegated facts, please check <https://docs.ansible.com/ansible/latest/user_guide/playbooks_delegation.html#delegating-facts>.

## [See Also](setup_module.md#id4)

> **See also:**
>
> [ansible.builtin.setup](../builtin/setup_module.md#ansible-collections-ansible-builtin-setup-module)
> :   Gathers facts about remote hosts.

## [Examples](setup_module.md#id5)

```yaml+jinja
- name: run the setup facts
  ansible.builtin.setup:
```

### Authors

- Ansible Core Team

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
