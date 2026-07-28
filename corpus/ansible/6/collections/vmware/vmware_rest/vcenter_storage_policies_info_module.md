---
collection: ansible
version: "6"
title: "vmware.vmware_rest.vcenter_storage_policies_info module – Returns information about at most 1024 visible (subject to permission checks) storage solicies availabe in vCenter"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/vcenter_storage_policies_info_module.html
fetched_at: 2026-07-28T00:22:13+00:00
---
# vmware.vmware_rest.vcenter_storage_policies_info module – Returns information about at most 1024 visible (subject to permission checks) storage solicies availabe in vCenter

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
> see [Requirements](vcenter_storage_policies_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-storage-policies-info-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_storage_policies_info`.

New in vmware.vmware_rest 0.3.0

- [Synopsis](vcenter_storage_policies_info_module.md#synopsis)
- [Requirements](vcenter_storage_policies_info_module.md#requirements)
- [Parameters](vcenter_storage_policies_info_module.md#parameters)
- [Notes](vcenter_storage_policies_info_module.md#notes)
- [Examples](vcenter_storage_policies_info_module.md#examples)
- [Return Values](vcenter_storage_policies_info_module.md#return-values)

## [Synopsis](vcenter_storage_policies_info_module.md#id1)

- Returns information about at most 1024 visible (subject to permission checks) storage solicies availabe in vCenter. These storage policies can be used for provisioning virtual machines or disks.

## [Requirements](vcenter_storage_policies_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_storage_policies_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **policies**  list / elements=string | Identifiers of storage policies that can match the filter. |
| **session_timeout**  float  added in vmware.vmware_rest 2.1.0 | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Notes](vcenter_storage_policies_info_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_storage_policies_info_module.md#id5)

```yaml+jinja
- name: List existing storage policies
  vmware.vmware_rest.vcenter_storage_policies_info:
  register: storage_policies
```

## [Return Values](vcenter_storage_policies_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **value**  list / elements=string | List existing storage policies  Returned: On success  Sample: `[{"description": "Management Storage policy used for VMC large cluster", "name": "Management Storage Policy - Large", "policy": "cd8f7c94-3e11-67fc-17f5-4e96d91a5beb"}, {"description": "Allow the datastore to determine the best placement strategy for storage objects", "name": "VVol No Requirements Policy", "policy": "f4e5bade-15a2-4805-bf8e-52318c4ce443"}, {"description": "Management Storage policy used for smaller VMC Stretched Cluster configuration.", "name": "Management Storage Policy - Stretched Lite", "policy": "d109de24-c966-428f-8da2-d281e6671e35"}, {"description": "Sample storage policy for VMware's VM and virtual disk encryption", "name": "VM Encryption Policy", "policy": "4d5f673c-536f-11e6-beb8-9e71128cae77"}, {"description": "Management Storage policy used for encrypting VM", "name": "Management Storage policy - Encryption", "policy": "b1263970-8662-69e2-adc6-fa8ae01abecc"}, {"description": "Management Storage policy used for VMC single node cluster", "name": "Management Storage Policy - Single Node", "policy": "a9423670-7455-11e8-adc0-fa7ae01bbebc"}, {"description": "Storage policy used as default for Host-local PMem datastores", "name": "Host-local PMem Default Storage Policy", "policy": "c268da1b-b343-49f7-a468-b1deeb7078e0"}, {"description": "Storage policy used as default for vSAN datastores", "name": "vSAN Default Storage Policy", "policy": "aa6d5a82-1c88-45da-85d3-3d74b91a5bad"}, {"description": "Management Storage policy used for VMC regular cluster", "name": "Management Storage Policy - Regular", "policy": "bb7e6b13-2d99-46eb-96e4-3d85c91a5bde"}, {"description": "Management Storage policy used for VMC regular cluster which requires THIN provisioning", "name": "Management Storage policy - Thin", "policy": "b6423670-8552-66e8-adc1-fa6ae01abeac"}, {"description": "Management Storage policy used for VMC stretched cluster", "name": "Management Storage Policy - Stretched", "policy": "f31f2442-8247-4517-87c2-8d69d7a6c696"}]` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
[Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
