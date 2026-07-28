---
collection: ansible
version: "6"
title: "cisco.dnac.site_health_info module – Information module for Site Health"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/site_health_info_module.html
fetched_at: 2026-07-27T16:54:14+00:00
---
# cisco.dnac.site_health_info module – Information module for Site Health

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
> see [Requirements](site_health_info_module.md#ansible-collections-cisco-dnac-site-health-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.site_health_info`.

New in cisco.dnac 3.1.0

- [Synopsis](site_health_info_module.md#synopsis)
- [Requirements](site_health_info_module.md#requirements)
- [Parameters](site_health_info_module.md#parameters)
- [Notes](site_health_info_module.md#notes)
- [See Also](site_health_info_module.md#see-also)
- [Examples](site_health_info_module.md#examples)
- [Return Values](site_health_info_module.md#return-values)

## [Synopsis](site_health_info_module.md#id1)

- Get all Site Health.
- Returns Overall Health information for all sites.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](site_health_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](site_health_info_module.md#id3)

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
| **limit**  integer | Limit query parameter. The max number of sites in the returned data set. Default is 25, and max at 50. |
| **offset**  integer | Offset query parameter. The offset value, starting from 1, of the first returned site entry. Default is 1. |
| **siteType**  string | SiteType query parameter. Type of the site to return. AREA or BUILDING. Default to AREA. |
| **timestamp**  string | Timestamp query parameter. Epoch time(in milliseconds) when the Site Hierarchy data is required. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](site_health_info_module.md#id4)

> **Note:**
>
> - SDK Method used are sites.Sites.get_site_health,
> - Paths used are get /dna/intent/api/v1/site-health,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](site_health_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Sites GetSiteHealth](https://developer.cisco.com/docs/dna-center/#!get-site-health)
> :   Complete reference of the GetSiteHealth API.

## [Examples](site_health_info_module.md#id6)

```yaml+jinja
- name: Get all Site Health
  cisco.dnac.site_health_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    timestamp: string
    siteType: string
    offset: 0
    limit: 0
  register: result
```

## [Return Values](site_health_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `"[\n  {\n    \"siteName\": \"string\",\n    \"siteId\": \"string\",\n    \"parentSiteId\": \"string\",\n    \"parentSiteName\": \"string\",\n    \"siteType\": \"string\",\n    \"latitude\": 0,\n    \"longitude\": 0,\n    \"healthyNetworkDevicePercentage\": {},\n    \"healthyClientsPercentage\": {},\n    \"clientHealthWired\": {},\n    \"clientHealthWireless\": {},\n    \"numberOfClients\": {},\n    \"numberOfNetworkDevice\": {},\n    \"networkHealthAverage\": {},\n    \"networkHealthAccess\": {},\n    \"networkHealthCore\": {},\n    \"networkHealthDistribution\": {},\n    \"networkHealthRouter\": {},\n    \"networkHealthWireless\": {},\n    \"networkHealthOthers\": {},\n    \"numberOfWiredClients\": {},\n    \"numberOfWirelessClients\": {},\n    \"totalNumberOfConnectedWiredClients\": {},\n    \"totalNumberOfActiveWirelessClients\": {},\n    \"wiredGoodClients\": {},\n    \"wirelessGoodClients\": {},\n    \"overallGoodDevices\": {},\n    \"accessGoodCount\": {},\n    \"accessTotalCount\": {},\n    \"coreGoodCount\": {},\n    \"coreTotalCount\": {},\n    \"distributionGoodCount\": {},\n    \"distributionTotalCount\": {},\n    \"routerGoodCount\": {},\n    \"routerTotalCount\": {},\n    \"wirelessDeviceGoodCount\": {},\n    \"wirelessDeviceTotalCount\": {},\n    \"applicationHealth\": {},\n    \"applicationGoodCount\": {},\n    \"applicationTotalCount\": {},\n    \"applicationBytesTotalCount\": {},\n    \"dnacInfo\": {},\n    \"applicationHealthStats\": {\n      \"appTotalCount\": 0,\n      \"businessRelevantAppCount\": {\n        \"poor\": 0,\n        \"fair\": 0,\n        \"good\": 0\n      },\n      \"businessIrrelevantAppCount\": {\n        \"poor\": 0,\n        \"fair\": 0,\n        \"good\": 0\n      },\n      \"defaultHealthAppCount\": {\n        \"poor\": 0,\n        \"fair\": 0,\n        \"good\": 0\n      }\n    }\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
