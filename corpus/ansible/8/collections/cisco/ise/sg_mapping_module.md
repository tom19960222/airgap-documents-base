---
collection: ansible
version: "8"
title: "cisco.ise.sg_mapping module – Resource module for SG Mapping"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/sg_mapping_module.html
fetched_at: 2026-07-28T01:30:46+00:00
---
# cisco.ise.sg_mapping module – Resource module for SG Mapping

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
> see [Requirements](sg_mapping_module.md#ansible-collections-cisco-ise-sg-mapping-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.sg_mapping`.

New in cisco.ise 1.0.0

- [Synopsis](sg_mapping_module.md#synopsis)
- [Requirements](sg_mapping_module.md#requirements)
- [Parameters](sg_mapping_module.md#parameters)
- [Notes](sg_mapping_module.md#notes)
- [See Also](sg_mapping_module.md#see-also)
- [Examples](sg_mapping_module.md#examples)
- [Return Values](sg_mapping_module.md#return-values)

## [Synopsis](sg_mapping_module.md#id1)

- Manage operations create, update and delete of the resource SG Mapping.
- This API creates an IP to SGT mapping.
- This API deletes an IP to SGT mapping.
- This API allows the client to update an IP to SGT mapping by ID.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sg_mapping_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](sg_mapping_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **deployTo**  string | Mandatory unless mappingGroup is set or unless deployType=ALL. |
| **deployType**  string | Allowed values - ALL, - ND, - NDG. |
| **hostIp**  string | Mandatory if hostName is empty – valid IP. |
| **hostName**  string | Mandatory if hostIp is empty. |
| **id**  string | SG Mapping’s id. |
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
| **mappingGroup**  string | Mapping Group Id. Mandatory unless sgt and deployTo and deployType are set. |
| **name**  string | SG Mapping’s name. |
| **sgt**  string | Mandatory unless mappingGroup is set. |

## [Notes](sg_mapping_module.md#id4)

> **Note:**
>
> - SDK Method used are ip_to_sgt_mapping.IpToSgtMapping.create_ip_to_sgt_mapping, ip_to_sgt_mapping.IpToSgtMapping.delete_ip_to_sgt_mapping_by_id, ip_to_sgt_mapping.IpToSgtMapping.update_ip_to_sgt_mapping_by_id,
> - Paths used are post /ers/config/sgmapping, delete /ers/config/sgmapping/{id}, put /ers/config/sgmapping/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](sg_mapping_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for IPToSGTMapping](https://developer.cisco.com/docs/identity-services-engine/v1/#!sgmapping)
> :   Complete reference of the IPToSGTMapping API.

## [Examples](sg_mapping_module.md#id6)

```yaml+jinja
- name: Update by id
  cisco.ise.sg_mapping:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    deployTo: string
    deployType: string
    hostIp: string
    hostName: string
    id: string
    mappingGroup: string
    name: string
    sgt: string

- name: Delete by id
  cisco.ise.sg_mapping:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.sg_mapping:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    deployTo: string
    deployType: string
    hostIp: string
    hostName: string
    mappingGroup: string
    name: string
    sgt: string
```

## [Return Values](sg_mapping_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"deployTo": "string", "deployType": "string", "hostIp": "string", "hostName": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "mappingGroup": "string", "name": "string", "sgt": "string"}` |
| **ise_update_response**  dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
