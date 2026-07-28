---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_gtm_server module – Manages F5 BIG-IP GTM servers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_gtm_server_module.html
fetched_at: 2026-07-27T17:26:54+00:00
---
# f5networks.f5_modules.bigip_gtm_server module – Manages F5 BIG-IP GTM servers

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_gtm_server`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_gtm_server_module.md#synopsis)
- [Parameters](bigip_gtm_server_module.md#parameters)
- [Notes](bigip_gtm_server_module.md#notes)
- [Examples](bigip_gtm_server_module.md#examples)
- [Return Values](bigip_gtm_server_module.md#return-values)

## [Synopsis](bigip_gtm_server_module.md#id1)

- Manage BIG-IP GTM (now BIG-IP DNS) server configuration. This module is able to manipulate the server definitions in a BIG-IP.

## [Parameters](bigip_gtm_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **availability_requirements**  dictionary | If you activate more than one health monitor, specifies the number of health monitors that must receive successful responses in order for the link to be considered available. |
| **at_least**  integer | Specifies the minimum number of active health monitors that must be successful before the link is considered up.  This parameter is only relevant when a `type` of `at_least` is used.  This parameter will be ignored if a type of either `all` or `require` is used. |
| **number_of_probers**  integer | Specifies the number of probers that should be used when running probes.  When creating a new virtual server, if this parameter is specified, the `number_of_probes` parameter must also be specified.  The value of this parameter should always be **higher** than, or **equal to**, the value of `number_of_probers`.  This parameter is only relevant when a `type` of `require` is used.  This parameter will be ignored if a type of either `all` or `at_least` is used. |
| **number_of_probes**  integer | Specifies the minimum number of probes that must succeed for this server to be declared up.  When creating a new virtual server, if this parameter is specified, then the `number_of_probers` parameter must also be specified.  The value of this parameter should always be **lower** than, or **equal to**, the value of `number_of_probers`.  This parameter is only relevant when a `type` of `require` is used.  This parameter will be ignored if a type of either `all` or `at_least` is used. |
| **type**  string / required | Monitor rule type when `monitors` is specified.  When creating a new pool, if this value is not specified, the default of **all** will be used.  Choices:   - `"all"` - `"at_least"` - `"require"` |
| **datacenter**  string | Data center to which the server belongs. When creating a new GTM server, this value is required. |
| **devices**  any | Lists the self IP addresses and translations for each device. When creating a new GTM server, this value is required. This list is a complex list that specifies a number of keys.  The `name` key specifies a name for the device. The device name must be unique per server. This key is required.  The `address` key contains an IP address, or list of IP addresses, for the destination server. This key is required.  The `translation` key contains an IP address to translate the `address` value above to. This key is optional.  Specifying duplicate `name` fields is a supported means of providing device addresses. In this scenario, the addresses will be assigned to the `name`‘s list of addresses. |
| **iquery_options**  dictionary | Specifies whether the Global Traffic Manager uses this BIG-IP system to conduct a variety of probes before delegating traffic to it. |
| **allow_path**  boolean | Specifies the system verifies the logical network route between a data center server and a local DNS server.  Choices:   - `false` - `true` |
| **allow_service_check**  boolean | Specifies the system verifies that an application on a server is running, by remotely running the application using an external service checker program.  Choices:   - `false` - `true` |
| **allow_snmp**  boolean | Specifies the system checks the performance of a server running an SNMP agent.  Choices:   - `false` - `true` |
| **limits**  dictionary | Specifies resource thresholds or limit requirements at the pool member level.  When you enable one or more limit settings, the system then uses that data to take members in and out of service.  You can define limits for any or all of the limit settings. However, when a member does not meet the resource threshold limit requirement, the system marks the member as unavailable and directs load balancing traffic to another resource. |
| **bits_enabled**  boolean | Whether the bits limit it enabled or not.  This parameter allows you to switch on or off the effect of the limit.  Choices:   - `false` - `true` |
| **bits_limit**  integer | Specifies the maximum allowable data throughput rate for the member, in bits per second.  If the network traffic volume exceeds this limit, the system marks the member as unavailable. |
| **connections_enabled**  boolean | Whether the current connections limit it enabled or not.  This parameter allows you to switch on or off the effect of the limit.  Choices:   - `false` - `true` |
| **connections_limit**  integer | Specifies the maximum number of concurrent connections, combined, for all of the members.  If the connections exceed this limit, the system marks the server as unavailable. |
| **cpu_enabled**  boolean | Whether the CPU limit it enabled or not.  This parameter allows you to switch on or off the effect of the limit.  Choices:   - `false` - `true` |
| **cpu_limit**  integer | Specifies the percent of CPU usage.  If percent of CPU usage goes above the limit, the system marks the server as unavailable. |
| **memory_enabled**  boolean | Whether the memory limit it enabled or not.  This parameter allows you to switch on or off the effect of the limit.  Choices:   - `false` - `true` |
| **memory_limit**  integer | Specifies the available memory required by the virtual servers on the server.  If available memory falls below this limit, the system marks the server as unavailable. |
| **packets_enabled**  boolean | Whether the packets limit it enabled or not.  This parameter allows you to switch on or off the effect of the limit.  Choices:   - `false` - `true` |
| **packets_limit**  integer | Specifies the maximum allowable data transfer rate for the member, in packets per second.  If the network traffic volume exceeds this limit, the system marks the member as unavailable. |
| **link_discovery**  string | Specifies whether the system auto-discovers the links for this server. When creating a new GTM server, if this parameter is not specified, the default value `disabled` is used.  If you set this parameter to `enabled` or `enabled-no-delete`, you must also ensure the `virtual_server_discovery` parameter is also set to `enabled` or `enabled-no-delete`.  Choices:   - `"enabled"` - `"disabled"` - `"enabled-no-delete"` |
| **monitors**  list / elements=string | Specifies the health monitors the system currently uses to monitor this resource.  When `availability_requirements.type` is `require`, you may only have a single monitor in the `monitors` list. |
| **name**  string / required | The name of the server.  If the virtual server is auto-discovered from the LTM,then the partition name needs to be included as part of the virtual server name when referencing from the module e.g. “/Common/vsname”. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **prober_fallback**  string | Specifies the type of prober to use to monitor this server’s resources when the preferred prober is not available.  This option is ignored in `TMOS` version `12.x`.  From `TMOS` version `13.x` and up, when prober_preference is set to `pool` a `prober_pool` parameter must be specified.  The choices are mutually exclusive with prober_preference parameter, with the exception of the `any-available` or `none` options.  Choices:   - `"any"` - `"inside-datacenter"` - `"outside-datacenter"` - `"inherit"` - `"pool"` - `"none"` |
| **prober_pool**  string | Specifies the name of the prober pool to use to monitor this server’s resources.  In `TMOS` version `13.x` and later, this parameter is mandatory when `prober_preference` is set to `pool`.  The format of the name can be either be prepended by partition (`/Common/foo`), or specified just as an object name (`foo`).  In `TMOS` version `12.x`, prober_pool can be set to an empty string to revert to default setting of `inherit`. |
| **prober_preference**  string | Specifies the type of prober to use to monitor this server’s resources.  This option is ignored in `TMOS` version `12.x`.  From `TMOS` version `13.x` and up, when prober_preference is set to `pool` a `prober_pool` parameter must be specified.  Choices:   - `"inside-datacenter"` - `"outside-datacenter"` - `"inherit"` - `"pool"` |
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
| **server_type**  aliases: product  string | Specifies the server type. The server type determines the metrics the system can collect from the server. When creating a new GTM server, the default value `bigip` is used.  Choices:   - `"alteon-ace-director"` - `"cisco-css"` - `"cisco-server-load-balancer"` - `"generic-host"` - `"radware-wsd"` - `"windows-nt-4.0"` - `"bigip"` - `"cisco-local-director-v2"` - `"extreme"` - `"generic-load-balancer"` - `"sun-solaris"` - `"cacheflow"` - `"cisco-local-director-v3"` - `"foundry-server-iron"` - `"netapp"` - `"windows-2000-server"` |
| **state**  string | The server state. If `absent`, the module attempts to delete the server. This will only succeed if this server is not in use by a virtual server. `present` creates the server and enables it. If `enabled`, enables the server if it exists. If `disabled`, creates the server if needed, and sets state to `disabled`.  Choices:   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` |
| **virtual_server_discovery**  string | Specifies whether the system auto-discovers the virtual servers for this server. When creating a new GTM server, if this parameter is not specified, the default value `disabled` is used.  Choices:   - `"enabled"` - `"disabled"` - `"enabled-no-delete"` |

## [Notes](bigip_gtm_server_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_gtm_server_module.md#id4)

```yaml+jinja
- name: Create server "GTM_Server"
  bigip_gtm_server:
    name: GTM_Server
    datacenter: /Common/New York
    server_type: bigip
    link_discovery: disabled
    virtual_server_discovery: disabled
    devices:
      - name: server_1
        address: 1.1.1.1
      - name: server_2
        address: 2.2.2.1
        translation: 192.168.2.1
      - name: server_2
        address: 2.2.2.2
      - name: server_3
        addresses:
          - address: 3.3.3.1
          - address: 3.3.3.2
      - name: server_4
        addresses:
          - address: 4.4.4.1
            translation: 192.168.14.1
          - address: 4.4.4.2
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Create server "GTM_Server" with expanded keys
  bigip_gtm_server:
    server: lb.mydomain.com
    user: admin
    password: secret
    name: GTM_Server
    datacenter: /Common/New York
    server_type: bigip
    link_discovery: disabled
    virtual_server_discovery: disabled
    devices:
      - name: server_1
        address: 1.1.1.1
      - name: server_2
        address: 2.2.2.1
        translation: 192.168.2.1
      - name: server_2
        address: 2.2.2.2
      - name: server_3
        addresses:
          - address: 3.3.3.1
          - address: 3.3.3.2
      - name: server_4
        addresses:
          - address: 4.4.4.1
            translation: 192.168.14.1
          - address: 4.4.4.2
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

## [Return Values](bigip_gtm_server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **bits_enabled**  boolean | Whether the bits limit is enabled.  Returned: changed  Sample: `true` |
| **bits_limit**  integer | The new bits_enabled limit.  Returned: changed  Sample: `100` |
| **connections_enabled**  boolean | Whether the connections limit is enabled.  Returned: changed  Sample: `true` |
| **connections_limit**  integer | The new connections_limit limit.  Returned: changed  Sample: `100` |
| **datacenter**  string | The new `datacenter` which the server is a part of.  Returned: changed  Sample: `"datacenter01"` |
| **link_discovery**  string | The new `link_discovery` configured on the remote device.  Returned: changed  Sample: `"enabled"` |
| **monitors**  list / elements=string | The new list of monitors for the resource.  Returned: changed  Sample: `["/Common/monitor1", "/Common/monitor2"]` |
| **packets_enabled**  boolean | Whether the packets limit is enabled.  Returned: changed  Sample: `true` |
| **packets_limit**  integer | The new packets_limit limit.  Returned: changed  Sample: `100` |
| **server_type**  string | The new type of the server.  Returned: changed  Sample: `"bigip"` |
| **virtual_server_discovery**  string | The new `virtual_server_discovery` name for the trap destination.  Returned: changed  Sample: `"disabled"` |

### Authors

- Robert Teller (@r-teller)
- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
