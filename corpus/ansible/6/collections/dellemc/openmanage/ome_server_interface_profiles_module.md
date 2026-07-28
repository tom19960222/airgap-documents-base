---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_server_interface_profiles module – Configure server interface profiles"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_server_interface_profiles_module.html
fetched_at: 2026-07-27T17:25:48+00:00
---
# dellemc.openmanage.ome_server_interface_profiles module – Configure server interface profiles

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/dellemc/openmanage) (version 5.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](ome_server_interface_profiles_module.md#ansible-collections-dellemc-openmanage-ome-server-interface-profiles-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_server_interface_profiles`.

New in dellemc.openmanage 5.1.0

- [Synopsis](ome_server_interface_profiles_module.md#synopsis)
- [Requirements](ome_server_interface_profiles_module.md#requirements)
- [Parameters](ome_server_interface_profiles_module.md#parameters)
- [Notes](ome_server_interface_profiles_module.md#notes)
- [Examples](ome_server_interface_profiles_module.md#examples)
- [Return Values](ome_server_interface_profiles_module.md#return-values)

## [Synopsis](ome_server_interface_profiles_module.md#id1)

- This module allows to configure server interface profiles on OpenManage Enterprise Modular.

## [Requirements](ome_server_interface_profiles_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_server_interface_profiles_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **device_id**  list / elements=integer | Device id of the Server under chassis fabric.  *device_id* and *device_service_tag* is mutually exclusive. |
| **device_service_tag**  list / elements=string | Service tag of the Server under chassis fabric.  *device_service_tag* and *device_id* is mutually exclusive. |
| **hostname**  string / required | OpenManage Enterprise Modular IP address or hostname. |
| **job_wait**  boolean | Provides the option to wait for job completion.  Choices:   - `false` - `true` ← (default) |
| **job_wait_timeout**  integer | The maximum wait time of *job_wait* in seconds. The job is tracked only for this duration.  This option is applicable when *job_wait* is `True`.  Default: `120` |
| **nic_configuration**  list / elements=dictionary | NIC configuration for the Servers to be applied. |
| **nic_identifier**  string / required | ID of the NIC or port number.  `Note` This will not be validated. |
| **tagged_networks**  dictionary | List of tagged networks  Network cannot be added as a tagged network if it is already assigned to untagged network |
| **names**  list / elements=string / required | List of network name to be marked as tagged networks  The *names* can be retrieved using the [dellemc.openmanage.ome_network_vlan_info](ome_network_vlan_info_module.md#ansible-collections-dellemc-openmanage-ome-network-vlan-info-module) |
| **state**  string | Indicates if a list of networks needs to be added or deleted.  `present` to add the network to the tagged list  `absent` to delete the Network from the tagged list  Choices:   - `"present"` ← (default) - `"absent"` |
| **team**  boolean | Group two or more ports. The ports must be connected to the same pair of Ethernet switches.  *team* is applicable only if *nic_teaming* is `LACP`.  Choices:   - `false` - `true` |
| **untagged_network**  integer | The maximum or minimum VLAN id of the network to be untagged.  The *untagged_network* can be retrieved using the [dellemc.openmanage.ome_network_vlan_info](ome_network_vlan_info_module.md#ansible-collections-dellemc-openmanage-ome-network-vlan-info-module)  If *untagged_network* needs to be unset this needs to be sent as `0`  `Note` The network cannot be added as a untagged network if it is already assigned to a tagged network. |
| **nic_teaming**  string | NIC teaming options.  `NoTeaming` the NICs are not bonded and provide no load balancing or redundancy.  `LACP` use LACP for NIC teaming.  `Other` use other technology for NIC teaming.  Choices:   - `"LACP"` - `"NoTeaming"` - `"Other"` |
| **password**  string / required | OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_server_interface_profiles_module.md#id4)

> **Note:**
>
> - This module supports `check_mode`.
> - Run this module from a system that has direct access to Dell EMC OpenManage Enterprise Modular.

## [Examples](ome_server_interface_profiles_module.md#id5)

```yaml+jinja
---
- name: Modify Server Interface Profile for the server using the service tag
  dellemc.openmanage.ome_server_interface_profiles:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_service_tag:
      - SVCTAG1
      - SVCTAG2
    nic_teaming: LACP
    nic_configuration:
      - nic_identifier: NIC.Mezzanine.1A-1-1
        team: no
        untagged_network: 2
        tagged_networks:
          names:
            - vlan1
      - nic_identifier: NIC.Mezzanine.1A-2-1
        team: yes
        untagged_network: 3
        tagged_networks:
          names:
            - range120-125

- name: Modify Server Interface Profile for the server using the device id
  dellemc.openmanage.ome_server_interface_profiles:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_id:
      - 34523
      - 48999
    nic_teaming: NoTeaming
    nic_configuration:
      - nic_identifier: NIC.Mezzanine.1A-1-1
        team: no
        untagged_network: 2
        tagged_networks:
          names:
            - vlan2
      - nic_identifier: NIC.Mezzanine.1A-2-1
        team: yes
        untagged_network: 3
        tagged_networks:
          names:
            - range120-125
```

## [Return Values](ome_server_interface_profiles_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **job_id**  integer | Job ID of the task to apply the server interface profiles.  Returned: on applying the Interface profiles  Sample: `14123` |
| **msg**  string | Status of the overall server interface operation.  Returned: always  Sample: `"Successfully triggered apply server profiles job."` |

### Authors

- Jagadeesh N V (@jagadeeshnv)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
