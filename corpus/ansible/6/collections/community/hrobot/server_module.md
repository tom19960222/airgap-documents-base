---
collection: ansible
version: "6"
title: "community.hrobot.server module – Update server information"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/hrobot/server_module.html
fetched_at: 2026-07-27T17:15:54+00:00
---
# community.hrobot.server module – Update server information

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
> To use it in a playbook, specify: `community.hrobot.server`.

New in community.hrobot 1.2.0

- [Synopsis](server_module.md#synopsis)
- [Parameters](server_module.md#parameters)
- [Attributes](server_module.md#attributes)
- [Examples](server_module.md#examples)
- [Return Values](server_module.md#return-values)

## [Synopsis](server_module.md#id1)

- Allows to update server information.
- Right now the API only supports updating the server’s name.

## [Parameters](server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hetzner_password**  string / required | The password for the Robot webservice user. |
| **hetzner_user**  string / required | The username for the Robot webservice user. |
| **server_name**  string | The server’s name.  If this option is not provided, it will not be adjusted. |
| **server_number**  integer / required | The server number of the server to update. |

## [Attributes](server_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action group: community.hrobot.robot  added in community.hrobot 1.6.0 | Use `group/community.hrobot.robot` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](server_module.md#id4)

```yaml+jinja
- name: Set server's name to foo.example.com
  community.hrobot.server:
    hetzner_user: foo
    hetzner_password: bar
    server_number: 123
    server_name: foo.example.com
```

## [Return Values](server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **server**  dictionary | Information on the server.  Returned: success |
| **cancelled**  boolean | Whether the server is cancelled.  Returned: success  Sample: `false` |
| **cpanel**  boolean | Flag of cPanel installation availability.  Returned: success  Sample: `true` |
| **dc**  string | The data center the server is located in.  Returned: success  Sample: `"NBG1-DC1"` |
| **hot_swap**  boolean | Flag of Hot Swap availability.  Returned: success  Sample: `true` |
| **ip**  list / elements=string | List of assigned single IP addresses.  Returned: success  Sample: `["123.123.123.123"]` |
| **linked_storagebox**  integer | Linked Storage Box ID.  Returned: success  Sample: `12345` |
| **paid_until**  string | The date until the server has been paid.  Returned: success  Sample: `"2018-08-04"` |
| **plesk**  boolean | Flag of Plesk installation availability.  Returned: success  Sample: `true` |
| **product**  string | The server product name.  Returned: success  Sample: `"EQ 8"` |
| **rescue**  boolean | Whether the rescue system is available.  Returned: success  Sample: `false` |
| **reset**  boolean | Whether the server can be automatically reset.  Returned: success  Sample: `true` |
| **server_ip**  string | The server’s main IP address.  Returned: success  Sample: `"123.123.123.123"` |
| **server_ipv6_net**  string | The server’s main IPv6 network address.  Returned: success  Sample: `"2a01:f48:111:4221::"` |
| **server_name**  string | The user-defined server’s name.  Returned: success  Sample: `"server1"` |
| **server_number**  integer | The server’s numeric ID.  Returned: success  Sample: `321` |
| **status**  string | Server status.  Returned: success  Can only return:   - `"ready"` - `"in process"`   Sample: `"ready"` |
| **subnet**  list / elements=dictionary | List of assigned subnets.  Returned: success  Sample: `[{"ip": "2a01:4f8:111:4221::", "mask": 64}]` |
| **ip**  string | The first IP in the subnet.  Returned: success  Sample: `"2a01:4f8:111:4221::"` |
| **mask**  string | The masks bitlength.  Returned: success  Sample: `"64"` |
| **traffic**  string | Free traffic quota.  `unlimited` in case of unlimited traffic.  Returned: success  Sample: `"5 TB"` |
| **vnc**  boolean | Flag of VNC installation availability.  Returned: success  Sample: `true` |
| **windows**  boolean | Flag of Windows installation availability.  Returned: success  Sample: `true` |
| **wol**  boolean | Flag of Wake On Lan availability.  Returned: success  Sample: `true` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.hrobot/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.hrobot)
[Submit a bug report](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-hrobot)
