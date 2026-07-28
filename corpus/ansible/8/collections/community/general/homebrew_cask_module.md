---
collection: ansible
version: "8"
title: "community.general.homebrew_cask module – Install and uninstall homebrew casks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/homebrew_cask_module.html
fetched_at: 2026-07-28T01:46:01+00:00
---
# community.general.homebrew_cask module – Install and uninstall homebrew casks

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
> To use it in a playbook, specify: `community.general.homebrew_cask`.

- [Synopsis](homebrew_cask_module.md#synopsis)
- [Parameters](homebrew_cask_module.md#parameters)
- [Attributes](homebrew_cask_module.md#attributes)
- [Examples](homebrew_cask_module.md#examples)

## [Synopsis](homebrew_cask_module.md#id1)

- Manages Homebrew casks.

Aliases: packaging.os.homebrew_cask

## [Parameters](homebrew_cask_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **accept_external_apps**  boolean | Allow external apps.  **Choices:**   - `false` ← (default) - `true` |
| **greedy**  boolean | Upgrade casks that auto update.  Passes `--greedy` to `brew outdated --cask` when checking if an installed cask has a newer version available, or to `brew upgrade --cask` when upgrading all casks.  **Choices:**   - `false` ← (default) - `true` |
| **install_options**  aliases: options  list / elements=string | Options flags to install a package. |
| **name**  aliases: cask, package, pkg  list / elements=string | Name of cask to install or remove. |
| **path**  path | ‘:’ separated list of paths to search for ‘brew’ executable.  **Default:** `"/usr/local/bin:/opt/homebrew/bin"` |
| **state**  string | State of the cask.  **Choices:**   - `"absent"` - `"installed"` - `"latest"` - `"present"` ← (default) - `"removed"` - `"uninstalled"` - `"upgraded"` |
| **sudo_password**  string | The sudo password to be passed to SUDO_ASKPASS. |
| **update_homebrew**  boolean | Update homebrew itself first.  Note that `brew cask update` is a synonym for `brew update`.  **Choices:**   - `false` ← (default) - `true` |
| **upgrade_all**  aliases: upgrade  boolean | Upgrade all casks.  Mutually exclusive with `upgraded` state.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](homebrew_cask_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](homebrew_cask_module.md#id4)

```yaml+jinja
- name: Install cask
  community.general.homebrew_cask:
    name: alfred
    state: present

- name: Remove cask
  community.general.homebrew_cask:
    name: alfred
    state: absent

- name: Install cask with install options
  community.general.homebrew_cask:
    name: alfred
    state: present
    install_options: 'appdir=/Applications'

- name: Install cask with install options
  community.general.homebrew_cask:
    name: alfred
    state: present
    install_options: 'debug,appdir=/Applications'

- name: Install cask with force option
  community.general.homebrew_cask:
    name: alfred
    state: present
    install_options: force

- name: Allow external app
  community.general.homebrew_cask:
    name: alfred
    state: present
    accept_external_apps: true

- name: Remove cask with force option
  community.general.homebrew_cask:
    name: alfred
    state: absent
    install_options: force

- name: Upgrade all casks
  community.general.homebrew_cask:
    upgrade_all: true

- name: Upgrade all casks with greedy option
  community.general.homebrew_cask:
    upgrade_all: true
    greedy: true

- name: Upgrade given cask with force option
  community.general.homebrew_cask:
    name: alfred
    state: upgraded
    install_options: force

- name: Upgrade cask with greedy option
  community.general.homebrew_cask:
    name: 1password
    state: upgraded
    greedy: true

- name: Using sudo password for installing cask
  community.general.homebrew_cask:
    name: wireshark
    state: present
    sudo_password: "{{ ansible_become_pass }}"
```

### Authors

- Indrajit Raychaudhuri (@indrajitr)
- Daniel Jaouen (@danieljaouen)
- Enric Lluelles (@enriclluelles)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
