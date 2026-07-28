---
collection: ansible
version: "6"
title: "community.general.mas module – Manage Mac App Store applications with mas-cli"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/mas_module.html
fetched_at: 2026-07-27T17:10:51+00:00
---
# community.general.mas module – Manage Mac App Store applications with mas-cli

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
> see [Requirements](mas_module.md#ansible-collections-community-general-mas-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.mas`.

New in community.general 0.2.0

- [Synopsis](mas_module.md#synopsis)
- [Requirements](mas_module.md#requirements)
- [Parameters](mas_module.md#parameters)
- [Notes](mas_module.md#notes)
- [Examples](mas_module.md#examples)

## [Synopsis](mas_module.md#id1)

- Installs, uninstalls and updates macOS applications from the Mac App Store using the `mas-cli`.

## [Requirements](mas_module.md#id2)

The below requirements are needed on the host that executes this module.

- macOS 10.11+
- mas-cli (<https://github.com/mas-cli/mas>) 1.5.0+ available as `mas` in the bin path
- The Apple ID to use already needs to be signed in to the Mac App Store (check with `mas account`).

## [Parameters](mas_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **id**  list / elements=integer | The Mac App Store identifier of the app(s) you want to manage.  This can be found by running `mas search APP_NAME` on your machine. |
| **state**  string | Desired state of the app installation.  The `absent` value requires root permissions, also see the examples.  Choices:   - `"absent"` - `"latest"` - `"present"` ← (default) |
| **upgrade_all**  aliases: upgrade  boolean | Upgrade all installed Mac App Store apps.  Choices:   - `false` ← (default) - `true` |

## [Notes](mas_module.md#id4)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](mas_module.md#id5)

```yaml+jinja
- name: Install Keynote
  community.general.mas:
    id: 409183694
    state: present

- name: Install Divvy with command mas installed in /usr/local/bin
  community.general.mas:
    id: 413857545
    state: present
  environment:
    PATH: /usr/local/bin:{{ ansible_facts.env.PATH }}

- name: Install a list of apps
  community.general.mas:
    id:
      - 409183694 # Keynote
      - 413857545 # Divvy
    state: present

- name: Ensure the latest Keynote version is installed
  community.general.mas:
    id: 409183694
    state: latest

- name: Upgrade all installed Mac App Store apps
  community.general.mas:
    upgrade_all: true

- name: Install specific apps and also upgrade all others
  community.general.mas:
    id:
      - 409183694 # Keynote
      - 413857545 # Divvy
    state: present
    upgrade_all: true

- name: Uninstall Divvy
  community.general.mas:
    id: 413857545
    state: absent
  become: true # Uninstallation requires root permissions
```

### Authors

- Michael Heap (@mheap)
- Lukas Bestle (@lukasbestle)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
