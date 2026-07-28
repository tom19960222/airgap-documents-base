---
collection: ansible
version: "6"
title: "cisco.iosxr.iosxr_facts module – Module to collect facts from remote devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/iosxr_facts_module.html
fetched_at: 2026-07-27T16:55:41+00:00
---
# cisco.iosxr.iosxr_facts module – Module to collect facts from remote devices.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/cisco/iosxr) (version 3.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_facts`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_facts_module.md#synopsis)
- [Parameters](iosxr_facts_module.md#parameters)
- [Notes](iosxr_facts_module.md#notes)
- [Examples](iosxr_facts_module.md#examples)
- [Return Values](iosxr_facts_module.md#return-values)

## [Synopsis](iosxr_facts_module.md#id1)

- Collects facts from network devices running the iosxr operating system. This module places the facts gathered in the fact tree keyed by the respective resource name. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## [Parameters](iosxr_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **available_network_resources**  boolean | When ‘True’ a list of network resources for which resource modules are available will be provided.  Choices:   - `false` ← (default) - `true` |
| **gather_network_resources**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all and the resources like interfaces, lacp etc. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected. Valid subsets are ‘all’, ‘lacp’, ‘lacp_interfaces’, ‘lldp_global’, ‘lldp_interfaces’, ‘interfaces’, ‘l2_interfaces’, ‘l3_interfaces’, ‘lag_interfaces’, ‘acls’, ‘acl_interfaces’, ‘static_routes’, ‘ospfv2’. |
| **gather_subset**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all, hardware, config, and interfaces. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected.  Default: `["min"]` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Specifies the type of connection based transport.  Choices:   - `"cli"` ← (default) - `"netconf"` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](iosxr_facts_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](iosxr_facts_module.md#id4)

```yaml+jinja
# Gather all facts
- cisco.iosxr.iosxr_facts:
    gather_subset: all
    gather_network_resources: all

# Collect only the config and default facts
- cisco.iosxr.iosxr_facts:
    gather_subset:
    - config

# Do not collect hardware facts
- cisco.iosxr.iosxr_facts:
    gather_subset:
    - '!hardware'

# Collect only the lacp facts
- cisco.iosxr.iosxr_facts:
    gather_subset:
    - '!all'
    - '!min'
    gather_network_resources:
    - lacp

# Do not collect lacp_interfaces facts
- cisco.iosxr.iosxr_facts:
    gather_network_resources:
    - '!lacp_interfaces'

# Collect lacp and minimal default facts
- cisco.iosxr.iosxr_facts:
    gather_subset: min
    gather_network_resources: lacp

# Collect only the interfaces facts
- cisco.iosxr.iosxr_facts:
    gather_subset:
    - '!all'
    - '!min'
    gather_network_resources:
    - interfaces
    - l2_interfaces
```

## [Return Values](iosxr_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_net_all_ipv4_addresses**  list / elements=string | All IPv4 addresses configured on the device  Returned: when interfaces is configured |
| **ansible_net_all_ipv6_addresses**  list / elements=string | All IPv6 addresses configured on the device  Returned: when interfaces is configured |
| **ansible_net_api**  string | The name of the transport  Returned: always |
| **ansible_net_config**  string | The current active config from the device  Returned: when config is configured |
| **ansible_net_filesystems**  list / elements=string | All file system names available on the device  Returned: when hardware is configured |
| **ansible_net_gather_network_resources**  list / elements=string | The list of fact resource subsets collected from the device  Returned: always |
| **ansible_net_gather_subset**  list / elements=string | The list of fact subsets collected from the device  Returned: always |
| **ansible_net_hostname**  string | The configured hostname of the device  Returned: always |
| **ansible_net_image**  string | The image file the device is running  Returned: always |
| **ansible_net_interfaces**  dictionary | A hash of all interfaces running on the system  Returned: when interfaces is configured |
| **ansible_net_memfree_mb**  integer | The available free memory on the remote device in Mb  Returned: when hardware is configured |
| **ansible_net_memtotal_mb**  integer | The total memory on the remote device in Mb  Returned: when hardware is configured |
| **ansible_net_model**  string | The model name returned from the device  Returned: always |
| **ansible_net_neighbors**  dictionary | The list of LLDP neighbors from the remote device  Returned: when interfaces is configured |
| **ansible_net_python_version**  string | The Python version Ansible controller is using  Returned: always |
| **ansible_net_version**  string | The operating system version running on the remote device  Returned: always |

### Authors

- Ricardo Carrillo Cruz (@rcarrillocruz)
- Nilashish Chakraborty (@Nilashishc)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
