---
collection: ansible
version: "8"
title: "ansible.windows.win_share module – Manage Windows shares"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/win_share_module.html
fetched_at: 2026-07-28T01:10:48+00:00
---
# ansible.windows.win_share module – Manage Windows shares

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ui/repo/published/ansible/windows/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
> You need further requirements to be able to use this module,
> see [Requirements](win_share_module.md#ansible-collections-ansible-windows-win-share-module-requirements) for details.
>
> To use it in a playbook, specify: `ansible.windows.win_share`.

- [Synopsis](win_share_module.md#synopsis)
- [Requirements](win_share_module.md#requirements)
- [Parameters](win_share_module.md#parameters)
- [Examples](win_share_module.md#examples)
- [Return Values](win_share_module.md#return-values)

## [Synopsis](win_share_module.md#id1)

- Add, modify or remove Windows share and set share permissions.

## [Requirements](win_share_module.md#id2)

The below requirements are needed on the host that executes this module.

- As this module used newer cmdlets like New-SmbShare this can only run on Windows 8 / Windows 2012 or newer.
- This is due to the reliance on the WMI provider MSFT_SmbShare <https://msdn.microsoft.com/en-us/library/hh830471> which was only added with these Windows releases.

## [Parameters](win_share_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **caching_mode**  string | Set the CachingMode for this share.  **Choices:**   - `"BranchCache"` - `"Documents"` - `"Manual"` ← (default) - `"None"` - `"Programs"` - `"Unknown"` |
| **change**  string | Specify user list that should get read and write access on share, separated by comma. |
| **deny**  string | Specify user list that should get no access, regardless of implied access on share, separated by comma. |
| **description**  string | Share description. |
| **encrypt**  boolean | Sets whether to encrypt the traffic to the share or not.  **Choices:**   - `false` ← (default) - `true` |
| **full**  string | Specify user list that should get full access on share, separated by comma. |
| **list**  boolean | Specify whether to allow or deny file listing, in case user has no permission on share. Also known as Access-Based Enumeration.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Share name. |
| **path**  path / required | Share directory. |
| **read**  string | Specify user list that should get read access on share, separated by comma. |
| **rule_action**  string | Whether to add or set (replace) access control entries.  **Choices:**   - `"set"` ← (default) - `"add"` |
| **state**  string | Specify whether to add `present` or remove `absent` the specified share.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Examples](win_share_module.md#id4)

```yaml+jinja
- name: Add secret share
  ansible.windows.win_share:
    name: internal
    description: top secret share
    path: C:\shares\internal
    list: false
    full: Administrators,CEO
    read: HR-Global
    deny: HR-External

- name: Add public company share
  ansible.windows.win_share:
    name: company
    description: top secret share
    path: C:\shares\company
    list: yes
    full: Administrators,CEO
    read: Global

- name: Remove previously added share
  ansible.windows.win_share:
    name: internal
    state: absent
```

## [Return Values](win_share_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **actions**  list / elements=string | A list of action cmdlets that were run by the module.  **Returned:** success  **Sample:** `["New-SmbShare -Name share -Path C:\\temp"]` |

### Authors

- Hans-Joachim Kliemeck (@h0nIg)
- David Baumann (@daBONDi)
- Shachaf Goldstein (@Shachaf92)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
