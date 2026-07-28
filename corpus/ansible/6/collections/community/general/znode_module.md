---
collection: ansible
version: "6"
title: "community.general.znode module – Create, delete, retrieve, and update znodes using ZooKeeper"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/znode_module.html
fetched_at: 2026-07-27T17:14:13+00:00
---
# community.general.znode module – Create, delete, retrieve, and update znodes using ZooKeeper

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
> see [Requirements](znode_module.md#ansible-collections-community-general-znode-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.znode`.

- [Synopsis](znode_module.md#synopsis)
- [Requirements](znode_module.md#requirements)
- [Parameters](znode_module.md#parameters)
- [Examples](znode_module.md#examples)

## [Synopsis](znode_module.md#id1)

- Create, delete, retrieve, and update znodes using ZooKeeper.

## [Requirements](znode_module.md#id2)

The below requirements are needed on the host that executes this module.

- kazoo >= 2.1
- python >= 2.6

## [Parameters](znode_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_credential**  string  added in community.general 5.8.0 | The authentication credential value. Depends on *auth_scheme*.  The format for *auth_scheme=digest* is `user:password`, and the format for *auth_scheme=sasl* is `user:password`. |
| **auth_scheme**  string  added in community.general 5.8.0 | Authentication scheme.  Choices:   - `"digest"` ← (default) - `"sasl"` |
| **hosts**  string / required | A list of ZooKeeper servers (format ‘[server]:[port]’). |
| **name**  string / required | The path of the znode. |
| **op**  string | An operation to perform. Mutually exclusive with state.  Choices:   - `"get"` - `"wait"` - `"list"` |
| **recursive**  boolean | Recursively delete node and all its children.  Choices:   - `false` ← (default) - `true` |
| **state**  string | The state to enforce. Mutually exclusive with op.  Choices:   - `"present"` - `"absent"` |
| **timeout**  integer | The amount of time to wait for a node to appear.  Default: `300` |
| **value**  string | The value assigned to the znode. |

## [Examples](znode_module.md#id4)

```yaml+jinja
- name: Creating or updating a znode with a given value
  community.general.znode:
    hosts: 'localhost:2181'
    name: /mypath
    value: myvalue
    state: present

- name: Getting the value and stat structure for a znode
  community.general.znode:
    hosts: 'localhost:2181'
    name: /mypath
    op: get

- name: Getting the value and stat structure for a znode using digest authentication
  community.general.znode:
    hosts: 'localhost:2181'
    auth_credential: 'user1:s3cr3t'
    name: /secretmypath
    op: get

- name: Listing a particular znode's children
  community.general.znode:
    hosts: 'localhost:2181'
    name: /zookeeper
    op: list

- name: Waiting 20 seconds for a znode to appear at path /mypath
  community.general.znode:
    hosts: 'localhost:2181'
    name: /mypath
    op: wait
    timeout: 20

- name: Deleting a znode at path /mypath
  community.general.znode:
    hosts: 'localhost:2181'
    name: /mypath
    state: absent

- name: Creating or updating a znode with a given value on a remote Zookeeper
  community.general.znode:
    hosts: 'my-zookeeper-node:2181'
    name: /mypath
    value: myvalue
    state: present
  delegate_to: 127.0.0.1
```

### Authors

- Trey Perry (@treyperry)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
