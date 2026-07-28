---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_linkagg module – (deprecated, removed after 2022-06-01) Manage link aggregation groups on Juniper JUNOS network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_linkagg_module.html
fetched_at: 2026-07-27T17:54:23+00:00
---
# junipernetworks.junos.junos_linkagg module – (deprecated, removed after 2022-06-01) Manage link aggregation groups on Juniper JUNOS network devices

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/junipernetworks/junos) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_linkagg_module.md#ansible-collections-junipernetworks-junos-junos-linkagg-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_linkagg`.

New in junipernetworks.junos 1.0.0

- [DEPRECATED](junos_linkagg_module.md#deprecated)
- [Synopsis](junos_linkagg_module.md#synopsis)
- [Requirements](junos_linkagg_module.md#requirements)
- [Parameters](junos_linkagg_module.md#parameters)
- [Notes](junos_linkagg_module.md#notes)
- [Examples](junos_linkagg_module.md#examples)
- [Return Values](junos_linkagg_module.md#return-values)
- [Status](junos_linkagg_module.md#status)

## [DEPRECATED](junos_linkagg_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   Use [junipernetworks.junos.junos_lag_interfaces](junos_lag_interfaces_module.md#ansible-collections-junipernetworks-junos-junos-lag-interfaces-module) instead.

## [Synopsis](junos_linkagg_module.md#id2)

- This module provides declarative management of link aggregation groups on Juniper JUNOS network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_linkagg_module.md#id3)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.5.2)

## [Parameters](junos_linkagg_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | Specifies whether or not the configuration is active or deactivated  Choices:   - `false` - `true` ← (default) |
| **aggregate**  list / elements=dictionary | List of link aggregation definitions. |
| **active**  boolean | Specifies whether or not the configuration is active or deactivated  Choices:   - `false` - `true` |
| **description**  string | Description of Interface. |
| **device_count**  integer | Number of aggregated ethernet devices that can be configured. Acceptable integer value is between 1 and 128. |
| **members**  list / elements=string | List of members interfaces of the link aggregation group. The value can be single interface or list of interfaces. |
| **min_links**  integer | Minimum members that should be up before bringing up the link aggregation group. |
| **mode**  string | Mode of the link aggregation group. A value of `on` will enable LACP in `passive` mode. `active` configures the link to actively information about the state of the link, or it can be configured in `passive` mode ie. send link state information only when received them from another link. A value of `off` will disable LACP.  Choices:   - `"on"` - `"off"` - `"active"` - `"passive"` |
| **name**  string / required | Name of the link aggregation group. |
| **state**  string | State of the link aggregation group.  Choices:   - `"present"` - `"absent"` - `"up"` - `"down"` |
| **description**  string | Description of Interface. |
| **device_count**  integer | Number of aggregated ethernet devices that can be configured. Acceptable integer value is between 1 and 128. |
| **members**  list / elements=string | List of members interfaces of the link aggregation group. The value can be single interface or list of interfaces. |
| **min_links**  integer | Minimum members that should be up before bringing up the link aggregation group. |
| **mode**  string | Mode of the link aggregation group. A value of `on` will enable LACP in `passive` mode. `active` configures the link to actively information about the state of the link, or it can be configured in `passive` mode ie. send link state information only when received them from another link. A value of `off` will disable LACP.  Choices:   - `"on"` ← (default) - `"off"` - `"active"` - `"passive"` |
| **name**  string | Name of the link aggregation group. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli` or `connection: netconf`.  For more information please see the [Junos OS Platform Options guide](../network/user_guide/platform_junos.md).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. The port value will default to the well known SSH port of 22 (for `transport=cli`) or port 830 (for `transport=netconf`) device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"cli"` - `"netconf"` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **state**  string | State of the link aggregation group.  Choices:   - `"present"` ← (default) - `"absent"` - `"up"` - `"down"` |

## [Notes](junos_linkagg_module.md#id5)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
> - Recommended connection is `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - This module also works with `local` connections for legacy playbooks.
> - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Juniper network devices see <https://www.ansible.com/ansible-juniper>.

## [Examples](junos_linkagg_module.md#id6)

```yaml+jinja
- name: configure link aggregation
  junipernetworks.junos.junos_linkagg:
    name: ae11
    members:
    - ge-0/0/5
    - ge-0/0/6
    - ge-0/0/7
    lacp: active
    device_count: 4
    state: present

- name: delete link aggregation
  junipernetworks.junos.junos_linkagg:
    name: ae11
    members:
    - ge-0/0/5
    - ge-0/0/6
    - ge-0/0/7
    lacp: active
    device_count: 4
    state: delete

- name: deactivate link aggregation
  junipernetworks.junos.junos_linkagg:
    name: ae11
    members:
    - ge-0/0/5
    - ge-0/0/6
    - ge-0/0/7
    lacp: active
    device_count: 4
    state: present
    active: false

- name: Activate link aggregation
  junipernetworks.junos.junos_linkagg:
    name: ae11
    members:
    - ge-0/0/5
    - ge-0/0/6
    - ge-0/0/7
    lacp: active
    device_count: 4
    state: present
    active: true

- name: Disable link aggregation
  junipernetworks.junos.junos_linkagg:
    name: ae11
    state: down

- name: Enable link aggregation
  junipernetworks.junos.junos_linkagg:
    name: ae11
    state: up
```

## [Return Values](junos_linkagg_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff**  string | Configuration difference before and after applying change.  Returned: when configuration is changed and diff option is enabled.  Sample: `"[edit interfaces] +   ge-0/0/6 { +       ether-options { +           802.3ad ae0; +       } +   } [edit interfaces ge-0/0/7] +   ether-options { +       802.3ad ae0; +   } [edit interfaces] +   ae0 { +       description \"configured by junos_linkagg\"; +       aggregated-ether-options { +           lacp { +               active; +           } +       } +   }\n"` |

## [Status](junos_linkagg_module.md#id8)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](junos_linkagg_module.md#deprecated).

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
