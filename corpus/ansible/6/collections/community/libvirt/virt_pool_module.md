---
collection: ansible
version: "6"
title: "community.libvirt.virt_pool module – Manage libvirt storage pools"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/libvirt/virt_pool_module.html
fetched_at: 2026-07-27T17:15:59+00:00
---
# community.libvirt.virt_pool module – Manage libvirt storage pools

> **Note:**
>
> This module is part of the [community.libvirt collection](https://galaxy.ansible.com/community/libvirt) (version 1.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.libvirt`.
> You need further requirements to be able to use this module,
> see [Requirements](virt_pool_module.md#ansible-collections-community-libvirt-virt-pool-module-requirements) for details.
>
> To use it in a playbook, specify: `community.libvirt.virt_pool`.

- [Synopsis](virt_pool_module.md#synopsis)
- [Requirements](virt_pool_module.md#requirements)
- [Parameters](virt_pool_module.md#parameters)
- [Examples](virt_pool_module.md#examples)

## [Synopsis](virt_pool_module.md#id1)

- Manage *libvirt* storage pools.

## [Requirements](virt_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- libvirt python bindings
- python >= 2.6
- python-lxml

## [Parameters](virt_pool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **autostart**  boolean | Specify if a given storage pool should be started automatically on system boot.  Choices:   - `false` - `true` |
| **command**  string | In addition to state management, various non-idempotent commands are available. See examples.  Choices:   - `"define"` - `"build"` - `"create"` - `"start"` - `"stop"` - `"destroy"` - `"delete"` - `"undefine"` - `"get_xml"` - `"list_pools"` - `"facts"` - `"info"` - `"status"` - `"refresh"` |
| **mode**  string | Pass additional parameters to ‘build’ or ‘delete’ commands.  Choices:   - `"new"` - `"repair"` - `"resize"` - `"no_overwrite"` - `"overwrite"` - `"normal"` - `"zeroed"` |
| **name**  aliases: pool  string | Name of the storage pool being managed. Note that pool must be previously defined with xml. |
| **state**  string | Specify which state you want a storage pool to be in. If ‘active’, pool will be started. If ‘present’, ensure that pool is present but do not change its state; if it is missing, you need to specify xml argument. If ‘inactive’, pool will be stopped. If ‘undefined’ or ‘absent’, pool will be removed from *libvirt* configuration. If ‘deleted’, pool contents will be deleted and then pool undefined.  Choices:   - `"active"` - `"inactive"` - `"present"` - `"absent"` - `"undefined"` - `"deleted"` |
| **uri**  string | Libvirt connection uri.  Default: `"qemu:///system"` |
| **xml**  string | XML document used with the define command.  Must be raw XML content using `lookup`. XML cannot be reference to a file. |

## [Examples](virt_pool_module.md#id4)

```yaml+jinja
- name: Define a new storage pool
  community.libvirt.virt_pool:
    command: define
    name: vms
    xml: '{{ lookup("template", "pool/dir.xml.j2") }}'

- name: Build a storage pool if it does not exist
  community.libvirt.virt_pool:
    command: build
    name: vms

- name: Start a storage pool
  community.libvirt.virt_pool:
    command: create
    name: vms

- name: List available pools
  community.libvirt.virt_pool:
    command: list_pools

- name: Get XML data of a specified pool
  community.libvirt.virt_pool:
    command: get_xml
    name: vms

- name: Stop a storage pool
  community.libvirt.virt_pool:
    command: destroy
    name: vms

- name: Delete a storage pool (destroys contents)
  community.libvirt.virt_pool:
    command: delete
    name: vms

- name: Undefine a storage pool
  community.libvirt.virt_pool:
    command: undefine
    name: vms

# Gather facts about storage pools
# Facts will be available as 'ansible_libvirt_pools'
- name: Gather facts about storage pools
  community.libvirt.virt_pool:
    command: facts

- name: Gather information about pools managed by 'libvirt' remotely using uri
  community.libvirt.virt_pool:
    command: info
    uri: '{{ item }}'
  with_items: '{{ libvirt_uris }}'
  register: storage_pools

- name: Ensure that a pool is active (needs to be defined and built first)
  community.libvirt.virt_pool:
    state: active
    name: vms

- name: Ensure that a pool is inactive
  community.libvirt.virt_pool:
    state: inactive
    name: vms

- name: Ensure that a given pool will be started at boot
  community.libvirt.virt_pool:
    autostart: yes
    name: vms

- name: Disable autostart for a given pool
  community.libvirt.virt_pool:
    autostart: no
    name: vms
```

### Authors

- Maciej Delmanowski (@drybjed)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.libvirt/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.libvirt)
