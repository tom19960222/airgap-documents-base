---
collection: ansible
version: "6"
title: "vmware.vmware_rest.vcenter_vmtemplate_libraryitems_info module – Returns information about a virtual machine template contained in the library item specified by { @ param . name templateLibraryItem}"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/vcenter_vmtemplate_libraryitems_info_module.html
fetched_at: 2026-07-28T00:22:50+00:00
---
# vmware.vmware_rest.vcenter_vmtemplate_libraryitems_info module – Returns information about a virtual machine template contained in the library item specified by [{@param.name](mailto:{%40param.name) templateLibraryItem}

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
> see [Requirements](vcenter_vmtemplate_libraryitems_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vmtemplate-libraryitems-info-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_vmtemplate_libraryitems_info`.

New in vmware.vmware_rest 2.2.0

- [Synopsis](vcenter_vmtemplate_libraryitems_info_module.md#synopsis)
- [Requirements](vcenter_vmtemplate_libraryitems_info_module.md#requirements)
- [Parameters](vcenter_vmtemplate_libraryitems_info_module.md#parameters)
- [Notes](vcenter_vmtemplate_libraryitems_info_module.md#notes)
- [Examples](vcenter_vmtemplate_libraryitems_info_module.md#examples)

## [Synopsis](vcenter_vmtemplate_libraryitems_info_module.md#id1)

- Returns information about a virtual machine template contained in the library item specified by [{@param.name](mailto:{%40param.name) templateLibraryItem}

## [Requirements](vcenter_vmtemplate_libraryitems_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_vmtemplate_libraryitems_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **session_timeout**  float  added in vmware.vmware_rest 2.1.0 | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **template_library_item**  string | identifier of the library item containing the virtual machine template. Required with *state=[‘get’]* |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Notes](vcenter_vmtemplate_libraryitems_info_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_vmtemplate_libraryitems_info_module.md#id5)

```yaml+jinja

```

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
[Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
