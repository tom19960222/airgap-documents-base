---
collection: ansible
version: "6"
title: "community.general.icinga2_feature module – Manage Icinga2 feature"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/icinga2_feature_module.html
fetched_at: 2026-07-27T17:09:37+00:00
---
# community.general.icinga2_feature module – Manage Icinga2 feature

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.icinga2_feature`.

- [Synopsis](icinga2_feature_module.md#synopsis)
- [Parameters](icinga2_feature_module.md#parameters)
- [Examples](icinga2_feature_module.md#examples)

## [Synopsis](icinga2_feature_module.md#id1)

- This module can be used to enable or disable an Icinga2 feature.

## [Parameters](icinga2_feature_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | This is the feature name to enable or disable. |
| **state**  string | If set to `present` and feature is disabled, then feature is enabled.  If set to `present` and feature is already enabled, then nothing is changed.  If set to `absent` and feature is enabled, then feature is disabled.  If set to `absent` and feature is already disabled, then nothing is changed.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Examples](icinga2_feature_module.md#id3)

```yaml+jinja
- name: Enable ido-pgsql feature
  community.general.icinga2_feature:
    name: ido-pgsql
    state: present

- name: Disable api feature
  community.general.icinga2_feature:
    name: api
    state: absent
```

### Authors

- Loic Blot (@nerzhul)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
