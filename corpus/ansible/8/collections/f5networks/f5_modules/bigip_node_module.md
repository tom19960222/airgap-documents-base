---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_node module – Manages F5 BIG-IP LTM nodes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_node_module.html
fetched_at: 2026-07-28T02:06:51+00:00
---
# f5networks.f5_modules.bigip_node module – Manages F5 BIG-IP LTM nodes

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules/) (version 1.27.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_node`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_node_module.md#synopsis)
- [Parameters](bigip_node_module.md#parameters)
- [Notes](bigip_node_module.md#notes)
- [Examples](bigip_node_module.md#examples)
- [Return Values](bigip_node_module.md#return-values)

## [Synopsis](bigip_node_module.md#id1)

- Manages F5 BIG-IP LTM nodes.

## [Parameters](bigip_node_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  aliases: ip, host  string | IP address of the node. This can be either IPv4 or IPv6. When creating a new node, you must provide one of either `address` or `fqdn`. This parameter cannot be updated after it is set. |
| **availability_requirements**  dictionary | If you activate more than one health monitor, specifies the number of health monitors that must receive successful responses in order for the link to be considered available. |
| **at_least**  integer | Specifies the minimum number of active health monitors that must be successful before the link is considered up.  This parameter is only relevant when a `type` of `at_least` is used.  This parameter will be ignored if a type of `all` is used. |
| **type**  string / required | Monitor rule type when `monitors` is specified.  When creating a new pool, if this value is not specified, the default of ‘all’ will be used.  **Choices:**   - `"all"` - `"at_least"` |
| **connection_limit**  integer | Node connection limit. Setting this to `0` disables the limit. |
| **description**  string | Specifies descriptive text that identifies the node.  You can remove a description by either specifying an empty string, or by specifying the special value `none`. |
| **dynamic_ratio**  integer | The dynamic ratio number for the node. Used for dynamic ratio load balancing.  When creating a new node, if this parameter is not specified, the default of `1` will be used. |
| **fqdn**  aliases: hostname  string | FQDN name of the node. This can be any name that is a valid RFC 1123 DNS name. Therefore, the only characters that can be used are “A” to “Z”, “a” to “z”, “0” to “9”, the hyphen (“-”) and the period (“.”).  FQDN names must include at least one period; delineating the host from the domain. For example, `host.domain`.  FQDN names must end with a letter or a number.  When creating a new node, you must provide one of either `address` or `fqdn` provided. This parameter cannot be updated after it is set. |
| **fqdn_address_type**  string | Specifies whether the FQDN of the node resolves to an IPv4 or IPv6 address.  When creating a new node, if this parameter is not specified and `fqdn` is specified, this parameter will default to `ipv4`.  This parameter cannot be changed after it has been set.  **Choices:**   - `"ipv4"` - `"ipv6"` - `"all"` |
| **fqdn_auto_populate**  boolean | Specifies whether the system automatically creates ephemeral nodes using the IP addresses returned by the resolution of a DNS query for a node defined by an FQDN.  When `true`, the system generates an ephemeral node for each IP address returned in response to a DNS query for the FQDN of the node. Additionally, when a DNS response indicates the IP address of an ephemeral node no longer exists, the system deletes the ephemeral node.  When `false`, the system resolves a DNS query for the FQDN of the node with the single IP address associated with the FQDN.  When creating a new node, if this parameter is not specified and `fqdn` is specified, this parameter defaults to `true`.  This parameter cannot be changed after it has been set.  **Choices:**   - `false` - `true` |
| **fqdn_down_interval**  integer | Specifies the interval in which a query occurs, when the DNS server is down. The associated monitor continues polling as long as the DNS server is down.  When creating a new node, if this parameter is not specified and `fqdn` is specified, this parameter will default to `5`. |
| **fqdn_up_interval**  string | Specifies the interval at which a query occurs, when the DNS server is up. The associated monitor attempts to probe three times, and marks the server down if it there is no response within the span of three times the interval value, in seconds.  This parameter accepts a value of `ttl` to query, based off of the TTL of the FQDN. The default TTL interval is similar to specifying `3600`.  When creating a new node, if this parameter is not specified and `fqdn` is specified, this parameter will default to `3600`. |
| **monitors**  list / elements=string | Specifies the health monitors the system currently uses to monitor this node. |
| **name**  string / required | Specifies the name of the node. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **provider**  dictionary  *added in f5networks.f5_modules 1.0.0* | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  **Choices:**   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP or the BIG-IQ.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host or the BIG-IQ host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  **Default:** `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  **Choices:**   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP or the BIG-IQ. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  **Choices:**   - `false` - `true` ← (default) |
| **rate_limit**  integer | Node rate limit (connections-per-second). Setting this to `0` disables the limit. |
| **ratio**  integer | Node ratio weight. Valid values range from 1 through 100.  When creating a new node, if this parameter is not specified, the default of `1` will be used. |
| **state**  string | Specifies the current state of the node. `enabled` (All traffic allowed), specifies the system sends traffic to this node regardless of the node’s state. `disabled` (Only persistent or active connections allowed), specifies the node can handle only persistent or active connections. `offline` (Only active connections allowed), specifies the node can handle only active connections. In all cases except `absent`, the node will be created if it does not yet exist.  Be particularly careful about changing the status of a node whose FQDN cannot be resolved. These situations disable your ability to change their `state` to `disabled` or `offline`. They will remain in an \*Unavailable - Enabled\* state.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` - `"offline"` |

## [Notes](bigip_node_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_node_module.md#id4)

```yaml+jinja
- name: Add node
  bigip_node:
    host: 10.20.30.40
    name: 10.20.30.40
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add node with a single 'ping' monitor
  bigip_node:
    host: 10.20.30.40
    name: mytestserver
    monitors:
      - /Common/icmp
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Modify node description
  bigip_node:
    name: 10.20.30.40
    description: Our best server yet
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Delete node
  bigip_node:
    state: absent
    name: 10.20.30.40
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Force node offline
  bigip_node:
    state: disabled
    name: 10.20.30.40
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add node by their FQDN
  bigip_node:
    fqdn: foo.bar.com
    name: foobar.net
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_node_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | Changed value for the description of the node.  **Returned:** changed and success  **Sample:** `"E-Commerce webserver in ORD"` |
| **monitors**  list / elements=string | Changed list of monitors for the node.  **Returned:** changed and success  **Sample:** `["icmp", "tcp_echo"]` |
| **session**  string | Changed value for the internal session of the node.  **Returned:** changed and success  **Sample:** `"user-disabled"` |
| **state**  string | Changed value for the internal state of the node.  **Returned:** changed and success  **Sample:** `"user-down"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
