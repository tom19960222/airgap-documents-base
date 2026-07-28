---
collection: ansible
version: "6"
title: "cisco.dnac.app_policy_intent_create module – Resource module for App Policy Intent Create"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/app_policy_intent_create_module.html
fetched_at: 2026-07-27T16:50:52+00:00
---
# cisco.dnac.app_policy_intent_create module – Resource module for App Policy Intent Create

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
> see [Requirements](app_policy_intent_create_module.md#ansible-collections-cisco-dnac-app-policy-intent-create-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.app_policy_intent_create`.

New in cisco.dnac 4.0.0

- [Synopsis](app_policy_intent_create_module.md#synopsis)
- [Requirements](app_policy_intent_create_module.md#requirements)
- [Parameters](app_policy_intent_create_module.md#parameters)
- [Notes](app_policy_intent_create_module.md#notes)
- [See Also](app_policy_intent_create_module.md#see-also)
- [Examples](app_policy_intent_create_module.md#examples)
- [Return Values](app_policy_intent_create_module.md#return-values)

## [Synopsis](app_policy_intent_create_module.md#id1)

- Manage operation create of the resource App Policy Intent Create.
- Create/Update/Delete application policy.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](app_policy_intent_create_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](app_policy_intent_create_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **createList**  list / elements=dictionary | App Policy Intent Create’s createList. |
| **advancedPolicyScope**  dictionary | App Policy Intent Create’s advancedPolicyScope. |
| **advancedPolicyScopeElement**  list / elements=dictionary | App Policy Intent Create’s advancedPolicyScopeElement. |
| **groupId**  list / elements=string | Group id. |
| **ssid**  list / elements=string | Ssid. |
| **name**  string | Policy name. |
| **consumer**  dictionary | App Policy Intent Create’s consumer. |
| **scalableGroup**  list / elements=dictionary | App Policy Intent Create’s scalableGroup. |
| **idRef**  string | Id ref to application Scalable group. |
| **contract**  dictionary | App Policy Intent Create’s contract. |
| **idRef**  string | Id ref to Queueing profile. |
| **deletePolicyStatus**  string | NONE deployed policy to devices, DELETED delete policy from devices, RESTORED restored to original configuration. |
| **exclusiveContract**  dictionary | App Policy Intent Create’s exclusiveContract. |
| **clause**  list / elements=dictionary | App Policy Intent Create’s clause. |
| **deviceRemovalBehavior**  string | Device eemoval behavior. |
| **hostTrackingEnabled**  boolean | Is host tracking enabled.  Choices:   - `false` - `true` |
| **relevanceLevel**  string | Relevance level. |
| **type**  string | Type. |
| **name**  string | Concatination of <polcy name>_<application-set-name> or <polcy name>_global_policy_configuration or <polcy name>_queuing_customization. |
| **policyScope**  string | Policy name. |
| **priority**  string | Set to 4095 while producer refer to application Scalable group otherwise 100. |
| **producer**  dictionary | App Policy Intent Create’s producer. |
| **scalableGroup**  list / elements=dictionary | App Policy Intent Create’s scalableGroup. |
| **idRef**  string | Id ref to application-set or application Scalable group. |
| **deleteList**  list / elements=string | Delete list of Group Based Policy ids. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **updateList**  list / elements=dictionary | App Policy Intent Create’s updateList. |
| **advancedPolicyScope**  dictionary | App Policy Intent Create’s advancedPolicyScope. |
| **advancedPolicyScopeElement**  list / elements=dictionary | App Policy Intent Create’s advancedPolicyScopeElement. |
| **groupId**  list / elements=string | Group id. |
| **id**  string | Id of Advance policy scope element. |
| **ssid**  list / elements=string | Ssid. |
| **id**  string | Id of Advance policy scope. |
| **name**  string | Policy name. |
| **consumer**  dictionary | App Policy Intent Create’s consumer. |
| **id**  string | Id of Consumer. |
| **scalableGroup**  list / elements=dictionary | App Policy Intent Create’s scalableGroup. |
| **idRef**  string | Id ref to application Scalable group. |
| **contract**  dictionary | App Policy Intent Create’s contract. |
| **idRef**  string | Id ref to Queueing profile. |
| **deletePolicyStatus**  string | NONE deployed policy to devices, DELETED delete policy from devices, RESTORED restored to original configuration. |
| **exclusiveContract**  dictionary | App Policy Intent Create’s exclusiveContract. |
| **clause**  list / elements=dictionary | App Policy Intent Create’s clause. |
| **deviceRemovalBehavior**  string | Device removal behavior. |
| **hostTrackingEnabled**  boolean | Host tracking enabled.  Choices:   - `false` - `true` |
| **id**  string | Id of Business relevance or Application policy knobs clause. |
| **relevanceLevel**  string | Relevance level. |
| **type**  string | Type. |
| **id**  string | Id of Exclusive contract. |
| **id**  string | Id of Group based policy. |
| **name**  string | Concatination of <polcy name>_<application-set-name> or <polcy name>_global_policy_configuration or <polcy name>_queuing_customization. |
| **policyScope**  string | Policy name. |
| **priority**  string | Set to 4095 while producer refer to application Scalable group otherwise 100. |
| **producer**  dictionary | App Policy Intent Create’s producer. |
| **id**  string | Id of Producer. |
| **scalableGroup**  list / elements=dictionary | App Policy Intent Create’s scalableGroup. |
| **idRef**  string | Id ref to application-set or application Scalable group. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](app_policy_intent_create_module.md#id4)

> **Note:**
>
> - SDK Method used are application_policy.ApplicationPolicy.application_policy_intent,
> - Paths used are post /dna/intent/api/v1/app-policy-intent,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](app_policy_intent_create_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Application Policy ApplicationPolicyIntent](https://developer.cisco.com/docs/dna-center/#!application-policy-intent)
> :   Complete reference of the ApplicationPolicyIntent API.

## [Examples](app_policy_intent_create_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.app_policy_intent_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    createList:
    - advancedPolicyScope:
        advancedPolicyScopeElement:
        - groupId:
          - string
          ssid:
          - string
        name: string
      consumer:
        scalableGroup:
        - idRef: string
      contract:
        idRef: string
      deletePolicyStatus: string
      exclusiveContract:
        clause:
        - deviceRemovalBehavior: string
          hostTrackingEnabled: true
          relevanceLevel: string
          type: string
      name: string
      policyScope: string
      priority: string
      producer:
        scalableGroup:
        - idRef: string
    deleteList:
    - string
    updateList:
    - advancedPolicyScope:
        advancedPolicyScopeElement:
        - groupId:
          - string
          id: string
          ssid:
          - string
        id: string
        name: string
      consumer:
        id: string
        scalableGroup:
        - idRef: string
      contract:
        idRef: string
      deletePolicyStatus: string
      exclusiveContract:
        clause:
        - deviceRemovalBehavior: string
          hostTrackingEnabled: true
          id: string
          relevanceLevel: string
          type: string
        id: string
      id: string
      name: string
      policyScope: string
      priority: string
      producer:
        id: string
        scalableGroup:
        - idRef: string
```

## [Return Values](app_policy_intent_create_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
