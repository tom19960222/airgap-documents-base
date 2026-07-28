---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_gtm_pool module – Manages F5 BIG-IP GTM pools"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_gtm_pool_module.html
fetched_at: 2026-07-27T17:26:53+00:00
---
# f5networks.f5_modules.bigip_gtm_pool module – Manages F5 BIG-IP GTM pools

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_gtm_pool`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_gtm_pool_module.md#synopsis)
- [Parameters](bigip_gtm_pool_module.md#parameters)
- [Notes](bigip_gtm_pool_module.md#notes)
- [Examples](bigip_gtm_pool_module.md#examples)
- [Return Values](bigip_gtm_pool_module.md#return-values)

## [Synopsis](bigip_gtm_pool_module.md#id1)

- Manages F5 BIG-IP GTM (now BIG-IP DNS) pools.

## [Parameters](bigip_gtm_pool_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **alternate_lb_method**  string | The load balancing mode the system tries if the `preferred_lb_method` is unsuccessful in picking a pool.  Choices:   - `"round-robin"` - `"return-to-dns"` - `"none"` - `"ratio"` - `"topology"` - `"static-persistence"` - `"global-availability"` - `"virtual-server-capacity"` - `"packet-rate"` - `"drop-packet"` - `"fallback-ip"` - `"virtual-server-score"` |
| **availability_requirements**  dictionary | If you activate more than one health monitor, specifies the number of health monitors that must receive successful responses in order for the link to be considered available. |
| **at_least**  integer | Specifies the minimum number of active health monitors that must be successful before the link is considered up.  This parameter is only relevant when a `type` of `at_least` is used.  This parameter will be ignored if a type of either `all` or `require` is used. |
| **number_of_probers**  integer | Specifies the number of probers that should be used when running probes.  When creating a new virtual server, if this parameter is specified, the `number_of_probes` parameter must also be specified.  The value of this parameter should always be **higher** than, or **equal to**, the value of `number_of_probers`.  This parameter is only relevant when a `type` of `require` is used.  This parameter will be ignored if a type of either `all` or `at_least` is used. |
| **number_of_probes**  integer | Specifies the minimum number of probes that must succeed for this server to be declared up.  When creating a new virtual server, if this parameter is specified, the `number_of_probers` parameter must also be specified.  The value of this parameter should always be **lower** than, or **equal to**, the value of `number_of_probers`.  This parameter is only relevant when a `type` of `require` is used.  This parameter will be ignored if a type of either `all` or `at_least` is used. |
| **type**  string / required | Monitor rule type when `monitors` is specified.  When creating a new pool, if this value is not specified, the default of ‘all’ will be used.  Choices:   - `"all"` - `"at_least"` - `"require"` |
| **fallback_ip**  string | Specifies the IPv4 or IPv6 address of the server to which the system directs requests when it cannot use one of its pools to do so. Note that the system uses the fallback IP only if you select the `fallback_ip` load balancing method. |
| **fallback_lb_method**  string | The load balancing mode the system tries if both the `preferred_lb_method` and `alternate_lb_method`s are unsuccessful in picking a pool.  Choices:   - `"round-robin"` - `"return-to-dns"` - `"ratio"` - `"topology"` - `"static-persistence"` - `"global-availability"` - `"virtual-server-capacity"` - `"least-connections"` - `"lowest-round-trip-time"` - `"fewest-hops"` - `"packet-rate"` - `"cpu"` - `"completion-rate"` - `"quality-of-service"` - `"kilobytes-per-second"` - `"drop-packet"` - `"fallback-ip"` - `"virtual-server-score"` - `"none"` |
| **max_answers_returned**  integer | Specifies the maximum number of available virtual servers the system lists in a response.  The maximum is 500. |
| **members**  list / elements=dictionary | Members to assign to the pool.  The order of the members in this list is the order they will be listed in the pool. |
| **server**  string / required | Name of the server which the pool member is a part of. |
| **virtual_server**  string / required | Name of the virtual server, associated with the server, the pool member is a part of. |
| **monitors**  list / elements=string | Specifies the health monitors the system currently uses to monitor this resource.  When `availability_requirements.type` is `require`, you may only have a single monitor in the `monitors` list. |
| **name**  string / required | Name of the GTM pool. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **preferred_lb_method**  string | The load balancing mode the system tries first.  Choices:   - `"round-robin"` - `"return-to-dns"` - `"ratio"` - `"topology"` - `"static-persistence"` - `"global-availability"` - `"virtual-server-capacity"` - `"least-connections"` - `"lowest-round-trip-time"` - `"fewest-hops"` - `"packet-rate"` - `"cpu"` - `"completion-rate"` - `"quality-of-service"` - `"kilobytes-per-second"` - `"drop-packet"` - `"fallback-ip"` - `"virtual-server-score"` |
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
| **state**  string | Pool state. When `present`, ensures the pool is created and enabled. When `absent`, ensures the pool is removed from the system. When `enabled` or `disabled`, ensures the pool is enabled or disabled (respectively) on the remote device.  Choices:   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` |
| **ttl**  integer | Specifies the number of seconds the IP address, once found, is valid. |
| **type**  string / required | The type of GTM pool you want to create.  Choices:   - `"a"` - `"aaaa"` - `"cname"` - `"mx"` - `"naptr"` - `"srv"` |

## [Notes](bigip_gtm_pool_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_gtm_pool_module.md#id4)

```yaml+jinja
- name: Create a GTM pool
  bigip_gtm_pool:
    name: my_pool
    type: a
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Disable pool
  bigip_gtm_pool:
    state: disabled
    name: my_pool
    type: a
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

## [Return Values](bigip_gtm_pool_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **alternate_lb_method**  string | New alternate load balancing method for the pool.  Returned: changed  Sample: `"drop-packet"` |
| **fallback_ip**  string | New fallback IP used when load balacing using the `fallback_ip` method.  Returned: changed  Sample: `"10.10.10.10"` |
| **fallback_lb_method**  string | New fallback load balancing method for the pool.  Returned: changed  Sample: `"fewest-hops"` |
| **max_answers_returned**  integer | The new Maximum Answers Returned value.  Returned: changed  Sample: `25` |
| **members**  complex | List of members in the pool.  Returned: changed |
| **server**  string | The name of the server portion of the member.  Returned: changed |
| **virtual_server**  string | The name of the virtual server portion of the member.  Returned: changed |
| **monitors**  list / elements=string | The new list of monitors for the resource.  Returned: changed  Sample: `["/Common/monitor1", "/Common/monitor2"]` |
| **preferred_lb_method**  string | New preferred load balancing method for the pool.  Returned: changed  Sample: `"topology"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
