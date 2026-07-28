---
collection: ansible
version: "6"
title: "vmware.vmware_rest.vcenter_vmtemplate_libraryitems module – Creates a library item in content library from a virtual machine"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/vcenter_vmtemplate_libraryitems_module.html
fetched_at: 2026-07-28T00:22:49+00:00
---
# vmware.vmware_rest.vcenter_vmtemplate_libraryitems module – Creates a library item in content library from a virtual machine

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
> see [Requirements](vcenter_vmtemplate_libraryitems_module.md#ansible-collections-vmware-vmware-rest-vcenter-vmtemplate-libraryitems-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_vmtemplate_libraryitems`.

New in vmware.vmware_rest 2.2.0

- [Synopsis](vcenter_vmtemplate_libraryitems_module.md#synopsis)
- [Requirements](vcenter_vmtemplate_libraryitems_module.md#requirements)
- [Parameters](vcenter_vmtemplate_libraryitems_module.md#parameters)
- [Notes](vcenter_vmtemplate_libraryitems_module.md#notes)
- [Examples](vcenter_vmtemplate_libraryitems_module.md#examples)
- [Return Values](vcenter_vmtemplate_libraryitems_module.md#return-values)

## [Synopsis](vcenter_vmtemplate_libraryitems_module.md#id1)

- Creates a library item in content library from a virtual machine. This [{@term](mailto:{%40term) operation} creates a library item in content library whose content is a virtual machine template created from the source virtual machine, using the supplied create specification. The virtual machine template is stored in a newly created library item.

## [Requirements](vcenter_vmtemplate_libraryitems_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_vmtemplate_libraryitems_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of the deployed virtual machine. |
| **disk_storage**  dictionary | Storage specification for the virtual machine template’s disks.  Valid attributes are:  - `datastore` (str): Identifier for the datastore associated the deployed virtual machine’s disk. ([‘deploy’, ‘present’]) - `storage_policy` (dict): Storage policy for the deployed virtual machine’s disk. ([‘deploy’, ‘present’])    - Accepted keys:      - type (string): Policy type for a virtual machine template’s disk.  Accepted value for this field:  - `USE_SPECIFIED_POLICY`   - policy (string): Identifier for the storage policy to use. |
| **disk_storage_overrides**  dictionary | Storage specification for individual disks in the deployed virtual machine. This is specified as a mapping between disk identifiers in the source virtual machine template contained in the library item and their storage specifications. |
| **guest_customization**  dictionary | Guest customization spec to apply to the deployed virtual machine.  Valid attributes are:  - `name` (str): Name of the customization specification. ([‘deploy’]) |
| **hardware_customization**  dictionary | Hardware customization spec which specifies updates to the deployed virtual machine.  Valid attributes are:  - `nics` (dict): Map of Ethernet network adapters to update. ([‘deploy’]) - `disks_to_remove` (list): Idenfiers of disks to remove from the deployed virtual machine. ([‘deploy’]) - `disks_to_update` (dict): Disk update specification for individual disks in the deployed virtual machine. ([‘deploy’]) - `cpu_update` (dict): CPU update specification for the deployed virtual machine. ([‘deploy’])    - Accepted keys:      - num_cpus (integer): Number of virtual processors in the deployed virtual machine.     - num_cores_per_socket (integer): Number of cores among which to distribute CPUs in the deployed virtual machine. - `memory_update` (dict): Memory update specification for the deployed virtual machine. ([‘deploy’])    - Accepted keys:      - memory (integer): Size of a virtual machine’s memory in MB. |
| **library**  string | Identifier of the library in which the new library item should be created. Required with *state=[‘present’]* |
| **name**  string / required | Name of the deployed virtual machine. This parameter is mandatory. |
| **placement**  dictionary | Information used to place the virtual machine template.  Valid attributes are:  - `folder` (str): Virtual machine folder into which the deployed virtual machine should be placed. ([‘deploy’, ‘present’]) - `resource_pool` (str): Resource pool into which the deployed virtual machine should be placed. ([‘deploy’, ‘present’]) - `host` (str): Host onto which the virtual machine should be placed. If `#host` and `#resource_pool` are both specified, `#resource_pool` must belong to `#host`. If `#host` and `#cluster` are both specified, `#host` must be a member of `#cluster`. ([‘deploy’, ‘present’]) - `cluster` (str): Cluster onto which the deployed virtual machine should be placed. If `#cluster` and `#resource_pool` are both specified, `#resource_pool` must belong to `#cluster`. If `#cluster` and `#host` are both specified, `#host` must be a member of `#cluster`. ([‘deploy’, ‘present’]) |
| **powered_on**  boolean | Specifies whether the deployed virtual machine should be powered on after deployment.  Choices:   - `false` - `true` |
| **session_timeout**  float  added in vmware.vmware_rest 2.1.0 | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **source_vm**  string | Identifier of the source virtual machine to create the library item from. Required with *state=[‘present’]* |
| **state**  string | Choices:   - `"deploy"` - `"present"` ← (default) |
| **template_library_item**  string | identifier of the content library item containing the source virtual machine template to be deployed. Required with *state=[‘deploy’]* |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |
| **vm_home_storage**  dictionary | Storage location for the virtual machine template’s configuration and log files.  Valid attributes are:  - `datastore` (str): Identifier of the datastore for the deployed virtual machine’s configuration and log files. ([‘deploy’, ‘present’]) - `storage_policy` (dict): Storage policy for the deployed virtual machine’s configuration and log files. ([‘deploy’, ‘present’])    - Accepted keys:      - type (string): Policy type for the virtual machine template’s configuration and log files.  Accepted value for this field:  - `USE_SPECIFIED_POLICY`   - policy (string): Identifier for the storage policy to use. |

## [Notes](vcenter_vmtemplate_libraryitems_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_vmtemplate_libraryitems_module.md#id5)

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

- name: Create a content library based on a DataStore
  vmware.vmware_rest.content_locallibrary:
    name: my_library_on_datastore
    description: automated
    publish_info:
      published: true
      authentication_method: NONE
    storage_backings:
    - datastore_id: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/local')\
        \ }}"
      type: DATASTORE
    state: present
  register: ds_lib

- name: Create a VM template on the library
  vmware.vmware_rest.vcenter_vmtemplate_libraryitems:
    name: foobar2001
    library: '{{ ds_lib.id }}'
    source_vm: '{{ my_vm.id }}'
    placement:
      cluster: "{{ lookup('vmware.vmware_rest.cluster_moid', '/my_dc/host/my_cluster')\
        \ }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources')\
        \ }}"
  register: mylib_item

- name: Deploy a new VM based on the template
  vmware.vmware_rest.vcenter_vmtemplate_libraryitems:
    name: foobar2002
    library: '{{ ds_lib.id }}'
    template_library_item: '{{ mylib_item.id }}'
    placement:
      cluster: "{{ lookup('vmware.vmware_rest.cluster_moid', '/my_dc/host/my_cluster')\
        \ }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources')\
        \ }}"
    state: deploy
  register: my_new_vm
```

## [Return Values](vcenter_vmtemplate_libraryitems_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | moid of the resource  Returned: On success  Sample: `"551beca2-0592-433a-86f2-b2581bfb3b60"` |
| **value**  dictionary | Create a VM template on the library  Returned: On success  Sample: `{"cpu": {"cores_per_socket": 1, "count": 1}, "disks": {"16000": {"capacity": 16106127360, "disk_storage": {"datastore": "datastore-1256"}}, "16001": {"capacity": 32000000000, "disk_storage": {"datastore": "datastore-1256"}}}, "guest_OS": "RHEL_7_64", "memory": {"size_MiB": 1024}, "nics": {"4000": {"backing_type": "STANDARD_PORTGROUP", "mac_type": "ASSIGNED", "network": "network-1257"}}, "vm_home_storage": {"datastore": "datastore-1256"}, "vm_template": "vm-1265"}` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
[Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
