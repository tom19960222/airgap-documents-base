---
collection: ansible
version: "8"
title: "community.vmware.vsphere_file module – Manage files on a vCenter datastore"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vsphere_file_module.html
fetched_at: 2026-07-28T02:01:32+00:00
---
# community.vmware.vsphere_file module – Manage files on a vCenter datastore

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
> To use it in a playbook, specify: `community.vmware.vsphere_file`.

- [Synopsis](vsphere_file_module.md#synopsis)
- [Parameters](vsphere_file_module.md#parameters)
- [Notes](vsphere_file_module.md#notes)
- [Examples](vsphere_file_module.md#examples)

## [Synopsis](vsphere_file_module.md#id1)

- Manage files on a vCenter datastore.

## [Parameters](vsphere_file_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string / required | The datacenter on the vCenter server that holds the datastore. |
| **datastore**  string / required | The datastore on the vCenter server to push files to. |
| **host**  aliases: hostname  string / required | The vCenter server on which the datastore is available. |
| **password**  string / required | The password to authenticate on the vCenter server. |
| **path**  aliases: dest  string / required | The file or directory on the datastore on the vCenter server. |
| **state**  string | The state of or the action on the provided path.  If `absent`, the file will be removed.  If `directory`, the directory will be created.  If `file`, more information of the (existing) file will be returned.  If `touch`, an empty file will be created if the path does not exist.  **Choices:**   - `"absent"` - `"directory"` - `"file"` ← (default) - `"touch"` |
| **timeout**  integer | The timeout in seconds for the upload to the datastore.  **Default:** `10` |
| **username**  string / required | The user name to authenticate on the vCenter server. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be set to `false` when no other option exists.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vsphere_file_module.md#id3)

> **Note:**
>
> - The vSphere folder API does not allow to remove directory objects.

## [Examples](vsphere_file_module.md#id4)

```yaml+jinja
- name: Create an empty file on a datastore
  community.vmware.vsphere_file:
    host: '{{ vhost }}'
    username: '{{ vuser }}'
    password: '{{ vpass }}'
    datacenter: DC1 Someplace
    datastore: datastore1
    path: some/remote/file
    state: touch
  delegate_to: localhost

- name: Create a directory on a datastore
  community.vmware.vsphere_file:
    host: '{{ vhost }}'
    username: '{{ vuser }}'
    password: '{{ vpass }}'
    datacenter: DC2 Someplace
    datastore: datastore2
    path: other/remote/file
    state: directory
  delegate_to: localhost

- name: Query a file on a datastore
  community.vmware.vsphere_file:
    host: '{{ vhost }}'
    username: '{{ vuser }}'
    password: '{{ vpass }}'
    datacenter: DC1 Someplace
    datastore: datastore1
    path: some/remote/file
    state: file
  delegate_to: localhost
  ignore_errors: true

- name: Delete a file on a datastore
  community.vmware.vsphere_file:
    host: '{{ vhost }}'
    username: '{{ vuser }}'
    password: '{{ vpass }}'
    datacenter: DC2 Someplace
    datastore: datastore2
    path: other/remote/file
    state: absent
  delegate_to: localhost
```

### Authors

- Dag Wieers (@dagwieers)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
