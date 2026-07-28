---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_message_routing_peer module – Manage peers for routing generic message protocol messages"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_message_routing_peer_module.html
fetched_at: 2026-07-27T17:27:07+00:00
---
# f5networks.f5_modules.bigip_message_routing_peer module – Manage peers for routing generic message protocol messages

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_message_routing_peer`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_message_routing_peer_module.md#synopsis)
- [Parameters](bigip_message_routing_peer_module.md#parameters)
- [Notes](bigip_message_routing_peer_module.md#notes)
- [Examples](bigip_message_routing_peer_module.md#examples)
- [Return Values](bigip_message_routing_peer_module.md#return-values)

## [Synopsis](bigip_message_routing_peer_module.md#id1)

- Manage peers for routing generic message protocol messages.

## [Parameters](bigip_message_routing_peer_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_init**  boolean | If `yes`, the BIG-IP automatically creates outbound connections to the active pool members in the specified `pool` using the configuration of the specified `transport_config`.  For auto-initialization to attempt to create a connection, the peer must be included in a route that is attached to a router instance. For each router instance the peer is contained in, a connection is initiated.  The `auto_init` logic verifies at `auto_init_interval` if the a connection exists between the BIG-IP and the pool members of the pool. If a connection does not exist, it attempts to reestablish one.  Choices:   - `false` - `true` |
| **auto_init_interval**  integer | Specifies the interval at which attempts to initiate a connection occur.  The default value upon peer object creation, that is supplied by the system is `5000` milliseconds.  The accepted range is between 0 and 4294967295 inclusive. |
| **connection_mode**  string | Specifies how the number of connections per host are to be limited.  Choices:   - `"per-blade"` - `"per-client"` - `"per-peer"` - `"per-tmm"` |
| **description**  string | The user-defined description of the peer. |
| **name**  string / required | Specifies the name of the peer to manage. |
| **number_of_connections**  integer | Specifies the distribution of connections between the BIG-IP and a remote host.  The accepted range is between 0 and 65535 inclusive. |
| **partition**  string | Device partition to create peer object on.  Default: `"Common"` |
| **pool**  string | Specifies the name of the pool that messages are routed towards.  The specified pool must be on the same partition as the peer. |
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
| **ratio**  integer | Specifies the ratio to be used for selection of a peer within a list of peers in a LTM route.  The accepted range is between 0 and 4294967295 inclusive. |
| **state**  string | When `present`, ensures the peer exists.  When `absent`, ensures the peer is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **transport_config**  string | The name of the LTM virtual or LTM transport-config to use for creating an outgoing connection.  The resource must exist on the same partition as the peer object. |
| **type**  string | Parameter used to specify the type of the peer to manage.  Default setting is `generic` with more options coming.  Choices:   - `"generic"` ← (default) |

## [Notes](bigip_message_routing_peer_module.md#id3)

> **Note:**
>
> - Requires BIG-IP >= 14.0.0
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_message_routing_peer_module.md#id4)

```yaml+jinja
- name: Create a simple peer
  bigip_message_routing_peer:
    name: foobar
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create message routing peer with additional settings
  bigip_message_routing_peer:
    name: foobar
    connection_mode: per-blade
    pool: /baz/bar
    partition: baz
    transport_config: foovirtual
    ratio: 10
    auto_init: yes
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Modify message routing peer settings
  bigip_message_routing_peer:
    name: foobar
    partition: baz
    ratio: 20
    auto_init_interval: 2000
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove message routing peer
  bigip_message_routing_peer:
    name: foobar
    partition: baz
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_message_routing_peer_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **auto_init**  boolean | Enables creation of outbound connections to the active pool members.  Returned: changed  Sample: `true` |
| **auto_init_interval**  integer | The interval at which attempts to initiate a connection occur.  Returned: changed  Sample: `2000` |
| **connection_mode**  string | Specifies how the number of connections per host are to be limited.  Returned: changed  Sample: `"per-peer"` |
| **description**  string | The user defined description of the peer.  Returned: changed  Sample: `"Some description"` |
| **number_of_connections**  integer | The distribution of connections between the BIG-IP and a remote host.  Returned: changed  Sample: `2000` |
| **pool**  string | The name of the pool that messages are routed towards.  Returned: changed  Sample: `"/Bazbar/foobar"` |
| **ratio**  integer | The ratio to be used for selection of a peer within a list of peers in a LTM route.  Returned: changed  Sample: `500` |
| **transport_config**  string | The LTM virtual or LTM transport-config to use for creating an outgoing connection.  Returned: changed  Sample: `"/Common/foobar"` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
