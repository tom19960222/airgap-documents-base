---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_network_globals module – Manage network global settings on BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_network_globals_module.html
fetched_at: 2026-07-27T17:27:21+00:00
---
# f5networks.f5_modules.bigip_network_globals module – Manage network global settings on BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_network_globals`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_network_globals_module.md#synopsis)
- [Parameters](bigip_network_globals_module.md#parameters)
- [Notes](bigip_network_globals_module.md#notes)
- [Examples](bigip_network_globals_module.md#examples)
- [Return Values](bigip_network_globals_module.md#return-values)

## [Synopsis](bigip_network_globals_module.md#id1)

- Module to manage STP, Multicast, DAG, LLDP and Self Allow global settings on a BIG-IP.

## [Parameters](bigip_network_globals_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dag**  dictionary | Manage global disaggregation settings. |
| **dag_ipv6_prefix_len**  integer | Specifies whether SPDAG or IPv6 prefix DAG should be used to disaggregate IPv6 traffic when vlan cmp hash is set to `src-ip` or `dst-ip`.  The valid value range is 0 - 128, with `128` value SPAG is in use.  This option is only available in TMOS version `13.x` and above. |
| **icmp_hash**  string | Specifies the ICMP hash for ICMP echo request and ICMP echo reply in SW DAG.  When `icmp`, ICMP echo request and ICMP echo reply are disaggregated based on ICMP id.  When `ipicmp`, ICMP echo request and ICMP echo reply are disaggregated based on ICMP id and IP addresses.  This option is only available in `TMOS` version `13.x` and above.  Choices:   - `"icmp"` - `"ipicmp"` |
| **round_robin_mode**  string | Specifies whether the round robin disaggregator (DAG) on a blade can disaggregate packets to all the TMMs in the system or only to the TMMs local to the blade.  When `global`, the DAG will disaggregate packets to all TMMs in the system.  When `local`, the DAG will disaggregate packets only to the TMMs local to the blade.  Choices:   - `"global"` - `"local"` |
| **lldp**  dictionary | Manage LLDP configuration options. |
| **enabled**  boolean | Specifies the current status of LLDP.  When `yes`, the LLDP is enabled globally on the device.  When `no`, the LLDP is disabled globally on the device.  Choices:   - `false` - `true` |
| **max_neighbors_per_port**  integer | Specifies the maximum number of neighbors per port.  The valid value range is 0 - 65535. |
| **reinit_delay**  integer | Specifies the maximum number of seconds to wait after reaching the TTL interval before resetting TTL timer.  The valid value range is 0 - 65535. |
| **tx_delay**  integer | Specifies the number of seconds to wait for LLDP to initialize on an interface before sending LLDP message.  The valid value range is 0 - 65535. |
| **tx_hold**  integer | Specifies the multiplier that determines the LLDP Time to Live (TTL). TTL is determined by multiplying this value and `tx_interval`.  The valid value range is 0 - 65535. |
| **tx_interval**  integer | Specifies the interval devices use to send LLDP information from each of their interfaces.  The valid value range is 0 - 65535. |
| **multicast**  dictionary | Manage multicast traffic configuration options. |
| **max_pending_packets**  integer | Specifies the maximum number of packet queued on behalf of a single incomplete MFC entry.  The valid range is 0 - 4294967295. |
| **max_pending_routes**  integer | Specifies the number of incomplete MFC entries each TMM will allow to exist at one time.  The valid range is 0 - 4294967295. |
| **rate_limit**  boolean | When `yes`, the DB variable `switchboard.maxmcastrate` setting controls the multicast packet per second rate limiting in the switch.  Choices:   - `false` - `true` |
| **route_lookup_timeout**  integer | Specifies maximum lifetime of an incomplete MFC entry, in seconds.  The valid range is 0 - 4294967295. |
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
| **self_allow**  dictionary  added in f5networks.f5_modules 1.1.0 | Manage Self Allow global configuration options. |
| **all**  boolean | Sets **all** or **none** ports and protocols as a system wide `self_allow` setting.  When `yes`, the self_allow allows all protocols and ports. This is the equivalent of setting **all** option in `TMSH`.  When `no`, the self_allow allows no protocols and ports. This is the equivalent of setting **none** option in `TMSH`.  Choices:   - `false` - `true` |
| **defaults**  list / elements=dictionary | The default set of protocols and ports allowed by a self IP if the self IP allow-service setting is **default**. |
| **port**  integer | The port number to be set.  The valid value range is 0 - 65535. |
| **protocol**  string | The protocol name to be set. |
| **stp**  dictionary | Manage global settings for STP on BIG-IP. |
| **config_name**  string | Specifies the configuration name. The accepted length is from 1 to 32 characters.  Only has effect when the `mode` is `mstp`. |
| **config_revision**  integer | Specifies the revision level of the MSTP configuration, when `mode` is `mstp`.  You must specify a number in the range of 0 to 65535. |
| **description**  string | User-defined description. |
| **fwd_delay**  integer | The number of seconds for which an interface was blocked from forwarding network traffic after a reconfiguration of the spanning tree topology. This parameter has no effect when `rstp` or `mstp` modes are used, as long as all bridges in the spanning tree use the RSTP or MSTP protocol.  If any legacy STP bridges are present, neighboring bridges must fall back to the old protocol, whose reconfiguration time is affected by the forward delay value.  The valid range is 4 to 30. |
| **hello_time**  integer | Specifies the time interval in seconds between the periodic transmissions that communicate spanning tree information to the adjacent bridges in the network.  The hello time set by default on the device is optimal in virtually all cases. F5 recommends that you do not change the hello time.  The valid range is 1 to 10. |
| **max_age**  integer | Specifies the number of seconds for which spanning tree information received from other bridges is considered valid.  The valid range is 6 to 40 seconds. |
| **max_hops**  integer | Specifies the maximum number of hops an MSTP packet may travel before it is discarded.  This option only takes effect when `mode` is `mstp`.  The number of hops must be in the range of 1 to 255. |
| **mode**  string | Specifies the spanning tree mode.  The `mstp`, `rstp` and `stp` options are only supported on hardware platforms. Attempting to set these modes on VE type platforms will result in failure. The only valid options on VE type platforms are: `passthru` and `disabled`.  Choices:   - `"disabled"` - `"mstp"` - `"passthru"` - `"rstp"` - `"stp"` |
| **transmit_hold**  integer | Specifies the absolute limit on the number of spanning tree protocol packets the traffic management system may transmit on a port in any hello time interval.  The valid range is 1 to 10 packets. |

## [Notes](bigip_network_globals_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_network_globals_module.md#id4)

```yaml+jinja
- name: Update STP settings
  bigip_network_globals:
    stp:
      config_name: foobar
      config_revision: 1
      max_hops: 20
      mode: mstp
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Update DAG settings
  bigip_network_globals:
    dag:
      icmp_hash: ipicmp
      round_robin_mode: local
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Update multiple settings
  bigip_network_globals:
    stp:
      config_name: foobar
      config_revision: 1
      max_hops: 20
      mode: mstp
    dag:
      icmp_hash: ipicmp
      round_robin_mode: local
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_network_globals_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dag**  complex | Manage multicast traffic configuration options.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **dag_ipv6_prefix_len**  integer | Specifies whether SPDAG or IPv6 prefix DAG should be used to disaggregate IPv6 traffic.  Returned: changed  Sample: `128` |
| **icmp_hash**  string | Specifies the ICMP hash for the ICMP echo request and ICMP echo reply in SW DAG.  Returned: changed  Sample: `"ipicmp"` |
| **round_robin_mode**  string | The mode of operation of the DAG on a blade.  Returned: changed  Sample: `"local"` |
| **lldp**  complex | Manage multicast traffic configuration options.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **enabled**  boolean | The current status of LLDP.  Returned: changed  Sample: `true` |
| **max_neighbors_per_port**  integer | The maximum number of neighbors per port.  Returned: changed  Sample: `128` |
| **reinit_delay**  integer | The maximum number of seconds to wait before resetting the TTL timer after reaching the TTL interval.  Returned: changed  Sample: `30` |
| **tx_delay**  integer | The number of seconds to wait for LLDP to initialize on an interface before sending LLDP message.  Returned: changed  Sample: `500` |
| **tx_hold**  integer | The multiplier that determines the LLDP Time to Live.  Returned: changed  Sample: `10` |
| **tx_interval**  integer | The interval devices use to send LLDP information from each of their interfaces.  Returned: changed  Sample: `240` |
| **multicast**  complex | Manage multicast traffic configuration options.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **max_pending_packets**  integer | The maximum number of packet queued on behalf of a single incomplete MFC entry.  Returned: changed  Sample: `3000` |
| **max_pending_routes**  integer | The number of incomplete MFC entries each TMM will allow to exist at one time.  Returned: changed  Sample: `50` |
| **rate_limit**  boolean | Enables DB variable control over multicast packet per second rate limiting in the switch.  Returned: changed  Sample: `true` |
| **route_lookup_timeout**  integer | The maximum lifetime of an incomplete MFC entry, in seconds.  Returned: changed  Sample: `20` |
| **self_allow**  complex | Manages self_allow system wide settings.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **all**  boolean | Allows all or none ports and protocols as a system wide self_allow setting.  Returned: changed  Sample: `true` |
| **defaults**  complex | The default set of protocols and ports allowed by a self IP.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **port**  integer | The port number to be set.  Returned: changed  Sample: `443` |
| **protocol**  string | The protocol name to be set.  Returned: changed  Sample: `"tcp"` |
| **stp**  complex | Manage global settings for STP on BIG-IP.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **config_name**  string | The configuration name.  Returned: changed  Sample: `"foobar"` |
| **config_revision**  integer | The revision level of the MSTP configuration.  Returned: changed  Sample: `2` |
| **description**  string | User-defined description.  Returned: changed  Sample: `"My description"` |
| **fwd_delay**  integer | The number of seconds for which an interface was blocked from forwarding network traffic.  Returned: changed  Sample: `4` |
| **hello_time**  integer | The time interval at seconds between the periodic transmissions of spanning tree information.  Returned: changed  Sample: `2` |
| **max_age**  integer | The number of seconds that spanning tree information received from other bridges is considered valid.  Returned: changed  Sample: `30` |
| **max_hops**  integer | The maximum number of hops an MSTP packet may travel before it is discarded.  Returned: changed  Sample: `15` |
| **mode**  string | The spanning tree mode.  Returned: changed  Sample: `"mstp"` |
| **transmit_hold**  integer | The limit on the number of STP the traffic management system may transmit on a port in any hello time interval.  Returned: changed  Sample: `5` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
