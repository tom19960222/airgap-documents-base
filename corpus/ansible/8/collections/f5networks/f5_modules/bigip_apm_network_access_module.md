---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_apm_network_access module – Manage APM Network Access resource"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_apm_network_access_module.html
fetched_at: 2026-07-28T02:05:34+00:00
---
# f5networks.f5_modules.bigip_apm_network_access module – Manage APM Network Access resource

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_apm_network_access`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_apm_network_access_module.md#synopsis)
- [Parameters](bigip_apm_network_access_module.md#parameters)
- [Notes](bigip_apm_network_access_module.md#notes)
- [Examples](bigip_apm_network_access_module.md#examples)
- [Return Values](bigip_apm_network_access_module.md#return-values)

## [Synopsis](bigip_apm_network_access_module.md#id1)

- Manage APM Network Access resource.

## [Parameters](bigip_apm_network_access_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow_local_dns**  boolean | Enables local access to DNS servers configured on the client prior to establishing a network access connection.  **Choices:**   - `false` - `true` |
| **allow_local_subnet**  boolean | Enables local subnet access and local access to any host or subnet in routes specified in the client routing table.  When `true` the system does not support integrated IP filtering.  **Choices:**   - `false` - `true` |
| **description**  string | User created network access description. |
| **dns_address_space**  list / elements=string | Specifies a list of domain names describing the target LAN DNS addresses. |
| **dtls**  boolean | When `true` the network access connection uses Datagram Transport Level Security instead of TCP, to provide better throughput for high demand applications like VoIP or streaming video.  **Choices:**   - `false` - `true` |
| **dtls_port**  integer | Specifies the port number the network access resource uses for secure UDP traffic with DTLS. |
| **excluded_dns_addresses**  list / elements=string | Specifies the DNS address spaces for which traffic is not forced through the tunnel. |
| **excluded_ipv4_adresses**  list / elements=dictionary | Specifies IPV4 address spaces for which traffic is not forced through the tunnel. |
| **subnet**  string | The address of subnet in CIDR format, e.g. `192.168.1.0/24`  Host addresses can be specified without the CIDR mask notation. |
| **excluded_ipv6_adresses**  list / elements=dictionary | Specifies IPV6 address spaces for which traffic is not forced through the tunnel. |
| **subnet**  string | The address of a subnet in CIDR format, e.g. `2001:db8:abcd:8000::/52`  Host addresses can be specified without the CIDR mask notation. |
| **ip_version**  string | Supported IP version on the network access resource.  **Choices:**   - `"ipv4"` - `"ipv4-ipv6"` |
| **ipv4_address_space**  list / elements=dictionary | Specifies a list of IPv4 hosts or networks describing the target LAN.  This option is mandatory when creating a new resource and `split_tunnel` is set to `true`. |
| **subnet**  string | The address of subnet in CIDR format, e.g. `192.168.1.0/24`  Host addresses can be specified without the CIDR mask notation. |
| **ipv4_lease_pool**  string | Specifies the IPV4 lease pool resource to use with network access.  Referencing a lease pool can be done in the full path format, for example `/Common/pool_name`.  When a lease pool is referenced in full path format, the `partition` parameter is ignored. |
| **ipv6_address_space**  list / elements=dictionary | Specifies a list of IPv6 hosts or networks describing the target LAN.  This option is mandatory when creating a new resource and `split_tunnel` is set to `true`. |
| **subnet**  string | The address of subnet in CIDR format, e.g. `2001:db8:abcd:8000::/52`  Host addresses can be specified without the CIDR mask notation. |
| **ipv6_lease_pool**  string | Specifies the IPV6 lease pool resource to use with network access.  Referencing a lease pool can be done in the full path format, for example `/Common/pool_name`.  When a lease pool is referenced in full path format, the `partition` parameter is ignored. |
| **name**  string / required | Specifies the name of the APM network access to manage/create. |
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
| **snat_pool**  string | Specifies the name of a SNAT pool used for implementing selective and intelligent SNATs.  When `none` the system uses no SNAT pool for this network resource.  When `automap` the system uses all of the self IP addresses as the translation addresses for the pool. |
| **split_tunnel**  boolean | Specifies that only the traffic targeted to a specified address space is sent over the network access tunnel.  **Choices:**   - `false` - `true` |
| **state**  string | When `state` is `present`, ensures the ACL exists.  When `state` is `absent`, ensures the ACL is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_apm_network_access_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_apm_network_access_module.md#id4)

```yaml+jinja
- name: Create a split tunnel IPV4 Network Access
  bigip_apm_network_access:
    name: foobar
    ip_version: ipv4
    split_tunnel: true
    snat_pool: "none"
    ipv4_lease_pool: leasefoo
    ipv4_address_space:
      - subnet: 10.10.1.1
      - subnet: 10.10.2.0/24
    excluded_ipv4_adresses:
      - subnet: 192.168.1.0/24
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Modify a split tunnel IPV4 Network Access
  bigip_apm_network_access:
    name: foobar
    snat_pool: /Common/poolsnat
    ipv4_address_space:
      - subnet: 172.16.23.0/24
    excluded_ipv4_adresses:
      - subnet: 10.10.2.0/24
    allow_local_subnet: true
    allow_local_dns: true
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove Network Access
  bigip_apm_network_access:
    name: foobar
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_apm_network_access_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allow_local_dns**  boolean | Enables local access to DNS servers configured on the client.  **Returned:** changed  **Sample:** `true` |
| **allow_local_subnet**  boolean | Enables local subnet access.  **Returned:** changed  **Sample:** `true` |
| **description**  string | The new description of Network Access.  **Returned:** changed  **Sample:** `"My Access"` |
| **dns_address_space**  list / elements=string | Specifies a list of domain names describing the target LAN DNS addresses.  **Returned:** changed  **Sample:** `["internal.net", "*.engnet.org"]` |
| **dtls**  boolean | Enables use of DTLS by network access.  **Returned:** changed  **Sample:** `false` |
| **dtls_port**  integer | Specifies the port number the network access resource uses for DTLS.  **Returned:** changed  **Sample:** `4433` |
| **excluded_dns_addresses**  list / elements=string | Specifies the DNS address spaces for which traffic is not forced through the tunnel.  **Returned:** changed  **Sample:** `["foobar.com", "bazbar.org"]` |
| **excluded_ipv4_adresses**  complex | Specifies IPV4 address spaces for which traffic is not forced through the tunnel.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **subnet**  string | The host or network address.  **Returned:** changed  **Sample:** `"192.168.10.1"` |
| **excluded_ipv6_adresses**  complex | Specifies IPV6 address spaces for which traffic is not forced through the tunnel.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **subnet**  string | The host or network address.  **Returned:** changed  **Sample:** `"2001:DB8:ABCD:0012::0"` |
| **ip_version**  string | Supported IP version on the network access resource.  **Returned:** changed  **Sample:** `"ipv4-ipv6"` |
| **ipv4_address_space**  complex | Specifies a list of IPv4 hosts or networks describing the target LAN.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **subnet**  string | The host or network address.  **Returned:** changed  **Sample:** `"192.168.10.1"` |
| **ipv4_lease_pool**  string | Specifies a IPV4 lease pool resource to use with network access.  **Returned:** changed  **Sample:** `"/Common/leasepoolv4"` |
| **ipv6_address_space**  complex | Specifies a list of IPv6 hosts or networks describing the target LAN.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **subnet**  string | The host or network address.  **Returned:** changed  **Sample:** `"2001:DB8:ABCD:0012::0"` |
| **ipv6_lease_pool**  string | Specifies a IPV6 lease pool resource to use with network access.  **Returned:** changed  **Sample:** `"/Common/leasepoolv6"` |
| **snat_pool**  string | The name of a SNAT pool used by the network access resource.  **Returned:** changed  **Sample:** `"/Common/my-pool"` |
| **split_tunnel**  boolean | Enables split tunnel on the network access resource.  **Returned:** changed  **Sample:** `true` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
