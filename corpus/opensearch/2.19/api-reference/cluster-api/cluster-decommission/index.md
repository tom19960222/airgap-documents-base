---
collection: "opensearch"
version: "2.19"
title: "Cluster decommission"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/cluster-api/cluster-decommission.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/cluster-api/cluster-decommission.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/cluster-api/cluster-decommission/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/cluster-api/cluster-decommission/"
canonical_route: "/api-reference/cluster-api/cluster-decommission/"
redirect_from: ["/api-reference/cluster-decommission/","/opensearch/rest-api/cluster-decommission/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 30
parent: "Cluster APIs"
---
# Cluster decommission
**Introduced 1.0**
{: .label .label-purple }

The cluster decommission operation adds support decommissioning based on awareness. It greatly benefits multi-zone deployments, where awareness attributes, such as `zones`, can aid in applying new upgrades to a cluster in a controlled fashion. This is especially useful during outages, in which case, you can decommission the unhealthy zone to prevent replication requests from stalling and prevent your request backlog from becoming too large.

For more information about allocation awareness, see [Shard allocation awareness](../../../tuning-your-cluster/index.md#shard-allocation-awareness).

## Endpoints

```json
PUT  /_cluster/decommission/awareness/{awareness_attribute_name}/{awareness_attribute_value}
GET  /_cluster/decommission/awareness/{awareness_attribute_name}/_status
DELETE /_cluster/decommission/awareness
```

## Path parameters

Parameter | Type | Description
:--- | :--- | :---
awareness_attribute_name | String | The name of awareness attribute, usually `zone`.
awareness_attribute_value | String | The value of the awareness attribute. For example, if you have shards allocated in two different zones, you can give each zone a value of `zone-a` or `zoneb`. The cluster decommission operation decommissions the zone listed in the method.

## Example requests

### Decommissioning and recommissioning a zone

You can use the following example requests to decommission and recommission a zone:

The following example request decommissions `zone-a`:

```json
PUT /_cluster/decommission/awareness/<zone>/<zone-a>
```

If you want to recommission a decommissioned zone, you can use the `DELETE` method:

```json
DELETE /_cluster/decommission/awareness
```

### Getting zone decommission status

The following example requests returns the decommission status of all zones.

```json
GET /_cluster/decommission/awareness/zone/_status
```

#### Example responses

The following example response shows a successful zone decommission:

```json
{
      "acknowledged": true
}
```

### Getting zone decommission status

The following example response returns the decommission status of all zones:

```json
{
     "zone-1": "INIT | DRAINING | IN_PROGRESS | SUCCESSFUL | FAILED"
}
```

## Next steps

- For more information about zone awareness and weight, see [Cluster awareness](../cluster-awareness/index.md).
- For more information about allocation awareness, see [Cluster formation](../../../tuning-your-cluster/index.md#advanced-step-6-configure-shard-allocation-awareness-or-forced-awareness).
