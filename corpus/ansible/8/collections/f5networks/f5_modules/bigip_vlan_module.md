---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_vlan module – Manage VLANs on a BIG-IP system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_vlan_module.html
fetched_at: 2026-07-28T02:07:35+00:00
---
# f5networks.f5_modules.bigip_vlan module – Manage VLANs on a BIG-IP system

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_vlan`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_vlan_module.md#synopsis)
- [Parameters](bigip_vlan_module.md#parameters)
- [Notes](bigip_vlan_module.md#notes)
- [Examples](bigip_vlan_module.md#examples)
- [Return Values](bigip_vlan_module.md#return-values)

## [Synopsis](bigip_vlan_module.md#id1)

- Manage VLANs on a BIG-IP system

## [Parameters](bigip_vlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cmp_hash**  string | Specifies how the traffic on the VLAN is disaggregated. The value you select determines the traffic disaggregation method. You can choose to disaggregate traffic based on `source-address` (the source IP address), `destination-address` (destination IP address), or `default`, which specifies the default CMP hash uses L4 ports.  When creating a new VLAN, if this parameter is not specified, the default is `default`.  **Choices:**   - `"default"` - `"destination-address"` - `"source-address"` - `"dst-ip"` - `"src-ip"` - `"dest"` - `"destination"` - `"source"` - `"dst"` - `"src"` |
| **dag_round_robin**  boolean | Specifies whether some of the stateless traffic on the VLAN should be disaggregated in a round-robin order instead of using a static hash. The stateless traffic includes non-IP L2 traffic, ICMP, some UDP protocols, and so on.  When creating a new VLAN, if this parameter is not specified, the default is (false).  **Choices:**   - `false` - `true` |
| **dag_tunnel**  string | Specifies how the disaggregator (DAG) distributes received tunnel-encapsulated packets to TMM instances. Select `inner` to distribute packets based on information in inner headers. Select `outer` to distribute packets based on information in outer headers without inspecting inner headers.  When creating a new VLAN, if this parameter is not specified, the default is `outer`.  This parameter is not supported on Virtual Editions (VEs) of BIG-IP.  **Choices:**   - `"inner"` - `"outer"` |
| **description**  string | The description of the VLAN. |
| **fail_safe**  boolean | When `true`, specifies the VLAN takes the specified `fail_safe_action` if the system detects a loss of traffic on this VLAN’s interfaces.  **Choices:**   - `false` - `true` |
| **fail_safe_action**  string | Specifies the action the system takes when it does not detect any traffic on this VLAN, and the `fail_safe_timeout` has expired.  **Choices:**   - `"reboot"` - `"restart-all"` - `"failover"` |
| **fail_safe_timeout**  integer | Specifies the number of seconds a system can run without detecting network traffic on this VLAN before it takes the `fail_safe_action`. |
| **hw_syn_cookie**  boolean  *added in f5networks.f5_modules 1.3.0* | Enables hardware syncookie mode on a VLAN.  When `true`, the hardware per-VLAN SYN cookie protection is triggered when the certain traffic threshold is reached on supported platforms.  **Choices:**   - `false` - `true` |
| **interfaces**  list / elements=dictionary | Interfaces you want to add to the VLAN. This can include both tagged and untagged interfaces, as the `tagging` parameter specifies.  This parameter is mutually exclusive with the `untagged_interfaces` and `tagged_interfaces` parameters. |
| **interface**  string | The name of the interface |
| **tagging**  string | Whether the interface is `tagged` or `untagged`.  **Choices:**   - `"tagged"` - `"untagged"` |
| **mtu**  integer | Specifies the maximum transmission unit (MTU) for traffic on this VLAN. When creating a new VLAN, if this parameter is not specified, the default value used is `1500`.  This number must be between 576 to 9198. |
| **name**  string / required | The VLAN to manage. If the special VLAN `ALL` is specified with the `state` value of `absent`, all VLANs will be removed. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
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
| **sflow_poll_interval**  integer | Specifies the maximum interval in seconds between two pollings. |
| **sflow_sampling_rate**  integer | Specifies the ratio of packets observed to the samples generated. |
| **source_check**  boolean | When `true`, specifies the system verifies the return route to an initial packet is the same VLAN from which the packet originated.  The system performs this verification only if the `auto_last_hop` option is `false`.  **Choices:**   - `false` - `true` |
| **state**  string | The state of the VLAN on the system. When `present`, guarantees the VLAN exists with the provided attributes. When `absent`, removes the VLAN from the system.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tag**  integer | Tag number for the VLAN. The tag number can be any integer between 1 and 4094. The system automatically assigns a tag number if you do not specify a value. |
| **tagged_interfaces**  aliases: tagged_interface  list / elements=string | Specifies a list of tagged interfaces and trunks you want to configure for the VLAN. Use tagged interfaces or trunks when you want to assign a single interface or trunk to multiple VLANs.  This parameter is mutually exclusive with the `untagged_interfaces` and `interfaces` parameters. |
| **untagged_interfaces**  aliases: untagged_interface  list / elements=string | Specifies a list of untagged interfaces and trunks you want to configure for the VLAN.  This parameter is mutually exclusive with the `tagged_interfaces` and `interfaces` parameters. |

## [Notes](bigip_vlan_module.md#id3)

> **Note:**
>
> - Requires BIG-IP versions >= 12.0.0
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_vlan_module.md#id4)

```yaml+jinja
- name: Create VLAN
  bigip_vlan:
    name: net1
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Set VLAN tag
  bigip_vlan:
    name: net1
    tag: 2345
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Add VLAN 2345 as tagged to interface 1.1
  bigip_vlan:
    tagged_interface: 1.1
    name: net1
    tag: 2345
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Add VLAN 1234 as tagged to interfaces 1.1 and 1.2
  bigip_vlan:
    tagged_interfaces:
      - 1.1
      - 1.2
    name: net1
    tag: 1234
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

## [Return Values](bigip_vlan_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cmp_hash**  string | New traffic disaggregation method.  **Returned:** changed  **Sample:** `"source-address"` |
| **dag_tunnel**  string | The new DAG tunnel setting.  **Returned:** changed  **Sample:** `"outer"` |
| **description**  string | The description set on the VLAN.  **Returned:** changed  **Sample:** `"foo VLAN"` |
| **fail_safe**  boolean | The new Fail Safe setting.  **Returned:** changed  **Sample:** `false` |
| **fail_safe_action**  string | The new Fail Safe Action setting.  **Returned:** changed  **Sample:** `"reboot"` |
| **fail_safe_timeout**  integer | The new Fail Safe Timeout setting.  **Returned:** changed  **Sample:** `90` |
| **hw_syn_cookie**  boolean | Enables hardware syncookie mode on a VLAN.  **Returned:** changed  **Sample:** `false` |
| **interfaces**  list / elements=string | Interfaces the VLAN is assigned to.  **Returned:** changed  **Sample:** `["1.1", "1.2"]` |
| **partition**  string | The partition the VLAN was created on.  **Returned:** changed  **Sample:** `"Common"` |
| **sflow_poll_interval**  integer | The new sFlow Polling Interval setting.  **Returned:** changed  **Sample:** `10` |
| **sflow_sampling_rate**  integer | The new sFlow Sampling Rate setting.  **Returned:** changed  **Sample:** `20` |
| **source_check**  boolean | The new Source Check setting.  **Returned:** changed  **Sample:** `true` |
| **tag**  integer | The ID of the VLAN.  **Returned:** changed  **Sample:** `2345` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
