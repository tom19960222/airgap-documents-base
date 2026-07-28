---
collection: ansible
version: "6"
title: "community.vmware.vmware_content_deploy_template module – Deploy Virtual Machine from template stored in content library."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_content_deploy_template_module.html
fetched_at: 2026-07-27T17:21:28+00:00
---
# community.vmware.vmware_content_deploy_template module – Deploy Virtual Machine from template stored in content library.

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
> You need further requirements to be able to use this module,
> see [Requirements](vmware_content_deploy_template_module.md#ansible-collections-community-vmware-vmware-content-deploy-template-module-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_content_deploy_template`.

- [Synopsis](vmware_content_deploy_template_module.md#synopsis)
- [Requirements](vmware_content_deploy_template_module.md#requirements)
- [Parameters](vmware_content_deploy_template_module.md#parameters)
- [Examples](vmware_content_deploy_template_module.md#examples)
- [Return Values](vmware_content_deploy_template_module.md#return-values)

## [Synopsis](vmware_content_deploy_template_module.md#id1)

- Module to deploy virtual machine from template in content library.
- Content Library feature is introduced in vSphere 6.0 version.
- vmtx templates feature is introduced in vSphere 67U1 and APIs for clone template from content library in 67U2.
- This module does not work with vSphere version older than 67U2.
- All variables and VMware object names are case sensitive.

## [Requirements](vmware_content_deploy_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere Automation SDK

## [Parameters](vmware_content_deploy_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cluster**  string | Name of the cluster in datacenter in which to place deployed VM.  Required if *resource_pool* is not specified. |
| **datacenter**  string / required | Name of the datacenter, where VM to be deployed. |
| **datastore**  string | Name of the datastore to store deployed VM and disk.  Required if *datastore_cluster* is not provided. |
| **datastore_cluster**  string  added in community.vmware 1.7.0 | Name of the datastore cluster to store deployed VM and disk.  Please make sure Storage DRS is active for recommended datastore from the given datastore cluster.  If Storage DRS is not enabled, datastore with largest free storage space is selected.  Required if *datastore* is not provided. |
| **folder**  string | Name of the folder in datacenter in which to place deployed VM.  Default: `"vm"` |
| **host**  string | Name of the ESX Host in datacenter in which to place deployed VM.  The host has to be a member of the cluster that contains the resource pool.  Required with *resource_pool* to find resource pool details. This will be used as additional information when there are resource pools with same name. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **library**  aliases: content_library, content_library_src  string | The name of the content library from where the template resides. |
| **log_level**  string  added in community.vmware 1.9.0 | The level of logging desired in this module.  Choices:   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **name**  aliases: vm_name  string / required | The name of the VM to be deployed. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **port**  integer | The port number of the vSphere vCenter.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Default: `443` |
| **protocol**  string | The connection to protocol.  Choices:   - `"http"` - `"https"` ← (default) |
| **proxy_host**  string  added in community.vmware 1.12.0 | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead. |
| **proxy_port**  integer  added in community.vmware 1.12.0 | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **resource_pool**  string | Name of the resource pool in datacenter in which to place deployed VM.  Required if *cluster* is not specified.  For default or non-unique resource pool names, specify *host* and *cluster*.  `Resources` is the default name of resource pool. |
| **state**  string | The state of Virtual Machine deployed from template in content library.  If set to `present` and VM does not exists, then VM is created.  If set to `present` and VM exists, no action is taken.  If set to `poweredon` and VM does not exists, then VM is created with powered on state.  If set to `poweredon` and VM exists, no action is taken.  Choices:   - `"present"` ← (default) - `"poweredon"` |
| **template**  aliases: template_src  string / required | The name of template from which VM to be deployed. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid.  Set to `False` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](vmware_content_deploy_template_module.md#id4)

```yaml+jinja
- name: Deploy Virtual Machine from template in content library
  community.vmware.vmware_content_deploy_template:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    template: rhel_test_template
    datastore: Shared_NFS_Volume
    folder: vm
    datacenter: Sample_DC_1
    name: Sample_VM
    resource_pool: test_rp
    state: present
  delegate_to: localhost

- name: Deploy Virtual Machine from template in content library with PowerON State
  community.vmware.vmware_content_deploy_template:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    template: rhel_test_template
    content_library: test_content_library
    datastore: Shared_NFS_Volume
    folder: vm
    datacenter: Sample_DC_1
    name: Sample_VM
    resource_pool: test_rp
    state: poweredon
  delegate_to: localhost
```

## [Return Values](vmware_content_deploy_template_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vm_deploy_info**  dictionary | Virtual machine deployment message and vm_id  Returned: on success  Sample: `{"msg": "Deployed Virtual Machine 'Sample_VM'.", "vm_id": "vm-1009"}` |

### Authors

- Pavan Bidkar (@pgbidkar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
