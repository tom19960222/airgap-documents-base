---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_logging module – Manage logging configuration on SONiC."
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_logging_module.html
fetched_at: 2026-07-28T02:03:42+00:00
---
# dellemc.enterprise_sonic.sonic_logging module – Manage logging configuration on SONiC.

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_logging`.

New in dellemc.enterprise_sonic 2.1.0

- [Synopsis](sonic_logging_module.md#synopsis)
- [Parameters](sonic_logging_module.md#parameters)
- [Examples](sonic_logging_module.md#examples)
- [Return Values](sonic_logging_module.md#return-values)

## [Synopsis](sonic_logging_module.md#id1)

- This module provides configuration management of logging for devices running SONiC.

## [Parameters](sonic_logging_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Specifies logging related configurations. |
| **remote_servers**  list / elements=dictionary | Remote logging sever configuration. |
| **host**  string / required | IPv4/IPv6 address or host name of the remote logging server. |
| **message_type**  string | Type of messages that remote server receives.  message_type can not be deleted.  **Choices:**   - `"log"` - `"event"` |
| **remote_port**  integer | Destination port number for logging messages sent to the server.  remote_port can not be deleted. |
| **source_interface**  string | Source interface used as source ip for sending logging packets.  source_interface can not be deleted. |
| **vrf**  string | VRF name used by remote logging server. |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` |

## [Examples](sonic_logging_module.md#id3)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#
#sonic# show logging servers
#--------------------------------------------------------------------------------
#HOST            PORT      SOURCE-INTERFACE    VRF            MESSGE-TYPE
#--------------------------------------------------------------------------------
#10.11.0.2       5         Ethernet24          -              event
#10.11.1.1       616       Ethernet8           -              log
#log1.dell.com   6         Ethernet28          -              log
#
- name: Delete logging server configuration
  sonic_logging:
    config:
      remote_servers:
        - host: 10.11.0.2
        - host: log1.dell.com
    state: deleted

# After state:
# ------------
#
#sonic# show logging servers
#--------------------------------------------------------------------------------
#HOST            PORT      SOURCE-INTERFACE    VRF            MESSGE-TYPE
#--------------------------------------------------------------------------------
#10.11.1.1       616       Ethernet8           -              log
#
#
# Using merged
#
# Before state:
# -------------
#
#sonic# show logging servers
#--------------------------------------------------------------------------------
#HOST            PORT      SOURCE-INTERFACE    VRF            MESSGE-TYPE
#--------------------------------------------------------------------------------
#10.11.1.1       616       Ethernet8           -              log
#
- name: Merge logging server configuration
  sonic_logging:
    config:
      remote_servers:
        - host: 10.11.0.2
          remote_port: 5
          source_interface: Ethernet24
          message_type: event
        - host: log1.dell.com
          remote_port: 6
          source_interface: Ethernet28
    state: merged

# After state:
# ------------
#
#sonic# show logging servers
#--------------------------------------------------------------------------------
#HOST            PORT      SOURCE-INTERFACE    VRF            MESSGE-TYPE
#--------------------------------------------------------------------------------
#10.11.0.2       5         Ethernet24          -              event
#10.11.1.1       616       Ethernet8           -              log
#log1.dell.com   6         Ethernet28          -              log
#
#
# Using overridden
#
# Before state:
# -------------
#
#sonic# show logging servers
#--------------------------------------------------------------------------------
#HOST            PORT      SOURCE-INTERFACE    VRF            MESSGE-TYPE
#--------------------------------------------------------------------------------
#10.11.1.1       616       Ethernet8           -              log
#10.11.1.2       626       Ethernet16          -              event
#
- name: Replace logging server configuration
  sonic_logging:
    config:
      remote_servers:
        - host: 10.11.1.2
          remote_port: 622
          source_interface: Ethernet24
          message_type: event
    state: overridden
#
# After state:
# ------------
#
#sonic# show logging servers
#--------------------------------------------------------------------------------
#HOST            PORT      SOURCE-INTERFACE    VRF            MESSGE-TYPE
#--------------------------------------------------------------------------------
#10.11.1.2       622       Ethernet24          -              event
#
# Using replaced
#
# Before state:
# -------------
#
#sonic# show logging servers
#--------------------------------------------------------------------------------
#HOST            PORT      SOURCE-INTERFACE    VRF            MESSGE-TYPE
#--------------------------------------------------------------------------------
#10.11.1.1       616       Ethernet8           -              log
#10.11.1.2       626       Ethernet16          -              event
#
- name: Replace logging server configuration
  sonic_logging:
    config:
      remote_servers:
        - host: 10.11.1.2
          remote_port: 622
    state: replaced
#
# After state:
# ------------
#
# "MESSAGE-TYPE" has default value of "log"
#
#sonic# show logging servers
#--------------------------------------------------------------------------------
#HOST            PORT      SOURCE-INTERFACE    VRF            MESSGE-TYPE
#--------------------------------------------------------------------------------
#10.11.1.1       616       Ethernet8           -              log
#10.11.1.2       622       -                   -              log
#
```

## [Return Values](sonic_logging_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- 13. Zhang (@mingjunzhang2019)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
