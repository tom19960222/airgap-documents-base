---
collection: ansible
version: "6"
title: "cisco.ios.ios_facts module – Module to collect facts from remote devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_facts_module.html
fetched_at: 2026-07-27T16:42:56+00:00
---
# cisco.ios.ios_facts module – Module to collect facts from remote devices.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/cisco/ios) (version 3.3.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_facts`.

New in cisco.ios 1.0.0

- [Synopsis](ios_facts_module.md#synopsis)
- [Parameters](ios_facts_module.md#parameters)
- [Notes](ios_facts_module.md#notes)
- [Examples](ios_facts_module.md#examples)
- [Return Values](ios_facts_module.md#return-values)

## [Synopsis](ios_facts_module.md#id1)

- Collects a base set of device facts from a remote device that is running IOS. This module prepends all of the base network fact keys with `ansible_net_<fact>`. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](ios_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **available_network_resources**  boolean | When ‘True’ a list of network resources for which resource modules are available will be provided.  Choices:   - `false` ← (default) - `true` |
| **gather_network_resources**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all and the resources like interfaces, vlans etc. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected. Valid subsets are ‘bgp_global’, ‘l3_interfaces’, ‘lag_interfaces’, ‘ntp_global’, ‘acls’, ‘hostname’, ‘interfaces’, ‘lldp_interfaces’, ‘logging_global’, ‘ospf_interfaces’, ‘ospfv2’, ‘prefix_lists’, ‘static_routes’, ‘acl_interfaces’, ‘all’, ‘bgp_address_family’, ‘l2_interfaces’, ‘lacp’, ‘lacp_interfaces’, ‘lldp_global’, ‘ospfv3’, ‘snmp_server’, ‘vlans’. |
| **gather_subset**  list / elements=string | When supplied, this argument restricts the facts collected to a given subset.  Possible values for this argument include `all`, `min`, `hardware`, `config`, and `interfaces`.  Specify a list of values to include a larger subset.  Use a value with an initial `!` to collect all facts except that subset.  Default: `["min"]` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>.   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](ios_facts_module.md#id3)

> **Note:**
>
> - Tested against IOS 15.6
> - Facts gathering for L3 devices are supposed to produce blank output for unsupported resources like vlan.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](ios_facts_module.md#id4)

```yaml+jinja
- name: Gather all legacy facts
  cisco.ios.ios_facts:
    gather_subset: all

- name: Gather only the config and default facts
  cisco.ios.ios_facts:
    gather_subset:
    - config

- name: Do not gather hardware facts
  cisco.ios.ios_facts:
    gather_subset:
    - '!hardware'

- name: Gather legacy and resource facts
  cisco.ios.ios_facts:
    gather_subset: all
    gather_network_resources: all

- name: Gather only the interfaces resource facts and no legacy facts
  cisco.ios.ios_facts:
    gather_subset:
    - '!all'
    - '!min'
    gather_network_resources:
    - interfaces

- name: Gather interfaces resource and minimal legacy facts
  cisco.ios.ios_facts:
    gather_subset: min
    gather_network_resources: interfaces

- name: Gather L2 interfaces resource and minimal legacy facts
  cisco.ios.ios_facts:
    gather_subset: min
    gather_network_resources: l2_interfaces

- name: Gather L3 interfaces resource and minimal legacy facts
  cisco.ios.ios_facts:
    gather_subset: min
    gather_network_resources: l3_interfaces
```

## [Return Values](ios_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_net_all_ipv4_addresses**  list / elements=string | All IPv4 addresses configured on the device  Returned: when interfaces is configured |
| **ansible_net_all_ipv6_addresses**  list / elements=string | All IPv6 addresses configured on the device  Returned: when interfaces is configured |
| **ansible_net_api**  string | The name of the transport  Returned: always |
| **ansible_net_config**  string | The current active config from the device  Returned: when config is configured |
| **ansible_net_filesystems**  list / elements=string | All file system names available on the device  Returned: when hardware is configured |
| **ansible_net_filesystems_info**  dictionary | A hash of all file systems containing info about each file system (e.g. free and total space)  Returned: when hardware is configured |
| **ansible_net_gather_network_resources**  list / elements=string | The list of fact for network resource subsets collected from the device  Returned: when the resource is configured |
| **ansible_net_gather_subset**  list / elements=string | The list of fact subsets collected from the device  Returned: always |
| **ansible_net_hostname**  string | The configured hostname of the device  Returned: always |
| **ansible_net_image**  string | The image file the device is running  Returned: always |
| **ansible_net_interfaces**  dictionary | A hash of all interfaces running on the system  Returned: when interfaces is configured |
| **ansible_net_iostype**  string | The operating system type (IOS or IOS-XE) running on the remote device  Returned: always |
| **ansible_net_memfree_mb**  integer | The available free memory on the remote device in Mb  Returned: when hardware is configured |
| **ansible_net_memtotal_mb**  integer | The total memory on the remote device in Mb  Returned: when hardware is configured |
| **ansible_net_model**  string | The model name returned from the device  Returned: always |
| **ansible_net_neighbors**  dictionary | The list of CDP and LLDP neighbors from the remote device. If both, CDP and LLDP neighbor data is present on one port, CDP is preferred.  Returned: when interfaces is configured |
| **ansible_net_python_version**  string | The Python version Ansible controller is using  Returned: always |
| **ansible_net_serialnum**  string | The serial number of the remote device  Returned: always |
| **ansible_net_stacked_models**  list / elements=string | The model names of each device in the stack  Returned: when multiple devices are configured in a stack |
| **ansible_net_stacked_serialnums**  list / elements=string | The serial numbers of each device in the stack  Returned: when multiple devices are configured in a stack |
| **ansible_net_version**  string | The operating system version running on the remote device  Returned: always |

### Authors

- Peter Sprygada (@privateip)
- Sumit Jaiswal (@justjais)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
