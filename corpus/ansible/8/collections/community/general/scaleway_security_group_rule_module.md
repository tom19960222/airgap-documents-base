---
collection: ansible
version: "8"
title: "community.general.scaleway_security_group_rule module – Scaleway Security Group Rule management module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/scaleway_security_group_rule_module.html
fetched_at: 2026-07-28T01:50:23+00:00
---
# community.general.scaleway_security_group_rule module – Scaleway Security Group Rule management module

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.scaleway_security_group_rule`.

- [Synopsis](scaleway_security_group_rule_module.md#synopsis)
- [Parameters](scaleway_security_group_rule_module.md#parameters)
- [Attributes](scaleway_security_group_rule_module.md#attributes)
- [Notes](scaleway_security_group_rule_module.md#notes)
- [Examples](scaleway_security_group_rule_module.md#examples)
- [Return Values](scaleway_security_group_rule_module.md#return-values)

## [Synopsis](scaleway_security_group_rule_module.md#id1)

- This module manages Security Group Rule on Scaleway account <https://developer.scaleway.com>.

Aliases: cloud.scaleway.scaleway_security_group_rule

## [Parameters](scaleway_security_group_rule_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string / required | Rule action.  **Choices:**   - `"accept"` - `"drop"` |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  **Default:** `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL.  **Default:** `"https://api.scaleway.com"` |
| **direction**  string / required | Rule direction.  **Choices:**   - `"inbound"` - `"outbound"` |
| **ip_range**  string | IPV4 CIDR notation to apply to the rule.  **Default:** `"0.0.0.0/0"` |
| **port**  integer / required | Port related to the rule, null value for all the ports. |
| **protocol**  string / required | Network protocol to use.  **Choices:**   - `"TCP"` - `"UDP"` - `"ICMP"` |
| **query_parameters**  dictionary | List of parameters passed to the query string.  **Default:** `{}` |
| **region**  string / required | Scaleway region to use (for example `par1`).  **Choices:**   - `"ams1"` - `"EMEA-NL-EVS"` - `"par1"` - `"EMEA-FR-PAR1"` - `"par2"` - `"EMEA-FR-PAR2"` - `"waw1"` - `"EMEA-PL-WAW1"` |
| **security_group**  string / required | Security Group unique identifier. |
| **state**  string | Indicate desired state of the Security Group Rule.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](scaleway_security_group_rule_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](scaleway_security_group_rule_module.md#id4)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence [`SCW_TOKEN`](../../environment_variables.md#envvar-SCW_TOKEN), [`SCW_API_KEY`](../../environment_variables.md#envvar-SCW_API_KEY), [`SCW_OAUTH_TOKEN`](../../environment_variables.md#envvar-SCW_OAUTH_TOKEN) or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_security_group_rule_module.md#id5)

```yaml+jinja
- name: Create a Security Group Rule
  community.general.scaleway_security_group_rule:
    state: present
    region: par1
    protocol: TCP
    port: 80
    ip_range: 0.0.0.0/0
    direction: inbound
    action: accept
    security_group: b57210ee-1281-4820-a6db-329f78596ecb
  register: security_group_rule_creation_task
```

## [Return Values](scaleway_security_group_rule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | This is only present when `state=present`.  **Returned:** when `state=present`  **Sample:** `{"scaleway_security_group_rule": {"action": "accept", "dest_port_from": 80, "dest_port_to": null, "direction": "inbound", "editable": null, "id": "10cb0b9a-80f6-4830-abd7-a31cd828b5e9", "ip_range": "0.0.0.0/0", "position": 2, "protocol": "TCP"}}` |

### Authors

- Antoine Barbare (@abarbare)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
