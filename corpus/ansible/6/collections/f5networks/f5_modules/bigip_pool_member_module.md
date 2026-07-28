---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_pool_member module – Manages F5 BIG-IP LTM pool members"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_pool_member_module.html
fetched_at: 2026-07-27T17:27:26+00:00
---
# f5networks.f5_modules.bigip_pool_member module – Manages F5 BIG-IP LTM pool members

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_pool_member`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_pool_member_module.md#synopsis)
- [Parameters](bigip_pool_member_module.md#parameters)
- [Notes](bigip_pool_member_module.md#notes)
- [Examples](bigip_pool_member_module.md#examples)
- [Return Values](bigip_pool_member_module.md#return-values)

## [Synopsis](bigip_pool_member_module.md#id1)

- Manages F5 BIG-IP LTM pool members via the REST API.

## [Parameters](bigip_pool_member_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  aliases: ip, host  string | IP address of the pool member. This can be either IPv4 or IPv6. When creating a new pool member, one of either `address` or `fqdn` must be provided. This parameter cannot be updated after it is set. |
| **aggregate**  aliases: members  list / elements=dictionary | List of pool member definitions to be created, modified, or removed.  When using `aggregates`, if one of the aggregate definitions is invalid, the aggregate run will fail, indicating the error it last encountered.  The module will **NOT** rollback any changes it has made prior to encountering the error.  The module also will not indicate what changes were made prior to failure. Therefore we strong advise you run the module in `check` mode to ensure basic validation prior to executing this module. |
| **availability_requirements**  dictionary | If you activate more than one health monitor, specifies the number of health monitors that must receive successful responses in order for the link to be considered available.  Specifying an empty string will remove the monitors and revert to inheriting from the pool (default).  Specifying `none` will remove any health monitoring from the member completely. |
| **at_least**  integer | Specifies the minimum number of active health monitors that must be successful before the link is considered up.  This parameter is only relevant when a `type` of `at_least` is used.  This parameter will be ignored if a type of `all` is used. |
| **type**  string / required | Monitor rule type when `monitors` is specified.  When creating a new pool, if this value is not specified, the default of `all` will be used.  Choices:   - `"all"` - `"at_least"` |
| **connection_limit**  integer | Pool member connection limit. Setting this to `0` disables the limit. |
| **description**  string | Pool member description. |
| **fqdn**  aliases: hostname  string | FQDN name of the pool member. This can be any name that is a valid RFC 1123 DNS name. Therefore, the only usable characters are “A” to “Z”, “a” to “z”, “0” to “9”, the hyphen (“-”) and the period (“.”).  FQDN names must include at least one period; delineating the host from the domain. For example, `host.domain`.  FQDN names must end with a letter or a number.  When creating a new pool member, one of either `address` or `fqdn` must be provided. This parameter cannot be updated after it is set. |
| **fqdn_auto_populate**  boolean | Specifies whether the system automatically creates ephemeral nodes using the IP addresses returned by the resolution of a DNS query for a node defined by an FQDN.  When `yes`, the system generates an ephemeral node for each IP address returned in response to a DNS query for the FQDN of the node. Additionally, when a DNS response indicates the IP address of an ephemeral node no longer exists, the system deletes the ephemeral node.  When `no`, the system resolves a DNS query for the FQDN of the node with the single IP address associated with the FQDN.  When creating a new pool member, the default for this parameter is `yes`.  Once set this parameter cannot be changed afterwards.  This parameter is ignored when `reuse_nodes` is `yes`.  Choices:   - `false` - `true` |
| **ip_encapsulation**  string | Specifies the IP encapsulation using either IPIP (IP encapsulation within IP, RFC 2003) or GRE (Generic Router Encapsulation, RFC 2784) on outbound packets (from BIG-IP system to server-pool member).  When `none`, disables IP encapsulation.  When `inherit`, inherits the IP encapsulation setting from the member’s pool.  When any other value, the options are None, Inherit from Pool, and Member Specific. |
| **monitors**  list / elements=string | Specifies the health monitors the system currently uses to monitor this resource. |
| **name**  string | Name of the node to create or re-use when creating a new pool member.  While this parameter is optional, we recommend specifying this parameter at all times to mitigate anyunexpected behavior.  If not specified, a node name is created automatically from either the specified `address` or `fqdn`.  The `enabled` state is an alias of `present`. |
| **partition**  string | Partition to manage resources on.  Default: `"Common"` |
| **pool**  string / required | Pool name. This pool must exist. |
| **port**  integer | Pool member port.  This value cannot be changed after it has been set.  Parameter must be provided when using aggregates. |
| **preserve_node**  boolean | When state is `absent`, the system attempts to remove the node the pool member references.  The node will not be removed if it is still referenced by other pool members. If this happens, the module will not raise an error.  Setting this to `yes` disables this behavior.  Choices:   - `false` - `true` |
| **priority_group**  integer | Specifies a number representing the priority group for the pool member.  When adding a new member, the default is `0`, meaning the member has no priority.  To specify a priority, you must activate priority group usage when you create a new pool or when adding or removing pool members. When activated, the system load balances traffic according to the priority group number assigned to the pool member.  The higher the number, the higher the priority. So a member with a priority of 3 has higher priority than a member with a priority of 1. |
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
| **rate_limit**  integer | Pool member rate limit (connections-per-second). Setting this to `0` disables the limit. |
| **ratio**  integer | Pool member ratio weight. Valid values range from 1 through 100. New pool members – unless overridden with this value – default to 1. |
| **replace_all_with**  aliases: purge  boolean | Removes members not defined in the `aggregate` parameter.  This operation is all or none, meaning it will stop if there are some pool members that cannot be removed.  Choices:   - `false` ← (default) - `true` |
| **reuse_nodes**  boolean | Reuses node definitions if requested.  Choices:   - `false` - `true` ← (default) |
| **state**  string | Pool member state.  Choices:   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` - `"forced_offline"` |

## [Notes](bigip_pool_member_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_pool_member_module.md#id4)

```yaml+jinja
- name: Add pool member
  bigip_pool_member:
    pool: my-pool
    partition: Common
    name: my-member
    host: "{{ ansible_default_ipv4['address'] }}"
    port: 80
    description: web server
    connection_limit: 100
    rate_limit: 50
    ratio: 2
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Modify pool member ratio and description
  bigip_pool_member:
    pool: my-pool
    partition: Common
    name: my-member
    host: "{{ ansible_default_ipv4['address'] }}"
    port: 80
    ratio: 1
    description: nginx server
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Remove pool member from pool
  bigip_pool_member:
    state: absent
    pool: my-pool
    partition: Common
    name: my-member
    host: "{{ ansible_default_ipv4['address'] }}"
    port: 80
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Force pool member offline
  bigip_pool_member:
    state: forced_offline
    pool: my-pool
    partition: Common
    name: my-member
    host: "{{ ansible_default_ipv4['address'] }}"
    port: 80
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Create members with priority groups
  bigip_pool_member:
    pool: my-pool
    partition: Common
    host: "{{ item.address }}"
    name: "{{ item.name }}"
    priority_group: "{{ item.priority_group }}"
    port: 80
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
  loop:
    - address: 1.1.1.1
      name: web1
      priority_group: 4
    - address: 2.2.2.2
      name: web2
      priority_group: 3
    - address: 3.3.3.3
      name: web3
      priority_group: 2
    - address: 4.4.4.4
      name: web4
      priority_group: 1

- name: Add pool members aggregate
  bigip_pool_member:
    pool: my-pool
    aggregate:
      - host: 192.168.1.1
        partition: Common
        port: 80
        description: web server
        connection_limit: 100
        rate_limit: 50
        ratio: 2
      - host: 192.168.1.2
        partition: Common
        port: 80
        description: web server
        connection_limit: 100
        rate_limit: 50
        ratio: 2
      - host: 192.168.1.3
        partition: Common
        port: 80
        description: web server
        connection_limit: 100
        rate_limit: 50
        ratio: 2
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add pool members aggregate, remove non aggregates
  bigip_pool_member:
    pool: my-pool
    aggregate:
      - host: 192.168.1.1
        partition: Common
        port: 80
        description: web server
        connection_limit: 100
        rate_limit: 50
        ratio: 2
      - host: 192.168.1.2
        partition: Common
        port: 80
        description: web server
        connection_limit: 100
        rate_limit: 50
        ratio: 2
      - host: 192.168.1.3
        partition: Common
        port: 80
        description: web server
        connection_limit: 100
        rate_limit: 50
        ratio: 2
    replace_all_with: yes
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_pool_member_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address**  string | The address of the pool member.  Returned: changed  Sample: `"1.2.3.4"` |
| **connection_limit**  integer | The new connection limit of the pool member.  Returned: changed  Sample: `1000` |
| **description**  string | The new description of pool member.  Returned: changed  Sample: `"My pool member"` |
| **fqdn**  string | The FQDN of the pool member.  Returned: changed  Sample: `"foo.bar.com"` |
| **fqdn_auto_populate**  boolean | Whether FQDN auto population was set on the member or not.  Returned: changed  Sample: `true` |
| **monitors**  list / elements=string | The new list of monitors for the resource.  Returned: changed  Sample: `["/Common/monitor1", "/Common/monitor2"]` |
| **priority_group**  integer | The new priority group.  Returned: changed  Sample: `3` |
| **rate_limit**  integer | The new rate limit, in connections per second, of the pool member.  Returned: changed  Sample: `100` |
| **ratio**  integer | The new pool member ratio weight.  Returned: changed  Sample: `50` |
| **replace_all_with**  boolean | Purges all non-aggregate pool members from device.  Returned: changed  Sample: `true` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
