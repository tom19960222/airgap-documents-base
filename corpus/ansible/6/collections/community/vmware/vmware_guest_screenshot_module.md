---
collection: ansible
version: "6"
title: "community.vmware.vmware_guest_screenshot module – Create a screenshot of the Virtual Machine console."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_guest_screenshot_module.html
fetched_at: 2026-07-27T17:22:01+00:00
---
# community.vmware.vmware_guest_screenshot module – Create a screenshot of the Virtual Machine console.

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_guest_screenshot`.

- [Synopsis](vmware_guest_screenshot_module.md#synopsis)
- [Parameters](vmware_guest_screenshot_module.md#parameters)
- [Notes](vmware_guest_screenshot_module.md#notes)
- [Examples](vmware_guest_screenshot_module.md#examples)
- [Return Values](vmware_guest_screenshot_module.md#return-values)

## [Synopsis](vmware_guest_screenshot_module.md#id1)

- This module is used to take screenshot of the given virtual machine when virtual machine is powered on.
- All parameters and VMware object names are case sensitive.

## [Parameters](vmware_guest_screenshot_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster**  string | The name of cluster where the virtual machine is running.  This is a required parameter, if `esxi_hostname` is not set.  `esxi_hostname` and `cluster` are mutually exclusive parameters. |
| **datacenter**  string | The datacenter name to which virtual machine belongs to. |
| **esxi_hostname**  string | The ESXi hostname where the virtual machine is running.  This is a required parameter, if `cluster` is not set.  `esxi_hostname` and `cluster` are mutually exclusive parameters. |
| **folder**  string | Destination folder, absolute or relative path to find an existing guest.  This is a required parameter, only if multiple VMs are found with same name.  The folder should include the datacenter. ESXi server’s datacenter is ha-datacenter.  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **local_path**  path | If `local_path` is not set, the created screenshot file will be kept in the directory of the virtual machine on ESXi host. If `local_path` is set to a valid path on local machine, then the screenshot file will be downloaded from ESXi host to the local directory.  If not download screenshot file to local machine, you can open it through the returned file URL in screenshot facts manually. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the virtual machine.  This is a required parameter, if parameter `uuid` or `moid` is not supplied. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the instance to gather facts if known, this is VMware’s unique identifier.  This is a required parameter, if parameter `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_guest_screenshot_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_screenshot_module.md#id4)

```yaml+jinja
- name: take a screenshot of the virtual machine console
  community.vmware.vmware_guest_screenshot:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    folder: "{{ folder_name }}"
    name: "{{ vm_name }}"
    local_path: "/tmp/"
  delegate_to: localhost
  register: take_screenshot

- name: Take a screenshot of the virtual machine console using MoID
  community.vmware.vmware_guest_screenshot:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    folder: "{{ folder_name }}"
    moid: vm-42
    local_path: "/tmp/"
  delegate_to: localhost
  register: take_screenshot
```

## [Return Values](vmware_guest_screenshot_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **screenshot_info**  dictionary | display the facts of captured virtual machine screenshot file  Returned: always  Sample: `{"download_file_size": 2367, "download_local_path": "/tmp/", "result": "success", "screenshot_file": "[datastore0] test_vm/test_vm-1.png", "screenshot_file_url": "https://test_vcenter/folder/test_vm/test_vm-1.png?dcPath=test-dc&dsName=datastore0", "task_complete_time": "2019-05-25T10:35:04.412622Z", "task_start_time": "2019-05-25T10:35:04.215016Z", "virtual_machine": "test_vm"}` |

### Authors

- Diane Wang (@Tomorrow9)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
