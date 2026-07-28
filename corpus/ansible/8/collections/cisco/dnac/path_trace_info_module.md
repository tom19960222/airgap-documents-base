---
collection: ansible
version: "8"
title: "cisco.dnac.path_trace_info module – Information module for Path Trace"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/path_trace_info_module.html
fetched_at: 2026-07-28T01:23:50+00:00
---
# cisco.dnac.path_trace_info module – Information module for Path Trace

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
> see [Requirements](path_trace_info_module.md#ansible-collections-cisco-dnac-path-trace-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.path_trace_info`.

New in cisco.dnac 3.1.0

- [Synopsis](path_trace_info_module.md#synopsis)
- [Requirements](path_trace_info_module.md#requirements)
- [Parameters](path_trace_info_module.md#parameters)
- [Notes](path_trace_info_module.md#notes)
- [See Also](path_trace_info_module.md#see-also)
- [Examples](path_trace_info_module.md#examples)
- [Return Values](path_trace_info_module.md#return-values)

## [Synopsis](path_trace_info_module.md#id1)

- Get all Path Trace.
- Get Path Trace by id.
- Returns a summary of all flow analyses stored. Results can be filtered by specified parameters.
- Returns result of a previously requested flow analysis by its Flow Analysis id.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](path_trace_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](path_trace_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **destIP**  string | DestIP query parameter. Destination IP adress. |
| **destPort**  string | DestPort query parameter. Destination port. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **flowAnalysisId**  string | FlowAnalysisId path parameter. Flow analysis request id. |
| **gtCreateTime**  string | GtCreateTime query parameter. Analyses requested after this time. |
| **headers**  dictionary | Additional headers. |
| **lastUpdateTime**  string | LastUpdateTime query parameter. Last update time. |
| **limit**  integer | Limit query parameter. Number of resources returned. |
| **ltCreateTime**  string | LtCreateTime query parameter. Analyses requested before this time. |
| **offset**  integer | Offset query parameter. Start index of resources returned (1-based). |
| **order**  string | Order query parameter. Order by this field. |
| **periodicRefresh**  boolean | PeriodicRefresh query parameter. Is analysis periodically refreshed?.  **Choices:**   - `false` - `true` |
| **protocol**  string | Protocol query parameter. |
| **sortBy**  string | SortBy query parameter. Sort by this field. |
| **sourceIP**  string | SourceIP query parameter. Source IP address. |
| **sourcePort**  string | SourcePort query parameter. Source port. |
| **status**  string | Status query parameter. |
| **taskId**  string | TaskId query parameter. Task ID. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](path_trace_info_module.md#id4)

> **Note:**
>
> - SDK Method used are path_trace.PathTrace.retrieves_previous_pathtrace, path_trace.PathTrace.retrives_all_previous_pathtraces_summary,
> - Paths used are get /dna/intent/api/v1/flow-analysis, get /dna/intent/api/v1/flow-analysis/{flowAnalysisId},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](path_trace_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Path Trace RetrievesPreviousPathtrace](https://developer.cisco.com/docs/dna-center/#!retrieves-previous-pathtrace)
> :   Complete reference of the RetrievesPreviousPathtrace API.
>
> [Cisco DNA Center documentation for Path Trace RetrivesAllPreviousPathtracesSummary](https://developer.cisco.com/docs/dna-center/#!retrives-all-previous-pathtraces-summary)
> :   Complete reference of the RetrivesAllPreviousPathtracesSummary API.

## [Examples](path_trace_info_module.md#id6)

```yaml+jinja
- name: Get all Path Trace
  cisco.dnac.path_trace_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    periodicRefresh: True
    sourceIP: string
    destIP: string
    sourcePort: string
    destPort: string
    gtCreateTime: string
    ltCreateTime: string
    protocol: string
    status: string
    taskId: string
    lastUpdateTime: string
    limit: 0
    offset: 0
    order: string
    sortBy: string
  register: result

- name: Get Path Trace by id
  cisco.dnac.path_trace_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    flowAnalysisId: string
  register: result
```

## [Return Values](path_trace_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"detailedStatus": {"aclTraceCalculation": "string", "aclTraceCalculationFailureReason": "string"}, "lastUpdate": "string", "networkElements": [{"accuracyList": [{"percent": 0, "reason": "string"}], "detailedStatus": {"aclTraceCalculation": "string", "aclTraceCalculationFailureReason": "string"}, "deviceStatistics": {"cpuStatistics": {"fiveMinUsageInPercentage": 0, "fiveSecsUsageInPercentage": 0, "oneMinUsageInPercentage": 0, "refreshedAt": 0}, "memoryStatistics": {"memoryUsage": 0, "refreshedAt": 0, "totalMemory": 0}}, "deviceStatsCollection": "string", "deviceStatsCollectionFailureReason": "string", "egressPhysicalInterface": {"aclAnalysis": {"aclName": "string", "matchingAces": [{"ace": "string", "matchingPorts": [{"ports": [{"destPorts": ["string"], "sourcePorts": ["string"]}], "protocol": "string"}], "result": "string"}], "result": "string"}, "id": "string", "interfaceStatistics": {"adminStatus": "string", "inputPackets": 0, "inputQueueCount": 0, "inputQueueDrops": 0, "inputQueueFlushes": 0, "inputQueueMaxDepth": 0, "inputRatebps": 0, "operationalStatus": "string", "outputDrop": 0, "outputPackets": 0, "outputQueueCount": 0, "outputQueueDepth": 0, "outputRatebps": 0, "refreshedAt": 0}, "interfaceStatsCollection": "string", "interfaceStatsCollectionFailureReason": "string", "name": "string", "pathOverlayInfo": [{"controlPlane": "string", "dataPacketEncapsulation": "string", "destIp": "string", "destPort": "string", "protocol": "string", "sourceIp": "string", "sourcePort": "string", "vxlanInfo": {"dscp": "string", "vnid": "string"}}], "qosStatistics": [{"classMapName": "string", "dropRate": 0, "numBytes": 0, "numPackets": 0, "offeredRate": 0, "queueBandwidthbps": "string", "queueDepth": 0, "queueNoBufferDrops": 0, "queueTotalDrops": 0, "refreshedAt": 0}], "qosStatsCollection": "string", "qosStatsCollectionFailureReason": "string", "usedVlan": "string", "vrfName": "string"}, "egressVirtualInterface": {"aclAnalysis": {"aclName": "string", "matchingAces": [{"ace": "string", "matchingPorts": [{"ports": [{"destPorts": ["string"], "sourcePorts": ["string"]}], "protocol": "string"}], "result": "string"}], "result": "string"}, "id": "string", "interfaceStatistics": {"adminStatus": "string", "inputPackets": 0, "inputQueueCount": 0, "inputQueueDrops": 0, "inputQueueFlushes": 0, "inputQueueMaxDepth": 0, "inputRatebps": 0, "operationalStatus": "string", "outputDrop": 0, "outputPackets": 0, "outputQueueCount": 0, "outputQueueDepth": 0, "outputRatebps": 0, "refreshedAt": 0}, "interfaceStatsCollection": "string", "interfaceStatsCollectionFailureReason": "string", "name": "string", "pathOverlayInfo": [{"controlPlane": "string", "dataPacketEncapsulation": "string", "destIp": "string", "destPort": "string", "protocol": "string", "sourceIp": "string", "sourcePort": "string", "vxlanInfo": {"dscp": "string", "vnid": "string"}}], "qosStatistics": [{"classMapName": "string", "dropRate": 0, "numBytes": 0, "numPackets": 0, "offeredRate": 0, "queueBandwidthbps": "string", "queueDepth": 0, "queueNoBufferDrops": 0, "queueTotalDrops": 0, "refreshedAt": 0}], "qosStatsCollection": "string", "qosStatsCollectionFailureReason": "string", "usedVlan": "string", "vrfName": "string"}, "flexConnect": {"authentication": "string", "dataSwitching": "string", "egressAclAnalysis": {"aclName": "string", "matchingAces": [{"ace": "string", "matchingPorts": [{"ports": [{"destPorts": ["string"], "sourcePorts": ["string"]}], "protocol": "string"}], "result": "string"}], "result": "string"}, "ingressAclAnalysis": {"aclName": "string", "matchingAces": [{"ace": "string", "matchingPorts": [{"ports": [{"destPorts": ["string"], "sourcePorts": ["string"]}], "protocol": "string"}], "result": "string"}], "result": "string"}, "wirelessLanControllerId": "string", "wirelessLanControllerName": "string"}, "id": "string", "ingressPhysicalInterface": {"aclAnalysis": {"aclName": "string", "matchingAces": [{"ace": "string", "matchingPorts": [{"ports": [{"destPorts": ["string"], "sourcePorts": ["string"]}], "protocol": "string"}], "result": "string"}], "result": "string"}, "id": "string", "interfaceStatistics": {"adminStatus": "string", "inputPackets": 0, "inputQueueCount": 0, "inputQueueDrops": 0, "inputQueueFlushes": 0, "inputQueueMaxDepth": 0, "inputRatebps": 0, "operationalStatus": "string", "outputDrop": 0, "outputPackets": 0, "outputQueueCount": 0, "outputQueueDepth": 0, "outputRatebps": 0, "refreshedAt": 0}, "interfaceStatsCollection": "string", "interfaceStatsCollectionFailureReason": "string", "name": "string", "pathOverlayInfo": [{"controlPlane": "string", "dataPacketEncapsulation": "string", "destIp": "string", "destPort": "string", "protocol": "string", "sourceIp": "string", "sourcePort": "string", "vxlanInfo": {"dscp": "string", "vnid": "string"}}], "qosStatistics": [{"classMapName": "string", "dropRate": 0, "numBytes": 0, "numPackets": 0, "offeredRate": 0, "queueBandwidthbps": "string", "queueDepth": 0, "queueNoBufferDrops": 0, "queueTotalDrops": 0, "refreshedAt": 0}], "qosStatsCollection": "string", "qosStatsCollectionFailureReason": "string", "usedVlan": "string", "vrfName": "string"}, "ingressVirtualInterface": {"aclAnalysis": {"aclName": "string", "matchingAces": [{"ace": "string", "matchingPorts": [{"ports": [{"destPorts": ["string"], "sourcePorts": ["string"]}], "protocol": "string"}], "result": "string"}], "result": "string"}, "id": "string", "interfaceStatistics": {"adminStatus": "string", "inputPackets": 0, "inputQueueCount": 0, "inputQueueDrops": 0, "inputQueueFlushes": 0, "inputQueueMaxDepth": 0, "inputRatebps": 0, "operationalStatus": "string", "outputDrop": 0, "outputPackets": 0, "outputQueueCount": 0, "outputQueueDepth": 0, "outputRatebps": 0, "refreshedAt": 0}, "interfaceStatsCollection": "string", "interfaceStatsCollectionFailureReason": "string", "name": "string", "pathOverlayInfo": [{"controlPlane": "string", "dataPacketEncapsulation": "string", "destIp": "string", "destPort": "string", "protocol": "string", "sourceIp": "string", "sourcePort": "string", "vxlanInfo": {"dscp": "string", "vnid": "string"}}], "qosStatistics": [{"classMapName": "string", "dropRate": 0, "numBytes": 0, "numPackets": 0, "offeredRate": 0, "queueBandwidthbps": "string", "queueDepth": 0, "queueNoBufferDrops": 0, "queueTotalDrops": 0, "refreshedAt": 0}], "qosStatsCollection": "string", "qosStatsCollectionFailureReason": "string", "usedVlan": "string", "vrfName": "string"}, "ip": "string", "linkInformationSource": "string", "name": "string", "perfMonCollection": "string", "perfMonCollectionFailureReason": "string", "perfMonStatistics": [{"byteRate": 0, "destIpAddress": "string", "destPort": "string", "inputInterface": "string", "ipv4DSCP": "string", "ipv4TTL": 0, "outputInterface": "string", "packetBytes": 0, "packetCount": 0, "packetLoss": 0, "packetLossPercentage": 0, "protocol": "string", "refreshedAt": 0, "rtpJitterMax": 0, "rtpJitterMean": 0, "rtpJitterMin": 0, "sourceIpAddress": "string", "sourcePort": "string"}], "role": "string", "ssid": "string", "tunnels": ["string"], "type": "string", "wlanId": "string"}], "networkElementsInfo": [{"accuracyList": [{"percent": 0, "reason": "string"}], "detailedStatus": {"aclTraceCalculation": "string", "aclTraceCalculationFailureReason": "string"}, "deviceStatistics": {"cpuStatistics": {"fiveMinUsageInPercentage": 0, "fiveSecsUsageInPercentage": 0, "oneMinUsageInPercentage": 0, "refreshedAt": 0}, "memoryStatistics": {"memoryUsage": 0, "refreshedAt": 0, "totalMemory": 0}}, "deviceStatsCollection": "string", "deviceStatsCollectionFailureReason": "string", "egressInterface": {"physicalInterface": {"aclAnalysis": {"aclName": "string", "matchingAces": [{"ace": "string", "matchingPorts": [{"ports": [{"destPorts": ["string"], "sourcePorts": ["string"]}], "protocol": "string"}], "result": "string"}], "result": "string"}, "id": "string", "interfaceStatistics": {"adminStatus": "string", "inputPackets": 0, "inputQueueCount": 0, "inputQueueDrops": 0, "inputQueueFlushes": 0, "inputQueueMaxDepth": 0, "inputRatebps": 0, "operationalStatus": "string", "outputDrop": 0, "outputPackets": 0, "outputQueueCount": 0, "outputQueueDepth": 0, "outputRatebps": 0, "refreshedAt": 0}, "interfaceStatsCollection": "string", "interfaceStatsCollectionFailureReason": "string", "name": "string", "pathOverlayInfo": [{"controlPlane": "string", "dataPacketEncapsulation": "string", "destIp": "string", "destPort": "string", "protocol": "string", "sourceIp": "string", "sourcePort": "string", "vxlanInfo": {"dscp": "string", "vnid": "string"}}], "qosStatistics": [{"classMapName": "string", "dropRate": 0, "numBytes": 0, "numPackets": 0, "offeredRate": 0, "queueBandwidthbps": "string", "queueDepth": 0, "queueNoBufferDrops": 0, "queueTotalDrops": 0, "refreshedAt": 0}], "qosStatsCollection": "string", "qosStatsCollectionFailureReason": "string", "usedVlan": "string", "vrfName": "string"}, "virtualInterface": [{"aclAnalysis": {"aclName": "string", "matchingAces": [{"ace": "string", "matchingPorts": [{"ports": [{"destPorts": ["string"], "sourcePorts": ["string"]}], "protocol": "string"}], "result": "string"}], "result": "string"}, "id": "string", "interfaceStatistics": {"adminStatus": "string", "inputPackets": 0, "inputQueueCount": 0, "inputQueueDrops": 0, "inputQueueFlushes": 0, "inputQueueMaxDepth": 0, "inputRatebps": 0, "operationalStatus": "string", "outputDrop": 0, "outputPackets": 0, "outputQueueCount": 0, "outputQueueDepth": 0, "outputRatebps": 0, "refreshedAt": 0}, "interfaceStatsCollection": "string", "interfaceStatsCollectionFailureReason": "string", "name": "string", "pathOverlayInfo": [{"controlPlane": "string", "dataPacketEncapsulation": "string", "destIp": "string", "destPort": "string", "protocol": "string", "sourceIp": "string", "sourcePort": "string", "vxlanInfo": {"dscp": "string", "vnid": "string"}}], "qosStatistics": [{"classMapName": "string", "dropRate": 0, "numBytes": 0, "numPackets": 0, "offeredRate": 0, "queueBandwidthbps": "string", "queueDepth": 0, "queueNoBufferDrops": 0, "queueTotalDrops": 0, "refreshedAt": 0}], "qosStatsCollection": "string", "qosStatsCollectionFailureReason": "string", "usedVlan": "string", "vrfName": "string"}]}, "flexConnect": {"authentication": "string", "dataSwitching": "string", "egressAclAnalysis": {"aclName": "string", "matchingAces": [{"ace": "string", "matchingPorts": [{"ports": [{"destPorts": ["string"], "sourcePorts": ["string"]}], "protocol": "string"}], "result": "string"}], "result": "string"}, "ingressAclAnalysis": {"aclName": "string", "matchingAces": [{"ace": "string", "matchingPorts": [{"ports": [{"destPorts": ["string"], "sourcePorts": ["string"]}], "protocol": "string"}], "result": "string"}], "result": "string"}, "wirelessLanControllerId": "string", "wirelessLanControllerName": "string"}, "id": "string", "ingressInterface": {"physicalInterface": {"aclAnalysis": {"aclName": "string", "matchingAces": [{"ace": "string", "matchingPorts": [{"ports": [{"destPorts": ["string"], "sourcePorts": ["string"]}], "protocol": "string"}], "result": "string"}], "result": "string"}, "id": "string", "interfaceStatistics": {"adminStatus": "string", "inputPackets": 0, "inputQueueCount": 0, "inputQueueDrops": 0, "inputQueueFlushes": 0, "inputQueueMaxDepth": 0, "inputRatebps": 0, "operationalStatus": "string", "outputDrop": 0, "outputPackets": 0, "outputQueueCount": 0, "outputQueueDepth": 0, "outputRatebps": 0, "refreshedAt": 0}, "interfaceStatsCollection": "string", "interfaceStatsCollectionFailureReason": "string", "name": "string", "pathOverlayInfo": [{"controlPlane": "string", "dataPacketEncapsulation": "string", "destIp": "string", "destPort": "string", "protocol": "string", "sourceIp": "string", "sourcePort": "string", "vxlanInfo": {"dscp": "string", "vnid": "string"}}], "qosStatistics": [{"classMapName": "string", "dropRate": 0, "numBytes": 0, "numPackets": 0, "offeredRate": 0, "queueBandwidthbps": "string", "queueDepth": 0, "queueNoBufferDrops": 0, "queueTotalDrops": 0, "refreshedAt": 0}], "qosStatsCollection": "string", "qosStatsCollectionFailureReason": "string", "usedVlan": "string", "vrfName": "string"}, "virtualInterface": [{"aclAnalysis": {"aclName": "string", "matchingAces": [{"ace": "string", "matchingPorts": [{"ports": [{"destPorts": ["string"], "sourcePorts": ["string"]}], "protocol": "string"}], "result": "string"}], "result": "string"}, "id": "string", "interfaceStatistics": {"adminStatus": "string", "inputPackets": 0, "inputQueueCount": 0, "inputQueueDrops": 0, "inputQueueFlushes": 0, "inputQueueMaxDepth": 0, "inputRatebps": 0, "operationalStatus": "string", "outputDrop": 0, "outputPackets": 0, "outputQueueCount": 0, "outputQueueDepth": 0, "outputRatebps": 0, "refreshedAt": 0}, "interfaceStatsCollection": "string", "interfaceStatsCollectionFailureReason": "string", "name": "string", "pathOverlayInfo": [{"controlPlane": "string", "dataPacketEncapsulation": "string", "destIp": "string", "destPort": "string", "protocol": "string", "sourceIp": "string", "sourcePort": "string", "vxlanInfo": {"dscp": "string", "vnid": "string"}}], "qosStatistics": [{"classMapName": "string", "dropRate": 0, "numBytes": 0, "numPackets": 0, "offeredRate": 0, "queueBandwidthbps": "string", "queueDepth": 0, "queueNoBufferDrops": 0, "queueTotalDrops": 0, "refreshedAt": 0}], "qosStatsCollection": "string", "qosStatsCollectionFailureReason": "string", "usedVlan": "string", "vrfName": "string"}]}, "ip": "string", "linkInformationSource": "string", "name": "string", "perfMonCollection": "string", "perfMonCollectionFailureReason": "string", "perfMonitorStatistics": [{"byteRate": 0, "destIpAddress": "string", "destPort": "string", "inputInterface": "string", "ipv4DSCP": "string", "ipv4TTL": 0, "outputInterface": "string", "packetBytes": 0, "packetCount": 0, "packetLoss": 0, "packetLossPercentage": 0, "protocol": "string", "refreshedAt": 0, "rtpJitterMax": 0, "rtpJitterMean": 0, "rtpJitterMin": 0, "sourceIpAddress": "string", "sourcePort": "string"}], "role": "string", "ssid": "string", "tunnels": ["string"], "type": "string", "wlanId": "string"}], "properties": ["string"], "request": {"controlPath": true, "createTime": 0, "destIP": "string", "destPort": "string", "failureReason": "string", "id": "string", "inclusions": ["string"], "lastUpdateTime": 0, "periodicRefresh": true, "protocol": "string", "sourceIP": "string", "sourcePort": "string", "status": "string"}}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
