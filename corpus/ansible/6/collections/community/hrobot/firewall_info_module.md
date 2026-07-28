---
collection: ansible
version: "6"
title: "community.hrobot.firewall_info module – Manage Hetzner’s dedicated server firewall"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/hrobot/firewall_info_module.html
fetched_at: 2026-07-27T17:15:52+00:00
---
# community.hrobot.firewall_info module – Manage Hetzner’s dedicated server firewall

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
> To use it in a playbook, specify: `community.hrobot.firewall_info`.

- [Synopsis](firewall_info_module.md#synopsis)
- [Parameters](firewall_info_module.md#parameters)
- [Attributes](firewall_info_module.md#attributes)
- [See Also](firewall_info_module.md#see-also)
- [Examples](firewall_info_module.md#examples)
- [Return Values](firewall_info_module.md#return-values)

## [Synopsis](firewall_info_module.md#id1)

- Manage Hetzner’s dedicated server firewall.

## [Parameters](firewall_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hetzner_password**  string / required | The password for the Robot webservice user. |
| **hetzner_user**  string / required | The username for the Robot webservice user. |
| **server_ip**  string / required | The server’s main IP address. |
| **timeout**  integer | Timeout (in seconds) for waiting for firewall to be configured.  Default: `180` |
| **wait_delay**  integer | Delay to wait (in seconds) before checking again whether the firewall has been configured.  Default: `10` |
| **wait_for_configured**  boolean | Whether to wait until the firewall has been successfully configured before returning from the module.  The API returns status `in progress` when the firewall is currently being configured. If this happens, the module will try again until the status changes to `active` or `disabled`.  Please note that there is a request limit. If you have to do multiple updates, it can be better to disable waiting, and regularly use [community.hrobot.firewall_info](firewall_info_module.md#ansible-collections-community-hrobot-firewall-info-module) to query status.  Choices:   - `false` - `true` ← (default) |

## [Attributes](firewall_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action group: community.hrobot.robot  added in community.hrobot 1.6.0 | Use `group/community.hrobot.robot` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support:  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](firewall_info_module.md#id4)

> **See also:**
>
> [Firewall documentation](https://docs.hetzner.com/robot/dedicated-server/firewall/)
> :   Hetzner’s documentation on the stateless firewall for dedicated servers
>
> [community.hrobot.firewall](firewall_module.md#ansible-collections-community-hrobot-firewall-module)
> :   Configure firewall.

## [Examples](firewall_info_module.md#id5)

```yaml+jinja
- name: Get firewall configuration for server with main IP 1.2.3.4
  community.hrobot.firewall_info:
    hetzner_user: foo
    hetzner_password: bar
    server_ip: 1.2.3.4
  register: result

- ansible.builtin.debug:
    msg: "{{ result.firewall }}"
```

## [Return Values](firewall_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **firewall**  dictionary | The firewall configuration.  Returned: success |
| **allowlist_hos**  boolean  added in community.hrobot 1.2.0 | Whether Hetzner services have access.  Returned: success  Sample: `true` |
| **port**  string | Switch port of firewall.  `main` or `kvm`.  Returned: success  Sample: `"main"` |
| **rules**  dictionary | Firewall rules.  Returned: success |
| **input**  list / elements=dictionary | Input firewall rules.  Returned: success |
| **action**  string | Action if rule matches.  `accept` or `discard`.  Returned: success  Sample: `"accept"` |
| **dst_ip**  string | Destination IP address or subnet address.  CIDR notation.  Returned: success  Sample: `"1.2.3.4/32"` |
| **dst_port**  string | Destination port or port range.  Returned: success  Sample: `"443"` |
| **ip_version**  string | Internet protocol version.  Returned: success  Sample: `"ipv4"` |
| **name**  string | Name of the firewall rule.  Returned: success  Sample: `"Allow HTTP access to server"` |
| **protocol**  string | Protocol above IP layer  Returned: success  Sample: `"tcp"` |
| **src_ip**  string | Source IP address or subnet address.  CIDR notation.  Returned: success |
| **src_port**  string | Source port or port range.  Returned: success |
| **tcp_flags**  string | TCP flags or logical combination of flags.  Returned: success |
| **server_ip**  string | Server’s main IP address.  Returned: success  Sample: `"1.2.3.4"` |
| **server_number**  integer | Hetzner’s internal server number.  Returned: success  Sample: `12345` |
| **status**  string | Status of the firewall.  `active` or `disabled`.  Will be `in process` if the firewall is currently updated, and *wait_for_configured* is set to `false` or *timeout* to a too small value.  Returned: success  Sample: `"active"` |
| **whitelist_hos**  boolean | Whether Hetzner services have access.  Old name of return value `allowlist_hos`, will be removed eventually.  Returned: success  Sample: `true` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.hrobot/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.hrobot)
[Submit a bug report](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-hrobot)
