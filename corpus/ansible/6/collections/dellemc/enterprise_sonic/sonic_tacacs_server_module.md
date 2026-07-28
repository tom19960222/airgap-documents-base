---
collection: ansible
version: "6"
title: "dellemc.enterprise_sonic.sonic_tacacs_server module – Manage TACACS server and its parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/enterprise_sonic/sonic_tacacs_server_module.html
fetched_at: 2026-07-27T17:24:59+00:00
---
# dellemc.enterprise_sonic.sonic_tacacs_server module – Manage TACACS server and its parameters

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/dellemc/enterprise_sonic) (version 1.1.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_tacacs_server`.

New in dellemc.enterprise_sonic 1.1.0

- [Synopsis](sonic_tacacs_server_module.md#synopsis)
- [Parameters](sonic_tacacs_server_module.md#parameters)
- [Notes](sonic_tacacs_server_module.md#notes)
- [Examples](sonic_tacacs_server_module.md#examples)
- [Return Values](sonic_tacacs_server_module.md#return-values)

## [Synopsis](sonic_tacacs_server_module.md#id1)

- This module provides configuration management of tacacs server parameters on devices running Enterprise SONiC.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_tacacs_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Specifies the tacacs server related configuration. |
| **auth_type**  string | Specifies the authentication type of the tacacs server.  Choices:   - `"pap"` ← (default) - `"chap"` - `"mschap"` - `"login"` |
| **key**  string | Specifies the key of the tacacs server. |
| **servers**  dictionary | Specifies the servers list of the tacacs server. |
| **host**  list / elements=dictionary | Specifies the host details of the tacacs servers list. |
| **auth_type**  string | Specifies the authentication type of the tacacs server host.  Choices:   - `"pap"` ← (default) - `"chap"` - `"mschap"` - `"login"` |
| **key**  string | Specifies the key of the tacacs server host. |
| **name**  string | Specifies the name of the tacacs server host. |
| **port**  integer | Specifies the port of the tacacs server host.  Default: `49` |
| **priority**  integer | Specifies the priority of the tacacs server host.  Default: `1` |
| **timeout**  integer | Specifies the timeout of the tacacs server host.  Default: `5` |
| **vrf**  string | Specifies the vrf of the tacacs server host.  Default: `"default"` |
| **source_interface**  string | Specifies the source interface of the tacacs server. |
| **timeout**  integer | Specifies the timeout of the tacacs server. |
| **state**  string | Specifies the operation to be performed on the tacacs server configured on the device.  In case of merged, the input mode configuration will be merged with the existing tacacs server configuration on the device.  In case of deleted the existing tacacs server mode configuration will be removed from the device.  Choices:   - `"merged"` ← (default) - `"deleted"` |

## [Notes](sonic_tacacs_server_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_tacacs_server_module.md#id4)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#
# do show tacacs-server
#---------------------------------------------------------
#TACACS Global Configuration
#---------------------------------------------------------
#source-interface  : Ethernet12
#timeout    : 10
#auth-type  : login
#key        : login
#------------------------------------------------------------------------------------------------
#HOST                 AUTH-TYPE       KEY        PORT       PRIORITY   TIMEOUT    VRF
#------------------------------------------------------------------------------------------------
#1.2.3.4              pap             *****      50         2          10         mgmt
#localhost            pap                        49         1          5          default
#

- name: Merge tacacs configurations
  dellemc.enterprise_sonic.sonic_tacacs_server:
    config:
      auth_type: login
      key: login
      source_interface: Ethernet 12
      timeout: 10
      servers:
        host:
          - name: 1.2.3.4
    state: deleted

# After state:
# ------------
#
#do show tacacs-server
#---------------------------------------------------------
#TACACS Global Configuration
#---------------------------------------------------------
#timeout    : 5
#auth-type  : pap
#------------------------------------------------------------------------------------------------
#HOST                 AUTH-TYPE       KEY        PORT       PRIORITY   TIMEOUT    VRF
#------------------------------------------------------------------------------------------------
#localhost            pap                        49         1          5          default

# Using deleted
#
# Before state:
# -------------
#
# do show tacacs-server
#---------------------------------------------------------
#TACACS Global Configuration
#---------------------------------------------------------
#source-interface  : Ethernet12
#timeout    : 10
#auth-type  : login
#key        : login
#------------------------------------------------------------------------------------------------
#HOST                 AUTH-TYPE       KEY        PORT       PRIORITY   TIMEOUT    VRF
#------------------------------------------------------------------------------------------------
#1.2.3.4              pap             *****      50         2          10         mgmt
#localhost            pap                        49         1          5          default
#

- name: Merge tacacs configurations
  dellemc.enterprise_sonic.sonic_tacacs_server:
    config:
    state: deleted

# After state:
# ------------
#
#do show tacacs-server
#---------------------------------------------------------
#TACACS Global Configuration
#---------------------------------------------------------
#timeout    : 5
#auth-type  : pap

# Using merged
#
# Before state:
# -------------
#
#sonic(config)# do show tacacs-server
#---------------------------------------------------------
#TACACS Global Configuration
#---------------------------------------------------------
#
- name: Merge tacacs configurations
  dellemc.enterprise_sonic.sonic_tacacs_server:
    config:
      auth_type: pap
      key: pap
      source_interface: Ethernet 12
      timeout: 10
      servers:
        host:
          - name: 1.2.3.4
            auth_type: pap
            key: 1234
    state: merged

# After state:
# ------------
#
#sonic(config)# do show tacacs-server
#---------------------------------------------------------
#TACACS Global Configuration
#---------------------------------------------------------
#source-interface  : Ethernet12
#timeout    : 10
#auth-type  : pap
#key        : pap
#------------------------------------------------------------------------------------------------
#HOST                 AUTH-TYPE       KEY        PORT       PRIORITY   TIMEOUT    VRF
#------------------------------------------------------------------------------------------------
#1.2.3.4              pap             1234       49         1          5          default
```

## [Return Values](sonic_tacacs_server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["command 1", "command 2", "command 3"]` |

### Authors

- Niraimadaiselvam M (@niraimadaiselvamm)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
