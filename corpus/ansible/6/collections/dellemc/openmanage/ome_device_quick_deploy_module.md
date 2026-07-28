---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_device_quick_deploy module – Configure Quick Deploy settings on OpenManage Enterprise Modular."
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_device_quick_deploy_module.html
fetched_at: 2026-07-27T17:25:36+00:00
---
# dellemc.openmanage.ome_device_quick_deploy module – Configure Quick Deploy settings on OpenManage Enterprise Modular.

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
> see [Requirements](ome_device_quick_deploy_module.md#ansible-collections-dellemc-openmanage-ome-device-quick-deploy-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_device_quick_deploy`.

New in dellemc.openmanage 5.0.0

- [Synopsis](ome_device_quick_deploy_module.md#synopsis)
- [Requirements](ome_device_quick_deploy_module.md#requirements)
- [Parameters](ome_device_quick_deploy_module.md#parameters)
- [Notes](ome_device_quick_deploy_module.md#notes)
- [Examples](ome_device_quick_deploy_module.md#examples)
- [Return Values](ome_device_quick_deploy_module.md#return-values)

## [Synopsis](ome_device_quick_deploy_module.md#id1)

- This module allows to configure the Quick Deploy settings of the server or IOM on OpenManage Enterprise Modular.

## [Requirements](ome_device_quick_deploy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_device_quick_deploy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **device_id**  integer | The ID of the chassis for which the Quick Deploy settings to be deployed.  If the device ID is not specified, this module updates the Quick Deploy settings for the *hostname*.  *device_id* is mutually exclusive with *device_service_tag*. |
| **device_service_tag**  string | The service tag of the chassis for which the Quick Deploy settings to be deployed.  If the device service tag is not specified, this module updates the Quick Deploy settings for the *hostname*.  *device_service_tag* is mutually exclusive with *device_id*. |
| **hostname**  string / required | OpenManage Enterprise Modular IP address or hostname. |
| **job_wait**  boolean | Determines whether to wait for the job completion or not.  Choices:   - `false` - `true` ← (default) |
| **job_wait_timeout**  integer | The maximum wait time of *job_wait* in seconds. The job is tracked only for this duration.  This option is applicable when *job_wait* is `True`.  Default: `120` |
| **password**  string / required | OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **quick_deploy_options**  dictionary / required | The Quick Deploy settings for server and IOM quick deploy. |
| **ipv4_enabled**  boolean | Enables or disables the IPv4 network.  Choices:   - `false` - `true` |
| **ipv4_gateway**  string | IPv4 gateway.  *ipv4_gateway* is required if *ipv4_network_type* is `Static`. |
| **ipv4_network_type**  string | IPv4 network type.  *ipv4_network_type* is required if *ipv4_enabled* is `True`.  `Static` to configure the static IP settings.  `DHCP` to configure the Dynamic IP settings.  Choices:   - `"Static"` - `"DHCP"` |
| **ipv4_subnet_mask**  string | IPv4 subnet mask.  *ipv4_subnet_mask* is required if *ipv4_network_type* is `Static`. |
| **ipv6_enabled**  boolean | Enables or disables the IPv6 network.  Choices:   - `false` - `true` |
| **ipv6_gateway**  string | IPv6 gateway.  *ipv6_gateway* is required if *ipv6_network_type* is `Static`. |
| **ipv6_network_type**  string | IPv6 network type.  *ipv6_network_type* is required if *ipv6_enabled* is `True`.  `Static` to configure the static IP settings.  `DHCP` to configure the Dynamic IP settings.  Choices:   - `"Static"` - `"DHCP"` |
| **ipv6_prefix_length**  integer | IPV6 prefix length.  *ipv6_prefix_length* is required if *ipv6_network_type* is `Static`. |
| **password**  string | The password to login to the server or IOM.  The module will always report change when *password* option is added. |
| **slots**  list / elements=dictionary | The slot configuration for the server or IOM. |
| **slot_id**  integer / required | The ID of the slot. |
| **slot_ipv4_address**  string | The IPv4 address of the slot. |
| **slot_ipv6_address**  string | The IPv6 address of the slot. |
| **vlan_id**  integer | The ID of the VLAN. |
| **setting_type**  string / required | The type of the Quick Deploy settings to be applied.  `ServerQuickDeploy` to apply the server Quick Deploy settings.  `IOMQuickDeploy` to apply the IOM Quick Deploy settings.  Choices:   - `"ServerQuickDeploy"` - `"IOMQuickDeploy"` |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_device_quick_deploy_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to OpenManage Enterprise Modular.
> - This module supports `check_mode`.
> - The module will always report change when *password* option is added.
> - If the chassis is a member of a multi-chassis group and it is assigned as a backup lead chassis, the operations performed on the chassis using this module may conflict with the management operations performed on the chassis through the lead chassis.

## [Examples](ome_device_quick_deploy_module.md#id5)

```yaml+jinja
---
- name: Configure server Quick Deploy settings of the chassis using device ID.
  dellemc.openmanage.ome_device_quick_deploy:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    device_id: 25011
    setting_type: ServerQuickDeploy
    ca_path: "/path/to/ca_cert.pem"
    quick_deploy_options:
      password: "password"
      ipv4_enabled: True
      ipv4_network_type: Static
      ipv4_subnet_mask: 255.255.255.0
      ipv4_gateway: 192.168.0.1
      ipv6_enabled: True
      ipv6_network_type: Static
      ipv6_prefix_length: 1
      ipv6_gateway: "::"
      slots:
        - slot_id: 1
          slot_ipv4_address: 192.168.0.2
          slot_ipv6_address: "::"
          vlan_id: 1
        - slot_id: 2
          slot_ipv4_address: 192.168.0.3
          slot_ipv6_address: "::"
          vlan_id: 2

- name: Configure server Quick Deploy settings of the chassis using device service tag.
  dellemc.openmanage.ome_device_quick_deploy:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    device_service_tag: GHRT2RL
    setting_type: IOMQuickDeploy
    ca_path: "/path/to/ca_cert.pem"
    quick_deploy_options:
      password: "password"
      ipv4_enabled: True
      ipv4_network_type: Static
      ipv4_subnet_mask: 255.255.255.0
      ipv4_gateway: 192.168.0.1
      ipv6_enabled: True
      ipv6_network_type: Static
      ipv6_prefix_length: 1
      ipv6_gateway: "::"
      slots:
        - slot_id: 1
          slot_ipv4_address: 192.168.0.2
          slot_ipv6_address: "::"
          vlan_id: 1
        - slot_id: 2
          slot_ipv4_address: 192.168.0.3
          slot_ipv6_address: "::"
          vlan_id: 2
```

## [Return Values](ome_device_quick_deploy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **job_id**  integer | The job ID of the submitted quick deploy job.  Returned: when quick deploy job is submitted.  Sample: `1234` |
| **msg**  string | Overall status of the device quick deploy settings.  Returned: always  Sample: `"Successfully deployed the quick deploy settings."` |
| **quick_deploy_settings**  dictionary | returned when quick deploy settings are deployed successfully.  Returned: success  Sample: `{"DeviceId": 25011, "IpV4Gateway": "192.168.0.1", "IpV4SubnetMask": "255.255.255.0", "IpV6Gateway": "::", "NetworkTypeV4": "Static", "NetworkTypeV6": "Static", "PrefixLength": "2", "ProtocolTypeV4": true, "ProtocolTypeV6": true, "SettingType": "ServerQuickDeploy", "slots": [{"DeviceCapabilities": [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 41, 8, 7, 4, 3, 2, 1, 31, 30], "DeviceIPV4Address": "192.168.0.2", "DeviceIPV6Address": "::", "DeviceId": 25011, "Dhcpipv4": "Disabled", "Dhcpipv6": "Disabled", "Ipv4Enabled": "Enabled", "Ipv6Enabled": "Enabled", "Model": "PowerEdge MX840c", "SlotIPV4Address": "192.168.0.2", "SlotIPV6Address": "::", "SlotId": 1, "SlotSelected": true, "SlotSettingsApplied": true, "SlotType": "2000", "Type": "1000", "VlanId": "1"}, {"DeviceId": 0, "Model": "", "SlotIPV4Address": "0.0.0.0", "SlotIPV6Address": "::", "SlotId": 2, "SlotSelected": false, "SlotSettingsApplied": false, "SlotType": "2000", "Type": "0"}, {"DeviceId": 0, "Model": "", "SlotIPV4Address": "0.0.0.0", "SlotIPV6Address": "::", "SlotId": 3, "SlotSelected": false, "SlotSettingsApplied": false, "SlotType": "2000", "Type": "0"}, {"DeviceId": 0, "Model": "", "SlotIPV4Address": "0.0.0.0", "SlotIPV6Address": "::", "SlotId": 4, "SlotSelected": false, "SlotSettingsApplied": false, "SlotType": "2000", "Type": "0"}, {"DeviceId": 0, "Model": "", "SlotIPV4Address": "0.0.0.0", "SlotIPV6Address": "::", "SlotId": 5, "SlotSelected": false, "SlotSettingsApplied": false, "SlotType": "2000", "Type": "0"}, {"DeviceId": 0, "Model": "", "SlotIPV4Address": "0.0.0.0", "SlotIPV6Address": "::", "SlotId": 6, "SlotSelected": false, "SlotSettingsApplied": false, "SlotType": "2000", "Type": "0"}, {"DeviceId": 0, "Model": "", "SlotIPV4Address": "0.0.0.0", "SlotIPV6Address": "::", "SlotId": 7, "SlotSelected": false, "SlotSettingsApplied": false, "SlotType": "2000", "Type": "0"}, {"DeviceId": 0, "Model": "", "SlotIPV4Address": "0.0.0.0", "SlotIPV6Address": "::", "SlotId": 8, "SlotSelected": false, "SlotSettingsApplied": false, "SlotType": "2000", "Type": "0"}]}` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
