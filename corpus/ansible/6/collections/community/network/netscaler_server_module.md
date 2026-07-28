---
collection: ansible
version: "6"
title: "community.network.netscaler_server module – Manage server configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/netscaler_server_module.html
fetched_at: 2026-07-27T17:19:06+00:00
---
# community.network.netscaler_server module – Manage server configuration

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](netscaler_server_module.md#ansible-collections-community-network-netscaler-server-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.netscaler_server`.

- [Synopsis](netscaler_server_module.md#synopsis)
- [Requirements](netscaler_server_module.md#requirements)
- [Parameters](netscaler_server_module.md#parameters)
- [Notes](netscaler_server_module.md#notes)
- [Examples](netscaler_server_module.md#examples)
- [Return Values](netscaler_server_module.md#return-values)

## [Synopsis](netscaler_server_module.md#id1)

- Manage server entities configuration.
- This module is intended to run either on the ansible control node or a bastion (jumpserver) with access to the actual netscaler instance.

## [Requirements](netscaler_server_module.md#id2)

The below requirements are needed on the host that executes this module.

- nitro python sdk

## [Parameters](netscaler_server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **comment**  string | Any information about the server. |
| **delay**  string | Time, in seconds, after which all the services configured on the server are disabled.  This option is meaningful only when setting the *disabled* option to `true` |
| **disabled**  boolean | When set to `true` the server state will be set to `disabled`.  When set to `false` the server state will be set to `enabled`.  Note that due to limitations of the underlying NITRO API a `disabled` state change alone does not cause the module result to report a changed status.  Choices:   - `false` ← (default) - `true` |
| **domain**  string | Domain name of the server. For a domain based configuration, you must create the server first.  Minimum length = 1 |
| **domainresolveretry**  string | Time, in seconds, for which the NetScaler appliance must wait, after DNS resolution fails, before sending the next DNS query to resolve the domain name.  Minimum value = `5`  Maximum value = `20939`  Default: `5` |
| **graceful**  boolean | Shut down gracefully, without accepting any new connections, and disabling each service when all of its connections are closed.  This option is meaningful only when setting the *disabled* option to `true`  Choices:   - `false` - `true` |
| **ipaddress**  string | IPv4 or IPv6 address of the server. If you create an IP address based server, you can specify the name of the server, instead of its IP address, when creating a service. Note: If you do not create a server entry, the server IP address that you enter when you create a service becomes the name of the server. |
| **ipv6address**  boolean | Support IPv6 addressing mode. If you configure a server with the IPv6 addressing mode, you cannot use the server in the IPv4 addressing mode.  Choices:   - `false` ← (default) - `true` |
| **name**  string | Name for the server.  Must begin with an ASCII alphabetic or underscore `_` character, and must contain only ASCII alphanumeric, underscore `_`, hash `#`, period `.`, space , colon `:`, at `@`, equals `=`, and hyphen `-` characters.  Can be changed after the name is created.  Minimum length = 1 |
| **nitro_pass**  string / required | The password with which to authenticate to the netscaler node. |
| **nitro_protocol**  string | Which protocol to use when accessing the nitro API objects.  Choices:   - `"http"` ← (default) - `"https"` |
| **nitro_timeout**  float | Time in seconds until a timeout error is thrown when establishing a new session with Netscaler  Default: `310.0` |
| **nitro_user**  string / required | The username with which to authenticate to the netscaler node. |
| **nsip**  string / required | The ip address of the netscaler appliance where the nitro API calls will be made.  The port can be specified with the colon (:). E.g. 192.168.1.1:555. |
| **save_config**  boolean | If `yes` the module will save the configuration on the netscaler node if it makes any changes.  The module will not save the configuration on the netscaler node if it made no changes.  Choices:   - `false` - `true` ← (default) |
| **state**  string | The state of the resource being configured by the module on the netscaler node.  When present the resource will be created if needed and configured according to the module’s parameters.  When absent the resource will be deleted from the netscaler node.  Choices:   - `"absent"` - `"present"` ← (default) |
| **td**  string | Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.  Minimum value = `0`  Maximum value = `4094` |
| **translationip**  string | IP address used to transform the server’s DNS-resolved IP address. |
| **translationmask**  string | The netmask of the translation ip. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](netscaler_server_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Citrix NetScaler Network devices see <https://www.ansible.com/ansible-netscaler>.

## [Examples](netscaler_server_module.md#id5)

```yaml+jinja
- name: Setup server
  delegate_to: localhost
  community.network.netscaler_server:
      nsip: 172.18.0.2
      nitro_user: nsroot
      nitro_pass: nsroot

      state: present

      name: server-1
      ipaddress: 192.168.1.1
```

## [Return Values](netscaler_server_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff**  dictionary | List of differences between the actual configured object and the configuration specified in the module  Returned: failure  Sample: `{"targetlbvserver": "difference. ours: (str) server1 other: (str) server2"}` |
| **loglines**  list / elements=string | list of logged messages by the module  Returned: always  Sample: `["message 1", "message 2"]` |
| **msg**  string | Message detailing the failure reason  Returned: failure  Sample: `"Action does not exist"` |

### Authors

- George Nikolopoulos (@giorgos-nikolopoulos)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
