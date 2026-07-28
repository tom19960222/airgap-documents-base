---
collection: ansible
version: "6"
title: "cisco.dnac.app_policy_info module – Information module for App Policy"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/app_policy_info_module.html
fetched_at: 2026-07-27T16:50:51+00:00
---
# cisco.dnac.app_policy_info module – Information module for App Policy

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/cisco/dnac) (version 6.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](app_policy_info_module.md#ansible-collections-cisco-dnac-app-policy-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.app_policy_info`.

New in cisco.dnac 4.0.0

- [Synopsis](app_policy_info_module.md#synopsis)
- [Requirements](app_policy_info_module.md#requirements)
- [Parameters](app_policy_info_module.md#parameters)
- [Notes](app_policy_info_module.md#notes)
- [See Also](app_policy_info_module.md#see-also)
- [Examples](app_policy_info_module.md#examples)
- [Return Values](app_policy_info_module.md#return-values)

## [Synopsis](app_policy_info_module.md#id1)

- Get all App Policy.
- Get all existing application policies.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](app_policy_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](app_policy_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **headers**  dictionary | Additional headers. |
| **policyScope**  string | PolicyScope query parameter. Policy scope name. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](app_policy_info_module.md#id4)

> **Note:**
>
> - SDK Method used are application_policy.ApplicationPolicy.get_application_policy,
> - Paths used are get /dna/intent/api/v1/app-policy,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](app_policy_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Application Policy GetApplicationPolicy](https://developer.cisco.com/docs/dna-center/#!get-application-policy)
> :   Complete reference of the GetApplicationPolicy API.

## [Examples](app_policy_info_module.md#id6)

```yaml+jinja
- name: Get all App Policy
  cisco.dnac.app_policy_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    policyScope: string
  register: result
```

## [Return Values](app_policy_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": [{"advancedPolicyScope": {"advancedPolicyScopeElement": [{"displayName": "string", "groupId": ["string"], "id": "string", "instanceCreatedOn": 0, "instanceId": 0, "instanceUpdatedOn": 0, "instanceVersion": 0, "ssid": [{}]}], "displayName": "string", "id": "string", "instanceCreatedOn": 0, "instanceId": 0, "instanceUpdatedOn": 0, "instanceVersion": 0, "name": "string"}, "cfsChangeInfo": [{}], "consumer": {"displayName": "string", "id": "string", "instanceCreatedOn": 0, "instanceId": 0, "instanceUpdatedOn": 0, "instanceVersion": 0, "scalableGroup": [{"idRef": "string"}]}, "contractList": [{}], "createTime": 0, "customProvisions": [{}], "deletePolicyStatus": "string", "deployed": true, "displayName": "string", "exclusiveContract": {"clause": [{"deviceRemovalBehavior": "string", "displayName": "string", "hostTrackingEnabled": true, "id": "string", "instanceCreatedOn": 0, "instanceId": 0, "instanceUpdatedOn": 0, "instanceVersion": 0, "priority": 0, "relevanceLevel": "string", "type": "string"}], "displayName": "string", "id": "string", "instanceCreatedOn": 0, "instanceId": 0, "instanceUpdatedOn": 0, "instanceVersion": 0}, "id": "string", "identitySource": {"displayName": "string", "id": "string", "instanceCreatedOn": 0, "instanceId": 0, "instanceUpdatedOn": 0, "instanceVersion": 0, "state": "string", "type": "string"}, "instanceCreatedOn": 0, "instanceId": 0, "instanceUpdatedOn": 0, "instanceVersion": 0, "internal": true, "isDeleted": true, "isEnabled": true, "isScopeStale": true, "isSeeded": true, "isStale": true, "iseReserved": true, "lastUpdateTime": 0, "name": "string", "namespace": "string", "policyScope": "string", "policyStatus": "string", "priority": 0, "producer": {"displayName": "string", "id": "string", "instanceCreatedOn": 0, "instanceId": 0, "instanceUpdatedOn": 0, "instanceVersion": 0, "scalableGroup": [{"idRef": "string"}]}, "provisioningState": "string", "pushed": true, "qualifier": "string", "resourceVersion": 0, "targetIdList": [{}], "type": "string"}], "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
