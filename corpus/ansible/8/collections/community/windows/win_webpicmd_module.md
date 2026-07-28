---
collection: ansible
version: "8"
title: "community.windows.win_webpicmd module – Installs packages using Web Platform Installer command-line"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_webpicmd_module.html
fetched_at: 2026-07-28T02:02:35+00:00
---
# community.windows.win_webpicmd module – Installs packages using Web Platform Installer command-line

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
> To use it in a playbook, specify: `community.windows.win_webpicmd`.

- [Synopsis](win_webpicmd_module.md#synopsis)
- [Parameters](win_webpicmd_module.md#parameters)
- [Notes](win_webpicmd_module.md#notes)
- [See Also](win_webpicmd_module.md#see-also)
- [Examples](win_webpicmd_module.md#examples)

## [Synopsis](win_webpicmd_module.md#id1)

- Installs packages using Web Platform Installer command-line (<http://www.iis.net/learn/install/web-platform-installer/web-platform-installer-v4-command-line-webpicmdexe-rtw-release>).
- Must be installed and present in PATH (see [chocolatey.chocolatey.win_chocolatey](../../chocolatey/chocolatey/win_chocolatey_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-module) module; ‘webpicmd’ is the package name, and you must install ‘lessmsi’ first too)?
- Install IIS first (see [ansible.windows.win_feature](../../ansible/windows/win_feature_module.md#ansible-collections-ansible-windows-win-feature-module) module).

## [Parameters](win_webpicmd_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Name of the package to be installed. |

## [Notes](win_webpicmd_module.md#id3)

> **Note:**
>
> - Accepts EULAs and suppresses reboot - you will need to check manage reboots yourself (see [ansible.windows.win_reboot](../../ansible/windows/win_reboot_module.md#ansible-collections-ansible-windows-win-reboot-module) module)

## [See Also](win_webpicmd_module.md#id4)

> **See also:**
>
> [ansible.windows.win_package](../../ansible/windows/win_package_module.md#ansible-collections-ansible-windows-win-package-module)
> :   Installs/uninstalls an installable package.

## [Examples](win_webpicmd_module.md#id5)

```yaml+jinja
- name: Install URLRewrite2.
  community.windows.win_webpicmd:
    name: URLRewrite2
```

### Authors

- Peter Mounce (@petemounce)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
