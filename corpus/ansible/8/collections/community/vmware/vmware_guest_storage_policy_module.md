---
collection: ansible
version: "8"
title: "community.vmware.vmware_guest_storage_policy module – Set VM Home and disk(s) storage policy profiles."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_guest_storage_policy_module.html
fetched_at: 2026-07-28T02:00:23+00:00
---
# community.vmware.vmware_guest_storage_policy module – Set VM Home and disk(s) storage policy profiles.

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
> To use it in a playbook, specify: `community.vmware.vmware_guest_storage_policy`.

- [Synopsis](vmware_guest_storage_policy_module.md#synopsis)
- [Parameters](vmware_guest_storage_policy_module.md#parameters)
- [Notes](vmware_guest_storage_policy_module.md#notes)
- [Examples](vmware_guest_storage_policy_module.md#examples)
- [Return Values](vmware_guest_storage_policy_module.md#return-values)

## [Synopsis](vmware_guest_storage_policy_module.md#id1)

- This module can be used to enforce storage policy profiles per disk and/or VM Home on a virtual machine.

## [Parameters](vmware_guest_storage_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **disk**  list / elements=dictionary | A list of disks with storage profile policies to enforce.  All values and parameters are case sensitive.  At least one of `disk` and `vm_home` are required parameters. |
| **controller_number**  integer | SCSI controller number.  Valid values range from 0 to 3.  **Default:** `0` |
| **policy**  string / required | Name of the storage profile policy to enforce for the disk. |
| **unit_number**  integer / required | Disk Unit Number.  Valid values range from 0 to 15. |
| **folder**  string | Destination folder, absolute or relative path to find an existing guest.  This is a required parameter if multiple VMs are found with same name.  The folder should include the datacenter. ESX’s datacenter is ha-datacenter.  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  One of `name`, `uuid`, or `moid` are required to define the virtual machine. |
| **name**  string | Name of the virtual machine.  One of `name`, `uuid`, or `moid` are required to define the virtual machine. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the virtual machine.  One of `name`, `uuid`, or `moid` are required to define the virtual machine. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **vm_home**  string | A storage profile policy to set on VM Home.  All values and parameters are case sensitive.  At least one of `disk` or `vm_home` are required parameters. |

## [Notes](vmware_guest_storage_policy_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_storage_policy_module.md#id4)

```yaml+jinja
- name: Enforce storepol1 policy for disk 0 and 1 on SCSI controller 0 using UUID
  community.vmware.vmware_guest_storage_policy:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    uuid: cefd316c-fc19-45f3-a539-2cd03427a78d
    disk:
      - unit_number: 0
        controller_number: 0
        policy: storepol1
      - unit_number: 1
        controller_number: 0
        policy: storepol1
  delegate_to: localhost
  register: policy_status

- name: Enforce storepol1 policy for VM Home using name
  community.vmware.vmware_guest_storage_policy:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    name: hostname1
    vm_home: storepol1
  delegate_to: localhost
```

## [Return Values](vmware_guest_storage_policy_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed_policies**  dictionary | Dictionary containing the changed policies of disk (list of dictionaries) and vm_home.  **Returned:** always  **Sample:** `{"disk": [{"policy": "storepol1", "unit_number": 0}], "vm_home": "storepol1"}` |
| **msg**  string | Informational message on the job result.  **Returned:** always  **Sample:** `"Policies successfully set."` |

### Authors

- Tyler Gates (@tgates81)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
