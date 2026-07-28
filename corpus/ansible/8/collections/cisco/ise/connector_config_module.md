---
collection: ansible
version: "8"
title: "cisco.ise.connector_config module – Resource module for Connector Config"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/connector_config_module.html
fetched_at: 2026-07-28T01:27:35+00:00
---
# cisco.ise.connector_config module – Resource module for Connector Config

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/ui/repo/published/cisco/ise/) (version 2.6.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](connector_config_module.md#ansible-collections-cisco-ise-connector-config-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.connector_config`.

New in cisco.ise 3.2_beta

- [Synopsis](connector_config_module.md#synopsis)
- [Requirements](connector_config_module.md#requirements)
- [Parameters](connector_config_module.md#parameters)
- [Notes](connector_config_module.md#notes)
- [Examples](connector_config_module.md#examples)
- [Return Values](connector_config_module.md#return-values)

## [Synopsis](connector_config_module.md#id1)

- Manage operations create, update and delete of the resource Connector Config.
- EDDA - Configure connectorconfig information.
- EDDA - Delete Configure connectorConfig information based on ConnectorName.
- EDDA - update Configure connectorConfig information based on ConnectorName.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](connector_config_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.1
- python >= 3.5

## [Parameters](connector_config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **additionalProperties**  dictionary | Connector Config’s additionalProperties. |
| **attributes**  dictionary | ConnectorName. |
| **attributeMapping**  list / elements=dictionary | <p>List of feature names</p>. |
| **dictionaryAttribute**  string | Connector Config’s dictionaryAttribute. |
| **includeInDictionary**  boolean | IncludeInDictionary flag.  **Choices:**   - `false` - `true` |
| **jsonAttribute**  string | Connector Config’s jsonAttribute. |
| **bulkUniqueIdentifier**  string | Uniqueness to identify. |
| **topLevelObject**  string | Root level of json. |
| **uniqueIdentifier**  string | Uniqueness to identify. |
| **versionIdentifier**  string | Version uniqueness to identify. |
| **connectorName**  string | ConnectorName. |
| **connectorType**  string | Connector Type list. |
| **deltasyncSchedule**  dictionary | Connector Config’s deltasyncSchedule. |
| **interval**  integer | Run at interval (hours). |
| **intervalUnit**  string | Interval Units. |
| **startDate**  string | Start date and Time. |
| **description**  string | Description. |
| **enabled**  boolean | Enabled flag.  **Choices:**   - `false` - `true` |
| **fullsyncSchedule**  dictionary | Connector Config’s fullsyncSchedule. |
| **interval**  integer | Run at interval (hours). |
| **intervalUnit**  string | Interval Units. |
| **startDate**  string | Start date and Time. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_single_request_timeout**  integer  *added in cisco.ise 3.0.0* | Timeout (in seconds) for RESTful HTTP requests.  **Default:** `60` |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  *added in cisco.ise 1.1.0* | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  **Choices:**   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  *added in cisco.ise 3.0.0* | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  **Choices:**   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  **Default:** `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  **Choices:**   - `false` - `true` ← (default) |
| **protocol**  string | Protocol. |
| **skipCertificateValidations**  boolean | SkipCertificateValidations flag.  **Choices:**   - `false` - `true` |
| **url**  dictionary | Connector Config’s url. |
| **accessKey**  string | Accesskey. |
| **authenticationType**  string | Authentication Type list. |
| **bulkUrl**  string | BulkUrl. |
| **clientId**  string | Clientid. |
| **clientSecret**  string | Clientsecret. |
| **incrementalUrl**  string | IncrementalUrl. |
| **password**  string | Password. |
| **refreshToken**  string | Refreshtoken. |
| **tokenHeader**  string | TokenHeader. |
| **userName**  string | UserName. |

## [Notes](connector_config_module.md#id4)

> **Note:**
>
> - SDK Method used are edda.Edda.create_connector_config, edda.Edda.delete_connector_config_by_connector_name, edda.Edda.update_connector_config_by_connector_name,
> - Paths used are post /api/v1/edda/connector-config, delete /api/v1/edda/connector-config/{connectorName}, put /api/v1/edda/connector-config/{connectorName},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](connector_config_module.md#id5)

```yaml+jinja
- name: Create
  cisco.ise.connector_config:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    additionalProperties: {}
    attributes:
      attributeMapping:
      - dictionaryAttribute: string
        includeInDictionary: true
        jsonAttribute: string
      bulkUniqueIdentifier: string
      topLevelObject: string
      uniqueIdentifier: string
      versionIdentifier: string
    connectorName: string
    connectorType: string
    deltasyncSchedule:
      interval: 0
      intervalUnit: string
      startDate: string
    description: string
    enabled: true
    fullsyncSchedule:
      interval: 0
      intervalUnit: string
      startDate: string
    protocol: string
    skipCertificateValidations: true
    url:
      accessKey: string
      authenticationType: string
      bulkUrl: string
      clientId: string
      clientSecret: string
      incrementalUrl: string
      password: string
      refreshToken: string
      tokenHeader: string
      userName: string

- name: Update by name
  cisco.ise.connector_config:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    additionalProperties: {}
    attributes:
      attributeMapping:
      - dictionaryAttribute: string
        includeInDictionary: true
        jsonAttribute: string
      bulkUniqueIdentifier: string
      topLevelObject: string
      uniqueIdentifier: string
      versionIdentifier: string
    connectorName: string
    connectorType: string
    deltasyncSchedule:
      interval: 0
      intervalUnit: string
      startDate: string
    description: string
    enabled: true
    fullsyncSchedule:
      interval: 0
      intervalUnit: string
      startDate: string
    protocol: string
    skipCertificateValidations: true
    url:
      accessKey: string
      authenticationType: string
      bulkUrl: string
      clientId: string
      clientSecret: string
      incrementalUrl: string
      password: string
      refreshToken: string
      tokenHeader: string
      userName: string

- name: Delete by name
  cisco.ise.connector_config:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    connectorName: string
```

## [Return Values](connector_config_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"connector": {"additionalProperties": {}, "attributes": {"attributeMapping": [{"dictionaryAttribute": "string", "includeInDictionary": true, "jsonAttribute": "string"}], "bulkUniqueIdentifier": "string", "topLevelObject": "string", "uniqueIdentifier": "string", "versionIdentifier": "string"}, "connectorName": "string", "connectorType": "string", "deltasyncSchedule": {"interval": 0, "intervalUnit": "string", "startDate": "string"}, "description": "string", "enabled": true, "fullsyncSchedule": {"interval": 0, "intervalUnit": "string", "startDate": "string"}, "protocol": "string", "skipCertificateValidations": true, "url": {"accessKey": "string", "authenticationType": "string", "bulkUrl": "string", "clientId": "string", "clientSecret": "string", "incrementalUrl": "string", "password": "string", "refreshToken": "string", "tokenHeader": "string", "userName": "string"}}}` |
| **ise_update_response**  string | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `"\"'string'\"\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
