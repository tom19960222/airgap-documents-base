---
collection: ansible
version: "8"
title: "community.general.ip_netns module – Manage network namespaces"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ip_netns_module.html
fetched_at: 2026-07-28T01:46:34+00:00
---
# community.general.ip_netns module – Manage network namespaces

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](ip_netns_module.md#ansible-collections-community-general-ip-netns-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ip_netns`.

- [Synopsis](ip_netns_module.md#synopsis)
- [Requirements](ip_netns_module.md#requirements)
- [Parameters](ip_netns_module.md#parameters)
- [Attributes](ip_netns_module.md#attributes)
- [Examples](ip_netns_module.md#examples)

## [Synopsis](ip_netns_module.md#id1)

- Create or delete network namespaces using the ip command.

Aliases: net_tools.ip_netns

## [Requirements](ip_netns_module.md#id2)

The below requirements are needed on the host that executes this module.

- ip

## [Parameters](ip_netns_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  string | Name of the namespace |
| **state**  string | Whether the namespace should exist  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Attributes](ip_netns_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](ip_netns_module.md#id5)

```yaml+jinja
- name: Create a namespace named mario
  community.general.ip_netns:
    name: mario
    state: present

- name: Delete a namespace named luigi
  community.general.ip_netns:
    name: luigi
    state: absent
```

### Authors

- Arie Bregman (@bregman-arie)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
