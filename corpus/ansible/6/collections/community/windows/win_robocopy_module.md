---
collection: ansible
version: "6"
title: "community.windows.win_robocopy module – Synchronizes the contents of two directories using Robocopy"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_robocopy_module.html
fetched_at: 2026-07-27T17:23:52+00:00
---
# community.windows.win_robocopy module – Synchronizes the contents of two directories using Robocopy

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_robocopy`.

- [Synopsis](win_robocopy_module.md#synopsis)
- [Parameters](win_robocopy_module.md#parameters)
- [Notes](win_robocopy_module.md#notes)
- [See Also](win_robocopy_module.md#see-also)
- [Examples](win_robocopy_module.md#examples)
- [Return Values](win_robocopy_module.md#return-values)

## [Synopsis](win_robocopy_module.md#id1)

- Synchronizes the contents of files/directories from a source to destination.
- Under the hood this just calls out to RoboCopy, since that should be available on most modern Windows systems.

## [Parameters](win_robocopy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dest**  path / required | Destination file/directory to sync (Will receive contents of src). |
| **flags**  string | Directly supply Robocopy flags.  If set, `purge` and `recurse` will be ignored. |
| **purge**  boolean | Deletes any files/directories found in the destination that do not exist in the source.  Toggles the `/purge` flag to RoboCopy.  If `flags` is set, this will be ignored.  Choices:   - `false` ← (default) - `true` |
| **recurse**  boolean | Includes all subdirectories (Toggles the `/e` flag to RoboCopy).  If `flags` is set, this will be ignored.  Choices:   - `false` ← (default) - `true` |
| **src**  path / required | Source file/directory to sync. |

## [Notes](win_robocopy_module.md#id3)

> **Note:**
>
> - This is not a complete port of the [ansible.posix.synchronize](../../ansible/posix/synchronize_module.md#ansible-collections-ansible-posix-synchronize-module) module. Unlike the [ansible.posix.synchronize](../../ansible/posix/synchronize_module.md#ansible-collections-ansible-posix-synchronize-module) module this only performs the sync/copy on the remote machine, not from the Ansible controller to the remote machine.
> - This module does not currently support all Robocopy flags.

## [See Also](win_robocopy_module.md#id4)

> **See also:**
>
> [ansible.posix.synchronize](../../ansible/posix/synchronize_module.md#ansible-collections-ansible-posix-synchronize-module)
> :   A wrapper around rsync to make common tasks in your playbooks quick and easy.
>
> [ansible.windows.win_copy](../../ansible/windows/win_copy_module.md#ansible-collections-ansible-windows-win-copy-module)
> :   Copies files to remote locations on windows hosts.

## [Examples](win_robocopy_module.md#id5)

```yaml+jinja
- name: Sync the contents of one directory to another
  community.windows.win_robocopy:
    src: C:\DirectoryOne
    dest: C:\DirectoryTwo

- name: Sync the contents of one directory to another, including subdirectories
  community.windows.win_robocopy:
    src: C:\DirectoryOne
    dest: C:\DirectoryTwo
    recurse: yes

- name: Sync the contents of one directory to another, and remove any files/directories found in destination that do not exist in the source
  community.windows.win_robocopy:
    src: C:\DirectoryOne
    dest: C:\DirectoryTwo
    purge: yes

- name: Sync content in recursive mode, removing any files/directories found in destination that do not exist in the source
  community.windows.win_robocopy:
    src: C:\DirectoryOne
    dest: C:\DirectoryTwo
    recurse: yes
    purge: yes

- name: Sync two directories in recursive and purging mode, specifying additional special flags
  community.windows.win_robocopy:
    src: C:\DirectoryOne
    dest: C:\DirectoryTwo
    flags: /E /PURGE /XD SOME_DIR /XF SOME_FILE /MT:32

- name: Sync one file from a remote UNC path in recursive and purging mode, specifying additional special flags
  community.windows.win_robocopy:
    src: \\Server1\Directory One
    dest: C:\DirectoryTwo
    flags: file.zip /E /PURGE /XD SOME_DIR /XF SOME_FILE /MT:32
```

## [Return Values](win_robocopy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cmd**  string | The used command line.  Returned: always  Sample: `"robocopy C:\\DirectoryOne C:\\DirectoryTwo /e /purge"` |
| **dest**  string | The Destination file/directory of the sync.  Returned: always  Sample: `"C:\\Some\\Path"` |
| **flags**  string | Any flags passed in by the user.  Returned: always  Sample: `"/e /purge"` |
| **msg**  string | Output interpreted into a concise message.  Returned: always  Sample: `"No files copied!"` |
| **output**  string | The output of running the robocopy command.  Returned: success  Sample: `"------------------------------------\\n   ROBOCOPY     ::     Robust File Copy for Windows         \\n------------------------------------\\n "` |
| **purge**  boolean | Whether or not the purge flag was toggled.  Returned: always  Sample: `false` |
| **rc**  integer | The return code returned by robocopy.  Returned: success  Sample: `1` |
| **recurse**  boolean | Whether or not the recurse flag was toggled.  Returned: always  Sample: `false` |
| **src**  string | The Source file/directory of the sync.  Returned: always  Sample: `"C:\\Some\\Path"` |

### Authors

- Corwin Brown (@blakfeld)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
