---
collection: ansible
version: "6"
title: "cisco.asa.asa_facts module – Collect facts from remote devices running Cisco ASA"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/asa/asa_facts_module.html
fetched_at: 2026-07-27T16:50:48+00:00
---
# cisco.asa.asa_facts module – Collect facts from remote devices running Cisco ASA

> **Note:**
>
> This module is part of the [cisco.asa collection](https://galaxy.ansible.com/cisco/asa) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.asa`.
>
> To use it in a playbook, specify: `cisco.asa.asa_facts`.

New in cisco.asa 1.0.0

- [Synopsis](asa_facts_module.md#synopsis)
- [Parameters](asa_facts_module.md#parameters)
- [Notes](asa_facts_module.md#notes)
- [Examples](asa_facts_module.md#examples)
- [Return Values](asa_facts_module.md#return-values)

## [Synopsis](asa_facts_module.md#id1)

- Collects a base set of device facts from a remote device that is running ASA. This module prepends all of the base network fact keys with `ansible_net_<fact>`. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.
- Note, to collects facts from ASA device properly user should elevate the privilege to become.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](asa_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **authorize**  boolean | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli` and `become: yes`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` - `true` |
| **context**  string | Specifies which context to target if you are running in the ASA in multiple context mode. Defaults to the current context you login to. |
| **gather_network_resources**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all and the resources like interfaces, vlans etc. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected. Values can also be used with an initial `!` to specify that a specific subset should not be collected. Valid subsets are ‘all’, ‘acls’, ‘ogs’. |
| **gather_subset**  list / elements=string | When supplied, this argument restricts the facts collected to a given subset.  Possible values for this argument include `all`, `min`, `hardware`, `config`.  Specify a list of values to include a larger subset.  Use a value with an initial `!` to collect all facts except that subset.  Default: `["!config"]` |
| **passwords**  boolean | Saves running-config passwords in clear-text when set to True. Defaults to False  Choices:   - `false` - `true` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies idle timeout in seconds for the connection, in seconds. Useful if the console freezes before continuing. For example when saving configurations. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](asa_facts_module.md#id3)

> **Note:**
>
> - Tested against asa 9.10(1)11
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](asa_facts_module.md#id4)

```yaml+jinja
- name: Gather all legacy facts
  cisco.asa.asa_facts:
    gather_subset: all

- name: Gather only the config and default facts
  cisco.asa.asa_facts:
    gather_subset:
    - config

- name: Do not gather hardware facts
  cisco.asa.asa_facts:
    gather_subset:
    - '!hardware'

- name: Gather legacy and resource facts
  cisco.asa.asa_facts:
    gather_subset: all
```

## [Return Values](asa_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_net_api**  string | The name of the transport  Returned: always |
| **ansible_net_asatype**  string | The operating system type (Cisco ASA) running on the remote device.  Returned: always |
| **ansible_net_config**  string | The current active config from the device  Returned: when config is configured |
| **ansible_net_device_mgr_version**  string | The Device manager version running on the remote device.  Returned: always |
| **ansible_net_filesystems**  list / elements=string | All file system names available on the device  Returned: when hardware is configured |
| **ansible_net_filesystems_info**  dictionary | A hash of all file systems containing info about each file system (e.g. free and total space)  Returned: when hardware is configured |
| **ansible_net_firepower_version**  string | The Firepower operating system version running on the remote device.  Returned: always |
| **ansible_net_gather_subset**  list / elements=string | The list of fact subsets collected from the device  Returned: always |
| **ansible_net_hostname**  string | The configured hostname of the device  Returned: always |
| **ansible_net_image**  string | The image file the device is running  Returned: always |
| **ansible_net_memfree_mb**  integer | The available free memory on the remote device in Mb  Returned: when hardware is configured |
| **ansible_net_memtotal_mb**  integer | The total memory on the remote device in Mb  Returned: when hardware is configured |
| **ansible_net_memused_mb**  integer | The used memory on the remote device in Mb  Returned: when hardware is configured |
| **ansible_net_model**  string | The model name returned from the device  Returned: always |
| **ansible_net_python_version**  string | The Python version Ansible controller is using  Returned: always |
| **ansible_net_serialnum**  string | The serial number of the remote device  Returned: always |
| **ansible_net_stacked_models**  list / elements=string | The model names of each device in the stack  Returned: when multiple devices are configured in a stack |
| **ansible_net_stacked_serialnums**  list / elements=string | The serial numbers of each device in the stack  Returned: when multiple devices are configured in a stack |
| **ansible_net_version**  string | The operating system version running on the remote device  Returned: always |

### Authors

- Sumit Jaiswal (@justjais)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.asa/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.asa)
