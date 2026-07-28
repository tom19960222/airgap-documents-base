---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_logging module – Manage logging on network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_logging_module.html
fetched_at: 2026-07-27T17:02:04+00:00
---
# cisco.nxos.nxos_logging module – Manage logging on network devices

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
> To use it in a playbook, specify: `cisco.nxos.nxos_logging`.

New in cisco.nxos 1.0.0

- [DEPRECATED](nxos_logging_module.md#deprecated)
- [Synopsis](nxos_logging_module.md#synopsis)
- [Parameters](nxos_logging_module.md#parameters)
- [Notes](nxos_logging_module.md#notes)
- [Examples](nxos_logging_module.md#examples)
- [Return Values](nxos_logging_module.md#return-values)
- [Status](nxos_logging_module.md#status)

## [DEPRECATED](nxos_logging_module.md#id1)

Removed in:
:   major release after 2023-08-01

Why:
:   Updated module released with more functionality.

Alternative:
:   nxos_logging_global

## [Synopsis](nxos_logging_module.md#id2)

- This module provides declarative management of logging on Cisco NX-OS devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_logging_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of logging definitions. |
| **dest**  string | Destination of the logs.  Choices:   - `"console"` - `"logfile"` - `"module"` - `"monitor"` - `"server"` |
| **dest_level**  aliases: level  integer | Set logging severity levels. |
| **event**  string | Link/trunk enable/default interface configuration logging  Choices:   - `"link-enable"` - `"link-default"` - `"trunk-enable"` - `"trunk-default"` |
| **facility**  string | Facility name for logging. |
| **facility_level**  integer | Set logging severity levels for facility based log messages. |
| **facility_link_status**  string | Set logging facility ethpm link status. Not idempotent with version 6.0 images.  Choices:   - `"link-down-notif"` - `"link-down-error"` - `"link-up-notif"` - `"link-up-error"` |
| **file_size**  integer | Set logfile size |
| **interface**  string | Interface to be used while configuring source-interface for logging (e.g., ‘Ethernet1/2’, ‘mgmt0’) |
| **interface_message**  string | Add interface description to interface syslogs. Does not work with version 6.0 images using nxapi as a transport.  Choices:   - `"add-interface-description"` |
| **name**  string | If value of `dest` is *logfile* it indicates file-name. |
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
| **purge**  boolean | Remove any switch logging configuration that does not match what has been configured Not supported for ansible_connection local. All nxos_logging tasks must use the same ansible_connection type.  Choices:   - `false` ← (default) - `true` |
| **remote_server**  string | Hostname or IP Address for remote logging (when dest is ‘server’). |
| **state**  string | State of the logging configuration.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timestamp**  string | Set logging timestamp format  Choices:   - `"microseconds"` - `"milliseconds"` - `"seconds"` |
| **use_vrf**  string | VRF to be used while configuring remote logging (when dest is ‘server’). |

## [Notes](nxos_logging_module.md#id4)

> **Note:**
>
> - Limited Support for Cisco MDS
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_logging_module.md#id5)

```yaml+jinja
- name: configure console logging with level
  cisco.nxos.nxos_logging:
    dest: console
    level: 2
    state: present
- name: remove console logging configuration
  cisco.nxos.nxos_logging:
    dest: console
    level: 2
    state: absent
- name: configure file logging with level
  cisco.nxos.nxos_logging:
    dest: logfile
    name: testfile
    dest_level: 3
    state: present
- name: Configure logging logfile with size
  cisco.nxos.nxos_logging:
    dest: logfile
    name: testfile
    dest_level: 3
    file_size: 16384
- name: configure facility level logging
  cisco.nxos.nxos_logging:
    facility: daemon
    facility_level: 0
    state: present
- name: remove facility level logging
  cisco.nxos.nxos_logging:
    facility: daemon
    facility_level: 0
    state: absent
- name: Configure Remote Logging
  cisco.nxos.nxos_logging:
    dest: server
    remote_server: test-syslogserver.com
    facility: auth
    facility_level: 1
    use_vrf: management
    state: present
- name: Configure Source Interface for Logging
  cisco.nxos.nxos_logging:
    interface: mgmt0
    state: present
- name: Purge nxos_logging configuration not managed by this playbook
  cisco.nxos.nxos_logging:
    purge: true
- name: Configure logging timestamp
  cisco.nxos.nxos_logging:
    timestamp: milliseconds
    state: present
- name: Configure logging facility ethpm link status
  cisco.nxos.nxos_logging:
    facility: ethpm
    facility_link_status: link-up-notif
    state: present
- name: Configure logging message ethernet description
  cisco.nxos.nxos_logging:
    interface_message: add-interface-description
    state: present
- name: Configure logging event link enable
  cisco.nxos.nxos_logging:
    event: link-enable
    state: present
- name: Configure logging using aggregate
  cisco.nxos.nxos_logging:
    aggregate:
    - {dest: console, dest_level: 2}
    - {dest: logfile, dest_level: 2, name: testfile}
    - {facility: daemon, facility_level: 0}
    state: present
```

## [Return Values](nxos_logging_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["logging console 2", "logging logfile testfile 3", "logging level daemon 0"]` |

## [Status](nxos_logging_module.md#id7)

- This module will be removed in a major release after 2023-08-01.
  *[deprecated]*
- For more information see [DEPRECATED](nxos_logging_module.md#deprecated).

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
