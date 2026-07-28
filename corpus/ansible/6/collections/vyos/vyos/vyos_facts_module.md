---
collection: ansible
version: "6"
title: "vyos.vyos.vyos_facts module – Get facts about vyos devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/vyos/vyos/vyos_facts_module.html
fetched_at: 2026-07-27T16:42:56+00:00
---
# vyos.vyos.vyos_facts module – Get facts about vyos devices.

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/vyos/vyos) (version 3.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_facts`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_facts_module.md#synopsis)
- [Parameters](vyos_facts_module.md#parameters)
- [Notes](vyos_facts_module.md#notes)
- [Examples](vyos_facts_module.md#examples)
- [Return Values](vyos_facts_module.md#return-values)

## [Synopsis](vyos_facts_module.md#id1)

- Collects facts from network devices running the vyos operating system. This module places the facts gathered in the fact tree keyed by the respective resource name. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## [Parameters](vyos_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **available_network_resources**  boolean | When ‘True’ a list of network resources for which resource modules are available will be provided.  Choices:   - `false` ← (default) - `true` |
| **gather_network_resources**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all and the resources like interfaces. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected. Valid subsets are ‘all’, ‘interfaces’, ‘l3_interfaces’, ‘lag_interfaces’, ‘lldp_global’, ‘lldp_interfaces’, ‘static_routes’, ‘firewall_rules’, ‘firewall_global’, ‘firewall_interfaces’, ‘ospfv3’, ‘ospfv2’. |
| **gather_subset**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include `all`, `default`, `config`, `neighbors` and `min`. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected.  Default: `["min"]` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](vyos_facts_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](vyos_facts_module.md#id4)

```yaml+jinja
# Gather all facts
- vyos.vyos.vyos_facts:
    gather_subset: all
    gather_network_resources: all

# collect only the config and default facts
- vyos.vyos.vyos_facts:
    gather_subset: config

# collect everything exception the config
- vyos.vyos.vyos_facts:
    gather_subset: '!config'

# Collect only the interfaces facts
- vyos.vyos.vyos_facts:
    gather_subset:
    - '!all'
    - '!min'
    gather_network_resources:
    - interfaces

# Do not collect interfaces facts
- vyos.vyos.vyos_facts:
    gather_network_resources:
    - '!interfaces'

# Collect interfaces and minimal default facts
- vyos.vyos.vyos_facts:
    gather_subset: min
    gather_network_resources: interfaces
```

## [Return Values](vyos_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_net_api**  string | The name of the transport  Returned: always |
| **ansible_net_commits**  list / elements=string | The set of available configuration revisions  Returned: when present |
| **ansible_net_config**  string | The running-config from the device  Returned: when config is configured |
| **ansible_net_gather_network_resources**  list / elements=string | The list of fact resource subsets collected from the device  Returned: always |
| **ansible_net_gather_subset**  list / elements=string | The list of subsets gathered by the module  Returned: always |
| **ansible_net_hostname**  string | The configured system hostname  Returned: always |
| **ansible_net_model**  string | The device model string  Returned: always |
| **ansible_net_neighbors**  list / elements=string | The set of LLDP neighbors  Returned: when interface is configured |
| **ansible_net_python_version**  string | The Python version Ansible controller is using  Returned: always |
| **ansible_net_serialnum**  string | The serial number of the device  Returned: always |
| **ansible_net_version**  string | The version of the software running  Returned: always |

### Authors

- Nathaniel Case (@qalthos)
- Nilashish Chakraborty (@Nilashishc)
- Rohit Thakur (@rohitthakur2590)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
[Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
