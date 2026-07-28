---
collection: ansible
version: "6"
title: "cisco.dnac.service_provider_create module – Resource module for Service Provider Create"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/service_provider_create_module.html
fetched_at: 2026-07-27T16:54:07+00:00
---
# cisco.dnac.service_provider_create module – Resource module for Service Provider Create

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
> see [Requirements](service_provider_create_module.md#ansible-collections-cisco-dnac-service-provider-create-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.service_provider_create`.

New in cisco.dnac 3.1.0

- [Synopsis](service_provider_create_module.md#synopsis)
- [Requirements](service_provider_create_module.md#requirements)
- [Parameters](service_provider_create_module.md#parameters)
- [Notes](service_provider_create_module.md#notes)
- [See Also](service_provider_create_module.md#see-also)
- [Examples](service_provider_create_module.md#examples)
- [Return Values](service_provider_create_module.md#return-values)

## [Synopsis](service_provider_create_module.md#id1)

- Manage operation create of the resource Service Provider Create.
- API to create service provider profile QOS .

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](service_provider_create_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](service_provider_create_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **settings**  dictionary | Service Provider Create’s settings. |
| **qos**  list / elements=dictionary | Service Provider Create’s qos. |
| **model**  string | Model. |
| **profileName**  string | Profile Name. |
| **wanProvider**  string | Wan Provider. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](service_provider_create_module.md#id4)

> **Note:**
>
> - SDK Method used are network_settings.NetworkSettings.create_sp_profile,
> - Paths used are post /dna/intent/api/v1/service-provider,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](service_provider_create_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Network Settings CreateSPProfile](https://developer.cisco.com/docs/dna-center/#!create-sp-profile)
> :   Complete reference of the CreateSPProfile API.

## [Examples](service_provider_create_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.service_provider_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    settings:
      qos:
      - model: string
        profileName: string
        wanProvider: string
```

## [Return Values](service_provider_create_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"executionId": "string", "executionStatusUrl": "string", "message": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
