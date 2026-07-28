---
collection: ansible
version: "8"
title: "vmware.vmware_rest.appliance_vmon_service module – Lists details of services managed by vMon."
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/appliance_vmon_service_module.html
fetched_at: 2026-07-28T02:57:40+00:00
---
# vmware.vmware_rest.appliance_vmon_service module – Lists details of services managed by vMon.

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
> see [Requirements](appliance_vmon_service_module.md#ansible-collections-vmware-vmware-rest-appliance-vmon-service-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.appliance_vmon_service`.

New in vmware.vmware_rest 2.0.0

- [Synopsis](appliance_vmon_service_module.md#synopsis)
- [Requirements](appliance_vmon_service_module.md#requirements)
- [Parameters](appliance_vmon_service_module.md#parameters)
- [Notes](appliance_vmon_service_module.md#notes)
- [Examples](appliance_vmon_service_module.md#examples)
- [Return Values](appliance_vmon_service_module.md#return-values)

## [Synopsis](appliance_vmon_service_module.md#id1)

- Lists details of services managed by vMon.

## [Requirements](appliance_vmon_service_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](appliance_vmon_service_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **service**  string | identifier of the service whose properties are being updated.  The parameter must be the id of a resource returned by [vmware.vmware_rest.appliance_vmon_service](appliance_vmon_service_module.md#ansible-collections-vmware-vmware-rest-appliance-vmon-service-module). Required with *state=[‘restart’, ‘start’, ‘stop’]* |
| **session_timeout**  float  *added in vmware.vmware_rest 2.1.0* | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **startup_type**  string | The *startup_type* enumerated type defines valid Startup Type for services managed by vMon.  **Choices:**   - `"AUTOMATIC"` - `"DISABLED"` - `"MANUAL"` |
| **state**  string | **Choices:**   - `"list_details"` - `"present"` ← (default) - `"restart"` - `"start"` - `"stop"` |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](appliance_vmon_service_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](appliance_vmon_service_module.md#id5)

```yaml+jinja
- name: Adjust vpxd configuration
  vmware.vmware_rest.appliance_vmon_service:
    service: vpxd
    startup_type: AUTOMATIC
  register: result
```

## [Return Values](appliance_vmon_service_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | moid of the resource  **Returned:** On success  **Sample:** `"vpxd"` |
| **value**  dictionary | Adjust vpxd configuration  **Returned:** On success  **Sample:** `{}` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
- [Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
