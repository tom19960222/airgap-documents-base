---
collection: ansible
version: "8"
title: "community.windows.win_scoop module – Manage packages using Scoop"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_scoop_module.html
fetched_at: 2026-07-28T02:02:27+00:00
---
# community.windows.win_scoop module – Manage packages using Scoop

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_scoop`.

- [Synopsis](win_scoop_module.md#synopsis)
- [Parameters](win_scoop_module.md#parameters)
- [See Also](win_scoop_module.md#see-also)
- [Examples](win_scoop_module.md#examples)

## [Synopsis](win_scoop_module.md#id1)

- Manage packages using Scoop.
- If Scoop is missing from the system, the module will install it.

## [Parameters](win_scoop_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **architecture**  aliases: arch  string | Force Scoop to install the package of a specific process architecture.  **Choices:**   - `"32bit"` - `"64bit"` |
| **global**  boolean | Install the app globally  **Choices:**   - `false` ← (default) - `true` |
| **independent**  boolean | Don’t install dependencies automatically  **Choices:**   - `false` ← (default) - `true` |
| **name**  list / elements=string / required | Name of the package(s) to be installed. |
| **no_cache**  boolean | Don’t use the download cache  **Choices:**   - `false` ← (default) - `true` |
| **purge**  boolean | Remove all persistent data  **Choices:**   - `false` ← (default) - `true` |
| **skip_checksum**  boolean | Skip hash validation  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | State of the package on the system.  When `absent`, will ensure the package is not installed.  When `present`, will ensure the package is installed.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [See Also](win_scoop_module.md#id3)

> **See also:**
>
> [chocolatey.chocolatey.win_chocolatey](../../chocolatey/chocolatey/win_chocolatey_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-module)
> :   Manage packages using chocolatey.
>
> [Scoop website](https://scoop.sh)
> :   More information about Scoop
>
> [Scoop installer repository](https://github.com/lukesampson/scoop)
> :   GitHub repository for the Scoop installer
>
> [Scoop main bucket](https://github.com/ScoopInstaller/Main)
> :   GitHub repository for the main bucket

## [Examples](win_scoop_module.md#id4)

```yaml+jinja
- name: Install jq.
  community.windows.win_scoop:
    name: jq
```

### Authors

- Jamie Magee (@JamieMagee)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
