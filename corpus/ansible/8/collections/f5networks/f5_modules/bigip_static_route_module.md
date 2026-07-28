---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_static_route module – Manipulate static routes on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_static_route_module.html
fetched_at: 2026-07-28T02:07:24+00:00
---
# f5networks.f5_modules.bigip_static_route module – Manipulate static routes on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_static_route`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_static_route_module.md#synopsis)
- [Parameters](bigip_static_route_module.md#parameters)
- [Notes](bigip_static_route_module.md#notes)
- [Examples](bigip_static_route_module.md#examples)
- [Return Values](bigip_static_route_module.md#return-values)

## [Synopsis](bigip_static_route_module.md#id1)

- Manipulate static routes on a BIG-IP system.

## [Parameters](bigip_static_route_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | Descriptive text that identifies the route. |
| **destination**  string | Specifies an IP address for the static entry in the routing table. When creating a new static route, this value is required.  This value cannot be changed once it is set. |
| **gateway_address**  string | Specifies the router for the system to use when forwarding packets to the destination host or network. Also known as the next-hop router address. This can be either an IPv4 or IPv6 address. When it is an IPv6 address that starts with `FE80:`, the address is treated as a link-local address. This requires the `vlan` parameter also be supplied. |
| **mtu**  string | Specifies a specific maximum transmission unit (MTU). |
| **name**  string / required | Name of the static route. |
| **netmask**  string | The netmask for the static route. When creating a new static route, this value is required.  This value can be in either IP or CIDR format.  This value cannot be changed once it is set. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **pool**  string | Specifies the pool through which the system forwards packets to the destination. |
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
| **reject**  boolean | Specifies the system drops packets sent to the destination.  **Choices:**   - `false` - `true` |
| **route_domain**  integer | The route domain ID of the system. When creating a new static route, if this value is not specified, the default value is `0`.  This value cannot be changed once it is set. |
| **state**  string | When `present`, ensures the static route exists.  When `absent`, ensures the static does not exist.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vlan**  string | Specifies the VLAN or Tunnel through which the system forwards packets to the destination. When `gateway_address` is a link-local IPv6 address, this value is required. |

## [Notes](bigip_static_route_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_static_route_module.md#id4)

```yaml+jinja
- name: Create static route with gateway address
  bigip_static_route:
    destination: 10.10.10.10
    netmask: 255.255.255.255
    gateway_address: 10.2.2.3
    name: test-route
    provider:
      password: secret
      server: lb.mydomain.come
      user: admin
      validate_certs: false
  delegate_to: localhost
```

## [Return Values](bigip_static_route_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | Descriptive text that identifies the route.  **Returned:** changed  **Sample:** `"Route tho DMZ"` |
| **destination**  string | An IP address for the static entry in the routing table.  **Returned:** changed  **Sample:** `"0.0.0.0/0"` |
| **gateway_address**  string | The router for the system to use when forwarding packets to the destination host or network.  **Returned:** changed  **Sample:** `"10.2.2.3"` |
| **netmask**  string | Netmask of the destination.  **Returned:** changed  **Sample:** `"255.255.255.255"` |
| **partition**  string | The partition that the static route was created on.  **Returned:** changed  **Sample:** `"Common"` |
| **pool**  string | Whether the banner is enabled or not.  **Returned:** changed  **Sample:** `"True"` |
| **reject**  boolean | Specifies the system drops packets sent to the destination.  **Returned:** changed  **Sample:** `true` |
| **route_domain**  integer | The route domain ID of the system.  **Returned:** changed  **Sample:** `1` |
| **vlan**  string | The VLAN or Tunnel through which the system forwards packets to the destination.  **Returned:** changed  **Sample:** `"/Common/vlan1"` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
