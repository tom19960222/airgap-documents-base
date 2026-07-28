---
collection: ansible
version: "6"
title: "gluster.gluster.gluster_peer module – Attach/Detach peers to/from the cluster"
source_url: https://docs.ansible.com/projects/ansible/6/collections/gluster/gluster/gluster_peer_module.html
fetched_at: 2026-07-27T17:47:33+00:00
---
# gluster.gluster.gluster_peer module – Attach/Detach peers to/from the cluster

> **Note:**
>
> This module is part of the [gluster.gluster collection](https://galaxy.ansible.com/gluster/gluster) (version 1.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install gluster.gluster`.
> You need further requirements to be able to use this module,
> see [Requirements](gluster_peer_module.md#ansible-collections-gluster-gluster-gluster-peer-module-requirements) for details.
>
> To use it in a playbook, specify: `gluster.gluster.gluster_peer`.

- [Synopsis](gluster_peer_module.md#synopsis)
- [Requirements](gluster_peer_module.md#requirements)
- [Parameters](gluster_peer_module.md#parameters)
- [Notes](gluster_peer_module.md#notes)
- [Examples](gluster_peer_module.md#examples)

## [Synopsis](gluster_peer_module.md#id1)

- Create or diminish a GlusterFS trusted storage pool. A set of nodes can be added into an existing trusted storage pool or a new storage pool can be formed. Or, nodes can be removed from an existing trusted storage pool.

## [Requirements](gluster_peer_module.md#id2)

The below requirements are needed on the host that executes this module.

- GlusterFS > 3.2

## [Parameters](gluster_peer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | Applicable only while removing the nodes from the pool. gluster will refuse to detach a node from the pool if any one of the node is down, in such cases force can be used.  Choices:   - `false` ← (default) - `true` |
| **nodes**  list / elements=string / required | List of nodes that have to be probed into the pool. |
| **state**  string / required | Determines whether the nodes should be attached to the pool or removed from the pool. If the state is present, nodes will be attached to the pool. If state is absent, nodes will be detached from the pool.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](gluster_peer_module.md#id4)

> **Note:**
>
> - This module does not support check mode.

## [Examples](gluster_peer_module.md#id5)

```yaml+jinja
- name: Create a trusted storage pool
  gluster.gluster.gluster_peer:
        state: present
        nodes:
             - 10.0.1.5
             - 10.0.1.10

- name: Delete a node from the trusted storage pool
  gluster.gluster.gluster_peer:
         state: absent
         nodes:
              - 10.0.1.10

- name: Delete a node from the trusted storage pool by force
  gluster.gluster.gluster_peer:
         state: absent
         nodes:
              - 10.0.0.1
         force: true
```

### Authors

- Sachidananda Urs (@sac)

### Collection links

[Issue Tracker](https://github.com/gluster/gluster-ansible-collection/issues)
[Repository (Sources)](https://github.com/gluster/gluster-ansible-collection)
