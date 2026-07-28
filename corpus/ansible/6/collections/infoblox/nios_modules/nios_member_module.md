---
collection: ansible
version: "6"
title: "infoblox.nios_modules.nios_member module – Configure Infoblox NIOS members"
source_url: https://docs.ansible.com/projects/ansible/6/collections/infoblox/nios_modules/nios_member_module.html
fetched_at: 2026-07-27T17:50:59+00:00
---
# infoblox.nios_modules.nios_member module – Configure Infoblox NIOS members

> **Note:**
>
> This module is part of the [infoblox.nios_modules collection](https://galaxy.ansible.com/infoblox/nios_modules) (version 1.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install infoblox.nios_modules`.
> You need further requirements to be able to use this module,
> see [Requirements](nios_member_module.md#ansible-collections-infoblox-nios-modules-nios-member-module-requirements) for details.
>
> To use it in a playbook, specify: `infoblox.nios_modules.nios_member`.

New in infoblox.nios_modules 1.0.0

- [Synopsis](nios_member_module.md#synopsis)
- [Requirements](nios_member_module.md#requirements)
- [Parameters](nios_member_module.md#parameters)
- [Notes](nios_member_module.md#notes)
- [Examples](nios_member_module.md#examples)

## [Synopsis](nios_member_module.md#id1)

- Adds and/or removes Infoblox NIOS servers. This module manages NIOS `member` objects using the Infoblox WAPI interface over REST.

## [Requirements](nios_member_module.md#id2)

The below requirements are needed on the host that executes this module.

- infoblox-client

## [Parameters](nios_member_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **comment**  string | A descriptive comment of the Grid member. |
| **config_addr_type**  string | Address configuration type (IPV4/IPV6/BOTH).  Default: `"IPV4"` |
| **create_token**  boolean | Flag for initiating a create token request for pre-provisioned members.  Choices:   - `false` ← (default) - `true` |
| **enable_ha**  boolean | If set to True, the member has two physical nodes (HA pair).  Choices:   - `false` ← (default) - `true` |
| **extattrs**  dictionary | Extensible attributes associated with the object. |
| **external_syslog_server_enable**  boolean | Determines if external syslog servers should be enabled.  Choices:   - `false` - `true` |
| **host_name**  aliases: name  string / required | Specifies the host name of the member to either add or remove from the NIOS instance. |
| **ipv6_setting**  list / elements=dictionary | Configures the IPv6 settings for the grid member. |
| **cidr_prefix**  integer | The IPv6 CIDR prefix for the Grid Member |
| **gateway**  string | The gateway address for the Grid Member |
| **virtual_ip**  string | The IPv6 Address of the Grid Member |
| **lan2_enabled**  boolean | When set to “true”, the LAN2 port is enabled as an independent port or as a port for failover purposes.  Choices:   - `false` ← (default) - `true` |
| **lan2_port_setting**  list / elements=dictionary | Settings for the Grid member LAN2 port if ‘lan2_enabled’ is set to “true”. |
| **enabled**  boolean | If set to True, then it has its own IP settings.  Choices:   - `false` - `true` |
| **network_setting**  list / elements=dictionary | If the ‘enable’ field is set to True, this defines IPv4 network settings for LAN2. |
| **address**  string | The IPv4 Address of LAN2 |
| **gateway**  string | The default gateway of LAN2 |
| **subnet_mask**  string | The subnet mask of LAN2 |
| **v6_network_setting**  list / elements=dictionary | If the ‘enable’ field is set to True, this defines IPv6 network settings for LAN2. |
| **cidr_prefix**  integer | The IPv6 CIDR prefix of LAN2 |
| **gateway**  string | The gateway address of LAN2 |
| **virtual_ip**  string | The IPv6 Address of LAN2 |
| **mgmt_port_setting**  list / elements=dictionary | Settings for the member MGMT port. |
| **enabled**  boolean | Determines if MGMT port settings should be enabled.  Choices:   - `false` - `true` |
| **security_access_enabled**  boolean | Determines if security access on the MGMT port is enabled or not.  Choices:   - `false` - `true` |
| **vpn_enabled**  boolean | Determines if VPN on the MGMT port is enabled or not.  Choices:   - `false` - `true` |
| **node_info**  list / elements=dictionary | Configures the node information list with detailed status report on the operations of the Grid Member. |
| **lan2_physical_setting**  list / elements=dictionary | Physical port settings for the LAN2 interface. |
| **auto_port_setting_enabled**  boolean | Enable or disalbe the auto port setting.  Choices:   - `false` - `true` |
| **duplex**  string | The port duplex; if speed is 1000, duplex must be FULL. |
| **speed**  string | The port speed; if speed is 1000, duplex is FULL. |
| **lan_ha_port_setting**  list / elements=dictionary | LAN/HA port settings for the node. |
| **ha_ip_address**  string | HA IP address. |
| **ha_port_setting**  list / elements=dictionary | Physical port settings for the HA interface. |
| **auto_port_setting_enabled**  boolean | Enable or disalbe the auto port setting.  Choices:   - `false` - `true` |
| **duplex**  string | The port duplex; if speed is 1000, duplex must be FULL. |
| **speed**  string | The port speed; if speed is 1000, duplex is FULL. |
| **lan_port_setting**  list / elements=dictionary | Physical port settings for the LAN interface. |
| **auto_port_setting_enabled**  boolean | Enable or disalbe the auto port setting.  Choices:   - `false` - `true` |
| **duplex**  string | The port duplex; if speed is 1000, duplex must be FULL. |
| **speed**  string | The port speed; if speed is 1000, duplex is FULL. |
| **mgmt_ipv6addr**  string | Public IPv6 address for the LAN1 interface. |
| **mgmt_lan**  string | Public IPv4 address for the LAN1 interface. |
| **mgmt_network_setting**  list / elements=dictionary | Network settings for the MGMT port of the node. |
| **address**  string | The IPv4 Address of MGMT |
| **gateway**  string | The default gateway of MGMT |
| **subnet_mask**  string | The subnet mask of MGMT |
| **v6_mgmt_network_setting**  list / elements=dictionary | The network settings for the IPv6 MGMT port of the node. |
| **cidr_prefix**  integer | The IPv6 CIDR prefix of MGMT |
| **gateway**  string | The gateway address of MGMT |
| **virtual_ip**  string | The IPv6 Address of MGMT |
| **platform**  string | Configures the Hardware Platform.  Default: `"INFOBLOX"` |
| **pre_provisioning**  list / elements=dictionary | Pre-provisioning information. |
| **hardware_info**  list / elements=dictionary | An array of structures that describe the hardware being pre-provisioned. |
| **hwmodel**  string | Hardware model |
| **hwtype**  string | Hardware type. |
| **licenses**  list / elements=string | An array of license types. |
| **provider**  dictionary | A dict object containing connection details. |
| **cert**  string | Specifies the client certificate file with digest of x509 config for extra layer secure connection the remote instance of NIOS.  Value can also be specified using `INFOBLOX_CERT` environment variable. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST  Value can also be specified using `INFOBLOX_HOST` environment variable. |
| **http_pool_connections**  integer | Insert decription here  Default: `10` |
| **http_pool_maxsize**  integer | Insert description here  Default: `10` |
| **http_request_timeout**  integer | The amount of time before to wait before receiving a response  Value can also be specified using `INFOBLOX_HTTP_REQUEST_TIMEOUT` environment variable.  Default: `10` |
| **key**  string | Specifies private key file for encryption with the certificate in order to connect with remote instance of NIOS.  Value can also be specified using `INFOBLOX_KEY` environment variable. |
| **max_results**  integer | Specifies the maximum number of objects to be returned, if set to a negative number the appliance will return an error when the number of returned objects would exceed the setting.  Value can also be specified using `INFOBLOX_MAX_RESULTS` environment variable.  Default: `1000` |
| **max_retries**  integer | Configures the number of attempted retries before the connection is declared usable  Value can also be specified using `INFOBLOX_MAX_RETRIES` environment variable.  Default: `3` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote instance of NIOS.  Value can also be specified using `INFOBLOX_PASSWORD` environment variable. |
| **silent_ssl_warnings**  boolean | Insert description here  Choices:   - `false` - `true` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote instance of NIOS.  Value can also be specified using `INFOBLOX_USERNAME` environment variable. |
| **validate_certs**  aliases: ssl_verify  boolean | Boolean value to enable or disable verifying SSL certificates  Value can also be specified using `INFOBLOX_SSL_VERIFY` environment variable.  Choices:   - `false` ← (default) - `true` |
| **wapi_version**  string | Specifies the version of WAPI to use  Value can also be specified using `INFOBLOX_WAP_VERSION` environment variable.  Until ansible 2.8 the default WAPI was 1.4  Default: `"2.1"` |
| **router_id**  integer | Virtual router identifier. Provide this ID if “ha_enabled” is set to “true”. This is a unique VRID number (from 1 to 255) for the local subnet. |
| **state**  string | Configures the intended state of the instance of the object on the NIOS server. When this value is set to `present`, the object is configured on the device and when this value is set to `absent` the value is removed (if necessary) from the device.  Choices:   - `"present"` ← (default) - `"absent"` |
| **syslog_servers**  list / elements=dictionary | The list of external syslog servers. |
| **address**  string | The server address. |
| **category_list**  list / elements=string | The list of all syslog logging categories. |
| **connection_type**  string | The connection type for communicating with this server.(STCP/TCP?UDP)  Default: `"UDP"` |
| **local_interface**  string | The local interface through which the appliance sends syslog messages to the syslog server.(ANY/LAN/MGMT)  Default: `"ANY"` |
| **message_node_id**  string | Identify the node in the syslog message. (HOSTNAME/IP_HOSTNAME/LAN/MGMT)  Default: `"LAN"` |
| **message_source**  string | The source of syslog messages to be sent to the external syslog server.  Default: `"ANY"` |
| **only_category_list**  boolean | The list of selected syslog logging categories. The appliance forwards syslog messages that belong to the selected categories.  Choices:   - `false` - `true` |
| **port**  integer | The port this server listens on.  Default: `514` |
| **severity**  string | The severity filter. The appliance sends log messages of the specified severity and above to the external syslog server.  Default: `"DEBUG"` |
| **upgrade_group**  string | The name of the upgrade group to which this Grid member belongs.  Default: `"Default"` |
| **use_syslog_proxy_setting**  boolean | Use flag for external_syslog_server_enable , syslog_servers, syslog_proxy_setting, syslog_size.  Choices:   - `false` - `true` |
| **vip_setting**  list / elements=dictionary | Configures the network settings for the grid member. |
| **address**  string | The IPv4 Address of the Grid Member |
| **gateway**  string | The default gateway for the Grid Member |
| **subnet_mask**  string | The subnet mask for the Grid Member |

## [Notes](nios_member_module.md#id4)

> **Note:**
>
> - This module supports `check_mode`.
> - This module must be run locally, which can be achieved by specifying `connection: local`.
> - Please read the :ref:`nios_guide` for more detailed information on how to use Infoblox with Ansible.

## [Examples](nios_member_module.md#id5)

```yaml+jinja
- name: Add a member to the grid with IPv4 address
  infoblox.nios_modules.nios_member:
    host_name: member01.localdomain
    vip_setting:
      - address: 192.168.1.100
        subnet_mask: 255.255.255.0
        gateway: 192.168.1.1
    config_addr_type: IPV4
    platform: VNIOS
    comment: "Created by Ansible"
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Add a HA member to the grid
  infoblox.nios_modules.nios_member:
    host_name: memberha.localdomain
    vip_setting:
      - address: 192.168.1.100
        subnet_mask: 255.255.255.0
        gateway: 192.168.1.1
    config_addr_type: IPV4
    platform: VNIOS
    enable_ha: true
    router_id: 150
    node_info:
      - lan_ha_port_setting:
         - ha_ip_address: 192.168.1.70
           mgmt_lan: 192.168.1.80
      - lan_ha_port_setting:
         - ha_ip_address: 192.168.1.71
           mgmt_lan: 192.168.1.81
    comment: "Created by Ansible"
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Update the member with pre-provisioning details specified
  infoblox.nios_modules.nios_member:
    name: member01.localdomain
    pre_provisioning:
      - hardware_info:
         - hwmodel: IB-VM-820
           hwtype: IB-VNIOS
        licenses:
         - dns
         - dhcp
         - enterprise
         - vnios
    comment: "Updated by Ansible"
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Remove the member
  infoblox.nios_modules.nios_member:
    name: member01.localdomain
    state: absent
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
```

### Authors

- Krishna Vasudevan (@krisvasudevan)

### Collection links

[Issue Tracker](https://github.com/infobloxopen/infoblox-ansible/issues)
[Homepage](https://github.com/infobloxopen/infoblox-ansible)
[Repository (Sources)](https://github.com/infobloxopen/infoblox-ansible/tree/master)
