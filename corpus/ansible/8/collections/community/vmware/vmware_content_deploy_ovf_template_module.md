---
collection: ansible
version: "8"
title: "community.vmware.vmware_content_deploy_ovf_template module – Deploy Virtual Machine from ovf template stored in content library."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_content_deploy_ovf_template_module.html
fetched_at: 2026-07-28T01:59:42+00:00
---
# community.vmware.vmware_content_deploy_ovf_template module – Deploy Virtual Machine from ovf template stored in content library.

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
> You need further requirements to be able to use this module,
> see [Requirements](vmware_content_deploy_ovf_template_module.md#ansible-collections-community-vmware-vmware-content-deploy-ovf-template-module-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_content_deploy_ovf_template`.

- [Synopsis](vmware_content_deploy_ovf_template_module.md#synopsis)
- [Requirements](vmware_content_deploy_ovf_template_module.md#requirements)
- [Parameters](vmware_content_deploy_ovf_template_module.md#parameters)
- [Examples](vmware_content_deploy_ovf_template_module.md#examples)
- [Return Values](vmware_content_deploy_ovf_template_module.md#return-values)

## [Synopsis](vmware_content_deploy_ovf_template_module.md#id1)

- Module to deploy virtual machine from ovf template in content library.
- All variables and VMware object names are case sensitive.

## [Requirements](vmware_content_deploy_ovf_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere Automation SDK

## [Parameters](vmware_content_deploy_ovf_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cluster**  string | Name of the cluster in datacenter in which to place deployed VM. |
| **datacenter**  string / required | Name of the datacenter, where VM to be deployed. |
| **datastore**  string | Name of the datastore to store deployed VM and disk. |
| **datastore_cluster**  string | Name of the datastore cluster housing a datastore to store deployed VM and disk.  If datastore is not specified, the recommended datastore from this cluster will be used. |
| **folder**  string | Name of the folder in datacenter in which to place deployed VM.  **Default:** `"vm"` |
| **host**  string | Name of the ESX Host in datacenter in which to place deployed VM. The host has to be a member of the cluster that contains the resource pool. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **library**  aliases: content_library, content_library_src  string | The name of the content library from where the template resides. |
| **log_level**  string | The level of logging desired in this module.  **Choices:**   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **name**  aliases: vm_name  string / required | The name of the VM to be deployed. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **port**  integer | The port number of the vSphere vCenter.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  **Default:** `443` |
| **protocol**  string | The connection to protocol.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead. |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **resource_pool**  string | Name of the resourcepool in datacenter in which to place deployed VM. |
| **storage_provisioning**  string | Default storage provisioning type to use for all sections of type vmw:StorageSection in the OVF descriptor.  **Choices:**   - `"thin"` ← (default) - `"thick"` - `"eagerZeroedThick"` - `"eagerzeroedthick"` |
| **template**  aliases: ovf, ovf_template, template_src  string / required | The name of OVF template from which VM to be deployed. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid.  Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](vmware_content_deploy_ovf_template_module.md#id4)

```yaml+jinja
- name: Deploy Virtual Machine from OVF template in content library
  community.vmware.vmware_content_deploy_ovf_template:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    ovf_template: rhel_test_template
    datastore: Shared_NFS_Volume
    folder: vm
    datacenter: Sample_DC_1
    name: Sample_VM
    resource_pool: test_rp
  delegate_to: localhost

- name: Deploy Virtual Machine from OVF template in content library with eagerZeroedThick storage
  vmware_content_deploy_ovf_template:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    ovf_template: rhel_test_template
    datastore: Shared_NFS_Volume
    folder: vm
    datacenter: Sample_DC_1
    name: Sample_VM
    resource_pool: test_rp
    storage_provisioning: eagerZeroedThick
  delegate_to: localhost
```

## [Return Values](vmware_content_deploy_ovf_template_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vm_deploy_info**  dictionary | Virtual machine deployment message and vm_id  **Returned:** on success  **Sample:** `{"msg": "Deployed Virtual Machine 'Sample_VM'.", "vm_id": "vm-1009"}` |

### Authors

- Lev Goncharv (@ultral)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
