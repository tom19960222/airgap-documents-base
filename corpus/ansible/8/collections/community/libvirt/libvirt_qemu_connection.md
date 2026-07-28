---
collection: ansible
version: "8"
title: "community.libvirt.libvirt_qemu connection – Run tasks on libvirt/qemu virtual machines"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/libvirt/libvirt_qemu_connection.html
fetched_at: 2026-07-28T01:53:53+00:00
---
# community.libvirt.libvirt_qemu connection – Run tasks on libvirt/qemu virtual machines

> **Note:**
>
> This connection plugin is part of the [community.libvirt collection](https://galaxy.ansible.com/ui/repo/published/community/libvirt/) (version 1.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.libvirt`.
> You need further requirements to be able to use this connection plugin,
> see [Requirements](libvirt_qemu_connection.md#ansible-collections-community-libvirt-libvirt-qemu-connection-requirements) for details.
>
> To use it in a playbook, specify: `community.libvirt.libvirt_qemu`.

New in community.libvirt 2.10.0

- [Synopsis](libvirt_qemu_connection.md#synopsis)
- [Requirements](libvirt_qemu_connection.md#requirements)
- [Parameters](libvirt_qemu_connection.md#parameters)
- [Notes](libvirt_qemu_connection.md#notes)

## [Synopsis](libvirt_qemu_connection.md#id1)

- Run commands or put/fetch files to libvirt/qemu virtual machines using the qemu agent API.

## [Requirements](libvirt_qemu_connection.md#id2)

The below requirements are needed on the local controller node that executes this connection.

- python >= 2.6
- libvirt python bindings

## [Parameters](libvirt_qemu_connection.md#id3)

| Parameter | Comments |
| --- | --- |
| **executable**  string | Shell to use for execution inside container.  Set this to ‘cmd’ or ‘powershell’ for Windows VMs.  **Default:** `"/bin/sh"`  **Configuration:**   - Variable: ansible_shell_type |
| **remote_addr**  string | Virtual machine name.  **Default:** `"inventory_hostname"`  **Configuration:**   - Variable: ansible_host - Variable: inventory_hostname |
| **virt_uri**  string | Libvirt URI to connect to to access the virtual machine.  **Default:** `"qemu:///system"`  **Configuration:**   - Variable: ansible_libvirt_uri |

## [Notes](libvirt_qemu_connection.md#id4)

> **Note:**
>
> - Currently DOES NOT work with selinux set to enforcing in the VM.
> - Requires the qemu-agent installed in the VM.
> - Requires access to the qemu-ga commands guest-exec, guest-exec-status, guest-file-close, guest-file-open, guest-file-read, guest-file-write.

### Authors

- Jesse Pretorius (@odyssey4me)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.libvirt/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.libvirt)
