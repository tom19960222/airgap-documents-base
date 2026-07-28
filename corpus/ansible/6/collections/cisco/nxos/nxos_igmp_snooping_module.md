---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_igmp_snooping module – Manages IGMP snooping global configuration."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_igmp_snooping_module.html
fetched_at: 2026-07-27T17:01:53+00:00
---
# cisco.nxos.nxos_igmp_snooping module – Manages IGMP snooping global configuration.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_igmp_snooping`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_igmp_snooping_module.md#synopsis)
- [Parameters](nxos_igmp_snooping_module.md#parameters)
- [Notes](nxos_igmp_snooping_module.md#notes)
- [Examples](nxos_igmp_snooping_module.md#examples)
- [Return Values](nxos_igmp_snooping_module.md#return-values)

## [Synopsis](nxos_igmp_snooping_module.md#id1)

- Manages IGMP snooping global configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_igmp_snooping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **group_timeout**  string | Group membership timeout value for all VLANs on the device. Accepted values are integer in range 1-10080, *never* and *default*. |
| **link_local_grp_supp**  boolean | Global link-local groups suppression.  Choices:   - `false` - `true` |
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
| **report_supp**  boolean | Global IGMPv1/IGMPv2 Report Suppression.  Choices:   - `false` - `true` |
| **snooping**  boolean | Enables/disables IGMP snooping on the switch.  Choices:   - `false` - `true` |
| **state**  string | Manage the state of the resource.  Choices:   - `"present"` ← (default) - `"default"` |
| **v3_report_supp**  boolean | Global IGMPv3 Report Suppression and Proxy Reporting.  Choices:   - `false` - `true` |

## [Notes](nxos_igmp_snooping_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - When `state=default`, params will be reset to a default state.
> - `group_timeout` also accepts *never* as an input.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_igmp_snooping_module.md#id4)

```yaml+jinja
# ensure igmp snooping params supported in this module are in there default state
- cisco.nxos.nxos_igmp_snooping:
    state: default

# ensure following igmp snooping params are in the desired state
- cisco.nxos.nxos_igmp_snooping:
    group_timeout: never
    snooping: true
    link_local_grp_supp: false
    optimize_mcast_flood: false
    report_supp: true
    v3_report_supp: true
```

## [Return Values](nxos_igmp_snooping_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | command sent to the device  Returned: always  Sample: `["ip igmp snooping link-local-groups-suppression", "ip igmp snooping group-timeout 50", "no ip igmp snooping report-suppression", "no ip igmp snooping v3-report-suppression", "no ip igmp snooping"]` |

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
