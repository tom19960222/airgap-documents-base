---
collection: ansible
version: "8"
title: "community.general.oneandone_firewall_policy module – Configure 1&1 firewall policy"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/oneandone_firewall_policy_module.html
fetched_at: 2026-07-28T01:48:23+00:00
---
# community.general.oneandone_firewall_policy module – Configure 1&1 firewall policy

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](oneandone_firewall_policy_module.md#ansible-collections-community-general-oneandone-firewall-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.oneandone_firewall_policy`.

- [Synopsis](oneandone_firewall_policy_module.md#synopsis)
- [Requirements](oneandone_firewall_policy_module.md#requirements)
- [Parameters](oneandone_firewall_policy_module.md#parameters)
- [Attributes](oneandone_firewall_policy_module.md#attributes)
- [Examples](oneandone_firewall_policy_module.md#examples)
- [Return Values](oneandone_firewall_policy_module.md#return-values)

## [Synopsis](oneandone_firewall_policy_module.md#id1)

- Create, remove, reconfigure, update firewall policies. This module has a dependency on 1and1 >= 1.0.

Aliases: cloud.oneandone.oneandone_firewall_policy

## [Requirements](oneandone_firewall_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- 1and1
- python >= 2.6

## [Parameters](oneandone_firewall_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **add_rules**  list / elements=dictionary | A list of rules that will be added to an existing firewall policy. It is syntax is the same as the one used for rules parameter. Used in combination with update state.  **Default:** `[]` |
| **add_server_ips**  list / elements=string | A list of server identifiers (id or name) to be assigned to a firewall policy. Used in combination with update state.  **Default:** `[]` |
| **api_url**  string | Custom API URL. Overrides the ONEANDONE_API_URL environment variable. |
| **auth_token**  string | Authenticating API token provided by 1&1. |
| **description**  string | Firewall policy description. maxLength=256 |
| **firewall_policy**  string | The identifier (id or name) of the firewall policy used with update state. |
| **name**  string | Firewall policy name used with present state. Used as identifier (id or name) when used with absent state. maxLength=128 |
| **remove_rules**  list / elements=string | A list of rule ids that will be removed from an existing firewall policy. Used in combination with update state.  **Default:** `[]` |
| **remove_server_ips**  list / elements=string | A list of server IP ids to be unassigned from a firewall policy. Used in combination with update state.  **Default:** `[]` |
| **rules**  list / elements=dictionary | A list of rules that will be set for the firewall policy. Each rule must contain protocol parameter, in addition to three optional parameters (port_from, port_to, and source)  **Default:** `[]` |
| **state**  string | Define a firewall policy state to create, remove, or update.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"update"` |
| **wait**  boolean | wait for the instance to be in state ‘running’ before returning  **Choices:**   - `false` - `true` ← (default) |
| **wait_interval**  integer | Defines the number of seconds to wait when using the _wait_for methods  **Default:** `5` |
| **wait_timeout**  integer | how long before wait gives up, in seconds  **Default:** `600` |

## [Attributes](oneandone_firewall_policy_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](oneandone_firewall_policy_module.md#id5)

```yaml+jinja
- name: Create a firewall policy
  community.general.oneandone_firewall_policy:
    auth_token: oneandone_private_api_key
    name: ansible-firewall-policy
    description: Testing creation of firewall policies with ansible
    rules:
     -
       protocol: TCP
       port_from: 80
       port_to: 80
       source: 0.0.0.0
    wait: true
    wait_timeout: 500

- name: Destroy a firewall policy
  community.general.oneandone_firewall_policy:
    auth_token: oneandone_private_api_key
    state: absent
    name: ansible-firewall-policy

- name: Update a firewall policy
  community.general.oneandone_firewall_policy:
    auth_token: oneandone_private_api_key
    state: update
    firewall_policy: ansible-firewall-policy
    name: ansible-firewall-policy-updated
    description: Testing creation of firewall policies with ansible - updated

- name: Add server to a firewall policy
  community.general.oneandone_firewall_policy:
    auth_token: oneandone_private_api_key
    firewall_policy: ansible-firewall-policy-updated
    add_server_ips:
     - server_identifier (id or name)
     - server_identifier #2 (id or name)
    wait: true
    wait_timeout: 500
    state: update

- name: Remove server from a firewall policy
  community.general.oneandone_firewall_policy:
    auth_token: oneandone_private_api_key
    firewall_policy: ansible-firewall-policy-updated
    remove_server_ips:
     - B2504878540DBC5F7634EB00A07C1EBD (server's IP id)
    wait: true
    wait_timeout: 500
    state: update

- name: Add rules to a firewall policy
  community.general.oneandone_firewall_policy:
    auth_token: oneandone_private_api_key
    firewall_policy: ansible-firewall-policy-updated
    description: Adding rules to an existing firewall policy
    add_rules:
     -
       protocol: TCP
       port_from: 70
       port_to: 70
       source: 0.0.0.0
     -
       protocol: TCP
       port_from: 60
       port_to: 60
       source: 0.0.0.0
    wait: true
    wait_timeout: 500
    state: update

- name: Remove rules from a firewall policy
  community.general.oneandone_firewall_policy:
    auth_token: oneandone_private_api_key
    firewall_policy: ansible-firewall-policy-updated
    remove_rules:
     - rule_id #1
     - rule_id #2
     - ...
    wait: true
    wait_timeout: 500
    state: update
```

## [Return Values](oneandone_firewall_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **firewall_policy**  dictionary | Information about the firewall policy that was processed  **Returned:** always  **Sample:** `{"id": "92B74394A397ECC3359825C1656D67A6", "name": "Default Policy"}` |

### Authors

- Amel Ajdinovic (@aajdinov)
- Ethan Devenport (@edevenport)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
