---
collection: ansible
version: "8"
title: "community.general.consul_policy module – Manipulate Consul policies"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/consul_policy_module.html
fetched_at: 2026-07-28T01:45:13+00:00
---
# community.general.consul_policy module – Manipulate Consul policies

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
> see [Requirements](consul_policy_module.md#ansible-collections-community-general-consul-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.consul_policy`.

New in community.general 7.2.0

- [Synopsis](consul_policy_module.md#synopsis)
- [Requirements](consul_policy_module.md#requirements)
- [Parameters](consul_policy_module.md#parameters)
- [Attributes](consul_policy_module.md#attributes)
- [Examples](consul_policy_module.md#examples)
- [Return Values](consul_policy_module.md#return-values)

## [Synopsis](consul_policy_module.md#id1)

- Allows the addition, modification and deletion of policies in a consul cluster via the agent. For more details on using and configuring ACLs, see <https://www.consul.io/docs/guides/acl.html>.

## [Requirements](consul_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](consul_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of the policy.  **Default:** `""` |
| **host**  string | Host of the consul agent, defaults to localhost.  **Default:** `"localhost"` |
| **name**  string / required | The name that should be associated with the policy, this is opaque to Consul. |
| **port**  integer | The port on which the consul agent is running.  **Default:** `8500` |
| **rules**  string | Rule document that should be associated with the current policy. |
| **scheme**  string | The protocol scheme on which the consul agent is running.  **Default:** `"http"` |
| **state**  string | Whether the policy should be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **token**  string | A management token is required to manipulate the policies. |
| **valid_datacenters**  list / elements=string | Valid datacenters for the policy. All if list is empty.  **Default:** `[]` |
| **validate_certs**  boolean | Whether to verify the TLS certificate of the consul agent or not.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](consul_policy_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](consul_policy_module.md#id5)

```yaml+jinja
- name: Create a policy with rules
  community.general.consul_policy:
    host: consul1.example.com
    token: some_management_acl
    name: foo-access
    rules: |
        key "foo" {
            policy = "read"
        }
        key "private/foo" {
            policy = "deny"
        }

- name: Update the rules associated to a policy
  community.general.consul_policy:
    host: consul1.example.com
    token: some_management_acl
    name: foo-access
    rules: |
        key "foo" {
            policy = "read"
        }
        key "private/foo" {
            policy = "deny"
        }
        event "bbq" {
            policy = "write"
        }

- name: Remove a policy
  community.general.consul_policy:
    host: consul1.example.com
    token: some_management_acl
    name: foo-access
    state: absent
```

## [Return Values](consul_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **operation**  string | The operation performed on the policy.  **Returned:** changed  **Sample:** `"update"` |

### Authors

- Håkon Lerring (@Hakon)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
