---
collection: ansible
version: "8"
title: "community.libvirt.virt_net module – Manage libvirt network configuration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/libvirt/virt_net_module.html
fetched_at: 2026-07-28T01:53:51+00:00
---
# community.libvirt.virt_net module – Manage libvirt network configuration

> **Note:**
>
> This module is part of the [community.libvirt collection](https://galaxy.ansible.com/ui/repo/published/community/libvirt/) (version 1.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.libvirt`.
> You need further requirements to be able to use this module,
> see [Requirements](virt_net_module.md#ansible-collections-community-libvirt-virt-net-module-requirements) for details.
>
> To use it in a playbook, specify: `community.libvirt.virt_net`.

- [Synopsis](virt_net_module.md#synopsis)
- [Requirements](virt_net_module.md#requirements)
- [Parameters](virt_net_module.md#parameters)
- [Examples](virt_net_module.md#examples)

## [Synopsis](virt_net_module.md#id1)

- Manage *libvirt* networks.

## [Requirements](virt_net_module.md#id2)

The below requirements are needed on the host that executes this module.

- libvirt python bindings
- python >= 2.6
- python-lxml

## [Parameters](virt_net_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **autostart**  boolean | Specify if a given network should be started automatically on system boot.  **Choices:**   - `false` - `true` |
| **command**  string | In addition to state management, various non-idempotent commands are available. See examples. Modify was added in Ansible version 2.1.  **Choices:**   - `"define"` - `"create"` - `"start"` - `"stop"` - `"destroy"` - `"undefine"` - `"get_xml"` - `"list_nets"` - `"facts"` - `"info"` - `"status"` - `"modify"` |
| **name**  aliases: network  string | Name of the network being managed. Note that network must be previously defined with xml. |
| **state**  string | Specify which state you want a network to be in. If ‘active’, network will be started. If ‘present’, ensure that network is present but do not change its state; if it is missing, you need to specify xml argument. If ‘inactive’, network will be stopped. If ‘undefined’ or ‘absent’, network will be removed from *libvirt* configuration.  **Choices:**   - `"active"` - `"inactive"` - `"present"` - `"absent"` |
| **uri**  string | Libvirt connection uri.  **Default:** `"qemu:///system"` |
| **xml**  string | XML document used with the define command.  Must be raw XML content using `lookup`. XML cannot be reference to a file. |

## [Examples](virt_net_module.md#id4)

```yaml+jinja
- name: Define a new network
  community.libvirt.virt_net:
    command: define
    name: br_nat
    xml: '{{ lookup("template", "network/bridge.xml.j2") }}'

- name: Start a network
  community.libvirt.virt_net:
    command: create
    name: br_nat

- name: List available networks
  community.libvirt.virt_net:
    command: list_nets

- name: Get XML data of a specified network
  community.libvirt.virt_net:
    command: get_xml
    name: br_nat

- name: Stop a network
  community.libvirt.virt_net:
    command: destroy
    name: br_nat

- name: Undefine a network
  community.libvirt.virt_net:
    command: undefine
    name: br_nat

# Gather facts about networks
# Facts will be available as 'ansible_libvirt_networks'
- name: Gather facts about networks
  community.libvirt.virt_net:
    command: facts

- name: Gather information about network managed by 'libvirt' remotely using uri
  community.libvirt.virt_net:
    command: info
    uri: '{{ item }}'
  with_items: '{{ libvirt_uris }}'
  register: networks

- name: Ensure that a network is active (needs to be defined and built first)
  community.libvirt.virt_net:
    state: active
    name: br_nat

- name: Ensure that a network is inactive
  community.libvirt.virt_net:
    state: inactive
    name: br_nat

- name: Ensure that a given network will be started at boot
  community.libvirt.virt_net:
    autostart: true
    name: br_nat

- name: Disable autostart for a given network
  community.libvirt.virt_net:
    autostart: false
    name: br_nat

- name: Add a new host in the dhcp pool
  community.libvirt.virt_net:
    name: br_nat
    command: modify
    xml: "<host mac='FC:C2:33:00:6c:3c' name='my_vm' ip='192.168.122.30'/>"
```

### Authors

- Maciej Delmanowski (@drybjed)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.libvirt/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.libvirt)
