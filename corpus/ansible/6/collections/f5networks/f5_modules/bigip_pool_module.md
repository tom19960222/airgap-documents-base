---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_pool module – Manages F5 BIG-IP LTM pools"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_pool_module.html
fetched_at: 2026-07-27T17:27:25+00:00
---
# f5networks.f5_modules.bigip_pool module – Manages F5 BIG-IP LTM pools

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_pool`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_pool_module.md#synopsis)
- [Parameters](bigip_pool_module.md#parameters)
- [Notes](bigip_pool_module.md#notes)
- [Examples](bigip_pool_module.md#examples)
- [Return Values](bigip_pool_module.md#return-values)

## [Synopsis](bigip_pool_module.md#id1)

- Manages F5 BIG-IP LTM pools via iControl REST API.

## [Parameters](bigip_pool_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  aliases: pools  list / elements=dictionary | List of pool definitions to be created, modified, or removed.  When using `aggregates`, if one of the aggregate definitions is invalid, the aggregate run will fail, indicating the error it last encountered.  The module will **NOT** rollback any changes it has made prior to encountering the error.  The module also will not indicate which changes were made prior to failure. Therefore we strongly advise you run the module in `check` mode to ensure basic validation prior to executing this module. |
| **description**  string | Specifies descriptive text that identifies the pool. |
| **lb_method**  string | Load balancing method. When creating a new pool, if this value is not specified, the default of `round-robin` is used.  Choices:   - `"dynamic-ratio-member"` - `"dynamic-ratio-node"` - `"fastest-app-response"` - `"fastest-node"` - `"least-connections-member"` - `"least-connections-node"` - `"least-sessions"` - `"observed-member"` - `"observed-node"` - `"predictive-member"` - `"predictive-node"` - `"ratio-least-connections-member"` - `"ratio-least-connections-node"` - `"ratio-member"` - `"ratio-node"` - `"ratio-session"` - `"round-robin"` - `"weighted-least-connections-member"` - `"weighted-least-connections-node"` |
| **metadata**  any | Arbitrary key/value pairs you can attach to a pool. This is useful in situations where you might want to annotate a pool to be managed by Ansible.  Key names are stored as strings; this includes names that are numbers.  Values for all of the keys are stored as strings; this includes values that are numbers.  Data will be persisted, not ephemeral. |
| **min_up_members**  integer | Specifies the minimum number of pool members that must be up,  otherwise, the system takes the action specified in the `min-up-members-action` option.  Use this option for gateway pools in a redundant system where a unit number is applied to the pool.  This indicates the pool is configured only on the specified unit.  When creating a new pool, if this parameter is not specified, the default is `0`. |
| **min_up_members_action**  string | Specifies the action to take if `min_up_members_checking` is `enabled` and the number of active pool members falls below the number specified in the `min_up_members` option.  When creating a new pool, if this parameter is not specified, the default is `failover`.  Choices:   - `"failover"` - `"reboot"` - `"restart-all"` |
| **min_up_members_checking**  string | Enables or disables the `min_up_members` feature.  If you enable this feature, you must also specify a value for both the `min_up_members` and `min_up_members_action` options.  When creating a new pool, if this parameter is not specified, the default is `disabled`.  Choices:   - `"enabled"` - `"disabled"` |
| **monitor_type**  aliases: availability_requirements_type  string | Monitor rule type when `monitors` is specified.  When creating a new pool, if this value is not specified, the default of `and_list` is used.  When `single`, ensures all specified monitors are checked, but additionally includes checks to make sure you only specified a single monitor.  When `and_list`, ensures **all** monitors are checked.  When `m_of_n`, ensures `quorum` of `monitors` are checked. `m_of_n` **requires** a `quorum` of 1 or greater be set either in the playbook, or already exist on the device.  Both `single` and `and_list` are functionally identical, as BIG-IP considers all monitors as “a list”.  Choices:   - `"and_list"` - `"m_of_n"` - `"single"` |
| **monitors**  list / elements=string | Monitor template name list. If the partition is not provided as part of the monitor name, the `partition` option is used instead. |
| **name**  aliases: pool  string | Pool name |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **priority_group_activation**  aliases: minimum_active_members  integer | Specifies whether the system load balances traffic according to the priority number assigned to the pool member.  When creating a new pool, if this parameter is not specified, the default of `0` is used.  To disable this setting, provide the value `0`.  Once you enable this setting, you can specify pool member priority when you create a new pool or on a pool member’s properties screen.  The system treats same-priority pool members as a group.  To enable priority group activation, provide a number from `0` to `65535` that represents the minimum number of members that must be available in one priority group before the system directs traffic to members in a lower priority group.  When a sufficient number of members become available in the higher priority group, the system again directs traffic to the higher priority group. |
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
| **quorum**  aliases: availability_requirements_at_least  integer | Monitor quorum value when `monitor_type` is `m_of_n`.  Quorum must be a value of 1 or greater when `monitor_type` is `m_of_n`. |
| **replace_all_with**  aliases: purge  boolean | Removes pools not defined in the `aggregate` parameter.  This operation is all or none, meaning it will stop if there are some pools that cannot be removed.  Choices:   - `false` ← (default) - `true` |
| **reselect_tries**  integer | Sets the number of times the system tries to contact a pool member after a passive failure. |
| **service_down_action**  string | Sets the action to take when node goes down in pool.  Choices:   - `"none"` - `"reset"` - `"drop"` - `"reselect"` |
| **slow_ramp_time**  integer | Sets the ramp-up time (in seconds) to gradually ramp up the load on newly added or freshly detected up pool members. |
| **state**  string | When `present`, guarantees the pool exists with the provided attributes.  When `absent`, removes the pool from the system.  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](bigip_pool_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_pool_module.md#id4)

```yaml+jinja
- name: Create pool
  bigip_pool:
    state: present
    name: my-pool
    partition: Common
    lb_method: least-connections-member
    slow_ramp_time: 120
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Modify load balancer method
  bigip_pool:
    state: present
    name: my-pool
    partition: Common
    lb_method: round-robin
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Set a single monitor (with enforcement)
  bigip_pool:
    state: present
    name: my-pool
    partition: Common
    monitor_type: single
    monitors:
      - http
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Set a single monitor (without enforcement)
  bigip_pool:
    state: present
    name: my-pool
    partition: Common
    monitors:
      - http
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Set multiple monitors (all must succeed)
  bigip_pool:
    state: present
    name: my-pool
    partition: Common
    monitor_type: and_list
    monitors:
      - http
      - tcp
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Set multiple monitors (at least 1 must succeed)
  bigip_pool:
    state: present
    name: my-pool
    partition: Common
    monitor_type: m_of_n
    quorum: 1
    monitors:
      - http
      - tcp
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Set multiple monitors (at least 2 must succeed)
  bigip_pool:
    state: present
    name: my-pool
    partition: Common
    availability_requirements_type: m_of_n
    availability_requirements_at_least: 2
    monitors:
      - http
      - tcp
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Delete pool
  bigip_pool:
    state: absent
    name: my-pool
    partition: Common
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add metadata to pool
  bigip_pool:
    state: present
    name: my-pool
    partition: Common
    metadata:
      ansible: 2.4
      updated_at: 2017-12-20T17:50:46Z
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add pools Aggregate
  bigip_pool:
    aggregate:
      - name: my-pool
        partition: Common
        lb_method: least-connections-member
        slow_ramp_time: 120
      - name: my-pool2
        partition: Common
        lb_method: least-sessions
        slow_ramp_time: 120
      - name: my-pool3
        partition: Common
        lb_method: round-robin
        slow_ramp_time: 120
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add pools Aggregate, purge others
  bigip_pool:
    aggregate:
      - name: my-pool
        partition: Common
        lb_method: least-connections-member
        slow_ramp_time: 120
      - name: my-pool2
        partition: Common
        lb_method: least-sessions
        slow_ramp_time: 120
      - name: my-pool3
        partition: Common
        lb_method: round-robin
        slow_ramp_time: 120
    replace_all_with: yes
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_pool_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | Description set on the pool.  Returned: changed  Sample: `"Pool of web servers"` |
| **lb_method**  string | The load balancing method set for the pool.  Returned: changed  Sample: `"round-robin"` |
| **metadata**  dictionary | The new value of the pool.  Returned: changed  Sample: `{"key1": "foo", "key2": "bar"}` |
| **monitor_type**  string | Changed value for the monitor_type of the pool.  Returned: changed  Sample: `"m_of_n"` |
| **monitors**  list / elements=string | Monitors set on the pool.  Returned: changed  Sample: `["/Common/http", "/Common/gateway_icmp"]` |
| **priority_group_activation**  integer | The new minimum number of members to activate the priority group.  Returned: changed  Sample: `10` |
| **quorum**  integer | The quorum that was set on the pool.  Returned: changed  Sample: `2` |
| **replace_all_with**  boolean | Purges all non-aggregate pools from device  Returned: changed  Sample: `true` |
| **reselect_tries**  integer | The new value set for the number of tries to contact member.  Returned: changed  Sample: `10` |
| **service_down_action**  string | Service down action that is set on the pool.  Returned: changed  Sample: `"reset"` |
| **slow_ramp_time**  integer | The new value set for the slow ramp-up time.  Returned: changed  Sample: `500` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
