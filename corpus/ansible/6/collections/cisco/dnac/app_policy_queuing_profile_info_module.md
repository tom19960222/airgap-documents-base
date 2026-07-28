---
collection: ansible
version: "6"
title: "cisco.dnac.app_policy_queuing_profile_info module – Information module for App Policy Queuing Profile"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/app_policy_queuing_profile_info_module.html
fetched_at: 2026-07-27T16:50:54+00:00
---
# cisco.dnac.app_policy_queuing_profile_info module – Information module for App Policy Queuing Profile

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
> see [Requirements](app_policy_queuing_profile_info_module.md#ansible-collections-cisco-dnac-app-policy-queuing-profile-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.app_policy_queuing_profile_info`.

New in cisco.dnac 4.0.0

- [Synopsis](app_policy_queuing_profile_info_module.md#synopsis)
- [Requirements](app_policy_queuing_profile_info_module.md#requirements)
- [Parameters](app_policy_queuing_profile_info_module.md#parameters)
- [Notes](app_policy_queuing_profile_info_module.md#notes)
- [See Also](app_policy_queuing_profile_info_module.md#see-also)
- [Examples](app_policy_queuing_profile_info_module.md#examples)
- [Return Values](app_policy_queuing_profile_info_module.md#return-values)

## [Synopsis](app_policy_queuing_profile_info_module.md#id1)

- Get all App Policy Queuing Profile.
- Get all or by name, existing application policy queuing profiles.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](app_policy_queuing_profile_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](app_policy_queuing_profile_info_module.md#id3)

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
| **name**  string | Name query parameter. Queuing profile name. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](app_policy_queuing_profile_info_module.md#id4)

> **Note:**
>
> - SDK Method used are application_policy.ApplicationPolicy.get_application_policy_queuing_profile,
> - Paths used are get /dna/intent/api/v1/app-policy-queuing-profile,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](app_policy_queuing_profile_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Application Policy GetApplicationPolicyQueuingProfile](https://developer.cisco.com/docs/dna-center/#!get-application-policy-queuing-profile)
> :   Complete reference of the GetApplicationPolicyQueuingProfile API.

## [Examples](app_policy_queuing_profile_info_module.md#id6)

```yaml+jinja
- name: Get all App Policy Queuing Profile
  cisco.dnac.app_policy_queuing_profile_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    name: string
  register: result
```

## [Return Values](app_policy_queuing_profile_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": [{"cfsChangeInfo": [{}], "clause": [{"displayName": "string", "id": "string", "instanceCreatedOn": 0, "instanceId": 0, "instanceUpdatedOn": 0, "instanceVersion": 0, "interfaceSpeedBandwidthClauses": [{"displayName": "string", "id": "string", "instanceCreatedOn": 0, "instanceId": 0, "instanceUpdatedOn": 0, "instanceVersion": 0, "interfaceSpeed": "string", "tcBandwidthSettings": [{"bandwidthPercentage": 0, "displayName": "string", "id": "string", "instanceCreatedOn": 0, "instanceId": 0, "instanceUpdatedOn": 0, "instanceVersion": 0, "trafficClass": "string"}]}], "isCommonBetweenAllInterfaceSpeeds": true, "priority": 0, "tcDscpSettings": [{"displayName": "string", "dscp": "string", "id": "string", "instanceCreatedOn": 0, "instanceId": 0, "instanceUpdatedOn": 0, "instanceVersion": 0, "trafficClass": "string"}], "type": "string"}], "contractClassifier": [{}], "createTime": 0, "customProvisions": [{}], "deployed": true, "description": "string", "displayName": "string", "genId": 0, "id": "string", "instanceCreatedOn": 0, "instanceId": 0, "instanceUpdatedOn": 0, "instanceVersion": 0, "internal": true, "isDeleted": true, "isSeeded": true, "isStale": true, "iseReserved": true, "lastUpdateTime": 0, "name": "string", "namespace": "string", "provisioningState": "string", "pushed": true, "qualifier": "string", "resourceVersion": 0, "targetIdList": [{}], "type": "string"}], "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
