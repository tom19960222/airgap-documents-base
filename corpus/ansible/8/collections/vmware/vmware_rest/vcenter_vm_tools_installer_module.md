---
collection: ansible
version: "8"
title: "vmware.vmware_rest.vcenter_vm_tools_installer module – Connects the VMware Tools CD installer as a CD-ROM for the guest operating system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/vcenter_vm_tools_installer_module.html
fetched_at: 2026-07-28T02:58:36+00:00
---
# vmware.vmware_rest.vcenter_vm_tools_installer module – Connects the VMware Tools CD installer as a CD-ROM for the guest operating system

> **Note:**
>
> This module is part of the [vmware.vmware_rest collection](https://galaxy.ansible.com/ui/repo/published/vmware/vmware_rest/) (version 2.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vmware.vmware_rest`.
> You need further requirements to be able to use this module,
> see [Requirements](vcenter_vm_tools_installer_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-tools-installer-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_vm_tools_installer`.

New in vmware.vmware_rest 0.1.0

- [Synopsis](vcenter_vm_tools_installer_module.md#synopsis)
- [Requirements](vcenter_vm_tools_installer_module.md#requirements)
- [Parameters](vcenter_vm_tools_installer_module.md#parameters)
- [Notes](vcenter_vm_tools_installer_module.md#notes)
- [Examples](vcenter_vm_tools_installer_module.md#examples)
- [Return Values](vcenter_vm_tools_installer_module.md#return-values)

## [Synopsis](vcenter_vm_tools_installer_module.md#id1)

- Connects the VMware Tools CD installer as a CD-ROM for the guest operating system. On Windows guest operating systems with autorun, this should cause the installer to initiate the Tools installation which will need user input to complete. On other (non-Windows) guest operating systems this will make the Tools installation available, and a a user will need to do guest-specific actions. On Linux, this includes opening an archive and running the installer. To monitor the status of the Tools install, clients should check the [{@name](mailto:{%40name) vcenter.vm.Tools.Info#versionStatus} and [{@name](mailto:{%40name) vcenter.vm.Tools.Info#runState} from [{@link](mailto:{%40link) vcenter.vm.Tools#get}

## [Requirements](vcenter_vm_tools_installer_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_vm_tools_installer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **session_timeout**  float  *added in vmware.vmware_rest 2.1.0* | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **state**  string / required | **Choices:**   - `"connect"` - `"disconnect"` |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |
| **vm**  string / required | Virtual machine ID This parameter is mandatory. |

## [Notes](vcenter_vm_tools_installer_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_vm_tools_installer_module.md#id5)

```yaml+jinja
- name: Create a VM
  vmware.vmware_rest.vcenter_vm:
    placement:
      cluster: "{{ lookup('vmware.vmware_rest.cluster_moid', '/my_dc/host/my_cluster') }}"
      datastore: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/local') }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources') }}"
    name: test_vm1
    guest_OS: RHEL_7_64
    hardware_version: VMX_11
    memory:
      hot_add_enabled: true
      size_MiB: 1024
    disks:
    - type: SATA
      backing:
        type: VMDK_FILE
        vmdk_file: '[local] test_vm1/{{ disk_name }}.vmdk'
    - type: SATA
      new_vmdk:
        name: second_disk
        capacity: 32000000000
    cdroms:
    - type: SATA
      sata:
        bus: 0
        unit: 2
    nics:
    - backing:
        type: STANDARD_PORTGROUP
        network: "{{ lookup('vmware.vmware_rest.network_moid', '/my_dc/network/VM Network') }}"
  register: my_vm

- name: Update the vm-tools
  vmware.vmware_rest.vcenter_vm_tools_installer:
    vm: '{{ my_vm.id }}'
    state: connect
```

## [Return Values](vcenter_vm_tools_installer_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **value**  dictionary | Update the vm-tools  **Returned:** On success  **Sample:** `{}` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
- [Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
