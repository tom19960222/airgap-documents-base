---
collection: ansible
version: "8"
title: "community.general.oneandone_load_balancer module – Configure 1&1 load balancer"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/oneandone_load_balancer_module.html
fetched_at: 2026-07-28T01:48:24+00:00
---
# community.general.oneandone_load_balancer module – Configure 1&1 load balancer

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
> see [Requirements](oneandone_load_balancer_module.md#ansible-collections-community-general-oneandone-load-balancer-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.oneandone_load_balancer`.

- [Synopsis](oneandone_load_balancer_module.md#synopsis)
- [Requirements](oneandone_load_balancer_module.md#requirements)
- [Parameters](oneandone_load_balancer_module.md#parameters)
- [Attributes](oneandone_load_balancer_module.md#attributes)
- [Examples](oneandone_load_balancer_module.md#examples)
- [Return Values](oneandone_load_balancer_module.md#return-values)

## [Synopsis](oneandone_load_balancer_module.md#id1)

- Create, remove, update load balancers. This module has a dependency on 1and1 >= 1.0.

Aliases: cloud.oneandone.oneandone_load_balancer

## [Requirements](oneandone_load_balancer_module.md#id2)

The below requirements are needed on the host that executes this module.

- 1and1
- python >= 2.6

## [Parameters](oneandone_load_balancer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **add_rules**  list / elements=dictionary | A list of rules that will be added to an existing load balancer. It is syntax is the same as the one used for rules parameter. Used in combination with update state.  **Default:** `[]` |
| **add_server_ips**  list / elements=string | A list of server identifiers (id or name) to be assigned to a load balancer. Used in combination with update state.  **Default:** `[]` |
| **api_url**  string | Custom API URL. Overrides the `ONEANDONE_API_URL` environment variable. |
| **auth_token**  string | Authenticating API token provided by 1&1. |
| **datacenter**  string | ID or country code of the datacenter where the load balancer will be created.  If not specified, it defaults to `US`.  **Choices:**   - `"US"` - `"ES"` - `"DE"` - `"GB"` |
| **description**  string | Description of the load balancer. maxLength=256 |
| **health_check_interval**  string | Health check period in seconds. minimum=5, maximum=300, multipleOf=1 |
| **health_check_parse**  string | Regular expression to check. Required for HTTP health check. maxLength=64 |
| **health_check_path**  string | Url to call for checking. Required for HTTP health check. maxLength=1000 |
| **health_check_test**  string | Type of the health check. At the moment, HTTP is not allowed.  **Choices:**   - `"NONE"` - `"TCP"` - `"HTTP"` - `"ICMP"` |
| **load_balancer**  string | The identifier (id or name) of the load balancer used with update state. |
| **method**  string | Balancing procedure.  **Choices:**   - `"ROUND_ROBIN"` - `"LEAST_CONNECTIONS"` |
| **name**  string | Load balancer name used with present state. Used as identifier (id or name) when used with absent state. maxLength=128 |
| **persistence**  boolean | Persistence.  **Choices:**   - `false` - `true` |
| **persistence_time**  string | Persistence time in seconds. Required if persistence is enabled. minimum=30, maximum=1200, multipleOf=1 |
| **remove_rules**  list / elements=string | A list of rule ids that will be removed from an existing load balancer. Used in combination with update state.  **Default:** `[]` |
| **remove_server_ips**  list / elements=string | A list of server IP ids to be unassigned from a load balancer. Used in combination with update state.  **Default:** `[]` |
| **rules**  list / elements=dictionary | A list of rule objects that will be set for the load balancer. Each rule must contain protocol, port_balancer, and port_server parameters, in addition to source parameter, which is optional.  **Default:** `[]` |
| **state**  string | Define a load balancer state to create, remove, or update.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"update"` |
| **wait**  boolean | wait for the instance to be in state ‘running’ before returning  **Choices:**   - `false` - `true` ← (default) |
| **wait_interval**  integer | Defines the number of seconds to wait when using the _wait_for methods  **Default:** `5` |
| **wait_timeout**  integer | how long before wait gives up, in seconds  **Default:** `600` |

## [Attributes](oneandone_load_balancer_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](oneandone_load_balancer_module.md#id5)

```yaml+jinja
- name: Create a load balancer
  community.general.oneandone_load_balancer:
    auth_token: oneandone_private_api_key
    name: ansible load balancer
    description: Testing creation of load balancer with ansible
    health_check_test: TCP
    health_check_interval: 40
    persistence: true
    persistence_time: 1200
    method: ROUND_ROBIN
    datacenter: US
    rules:
     -
       protocol: TCP
       port_balancer: 80
       port_server: 80
       source: 0.0.0.0
    wait: true
    wait_timeout: 500

- name: Destroy a load balancer
  community.general.oneandone_load_balancer:
    auth_token: oneandone_private_api_key
    name: ansible load balancer
    wait: true
    wait_timeout: 500
    state: absent

- name: Update a load balancer
  community.general.oneandone_load_balancer:
    auth_token: oneandone_private_api_key
    load_balancer: ansible load balancer
    name: ansible load balancer updated
    description: Testing the update of a load balancer with ansible
    wait: true
    wait_timeout: 500
    state: update

- name: Add server to a load balancer
  community.general.oneandone_load_balancer:
    auth_token: oneandone_private_api_key
    load_balancer: ansible load balancer updated
    description: Adding server to a load balancer with ansible
    add_server_ips:
     - server identifier (id or name)
    wait: true
    wait_timeout: 500
    state: update

- name: Remove server from a load balancer
  community.general.oneandone_load_balancer:
    auth_token: oneandone_private_api_key
    load_balancer: ansible load balancer updated
    description: Removing server from a load balancer with ansible
    remove_server_ips:
     - B2504878540DBC5F7634EB00A07C1EBD (server's ip id)
    wait: true
    wait_timeout: 500
    state: update

- name: Add rules to a load balancer
  community.general.oneandone_load_balancer:
    auth_token: oneandone_private_api_key
    load_balancer: ansible load balancer updated
    description: Adding rules to a load balancer with ansible
    add_rules:
     -
       protocol: TCP
       port_balancer: 70
       port_server: 70
       source: 0.0.0.0
     -
       protocol: TCP
       port_balancer: 60
       port_server: 60
       source: 0.0.0.0
    wait: true
    wait_timeout: 500
    state: update

- name: Remove rules from a load balancer
  community.general.oneandone_load_balancer:
    auth_token: oneandone_private_api_key
    load_balancer: ansible load balancer updated
    description: Adding rules to a load balancer with ansible
    remove_rules:
     - rule_id #1
     - rule_id #2
     - ...
    wait: true
    wait_timeout: 500
    state: update
```

## [Return Values](oneandone_load_balancer_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **load_balancer**  dictionary | Information about the load balancer that was processed  **Returned:** always  **Sample:** `{"id": "92B74394A397ECC3359825C1656D67A6", "name": "Default Balancer"}` |

### Authors

- Amel Ajdinovic (@aajdinov)
- Ethan Devenport (@edevenport)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
