---
collection: ansible
version: "6"
title: "cisco.iosxr.iosxr_logging module – (deprecated, removed after 2023-08-01) Configuration management of system logging services on network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/iosxr_logging_module.html
fetched_at: 2026-07-27T16:55:49+00:00
---
# cisco.iosxr.iosxr_logging module – (deprecated, removed after 2023-08-01) Configuration management of system logging services on network devices

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/cisco/iosxr) (version 3.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
> You need further requirements to be able to use this module,
> see [Requirements](iosxr_logging_module.md#ansible-collections-cisco-iosxr-iosxr-logging-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_logging`.

New in cisco.iosxr 1.0.0

- [DEPRECATED](iosxr_logging_module.md#deprecated)
- [Synopsis](iosxr_logging_module.md#synopsis)
- [Requirements](iosxr_logging_module.md#requirements)
- [Parameters](iosxr_logging_module.md#parameters)
- [Notes](iosxr_logging_module.md#notes)
- [Examples](iosxr_logging_module.md#examples)
- [Return Values](iosxr_logging_module.md#return-values)
- [Status](iosxr_logging_module.md#status)

## [DEPRECATED](iosxr_logging_module.md#id1)

Removed in:
:   major release after 2023-08-01

Why:
:   Updated module released with more functionality.

Alternative:
:   iosxr_logging_global

## [Synopsis](iosxr_logging_module.md#id2)

- This module provides declarative management configuration of system logging (syslog) on Cisco IOS XR devices.

## [Requirements](iosxr_logging_module.md#id3)

The below requirements are needed on the host that executes this module.

- ncclient >= 0.5.3 when using netconf
- lxml >= 4.1.1 when using netconf

## [Parameters](iosxr_logging_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of syslog logging configuration definitions. |
| **dest**  string | Destination for system logging (syslog) messages.  Choices:   - `"host"` - `"console"` - `"monitor"` - `"buffered"` - `"file"` |
| **facility**  string | To configure the type of syslog facility in which system logging (syslog) messages are sent to syslog servers Optional config for `dest` = `host` |
| **hostnameprefix**  string | To append a hostname prefix to system logging (syslog) messages logged to syslog servers. Optional config for `dest` = `host` |
| **level**  aliases: severity  string | Specifies the severity level for the logging.  Choices:   - `"emergencies"` - `"alerts"` - `"critical"` - `"errors"` - `"warning"` - `"notifications"` - `"informational"` - `"debugging"` |
| **name**  string | When `dest` = *file* name indicates file-name  When `dest` = *host* name indicates the host-name or ip-address of syslog server. |
| **path**  string | Set file path. |
| **size**  integer | Size of buffer when `dest` = `buffered`. The acceptable value is in the range *307200 to 125000000 bytes*. Default 307200  Size of file when `dest` = `file`. The acceptable value is in the range *1 to 2097152*KB. Default 2 GB |
| **state**  string | Existential state of the logging configuration on the node.  Choices:   - `"present"` - `"absent"` |
| **vrf**  string | vrf name when syslog server is configured, `dest` = `host` |
| **dest**  string | Destination for system logging (syslog) messages.  Choices:   - `"host"` - `"console"` - `"monitor"` - `"buffered"` - `"file"` |
| **facility**  string | To configure the type of syslog facility in which system logging (syslog) messages are sent to syslog servers Optional config for `dest` = `host`  Default: `"local7"` |
| **hostnameprefix**  string | To append a hostname prefix to system logging (syslog) messages logged to syslog servers. Optional config for `dest` = `host` |
| **level**  aliases: severity  string | Specifies the severity level for the logging.  Choices:   - `"emergencies"` - `"alerts"` - `"critical"` - `"errors"` - `"warning"` - `"notifications"` - `"informational"` - `"debugging"` ← (default) |
| **name**  string | When `dest` = *file* name indicates file-name  When `dest` = *host* name indicates the host-name or ip-address of syslog server. |
| **path**  string | Set file path. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Specifies the type of connection based transport.  Choices:   - `"cli"` ← (default) - `"netconf"` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **size**  integer | Size of buffer when `dest` = `buffered`. The acceptable value is in the range *307200 to 125000000 bytes*. Default 307200  Size of file when `dest` = `file`. The acceptable value is in the range *1 to 2097152*KB. Default 2 GB |
| **state**  string | Existential state of the logging configuration on the node.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vrf**  string | vrf name when syslog server is configured, `dest` = `host`  Default: `"default"` |

## [Notes](iosxr_logging_module.md#id5)

> **Note:**
>
> - This module works with connection `network_cli` and `netconf`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](iosxr_logging_module.md#id6)

```yaml+jinja
- name: configure logging for syslog server host
  cisco.iosxr.iosxr_logging:
    dest: host
    name: 10.10.10.1
    level: critical
    state: present

- name: add hostnameprefix configuration
  cisco.iosxr.iosxr_logging:
    hostnameprefix: host1
    state: absent

- name: add facility configuration
  cisco.iosxr.iosxr_logging:
    facility: local1
    state: present

- name: configure console logging level
  cisco.iosxr.iosxr_logging:
    dest: console
    level: debugging
    state: present

- name: configure monitor logging level
  cisco.iosxr.iosxr_logging:
    dest: monitor
    level: errors
    state: present

- name: configure syslog to a file
  cisco.iosxr.iosxr_logging:
    dest: file
    name: file_name
    size: 2048
    level: errors
    state: present

- name: configure buffered logging with size
  cisco.iosxr.iosxr_logging:
    dest: buffered
    size: 5100000

- name: Configure logging using aggregate
  cisco.iosxr.iosxr_logging:
    aggregate:
    - {dest: console, level: warning}
    - {dest: buffered, size: 4800000}
    - {dest: file, name: file3, size: 2048}
    - {dest: host, name: host3, level: critical}

- name: Delete logging using aggregate
  cisco.iosxr.iosxr_logging:
    aggregate:
    - {dest: console, level: warning}
    - {dest: buffered, size: 4800000}
    - {dest: file, name: file3, size: 2048}
    - {dest: host, name: host3, level: critical}
    state: absent
```

## [Return Values](iosxr_logging_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always (empty list when no commands to send)  Sample: `["logging 10.10.10.1 vrf default severity debugging", "logging facility local7", "logging hostnameprefix host1", "logging console critical", "logging buffered 2097153", "logging buffered warnings", "logging monitor errors", "logging file log_file maxfilesize 1024 severity info"]` |
| **xml**  list / elements=string | NetConf rpc xml sent to device with transport `netconf`  Returned: always (empty list when no xml rpc to send)  Sample: `["<config xmlns:xc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <syslog xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XR-infra-syslog-cfg\"> <files> <file xc:operation=\"delete\"> <file-name>file1</file-name> <file-log-attributes> <max-file-size>2097152</max-file-size> <severity>2</severity> </file-log-attributes> </file> </files> </syslog> </config>"]` |

## [Status](iosxr_logging_module.md#id8)

- This module will be removed in a major release after 2023-08-01.
  *[deprecated]*
- For more information see [DEPRECATED](iosxr_logging_module.md#deprecated).

### Authors

- Trishna Guha (@trishnaguha)
- Kedar Kekan (@kedarX)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
