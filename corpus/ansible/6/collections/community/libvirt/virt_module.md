---
collection: ansible
version: "6"
title: "community.libvirt.virt module – Manages virtual machines supported by libvirt"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/libvirt/virt_module.html
fetched_at: 2026-07-27T17:15:58+00:00
---
# community.libvirt.virt module – Manages virtual machines supported by libvirt

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
> see [Requirements](virt_module.md#ansible-collections-community-libvirt-virt-module-requirements) for details.
>
> To use it in a playbook, specify: `community.libvirt.virt`.

- [Synopsis](virt_module.md#synopsis)
- [Requirements](virt_module.md#requirements)
- [Parameters](virt_module.md#parameters)
- [Examples](virt_module.md#examples)
- [Return Values](virt_module.md#return-values)

## [Synopsis](virt_module.md#id1)

- Manages virtual machines supported by *libvirt*.

## [Requirements](virt_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- libvirt python bindings

## [Parameters](virt_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **autostart**  boolean | Start VM at host startup.  Choices:   - `false` - `true` |
| **command**  string | In addition to state management, various non-idempotent commands are available.  Choices:   - `"create"` - `"define"` - `"destroy"` - `"freemem"` - `"get_xml"` - `"info"` - `"list_vms"` - `"nodeinfo"` - `"pause"` - `"shutdown"` - `"start"` - `"status"` - `"stop"` - `"undefine"` - `"unpause"` - `"virttype"` |
| **name**  aliases: guest  string | name of the guest VM being managed. Note that VM must be previously defined with xml.  This option is required unless *command* is `list_vms` or `info`. |
| **state**  string | Note that there may be some lag for state requests like `shutdown` since these refer only to VM states. After starting a guest, it may not be immediately accessible. state and command are mutually exclusive except when command=list_vms. In this case all VMs in specified state will be listed.  Choices:   - `"destroyed"` - `"paused"` - `"running"` - `"shutdown"` |
| **uri**  string | Libvirt connection uri.  Default: `"qemu:///system"` |
| **xml**  string | XML document used with the define command.  Must be raw XML content using `lookup`. XML cannot be reference to a file. |

## [Examples](virt_module.md#id4)

```yaml+jinja
# a playbook task line:
- name: Start a VM
  community.libvirt.virt:
    name: alpha
    state: running

# /usr/bin/ansible invocations
# ansible host -m virt -a "name=alpha command=status"
# ansible host -m virt -a "name=alpha command=get_xml"
# ansible host -m virt -a "name=alpha command=create uri=lxc:///"

# defining and launching an LXC guest
- name: Define a VM
  community.libvirt.virt:
    command: define
    xml: "{{ lookup('template', 'container-template.xml.j2') }}"
    uri: 'lxc:///'
- name: start vm
  community.libvirt.virt:
    name: foo
    state: running
    uri: 'lxc:///'

# setting autostart on a qemu VM (default uri)
- name: Set autostart for a VM
  community.libvirt.virt:
    name: foo
    autostart: yes

# Defining a VM and making is autostart with host. VM will be off after this task
- name: Define vm from xml and set autostart
  community.libvirt.virt:
    command: define
    xml: "{{ lookup('template', 'vm_template.xml.j2') }}"
    autostart: yes

# Listing VMs
- name: List all VMs
  community.libvirt.virt:
    command: list_vms
  register: all_vms

- name: List only running VMs
  community.libvirt.virt:
    command: list_vms
    state: running
  register: running_vms
```

## [Return Values](virt_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **list_vms**  list / elements=string | The list of vms defined on the remote system.  Returned: success  Sample: `["build.example.org", "dev.example.org"]` |
| **status**  string | The status of the VM, among running, crashed, paused and shutdown.  Returned: success  Sample: `"success"` |

### Authors

- Ansible Core Team
- Michael DeHaan
- Seth Vidal (@skvidal)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.libvirt/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.libvirt)
