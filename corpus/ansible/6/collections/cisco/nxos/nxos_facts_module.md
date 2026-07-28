---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_facts module – Gets facts about NX-OS switches"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_facts_module.html
fetched_at: 2026-07-27T17:01:46+00:00
---
# cisco.nxos.nxos_facts module – Gets facts about NX-OS switches

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
> To use it in a playbook, specify: `cisco.nxos.nxos_facts`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_facts_module.md#synopsis)
- [Parameters](nxos_facts_module.md#parameters)
- [Notes](nxos_facts_module.md#notes)
- [Examples](nxos_facts_module.md#examples)
- [Return Values](nxos_facts_module.md#return-values)

## [Synopsis](nxos_facts_module.md#id1)

- Collects facts from Cisco Nexus devices running the NX-OS operating system. Fact collection is supported over both Cli and Nxapi transports. This module prepends all of the base network fact keys with `ansible_net_<fact>`. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **available_network_resources**  boolean | When ‘True’ a list of network resources for which resource modules are available will be provided.  Choices:   - `false` ← (default) - `true` |
| **gather_network_resources**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all and the resources like interfaces, vlans etc. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected. Valid subsets are `all`, `bfd_interfaces`, `lag_interfaces`, `telemetry`, `vlans`, `lacp`, `lacp_interfaces`, `interfaces`, `l3_interfaces`, `l2_interfaces`, `lldp_global`, `acls`, `acl_interfaces`, `ospfv2`, `ospfv3`, `ospf_interfaces`, `bgp_global`, `bgp_address_family`, `route_maps`, `prefix_lists`, `logging_global`, `ntp_global`, `snmp_server`. |
| **gather_subset**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include `all`, `hardware`, `config`, `legacy`, `interfaces`, and `min`. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected.  Default: `["min"]` |
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

## [Notes](nxos_facts_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_facts_module.md#id4)

```yaml+jinja
- name: Gather all legacy facts
  cisco.nxos.nxos_facts:
    gather_subset: all
- name: Gather only the config and default facts
  cisco.nxos.nxos_facts:
    gather_subset:
    - config
- name: Do not gather hardware facts
  cisco.nxos.nxos_facts:
    gather_subset:
    - '!hardware'
- name: Gather legacy and resource facts
  cisco.nxos.nxos_facts:
    gather_subset: all
    gather_network_resources: all
- name: Gather only the interfaces resource facts and no legacy facts
  cisco.nxos.nxos_facts:
    gather_subset:
    - '!all'
    - '!min'
    gather_network_resources:
    - interfaces
- name: Gather interfaces resource and minimal legacy facts
  cisco.nxos.nxos_facts:
    gather_subset: min
    gather_network_resources: interfaces
```

## [Return Values](nxos_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_net_all_ipv4_addresses**  list / elements=string | All IPv4 addresses configured on the device  Returned: when interfaces is configured |
| **ansible_net_all_ipv6_addresses**  list / elements=string | All IPv6 addresses configured on the device  Returned: when interfaces is configured |
| **ansible_net_api**  string | The name of the transport  Returned: always |
| **ansible_net_config**  string | The current active config from the device  Returned: when config is configured |
| **ansible_net_filesystems**  list / elements=string | All file system names available on the device  Returned: when hardware is configured |
| **ansible_net_gather_network_resources**  list / elements=string | The list of fact for network resource subsets collected from the device  Returned: when the resource is configured |
| **ansible_net_gather_subset**  list / elements=string | The list of fact subsets collected from the device  Returned: always |
| **ansible_net_hostname**  string | The configured hostname of the device  Returned: always |
| **ansible_net_image**  string | The image file the device is running  Returned: always |
| **ansible_net_interfaces**  dictionary | A hash of all interfaces running on the system  Returned: when interfaces is configured |
| **ansible_net_license_hostid**  string | The License host id of the device  Returned: always |
| **ansible_net_memfree_mb**  integer | The available free memory on the remote device in Mb  Returned: when hardware is configured |
| **ansible_net_memtotal_mb**  integer | The total memory on the remote device in Mb  Returned: when hardware is configured |
| **ansible_net_model**  string | The model name returned from the device  Returned: always |
| **ansible_net_neighbors**  dictionary | The list of LLDP and CDP neighbors from the device. If both, CDP and LLDP neighbor data is present on one port, CDP is preferred.  Returned: when interfaces is configured |
| **ansible_net_python_version**  string | The Python version Ansible controller is using  Returned: always |
| **ansible_net_serialnum**  string | The serial number of the remote device  Returned: always |
| **ansible_net_version**  string | The operating system version running on the remote device  Returned: always |
| **fan_info**  dictionary | A hash of facts about fans in the remote device  Returned: when legacy is configured |
| **hostname**  dictionary | The configured hostname of the remote device  Returned: when legacy is configured |
| **interfaces_list**  dictionary | The list of interface names on the remote device  Returned: when legacy is configured |
| **kickstart**  string | The software version used to boot the system  Returned: when legacy is configured |
| **module**  dictionary | A hash of facts about the modules in a remote device  Returned: when legacy is configured |
| **platform**  string | The hardware platform reported by the remote device  Returned: when legacy is configured |
| **power_supply_info**  string | A hash of facts about the power supplies in the remote device  Returned: when legacy is configured |
| **vlan_list**  list / elements=string | The list of VLAN IDs configured on the remote device  Returned: when legacy is configured |

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
