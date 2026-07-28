---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_acl module – (deprecated, removed after 2022-06-01) Manages access list entries for ACLs."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_acl_module.html
fetched_at: 2026-07-27T17:01:34+00:00
---
# cisco.nxos.nxos_acl module – (deprecated, removed after 2022-06-01) Manages access list entries for ACLs.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_acl`.

New in cisco.nxos 1.0.0

- [DEPRECATED](nxos_acl_module.md#deprecated)
- [Synopsis](nxos_acl_module.md#synopsis)
- [Parameters](nxos_acl_module.md#parameters)
- [Notes](nxos_acl_module.md#notes)
- [Examples](nxos_acl_module.md#examples)
- [Return Values](nxos_acl_module.md#return-values)
- [Status](nxos_acl_module.md#status)

## [DEPRECATED](nxos_acl_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   nxos_acls

## [Synopsis](nxos_acl_module.md#id2)

- Manages access list entries for ACLs.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_acl_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ack**  string | Match on the ACK bit.  Choices:   - `"enable"` |
| **action**  string | Action of the ACE.  Choices:   - `"permit"` - `"deny"` - `"remark"` |
| **dest**  string | Destination ip and mask using IP/MASK notation and supports the keyword ‘any’. |
| **dest_port1**  string | Port/protocol and also first (lower) port when using range operand. |
| **dest_port2**  string | Second (end) port when using range operand. |
| **dest_port_op**  string | Destination port operands such as eq, neq, gt, lt, range.  Choices:   - `"any"` - `"eq"` - `"gt"` - `"lt"` - `"neq"` - `"range"` |
| **dscp**  string | Match packets with given dscp value.  Choices:   - `"af11"` - `"af12"` - `"af13"` - `"af21"` - `"af22"` - `"af23"` - `"af31"` - `"af32"` - `"af33"` - `"af41"` - `"af42"` - `"af43"` - `"cs1"` - `"cs2"` - `"cs3"` - `"cs4"` - `"cs5"` - `"cs6"` - `"cs7"` - `"default"` - `"ef"` |
| **established**  string | Match established connections.  Choices:   - `"enable"` |
| **fin**  string | Match on the FIN bit.  Choices:   - `"enable"` |
| **fragments**  string | Check non-initial fragments.  Choices:   - `"enable"` |
| **log**  string | Log matches against this entry.  Choices:   - `"enable"` |
| **name**  string / required | Case sensitive name of the access list (ACL). |
| **precedence**  string | Match packets with given precedence.  Choices:   - `"critical"` - `"flash"` - `"flash-override"` - `"immediate"` - `"internet"` - `"network"` - `"priority"` - `"routine"` |
| **proto**  string | Port number or protocol (as supported by the switch). |
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
| **psh**  string | Match on the PSH bit.  Choices:   - `"enable"` |
| **remark**  string | If action is set to remark, this is the description. |
| **rst**  string | Match on the RST bit.  Choices:   - `"enable"` |
| **seq**  string | Sequence number of the entry (ACE). |
| **src**  string | Source ip and mask using IP/MASK notation and supports keyword ‘any’. |
| **src_port1**  string | Port/protocol and also first (lower) port when using range operand. |
| **src_port2**  string | Second (end) port when using range operand. |
| **src_port_op**  string | Source port operands such as eq, neq, gt, lt, range.  Choices:   - `"any"` - `"eq"` - `"gt"` - `"lt"` - `"neq"` - `"range"` |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` - `"delete_acl"` |
| **syn**  string | Match on the SYN bit.  Choices:   - `"enable"` |
| **time_range**  string | Name of time-range to apply. |
| **urg**  string | Match on the URG bit.  Choices:   - `"enable"` |

## [Notes](nxos_acl_module.md#id4)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - `state=absent` removes the ACE if it exists.
> - `state=delete_acl` deletes the ACL if it exists.
> - For idempotency, use port numbers for the src/dest port params like *src_port1* and names for the well defined protocols for the *proto* param.
> - Although this module is idempotent in that if the ace as presented in the task is identical to the one on the switch, no changes will be made. If there is any difference, what is in Ansible will be pushed (configured options will be overridden). This is to improve security, but at the same time remember an ACE is removed, then re-added, so if there is a change, the new ACE will be exactly what parameters you are sending to the module.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_acl_module.md#id5)

```yaml+jinja
# configure ACL ANSIBLE
- cisco.nxos.nxos_acl:
    name: ANSIBLE
    seq: 10
    action: permit
    proto: tcp
    src: 192.0.2.1/24
    dest: any
    state: present
```

## [Return Values](nxos_acl_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  Returned: always  Sample: `["ip access-list ANSIBLE", "10 permit tcp 192.0.2.1/24 any"]` |

## [Status](nxos_acl_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](nxos_acl_module.md#deprecated).

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
