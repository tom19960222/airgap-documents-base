---
collection: ansible
version: "8"
title: "community.general.sysupgrade module – Manage OpenBSD system upgrades"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/sysupgrade_module.html
fetched_at: 2026-07-28T01:50:56+00:00
---
# community.general.sysupgrade module – Manage OpenBSD system upgrades

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.sysupgrade`.

New in community.general 1.1.0

- [Synopsis](sysupgrade_module.md#synopsis)
- [Parameters](sysupgrade_module.md#parameters)
- [Attributes](sysupgrade_module.md#attributes)
- [Examples](sysupgrade_module.md#examples)
- [Return Values](sysupgrade_module.md#return-values)

## [Synopsis](sysupgrade_module.md#id1)

- Manage OpenBSD system upgrades using sysupgrade.

Aliases: system.sysupgrade

## [Parameters](sysupgrade_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **fetch_only**  boolean | Fetch and verify files and create /bsd.upgrade but do not reboot.  Set to `false` if you want sysupgrade to reboot. This will cause Ansible to error, as it expects the module to exit gracefully. See the examples.  **Choices:**   - `false` - `true` ← (default) |
| **force**  boolean | Force upgrade (for snapshots only).  **Choices:**   - `false` ← (default) - `true` |
| **installurl**  string | OpenBSD mirror top-level URL for fetching an upgrade.  By default, the mirror URL is pulled from /etc/installurl. |
| **keep_files**  boolean | Keep the files under /home/_sysupgrade.  By default, the files will be deleted after the upgrade.  **Choices:**   - `false` ← (default) - `true` |
| **snapshot**  boolean | Apply the latest snapshot.  Otherwise release will be applied.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](sysupgrade_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](sysupgrade_module.md#id4)

```yaml+jinja
- name: Upgrade to latest release
  community.general.sysupgrade:
  register: sysupgrade

- name: Upgrade to latest snapshot
  community.general.sysupgrade:
    snapshot: true
    installurl: https://cloudflare.cdn.openbsd.org/pub/OpenBSD
  register: sysupgrade

- name: Reboot to apply upgrade if needed
  ansible.builtin.reboot:
  when: sysupgrade.changed

# Note: Ansible will error when running this way due to how
#   the reboot is forcefully handled by sysupgrade:

- name: Have sysupgrade automatically reboot
  community.general.sysupgrade:
    fetch_only: false
  ignore_errors: true
```

## [Return Values](sysupgrade_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **rc**  integer | The command return code (0 means success).  **Returned:** always |
| **stderr**  string | Sysupgrade standard error.  **Returned:** always  **Sample:** `"sysupgrade: need root privileges"` |
| **stdout**  string | Sysupgrade standard output.  **Returned:** always |

### Authors

- Andrew Klaus (@precurse)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
