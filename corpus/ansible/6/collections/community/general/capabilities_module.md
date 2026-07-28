---
collection: ansible
version: "6"
title: "community.general.capabilities module – Manage Linux capabilities"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/capabilities_module.html
fetched_at: 2026-07-27T17:08:20+00:00
---
# community.general.capabilities module – Manage Linux capabilities

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
> To use it in a playbook, specify: `community.general.capabilities`.

- [Synopsis](capabilities_module.md#synopsis)
- [Parameters](capabilities_module.md#parameters)
- [Notes](capabilities_module.md#notes)
- [Examples](capabilities_module.md#examples)

## [Synopsis](capabilities_module.md#id1)

- This module manipulates files privileges using the Linux capabilities(7) system.

## [Parameters](capabilities_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **capability**  aliases: cap  string / required | Desired capability to set (with operator and flags, if state is `present`) or remove (if state is `absent`) |
| **path**  aliases: key  string / required | Specifies the path to the file to be managed. |
| **state**  string | Whether the entry should be present or absent in the file’s capabilities.  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](capabilities_module.md#id3)

> **Note:**
>
> - The capabilities system will automatically transform operators and flags into the effective set, so for example, `cap_foo=ep` will probably become `cap_foo+ep`.
> - This module does not attempt to determine the final operator and flags to compare, so you will want to ensure that your capabilities argument matches the final capabilities.

## [Examples](capabilities_module.md#id4)

```yaml+jinja
- name: Set cap_sys_chroot+ep on /foo
  community.general.capabilities:
    path: /foo
    capability: cap_sys_chroot+ep
    state: present

- name: Remove cap_net_bind_service from /bar
  community.general.capabilities:
    path: /bar
    capability: cap_net_bind_service
    state: absent
```

### Authors

- Nate Coraor (@natefoo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
