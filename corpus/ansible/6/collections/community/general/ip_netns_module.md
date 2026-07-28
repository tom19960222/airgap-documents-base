---
collection: ansible
version: "6"
title: "community.general.ip_netns module – Manage network namespaces"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ip_netns_module.html
fetched_at: 2026-07-27T17:09:49+00:00
---
# community.general.ip_netns module – Manage network namespaces

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
> see [Requirements](ip_netns_module.md#ansible-collections-community-general-ip-netns-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ip_netns`.

- [Synopsis](ip_netns_module.md#synopsis)
- [Requirements](ip_netns_module.md#requirements)
- [Parameters](ip_netns_module.md#parameters)
- [Examples](ip_netns_module.md#examples)

## [Synopsis](ip_netns_module.md#id1)

- Create or delete network namespaces using the ip command.

## [Requirements](ip_netns_module.md#id2)

The below requirements are needed on the host that executes this module.

- ip

## [Parameters](ip_netns_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  string | Name of the namespace |
| **state**  string | Whether the namespace should exist  Choices:   - `"present"` ← (default) - `"absent"` |

## [Examples](ip_netns_module.md#id4)

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

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
