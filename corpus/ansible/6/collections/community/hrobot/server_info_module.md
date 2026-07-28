---
collection: ansible
version: "6"
title: "community.hrobot.server_info module – Query information on one or more servers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/hrobot/server_info_module.html
fetched_at: 2026-07-27T17:15:55+00:00
---
# community.hrobot.server_info module – Query information on one or more servers

> **Note:**
>
> This module is part of the [community.hrobot collection](https://galaxy.ansible.com/community/hrobot) (version 1.6.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.hrobot`.
>
> To use it in a playbook, specify: `community.hrobot.server_info`.

New in community.hrobot 1.2.0

- [Synopsis](server_info_module.md#synopsis)
- [Parameters](server_info_module.md#parameters)
- [Attributes](server_info_module.md#attributes)
- [Examples](server_info_module.md#examples)
- [Return Values](server_info_module.md#return-values)

## [Synopsis](server_info_module.md#id1)

- Query information on one or more servers.

## [Parameters](server_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **full_info**  boolean | Whether to provide full information for every server.  Setting this to `true` requires one REST call per server, which is slow and reduces your rate limit. Use with care.  When *server_number* is specified, this option is set to `true`.  Choices:   - `false` ← (default) - `true` |
| **hetzner_password**  string / required | The password for the Robot webservice user. |
| **hetzner_user**  string / required | The username for the Robot webservice user. |
| **server_name**  string | Limit result list to servers of this name. |
| **server_number**  integer | Limit result list to server with this number. |

## [Attributes](server_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action group: community.hrobot.robot  added in community.hrobot 1.6.0 | Use `group/community.hrobot.robot` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support:  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](server_info_module.md#id4)

```yaml+jinja
- name: Query a list of all servers
  community.hrobot.server_info:
    hetzner_user: foo
    hetzner_password: bar
  register: result

- name: Query a specific server
  community.hrobot.server_info:
    hetzner_user: foo
    hetzner_password: bar
    server_number: 23
  register: result

- name: Output data on specific server
  ansible.builtin.debug:
    msg: "Server name: {{ result.servers[0].server_name }}"
```

## [Return Values](server_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **servers**  list / elements=dictionary | List of servers matching the provided options.  Returned: success |
| **cancelled**  boolean | Whether the server is cancelled.  Returned: success  Sample: `false` |
| **cpanel**  boolean | Flag of cPanel installation availability.  Returned: when *full_info=true*  Sample: `true` |
| **dc**  string | The data center the server is located in.  Returned: success  Sample: `"NBG1-DC1"` |
| **hot_swap**  boolean | Flag of Hot Swap availability.  Returned: when *full_info=true*  Sample: `true` |
| **ip**  list / elements=string | List of assigned single IP addresses.  Returned: success  Sample: `["123.123.123.123"]` |
| **linked_storagebox**  integer | Linked Storage Box ID.  Returned: when *full_info=true*  Sample: `12345` |
| **paid_until**  string | The date until the server has been paid.  Returned: success  Sample: `"2018-08-04"` |
| **plesk**  boolean | Flag of Plesk installation availability.  Returned: when *full_info=true*  Sample: `true` |
| **product**  string | The server product name.  Returned: success  Sample: `"EQ 8"` |
| **rescue**  boolean | Whether the rescue system is available.  Returned: when *full_info=true*  Sample: `false` |
| **reset**  boolean | Whether the server can be automatically reset.  Returned: when *full_info=true*  Sample: `true` |
| **server_ip**  string | The server’s main IP address.  Returned: success  Sample: `"123.123.123.123"` |
| **server_ipv6_net**  string | The server’s main IPv6 network address.  Returned: success  Sample: `"2a01:f48:111:4221::"` |
| **server_name**  string | The user-defined server’s name.  Returned: success  Sample: `"server1"` |
| **server_number**  integer | The server’s numeric ID.  Returned: success  Sample: `321` |
| **status**  string | Server status.  Returned: success  Can only return:   - `"ready"` - `"in process"`   Sample: `"ready"` |
| **subnet**  list / elements=dictionary | List of assigned subnets.  Returned: success  Sample: `[{"ip": "2a01:4f8:111:4221::", "mask": 64}]` |
| **ip**  string | The first IP in the subnet.  Returned: success  Sample: `"2a01:4f8:111:4221::"` |
| **mask**  string | The masks bitlength.  Returned: success  Sample: `"64"` |
| **traffic**  string | Free traffic quota.  `unlimited` in case of unlimited traffic.  Returned: success  Sample: `"5 TB"` |
| **vnc**  boolean | Flag of VNC installation availability.  Returned: when *full_info=true*  Sample: `true` |
| **windows**  boolean | Flag of Windows installation availability.  Returned: when *full_info=true*  Sample: `true` |
| **wol**  boolean | Flag of Wake On Lan availability.  Returned: when *full_info=true*  Sample: `true` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.hrobot/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.hrobot)
[Submit a bug report](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-hrobot)
