---
collection: ansible
version: "6"
title: "vmware.vmware_rest.vcenter_vm_guest_power module – Issues a request to the guest operating system asking it to perform a soft shutdown, standby (suspend) or soft reboot"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/vcenter_vm_guest_power_module.html
fetched_at: 2026-07-28T00:22:19+00:00
---
# vmware.vmware_rest.vcenter_vm_guest_power module – Issues a request to the guest operating system asking it to perform a soft shutdown, standby (suspend) or soft reboot

> **Note:**
>
> This module is part of the [vmware.vmware_rest collection](https://galaxy.ansible.com/vmware/vmware_rest) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vmware.vmware_rest`.
> You need further requirements to be able to use this module,
> see [Requirements](vcenter_vm_guest_power_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-guest-power-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_vm_guest_power`.

New in vmware.vmware_rest 0.1.0

- [Synopsis](vcenter_vm_guest_power_module.md#synopsis)
- [Requirements](vcenter_vm_guest_power_module.md#requirements)
- [Parameters](vcenter_vm_guest_power_module.md#parameters)
- [Notes](vcenter_vm_guest_power_module.md#notes)
- [See Also](vcenter_vm_guest_power_module.md#see-also)
- [Examples](vcenter_vm_guest_power_module.md#examples)
- [Return Values](vcenter_vm_guest_power_module.md#return-values)

## [Synopsis](vcenter_vm_guest_power_module.md#id1)

- Issues a request to the guest operating system asking it to perform a soft shutdown, standby (suspend) or soft reboot. This request returns immediately and does not wait for the guest operating.

## [Requirements](vcenter_vm_guest_power_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_vm_guest_power_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **session_timeout**  float  added in vmware.vmware_rest 2.1.0 | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **state**  string / required | Choices:   - `"reboot"` - `"shutdown"` - `"standby"` |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |
| **vm**  string / required | Identifier of the virtual machine. This parameter is mandatory. |

## [Notes](vcenter_vm_guest_power_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [See Also](vcenter_vm_guest_power_module.md#id5)

> **See also:**
>
> [vmware.vmware_rest.vcenter_vm_power](vcenter_vm_power_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-power-module)
> :   A module to boot, hard shutdown and hard reset guest

## [Examples](vcenter_vm_guest_power_module.md#id6)

```yaml+jinja
- name: Create a VM
  vmware.vmware_rest.vcenter_vm:
    placement:
      cluster: "{{ lookup('vmware.vmware_rest.cluster_moid', '/my_dc/host/my_cluster')\
        \ }}"
      datastore: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/local')\
        \ }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources')\
        \ }}"
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
        network: "{{ lookup('vmware.vmware_rest.network_moid', '/my_dc/network/VM\
          \ Network') }}"

  register: my_vm

- name: Shut down the VM
  vmware.vmware_rest.vcenter_vm_guest_power:
    state: shutdown
    vm: '{{ my_vm.id }}'
```

## [Return Values](vcenter_vm_guest_power_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **value**  dictionary | Shut down the VM  Returned: On success  Sample: `{}` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
[Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
