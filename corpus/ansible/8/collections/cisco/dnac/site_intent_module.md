---
collection: ansible
version: "8"
title: "cisco.dnac.site_intent module – Resource module for Site operations"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/site_intent_module.html
fetched_at: 2026-07-28T01:25:04+00:00
---
# cisco.dnac.site_intent module – Resource module for Site operations

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
> see [Requirements](site_intent_module.md#ansible-collections-cisco-dnac-site-intent-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.site_intent`.

New in cisco.dnac 6.6.0

- [Synopsis](site_intent_module.md#synopsis)
- [Requirements](site_intent_module.md#requirements)
- [Parameters](site_intent_module.md#parameters)
- [Notes](site_intent_module.md#notes)
- [Examples](site_intent_module.md#examples)
- [Return Values](site_intent_module.md#return-values)

## [Synopsis](site_intent_module.md#id1)

- Manage operation create, update and delete of the resource Sites.
- Creates site with area/building/floor with specified hierarchy.
- Updates site with area/building/floor with specified hierarchy.
- Deletes site with area/building/floor with specified hierarchy.

## [Requirements](site_intent_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk == 2.4.5
- python >= 3.5

## [Parameters](site_intent_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary / required | List of details of site being managed. |
| **site**  dictionary | Site Details. |
| **area**  dictionary | Site Create’s area. |
| **name**  string | Name of the area (eg Area1). |
| **parentName**  string | Parent name of the area to be created. |
| **building**  dictionary | Building Details. |
| **address**  string | Address of the building to be created. |
| **latitude**  integer | Latitude coordinate of the building (eg 37.338).Values between -90 to +90. |
| **longitude**  integer | Longitude coordinate of the building (eg -121.832).Values between -180 to +180. |
| **name**  string | Name of the building (eg building1). |
| **parentName**  string | Parent name of building to be created. |
| **floor**  dictionary | Site Create’s floor. |
| **floorNumber**  integer | Floor number in the building/site (eg 5). |
| **height**  integer | Height of the floor units is ft. (eg 15). |
| **length**  integer | Length of the floor units is ft. (eg 100). |
| **name**  string | Name of the floor (eg floor-1). |
| **parentName**  string | Complete Parent name of the floor to be created(eg Global/USA/San Francisco/BGL_18). |
| **rfModel**  string | Type of floor. Allowed values are ‘Cubes And Walled Offices’, ‘Drywall Office Only’, ‘Indoor High Ceiling’, ‘Outdoor Open Space’. |
| **width**  integer | Width of the floor units is ft. (eg 100). |
| **type**  string | Type of site to create/update/delete (eg area, building, floor). |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_log**  boolean | Flag for logging playbook execution details. If set to true the log file will be created at the location of the execution with the name dnac.log  **Choices:**   - `false` ← (default) - `true` |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  string | The Cisco DNA Center port.  **Default:** `"443"` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.2.3.3"` |
| **state**  string | The state of DNAC after module completion.  **Choices:**   - `"merged"` ← (default) - `"deleted"` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](site_intent_module.md#id4)

> **Note:**
>
> - SDK Method used are sites.Sites.create_site, sites.Sites.update_site, sites.Sites.delete_site
> - Paths used are post /dna/intent/api/v1/site, put dna/intent/api/v1/site/{siteId}, delete dna/intent/api/v1/site/{siteId}
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [Examples](site_intent_module.md#id5)

```yaml+jinja
- name: Create a new building site
  cisco.dnac.site_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: "{{dnac_log}}"
    config:
    - site:
        building:
          address: string
          latitude: 0
          longitude: 0
          name: string
          parentName: string
      type: string
```

## [Return Values](site_intent_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **response_1**  dictionary | A dictionary with API execution details as returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `"{\n  \"response\":\n    {\n         \"bapiExecutionId\": String,\n         \"bapiKey\": String,\n         \"bapiName\": String,\n         \"endTime\": String,\n         \"endTimeEpoch\": 0,\n         \"runtimeInstanceId\": String,\n         \"siteId\": String,\n         \"startTime\": String,\n         \"startTimeEpoch\": 0,\n         \"status\": String,\n         \"timeDuration\": 0\n\n    },\n  \"msg\": \"string\"\n}\n"` |
| **response_2**  dictionary | A dictionary with existing site details.  **Returned:** always  **Sample:** `"{\n  \"response\":\n  {\n        \"site\": {},\n        \"siteId\": String,\n        \"type\": String\n  },\n  \"msg\": String\n}\n"` |
| **response_3**  dictionary | A dictionary with API execution details as returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `"{\n  \"response\":\n    {\n         \"bapiError\": String,\n         \"bapiExecutionId\": String,\n         \"bapiKey\": String,\n         \"bapiName\": String,\n         \"endTime\": String,\n         \"endTimeEpoch\": 0,\n         \"runtimeInstanceId\": String,\n         \"startTime\": String,\n         \"startTimeEpoch\": 0,\n         \"status\": String,\n         \"timeDuration\": 0\n\n    },\n  \"msg\": \"string\"\n}\n"` |
| **response_4**  list / elements=string | A list with the response returned by the Cisco DNAC Python  **Returned:** always  **Sample:** `["{\n   \"response\": []", "\n   \"msg\": String\n}\n"]` |

### Authors

- Madhan Sankaranarayanan (@madhansansel) Rishita Chowdhary (@rishitachowdhary) Abhishek Maheshwari (@abhishekmaheshwari)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
