---
collection: ansible
version: "8"
title: "cisco.dnac.app_policy_queuing_profile module – Resource module for App Policy Queuing Profile"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/app_policy_queuing_profile_module.html
fetched_at: 2026-07-28T01:21:14+00:00
---
# cisco.dnac.app_policy_queuing_profile module – Resource module for App Policy Queuing Profile

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/ui/repo/published/cisco/dnac/) (version 6.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](app_policy_queuing_profile_module.md#ansible-collections-cisco-dnac-app-policy-queuing-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.app_policy_queuing_profile`.

New in cisco.dnac 4.0.0

- [Synopsis](app_policy_queuing_profile_module.md#synopsis)
- [Requirements](app_policy_queuing_profile_module.md#requirements)
- [Parameters](app_policy_queuing_profile_module.md#parameters)
- [Notes](app_policy_queuing_profile_module.md#notes)
- [See Also](app_policy_queuing_profile_module.md#see-also)
- [Examples](app_policy_queuing_profile_module.md#examples)
- [Return Values](app_policy_queuing_profile_module.md#return-values)

## [Synopsis](app_policy_queuing_profile_module.md#id1)

- Manage operations create, update and delete of the resource App Policy Queuing Profile.
- Create new custom application queuing profile.
- Delete existing custom application policy queuing profile by id.
- Update existing custom application queuing profile.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](app_policy_queuing_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](app_policy_queuing_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **id**  string | Id path parameter. Id of custom queuing profile to delete. |
| **payload**  list / elements=dictionary | App Policy Queuing Profile’s payload. |
| **clause**  list / elements=dictionary | App Policy Queuing Profile’s clause. |
| **instanceId**  integer | Instance id. |
| **interfaceSpeedBandwidthClauses**  list / elements=dictionary | App Policy Queuing Profile’s interfaceSpeedBandwidthClauses. |
| **instanceId**  integer | Instance id. |
| **interfaceSpeed**  string | Interface speed. |
| **tcBandwidthSettings**  list / elements=dictionary | App Policy Queuing Profile’s tcBandwidthSettings. |
| **bandwidthPercentage**  integer | Bandwidth percentage. |
| **instanceId**  integer | Instance id. |
| **trafficClass**  string | Traffic Class. |
| **isCommonBetweenAllInterfaceSpeeds**  boolean | Is common between all interface speeds.  **Choices:**   - `false` - `true` |
| **tcDscpSettings**  list / elements=dictionary | App Policy Queuing Profile’s tcDscpSettings. |
| **dscp**  string | Dscp value. |
| **instanceId**  integer | Instance id. |
| **trafficClass**  string | Traffic Class. |
| **type**  string | Type. |
| **description**  string | Free test description. |
| **id**  string | Id of Queueing profile. |
| **name**  string | Queueing profile name. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](app_policy_queuing_profile_module.md#id4)

> **Note:**
>
> - SDK Method used are application_policy.ApplicationPolicy.create_application_policy_queuing_profile, application_policy.ApplicationPolicy.delete_application_policy_queuing_profile, application_policy.ApplicationPolicy.update_application_policy_queuing_profile,
> - Paths used are post /dna/intent/api/v1/app-policy-queuing-profile, delete /dna/intent/api/v1/app-policy-queuing-profile/{id}, put /dna/intent/api/v1/app-policy-queuing-profile,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](app_policy_queuing_profile_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Application Policy CreateApplicationPolicyQueuingProfile](https://developer.cisco.com/docs/dna-center/#!create-application-policy-queuing-profile)
> :   Complete reference of the CreateApplicationPolicyQueuingProfile API.
>
> [Cisco DNA Center documentation for Application Policy DeleteApplicationPolicyQueuingProfile](https://developer.cisco.com/docs/dna-center/#!delete-application-policy-queuing-profile)
> :   Complete reference of the DeleteApplicationPolicyQueuingProfile API.
>
> [Cisco DNA Center documentation for Application Policy UpdateApplicationPolicyQueuingProfile](https://developer.cisco.com/docs/dna-center/#!update-application-policy-queuing-profile)
> :   Complete reference of the UpdateApplicationPolicyQueuingProfile API.

## [Examples](app_policy_queuing_profile_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.dnac.app_policy_queuing_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - clause:
      - instanceId: 0
        interfaceSpeedBandwidthClauses:
        - instanceId: 0
          interfaceSpeed: string
          tcBandwidthSettings:
          - bandwidthPercentage: 0
            instanceId: 0
            trafficClass: string
        isCommonBetweenAllInterfaceSpeeds: true
        tcDscpSettings:
        - dscp: string
          instanceId: 0
          trafficClass: string
        type: string
      description: string
      id: string
      name: string

- name: Create
  cisco.dnac.app_policy_queuing_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - clause:
      - interfaceSpeedBandwidthClauses:
        - interfaceSpeed: string
          tcBandwidthSettings:
          - bandwidthPercentage: 0
            trafficClass: string
        isCommonBetweenAllInterfaceSpeeds: true
        tcDscpSettings:
        - dscp: string
          trafficClass: string
        type: string
      description: string
      name: string

- name: Delete by id
  cisco.dnac.app_policy_queuing_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
```

## [Return Values](app_policy_queuing_profile_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
