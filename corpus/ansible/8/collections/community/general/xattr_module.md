---
collection: ansible
version: "8"
title: "community.general.xattr module – Manage user defined extended attributes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/xattr_module.html
fetched_at: 2026-07-28T01:51:27+00:00
---
# community.general.xattr module – Manage user defined extended attributes

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
> To use it in a playbook, specify: `community.general.xattr`.

- [Synopsis](xattr_module.md#synopsis)
- [Parameters](xattr_module.md#parameters)
- [Attributes](xattr_module.md#attributes)
- [Notes](xattr_module.md#notes)
- [Examples](xattr_module.md#examples)

## [Synopsis](xattr_module.md#id1)

- Manages filesystem user defined extended attributes.
- Requires that extended attributes are enabled on the target filesystem and that the setfattr/getfattr utilities are present.

Aliases: files.xattr

## [Parameters](xattr_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **follow**  boolean | If `true`, dereferences symlinks and sets/gets attributes on symlink target, otherwise acts on symlink itself.  **Choices:**   - `false` - `true` ← (default) |
| **key**  string | The name of a specific Extended attribute key to set/retrieve. |
| **namespace**  string | Namespace of the named name/key.  **Default:** `"user"` |
| **path**  aliases: name  path / required | The full path of the file/object to get the facts of.  Before 2.3 this option was only usable as `name`. |
| **state**  string | defines which state you want to do. `read` retrieves the current value for a `key` (default) `present` sets `path` to `value`, default if value is set `all` dumps all data `keys` retrieves all keys `absent` deletes the key  **Choices:**   - `"absent"` - `"all"` - `"keys"` - `"present"` - `"read"` ← (default) |
| **value**  string | The value to set the named name/key to, it automatically sets the `state` to `present`. |

## [Attributes](xattr_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](xattr_module.md#id4)

> **Note:**
>
> - As of Ansible 2.3, the `name` option has been changed to `path` as default, but `name` still works as well.

## [Examples](xattr_module.md#id5)

```yaml+jinja
- name: Obtain the extended attributes  of /etc/foo.conf
  community.general.xattr:
    path: /etc/foo.conf

- name: Set the key 'user.foo' to value 'bar'
  community.general.xattr:
    path: /etc/foo.conf
    key: foo
    value: bar

- name: Set the key 'trusted.glusterfs.volume-id' to value '0x817b94343f164f199e5b573b4ea1f914'
  community.general.xattr:
    path: /mnt/bricks/brick1
    namespace: trusted
    key: glusterfs.volume-id
    value: "0x817b94343f164f199e5b573b4ea1f914"

- name: Remove the key 'user.foo'
  community.general.xattr:
    path: /etc/foo.conf
    key: foo
    state: absent

- name: Remove the key 'trusted.glusterfs.volume-id'
  community.general.xattr:
    path: /mnt/bricks/brick1
    namespace: trusted
    key: glusterfs.volume-id
    state: absent
```

### Authors

- Brian Coca (@bcoca)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
