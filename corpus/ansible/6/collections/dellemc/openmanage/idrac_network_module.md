---
collection: ansible
version: "6"
title: "dellemc.openmanage.idrac_network module – Configures the iDRAC network attributes"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/idrac_network_module.html
fetched_at: 2026-07-27T17:25:15+00:00
---
# dellemc.openmanage.idrac_network module – Configures the iDRAC network attributes

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
> see [Requirements](idrac_network_module.md#ansible-collections-dellemc-openmanage-idrac-network-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_network`.

New in dellemc.openmanage 2.1.0

- [Synopsis](idrac_network_module.md#synopsis)
- [Requirements](idrac_network_module.md#requirements)
- [Parameters](idrac_network_module.md#parameters)
- [Notes](idrac_network_module.md#notes)
- [Examples](idrac_network_module.md#examples)
- [Return Values](idrac_network_module.md#return-values)

## [Synopsis](idrac_network_module.md#id1)

- This module allows to configure iDRAC network settings.

## [Requirements](idrac_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- omsdk >= 1.2.488
- python >= 3.8.6

## [Parameters](idrac_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auto_config**  string | Allows to enable or disable auto-provisioning to automatically acquire domain name from DHCP.  Choices:   - `"Enabled"` - `"Disabled"` |
| **auto_detect**  string | Allows to auto detect the available NIC types used by iDRAC.  Choices:   - `"Enabled"` - `"Disabled"` |
| **auto_negotiation**  string | Allows iDRAC to automatically set the duplex mode and network speed.  Choices:   - `"Enabled"` - `"Disabled"` |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **dns_from_dhcp**  string | Allows to enable DHCP to obtain DNS server address.  Choices:   - `"Enabled"` - `"Disabled"` |
| **dns_idrac_name**  string | Name of the DNS to register iDRAC. |
| **duplex_mode**  string | Select the type of data transmission for the NIC.  Choices:   - `"Full"` - `"Half"` |
| **enable_dhcp**  string | Allows to enable or disable Dynamic Host Configuration Protocol (DHCP) in iDRAC.  Choices:   - `"Enabled"` - `"Disabled"` |
| **enable_ipv4**  string | Allows to enable or disable IPv4 configuration.  Choices:   - `"Enabled"` - `"Disabled"` |
| **enable_nic**  string | Allows to enable or disable the Network Interface Controller (NIC) used by iDRAC.  Choices:   - `"Enabled"` - `"Disabled"` |
| **failover_network**  string | Select one of the remaining LOMs. If a network fails, the traffic is routed through the failover network.  Choices:   - `"ALL"` - `"LOM1"` - `"LOM2"` - `"LOM3"` - `"LOM4"` - `"T_None"` |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  Default: `443` |
| **idrac_user**  string / required | iDRAC username. |
| **ip_address**  string | Enter a valid iDRAC static IPv4 address. |
| **network_speed**  string | Select the network speed for the selected NIC.  Choices:   - `"T_10"` - `"T_100"` - `"T_1000"` |
| **nic_mtu**  integer | Maximum Transmission Unit of the NIC. |
| **nic_selection**  string | Select one of the available NICs.  Choices:   - `"Dedicated"` - `"LOM1"` - `"LOM2"` - `"LOM3"` - `"LOM4"` |
| **register_idrac_on_dns**  string | Registers iDRAC on a Domain Name System (DNS).  Choices:   - `"Enabled"` - `"Disabled"` |
| **setup_idrac_nic_vlan**  string | Allows to configure VLAN on iDRAC.  Choices:   - `"Enabled"` - `"Disabled"` |
| **share_mnt**  string | Local mount path of the network share with read-write permission for ansible user. This option is mandatory for network shares. |
| **share_name**  string / required | Network share or a local path. |
| **share_password**  aliases: share_pwd  string | Network share user password. This option is mandatory for CIFS share. |
| **share_user**  string | Network share user name. Use the format [‘user@domain](mailto:'user%40domain)’ or ‘domain\\user’ if user is part of a domain. This option is mandatory for CIFS share. |
| **static_dns**  string | Enter the static DNS domain name. |
| **static_dns_1**  string | Enter the preferred static DNS server IPv4 address. |
| **static_dns_2**  string | Enter the preferred static DNS server IPv4 address. |
| **static_gateway**  string | Enter the static IPv4 gateway address to iDRAC. |
| **static_net_mask**  string | Enter the static IP subnet mask to iDRAC. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |
| **vlan_id**  integer | Enter the VLAN ID. The VLAN ID must be a number from 1 through 4094. |
| **vlan_priority**  integer | Enter the priority for the VLAN ID. The priority value must be a number from 0 through 7. |

## [Notes](idrac_network_module.md#id4)

> **Note:**
>
> - This module requires ‘Administrator’ privilege for *idrac_user*.
> - Run this module from a system that has direct access to Dell EMC iDRAC.
> - This module supports `check_mode`.

## [Examples](idrac_network_module.md#id5)

```yaml+jinja
---
- name: Configure iDRAC network settings
  dellemc.openmanage.idrac_network:
       idrac_ip:   "192.168.0.1"
       idrac_user: "user_name"
       idrac_password:  "user_password"
       ca_path: "/path/to/ca_cert.pem"
       share_name: "192.168.0.1:/share"
       share_password:  "share_pwd"
       share_user: "share_user"
       share_mnt: "/mnt/share"
       register_idrac_on_dns: Enabled
       dns_idrac_name: None
       auto_config: None
       static_dns: None
       setup_idrac_nic_vlan: Enabled
       vlan_id: 0
       vlan_priority: 1
       enable_nic: Enabled
       nic_selection: Dedicated
       failover_network: T_None
       auto_detect: Disabled
       auto_negotiation: Enabled
       network_speed: T_1000
       duplex_mode: Full
       nic_mtu: 1500
       ip_address: "192.168.0.1"
       enable_dhcp: Enabled
       enable_ipv4: Enabled
       static_dns_1: "192.168.0.1"
       static_dns_2: "192.168.0.1"
       dns_from_dhcp: Enabled
       static_gateway: None
       static_net_mask: None
```

## [Return Values](idrac_network_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Successfully configured the idrac network settings.  Returned: always  Sample: `"Successfully configured the idrac network settings."` |
| **network_status**  dictionary | Status of the Network settings operation job.  Returned: success  Sample: `{"@odata.context": "/redfish/v1/$metadata#DellJob.DellJob", "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Jobs/JID_856418531008", "@odata.type": "#DellJob.v1_0_2.DellJob", "CompletionTime": "2020-03-31T03:04:15", "Description": "Job Instance", "EndTime": null, "Id": "JID_856418531008", "JobState": "Completed", "JobType": "ImportConfiguration", "Message": "Successfully imported and applied Server Configuration Profile.", "MessageArgs": [], "MessageArgs@odata.count": 0, "MessageId": "SYS053", "Name": "Import Configuration", "PercentComplete": 100, "StartTime": "TIME_NOW", "Status": "Success", "TargetSettingsURI": null, "retval": true}` |

### Authors

- Felix Stephen (@felixs88)
- Anooja Vardhineni (@anooja-vardhineni)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
