---
collection: ansible
version: "6"
title: "cisco.ise.node_group module – Resource module for Node Group"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/node_group_module.html
fetched_at: 2026-07-27T16:58:21+00:00
---
# cisco.ise.node_group module – Resource module for Node Group

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/cisco/ise) (version 2.5.9).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](node_group_module.md#ansible-collections-cisco-ise-node-group-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.node_group`.

New in cisco.ise 1.0.0

- [Synopsis](node_group_module.md#synopsis)
- [Requirements](node_group_module.md#requirements)
- [Parameters](node_group_module.md#parameters)
- [Notes](node_group_module.md#notes)
- [See Also](node_group_module.md#see-also)
- [Examples](node_group_module.md#examples)
- [Return Values](node_group_module.md#return-values)

## [Synopsis](node_group_module.md#id1)

- Manage operations create, update and delete of the resource Node Group.
- This API creates a node group in the cluster. A node group is a group of PSNs,.
- Delete an existing node group in the cluster. Deleting the node group does not delete the nodes, but failover is no longer carried out among the nodes.
- Purpose of this API is to update an existing node group.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](node_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](node_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Node Group’s description. |
| **forceDelete**  boolean | ForceDelete query parameter. Force delete the group even if the node group contains one or more nodes.  Choices:   - `false` - `true` |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **marCache**  dictionary | Node Group’s marCache. |
| **query-attempts**  integer | The number of times Cisco ISE attempts to perform the cache entry query. (0 - 5). |
| **query-timeout**  integer | The time, in seconds, after which the cache entry query times out. (1 - 10). |
| **replication-attempts**  integer | The number of times Cisco ISE attempts to perform MAR cache entry replication. (0 - 5). |
| **replication-timeout**  integer | The time, in seconds, after which the cache entry replication times out. (1 - 10). |
| **name**  string | Node Group’s name. |
| **nodeGroupName**  string | NodeGroupName path parameter. Name of the existing node group. |

## [Notes](node_group_module.md#id4)

> **Note:**
>
> - SDK Method used are node_group.NodeGroup.create_node_group, node_group.NodeGroup.delete_node_group, node_group.NodeGroup.update_node_group,
> - Paths used are post /api/v1/deployment/node-group, delete /api/v1/deployment/node-group/{nodeGroupName}, put /api/v1/deployment/node-group/{nodeGroupName},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](node_group_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for Node Group](https://developer.cisco.com/docs/identity-services-engine/v1/#!deployment-openapi)
> :   Complete reference of the Node Group API.

## [Examples](node_group_module.md#id6)

```yaml+jinja
- name: Create
  cisco.ise.node_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    marCache:
      query-attempts: 0
      query-timeout: 0
      replication-attempts: 0
      replication-timeout: 0
    name: string

- name: Update by name
  cisco.ise.node_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    marCache:
      query-attempts: 0
      query-timeout: 0
      replication-attempts: 0
      replication-timeout: 0
    name: string
    nodeGroupName: string

- name: Delete by name
  cisco.ise.node_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    forceDelete: true
    nodeGroupName: string
```

## [Return Values](node_group_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"description": "string", "marCache": {"query-attempts": 0, "query-timeout": 0, "replication-attempts": 0, "replication-timeout": 0}, "name": "string"}` |
| **ise_update_response**  dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"success": {"message": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
