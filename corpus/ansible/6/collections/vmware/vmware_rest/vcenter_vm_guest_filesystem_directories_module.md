---
collection: ansible
version: "6"
title: "vmware.vmware_rest.vcenter_vm_guest_filesystem_directories module – Creates a directory in the guest operating system"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/vcenter_vm_guest_filesystem_directories_module.html
fetched_at: 2026-07-28T00:22:15+00:00
---
# vmware.vmware_rest.vcenter_vm_guest_filesystem_directories module – Creates a directory in the guest operating system

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
> see [Requirements](vcenter_vm_guest_filesystem_directories_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-guest-filesystem-directories-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_vm_guest_filesystem_directories`.

New in vmware.vmware_rest 2.0.0

- [Synopsis](vcenter_vm_guest_filesystem_directories_module.md#synopsis)
- [Requirements](vcenter_vm_guest_filesystem_directories_module.md#requirements)
- [Parameters](vcenter_vm_guest_filesystem_directories_module.md#parameters)
- [Notes](vcenter_vm_guest_filesystem_directories_module.md#notes)
- [Examples](vcenter_vm_guest_filesystem_directories_module.md#examples)

## [Synopsis](vcenter_vm_guest_filesystem_directories_module.md#id1)

- Creates a directory in the guest operating system. <p>

## [Requirements](vcenter_vm_guest_filesystem_directories_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_vm_guest_filesystem_directories_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **create_parents**  boolean | Whether any parent directories should be created. If any failure occurs, some parent directories could be left behind.  Choices:   - `false` - `true` |
| **credentials**  dictionary / required | The guest authentication data. This parameter is mandatory.  Valid attributes are:  - `interactive_session` (bool): If [{@term](mailto:{%40term) set}, theoperation will interact with the logged-in desktop session in the guest. This requires that the logged-on user matches the user specified by the [{@link](mailto:{%40link) Credentials}. This is currently only supported for [{@link](mailto:{%40link) Type#USERNAME_PASSWORD}. ([‘absent’, ‘create_temporary’, ‘move’, ‘present’])  This key is required with [‘absent’, ‘create_temporary’, ‘move’, ‘present’]. - `type` (str): Types of guest credentials ([‘absent’, ‘create_temporary’, ‘move’, ‘present’])  This key is required with [‘absent’, ‘create_temporary’, ‘move’, ‘present’].    - Accepted values:      - SAML_BEARER_TOKEN     - USERNAME_PASSWORD - `user_name` (str): For [{@link](mailto:{%40link) Type#SAML_BEARER_TOKEN}, this is the guest user to be associated with the credentials. For [{@link](mailto:{%40link) Type#USERNAME_PASSWORD} this is the guest username. ([‘absent’, ‘create_temporary’, ‘move’, ‘present’]) - `password` (str): password ([‘absent’, ‘create_temporary’, ‘move’, ‘present’]) - `saml_token` (str): SAML Bearer Token ([‘absent’, ‘create_temporary’, ‘move’, ‘present’]) |
| **new_path**  string | The complete path to where the directory is moved or its new name. It cannot be a path to an existing directory or an existing file. Required with *state=[‘move’]* |
| **parent_path**  string | The complete path to the directory in which to create the new directory. |
| **path**  string | The complete path to the directory to be created. Required with *state=[‘absent’, ‘move’, ‘present’]* |
| **prefix**  string | The prefix to be given to the new temporary directory. Required with *state=[‘create_temporary’]* |
| **recursive**  boolean | If true, all files and subdirectories are also deleted. If false, the directory must be empty for the operation to succeed.  Choices:   - `false` - `true` |
| **session_timeout**  float  added in vmware.vmware_rest 2.1.0 | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **state**  string | Choices:   - `"absent"` - `"create_temporary"` - `"move"` - `"present"` ← (default) |
| **suffix**  string | The suffix to be given to the new temporary directory. Required with *state=[‘create_temporary’]* |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |
| **vm**  string / required | Virtual Machine to perform the operation on. This parameter is mandatory. |

## [Notes](vcenter_vm_guest_filesystem_directories_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_vm_guest_filesystem_directories_module.md#id5)

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

- name: Create a directory in /tmp
  vmware.vmware_rest.vcenter_vm_guest_filesystem_directories:
    vm: '{{ my_vm.id }}'
    path: /tmp/my/path
    create_parents: true
    credentials:
      interactive_session: false
      type: USERNAME_PASSWORD
      user_name: root
      password: root
```

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
[Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
