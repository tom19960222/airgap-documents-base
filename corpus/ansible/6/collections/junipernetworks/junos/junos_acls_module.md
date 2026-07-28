---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_acls module – ACLs resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_acls_module.html
fetched_at: 2026-07-27T17:54:10+00:00
---
# junipernetworks.junos.junos_acls module – ACLs resource module

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
> see [Requirements](junos_acls_module.md#ansible-collections-junipernetworks-junos-junos-acls-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_acls`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_acls_module.md#synopsis)
- [Requirements](junos_acls_module.md#requirements)
- [Parameters](junos_acls_module.md#parameters)
- [Notes](junos_acls_module.md#notes)
- [Examples](junos_acls_module.md#examples)
- [Return Values](junos_acls_module.md#return-values)

## [Synopsis](junos_acls_module.md#id1)

- This module provides declarative management of acls/filters on Juniper JUNOS devices

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_acls_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_acls_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of acls options |
| **acls**  list / elements=dictionary | List of Access Control Lists (ACLs). |
| **aces**  list / elements=dictionary | List of Access Control Entries (ACEs) for this Access Control List (ACL). |
| **destination**  dictionary | Specifies the destination for the filter |
| **address**  any | Match IP destination address |
| **port_protocol**  dictionary | Specify the destination port or protocol. |
| **eq**  string | Match only packets on a given port number. |
| **range**  dictionary | Match only packets in the range of port numbers |
| **end**  integer | Specify the end of the port range |
| **start**  integer | Specify the start of the port range |
| **prefix_list**  list / elements=dictionary | Match IP destination prefixes in named list |
| **name**  string | Name of the list |
| **grant**  string | Action to take after matching condition (allow, discard/reject)  Choices:   - `"permit"` - `"deny"` |
| **name**  string / required | Filter term name |
| **protocol**  string | Specify the protocol to match.  Refer to vendor documentation for valid values. |
| **protocol_options**  dictionary | All possible suboptions for the protocol chosen. |
| **icmp**  dictionary | ICMP protocol options. |
| **dod_host_prohibited**  boolean | Host prohibited  Choices:   - `false` - `true` |
| **dod_net_prohibited**  boolean | Net prohibited  Choices:   - `false` - `true` |
| **echo**  boolean | Echo (ping)  Choices:   - `false` - `true` |
| **echo_reply**  boolean | Echo reply  Choices:   - `false` - `true` |
| **host_redirect**  boolean | Host redirect  Choices:   - `false` - `true` |
| **host_tos_redirect**  boolean | Host redirect for TOS  Choices:   - `false` - `true` |
| **host_tos_unreachable**  boolean | Host unreachable for TOS  Choices:   - `false` - `true` |
| **host_unknown**  boolean | Host unknown  Choices:   - `false` - `true` |
| **host_unreachable**  boolean | Host unreachable  Choices:   - `false` - `true` |
| **net_redirect**  boolean | Network redirect  Choices:   - `false` - `true` |
| **net_tos_redirect**  boolean | Net redirect for TOS  Choices:   - `false` - `true` |
| **network_unknown**  boolean | Network unknown  Choices:   - `false` - `true` |
| **port_unreachable**  boolean | Port unreachable  Choices:   - `false` - `true` |
| **protocol_unreachable**  boolean | Protocol unreachable  Choices:   - `false` - `true` |
| **reassembly_timeout**  boolean | Reassembly timeout  Choices:   - `false` - `true` |
| **redirect**  boolean | All redirects  Choices:   - `false` - `true` |
| **router_advertisement**  boolean | Router discovery advertisements  Choices:   - `false` - `true` |
| **router_solicitation**  boolean | Router discovery solicitations  Choices:   - `false` - `true` |
| **source_route_failed**  boolean | Source route failed  Choices:   - `false` - `true` |
| **time_exceeded**  boolean | All time exceeded.  Choices:   - `false` - `true` |
| **ttl_exceeded**  boolean | TTL exceeded  Choices:   - `false` - `true` |
| **source**  dictionary | Specifies the source for the filter |
| **address**  any | IP source address to use for the filter |
| **port_protocol**  dictionary | Specify the source port or protocol. |
| **eq**  string | Match only packets on a given port number. |
| **range**  dictionary | Match only packets in the range of port numbers |
| **end**  integer | Specify the end of the port range |
| **start**  integer | Specify the start of the port range |
| **prefix_list**  list / elements=dictionary | IP source prefix list to use for the filter |
| **name**  string | Name of the list |
| **name**  string / required | Name to use for the acl filter |
| **afi**  string / required | Protocol family to use by the acl filter  Choices:   - `"ipv4"` - `"ipv6"` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show firewall**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state the configuration should be left in  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](junos_acls_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed
> - This module works with connection `netconf`
> - See [the Junos OS Platform Options](https://docsansiblecom/ansible/latest/network/user_guide/platform_junoshtml)
> - Tested against JunOS v18.4R1

## [Examples](junos_acls_module.md#id5)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# admin# show firewall

- name: Merge JUNOS acl
  junipernetworks.junos.junos_acls:
    config:
    - afi: ipv4
      acls:
      - name: allow_ssh_acl
        aces:
        - name: ssh_rule
          source:
            port_protocol:
              eq: ssh
          protocol: tcp
      state: merged

# After state:
# -------------
# admin# show firewall
# family inet {
#     filter allow_ssh_acl {
#         term ssh_rule {
#             from {
#                 protocol tcp;
#                 source-port ssh;
#             }
#         }
#     }
# }
```

## [Return Values](junos_acls_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["command 1", "command 2", "command 3"]` |

### Authors

- Daniel Mellado (@dmellado)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
