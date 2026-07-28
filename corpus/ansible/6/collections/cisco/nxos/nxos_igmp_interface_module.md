---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_igmp_interface module – Manages IGMP interface configuration."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_igmp_interface_module.html
fetched_at: 2026-07-27T17:01:53+00:00
---
# cisco.nxos.nxos_igmp_interface module – Manages IGMP interface configuration.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/cisco/nxos) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_igmp_interface`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_igmp_interface_module.md#synopsis)
- [Parameters](nxos_igmp_interface_module.md#parameters)
- [Notes](nxos_igmp_interface_module.md#notes)
- [Examples](nxos_igmp_interface_module.md#examples)
- [Return Values](nxos_igmp_interface_module.md#return-values)

## [Synopsis](nxos_igmp_interface_module.md#id1)

- Manages IGMP interface configuration settings.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_igmp_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **group_timeout**  string | Sets the group membership timeout for IGMPv2. Values can range from 3 to 65,535 seconds or keyword ‘default’. The default is 260 seconds. |
| **immediate_leave**  boolean | Enables the device to remove the group entry from the multicast routing table immediately upon receiving a leave message for the group. Use this command to minimize the leave latency of IGMPv2 group memberships on a given IGMP interface because the device does not send group-specific queries. The default is disabled.  Choices:   - `false` - `true` |
| **interface**  string / required | The full interface name for IGMP configuration. e.g. *Ethernet1/2*. |
| **last_member_qrt**  string | Sets the query interval waited after sending membership reports before the software deletes the group state. Values can range from 1 to 25 seconds or keyword ‘default’. The default is 1 second. |
| **last_member_query_count**  string | Sets the number of times that the software sends an IGMP query in response to a host leave message. Values can range from 1 to 5 or keyword ‘default’. The default is 2. |
| **oif_ps**  any | Configure prefixes and sources for static outgoing interface (OIF). This is a list of dict where each dict has source and prefix defined or just prefix if source is not needed. The specified values will be configured on the device and if any previous prefix/sources exist, they will be removed. Keyword ‘default’ is also accepted which removes all existing prefix/sources. |
| **oif_routemap**  string | Configure a routemap for static outgoing interface (OIF) or keyword ‘default’. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  Starting with Ansible 2.6 we recommend using `connection: httpapi` for NX-API.  This option will be removed in a release after 2022-06-01.  For more information please see the <https://docs.ansible.com/ansible/latest/network/user_guide/platform_nxos.html>.   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This is a common argument used for either *cli* or *nxapi* transports. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. This value applies to either *cli* or *nxapi*. The port value will default to the appropriate transport common port if none is provided in the task. (cli=22, http=80, https=443). |
| **ssh_keyfile**  string | Specifies the SSH key to use to authenticate the connection to the remote device. This argument is only used for the *cli* transport. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc). |
| **transport**  string | Configures the transport connection to use when connecting to the remote device. The transport argument supports connectivity to the device over cli (ssh) or nxapi.  Choices:   - `"cli"` ← (default) - `"nxapi"` |
| **use_proxy**  boolean | If `no`, the environment variables `http_proxy` and `https_proxy` will be ignored.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | Configures the *transport* to use SSL if set to `yes` only when the `transport=nxapi`, otherwise this value is ignored.  Choices:   - `false` ← (default) - `true` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates. If the transport argument is not nxapi, this value is ignored.  Choices:   - `false` ← (default) - `true` |
| **querier_timeout**  string | Sets the querier timeout that the software uses when deciding to take over as the querier. Values can range from 1 to 65535 seconds or keyword ‘default’. The default is 255 seconds. |
| **query_interval**  string | Sets the frequency at which the software sends IGMP host query messages. Values can range from 1 to 18000 seconds or keyword ‘default’. The default is 125 seconds. |
| **query_mrt**  string | Sets the response time advertised in IGMP queries. Values can range from 1 to 25 seconds or keyword ‘default’. The default is 10 seconds. |
| **report_llg**  boolean | Configures report-link-local-groups. Enables sending reports for groups in 224.0.0.0/24. Reports are always sent for nonlink local groups. By default, reports are not sent for link local groups.  Choices:   - `false` - `true` |
| **restart**  boolean | Restart IGMP. This is NOT idempotent as this is action only.  Choices:   - `false` ← (default) - `true` |
| **robustness**  string | Sets the robustness variable. Values can range from 1 to 7 or keyword ‘default’. The default is 2. |
| **startup_query_count**  string | Query count used when the IGMP process starts up. The range is from 1 to 10 or keyword ‘default’. The default is 2. |
| **startup_query_interval**  string | Query interval used when the IGMP process starts up. The range is from 1 to 18000 or keyword ‘default’. The default is 31. |
| **state**  string | Manages desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` - `"default"` |
| **version**  string | IGMP version. It can be 2 or 3 or keyword ‘default’.  Choices:   - `"2"` - `"3"` - `"default"` |

## [Notes](nxos_igmp_interface_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - When `state=default`, supported params will be reset to a default state. These include `version`, `startup_query_interval`, `startup_query_count`, `robustness`, `querier_timeout`, `query_mrt`, `query_interval`, `last_member_qrt`, `last_member_query_count`, `group_timeout`, `report_llg`, and `immediate_leave`.
> - When `state=absent`, all configs for `oif_ps`, and `oif_routemap` will be removed.
> - PIM must be enabled to use this module.
> - This module is for Layer 3 interfaces.
> - Route-map check not performed (same as CLI) check when configuring route-map with ‘static-oif’
> - If restart is set to true with other params set, the restart will happen last, i.e. after the configuration takes place. However, ‘restart’ itself is not idempotent as it is an action and not configuration.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_igmp_interface_module.md#id4)

```yaml+jinja
- cisco.nxos.nxos_igmp_interface:
    interface: ethernet1/32
    startup_query_interval: 30
    oif_ps:
    - {prefix: 238.2.2.6}
    - {source: 192.168.0.1, prefix: 238.2.2.5}
    state: present
```

## [Return Values](nxos_igmp_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of igmp interface configuration after module execution  Returned: always  Sample: `{"oif_ps": [{"prefix": "238.2.2.6"}, {"prefix": "238.2.2.5", "source": "192.168.0.1"}], "startup_query_count": "30"}` |
| **existing**  dictionary | k/v pairs of existing igmp_interface configuration  Returned: always  Sample: `{"oif_ps": [], "startup_query_count": "2"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"oif_ps": [{"prefix": "238.2.2.6"}, {"prefix": "238.2.2.5", "source": "192.168.0.1"}], "startup_query_count": "30"}` |
| **updates**  list / elements=string | commands sent to the device  Returned: always  Sample: `["interface Ethernet1/32", "ip igmp startup-query-count 30", "ip igmp static-oif 238.2.2.6", "ip igmp static-oif 238.2.2.5 source 192.168.0.1"]` |

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
