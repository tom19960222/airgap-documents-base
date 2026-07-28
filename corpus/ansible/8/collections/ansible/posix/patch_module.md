---
collection: ansible
version: "8"
title: "ansible.posix.patch module – Apply patch files using the GNU patch tool"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/posix/patch_module.html
fetched_at: 2026-07-28T01:09:28+00:00
---
# ansible.posix.patch module – Apply patch files using the GNU patch tool

> **Note:**
>
> This module is part of the [ansible.posix collection](https://galaxy.ansible.com/ui/repo/published/ansible/posix/) (version 1.5.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.posix`.
>
> To use it in a playbook, specify: `ansible.posix.patch`.

New in ansible.posix 1.0.0

- [Synopsis](patch_module.md#synopsis)
- [Parameters](patch_module.md#parameters)
- [Notes](patch_module.md#notes)
- [Examples](patch_module.md#examples)

## [Synopsis](patch_module.md#id1)

- Apply patch files using the GNU patch tool.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](patch_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backup**  boolean | Passes `--backup --version-control=numbered` to patch, producing numbered backup copies.  **Choices:**   - `false` ← (default) - `true` |
| **basedir**  path | Path of a base directory in which the patch file will be applied.  May be omitted when `dest` option is specified, otherwise required. |
| **binary**  boolean | Setting to `true` will disable patch’s heuristic for transforming CRLF line endings into LF.  Line endings of src and dest must match.  If set to `false`, `patch` will replace CRLF in `src` files on POSIX.  **Choices:**   - `false` ← (default) - `true` |
| **dest**  aliases: originalfile  path | Path of the file on the remote machine to be patched.  The names of the files to be patched are usually taken from the patch file, but if there’s just one file to be patched it can specified with this option. |
| **ignore_whitespace**  boolean | Setting to `true` will ignore white space changes between patch and input.  **Choices:**   - `false` ← (default) - `true` |
| **remote_src**  boolean | If `false`, it will search for src at originating/controller machine, if `true` it will go to the remote/target machine for the `src`.  **Choices:**   - `false` ← (default) - `true` |
| **src**  aliases: patchfile  path / required | Path of the patch file as accepted by the GNU patch tool. If `remote_src` is `false`, the patch source file is looked up from the module’s *files* directory. |
| **state**  string | Whether the patch should be applied or reverted.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **strip**  integer | Number that indicates the smallest prefix containing leading slashes that will be stripped from each file name found in the patch file.  For more information see the strip parameter of the GNU patch tool.  **Default:** `0` |

## [Notes](patch_module.md#id3)

> **Note:**
>
> - This module requires GNU *patch* utility to be installed on the remote host.

## [Examples](patch_module.md#id4)

```yaml+jinja
- name: Apply patch to one file
  ansible.posix.patch:
    src: /tmp/index.html.patch
    dest: /var/www/index.html

- name: Apply patch to multiple files under basedir
  ansible.posix.patch:
    src: /tmp/customize.patch
    basedir: /var/www
    strip: 1

- name: Revert patch to one file
  ansible.posix.patch:
    src: /tmp/index.html.patch
    dest: /var/www/index.html
    state: absent
```

### Authors

- Jakub Jirutka (@jirutka)
- Luis Alberto Perez Lazaro (@luisperlaz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.posix)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
