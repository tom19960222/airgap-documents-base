---
collection: ansible
version: "6"
title: "vmware.vmware_rest.vcenter_ovf_libraryitem module – Creates a library item in content library from a virtual machine or virtual appliance"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/vcenter_ovf_libraryitem_module.html
fetched_at: 2026-07-28T00:22:11+00:00
---
# vmware.vmware_rest.vcenter_ovf_libraryitem module – Creates a library item in content library from a virtual machine or virtual appliance

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
> see [Requirements](vcenter_ovf_libraryitem_module.md#ansible-collections-vmware-vmware-rest-vcenter-ovf-libraryitem-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_ovf_libraryitem`.

New in vmware.vmware_rest 2.0.0

- [Synopsis](vcenter_ovf_libraryitem_module.md#synopsis)
- [Requirements](vcenter_ovf_libraryitem_module.md#requirements)
- [Parameters](vcenter_ovf_libraryitem_module.md#parameters)
- [Notes](vcenter_ovf_libraryitem_module.md#notes)
- [Examples](vcenter_ovf_libraryitem_module.md#examples)
- [Return Values](vcenter_ovf_libraryitem_module.md#return-values)

## [Synopsis](vcenter_ovf_libraryitem_module.md#id1)

- Creates a library item in content library from a virtual machine or virtual appliance. <p> This [{@term](mailto:{%40term) operation} creates a library item in content library whose content is an OVF package derived from a source virtual machine or virtual appliance, using the supplied create specification. The OVF package may be stored as in a newly created library item or in an in an existing library item. For an existing library item whose content is updated by this [{@term](mailto:{%40term) operation}, the original content is overwritten. Meta data such as name and description is not updated for the exisitng library item. </p>

## [Requirements](vcenter_ovf_libraryitem_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_ovf_libraryitem_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **client_token**  string | Client-generated token used to retry a request if the client fails to get a response from the server. If the original request succeeded, the result of that request will be returned, otherwise the operation will be retried. |
| **create_spec**  dictionary | Information used to create the OVF package from the source virtual machine or virtual appliance. Required with *state=[‘present’]*  Valid attributes are:  - `name` (str): Name to use in the OVF descriptor stored in the library item. ([‘present’]) - `description` (str): Description to use in the OVF descriptor stored in the library item. ([‘present’]) - `flags` (list): Flags to use for OVF package creation. The supported flags can be obtained using [{@link](mailto:{%40link) ExportFlag#list}. ([‘present’]) |
| **deployment_spec**  dictionary | Specification of how the OVF package should be deployed to the target. Required with *state=[‘deploy’]*  Valid attributes are:  - `name` (str): Name assigned to the deployed target virtual machine or virtual appliance. ([‘deploy’]) - `annotation` (str): Annotation assigned to the deployed target virtual machine or virtual appliance. ([‘deploy’]) - `accept_all_EULA` (bool): Whether to accept all End User License Agreements. ([‘deploy’])  This key is required with [‘deploy’]. - `network_mappings` (dict): Specification of the target network to use for sections of type ovf:NetworkSection in the OVF descriptor. The key in the {@term map} is the section identifier of the ovf:NetworkSection section in the OVF descriptor and the value is the target network to be used for deployment. ([‘deploy’]) - `storage_mappings` (dict): Specification of the target storage to use for sections of type vmw:StorageGroupSection in the OVF descriptor. The key in the {@term map} is the section identifier of the ovf:StorageGroupSection section in the OVF descriptor and the value is the target storage specification to be used for deployment. ([‘deploy’]) - `storage_provisioning` (str): The `disk_provisioning_type` defines the virtual disk provisioning types that can be set for a disk on the target platform. ([‘deploy’])    - Accepted values:      - eagerZeroedThick     - thick     - thin - `storage_profile_id` (str): Default storage profile to use for all sections of type vmw:StorageSection in the OVF descriptor. ([‘deploy’]) - `locale` (str): The locale to use for parsing the OVF descriptor. ([‘deploy’]) - `flags` (list): Flags to be use for deployment. The supported flag values can be obtained using [{@link](mailto:{%40link) ImportFlag#list}. ([‘deploy’]) - `additional_parameters` (list): Additional OVF parameters that may be needed for the deployment. Additional OVF parameters may be required by the OVF descriptor of the OVF package in the library item. Examples of OVF parameters that can be specified through this field include, but are not limited to: <ul> <li>{@link DeploymentOptionParams}</li> <li>{@link ExtraConfigParams}</li> <li>{@link IpAllocationParams}</li> <li>{@link PropertyParams}</li> <li>{@link ScaleOutParams}</li> <li>{@link VcenterExtensionParams}</li> </ul> ([‘deploy’]) - `default_datastore_id` (str): Default datastore to use for all sections of type vmw:StorageSection in the OVF descriptor. ([‘deploy’]) |
| **ovf_library_item_id**  string | Identifier of the content library item containing the OVF package to be deployed. Required with *state=[‘deploy’, ‘filter’]* |
| **session_timeout**  float  added in vmware.vmware_rest 2.1.0 | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **source**  dictionary | Identifier of the virtual machine or virtual appliance to use as the source. Required with *state=[‘present’]*  Valid attributes are:  - `type` (str): Type of the deployable resource. ([‘present’])  This key is required with [‘present’]. - `id` (str): Identifier of the deployable resource. ([‘present’])  This key is required with [‘present’]. |
| **state**  string | Choices:   - `"deploy"` - `"filter"` - `"present"` ← (default) |
| **target**  dictionary / required | Specification of the target content library and library item. This parameter is mandatory.  Valid attributes are:  - `library_id` (str): Identifier of the library in which a new library item should be created. This field is not used if the `#library_item_id` field is specified. ([‘present’]) - `library_item_id` (str): Identifier of the library item that should be should be updated. ([‘present’]) - `resource_pool_id` (str): Identifier of the resource pool to which the virtual machine or virtual appliance should be attached. ([‘deploy’, ‘filter’])  This key is required with [‘deploy’, ‘filter’]. - `host_id` (str): Identifier of the target host on which the virtual machine or virtual appliance will run. The target host must be a member of the cluster that contains the resource pool identified by [{@link](mailto:{%40link) #resourcePoolId}. ([‘deploy’, ‘filter’]) - `folder_id` (str): Identifier of the vCenter folder that should contain the virtual machine or virtual appliance. The folder must be virtual machine folder. ([‘deploy’, ‘filter’]) |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Notes](vcenter_ovf_libraryitem_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_ovf_libraryitem_module.md#id5)

```yaml+jinja
- name: Create a VM
  vmware.vmware_rest.vcenter_vm:
    placement:
      cluster: "{{ lookup('vmware.vmware_rest.cluster_moid', '/my_dc/host/my_cluster')\
        \ }}"
      datastore: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/rw_datastore')\
        \ }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources')\
        \ }}"
    name: test_vm1
    guest_OS: DEBIAN_8_64
    hardware_version: VMX_11
    memory:
      hot_add_enabled: true
      size_MiB: 1024
  register: my_vm

- name: Create a content library pointing on a NFS share
  vmware.vmware_rest.content_locallibrary:
    name: my_library_on_nfs
    description: automated
    publish_info:
      published: true
      authentication_method: NONE
    storage_backings:
    - storage_uri: nfs://datastore.test/srv/share/content-library
      type: OTHER
    state: present
  register: nfs_lib

- name: Export the VM as an OVF on the library
  vmware.vmware_rest.vcenter_ovf_libraryitem:
    session_timeout: 2900
    source:
      type: VirtualMachine
      id: '{{ my_vm.id }}'
    target:
      library_id: '{{ nfs_lib.id }}'
    create_spec:
      name: my_vm
      description: an OVF example
      flags: []
    state: present
  register: ovf_item

- name: Create a new VM from the OVF
  vmware.vmware_rest.vcenter_ovf_libraryitem:
    session_timeout: 2900
    ovf_library_item_id: '{{ (lib_items.value|selectattr("name", "equalto", "my_vm")|first).id
      }}'
    state: deploy
    target:
      resource_pool_id: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources')\
        \ }}"
    deployment_spec:
      name: my_vm_from_ovf
      accept_all_EULA: true
      storage_provisioning: thin

- name: Create a new VM from the OVF and specify the host and folder
  vmware.vmware_rest.vcenter_ovf_libraryitem:
    session_timeout: 2900
    ovf_library_item_id: '{{ (lib_items.value|selectattr("name", "equalto", "my_vm")|first).id
      }}'
    state: deploy
    target:
      resource_pool_id: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources')\
        \ }}"
      folder_id: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      host_id: "{{ lookup('vmware.vmware_rest.host_moid', '/my_dc/host/my_cluster/esxi1.test/test_vm1')\
        \ }}"
    deployment_spec:
      name: my_vm_from_ovf_on_a_host
      accept_all_EULA: true
      storage_provisioning: thin
```

## [Return Values](vcenter_ovf_libraryitem_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **value**  dictionary | Create a new VM from the OVF and specify the host and folder  Returned: On success  Sample: `{"error": {"errors": [], "information": [], "warnings": []}, "resource_id": {"id": "vm-1211", "type": "VirtualMachine"}, "succeeded": 1}` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
[Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
