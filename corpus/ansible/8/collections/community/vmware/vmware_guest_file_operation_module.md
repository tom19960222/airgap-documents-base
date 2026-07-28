---
collection: ansible
version: "8"
title: "community.vmware.vmware_guest_file_operation module – Files operation in a VMware guest operating system without network"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_guest_file_operation_module.html
fetched_at: 2026-07-28T02:00:13+00:00
---
# community.vmware.vmware_guest_file_operation module – Files operation in a VMware guest operating system without network

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_guest_file_operation`.

- [Synopsis](vmware_guest_file_operation_module.md#synopsis)
- [Parameters](vmware_guest_file_operation_module.md#parameters)
- [Notes](vmware_guest_file_operation_module.md#notes)
- [Examples](vmware_guest_file_operation_module.md#examples)

## [Synopsis](vmware_guest_file_operation_module.md#id1)

- Module to copy a file to a VM, fetch a file from a VM and create or delete a directory in the guest OS.

## [Parameters](vmware_guest_file_operation_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster**  string | The cluster hosting the virtual machine.  If set, it will help to speed up virtual machine search. |
| **copy**  dictionary | Copy file to vm without requiring network. |
| **dest**  string / required | File destination, path must be exist. |
| **overwrite**  boolean | Overwrite or not.  **Choices:**   - `false` ← (default) - `true` |
| **src**  string / required | File source absolute or relative. |
| **datacenter**  string | The datacenter hosting the virtual machine.  If set, it will help to speed up virtual machine search. |
| **directory**  dictionary | Create or delete a directory.  Can be used to create temp directory inside guest using mktemp operation.  mktemp sets variable `dir` in the result with the name of the new directory.  mktemp operation option is added in version 2.8. |
| **operation**  string / required | Operation to perform.  **Choices:**   - `"create"` - `"delete"` - `"mktemp"` |
| **path**  string | Directory path.  Required for `create` or `remove`. |
| **prefix**  string | Temporary directory prefix.  Required for `mktemp`. |
| **recurse**  boolean | Not required.  **Choices:**   - `false` ← (default) - `true` |
| **suffix**  string | Temporary directory suffix.  Required for `mktemp`. |
| **fetch**  dictionary | Get file from virtual machine without requiring network. |
| **dest**  string / required | File destination on localhost, path must be exist. |
| **src**  string / required | The file on the remote system to fetch.  This *must* be a file, not a directory. |
| **folder**  string | Destination folder, absolute path to find an existing guest or create the new guest.  The folder should include the datacenter. ESX’s datacenter is ha-datacenter  Used only if `vm_id_type` is `inventory_path`.  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2  folder: vm/folder2  folder: folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **timeout**  integer  *added in community.vmware 3.1.0* | Timeout seconds for fetching or copying a file.  **Default:** `100` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **vm_id**  string / required | Name of the virtual machine to work with. |
| **vm_id_type**  string | The VMware identification method by which the virtual machine will be identified.  **Choices:**   - `"uuid"` - `"instance_uuid"` - `"dns_name"` - `"inventory_path"` - `"vm_name"` ← (default) |
| **vm_password**  string / required | The password used to login-in to the virtual machine. |
| **vm_username**  string / required | The user to login in to the virtual machine. |

## [Notes](vmware_guest_file_operation_module.md#id3)

> **Note:**
>
> - Only the first match against vm_id is used, even if there are multiple matches
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_file_operation_module.md#id4)

```yaml+jinja
- name: Create directory inside a vm
  community.vmware.vmware_guest_file_operation:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    vm_id: "{{ guest_name }}"
    vm_username: "{{ guest_username }}"
    vm_password: "{{ guest_userpassword }}"
    directory:
      path: "/test"
      operation: create
      recurse: false
  delegate_to: localhost

- name: copy file to vm
  community.vmware.vmware_guest_file_operation:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    vm_id: "{{ guest_name }}"
    vm_username: "{{ guest_username }}"
    vm_password: "{{ guest_userpassword }}"
    copy:
        src: "files/test.zip"
        dest: "/root/test.zip"
        overwrite: false
  delegate_to: localhost

- name: fetch file from vm
  community.vmware.vmware_guest_file_operation:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    vm_id: "{{ guest_name }}"
    vm_username: "{{ guest_username }}"
    vm_password: "{{ guest_userpassword }}"
    fetch:
        src: "/root/test.zip"
        dest: "files/test.zip"
  delegate_to: localhost

- name: If a timeout error occurs, specify a high(er) timeout value
  community.vmware.vmware_guest_file_operation:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    vm_id: "{{ guest_name }}"
    vm_username: "{{ guest_username }}"
    vm_password: "{{ guest_userpassword }}"
    timeout: 10000
    copy:
        src: "files/test.zip"
        dest: "/root/test.zip"
        overwrite: false
  delegate_to: localhost
```

### Authors

- Stéphane Travassac (@stravassac)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
