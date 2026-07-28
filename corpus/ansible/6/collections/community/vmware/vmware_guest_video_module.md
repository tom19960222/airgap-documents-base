---
collection: ansible
version: "6"
title: "community.vmware.vmware_guest_video module – Modify video card configurations of specified virtual machine in given vCenter infrastructure"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_guest_video_module.html
fetched_at: 2026-07-27T17:22:09+00:00
---
# community.vmware.vmware_guest_video module – Modify video card configurations of specified virtual machine in given vCenter infrastructure

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
> To use it in a playbook, specify: `community.vmware.vmware_guest_video`.

- [Synopsis](vmware_guest_video_module.md#synopsis)
- [Parameters](vmware_guest_video_module.md#parameters)
- [Notes](vmware_guest_video_module.md#notes)
- [Examples](vmware_guest_video_module.md#examples)
- [Return Values](vmware_guest_video_module.md#return-values)

## [Synopsis](vmware_guest_video_module.md#id1)

- This module is used to reconfigure video card settings of given virtual machine.
- All parameters and VMware object names are case sensitive.

## [Parameters](vmware_guest_video_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string | The datacenter name to which virtual machine belongs to.  This parameter is case sensitive.  Default: `"ha-datacenter"` |
| **display_number**  integer | The number of display. Valid value from 1 to 10. The maximum display number is 4 on vCenter 6.0, 6.5 web UI. |
| **enable_3D**  boolean | Enable 3D for guest operating systems on which VMware supports 3D.  Choices:   - `false` - `true` |
| **folder**  string | Destination folder, absolute or relative path to find an existing guest.  This is a required parameter, only if multiple VMs are found with same name.  The folder should include the datacenter. ESXi server’s datacenter is ha-datacenter.  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **gather_video_facts**  boolean | If set to `True`, return settings of the video card, other attributes are ignored.  If set to `False`, will do reconfiguration and return video card settings.  Choices:   - `false` ← (default) - `true` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **memory_3D_mb**  integer | The value of 3D Memory must be power of 2 and valid value is from 32 MB to 2048 MB. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the virtual machine.  This is a required parameter, if parameter `uuid` or `moid` is not supplied. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **renderer_3D**  string | If set to `automatic`, selects the appropriate option (software or hardware) for this virtual machine automatically.  If set to `software`, uses normal CPU processing for 3D calculations.  If set to `hardware`, requires graphics hardware (GPU) for faster 3D calculations.  Choices:   - `"automatic"` - `"software"` - `"hardware"` |
| **use_auto_detect**  boolean | If set to `True`, applies common video settings to the guest operating system, attributes `display_number` and `video_memory_mb` are ignored.  If set to `False`, the number of display and the total video memory will be reconfigured using `display_number` and `video_memory_mb`.  Choices:   - `false` - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the instance to gather facts if known, this is VMware’s unique identifier.  This is a required parameter, if parameter `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |
| **video_memory_mb**  float | Valid total MB of video memory range of virtual machine is from 1.172 MB to 256 MB on ESXi 6.7U1, from 1.172 MB to 128 MB on ESXi 6.7 and previous versions.  For specific guest OS, supported minimum and maximum video memory are different, please be careful on setting this. |

## [Notes](vmware_guest_video_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_video_module.md#id4)

```yaml+jinja
- name: Change video card settings of virtual machine
  community.vmware.vmware_guest_video:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    name: test-vm
    gather_video_facts: false
    use_auto_detect: false
    display_number: 2
    video_memory_mb: 8.0
    enable_3D: true
    renderer_3D: automatic
    memory_3D_mb: 512
  delegate_to: localhost
  register: video_facts

- name: Change video card settings of virtual machine using MoID
  community.vmware.vmware_guest_video:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    moid: vm-42
    gather_video_facts: false
    use_auto_detect: false
    display_number: 2
    video_memory_mb: 8.0
    enable_3D: true
    renderer_3D: automatic
    memory_3D_mb: 512
  delegate_to: localhost
  register: video_facts

- name: Gather video card settings of virtual machine
  community.vmware.vmware_guest_video:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    name: test-vm
    gather_video_facts: false
  delegate_to: localhost
  register: video_facts
```

## [Return Values](vmware_guest_video_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **video_status**  dictionary | metadata about the virtual machine’s video card after managing them  Returned: always  Sample: `{"auto_detect": false, "display_number": 2, "enable_3D_support": true, "memory_3D": 524288, "renderer_3D": "automatic", "video_memory": 8192}` |

### Authors

- Diane Wang (@Tomorrow9)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
