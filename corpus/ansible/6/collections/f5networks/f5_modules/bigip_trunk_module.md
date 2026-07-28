---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_trunk module – Manage trunks on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_trunk_module.html
fetched_at: 2026-07-27T17:27:58+00:00
---
# f5networks.f5_modules.bigip_trunk module – Manage trunks on a BIG-IP

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_trunk`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_trunk_module.md#synopsis)
- [Parameters](bigip_trunk_module.md#parameters)
- [Notes](bigip_trunk_module.md#notes)
- [Examples](bigip_trunk_module.md#examples)
- [Return Values](bigip_trunk_module.md#return-values)

## [Synopsis](bigip_trunk_module.md#id1)

- Manages trunks on a BIG-IP.

## [Parameters](bigip_trunk_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of the trunk. |
| **frame_distribution_hash**  string | Specifies the basis for the hash the system uses as the frame distribution algorithm. The system uses the resulting hash to determine which interface to use for forwarding traffic.  When creating a new trunk, if this parameter is not specified, the default is `source-destination-ip`.  When `source-destination-mac`, specifies the system bases the hash on the combined MAC addresses of the source and the destination.  When `destination-mac`, specifies the system bases the hash on the MAC address of the destination.  When `source-destination-ip`, specifies the system bases the hash on the combined IP addresses of the source and the destination.  Choices:   - `"destination-mac"` - `"source-destination-ip"` - `"source-destination-mac"` |
| **interfaces**  list / elements=string | The interfaces that are part of the trunk.  To clear the list of interfaces, specify an empty list. |
| **lacp_enabled**  boolean | When `yes`, specifies the system supports the link aggregation control protocol (LACP), which monitors the trunk by exchanging control packets over the member links to determine the health of the links.  If LACP detects a failure in a member link, it removes the link from the link aggregation.  When creating a new trunk, if this parameter is not specified, LACP is `no`.  LACP is disabled by default for backward compatibility. If this does not apply to your network, we recommend that you enable LACP.  Choices:   - `false` - `true` |
| **lacp_mode**  string | Specifies the operation mode for link aggregation control protocol (LACP), if LACP is enabled for the trunk.  When creating a new trunk, if this parameter is not specified, the default is `active`.  When `active`, specifies the system periodically sends control packets regardless of whether the partner system has issued a request.  When `passive`, specifies the system sends control packets only when the partner system has issued a request.  Choices:   - `"active"` - `"passive"` |
| **lacp_timeout**  string | Specifies the rate at which the system sends the LACP control packets.  When creating a new trunk, if this parameter is not specified, the default is `long`.  When `long`, specifies the system sends an LACP control packet every 30 seconds.  When `short`, specifies the system sends an LACP control packet every second.  Choices:   - `"long"` - `"short"` |
| **link_selection_policy**  string | Once the trunk is configured, specifies the policy the trunk uses to determine which member link (interface) can handle new traffic.  When creating a new trunk, if this value is not specified, the default is `auto`.  When `auto`, specifies the system automatically determines which interfaces can handle new traffic. For the `auto` option, the member links must all be the same media type and speed.  When `maximum-bandwidth`, specifies the system determines which interfaces can handle new traffic based on the members’ maximum bandwidth.  Choices:   - `"auto"` - `"maximum-bandwidth"` |
| **name**  string / required | Specifies the name of the trunk. |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **qinq_ethertype**  any | Specifies the ether-type value used for the packets handled on this trunk when it is a member in a QinQ VLAN.  The ether-type can be set to any string containing a valid hexadecimal 16 bits number, or any of the well known ether-types; `0x8100`, `0x9100`, `0x88a8`.  This parameter is not supported on Virtual Editions.  You should always wrap this value in quotes to prevent Ansible from interpreting the value as a literal hexadecimal number and converting it to an integer. |
| **state**  string | When `present`, ensures the resource exists.  When `absent`, ensures the resource is removed.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_trunk_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_trunk_module.md#id4)

```yaml+jinja
- name: Create a trunk on hardware
  bigip_trunk:
    name: trunk1
    interfaces:
      - 1.1
      - 1.2
    link_selection_policy: maximum-bandwidth
    frame_distribution_hash: destination-mac
    lacp_enabled: yes
    lacp_mode: passive
    lacp_timeout: short
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_trunk_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | Description of the trunk.  Returned: changed  Sample: `"My trunk"` |
| **frame_distribution_hash**  string | Hash the system uses as the frame distribution algorithm.  Returned: changed  Sample: `"src-dst-ipport"` |
| **interfaces**  list / elements=string | Interfaces that are part of the trunk.  Returned: changed  Sample: `["int1", "int2"]` |
| **lacp_enabled**  boolean | Whether the system supports the link aggregation control protocol (LACP) or not.  Returned: changed  Sample: `true` |
| **lacp_mode**  string | Operation mode for LACP if the lacp option is enabled for the trunk.  Returned: changed  Sample: `"active"` |
| **lacp_timeout**  string | Rate at which the system sends the LACP control packets.  Returned: changed  Sample: `"long"` |
| **link_selection_policy**  string | LACP policy the trunk uses to determine which member link (interface) can handle new traffic.  Returned: changed  Sample: `"auto"` |
| **qinq_ethertype**  string | Ether-type value used for the packets handled on this trunk when it is a member in a QinQ VLAN.  Returned: changed  Sample: `"37120"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
