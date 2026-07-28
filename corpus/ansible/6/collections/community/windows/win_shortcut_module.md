---
collection: ansible
version: "6"
title: "community.windows.win_shortcut module – Manage shortcuts on Windows"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_shortcut_module.html
fetched_at: 2026-07-27T17:23:58+00:00
---
# community.windows.win_shortcut module – Manage shortcuts on Windows

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
> To use it in a playbook, specify: `community.windows.win_shortcut`.

- [Synopsis](win_shortcut_module.md#synopsis)
- [Parameters](win_shortcut_module.md#parameters)
- [Notes](win_shortcut_module.md#notes)
- [See Also](win_shortcut_module.md#see-also)
- [Examples](win_shortcut_module.md#examples)

## [Synopsis](win_shortcut_module.md#id1)

- Create, manage and delete Windows shortcuts

## [Parameters](win_shortcut_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **arguments**  aliases: args  string | Additional arguments for the executable defined in `src`. |
| **description**  string | Description for the shortcut.  This is usually shown when hoovering the icon. |
| **dest**  path / required | Destination file for the shortcuting file.  File name should have a `.lnk` or `.url` extension. |
| **directory**  path | Working directory for executable defined in `src`. |
| **hotkey**  string | Key combination for the shortcut.  This is a combination of one or more modifiers and a key.  Possible modifiers are Alt, Ctrl, Shift, Ext.  Possible keys are [A-Z] and [0-9]. |
| **icon**  path | Icon used for the shortcut.  File name should have a `.ico` extension.  The file name is followed by a comma and the number in the library file (.dll) or use 0 for an image file. |
| **run_as_admin**  boolean | When `src` is an executable, this can control whether the shortcut will be opened as an administrator or not.  Choices:   - `false` ← (default) - `true` |
| **src**  string | Executable or URL the shortcut points to.  The executable needs to be in your PATH, or has to be an absolute path to the executable. |
| **state**  string | When `absent`, removes the shortcut if it exists.  When `present`, creates or updates the shortcut.  Choices:   - `"absent"` - `"present"` ← (default) |
| **windowstyle**  string | Influences how the application is displayed when it is launched.  Choices:   - `"maximized"` - `"minimized"` - `"normal"` |

## [Notes](win_shortcut_module.md#id3)

> **Note:**
>
> - The following options can include Windows environment variables: `dest`, `args`, `description`, `dest`, `directory`, `icon` `src`
> - Windows has two types of shortcuts: Application and URL shortcuts. URL shortcuts only consists of `dest` and `src`

## [See Also](win_shortcut_module.md#id4)

> **See also:**
>
> [ansible.windows.win_file](../../ansible/windows/win_file_module.md#ansible-collections-ansible-windows-win-file-module)
> :   Creates, touches or removes files or directories.

## [Examples](win_shortcut_module.md#id5)

```yaml+jinja
- name: Create an application shortcut on the desktop
  community.windows.win_shortcut:
    src: C:\Program Files\Mozilla Firefox\Firefox.exe
    dest: C:\Users\Public\Desktop\Mozilla Firefox.lnk
    icon: C:\Program Files\Mozilla Firefox\Firefox.exe,0

- name: Create the same shortcut using environment variables
  community.windows.win_shortcut:
    description: The Mozilla Firefox web browser
    src: '%ProgramFiles%\Mozilla Firefox\Firefox.exe'
    dest: '%Public%\Desktop\Mozilla Firefox.lnk'
    icon: '%ProgramFiles\Mozilla Firefox\Firefox.exe,0'
    directory: '%ProgramFiles%\Mozilla Firefox'
    hotkey: Ctrl+Alt+F

- name: Create an application shortcut for an executable in PATH to your desktop
  community.windows.win_shortcut:
    src: cmd.exe
    dest: Desktop\Command prompt.lnk

- name: Create an application shortcut for the Ansible website
  community.windows.win_shortcut:
    src: '%ProgramFiles%\Google\Chrome\Application\chrome.exe'
    dest: '%UserProfile%\Desktop\Ansible website.lnk'
    arguments: --new-window https://ansible.com/
    directory: '%ProgramFiles%\Google\Chrome\Application'
    icon: '%ProgramFiles%\Google\Chrome\Application\chrome.exe,0'
    hotkey: Ctrl+Alt+A

- name: Create a URL shortcut for the Ansible website
  community.windows.win_shortcut:
    src: https://ansible.com/
    dest: '%Public%\Desktop\Ansible website.url'
```

### Authors

- Dag Wieers (@dagwieers)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
