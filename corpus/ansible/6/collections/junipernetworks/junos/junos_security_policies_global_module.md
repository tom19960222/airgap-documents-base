---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_security_policies_global module – Manage global security policy settings on Juniper JUNOS devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_security_policies_global_module.html
fetched_at: 2026-07-27T17:54:37+00:00
---
# junipernetworks.junos.junos_security_policies_global module – Manage global security policy settings on Juniper JUNOS devices

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
> see [Requirements](junos_security_policies_global_module.md#ansible-collections-junipernetworks-junos-junos-security-policies-global-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_security_policies_global`.

New in junipernetworks.junos 2.9.0

- [Synopsis](junos_security_policies_global_module.md#synopsis)
- [Requirements](junos_security_policies_global_module.md#requirements)
- [Parameters](junos_security_policies_global_module.md#parameters)
- [Notes](junos_security_policies_global_module.md#notes)
- [Examples](junos_security_policies_global_module.md#examples)
- [Return Values](junos_security_policies_global_module.md#return-values)

## [Synopsis](junos_security_policies_global_module.md#id1)

- This module provides declarative management of global security policy settings on Juniper JUNOS devices

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_security_policies_global_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_security_policies_global_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of security policies |
| **default_policy**  string | Configure the default security policy that defines the actions the device takes on a packet that does not match any user-defined policy.  Choices:   - `"deny-all"` - `"permit-all"` |
| **policy_rematch**  dictionary | Enable the device to reevaluate an active session when its associated security policy is modified. The session remains open if it still matches the policy that allowed the session initially. |
| **enable**  boolean | Enable the device to reevaluate an active session when its associated security policy is modified. The session remains open if it still matches the policy that allowed the session initially.  Choices:   - `false` - `true` |
| **extensive**  boolean | When a policy is modified or deleted, extensive option checks if any suitable policy permit to keep these sessions alive.  Choices:   - `false` - `true` |
| **policy_stats**  dictionary | Configure policies statistics. |
| **enable**  boolean | Enable policies statistics.  Choices:   - `false` - `true` |
| **system_wide**  boolean | Configure systemwide policies statistics.  Choices:   - `false` - `true` |
| **pre_id_default_policy_action**  dictionary | Configures default policy actions that occur prior to dynamic application identification (AppID) when the packet matches the criteria. |
| **log**  dictionary | Specifies the log details at session close time and session initialization time. |
| **session_close**  boolean | Enable logging on session close time  Choices:   - `false` - `true` |
| **session_init**  boolean | Enable logging on session initialization time  Choices:   - `false` - `true` |
| **session_timeout**  dictionary | When you update a session, the session timeout is configured, which specifies the session timeout details in seconds. |
| **icmp**  integer | Timeout value for ICMP sessions (seconds) |
| **icmp6**  integer | Timeout value for ICMP6 sessions (seconds) |
| **ospf**  integer | Timeout value for OSPF sessions (seconds) |
| **others**  integer | Timeout value for other sessions (seconds) |
| **tcp**  integer | Timeout value for TCP sessions (seconds) |
| **udp**  integer | Timeout value for UDP sessions (seconds) |
| **traceoptions**  dictionary | A dictionary of security policies |
| **file**  dictionary | A dictionary to configure the trace file options |
| **files**  integer | Maximum number of trace files |
| **match**  string | Refine the output to include lines that contain the regular expression. |
| **no_world_readable**  boolean | Log files can be accessed only by the user who configures the tracing operation.  Choices:   - `false` - `true` |
| **size**  string | The maximum tracefile size |
| **world_readable**  boolean | The world_readable option enables any user to read the file.  Choices:   - `false` - `true` |
| **flag**  string | Trace operation to perform.  Choices:   - `"all"` - `"configuration"` - `"compilation"` - `"ipc"` - `"lookup"` - `"routing-socket"` - `"rules"` |
| **no_remote_trace**  boolean | Disable remote tracing.  Choices:   - `false` - `true` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the JunOS device by executing the command **show security policies**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required. behaviour for this module.  The state *replaced* will replace the running configuration with the provided configuration  The state *replaced* and state *overridden* have the same behaviour  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show security policies detail* executed on device. For state *parsed* active connection to remote host is not required.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"gathered"` - `"parsed"` |

## [Notes](junos_security_policies_global_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - This module works with connection `netconf`.
> - See [the Junos OS Platform Options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
> - Tested against JunOS v18.4R1

## [Examples](junos_security_policies_global_module.md#id5)

```yaml+jinja
# Using merged
#
# Before state
# ------------
#
# vagrant@vsrx# show security policies
# default-policy {
#   permit-all;
# }
#
- name: Update the running configuration with provided configuration
  junipernetworks.junos.junos_security_policies_global:
    config:
      policy_rematch:
        enable: true
      policy_stats:
        enable: true
      pre_id_default_policy_action:
        log:
          session_init: true
        session_timeout:
          icmp: 10
          others: 10
      traceoptions:
        file:
          files: 4
          match: /[A-Z]*/gm
          size: 10k
          no_world_readable: true
        flag: all
        no_remote_trace: true
    state: merged
#
# -------------------------
# Module Execution Result
# -------------------------
# "after": {
#     "default_policy": "permit-all",
#     "policy_rematch": {
#         "enable": true,
#         "extensive": true
#     },
#     "policy_stats": {
#         "enable": true,
#         "system_wide": true
#     },
#     "pre_id_default_policy_action": {
#         "log": {
#             "session_init": true
#         },
#         "session_timeout": {
#             "icmp": 10,
#             "others": 10
#         }
#     },
#     "traceoptions": {
#         "file": {
#             "files": 3,
#             "match": "/[A-Z]*/gm",
#             "no_world_readable": true,
#             "size": "10k"
#         },
#         "flag": "all",
#         "no_remote_trace": true
#     }
# },
# "before": {},
# "changed": true,
# "commands": "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:policies>
#   <nc:policy-rematch> <nc:extensive/></nc:policy-rematch><nc:policy-stats>
#   <nc:system-wide>enable</nc:system-wide></nc:policy-stats><nc:pre-id-default-policy>
#   <nc:then><nc:log><nc:session-init/></nc:log><nc:session-timeout><nc:icmp>10</nc:icmp>
#   <nc:others>10</nc:others></nc:session-timeout></nc:then></nc:pre-id-default-policy>
#   <nc:traceoptions><nc:file><nc:files>3</nc:files><nc:match>/[A-Z]*/gm</nc:match>
#   <nc:size>10k</nc:size><nc:no-world-readable/></nc:file><nc:flag><nc:name>all
#   </nc:name></nc:flag><nc:no-remote-trace/></nc:traceoptions></nc:policies></nc:security>"
# After state
# -----------
#
# vagrant@vsrx# show security policies
# traceoptions {
#   no-remote-trace;
#   file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
#   flag all;
# }
# default-policy {
#   permit-all;
# }
# policy-rematch extensive;
# policy-stats;
# pre-id-default-policy {
#   then {
#     log {
#       session-init;
#     }
#     session-timeout {
#       icmp 10;
#       others 10;
#     }
#   }
# }
#
#
# Using Replaced
# Before state
# ------------
#
# vagrant@vsrx# show security policies
# traceoptions {
#   no-remote-trace;
#   file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
#   flag all;
# }
# default-policy {
#   permit-all;
# }
# policy-rematch extensive;
# policy-stats;
# pre-id-default-policy {
#   then {
#     log {
#       session-init;
#     }
#     session-timeout {
#       icmp 10;
#       others 10;
#     }
#   }
# }

- name: Replace the running configuration with provided configuration
  junipernetworks.junos.junos_security_policies_global:
    config:
      default_policy: deny-all
      policy_rematch:
        enable: true
      policy_stats:
        enable: true
      pre_id_default_policy_action:
        log:
          session_init: true
        session_timeout:
          icmp: 10
          others: 10
      traceoptions:
        file:
          files: 4
          match: /[A-Z]*/gm
          size: 10k
          no_world_readable: true
        flag: all
        no_remote_trace: true
    state: replaced
#
# -------------------------
# Module Execution Result
# -------------------------
# "after": {
#     "default_policy": "deny-all",
#     "policy_rematch": {
#         "enable": true
#     },
#     "policy_stats": {
#         "enable": true
#     },
#     "pre_id_default_policy_action": {
#         "log": {
#             "session_init": true
#         },
#         "session_timeout": {
#             "icmp": 10,
#             "others": 10
#         }
#     },
#     "traceoptions": {
#         "file": {
#             "files": 4,
#             "match": "/[A-Z]*/gm",
#             "no_world_readable": true,
#             "size": "10k"
#         },
#         "flag": "all",
#         "no_remote_trace": true
#     }
# },
# "before": {
#     "default_policy": "permit-all",
#     "policy_rematch": {
#         "enable": true,
#         "extensive": true
#     },
#     "policy_stats": {
#         "enable": true
#     },
#     "pre_id_default_policy_action": {
#         "log": {
#             "session_init": true
#         },
#         "session_timeout": {
#             "icmp": 10,
#             "others": 10
#         }
#     },
#     "traceoptions": {
#         "file": {
#             "files": 4,
#             "match": "/[A-Z]*/gm",
#             "no_world_readable": true,
#             "size": "10k"
#         },
#         "flag": "all",
#         "no_remote_trace": true
#     }
# },
# "changed": true,
# "commands": "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
# <nc:policies delete="delete"/><nc:policies><nc:default-policy><nc:deny-all/></nc:default-policy>
# <nc:policy-rematch> </nc:policy-rematch><nc:policy-stats> </nc:policy-stats><nc:pre-id-default-policy>
# <nc:then><nc:log><nc:session-init/></nc:log><nc:session-timeout><nc:icmp>10</nc:icmp><nc:others>10
# </nc:others></nc:session-timeout></nc:then></nc:pre-id-default-policy><nc:traceoptions><nc:file>
# <nc:files>4</nc:files><nc:match>/[A-Z]*/gm</nc:match><nc:size>10k</nc:size><nc:no-world-readable/>
# </nc:file><nc:flag><nc:name>all</nc:name></nc:flag><nc:no-remote-trace/></nc:traceoptions></nc:policies>
# </nc:security>"
#
# After state
# -----------
#
# vagrant@vsrx# show security policies
# traceoptions {
#     no-remote-trace;
#     file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
#     flag all;
# }
# default-policy {
#     deny-all;
# }
# policy-rematch;
# policy-stats;
# pre-id-default-policy {
#     then {
#         log {
#             session-init;
#         }
#         session-timeout {
#             icmp 10;
#             others 10;
#         }
#     }
# }

# Using overridden
#
# Before state
# ------------
#
# vagrant@vsrx# show security policies
# traceoptions {
#   no-remote-trace;
#   file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
#   flag all;
# }
# default-policy {
#   permit-all;
# }
# policy-rematch extensive;
# policy-stats;
# pre-id-default-policy {
#   then {
#     log {
#       session-init;
#     }
#     session-timeout {
#       icmp 10;
#       others 10;
#     }
#   }
# }

- name: Replace the running configuration with provided configuration
  junipernetworks.junos.junos_security_policies_global:
    config:
      default_policy: deny-all
      policy_rematch:
        enable: true
      policy_stats:
        enable: true
      pre_id_default_policy_action:
        log:
          session_init: true
        session_timeout:
          icmp: 10
          others: 10
      traceoptions:
        file:
          files: 4
          match: /[A-Z]*/gm
          size: 10k
          no_world_readable: true
        flag: all
        no_remote_trace: true
    state: overridden
#
# -------------------------
# Module Execution Result
# -------------------------
# "after": {
#     "default_policy": "deny-all",
#     "policy_rematch": {
#         "enable": true
#     },
#     "policy_stats": {
#         "enable": true
#     },
#     "pre_id_default_policy_action": {
#         "log": {
#             "session_init": true
#         },
#         "session_timeout": {
#             "icmp": 10,
#             "others": 10
#         }
#     },
#     "traceoptions": {
#         "file": {
#             "files": 4,
#             "match": "/[A-Z]*/gm",
#             "no_world_readable": true,
#             "size": "10k"
#         },
#         "flag": "all",
#         "no_remote_trace": true
#     }
# },
# "before": {
#     "default_policy": "permit-all",
#     "policy_rematch": {
#         "enable": true,
#         "extensive": true
#     },
#     "policy_stats": {
#         "enable": true
#     },
#     "pre_id_default_policy_action": {
#         "log": {
#             "session_init": true
#         },
#         "session_timeout": {
#             "icmp": 10,
#             "others": 10
#         }
#     },
#     "traceoptions": {
#         "file": {
#             "files": 4,
#             "match": "/[A-Z]*/gm",
#             "no_world_readable": true,
#             "size": "10k"
#         },
#         "flag": "all",
#         "no_remote_trace": true
#     }
# },
# "changed": true,
# "commands": "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
# <nc:policies delete="delete"/><nc:policies><nc:default-policy><nc:deny-all/></nc:default-policy>
# <nc:policy-rematch> </nc:policy-rematch><nc:policy-stats> </nc:policy-stats><nc:pre-id-default-policy>
# <nc:then><nc:log><nc:session-init/></nc:log><nc:session-timeout><nc:icmp>10</nc:icmp><nc:others>10
# </nc:others></nc:session-timeout></nc:then></nc:pre-id-default-policy><nc:traceoptions><nc:file>
# <nc:files>4</nc:files><nc:match>/[A-Z]*/gm</nc:match><nc:size>10k</nc:size><nc:no-world-readable/>
# </nc:file><nc:flag><nc:name>all</nc:name></nc:flag><nc:no-remote-trace/></nc:traceoptions></nc:policies>
# </nc:security>"
#
# After state
# -----------
#
# vagrant@vsrx# show security policies
# traceoptions {
#     no-remote-trace;
#     file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
#     flag all;
# }
# default-policy {
#     deny-all;
# }
# policy-rematch;
# policy-stats;
# pre-id-default-policy {
#     then {
#         log {
#             session-init;
#         }
#         session-timeout {
#             icmp 10;
#             others 10;
#         }
#     }
# }
#
# Using deleted
#
# Before state
# ------------
#
# vagrant@vsrx# show security policies
# traceoptions {
#     no-remote-trace;
#     file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
#     flag all;
# }
# default-policy {
#     deny-all;
# }
# policy-rematch;
# policy-stats;
# pre-id-default-policy {
#     then {
#         log {
#             session-init;
#         }
#         session-timeout {
#             icmp 10;
#             others 10;
#         }
#     }
# }
#
- name: Delete the running configuration
  junipernetworks.junos.junos_security_policies_global:
    config:
    state: deleted
#
# -------------------------
# Module Execution Result
# -------------------------
# "after": {},
# "before": {
#     "default_policy": "deny-all",
#     "policy_rematch": {
#         "enable": true
#     },
#     "policy_stats": {
#         "enable": true
#     },
#     "pre_id_default_policy_action": {
#         "log": {
#             "session_init": true
#         },
#         "session_timeout": {
#             "icmp": 10,
#             "others": 10
#         }
#     },
#     "traceoptions": {
#         "file": {
#             "files": 4,
#             "match": "/[A-Z]*/gm",
#             "no_world_readable": true,
#             "size": "10k"
#         },
#         "flag": "all",
#         "no_remote_trace": true
#     }
# },
# "changed": true,
# "commands": "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#               <nc:policies delete="delete"/></nc:security>"
#
# After state
# -----------
#
# vagrant@vsrx# show security policies
#
#
# Using gathered
#
# Before state
# ------------
#
# vagrant@vsrx# show security policies
# traceoptions {
#     no-remote-trace;
#     file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
#     flag all;
# }
# default-policy {
#     deny-all;
# }
# policy-rematch;
# policy-stats;
# pre-id-default-policy {
#     then {
#         log {
#             session-init;
#         }
#         session-timeout {
#             icmp 10;
#             others 10;
#         }
#     }
# }
#
- name: Gather the running configuration
  junipernetworks.junos.junos_security_policies_global:
    config:
    state: gathered
#
# -------------------------
# Module Execution Result
# -------------------------
# "gathered": {
#     "default_policy": "deny-all",
#     "policy_rematch": {
#         "enable": true
#     },
#     "policy_stats": {
#         "enable": true
#     },
#     "pre_id_default_policy_action": {
#         "log": {
#             "session_init": true
#         },
#         "session_timeout": {
#             "icmp": 10,
#             "others": 10
#         }
#     },
#     "traceoptions": {
#         "file": {
#             "files": 4,
#             "match": "/[A-Z]*/gm",
#             "no_world_readable": true,
#             "size": "10k"
#         },
#         "flag": "all",
#         "no_remote_trace": true
#     }
# }
#
# Using rendered
#
# Before state
# ------------
#
- name: Render the provided configuration
  junipernetworks.junos.junos_security_policies_global:
    config:
      default_policy: deny-all
      policy_rematch:
        enable: true
      policy_stats:
        enable: true
      pre_id_default_policy_action:
        log:
          session_init: true
        session_timeout:
          icmp: 10
          others: 10
      traceoptions:
        file:
          files: 4
          match: /[A-Z]*/gm
          size: 10k
          no_world_readable: true
        flag: all
        no_remote_trace: true
    state: replaced
#
# -------------------------
# Module Execution Result
# -------------------------
#     "rendered": "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:policies>
#     <nc:default-policy><nc:deny-all/></nc:default-policy><nc:policy-rematch> </nc:policy-rematch>
#     <nc:policy-stats> </nc:policy-stats><nc:pre-id-default-policy><nc:then><nc:log><nc:session-init/>
#     </nc:log><nc:session-timeout><nc:icmp>10</nc:icmp><nc:others>10</nc:others></nc:session-timeout>
#     </nc:then></nc:pre-id-default-policy><nc:traceoptions><nc:file><nc:files>4</nc:files>
#     <nc:match>/[A-Z]*/gm</nc:match><nc:size>10k</nc:size><nc:no-world-readable/></nc:file><nc:flag>
#     <nc:name>all</nc:name></nc:flag><nc:no-remote-trace/></nc:traceoptions></nc:policies>
#     </nc:security>"
#
# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#    <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#       <version>18.4R1-S2.4</version>
#         <security>
#             <policies>
#                 <traceoptions>
#                     <no-remote-trace />
#                     <file>
#                         <size>10k</size>
#                         <files>3</files>
#                         <no-world-readable />
#                         <match>/[A-Z]*/gm</match>
#                     </file>
#                     <flag>
#                         <name>all</name>
#                     </flag>
#                 </traceoptions>
#                 <default-policy>
#                     <permit-all />
#                 </default-policy>
#                 <policy-rematch>
#                     <extensive />
#                 </policy-rematch>
#                 <policy-stats>
#                     <system-wide>enable</system-wide>
#                 </policy-stats>
#                 <pre-id-default-policy>
#                     <then>
#                         <log>
#                             <session-init />
#                         </log>
#                         <session-timeout>
#                             <icmp>10</icmp>
#                             <others>10</others>
#                         </session-timeout>
#                     </then>
#                 </pre-id-default-policy>
#             </policies>
#         </security>
#     </configuration>
# </rpc-reply>
#
#
- name: Parse security policies global running config
  junipernetworks.junos.junos_security_policies_global:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": {
#     "default_policy": "permit-all",
#     "policy_rematch": {
#         "enable": true,
#         "extensive": true
#     },
#     "policy_stats": {
#         "enable": true,
#         "system_wide": true
#     },
#     "pre_id_default_policy_action": {
#         "log": {
#             "session_init": true
#         },
#         "session_timeout": {
#             "icmp": 10,
#             "others": 10
#         }
#     },
#     "traceoptions": {
#         "file": {
#             "files": 3,
#             "match": "/[A-Z]*/gm",
#             "no_world_readable": true,
#             "size": "10k"
#         },
#         "flag": "all",
#         "no_remote_trace": true
#     }
# }
#
#
```

## [Return Values](junos_security_policies_global_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  Returned: when changed  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  Returned: when state is *merged*, *replaced*, *overridden*, *deleted*  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: when state is *merged*, *replaced*, *overridden* or *deleted*  Sample: `["<rpc-reply> <configuration> <security> <policies> <default-policy> <permit-all /> </default-policy> </policies> </security> </configuration> </rpc-reply>"]` |
| **gathered**  dictionary | Facts about the network resource gathered from the remote device as structured data.  Returned: when state is *gathered*  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **parsed**  dictionary | The device native config provided in *running_config* option parsed into structured data as per module argspec.  Returned: when state is *parsed*  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **rendered**  dictionary | The provided configuration in the task rendered in device-native format (offline).  Returned: when state is *rendered*  Sample: `["<rpc-reply> <configuration> <security> <policies> <default-policy> <permit-all /> </default-policy> </policies> </security> </configuration> </rpc-reply>"]` |

### Authors

- Pranav Bhatt (@pranav-bhatt)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
