---
collection: ansible
version: "8"
title: "community.windows.win_defrag module – Consolidate fragmented files on local volumes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_defrag_module.html
fetched_at: 2026-07-28T02:01:41+00:00
---
# community.windows.win_defrag module – Consolidate fragmented files on local volumes

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
> You need further requirements to be able to use this module,
> see [Requirements](win_defrag_module.md#ansible-collections-community-windows-win-defrag-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_defrag`.

- [Synopsis](win_defrag_module.md#synopsis)
- [Requirements](win_defrag_module.md#requirements)
- [Parameters](win_defrag_module.md#parameters)
- [Examples](win_defrag_module.md#examples)
- [Return Values](win_defrag_module.md#return-values)

## [Synopsis](win_defrag_module.md#id1)

- Locates and consolidates fragmented files on local volumes to improve system performance.
- More information regarding `win_defrag` is available from: <https://technet.microsoft.com/en-us/library/cc731650%2528v%253Dws.11.aspx%2529>

## [Requirements](win_defrag_module.md#id2)

The below requirements are needed on the host that executes this module.

- defrag.exe

## [Parameters](win_defrag_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **exclude_volumes**  list / elements=string | A list of drive letters or mount point paths to exclude from defragmentation. |
| **freespace_consolidation**  boolean | Perform free space consolidation on the specified volumes.  **Choices:**   - `false` ← (default) - `true` |
| **include_volumes**  list / elements=string | A list of drive letters or mount point paths of the volumes to be defragmented.  If this parameter is omitted, all volumes (not excluded) will be fragmented. |
| **parallel**  boolean | Run the operation on each volume in parallel in the background.  **Choices:**   - `false` ← (default) - `true` |
| **priority**  string | Run the operation at low or normal priority.  **Choices:**   - `"low"` ← (default) - `"normal"` |

## [Examples](win_defrag_module.md#id4)

```yaml+jinja
- name: Defragment all local volumes (in parallel)
  community.windows.win_defrag:
    parallel: yes

- name: 'Defragment all local volumes, except C: and D:'
  community.windows.win_defrag:
    exclude_volumes: [ C, D ]

- name: 'Defragment volume D: with normal priority'
  community.windows.win_defrag:
    include_volumes: D
    priority: normal

- name: Consolidate free space (useful when reducing volumes)
  community.windows.win_defrag:
    freespace_consolidation: yes
```

## [Return Values](win_defrag_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not any changes were made.  **Returned:** always  **Sample:** `true` |
| **cmd**  string | The complete command line used by the module.  **Returned:** always  **Sample:** `"defrag.exe /C /V"` |
| **msg**  string | Possible error message on failure.  **Returned:** failed  **Sample:** `"Command 'defrag.exe' not found in $env:PATH."` |
| **rc**  integer | The return code for the command.  **Returned:** always  **Sample:** `0` |
| **stderr**  string | The error output from the command.  **Returned:** always |
| **stdout**  string | The standard output from the command.  **Returned:** always  **Sample:** `"Success."` |

### Authors

- Dag Wieers (@dagwieers)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
