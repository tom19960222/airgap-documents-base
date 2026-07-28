---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_virtual_address module – Manage LTM virtual addresses on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_virtual_address_module.html
fetched_at: 2026-07-27T17:28:02+00:00
---
# f5networks.f5_modules.bigip_virtual_address module – Manage LTM virtual addresses on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_virtual_address`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_virtual_address_module.md#synopsis)
- [Parameters](bigip_virtual_address_module.md#parameters)
- [Notes](bigip_virtual_address_module.md#notes)
- [Examples](bigip_virtual_address_module.md#examples)
- [Return Values](bigip_virtual_address_module.md#return-values)

## [Synopsis](bigip_virtual_address_module.md#id1)

- Manage LTM virtual addresses on a BIG-IP system.

## [Parameters](bigip_virtual_address_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string | Specifies the virtual address. This value cannot be modified after it is set.  If you never created a virtual address, but did create virtual servers, a virtual address for each virtual server was created automatically. The name of this virtual address is its IP address value. |
| **arp**  boolean | Specifies whether the system accepts ARP requests.  When `no`, specifies the system does not accept ARP requests.  When `yes`, the packets are dropped.  Both ARP and ICMP Echo must be disabled in order for forwarding virtual servers using that virtual address to forward ICMP packets.  When creating a new virtual address, if this parameter is not specified, the default value is `yes`.  Choices:   - `false` - `true` |
| **auto_delete**  boolean | Specifies whether the system automatically deletes the virtual address with the deletion of the last associated virtual server. When `no`, specifies the system leaves the virtual address, even when all associated virtual servers have been deleted. When creating the virtual address, the default value is `yes`.  Choices:   - `false` - `true` |
| **availability_calculation**  aliases: advertise_route  string | Specifies which routes of the virtual address the system advertises. When `when_any_available`, advertises the route when any virtual server is available. When `when_all_available`, advertises the route when all virtual servers are available. When (always), always advertises the route regardless of the virtual servers available.  Choices:   - `"always"` - `"when_all_available"` - `"when_any_available"` |
| **connection_limit**  integer | Specifies the number of concurrent connections the system allows on this virtual address. |
| **icmp_echo**  string | Specifies how the system sends responses to (ICMP) echo requests on a per-virtual address basis for enabling route advertisement. When `enabled`, the BIG-IP system intercepts ICMP echo request packets and responds to them directly. When `disabled`, the BIG-IP system passes ICMP echo requests through to the backend servers. When (selective), causes the BIG-IP system to internally enable or disable responses based on virtual server state; `when_any_available`, `when_all_available, or C(always`, regardless of the state of any virtual servers.  Choices:   - `"enabled"` - `"disabled"` - `"selective"` |
| **name**  string | Name of the virtual address.  If this parameter is not provided, the system uses the value of `address`. |
| **netmask**  string | Specifies the netmask of the provided virtual address. This value cannot be modified after it is set.  When creating a new virtual address, if this parameter is not specified, the default value is `255.255.255.255` for IPv4 addresses and `ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff` for IPv6 addresses. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
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
| **route_advertisement**  string | Specifies whether the system uses route advertisement for this virtual address.  When disabled, the system does not advertise routes for this virtual address.  The majority of these options are only supported on versions 13.0.0-HF1 or later. On versions prior than this, all choices expect `disabled` translate to `enabled`.  When `always`, the BIG-IP system always advertises the route for the virtual address, regardless of availability status. This requires an `enabled` virtual address.  When `enabled`, the BIG-IP system advertises the route for the available virtual address, based on the calculation method in the availability calculation.  When `disabled`, the BIG-IP system does not advertise the route for the virtual address, regardless of the availability status.  When `selective`, you can also selectively enable ICMP echo responses, which causes the BIG-IP system to internally enable or disable responses based on virtual server state.  When `any`, the BIG-IP system advertises the route for the virtual address when any virtual server is available.  When `all`, the BIG-IP system advertises the route for the virtual address when all virtual servers are available.  Choices:   - `"disabled"` - `"enabled"` - `"always"` - `"selective"` - `"any"` - `"all"` |
| **route_domain**  string | The route domain of the `address` you want to use.  This value cannot be modified after it is set. |
| **spanning**  boolean | Enables all BIG-IP systems in a device group to listen for and process traffic on the same virtual address.  Spanning for a virtual address occurs when you enable the `spanning` option on a device, and then sync the virtual address to the other members of the device group.  Spanning also relies on the upstream router to distribute application flows to the BIG-IP systems using ECMP routes. ECMP defines a route to the virtual address using distinct Floating self-IP addresses configured on each BIG-IP system.  You must also configure MAC masquerade addresses and disable `arp` on the virtual address when Spanning is enabled.  When creating a new virtual address, if this parameter is not specified, the default valus is `no`.  Choices:   - `false` - `true` |
| **state**  string | The virtual address state. If `absent`, the system makes an attempt to delete the virtual address. This will only succeed if this virtual address is not in use by a virtual server. `present` creates the virtual address and enables it. If `enabled`, enables the virtual address if it exists. If `disabled`, creates the virtual address if needed, and sets the state to `disabled`.  Choices:   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` |
| **traffic_group**  string | The traffic group for the virtual address. When creating a new address, if this value is not specified, the default is `/Common/traffic-group-1`. |

## [Notes](bigip_virtual_address_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_virtual_address_module.md#id4)

```yaml+jinja
- name: Add virtual address
  bigip_virtual_address:
    state: present
    partition: Common
    address: 10.10.10.10
    provider:
      server: lb.mydomain.net
      user: admin
      password: secret
  delegate_to: localhost

- name: Enable route advertisement on the virtual address
  bigip_virtual_address:
    state: present
    address: 10.10.10.10
    route_advertisement: any
    provider:
      server: lb.mydomain.net
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_virtual_address_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address**  integer | The address of the virtual address.  Returned: created  Sample: `2345` |
| **arp**  boolean | The new way the virtual address handles ARP requests.  Returned: changed  Sample: `true` |
| **auto_delete**  boolean | New setting for auto deleting virtual address.  Returned: changed  Sample: `true` |
| **availability_calculation**  string | Specifies which routes of the virtual address the system advertises.  Returned: changed  Sample: `"always"` |
| **connection_limit**  integer | The new connection limit of the virtual address.  Returned: changed  Sample: `1000` |
| **icmp_echo**  string | New ICMP echo setting applied to virtual address.  Returned: changed  Sample: `"disabled"` |
| **netmask**  integer | The netmask of the virtual address.  Returned: created  Sample: `2345` |
| **spanning**  string | Whether spanning is enabled or not.  Returned: changed  Sample: `"disabled"` |
| **state**  string | The new state of the virtual address.  Returned: changed  Sample: `"disabled"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
