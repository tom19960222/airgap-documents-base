---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_gtm_pool_member module – Manage GTM pool member settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_gtm_pool_member_module.html
fetched_at: 2026-07-28T02:06:20+00:00
---
# f5networks.f5_modules.bigip_gtm_pool_member module – Manage GTM pool member settings

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_gtm_pool_member`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_gtm_pool_member_module.md#synopsis)
- [Parameters](bigip_gtm_pool_member_module.md#parameters)
- [Notes](bigip_gtm_pool_member_module.md#notes)
- [Examples](bigip_gtm_pool_member_module.md#examples)
- [Return Values](bigip_gtm_pool_member_module.md#return-values)

## [Synopsis](bigip_gtm_pool_member_module.md#id1)

- Manages a variety of settings on GTM (now BIG-IP DNS) pool members. The settings that can be adjusted with this module are much more broad that what can be done in the `bigip_gtm_pool` module. The pool module is intended to allow you to adjust the member order in the pool, not the various settings of the members. The `bigip_gtm_pool_member` module should be used to adjust all of the other settings.

## [Parameters](bigip_gtm_pool_member_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  aliases: members  list / elements=dictionary | List of GTM pool member definitions to be created, modified, or removed.  When using `aggregates`, if one of the aggregate definitions is invalid, the aggregate run will fail, indicating the error it last encountered.  The module will `NOT` rollback any changes it has made prior to encountering the error.  The module also will not indicate what changes were made prior to failure, therefore we strongly advise you run the module in check mode to make basic validation, prior to module execution. |
| **description**  string | The description of the pool member. |
| **limits**  dictionary | Specifies resource thresholds or limit requirements at the pool member level.  When you enable one or more limit settings, the system then uses that data to take members in and out of service.  You can define limits for any or all of the limit settings. However, when a member does not meet the resource threshold limit requirement, the system marks the member as unavailable and directs load balancing traffic to another resource. |
| **bits_enabled**  boolean | Whether or not the bits limit is enabled.  **Choices:**   - `false` - `true` |
| **bits_limit**  integer | Specifies the maximum allowable data throughput rate for the member, in bits per second. |
| **connections_enabled**  boolean | Whether or not the current connections limit is enabled.  **Choices:**   - `false` - `true` |
| **connections_limit**  integer | Specifies the maximum number of concurrent connections, combined, for all of the members. |
| **packets_enabled**  boolean | Whether or not the packets limit is enabled.  **Choices:**   - `false` - `true` |
| **packets_limit**  integer | Specifies the maximum allowable data transfer rate for the member, in packets per second. |
| **member_order**  integer | Specifies the order in which the member will appear in the pool.  The system uses this number with load balancing methods that involve prioritizing pool members, such as the Ratio load balancing method. |
| **monitor**  string | Specifies the monitor assigned to this pool member.  Pool members only support a single monitor.  If the `port` of the `gtm_virtual_server` is `*`, the accepted values of this parameter will be affected.  If this parameter is not specified when creating a new pool member, the default of `default` will be used.  To remove the monitor from the pool member, use the value `none`. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **ratio**  integer | Specifies the weight of the pool member for load balancing purposes. |
| **server_name**  string | Specifies the GTM server which contains the `virtual_server`. |
| **state**  string | Pool member state. When `present`, ensures the pool member is created and enabled. When `absent`, ensures the pool member is removed from the system. When `enabled` or `disabled`, ensures the pool member is enabled or disabled (respectively) on the remote device.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` |
| **virtual_server**  string | Specifies the name of the GTM virtual server which is assigned to the specified `server`. |
| **description**  string | The description of the pool member. |
| **limits**  dictionary | Specifies resource thresholds or limit requirements at the pool member level.  When you enable one or more limit settings, the system then uses that data to take members in and out of service.  You can define limits for any or all of the limit settings. However, when a member does not meet the resource threshold limit requirement, the system marks the member as unavailable and directs load balancing traffic to another resource. |
| **bits_enabled**  boolean | Whether or not the bits limit is enabled.  **Choices:**   - `false` - `true` |
| **bits_limit**  integer | Specifies the maximum allowable data throughput rate for the member, in bits per second. |
| **connections_enabled**  boolean | Whether or not the current connections limit is enabled.  **Choices:**   - `false` - `true` |
| **connections_limit**  integer | Specifies the maximum number of concurrent connections, combined, for all of the members. |
| **packets_enabled**  boolean | Whether or not the packets limit is enabled.  **Choices:**   - `false` - `true` |
| **packets_limit**  integer | Specifies the maximum allowable data transfer rate for the member, in packets per second. |
| **member_order**  integer | Specifies the order in which the member will appear in the pool.  The system uses this number with load balancing methods that involve prioritizing pool members, such as the Ratio load balancing method. |
| **monitor**  string | Specifies the monitor assigned to this pool member.  Pool members only support a single monitor.  If the `port` of the `gtm_virtual_server` is `*`, the accepted values of this parameter will be affected.  If this parameter is not specified when creating a new pool member, the default of `default` will be used.  To remove the monitor from the pool member, use the value `none`. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **pool**  string / required | Name of the GTM pool.  For pools created on different partitions, you must specify partition of the pool in the full path format, for example, `/FooBar/pool_name`. |
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
| **ratio**  integer | Specifies the weight of the pool member for load balancing purposes. |
| **replace_all_with**  aliases: purge  boolean | Removes members not defined in the `aggregate` parameter.  This operation is all or none, meaning it will stop if there are some pool members that cannot be removed.  **Choices:**   - `false` ← (default) - `true` |
| **server_name**  string | Specifies the GTM server which contains the `virtual_server`. |
| **state**  string | Pool member state. When `present`, ensures the pool member is created and enabled. When `absent`, ensures the pool member is removed from the system. When `enabled` or `disabled`, ensures the pool member is enabled or disabled (respectively) on the remote device.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` |
| **type**  string / required | The type of GTM pool that the member is in.  **Choices:**   - `"a"` - `"aaaa"` - `"cname"` - `"mx"` - `"naptr"` - `"srv"` |
| **virtual_server**  string | Specifies the name of the GTM virtual server which is assigned to the specified `server`. |

## [Notes](bigip_gtm_pool_member_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_gtm_pool_member_module.md#id4)

```yaml+jinja
- name: Create a GTM pool member
  bigip_gtm_pool_member:
    pool: pool1
    server_name: server1
    virtual_server: vs1
    type: a
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create a GTM pool member different partition
  bigip_gtm_pool_member:
    server_name: /Common/foo_name
    virtual_server: GTMVSName
    type: a
    pool: /FooBar/foo-pool
    partition: Common
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Add GTM pool members aggregate
  bigip_gtm_pool_member:
    pool: pool1
    type: a
    aggregate:
      - server_name: server1
        virtual_server: vs1
        partition: Common
        description: web server1
        member_order: 0
      - server_name: server2
        virtual_server: vs2
        partition: Common
        description: web server2
        member_order: 1
      - server_name: server3
        virtual_server: vs3
        partition: Common
        description: web server3
        member_order: 2
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add GTM pool members aggregate, remove non aggregates
  bigip_gtm_pool_member:
    pool: pool1
    type: a
    aggregate:
      - server_name: server1
        virtual_server: vs1
        partition: Common
        description: web server1
        member_order: 0
      - server_name: server2
        virtual_server: vs2
        partition: Common
        description: web server2
        member_order: 1
      - server_name: server3
        virtual_server: vs3
        partition: Common
        description: web server3
        member_order: 2
    replace_all_with: true
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_gtm_pool_member_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **bits_enabled**  boolean | Whether the bits limit is enabled.  **Returned:** changed  **Sample:** `true` |
| **bits_limit**  integer | The new bits_enabled limit.  **Returned:** changed  **Sample:** `100` |
| **connections_enabled**  boolean | Whether the connections limit is enabled.  **Returned:** changed  **Sample:** `true` |
| **connections_limit**  integer | The new connections_limit limit.  **Returned:** changed  **Sample:** `100` |
| **description**  string | The new description of the member.  **Returned:** changed  **Sample:** `"My description"` |
| **disabled**  boolean | Whether the pool member is disabled or not.  **Returned:** changed  **Sample:** `true` |
| **enabled**  boolean | Whether the pool member is enabled or not.  **Returned:** changed  **Sample:** `true` |
| **member_order**  integer | The new order in which the member appears in the pool.  **Returned:** changed  **Sample:** `2` |
| **monitor**  string | The new monitor assigned to the pool member.  **Returned:** changed  **Sample:** `"/Common/monitor1"` |
| **packets_enabled**  boolean | Whether the packets limit is enabled.  **Returned:** changed  **Sample:** `true` |
| **packets_limit**  integer | The new packets_limit limit.  **Returned:** changed  **Sample:** `100` |
| **ratio**  integer | The new weight of the member for load balancing.  **Returned:** changed  **Sample:** `10` |
| **replace_all_with**  boolean | Purges all non-aggregate pool members from device  **Returned:** changed  **Sample:** `true` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
