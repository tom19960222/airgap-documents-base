---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_static_route module – (deprecated, removed after 2022-06-01) Manage static IP routes on Juniper JUNOS network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_static_route_module.html
fetched_at: 2026-07-27T17:54:40+00:00
---
# junipernetworks.junos.junos_static_route module – (deprecated, removed after 2022-06-01) Manage static IP routes on Juniper JUNOS network devices

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
> see [Requirements](junos_static_route_module.md#ansible-collections-junipernetworks-junos-junos-static-route-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_static_route`.

New in junipernetworks.junos 1.0.0

- [DEPRECATED](junos_static_route_module.md#deprecated)
- [Synopsis](junos_static_route_module.md#synopsis)
- [Requirements](junos_static_route_module.md#requirements)
- [Parameters](junos_static_route_module.md#parameters)
- [Notes](junos_static_route_module.md#notes)
- [Examples](junos_static_route_module.md#examples)
- [Return Values](junos_static_route_module.md#return-values)
- [Status](junos_static_route_module.md#status)

## [DEPRECATED](junos_static_route_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   Use [junipernetworks.junos.junos_static_routes](junos_static_routes_module.md#ansible-collections-junipernetworks-junos-junos-static-routes-module) instead.

## [Synopsis](junos_static_route_module.md#id2)

- This module provides declarative management of static IP routes on Juniper JUNOS network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_static_route_module.md#id3)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.5.2)

## [Parameters](junos_static_route_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | Specifies whether or not the configuration is active or deactivated  Choices:   - `false` - `true` ← (default) |
| **address**  aliases: prefix  string | Network address with prefix of the static route. |
| **aggregate**  list / elements=dictionary | List of static route definitions |
| **active**  boolean | Specifies whether or not the configuration is active or deactivated  Choices:   - `false` - `true` |
| **address**  string / required | Network address with prefix of the static route. |
| **next_hop**  string | Next hop IP of the static route. |
| **preference**  aliases: admin_distance  integer | Global admin preference of the static route. |
| **qualified_next_hop**  string | Qualified next hop IP of the static route. Qualified next hops allow to associate preference with a particular next-hop address. |
| **qualified_preference**  integer | Assign preference for qualified next hop. |
| **state**  string | State of the static route configuration.  Choices:   - `"present"` - `"absent"` |
| **next_hop**  string | Next hop IP of the static route. |
| **preference**  aliases: admin_distance  integer | Global admin preference of the static route. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli` or `connection: netconf`.  For more information please see the [Junos OS Platform Options guide](../network/user_guide/platform_junos.md).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. The port value will default to the well known SSH port of 22 (for `transport=cli`) or port 830 (for `transport=netconf`) device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"cli"` - `"netconf"` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **qualified_next_hop**  string | Qualified next hop IP of the static route. Qualified next hops allow to associate preference with a particular next-hop address. |
| **qualified_preference**  integer | Assign preference for qualified next hop. |
| **state**  string | State of the static route configuration.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](junos_static_route_module.md#id5)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
> - Recommended connection is `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - This module also works with `local` connections for legacy playbooks.
> - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Juniper network devices see <https://www.ansible.com/ansible-juniper>.

## [Examples](junos_static_route_module.md#id6)

```yaml+jinja
- name: configure static route
  junipernetworks.junos.junos_static_route:
    address: 192.168.2.0/24
    next_hop: 10.0.0.1
    preference: 10
    qualified_next_hop: 10.0.0.2
    qualified_preference: 3
    state: present

- name: delete static route
  junipernetworks.junos.junos_static_route:
    address: 192.168.2.0/24
    state: absent

- name: deactivate static route configuration
  junipernetworks.junos.junos_static_route:
    address: 192.168.2.0/24
    next_hop: 10.0.0.1
    preference: 10
    qualified_next_hop: 10.0.0.2
    qualified_preference: 3
    state: present
    active: false

- name: activate static route configuration
  junipernetworks.junos.junos_static_route:
    address: 192.168.2.0/24
    next_hop: 10.0.0.1
    preference: 10
    qualified_next_hop: 10.0.0.2
    qualified_preference: 3
    state: present
    active: true

- name: Configure static route using aggregate
  junipernetworks.junos.junos_static_route:
    aggregate:
    - {address: 4.4.4.0/24, next_hop: 3.3.3.3, qualified_next_hop: 5.5.5.5, qualified_preference: 30}
    - {address: 5.5.5.0/24, next_hop: 6.6.6.6, qualified_next_hop: 7.7.7.7, qualified_preference: 12}
    preference: 10

- name: Delete static route using aggregate
  junipernetworks.junos.junos_static_route:
    aggregate:
    - address: 4.4.4.0/24
    - address: 5.5.5.0/24
    state: absent
```

## [Return Values](junos_static_route_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff.prepared**  string | Configuration difference before and after applying change.  Returned: when configuration is changed and diff option is enabled.  Sample: `"[edit routing-options static]\n     route 2.2.2.0/24 { ... }\n+    route 4.4.4.0/24 {\n        next-hop 3.3.3.3;\n        qualified-next-hop 5.5.5.5 {\n+            preference 30;\n         }\n+        preference 10; +    }\n"` |

## [Status](junos_static_route_module.md#id8)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](junos_static_route_module.md#deprecated).

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
