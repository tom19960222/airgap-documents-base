---
collection: ansible
version: "8"
title: "community.windows.win_unzip module – Unzips compressed files and archives on the Windows node"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_unzip_module.html
fetched_at: 2026-07-28T02:02:32+00:00
---
# community.windows.win_unzip module – Unzips compressed files and archives on the Windows node

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
> see [Requirements](win_unzip_module.md#ansible-collections-community-windows-win-unzip-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_unzip`.

- [Synopsis](win_unzip_module.md#synopsis)
- [Requirements](win_unzip_module.md#requirements)
- [Parameters](win_unzip_module.md#parameters)
- [Notes](win_unzip_module.md#notes)
- [See Also](win_unzip_module.md#see-also)
- [Examples](win_unzip_module.md#examples)
- [Return Values](win_unzip_module.md#return-values)

## [Synopsis](win_unzip_module.md#id1)

- Unzips compressed files and archives.
- Supports .zip files natively.
- Supports other formats supported by the Powershell Community Extensions (PSCX) module (basically everything 7zip supports).
- For non-Windows targets, use the [ansible.builtin.unarchive](../../ansible/builtin/unarchive_module.md#ansible-collections-ansible-builtin-unarchive-module) module instead.

## [Requirements](win_unzip_module.md#id2)

The below requirements are needed on the host that executes this module.

- PSCX

## [Parameters](win_unzip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **creates**  path | If this file or directory exists the specified src will not be extracted. |
| **delete_archive**  aliases: rm  boolean | Remove the zip file, after unzipping.  **Choices:**   - `false` ← (default) - `true` |
| **dest**  path / required | Destination of zip file (provide absolute path of directory). If it does not exist, the directory will be created. |
| **password**  string | If a zip file is encrypted with password.  Passing a value to a password parameter requires the PSCX module to be installed. |
| **recurse**  boolean | Recursively expand zipped files within the src file.  Setting to a value of `yes` requires the PSCX module to be installed.  **Choices:**   - `false` ← (default) - `true` |
| **src**  path / required | File to be unzipped (provide absolute path). |

## [Notes](win_unzip_module.md#id4)

> **Note:**
>
> - This module is not really idempotent, it will extract the archive every time, and report a change.
> - For extracting any compression types other than .zip, the PowerShellCommunityExtensions (PSCX) Module is required. This module (in conjunction with PSCX) has the ability to recursively unzip files within the src zip file provided and also functionality for many other compression types. If the destination directory does not exist, it will be created before unzipping the file. Specifying rm parameter will force removal of the src file after extraction.

## [See Also](win_unzip_module.md#id5)

> **See also:**
>
> [ansible.builtin.unarchive](../../ansible/builtin/unarchive_module.md#ansible-collections-ansible-builtin-unarchive-module)
> :   Unpacks an archive after (optionally) copying it from the local machine.

## [Examples](win_unzip_module.md#id6)

```yaml+jinja
# This unzips a library that was downloaded with win_get_url, and removes the file after extraction
# $ ansible -i hosts -m win_unzip -a "src=C:\LibraryToUnzip.zip dest=C:\Lib remove=yes" all

- name: Unzip a bz2 (BZip) file
  community.windows.win_unzip:
    src: C:\Users\Phil\Logs.bz2
    dest: C:\Users\Phil\OldLogs
    creates: C:\Users\Phil\OldLogs

- name: Unzip gz log
  community.windows.win_unzip:
    src: C:\Logs\application-error-logs.gz
    dest: C:\ExtractedLogs\application-error-logs

# Unzip .zip file, recursively decompresses the contained .gz files and removes all unneeded compressed files after completion.
- name: Recursively decompress GZ files in ApplicationLogs.zip
  community.windows.win_unzip:
    src: C:\Downloads\ApplicationLogs.zip
    dest: C:\Application\Logs
    recurse: yes
    delete_archive: yes

- name: Install PSCX
  community.windows.win_psmodule:
    name: Pscx
    state: present

- name: Unzip .7z file which is password encrypted
  community.windows.win_unzip:
    src: C:\Downloads\ApplicationLogs.7z
    dest: C:\Application\Logs
    password: abcd
    delete_archive: yes
```

## [Return Values](win_unzip_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dest**  string | The provided destination path  **Returned:** always  **Sample:** `"C:\\ExtractedLogs\\application-error-logs"` |
| **removed**  boolean | Whether the module did remove any files during task run  **Returned:** always  **Sample:** `true` |
| **src**  string | The provided source path  **Returned:** always  **Sample:** `"C:\\Logs\\application-error-logs.gz"` |

### Authors

- Phil Schwartz (@schwartzmx)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
