---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_gtm_dns_listener module – Configures the BIG-IP DNS system to answer TCP or UDP DNS requests"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_gtm_dns_listener_module.html
fetched_at: 2026-07-27T17:26:47+00:00
---
# f5networks.f5_modules.bigip_gtm_dns_listener module – Configures the BIG-IP DNS system to answer TCP or UDP DNS requests

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_gtm_dns_listener`.

New in f5networks.f5_modules 1.4.0

- [Synopsis](bigip_gtm_dns_listener_module.md#synopsis)
- [Parameters](bigip_gtm_dns_listener_module.md#parameters)
- [Notes](bigip_gtm_dns_listener_module.md#notes)
- [Examples](bigip_gtm_dns_listener_module.md#examples)
- [Return Values](bigip_gtm_dns_listener_module.md#return-values)

## [Synopsis](bigip_gtm_dns_listener_module.md#id1)

- Defines one or more Listener objects to control which protocols are available for the BIG-IP DNS system to process DNS requests.
- BIG-IP DNS Listeners allow TCP and UDP protocols.

## [Parameters](bigip_gtm_dns_listener_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string / required | Specifies the IP address on which the system listens. |
| **advertise**  boolean | Specifies whether this Listener’s address is advertised to surrounding routers.  Choices:   - `false` - `true` |
| **auto_lasthop**  string | Specifies whether to automatically map the last hop for pools or not. |
| **description**  string | Provides a brief description for DNS Listener. |
| **disabled_vlans**  list / elements=string | List of VLANs to be disabled. If the partition is not specified in the VLAN, then the `partition` option of this module will be used.  This parameter is mutually exclusive with the `enabled_vlans` parameters. |
| **enabled_vlans**  list / elements=string | List of VLANs to be enabled. When a VLAN named `all` is used, all VLANs will be allowed. VLANs can be specified with or without the leading partition. If the partition is not specified in the VLAN, then the `partition` option of this module will be used.  This parameter is mutually exclusive with the `disabled_vlans` parameter. |
| **fallback_persistence**  string | Specifies a fallback persistence profile for the Listener to use when the default persistence profile is not available. |
| **ip_protocol**  string | Specifies the protocol on which this Listener receives network traffic. |
| **irules**  list / elements=string | Specifies list of iRules to run on the Listener.  iRules help automate the intercepting, processing, and routing of application traffic.  If you want to remove existing iRules, provide an empty list value; `[]`. See the documentation for an example. |
| **last_hop_pool**  string | Specifies the name of the last hop pool that you want the Listener to use to direct reply traffic to the last hop router. |
| **mask**  string | Specifies the netmask for a network Listener only.  Netmask clarifies whether the host bit is an actual zero or a wildcard representation. |
| **name**  string / required | Specifies the name of the DNS Listener. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **pool**  string | Specifies a default pool to which the Listener automatically directs traffic. |
| **port**  integer | Specifies the port on which the Listener listens for connections.  Valid range of values is between `0` and `65535` inclusive. |
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
| **source_port**  string | Specifies whether the system preserves the source port of the connection. |
| **state**  string | DNS Listener state.  When `present`, ensures the pool is created and enabled.  When `absent`, ensures the pool is removed from the system.  When `enabled` or `disabled`, ensures the pool is enabled or disabled respectively) on the remote device.  Choices:   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` |
| **translate_address**  boolean | Enables or disables address translation for the Listener.  Choices:   - `false` - `true` |
| **translate_port**  boolean | Enables or disables port translation.  Choices:   - `false` - `true` |

## [Notes](bigip_gtm_dns_listener_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_gtm_dns_listener_module.md#id4)

```yaml+jinja
- name: 'Create DNS Listener'
  bigip_gtm_dns_listener:
    address: '192.0.1.0'
    advertise: false
    auto_lasthop: default
    description: 'this is a test DNS listener'
    enabled_vlans:
      - /Common/external
    ip_protocol: tcp
    irules:
      - /Common/irule1
    mask: '255.255.255.0'
    pool: /Common/webpool
    name: test-dns-listener
    port: 30025
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
    source_port: preserve
    state: present
    translate_address: yes
    translate_port: yes
  delegate_to: localhost

- name: 'Disable a DNS Listener'
  bigip_gtm_dns_listener:
    address: '192.0.1.0'
    state: disabled
    name: test-dns-listener
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_gtm_dns_listener_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address**  string | IP address on which the system listens.  Returned: changed  Sample: `"10.0.0.2"` |
| **advertise**  boolean | Specifies if the Listener advertises to surrounding routers.  Returned: changed  Sample: `true` |
| **auto_lasthop**  string | Shows whether the system automatically maps the last hop for pools.  Returned: changed  Sample: `"default"` |
| **disabled_vlans**  list / elements=string | List of VLANs the virtual is disabled for.  Returned: changed  Sample: `["/Common/vlan1", "/Common/vlan2"]` |
| **enabled**  boolean | Provides DNS Listener state.  Returned: changed  Sample: `true` |
| **enabled_vlans**  list / elements=string | List of VLANs the virtual is enabled for.  Returned: changed  Sample: `["/Common/vlan5", "/Common/vlan6"]` |
| **fallback_persistence**  string | Fallback persistence profile for the Listener to use when the default persistence profile is not available.  Returned: changed  Sample: `"/Common/fallback-profile"` |
| **ip_protocol**  string | IP protocol used by the DNS Listener.  Returned: changed  Sample: `"tcp"` |
| **irules**  list / elements=string | List of rules run by the DNS Listener.  Returned: changed  Sample: `["/Common/rule1", "/Common/rule2"]` |
| **mask**  string | Subnet mask used by the Listener to identify address range.  Returned: changed  Sample: `"255.255.0.0"` |
| **name**  string | DNS Listener name.  Returned: changed  Sample: `"test-dns-listener"` |
| **port**  integer | Port on which the system listens.  Returned: changed  Sample: `53` |
| **source_port**  string | Specifies if system preserves the source port of the connection.  Returned: changed  Sample: `"preserve"` |
| **translate_address**  string | Specifies if address translation is enabled.  Returned: changed  Sample: `"enabled"` |
| **translate_port**  string | Specifies if port translation is enabled.  Returned: changed  Sample: `"enabled"` |

### Authors

- Andrey Kashcheev (@andreykashcheev)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
