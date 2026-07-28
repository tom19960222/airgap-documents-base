---
collection: ansible
version: "6"
title: "sensu.sensu_go.role_binding module – Manage Sensu role bindings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/sensu/sensu_go/role_binding_module.html
fetched_at: 2026-07-28T00:19:42+00:00
---
# sensu.sensu_go.role_binding module – Manage Sensu role bindings

> **Note:**
>
> This module is part of the [sensu.sensu_go collection](https://galaxy.ansible.com/sensu/sensu_go) (version 1.13.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install sensu.sensu_go`.
> You need further requirements to be able to use this module,
> see [Requirements](role_binding_module.md#ansible-collections-sensu-sensu-go-role-binding-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.role_binding`.

New in sensu.sensu_go 1.0.0

- [Synopsis](role_binding_module.md#synopsis)
- [Requirements](role_binding_module.md#requirements)
- [Parameters](role_binding_module.md#parameters)
- [See Also](role_binding_module.md#see-also)
- [Examples](role_binding_module.md#examples)
- [Return Values](role_binding_module.md#return-values)

## [Synopsis](role_binding_module.md#id1)

- Create, update or delete Sensu role binding.
- For more information, refer to the Sensu documentation at <https://docs.sensu.io/sensu-go/latest/reference/rbac/#role-bindings-and-cluster-role-bindings>.

## [Requirements](role_binding_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](role_binding_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  added in sensu.sensu_go 1.3.0 | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  added in sensu.sensu_go 1.5.0 | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  Default: `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"admin"` |
| **verify**  boolean  added in sensu.sensu_go 1.5.0 | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  Choices:   - `false` - `true` ← (default) |
| **cluster_role**  string | Name of the cluster role. Note that the resulting role binding grants the cluster role to the provided users and groups in the context of *auth.namespace* only.  This parameter is mutually exclusive with *role*. |
| **groups**  list / elements=string | List of groups to bind to the role or cluster role.  Note that at least one of *users* and *groups* must be specified when creating a role binding. |
| **name**  string / required | The Sensu resource’s name. This name (in combination with the namespace where applicable) uniquely identifies the resource that Ansible operates on.  If the resource with selected name already exists, Ansible module will update it to match the specification in the task.  Consult the *name* metadata attribute specification in the upstream docs on <https://docs.sensu.io/sensu-go/latest/reference/> for more details about valid names and other restrictions. |
| **namespace**  string | RBAC namespace to operate in. If this is not set the value of the SENSU_NAMESPACE environment variable will be used.  Default: `"default"` |
| **role**  string | Name of the role.  This parameter is mutually exclusive with *cluster_role*. |
| **state**  string | Target state of the Sensu object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **users**  list / elements=string | List of users to bind to the role or cluster role.  Note that at least one of *users* and *groups* must be specified when creating a role binding. |

## [See Also](role_binding_module.md#id4)

> **See also:**
>
> [sensu.sensu_go.role_binding_info](role_binding_info_module.md#ansible-collections-sensu-sensu-go-role-binding-info-module)
> :   List Sensu role bindings.
>
> [sensu.sensu_go.role](role_module.md#ansible-collections-sensu-sensu-go-role-module)
> :   Manage Sensu roles.
>
> [sensu.sensu_go.cluster_role](cluster_role_module.md#ansible-collections-sensu-sensu-go-cluster-role-module)
> :   Manage Sensu cluster roles.
>
> [sensu.sensu_go.cluster_role_binding](cluster_role_binding_module.md#ansible-collections-sensu-sensu-go-cluster-role-binding-module)
> :   Manage Sensu cluster role bindings.

## [Examples](role_binding_module.md#id5)

```yaml+jinja
- name: Create a role binding
  sensu.sensu_go.role_binding:
    name: dev_and_testing
    role: testers_permissive
    groups:
      - testers
      - dev
      - ops
    users:
      - alice

- name: Create a role binding for admins
  sensu.sensu_go.role_binding:
    name: org-admins
    cluster_role: admin
    groups:
      - team1-admins
      - team2-admins

- name: Delete a role binding
  sensu.sensu_go.role_binding:
    name: org-admins
    state: absent
```

## [Return Values](role_binding_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu role binding.  Returned: success  Sample: `{"metadata": {"name": "event-reader-binding", "namespace": "default"}, "role_ref": {"name": "event-reader", "type": "Role"}, "subjects": [{"name": "bob", "type": "User"}]}` |

### Authors

- Paul Arthur (@flowerysong)
- Manca Bizjak (@mancabizjak)
- Aljaz Kosir (@aljazkosir)
- Tadej Borovsak (@tadeboro)

### Collection links

[Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
[Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
