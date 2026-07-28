---
collection: ansible
version: "8"
title: "ansible.posix.rpm_ostree_upgrade module – Manage rpm-ostree upgrade transactions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/posix/rpm_ostree_upgrade_module.html
fetched_at: 2026-07-28T01:09:30+00:00
---
# ansible.posix.rpm_ostree_upgrade module – Manage rpm-ostree upgrade transactions

> **Note:**
>
> This module is part of the [ansible.posix collection](https://galaxy.ansible.com/ui/repo/published/ansible/posix/) (version 1.5.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.posix`.
> You need further requirements to be able to use this module,
> see [Requirements](rpm_ostree_upgrade_module.md#ansible-collections-ansible-posix-rpm-ostree-upgrade-module-requirements) for details.
>
> To use it in a playbook, specify: `ansible.posix.rpm_ostree_upgrade`.

New in ansible.posix 1.5.0

- [Synopsis](rpm_ostree_upgrade_module.md#synopsis)
- [Requirements](rpm_ostree_upgrade_module.md#requirements)
- [Parameters](rpm_ostree_upgrade_module.md#parameters)
- [Examples](rpm_ostree_upgrade_module.md#examples)
- [Return Values](rpm_ostree_upgrade_module.md#return-values)

## [Synopsis](rpm_ostree_upgrade_module.md#id1)

- Manage an rpm-ostree upgrade transactions.

## [Requirements](rpm_ostree_upgrade_module.md#id2)

The below requirements are needed on the host that executes this module.

- rpm-ostree

## [Parameters](rpm_ostree_upgrade_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_downgrade**  boolean | Allow for the upgrade to be a chronologically older tree.  **Choices:**   - `false` ← (default) - `true` |
| **cache_only**  boolean | Perform the transaction using only pre-cached data, do not download.  **Choices:**   - `false` ← (default) - `true` |
| **os**  string | The OSNAME upon which to operate.  **Default:** `""` |
| **peer**  boolean | Force peer-to-peer connection instead of using a system message bus.  **Choices:**   - `false` ← (default) - `true` |

## [Examples](rpm_ostree_upgrade_module.md#id4)

```yaml+jinja
- name: Upgrade the rpm-ostree image without options, accept all defaults
  ansible.posix.rpm_ostree_upgrade:

- name: Upgrade the rpm-ostree image allowing downgrades
  ansible.posix.rpm_ostree_upgrade:
    allow_downgrade: true
```

## [Return Values](rpm_ostree_upgrade_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The command standard output  **Returned:** always  **Sample:** `"No upgrade available."` |

### Authors

- Adam Miller (@maxamillion)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.posix)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
