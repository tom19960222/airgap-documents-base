---
collection: ansible
version: "8"
title: "cisco.dnac.client_enrichment_details_info module – Information module for Client Enrichment Details"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/client_enrichment_details_info_module.html
fetched_at: 2026-07-28T01:21:30+00:00
---
# cisco.dnac.client_enrichment_details_info module – Information module for Client Enrichment Details

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
> see [Requirements](client_enrichment_details_info_module.md#ansible-collections-cisco-dnac-client-enrichment-details-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.client_enrichment_details_info`.

New in cisco.dnac 3.1.0

- [Synopsis](client_enrichment_details_info_module.md#synopsis)
- [Requirements](client_enrichment_details_info_module.md#requirements)
- [Parameters](client_enrichment_details_info_module.md#parameters)
- [Notes](client_enrichment_details_info_module.md#notes)
- [See Also](client_enrichment_details_info_module.md#see-also)
- [Examples](client_enrichment_details_info_module.md#examples)
- [Return Values](client_enrichment_details_info_module.md#return-values)

## [Synopsis](client_enrichment_details_info_module.md#id1)

- Get all Client Enrichment Details.
- Enriches a given network End User context a network user-id or end user’s device Mac Address with details about the user, the devices that the user is connected to and the assurance issues that the user is impacted by.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](client_enrichment_details_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](client_enrichment_details_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **headers**  dictionary | Additional headers. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](client_enrichment_details_info_module.md#id4)

> **Note:**
>
> - SDK Method used are clients.Clients.get_client_enrichment_details,
> - Paths used are get /dna/intent/api/v1/client-enrichment-details,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](client_enrichment_details_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Clients GetClientEnrichmentDetails](https://developer.cisco.com/docs/dna-center/#!get-client-enrichment-details)
> :   Complete reference of the GetClientEnrichmentDetails API.

## [Examples](client_enrichment_details_info_module.md#id6)

```yaml+jinja
- name: Get all Client Enrichment Details
  cisco.dnac.client_enrichment_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
```

## [Return Values](client_enrichment_details_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `"[\n  {\n    \"userDetails\": {\n      \"id\": \"string\",\n      \"connectionStatus\": \"string\",\n      \"hostType\": \"string\",\n      \"userId\": \"string\",\n      \"hostName\": {},\n      \"hostOs\": {},\n      \"hostVersion\": {},\n      \"subType\": {},\n      \"lastUpdated\": 0,\n      \"healthScore\": [\n        {\n          \"healthType\": \"string\",\n          \"reason\": \"string\",\n          \"score\": 0\n        }\n      ],\n      \"hostMac\": \"string\",\n      \"hostIpV4\": \"string\",\n      \"hostIpV6\": [\n        {}\n      ],\n      \"authType\": {},\n      \"vlanId\": \"string\",\n      \"ssid\": {},\n      \"location\": {},\n      \"clientConnection\": \"string\",\n      \"connectedDevice\": [\n        {}\n      ],\n      \"issueCount\": 0,\n      \"rssi\": {},\n      \"snr\": {},\n      \"dataRate\": {},\n      \"port\": {}\n    },\n    \"connectedDevice\": [\n      {\n        \"deviceDetails\": {\n          \"family\": \"string\",\n          \"type\": \"string\",\n          \"location\": {},\n          \"errorCode\": \"string\",\n          \"macAddress\": \"string\",\n          \"role\": \"string\",\n          \"apManagerInterfaceIp\": \"string\",\n          \"associatedWlcIp\": \"string\",\n          \"bootDateTime\": {},\n          \"collectionStatus\": \"string\",\n          \"interfaceCount\": {},\n          \"lineCardCount\": {},\n          \"lineCardId\": {},\n          \"managementIpAddress\": \"string\",\n          \"memorySize\": \"string\",\n          \"platformId\": \"string\",\n          \"reachabilityFailureReason\": \"string\",\n          \"reachabilityStatus\": \"string\",\n          \"snmpContact\": \"string\",\n          \"snmpLocation\": \"string\",\n          \"tunnelUdpPort\": \"string\",\n          \"waasDeviceMode\": {},\n          \"series\": \"string\",\n          \"inventoryStatusDetail\": \"string\",\n          \"collectionInterval\": \"string\",\n          \"serialNumber\": \"string\",\n          \"softwareVersion\": \"string\",\n          \"roleSource\": \"string\",\n          \"hostname\": \"string\",\n          \"upTime\": \"string\",\n          \"lastUpdateTime\": 0,\n          \"errorDescription\": {},\n          \"locationName\": {},\n          \"tagCount\": \"string\",\n          \"lastUpdated\": \"string\",\n          \"instanceUuid\": \"string\",\n          \"id\": \"string\",\n          \"neighborTopology\": [\n            {\n              \"nodes\": [\n                {\n                  \"role\": \"string\",\n                  \"name\": \"string\",\n                  \"id\": \"string\",\n                  \"description\": \"string\",\n                  \"deviceType\": {},\n                  \"platformId\": {},\n                  \"family\": {},\n                  \"ip\": {},\n                  \"softwareVersion\": {},\n                  \"userId\": {},\n                  \"nodeType\": {},\n                  \"radioFrequency\": {},\n                  \"clients\": 0,\n                  \"count\": {},\n                  \"healthScore\": {},\n                  \"level\": 0,\n                  \"fabricGroup\": {}\n                }\n              ],\n              \"links\": [\n                {\n                  \"source\": \"string\",\n                  \"linkStatus\": \"string\",\n                  \"label\": [\n                    {}\n                  ],\n                  \"target\": \"string\",\n                  \"id\": {},\n                  \"portUtilization\": {}\n                }\n              ]\n            }\n          ],\n          \"cisco360view\": \"string\"\n        }\n      }\n    ],\n    \"issueDetails\": {\n      \"issue\": [\n        {\n          \"issueId\": \"string\",\n          \"issueSource\": \"string\",\n          \"issueCategory\": \"string\",\n          \"issueName\": \"string\",\n          \"issueDescription\": \"string\",\n          \"issueEntity\": \"string\",\n          \"issueEntityValue\": \"string\",\n          \"issueSeverity\": \"string\",\n          \"issuePriority\": \"string\",\n          \"issueSummary\": \"string\",\n          \"issueTimestamp\": 0,\n          \"suggestedActions\": [\n            {\n              \"message\": \"string\",\n              \"steps\": [\n                {}\n              ]\n            }\n          ],\n          \"impactedHosts\": [\n            {\n              \"hostType\": \"string\",\n              \"hostName\": \"string\",\n              \"hostOs\": \"string\",\n              \"ssid\": \"string\",\n              \"connectedInterface\": \"string\",\n              \"macAddress\": \"string\",\n              \"failedAttempts\": 0,\n              \"location\": {\n                \"siteId\": \"string\",\n                \"siteType\": \"string\",\n                \"area\": \"string\",\n                \"building\": \"string\",\n                \"floor\": {},\n                \"apsImpacted\": [\n                  {}\n                ]\n              },\n              \"timestamp\": 0\n            }\n          ]\n        }\n      ]\n    }\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
