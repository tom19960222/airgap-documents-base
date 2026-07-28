---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_message_routing_router module – Manages router profiles for message-routing protocols"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_message_routing_router_module.html
fetched_at: 2026-07-27T17:27:09+00:00
---
# f5networks.f5_modules.bigip_message_routing_router module – Manages router profiles for message-routing protocols

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_message_routing_router`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_message_routing_router_module.md#synopsis)
- [Parameters](bigip_message_routing_router_module.md#parameters)
- [Notes](bigip_message_routing_router_module.md#notes)
- [Examples](bigip_message_routing_router_module.md#examples)
- [Return Values](bigip_message_routing_router_module.md#return-values)

## [Synopsis](bigip_message_routing_router_module.md#id1)

- Manages router profiles for message-routing protocols.

## [Parameters](bigip_message_routing_router_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | The user-defined description of the router profile. |
| **ignore_client_port**  boolean | When `yes`, the remote port on clientside connections (connections where the peer connected to the BIG-IP) is ignored when searching for an existing connection.  Choices:   - `false` - `true` |
| **inherited_traffic_group**  boolean | When set to `yes`, the `traffic_group` will be inherited from the containing folder. When not specified the system sets this to `no` when creating new router profile.  Choices:   - `false` - `true` |
| **max_pending_bytes**  integer | The maximum number of bytes worth of pending messages that will be held while waiting for a connection to a peer to be created. Once reached, any additional messages to the peer will be flagged as undeliverable and returned to the originator.  The accepted range is between 0 and 4294967295 inclusive. |
| **max_pending_messages**  integer | The maximum number of pending messages that will be held while waiting for a connection to a peer to be created. Once reached, any additional messages to the peer will be flagged as undeliverable and returned to the originator.  The accepted range is between 0 and 65535 inclusive. |
| **max_retries**  integer | Sets the maximum number of time a message may be resubmitted for rerouting by the `MR::retry` iRule command.  The accepted range is between 0 and 4294967295 inclusive. |
| **mirror**  boolean | Enables or disables state mirroring. State mirroring can be used to maintain the same state information in the standby unit that is in the active unit.  Choices:   - `false` - `true` |
| **mirrored_msg_sweeper_interval**  integer | Specifies the maximum time in milliseconds that a message will be held on the standby device as it waits for the active device to route the message.  Messages on the standby device held for longer than the configurable sweeper interval, will be dropped.  The acceptable range is between 0 and 4294967295 inclusive. |
| **name**  string / required | Specifies the name of the router profile. |
| **parent**  string | The parent template of this router profile. Once this value has been set, it cannot be changed.  The default values are set by the system if not specified and they correspond to the router type created, for example, `/Common/messagerouter` for `generic` `type` and so on. |
| **partition**  string | Device partition to create router profile on.  Default: `"Common"` |
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
| **routes**  list / elements=string | Specifies a list of static routes for the router instance to use.  The route must be on the same partition as router profile. |
| **state**  string | When `present`, ensures the router profile exists.  When `absent`, ensures the router profile is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **traffic_group**  string | Specifies the traffic-group of the router profile.  Setting the `traffic_group` to an empty string value `""` will cause the device to inherit from containing folder, which means the value of `inherited_traffic_group` on device will be `yes`. |
| **type**  string | Parameter used to specify the type of the router profile to manage.  Default setting is `generic` with more options coming.  Choices:   - `"generic"` ← (default) |
| **use_local_connection**  boolean | If `yes`, the router will route a message to an existing connection on the same TMM as the message was received.  Choices:   - `false` - `true` |

## [Notes](bigip_message_routing_router_module.md#id3)

> **Note:**
>
> - Requires BIG-IP >= 14.0.0
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_message_routing_router_module.md#id4)

```yaml+jinja
- name: Create a generic router profile
  bigip_message_routing_router:
    name: foo
    max_retries: 10
    ignore_client_port: yes
    routes:
      - /Common/route1
      - /Common/route2
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Modify a generic router profile
  bigip_message_routing_router:
    name: foo
    ignore_client_port: no
    mirror: yes
    mirrored_msg_sweeper_interval: 4000
    traffic_group: /Common/traffic-group-2
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove a generic router profile
  bigip_message_routing_router:
    name: foo
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_message_routing_router_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | The user-defined description of the router profile.  Returned: changed  Sample: `"My description"` |
| **ignore_client_port**  boolean | Enables ignoring of the remote port on clientside connections when searching for an existing connection.  Returned: changed  Sample: `false` |
| **inherited_traffic_group**  boolean | Specifies if a traffic-group should be inherited from containing folder.  Returned: changed  Sample: `true` |
| **max_pending_bytes**  integer | The maximum number of bytes worth of pending messages that will be held.  Returned: changed  Sample: `10000` |
| **max_pending_messages**  integer | The maximum number of pending messages that will be held.  Returned: changed  Sample: `64` |
| **max_retries**  integer | The maximum number of time a message may be resubmitted for rerouting.  Returned: changed  Sample: `10` |
| **mirror**  boolean | Enables or disables state mirroring.  Returned: changed  Sample: `true` |
| **mirrored_msg_sweeper_interval**  integer | The maximum time in milliseconds that a message will be held on the standby device.  Returned: changed  Sample: `2000` |
| **parent**  string | The parent template of this router profile.  Returned: changed  Sample: `"/Common/messagerouter"` |
| **routes**  list / elements=string | The list of static routes for the router instance to use.  Returned: changed  Sample: `["/Common/route1", "/Common/route2"]` |
| **traffic_group**  string | The traffic-group of the router profile.  Returned: changed  Sample: `"/Common/traffic-group-1"` |
| **use_local_connection**  boolean | Enables routing of messages to an existing connection on the same TMM as the message was received.  Returned: changed  Sample: `true` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
