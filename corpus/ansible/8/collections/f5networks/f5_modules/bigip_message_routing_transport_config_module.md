---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_message_routing_transport_config module – Manages configuration for an outgoing connection"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_message_routing_transport_config_module.html
fetched_at: 2026-07-28T02:06:37+00:00
---
# f5networks.f5_modules.bigip_message_routing_transport_config module – Manages configuration for an outgoing connection

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_message_routing_transport_config`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_message_routing_transport_config_module.md#synopsis)
- [Parameters](bigip_message_routing_transport_config_module.md#parameters)
- [Notes](bigip_message_routing_transport_config_module.md#notes)
- [Examples](bigip_message_routing_transport_config_module.md#examples)
- [Return Values](bigip_message_routing_transport_config_module.md#return-values)

## [Synopsis](bigip_message_routing_transport_config_module.md#id1)

- Manages configuration for an outgoing connection in BIG-IP message routing.

## [Parameters](bigip_message_routing_transport_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | The user-defined description of the transport config. |
| **name**  string / required | Specifies the name of the transport config to manage. |
| **partition**  string | Device partition to create transport-config object on.  **Default:** `"Common"` |
| **profiles**  list / elements=string | Specifies a list of profiles for the outgoing connection to use to direct and manage traffic. |
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
| **rules**  list / elements=string | The iRules you want run on this transport config. iRules help automate the intercepting, processing, and routing of application traffic. |
| **src_addr_translation**  dictionary | Specifies the type of source address translation enabled for the transport config and the pool the source address translation will use. |
| **pool**  string | Specifies the name of a LSN or SNAT pool used by the specified transport config.  Name can also be specified in `fullPath` format: `/Common/foobar`.  When `type` is `none` or `automap`, the pool parameter will be replaced by `none` keyword, thus any defined `pool` parameter will be ignored. |
| **type**  string | Specifies the type of source address translation associated with the specified transport config.  When set to `snat`, the `pool` parameter needs to contain a name for a valid LSN or SNAT pool.  **Choices:**   - `"snat"` - `"none"` - `"automap"` |
| **src_port**  integer | Specifies the source port for the connection being created.  If no value is specified an ephemeral port is chosen for the connection being created.  The acceptable range is between 0 and 65535 inclusive. |
| **state**  string | When `present`, ensures the transport-config object exists.  When `absent`, ensures the transport-config object is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **type**  string | Parameter used to specify the type of transport-config object to manage.  Default setting is `generic` with more options coming.  **Choices:**   - `"generic"` ← (default) |

## [Notes](bigip_message_routing_transport_config_module.md#id3)

> **Note:**
>
> - Requires BIG-IP >= 14.0.0
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_message_routing_transport_config_module.md#id4)

```yaml+jinja
- name: Create generic transport config
  bigip_message_routing_transport_config:
    name: foo
    profiles:
      transport: genericmsg
      tcp: tcp-lan-optimized
    description: new_transport
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Modify generic transport config
  bigip_message_routing_transport_config:
    name: foo
    rules:
      - rule_1
      - rule_2
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove generic transport config
  bigip_message_routing_transport_config:
    name: foo
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_message_routing_transport_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | The user-defined description of the router profile.  **Returned:** changed  **Sample:** `"My description"` |
| **profiles**  list / elements=string | The profiles for the outgoing connection .  **Returned:** changed  **Sample:** `["/Common/profile1", "/Common/profile2"]` |
| **rules**  list / elements=string | The iRules running on transport config.  **Returned:** changed  **Sample:** `["/Common/rule1", "/Common/rule2"]` |
| **source_port**  integer | The source port for the connection being created.  **Returned:** changed  **Sample:** `10041` |
| **src_addr_translation**  complex | The type of source address translation enabled for the transport config.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **pool**  string | The name of a LSN or SNAT pool used by the specified transport config.  **Returned:** changed  **Sample:** `"/Common/pool1"` |
| **type**  string | the type of source address translation associated with the specified transport config.  **Returned:** changed  **Sample:** `"automap"` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
