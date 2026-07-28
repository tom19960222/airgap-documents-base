---
collection: ansible
version: "8"
title: "gluster.gluster.gluster_volume module – Manage GlusterFS volumes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/gluster/gluster/gluster_volume_module.html
fetched_at: 2026-07-28T01:05:43+00:00
---
# gluster.gluster.gluster_volume module – Manage GlusterFS volumes

> **Note:**
>
> This module is part of the [gluster.gluster collection](https://galaxy.ansible.com/ui/repo/published/gluster/gluster/) (version 1.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install gluster.gluster`.
>
> To use it in a playbook, specify: `gluster.gluster.gluster_volume`.

- [Synopsis](gluster_volume_module.md#synopsis)
- [Parameters](gluster_volume_module.md#parameters)
- [Notes](gluster_volume_module.md#notes)
- [Examples](gluster_volume_module.md#examples)

## [Synopsis](gluster_volume_module.md#id1)

- Create, remove, start, stop and tune GlusterFS volumes

## [Parameters](gluster_volume_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **arbiters**  integer | Arbiter count for volume. |
| **bricks**  aliases: brick  string | Brick paths on servers. Multiple brick paths can be separated by commas. |
| **cluster**  list / elements=string | List of hosts to use for probing and brick setup. |
| **directory**  string | Directory for limit-usage. |
| **disperses**  integer | Disperse count for volume. |
| **force**  boolean | If brick is being created in the root partition, module will fail. Set force to true to override this behaviour.  **Choices:**   - `false` - `true` |
| **host**  string | Override local hostname (for peer probing purposes). |
| **name**  aliases: volume  string / required | The volume name. |
| **options**  dictionary | A dictionary/hash with options/settings for the volume. |
| **quota**  string | Quota value for limit-usage (be sure to use 10.0MB instead of 10MB, see quota list). |
| **rebalance**  boolean | Controls whether the cluster is rebalanced after changes.  **Choices:**   - `false` ← (default) - `true` |
| **redundancies**  integer | Redundancy count for volume. |
| **replicas**  integer | Replica count for volume. |
| **start_on_create**  boolean | Controls whether the volume is started after creation or not.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string / required | Use present/absent ensure if a volume exists or not. Use started/stopped to control its availability.  **Choices:**   - `"absent"` - `"present"` - `"started"` - `"stopped"` |
| **stripes**  integer | Stripe count for volume. |
| **transport**  string | Transport type for volume.  **Choices:**   - `"tcp"` ← (default) - `"rdma"` - `"tcp,rdma"` |

## [Notes](gluster_volume_module.md#id3)

> **Note:**
>
> - Requires cli tools for GlusterFS on servers.
> - Will add new bricks, but not remove them.

## [Examples](gluster_volume_module.md#id4)

```yaml+jinja
- name: create gluster volume
  gluster.gluster.gluster_volume:
    state: present
    name: test1
    bricks: /bricks/brick1/g1
    rebalance: yes
    cluster:
      - 192.0.2.10
      - 192.0.2.11
  run_once: true

- name: tune
  gluster.gluster.gluster_volume:
    state: present
    name: test1
    options:
      performance.cache-size: 256MB

- name: Set multiple options on GlusterFS volume
  gluster.gluster.gluster_volume:
    state: present
    name: test1
    options:
      { performance.cache-size: 128MB,
        write-behind: 'off',
        quick-read: 'on'
      }

- name: start gluster volume
  gluster.gluster.gluster_volume:
    state: started
    name: test1

- name: limit usage
  gluster.gluster.gluster_volume:
    state: present
    name: test1
    directory: /foo
    quota: 20.0MB

- name: stop gluster volume
  gluster.gluster.gluster_volume:
    state: stopped
    name: test1

- name: remove gluster volume
  gluster.gluster.gluster_volume:
    state: absent
    name: test1

- name: create gluster volume with multiple bricks
  gluster.gluster.gluster_volume:
    state: present
    name: test2
    bricks: /bricks/brick1/g2,/bricks/brick2/g2
    cluster:
      - 192.0.2.10
      - 192.0.2.11
  run_once: true

- name: Remove the bricks from gluster volume
  gluster.gluster.gluster_volume:
    state: present
    name: testvol
    bricks: /bricks/brick1/b1,/bricks/brick2/b2
    cluster:
      - 10.70.42.85
    force: true
  run_once: true

- name: Reduce cluster configuration
  gluster.gluster.gluster_volume:
    state: present
    name: testvol
    bricks: /bricks/brick3/b1,/bricks/brick4/b2
    replicas: 2
    cluster:
      - 10.70.42.85
    force: true
  run_once: true
```

### Authors

- Taneli Leppä (@rosmo)

### Collection links

- [Issue Tracker](https://github.com/gluster/gluster-ansible-collection/issues)
- [Repository (Sources)](https://github.com/gluster/gluster-ansible-collection)
