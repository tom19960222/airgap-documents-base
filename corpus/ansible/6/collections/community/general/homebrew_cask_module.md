---
collection: ansible
version: "6"
title: "community.general.homebrew_cask module – Install and uninstall homebrew casks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/homebrew_cask_module.html
fetched_at: 2026-07-27T17:09:19+00:00
---
# community.general.homebrew_cask module – Install and uninstall homebrew casks

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](homebrew_cask_module.md#ansible-collections-community-general-homebrew-cask-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.homebrew_cask`.

- [Synopsis](homebrew_cask_module.md#synopsis)
- [Requirements](homebrew_cask_module.md#requirements)
- [Parameters](homebrew_cask_module.md#parameters)
- [Examples](homebrew_cask_module.md#examples)

## [Synopsis](homebrew_cask_module.md#id1)

- Manages Homebrew casks.

## [Requirements](homebrew_cask_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](homebrew_cask_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accept_external_apps**  boolean | Allow external apps.  Choices:   - `false` ← (default) - `true` |
| **greedy**  boolean | Upgrade casks that auto update.  Passes –greedy to brew cask outdated when checking if an installed cask has a newer version available.  Choices:   - `false` ← (default) - `true` |
| **install_options**  aliases: options  list / elements=string | Options flags to install a package. |
| **name**  aliases: cask, package, pkg  list / elements=string | Name of cask to install or remove. |
| **path**  path | ‘:’ separated list of paths to search for ‘brew’ executable.  Default: `"/usr/local/bin:/opt/homebrew/bin"` |
| **state**  string | State of the cask.  Choices:   - `"absent"` - `"installed"` - `"latest"` - `"present"` ← (default) - `"removed"` - `"uninstalled"` - `"upgraded"` |
| **sudo_password**  string | The sudo password to be passed to SUDO_ASKPASS. |
| **update_homebrew**  boolean | Update homebrew itself first.  Note that `brew cask update` is a synonym for `brew update`.  Choices:   - `false` ← (default) - `true` |
| **upgrade_all**  aliases: upgrade  boolean | Upgrade all casks.  Mutually exclusive with `upgraded` state.  Choices:   - `false` ← (default) - `true` |

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

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
