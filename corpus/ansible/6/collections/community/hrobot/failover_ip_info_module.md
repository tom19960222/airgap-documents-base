---
collection: ansible
version: "6"
title: "community.hrobot.failover_ip_info module – Retrieve information on Hetzner’s failover IPs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/hrobot/failover_ip_info_module.html
fetched_at: 2026-07-27T17:15:51+00:00
---
# community.hrobot.failover_ip_info module – Retrieve information on Hetzner’s failover IPs

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
> To use it in a playbook, specify: `community.hrobot.failover_ip_info`.

- [Synopsis](failover_ip_info_module.md#synopsis)
- [Parameters](failover_ip_info_module.md#parameters)
- [Attributes](failover_ip_info_module.md#attributes)
- [See Also](failover_ip_info_module.md#see-also)
- [Examples](failover_ip_info_module.md#examples)
- [Return Values](failover_ip_info_module.md#return-values)

## [Synopsis](failover_ip_info_module.md#id1)

- Retrieve information on Hetzner’s failover IPs.

## [Parameters](failover_ip_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **failover_ip**  string / required | The failover IP address. |
| **hetzner_password**  string / required | The password for the Robot webservice user. |
| **hetzner_user**  string / required | The username for the Robot webservice user. |

## [Attributes](failover_ip_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action group: community.hrobot.robot  added in community.hrobot 1.6.0 | Use `group/community.hrobot.robot` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support:  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](failover_ip_info_module.md#id4)

> **See also:**
>
> [Failover IP documentation](https://docs.hetzner.com/robot/dedicated-server/ip/failover/)
> :   Hetzner’s documentation on failover IPs.
>
> [community.hrobot.failover_ip](failover_ip_module.md#ansible-collections-community-hrobot-failover-ip-module)
> :   Manage failover IPs.

## [Examples](failover_ip_info_module.md#id5)

```yaml+jinja
- name: Get value of failover IP 1.2.3.4
  community.hrobot.failover_ip_info:
    hetzner_user: foo
    hetzner_password: bar
    failover_ip: 1.2.3.4
    value: 5.6.7.8
  register: result

- name: Print value of failover IP 1.2.3.4 in case it is routed
  ansible.builtin.debug:
    msg: "1.2.3.4 routes to {{ result.value }}"
  when: result.state == 'routed'
```

## [Return Values](failover_ip_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failover_ip**  string | The failover IP.  Returned: success  Sample: `"1.2.3.4"` |
| **failover_netmask**  string | The netmask for the failover IP.  Returned: success  Sample: `"255.255.255.255"` |
| **server_ip**  string | The main IP of the server this failover IP is associated to.  This is *not* the server the failover IP is routed to.  Returned: success |
| **server_number**  integer | The number of the server this failover IP is associated to.  This is *not* the server the failover IP is routed to.  Returned: success |
| **state**  string | Will be `routed` or `unrouted`.  Returned: success |
| **value**  string | The value of the failover IP.  Will be `none` if the IP is unrouted.  Returned: success |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.hrobot/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.hrobot)
[Submit a bug report](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-hrobot)
