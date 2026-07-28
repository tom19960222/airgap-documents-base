---
collection: ansible
version: "8"
title: "community.general.consul_role module – Manipulate Consul roles"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/consul_role_module.html
fetched_at: 2026-07-28T01:45:13+00:00
---
# community.general.consul_role module – Manipulate Consul roles

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
> see [Requirements](consul_role_module.md#ansible-collections-community-general-consul-role-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.consul_role`.

New in community.general 7.5.0

- [Synopsis](consul_role_module.md#synopsis)
- [Requirements](consul_role_module.md#requirements)
- [Parameters](consul_role_module.md#parameters)
- [Attributes](consul_role_module.md#attributes)
- [Examples](consul_role_module.md#examples)
- [Return Values](consul_role_module.md#return-values)

## [Synopsis](consul_role_module.md#id1)

- Allows the addition, modification and deletion of roles in a consul cluster via the agent. For more details on using and configuring ACLs, see <https://www.consul.io/docs/guides/acl.html>.

## [Requirements](consul_role_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](consul_role_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of the role.  If not specified, the assigned description will not be changed. |
| **host**  string | Host of the consul agent, defaults to `localhost`.  **Default:** `"localhost"` |
| **name**  string / required | A name used to identify the role. |
| **node_identities**  list / elements=dictionary | List of node identities to attach to the role.  If not specified, any node identities currently assigned will not be changed.  If the parameter is an empty array (`[]`), any node identities assigned will be unassigned. |
| **datacenter**  string / required | The nodes datacenter.  This will result in effective policy only being valid in this datacenter. |
| **name**  string / required | The name of the node.  Must not be longer than 256 characters, must start and end with a lowercase alphanumeric character.  May only contain lowercase alphanumeric characters as well as - and _. |
| **policies**  list / elements=dictionary | List of policies to attach to the role. Each policy is a dict.  If the parameter is left blank, any policies currently assigned will not be changed.  Any empty array (`[]`) will clear any policies previously set. |
| **id**  string | The ID of the policy to attach to this role; see [community.general.consul_policy](consul_policy_module.md#ansible-collections-community-general-consul-policy-module) for more info.  Either this or `policies[].name` must be specified. |
| **name**  string | The name of the policy to attach to this role; see [community.general.consul_policy](consul_policy_module.md#ansible-collections-community-general-consul-policy-module) for more info.  Either this or `policies[].id` must be specified. |
| **port**  integer | The port on which the consul agent is running.  **Default:** `8500` |
| **scheme**  string | The protocol scheme on which the consul agent is running.  **Default:** `"http"` |
| **service_identities**  list / elements=dictionary | List of service identities to attach to the role.  If not specified, any service identities currently assigned will not be changed.  If the parameter is an empty array (`[]`), any node identities assigned will be unassigned. |
| **datacenters**  list / elements=string / required | The datacenters the policies will be effective.  This will result in effective policy only being valid in this datacenter.  If an empty array (`[]`) is specified, the policies will valid in all datacenters.  including those which do not yet exist but may in the future. |
| **name**  string / required | The name of the node.  Must not be longer than 256 characters, must start and end with a lowercase alphanumeric character.  May only contain lowercase alphanumeric characters as well as - and _. |
| **state**  string | whether the role should be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **token**  string | A management token is required to manipulate the roles. |
| **validate_certs**  boolean | Whether to verify the TLS certificate of the consul agent.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](consul_role_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](consul_role_module.md#id5)

```yaml+jinja
- name: Create a role with 2 policies
  community.general.consul_role:
    host: consul1.example.com
    token: some_management_acl
    name: foo-role
    policies:
      - id: 783beef3-783f-f41f-7422-7087dc272765
      - name: "policy-1"

- name: Create a role with service identity
  community.general.consul_role:
    host: consul1.example.com
    token: some_management_acl
    name: foo-role-2
    service_identities:
      - name: web
        datacenters:
          - dc1

- name: Create a role with node identity
  community.general.consul_role:
    host: consul1.example.com
    token: some_management_acl
    name: foo-role-3
    node_identities:
      - name: node-1
        datacenter: dc2

- name: Remove a role
  community.general.consul_role:
    host: consul1.example.com
    token: some_management_acl
    name: foo-role-3
    state: absent
```

## [Return Values](consul_role_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **operation**  string | The operation performed on the role.  **Returned:** changed  **Sample:** `"update"` |
| **role**  dictionary | The role object.  **Returned:** success  **Sample:** `{"CreateIndex": 39, "Description": "", "Hash": "Trt0QJtxVEfvTTIcdTUbIJRr6Dsi6E4EcwSFxx9tCYM=", "ID": "9a300b8d-48db-b720-8544-a37c0f5dafb5", "ModifyIndex": 39, "Name": "foo-role", "Policies": [{"ID": "b1a00172-d7a1-0e66-a12e-7a4045c4b774", "Name": "foo-access"}]}` |

### Authors

- Håkon Lerring (@Hakon)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
