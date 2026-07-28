---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_message_routing_route module – Manages static routes for routing message protocol messages"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_message_routing_route_module.html
fetched_at: 2026-07-28T02:06:36+00:00
---
# f5networks.f5_modules.bigip_message_routing_route module – Manages static routes for routing message protocol messages

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_message_routing_route`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_message_routing_route_module.md#synopsis)
- [Parameters](bigip_message_routing_route_module.md#parameters)
- [Notes](bigip_message_routing_route_module.md#notes)
- [Examples](bigip_message_routing_route_module.md#examples)
- [Return Values](bigip_message_routing_route_module.md#return-values)

## [Synopsis](bigip_message_routing_route_module.md#id1)

- Manages static routes for routing message protocol messages.

## [Parameters](bigip_message_routing_route_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | The user-defined description of the static route. |
| **dst_address**  string | Specifies the destination address of the route.  Setting the attribute to an empty string will create a wildcard matching all message destination-addresses, which is the default when creating a new route. |
| **name**  string / required | Specifies the name of the static route. |
| **partition**  string | Device partition to create route object on.  **Default:** `"Common"` |
| **peer_selection_mode**  string | Specifies the method to use when selecting a peer from the provided list of `peers`.  **Choices:**   - `"ratio"` - `"sequential"` |
| **peers**  list / elements=string | Specifies a list of ltm messagerouting-peer objects.  The specified peer must be on the same partition as the route. |
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
| **src_address**  string | Specifies the source address of the route.  Setting the attribute to an empty string will create a wildcard matching all message source-addresses, which is the default when creating a new route. |
| **state**  string | When `present`, ensures the route exists.  When `absent`, ensures the route is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **type**  string | Parameter used to specify the type of the route to manage.  Default setting is `generic` with more options coming.  **Choices:**   - `"generic"` ← (default) |

## [Notes](bigip_message_routing_route_module.md#id3)

> **Note:**
>
> - Requires BIG-IP >= 14.0.0
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_message_routing_route_module.md#id4)

```yaml+jinja
- name: Create a simple generic route
  bigip_message_routing_route:
    name: foobar
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Modify a generic route
  bigip_message_routing_route:
    name: foobar
    peers:
      - peer1
      - peer2
    peer_selection_mode: ratio
    src_address: annoying_user
    dst_address: blackhole
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove a generic
  bigip_message_routing_route:
    name: foobar
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_message_routing_route_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | The user-defined description of the route.  **Returned:** changed  **Sample:** `"Some description"` |
| **dst_address**  string | The destination address of the route.  **Returned:** changed  **Sample:** `"blackhole"` |
| **peer_selection_mode**  string | The method to use when selecting a peer.  **Returned:** changed  **Sample:** `"ratio"` |
| **peers**  list / elements=string | The list of ltm messagerouting-peer object.  **Returned:** changed  **Sample:** `["/Common/peer1", "/Common/peer2"]` |
| **src_address**  string | The source address of the route.  **Returned:** changed  **Sample:** `"annyoing_user"` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
