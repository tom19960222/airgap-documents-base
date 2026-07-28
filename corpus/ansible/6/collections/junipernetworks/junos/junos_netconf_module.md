---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_netconf module – Configures the Junos Netconf system service"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_netconf_module.html
fetched_at: 2026-07-27T17:54:28+00:00
---
# junipernetworks.junos.junos_netconf module – Configures the Junos Netconf system service

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/junipernetworks/junos) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_netconf`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_netconf_module.md#synopsis)
- [Parameters](junos_netconf_module.md#parameters)
- [Notes](junos_netconf_module.md#notes)
- [Examples](junos_netconf_module.md#examples)
- [Return Values](junos_netconf_module.md#return-values)

## [Synopsis](junos_netconf_module.md#id1)

- This module provides an abstraction that enables and configures the netconf system service running on Junos devices. This module can be used to easily enable the Netconf API. Netconf provides a programmatic interface for working with configuration and state resources as defined in RFC 6242. If the `netconf_port` is not mentioned in the task by default netconf will be enabled on port 830 only.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](junos_netconf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **netconf_port**  aliases: listens_on  integer | This argument specifies the port the netconf service should listen on for SSH connections. The default port as defined in RFC 6242 is 830.  Default: `830` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli` or `connection: netconf`.  For more information please see the [Junos OS Platform Options guide](../network/user_guide/platform_junos.md).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. The port value will default to the well known SSH port of 22 (for `transport=cli`) or port 830 (for `transport=netconf`) device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"cli"` - `"netconf"` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **state**  string | Specifies the state of the `junos_netconf` resource on the remote device. If the *state* argument is set to *present* the netconf service will be configured. If the *state* argument is set to *absent* the netconf service will be removed from the configuration.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](junos_netconf_module.md#id3)

> **Note:**
>
> - Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
> - Recommended connection is `network_cli`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - This module also works with `local` connections for legacy playbooks.
> - If `netconf_port` value is not mentioned in task by default it will be enabled on port 830 only. Although `netconf_port` value can be from 1 through 65535, avoid configuring access on a port that is normally assigned for another service. This practice avoids potential resource conflicts.
> - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Juniper network devices see <https://www.ansible.com/ansible-juniper>.

## [Examples](junos_netconf_module.md#id4)

```yaml+jinja
- name: enable netconf service on port 830
  junipernetworks.junos.junos_netconf:
    listens_on: 830
    state: present

- name: disable netconf service
  junipernetworks.junos.junos_netconf:
    state: absent
```

## [Return Values](junos_netconf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  string | Returns the command sent to the remote device  Returned: when changed is True  Sample: `"set system services netconf ssh port 830"` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
