---
collection: ansible
version: "8"
title: "dellemc.powerflex.sdc module – Manage SDCs on Dell PowerFlex"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/powerflex/sdc_module.html
fetched_at: 2026-07-28T02:05:13+00:00
---
# dellemc.powerflex.sdc module – Manage SDCs on Dell PowerFlex

> **Note:**
>
> This module is part of the [dellemc.powerflex collection](https://galaxy.ansible.com/ui/repo/published/dellemc/powerflex/) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.powerflex`.
> You need further requirements to be able to use this module,
> see [Requirements](sdc_module.md#ansible-collections-dellemc-powerflex-sdc-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.powerflex.sdc`.

New in dellemc.powerflex 1.0.0

- [Synopsis](sdc_module.md#synopsis)
- [Requirements](sdc_module.md#requirements)
- [Parameters](sdc_module.md#parameters)
- [Notes](sdc_module.md#notes)
- [Examples](sdc_module.md#examples)
- [Return Values](sdc_module.md#return-values)

## [Synopsis](sdc_module.md#id1)

- Managing SDCs on PowerFlex storage system includes getting details of SDC and renaming SDC.

Aliases: dellemc_powerflex_sdc

## [Requirements](sdc_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.5 or later.
- Ansible-core 2.13 or later.
- PyPowerFlex 1.8.0.
- Python 3.9, 3.10 or 3.11.

## [Parameters](sdc_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  aliases: gateway_host  string / required | IP or FQDN of the PowerFlex host. |
| **password**  string / required | The password of the PowerFlex host. |
| **performance_profile**  string | Define the performance profile as *Compact* or *HighPerformance*.  The high performance profile configures a predefined set of parameters for very high performance use cases.  **Choices:**   - `"Compact"` - `"HighPerformance"` |
| **port**  integer | Port number through which communication happens with PowerFlex host.  **Default:** `443` |
| **sdc_id**  string | ID of the SDC.  Specify either *sdc_name*, *sdc_id* or *sdc_ip* for get/rename operation.  Mutually exclusive with *sdc_name* and *sdc_ip*. |
| **sdc_ip**  string | IP of the SDC.  Specify either *sdc_name*, *sdc_id* or *sdc_ip* for get/rename operation.  Mutually exclusive with *sdc_id* and *sdc_name*. |
| **sdc_name**  string | Name of the SDC.  Specify either *sdc_name*, *sdc_id* or *sdc_ip* for get/rename operation.  Mutually exclusive with *sdc_id* and *sdc_ip*. |
| **sdc_new_name**  string | New name of the SDC. Used to rename the SDC. |
| **state**  string / required | State of the SDC.  **Choices:**   - `"present"` - `"absent"` |
| **timeout**  integer | Time after which connection will get terminated.  It is to be mentioned in seconds.  **Default:** `120` |
| **username**  string / required | The username of the PowerFlex host. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](sdc_module.md#id4)

> **Note:**
>
> - The *check_mode* is not supported.
> - The modules present in the collection named as ‘dellemc.powerflex’ are built to support the Dell PowerFlex storage platform.

## [Examples](sdc_module.md#id5)

```yaml+jinja
- name: Get SDC details using SDC ip
  dellemc.powerflex.sdc:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    sdc_ip: "{{sdc_ip}}"
    state: "present"

- name: Rename SDC using SDC name
  dellemc.powerflex.sdc:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    sdc_name: "centos_sdc"
    sdc_new_name: "centos_sdc_renamed"
    state: "present"

- name: Modify performance profile of SDC using SDC name
  dellemc.powerflex.sdc:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    sdc_name: "centos_sdc"
    performance_profile: "Compact"
    state: "present"

- name: Remove SDC using SDC name
  dellemc.powerflex.sdc:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    sdc_name: "centos_sdc"
    state: "absent"
```

## [Return Values](sdc_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `false` |
| **sdc_details**  dictionary | Details of the SDC.  **Returned:** When SDC exists  **Sample:** `{"id": "07335d3d00000006", "installedSoftwareVersionInfo": "R3_6.0.0", "kernelBuildNumber": null, "kernelVersion": "3.10.0", "links": [{"href": "/api/instances/Sdc::07335d3d00000006", "rel": "self"}, {"href": "/api/instances/Sdc::07335d3d00000006/relationships/ Statistics", "rel": "/api/Sdc/relationship/Statistics"}, {"href": "/api/instances/Sdc::07335d3d00000006/relationships/ Volume", "rel": "/api/Sdc/relationship/Volume"}, {"href": "/api/instances/System::4a54a8ba6df0690f", "rel": "/api/parent/relationship/systemId"}], "mapped_volumes": [], "mdmConnectionState": "Disconnected", "memoryAllocationFailure": null, "name": "LGLAP203", "osType": "Linux", "peerMdmId": null, "perfProfile": "HighPerformance", "sdcApproved": true, "sdcApprovedIps": null, "sdcGuid": "F8ECB844-23B8-4629-92BB-B6E49A1744CB", "sdcIp": "N/A", "sdcIps": null, "sdcType": "AppSdc", "sdrId": null, "socketAllocationFailure": null, "softwareVersionInfo": "R3_6.0.0", "systemId": "4a54a8ba6df0690f", "versionInfo": "R3_6.0.0"}` |
| **id**  string | The ID of the SDC.  **Returned:** success |
| **mapped_volumes**  list / elements=string | The details of the mapped volumes.  **Returned:** success |
| **id**  string | The ID of the volume.  **Returned:** success |
| **name**  string | The name of the volume.  **Returned:** success |
| **volumeType**  string | Type of the volume.  **Returned:** success |
| **name**  string | Name of the SDC.  **Returned:** success |
| **osType**  string | OS type of the SDC.  **Returned:** success |
| **sdcApproved**  boolean | Indicates whether an SDC has approved access to the system.  **Returned:** success |
| **sdcIp**  string | IP of the SDC.  **Returned:** success |

### Authors

- Akash Shendge (@shenda1)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-powerflex/tree/1.9.0)
