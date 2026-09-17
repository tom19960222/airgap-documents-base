---
collection: "opensearch"
version: "2.19"
title: "ISM Error Prevention resolutions"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_im-plugin/ism/error-prevention/resolutions.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_im-plugin/ism/error-prevention/resolutions.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/im-plugin/ism/error-prevention/resolutions/"
canonical_url: "https://docs.opensearch.org/latest/im-plugin/ism/error-prevention/resolutions/"
canonical_route: "/im-plugin/ism/error-prevention/resolutions/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Index State Management"
layout: "default"
nav_order: 5
parent: "ISM Error Prevention"
---
# ISM error prevention resolutions

Resolutions of errors for each validation rule action are listed in the following sections.

---

#### Table of contents
1. TOC
<!-- local-toc -->
---

## The index is not the write index

To confirm that the index is a write index, run the following request:

```bash
GET <index>/_alias?pretty
```

If the response does not contain `"is_write_index"` : true, the index is not a write index. The following example confirms that the index is a write index:

```json
{
  "<index>" : {
    "aliases" : {
      "<index_alias>" : {
        "is_write_index" : true
      }
    }
  }
}
```

To set the index as a write index, run the following request:

```bash
PUT <index>
{
  "aliases": {
    "<index_alias>" : {
        "is_write_index" : true
    }
  }
}
```

## The index does not have an alias

If the index does not have an alias, you can add one by running the following request:

```bash
POST _aliases
{
  "actions": [
    {
      "add": {
        "index": "<target_index>",
        "alias": "<index_alias>"
      }
    }
  ]
}
```

## Skipping rollover action is true

In the event that skipping a rollover action occurs, run the following request:

```bash
 GET <target_index>/_settings?pretty
```

If you receive the response in the first example, you can reset it by running the request in the second example:

```json
{
  "index": {
    "opendistro.index_state_management.rollover_skip": true
  }
}
```

```bash
PUT <target_index>/_settings
{
    "index": {
      "index_state_management.rollover_skip": false
  }
}
```

## This index has already been rolled over successfully

Remove the [rollover policy from the index](../../api/index.md#remove-policy-from-index) to prevent this error from reoccurring.

## The rollover policy misses rollover_alias index setting

Add a `rollover_alias` index setting to the rollover policy to resolve this issue. Run the following request:

```bash
PUT _index_template/ism_rollover
{
  "index_patterns": ["<index_patterns_in_rollover_policy>"],
  "template": {
   "settings": {
    "plugins.index_state_management.rollover_alias": "<rollover_alias>"
   }
 }
}
```

## Data too large and exceeding the threshold

Check the [JVM information](../../../../api-reference/nodes-apis/nodes-info/index.md) and increase the heap memory.

## Maximum shards exceeded

The shard limit per node, or per index, causes this issue to occur. Check whether there is a `total_shards_per_node` limit by running the following request:

```bash
GET /_cluster/settings
```

If the response contains `total_shards_per_node`, increase its value temporarily by running the following request:

```bash
PUT _cluster/settings
{
   "transient":{
      "cluster.routing.allocation.total_shards_per_node":100
   }
}
```

To check whether there is a shard limit for an index, run the following request:

```bash
GET <index>/_settings/index.routing-
```

If the response contains the setting in the first example, increase its value or set it to `-1` for unlimited shards, as shown in the second example:

```json
"index" : {
        "routing" : {
          "allocation" : {
            "total_shards_per_node" : "10"
          }
        }
      }
```

```bash
PUT <index>/_settings
{"index.routing.allocation.total_shards_per_node":-1}
```

## The index is a write index for some data stream

If you still want to delete the index, check your [data stream](../../../data-streams/index.md) settings and change the write index.

## The index is blocked

Generally, the index is blocked because disk usage has exceeded the flood-stage watermark and the index has a `read-only-allow-delete` block. To resolve this issue, you can:

1. Remove the `-index.blocks.read_only_allow_delete-` parameter.
1. Temporarily increase the disk watermarks.
1. Temporarily disable the disk allocation threshold.

To prevent the issue from reoccurring, it is better to reduce the usage of the disk by increasing disk space, adding new nodes, or removing data or indexes that are no longer needed.

Remove `-index.blocks.read_only_allow_delete-` by running the following request:

```bash
PUT <index>/_settings
{
    "index.blocks.read_only_allow_delete": null
}
```

Increase the low disk watermarks by running the following request:

```bash
PUT _cluster/settings
{
    "transient": {
        "cluster": {
            "routing": {
                "allocation": {
                    "disk": {
                        "watermark": {
                            "low": "25.0gb"
                        }
                    }
                }
            }
        }
    }
}
```

Disable the disk allocation threshold by running the following request:

```bash
PUT _cluster/settings
{
    "transient": {
        "cluster": {
            "routing": {
                "allocation": {
                    "disk": {
                        "threshold_enabled" : false
                    }
                }
            }
        }
    }
}
```
