---
collection: ansible
version: "6"
title: "cisco.ise.node_deployment_info module – Information module for Node Deployment"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/node_deployment_info_module.html
fetched_at: 2026-07-27T16:58:20+00:00
---
# cisco.ise.node_deployment_info module – Information module for Node Deployment

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
> see [Requirements](node_deployment_info_module.md#ansible-collections-cisco-ise-node-deployment-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.node_deployment_info`.

New in cisco.ise 1.0.0

- [Synopsis](node_deployment_info_module.md#synopsis)
- [Requirements](node_deployment_info_module.md#requirements)
- [Parameters](node_deployment_info_module.md#parameters)
- [Notes](node_deployment_info_module.md#notes)
- [See Also](node_deployment_info_module.md#see-also)
- [Examples](node_deployment_info_module.md#examples)
- [Return Values](node_deployment_info_module.md#return-values)

## [Synopsis](node_deployment_info_module.md#id1)

- Get all Node Deployment.
- Get Node Deployment by name.
- The API lists all the nodes that are deployed in the cluster.
- This API retrieves detailed information of the deployed node.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](node_deployment_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](node_deployment_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **filter**  list / elements=string | Filter query parameter. .. Container \*\*Simple filtering\*\* is available through the filter query string parameter. The structure of a filter is a triplet of field operator and value, separated by dots. More than one filter can be sent. The logical operator common to all filter criteria is AND by default, and can be changed by using the \*”filterType=or”\* query string parameter.  Each resource Data model description should specify if an attribute is a filtered field.  The ‘EQ’ operator describes ‘Equals’.  The ‘NEQ’ operator describes ‘Not Equals’.  The ‘GT’ operator describes ‘Greater Than’.  The ‘LT’ operator describes ‘Less Than’.  The ‘STARTSW’ operator describes ‘Starts With’.  The ‘NSTARTSW’ operator describes ‘Not Starts With’.  The ‘ENDSW’ operator describes ‘Ends With’.  The ‘NENDSW’ operator describes ‘Not Ends With’.  The ‘CONTAINS’ operator describes ‘Contains’.  The ‘NCONTAINS’ operator describes ‘Not Contains’. |
| **filterType**  string | FilterType query parameter. The logical operator common to all filter criteria is AND by default, and can be changed by using this parameter. |
| **hostname**  string | Hostname path parameter. Hostname of the deployed node. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |

## [Notes](node_deployment_info_module.md#id4)

> **Note:**
>
> - SDK Method used are node_deployment.NodeDeployment.get_node_details, node_deployment.NodeDeployment.get_nodes,
> - Paths used are get /api/v1/deployment/node, get /api/v1/deployment/node/{hostname},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](node_deployment_info_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for Node Deployment](https://developer.cisco.com/docs/identity-services-engine/v1/#!deployment-openapi)
> :   Complete reference of the Node Deployment API.

## [Examples](node_deployment_info_module.md#id6)

```yaml+jinja
- name: Get all Node Deployment
  cisco.ise.node_deployment_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    filter: []
    filterType: string
  register: result

- name: Get Node Deployment by name
  cisco.ise.node_deployment_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    hostname: string
  register: result
```

## [Return Values](node_deployment_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"fqdn": "string", "hostname": "string", "ipAddress": "string", "nodeStatus": "string", "roles": ["string"], "services": ["string"]}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
