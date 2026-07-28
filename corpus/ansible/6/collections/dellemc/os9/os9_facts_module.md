---
collection: ansible
version: "6"
title: "dellemc.os9.os9_facts module – Collect facts from remote devices running Dell EMC Networking OS9"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/os9/os9_facts_module.html
fetched_at: 2026-07-27T17:26:08+00:00
---
# dellemc.os9.os9_facts module – Collect facts from remote devices running Dell EMC Networking OS9

> **Note:**
>
> This module is part of the [dellemc.os9 collection](https://galaxy.ansible.com/dellemc/os9) (version 1.0.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.os9`.
>
> To use it in a playbook, specify: `dellemc.os9.os9_facts`.

- [Synopsis](os9_facts_module.md#synopsis)
- [Parameters](os9_facts_module.md#parameters)
- [Notes](os9_facts_module.md#notes)
- [Examples](os9_facts_module.md#examples)
- [Return Values](os9_facts_module.md#return-values)

## [Synopsis](os9_facts_module.md#id1)

- Collects a base set of device facts from a remote device that is running OS9. This module prepends all of the base network fact keys with `ansible_net_<fact>`. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](os9_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **gather_subset**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all, hardware, config, and interfaces. Can specify a list of values to include a larger subset. Values can also be used with an initial `M(!`) to specify that a specific subset should not be collected.  Default: `["!config"]` |
| **provider**  dictionary | A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Password to authenticate the SSH session to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Path to an ssh key used to authenticate the SSH session to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies idle timeout (in seconds) for the connection. Useful if the console freezes before continuing. For example when saving configurations. |
| **username**  string | User to authenticate the SSH session to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](os9_facts_module.md#id3)

> **Note:**
>
> - This module requires OS9 version 9.10.0.1P13 or above.
> - This module requires an increase of the SSH connection rate limit. Use the following command *ip ssh connection-rate-limit 60* to configure the same. This can be also be done with the **ERROR while parsing**: While parsing M() at index 186: Module name “os9_config” is not a FQCN module.
> - For more information on using Ansible to manage Dell EMC Network devices see <https://www.ansible.com/ansible-dell-networking>.

## [Examples](os9_facts_module.md#id4)

```yaml+jinja
# Collect all facts from the device
- os9_facts:
    gather_subset: all
# Collect only the config and default facts
- os9_facts:
    gather_subset:
      - config
# Do not collect hardware facts
- os9_facts:
    gather_subset:
      - "!hardware"
```

## [Return Values](os9_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_net_all_ipv4_addresses**  list / elements=string | All IPv4 addresses configured on the device  Returned: when interfaces is configured |
| **ansible_net_all_ipv6_addresses**  list / elements=string | All IPv6 addresses configured on the device  Returned: when interfaces is configured |
| **ansible_net_config**  string | The current active config from the device  Returned: when config is configured |
| **ansible_net_filesystems**  list / elements=string | All file system names available on the device  Returned: when hardware is configured |
| **ansible_net_gather_subset**  list / elements=string | The list of fact subsets collected from the device  Returned: always |
| **ansible_net_hostname**  string | The configured hostname of the device  Returned: always |
| **ansible_net_image**  string | The image file the device is running  Returned: always |
| **ansible_net_interfaces**  dictionary | A hash of all interfaces running on the system  Returned: when interfaces is configured |
| **ansible_net_memfree_mb**  integer | The available free memory on the remote device in Mb  Returned: when hardware is configured |
| **ansible_net_memtotal_mb**  integer | The total memory on the remote device in Mb  Returned: when hardware is configured |
| **ansible_net_model**  string | The model name returned from the device  Returned: always |
| **ansible_net_neighbors**  dictionary | The list of LLDP neighbors from the remote device  Returned: when interfaces is configured |
| **ansible_net_serialnum**  string | The serial number of the remote device  Returned: always |
| **ansible_net_servicetags**  list / elements=string | The servicetags from remote device  Returned: always |
| **ansible_net_version**  string | The operating system version running on the remote device  Returned: always |

### Authors

- Dhivya P (@dhivyap)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.os9/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.os9)
