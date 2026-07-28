---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_gtm_virtual_server module – Manages F5 BIG-IP GTM virtual servers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_gtm_virtual_server_module.html
fetched_at: 2026-07-27T17:26:56+00:00
---
# f5networks.f5_modules.bigip_gtm_virtual_server module – Manages F5 BIG-IP GTM virtual servers

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_gtm_virtual_server`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_gtm_virtual_server_module.md#synopsis)
- [Parameters](bigip_gtm_virtual_server_module.md#parameters)
- [Notes](bigip_gtm_virtual_server_module.md#notes)
- [Examples](bigip_gtm_virtual_server_module.md#examples)
- [Return Values](bigip_gtm_virtual_server_module.md#return-values)

## [Synopsis](bigip_gtm_virtual_server_module.md#id1)

- Manages F5 BIG-IP GTM (now BIG-IP DNS) virtual servers. A GTM server can have many virtual servers associated with it. They are arranged in much the same way that pool members are to pools.

## [Parameters](bigip_gtm_virtual_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string | Specifies the IP Address of the virtual server.  When creating a new GTM virtual server, this parameter is required. |
| **availability_requirements**  dictionary | If you activate more than one health monitor, specifies the number of health monitors that must receive successful responses in order for the link to be considered available. |
| **at_least**  integer | Specifies the minimum number of active health monitors that must be successful before the link is considered up.  This parameter is only relevant when a `type` of `at_least` is used.  This parameter will be ignored if a type of either `all` or `require` is used. |
| **number_of_probers**  integer | Specifies the number of probers that should be used when running probes.  When creating a new virtual server, if this parameter is specified, the `number_of_probes` parameter must also be specified.  The value of this parameter should always be **higher** than or **equal to** the value of `number_of_probers`.  This parameter is only relevant when a `type` of `require` is used.  This parameter will be ignored if a type of either `all` or `at_least` is used. |
| **number_of_probes**  integer | Specifies the minimum number of probes that must succeed for this server to be declared up.  When creating a new virtual server, if this parameter is specified, then the `number_of_probers` parameter must also be specified.  The value of this parameter should always be **lower** than or **equal to** the value of `number_of_probers`.  This parameter is only relevant when a `type` of `require` is used.  This parameter will be ignored if a type of either `all` or `at_least` is used. |
| **type**  string / required | Monitor rule type when `monitors` is specified.  When creating a new virtual, if this value is not specified, the default of `all` will be used.  Choices:   - `"all"` - `"at_least"` - `"require"` |
| **limits**  dictionary | Specifies resource thresholds or limit requirements at the server level.  When you enable one or more limit settings, the system then uses that data to take servers in and out of service.  You can define limits for any or all of the limit settings. However, when a server does not meet the resource threshold limit requirement, the system marks the entire server as unavailable and directs load balancing traffic to another resource.  The limit settings available depend on the type of server. |
| **bits_enabled**  boolean | Whether the bits limit is enabled or not.  This parameter allows you to switch on or off the effect of the limit.  Choices:   - `false` - `true` |
| **bits_limit**  integer | Specifies the maximum allowable data throughput rate for the virtual servers on the server, in bits per second.  If the network traffic volume exceeds this limit, the system marks the server as unavailable. |
| **connections_enabled**  boolean | Whether the current connections limit is enabled or not.  This parameter allows you to switch on or off the effect of the limit.  Choices:   - `false` - `true` |
| **connections_limit**  integer | Specifies the maximum number of concurrent connections, combined, for all of the virtual servers on the server.  If the connections exceed this limit, the system marks the server as unavailable. |
| **packets_enabled**  boolean | Whether the packets limit is enabled or not.  This parameter allows you to switch on or off the effect of the limit.  Choices:   - `false` - `true` |
| **packets_limit**  integer | Specifies the maximum allowable data transfer rate for the virtual servers on the server, in packets per second.  If the network traffic volume exceeds this limit, the system marks the server as unavailable. |
| **link**  string | Specifies a link to assign to the server or virtual server. |
| **monitors**  list / elements=string | Specifies the health monitors the system currently uses to monitor this resource.  When `availability_requirements.type` is `require`, you may only have a single monitor in the `monitors` list. |
| **name**  string / required | Specifies the name of the virtual server. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **port**  integer | Specifies the service port number for the virtual server or pool member. For example, the HTTP service is typically port 80.  To specify all ports, use an `*`.  When creating a new GTM virtual server, if this parameter is not specified, a default of `*` will be used. |
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
| **server_name**  string / required | Specifies the name of the server the virtual server is associated with. |
| **state**  string | When `present`, ensures the resource exists.  When `absent`, ensures the resource is removed.  Choices:   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` |
| **translation_address**  string | Specifies the translation IP address for the virtual server.  To unset this parameter, use an empty string (`""`) as a value.  When creating a new GTM virtual server, if this parameter is not specified, a default of `::` will be used. |
| **translation_port**  string | Specifies the translation port number or service name for the virtual server.  To specify all ports, use an `*`.  When creating a new GTM virtual server, if this parameter is not specified, a default of `*` will be used. |
| **virtual_server_dependencies**  list / elements=dictionary | Specifies the virtual servers on which the current virtual server depends.  If any of the specified servers are unavailable, the current virtual server is also listed as unavailable. |
| **server**  string / required | Server which the dependant virtual server is part of. |
| **virtual_server**  string / required | Virtual server to depend on. |

## [Notes](bigip_gtm_virtual_server_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_gtm_virtual_server_module.md#id4)

```yaml+jinja
- name: Enable virtual server
  bigip_gtm_virtual_server:
    server_name: server1
    name: my-virtual-server
    state: enabled
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

## [Return Values](bigip_gtm_virtual_server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address**  string | The new address of the resource.  Returned: changed  Sample: `"1.2.3.4"` |
| **availability_requirements**  dictionary | The new availability requirement configurations for the resource.  Returned: changed  Sample: `{"type": "all"}` |
| **limits**  dictionary | The new limit configurations for the resource.  Returned: changed  Sample: `{"bits_enabled": true, "bits_limit": 100}` |
| **link**  string | The new link value for the resource.  Returned: changed  Sample: `"/Common/my-link"` |
| **monitors**  list / elements=string | The new list of monitors for the resource.  Returned: changed  Sample: `["/Common/monitor1", "/Common/monitor2"]` |
| **port**  integer | The new port of the resource.  Returned: changed  Sample: `500` |
| **server_name**  string | The server name associated with the virtual server.  Returned: changed  Sample: `"/Common/my-gtm-server"` |
| **translation_address**  integer | The new translation address of the resource.  Returned: changed  Sample: `500` |
| **translation_port**  integer | The new translation port of the resource.  Returned: changed  Sample: `500` |
| **virtual_server_dependencies**  list / elements=string | The new list of virtual server dependencies for the resource.  Returned: changed  Sample: `["/Common/vs1", "/Common/vs2"]` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
