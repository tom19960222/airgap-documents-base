---
collection: ansible
version: "6"
title: "cisco.dnac.applications module – Resource module for Applications"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/applications_module.html
fetched_at: 2026-07-27T16:50:57+00:00
---
# cisco.dnac.applications module – Resource module for Applications

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
> see [Requirements](applications_module.md#ansible-collections-cisco-dnac-applications-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.applications`.

New in cisco.dnac 3.1.0

- [Synopsis](applications_module.md#synopsis)
- [Requirements](applications_module.md#requirements)
- [Parameters](applications_module.md#parameters)
- [Notes](applications_module.md#notes)
- [See Also](applications_module.md#see-also)
- [Examples](applications_module.md#examples)
- [Return Values](applications_module.md#return-values)

## [Synopsis](applications_module.md#id1)

- Manage operations create, update and delete of the resource Applications.
- Create new Custom application.
- Delete existing application by its id.
- Edit the attributes of an existing application.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](applications_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](applications_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **id**  string | Id query parameter. Application’s Id. |
| **payload**  list / elements=dictionary | Applications’s payload. |
| **applicationSet**  dictionary | Applications’s applicationSet. |
| **idRef**  string | Id Ref. |
| **indicativeNetworkIdentity**  list / elements=dictionary | Applications’s indicativeNetworkIdentity. |
| **displayName**  string | DisplayName. |
| **id**  string | Id. |
| **lowerPort**  integer | LowerPort. |
| **ports**  string | Ports. |
| **protocol**  string | Protocol. |
| **upperPort**  integer | UpperPort. |
| **name**  string | Name. |
| **networkApplications**  list / elements=dictionary | Applications’s networkApplications. |
| **applicationSubType**  string | Application Sub Type. |
| **applicationType**  string | Application Type. |
| **appProtocol**  string | App Protocol. |
| **categoryId**  string | Category Id. |
| **displayName**  string | Display Name. |
| **dscp**  string | Dscp. |
| **engineId**  string | Engine Id. |
| **helpString**  string | Help String. |
| **ignoreConflict**  string | Ignore Conflict. |
| **longDescription**  string | Long Description. |
| **name**  string | Name. |
| **popularity**  string | Popularity. |
| **rank**  string | Rank. |
| **serverName**  string | Server Name. |
| **trafficClass**  string | Traffic Class. |
| **url**  string | Url. |
| **networkIdentity**  list / elements=dictionary | Applications’s networkIdentity. |
| **displayName**  string | Display Name. |
| **lowerPort**  string | Lower Port. |
| **ports**  string | Ports. |
| **protocol**  string | Protocol. |
| **upperPort**  string | Upper Port. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](applications_module.md#id4)

> **Note:**
>
> - SDK Method used are application_policy.ApplicationPolicy.create_application, application_policy.ApplicationPolicy.delete_application, application_policy.ApplicationPolicy.edit_application,
> - Paths used are post /dna/intent/api/v1/applications, delete /dna/intent/api/v1/applications, put /dna/intent/api/v1/applications,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](applications_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Application Policy CreateApplication](https://developer.cisco.com/docs/dna-center/#!create-application)
> :   Complete reference of the CreateApplication API.
>
> [Cisco DNA Center documentation for Application Policy DeleteApplication](https://developer.cisco.com/docs/dna-center/#!delete-application)
> :   Complete reference of the DeleteApplication API.
>
> [Cisco DNA Center documentation for Application Policy EditApplication](https://developer.cisco.com/docs/dna-center/#!edit-application)
> :   Complete reference of the EditApplication API.

## [Examples](applications_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.applications:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - applicationSet:
        idRef: string
      indicativeNetworkIdentity:
      - displayName: string
        id: string
        lowerPort: 0
        ports: string
        protocol: string
        upperPort: 0
      name: string
      networkApplications:
      - appProtocol: string
        applicationSubType: string
        applicationType: string
        categoryId: string
        displayName: string
        dscp: string
        engineId: string
        helpString: string
        ignoreConflict: string
        longDescription: string
        name: string
        popularity: string
        rank: string
        serverName: string
        trafficClass: string
        url: string
      networkIdentity:
      - displayName: string
        lowerPort: string
        ports: string
        protocol: string
        upperPort: string

- name: Update all
  cisco.dnac.applications:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - applicationSet:
        idRef: string
      id: string
      name: string
      networkApplications:
      - appProtocol: string
        applicationSubType: string
        applicationType: string
        categoryId: string
        displayName: string
        dscp: string
        engineId: string
        helpString: string
        id: string
        ignoreConflict: string
        longDescription: string
        name: string
        popularity: string
        rank: string
        serverName: string
        trafficClass: string
        url: string
      networkIdentity:
      - displayName: string
        id: string
        lowerPort: string
        ports: string
        protocol: string
        upperPort: string

- name: Delete all
  cisco.dnac.applications:
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

## [Return Values](applications_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"taskId": "string", "url": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
