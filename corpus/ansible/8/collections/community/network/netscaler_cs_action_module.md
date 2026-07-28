---
collection: ansible
version: "8"
title: "community.network.netscaler_cs_action module – Manage content switching actions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/netscaler_cs_action_module.html
fetched_at: 2026-07-28T01:57:03+00:00
---
# community.network.netscaler_cs_action module – Manage content switching actions

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](netscaler_cs_action_module.md#ansible-collections-community-network-netscaler-cs-action-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.netscaler_cs_action`.

- [Synopsis](netscaler_cs_action_module.md#synopsis)
- [Requirements](netscaler_cs_action_module.md#requirements)
- [Parameters](netscaler_cs_action_module.md#parameters)
- [Notes](netscaler_cs_action_module.md#notes)
- [Examples](netscaler_cs_action_module.md#examples)
- [Return Values](netscaler_cs_action_module.md#return-values)

## [Synopsis](netscaler_cs_action_module.md#id1)

- Manage content switching actions
- This module is intended to run either on the ansible control node or a bastion (jumpserver) with access to the actual netscaler instance

Aliases: network.netscaler.netscaler_cs_action

## [Requirements](netscaler_cs_action_module.md#id2)

The below requirements are needed on the host that executes this module.

- nitro python sdk

## [Parameters](netscaler_cs_action_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **comment**  string | Comments associated with this cs action. |
| **name**  string | Name for the content switching action. Must begin with an ASCII alphanumeric or underscore `_` character, and must contain only ASCII alphanumeric, underscore `_`, hash `#`, period `.`, space , colon `:`, at sign `@`, equal sign `=`, and hyphen `-` characters. Can be changed after the content switching action is created. |
| **nitro_pass**  string / required | The password with which to authenticate to the netscaler node. |
| **nitro_protocol**  string | Which protocol to use when accessing the nitro API objects.  **Choices:**   - `"http"` ← (default) - `"https"` |
| **nitro_timeout**  float | Time in seconds until a timeout error is thrown when establishing a new session with Netscaler  **Default:** `310.0` |
| **nitro_user**  string / required | The username with which to authenticate to the netscaler node. |
| **nsip**  string / required | The ip address of the netscaler appliance where the nitro API calls will be made.  The port can be specified with the colon (:). E.g. 192.168.1.1:555. |
| **save_config**  boolean | If `yes` the module will save the configuration on the netscaler node if it makes any changes.  The module will not save the configuration on the netscaler node if it made no changes.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | The state of the resource being configured by the module on the netscaler node.  When present the resource will be created if needed and configured according to the module’s parameters.  When absent the resource will be deleted from the netscaler node.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **targetlbvserver**  string | Name of the load balancing virtual server to which the content is switched. |
| **targetvserver**  string | Name of the VPN virtual server to which the content is switched. |
| **targetvserverexpr**  string | Information about this content switching action. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](netscaler_cs_action_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Citrix NetScaler Network devices see <https://www.ansible.com/ansible-netscaler>.

## [Examples](netscaler_cs_action_module.md#id5)

```yaml+jinja
# lb_vserver_1 must have been already created with the netscaler_lb_vserver module

- name: Configure netscaler content switching action
  delegate_to: localhost
  community.network.netscaler_cs_action:
      nsip: 172.18.0.2
      nitro_user: nsroot
      nitro_pass: nsroot
      validate_certs: false

      state: present

      name: action-1
      targetlbvserver: lb_vserver_1
```

## [Return Values](netscaler_cs_action_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff**  dictionary | List of differences between the actual configured object and the configuration specified in the module  **Returned:** failure  **Sample:** `{"targetlbvserver": "difference. ours: (str) server1 other: (str) server2"}` |
| **loglines**  list / elements=string | list of logged messages by the module  **Returned:** always  **Sample:** `["['message 1'", " 'message 2']"]` |
| **msg**  string | Message detailing the failure reason  **Returned:** failure  **Sample:** `"Action does not exist"` |

### Authors

- George Nikolopoulos (@giorgos-nikolopoulos)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
