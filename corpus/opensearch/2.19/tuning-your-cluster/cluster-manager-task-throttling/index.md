---
collection: "opensearch"
version: "2.19"
title: "Cluster manager task throttling"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_tuning-your-cluster/cluster-manager-task-throttling.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_tuning-your-cluster/cluster-manager-task-throttling.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/tuning-your-cluster/cluster-manager-task-throttling/"
canonical_url: "https://docs.opensearch.org/latest/tuning-your-cluster/cluster-manager-task-throttling/"
canonical_route: "/tuning-your-cluster/cluster-manager-task-throttling/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 10
---
# Cluster manager task throttling

For many cluster state updates, such as defining a mapping or creating an index, nodes submit tasks to the cluster manager. The cluster manager maintains a pending task queue for these tasks and runs them in a single-threaded environment. When nodes send tens of thousands of resource-intensive tasks, like `put-mapping` or snapshot tasks, these tasks can pile up in the queue and flood the cluster manager. This affects the cluster manager's performance and may in turn affect the availability of the whole cluster.

The first line of defense is to implement mechanisms in the caller nodes to avoid task overload on the cluster manager. However, even with those mechanisms in place, the cluster manager needs a built-in way to protect itself: cluster manager task throttling.

To turn on cluster manager task throttling, you need to set throttling limits. The cluster manager uses the throttling limits to determine whether to reject a task.

The cluster manager rejects a task based on its type. For any incoming task, the cluster manager evaluates the total number of tasks of the same type in the pending task queue. If this number exceeds the threshold for this task type, the cluster manager rejects the incoming task. Rejecting a task does not affect tasks of a different type. For example, if the cluster manager rejects a `put-mapping` task, it can still accept a subsequent `create-index` task.

When the cluster manager rejects a task, the node performs retries with exponential backoff to resubmit the task to the cluster manager. If retries are unsuccessful within the timeout period, OpenSearch returns a cluster timeout error.

## Setting throttling limits

You can set throttling limits by specifying them in the `cluster_manager.throttling.thresholds` object and updating the [OpenSearch cluster settings](../../api-reference/cluster-api/cluster-settings/index.md). The setting is dynamic, so you can change the behavior of this feature without restarting your cluster.

By default, throttling is disabled for all task types.
{: .note}

The request has the following format:

```json
PUT _cluster/settings
{
  "persistent": {
    "cluster_manager.throttling.thresholds" : {
      "<task-type>" : {
          "value" : <threshold limit>
      }
    }
  }
}
```

The following table describes the `cluster_manager.throttling.thresholds` object.

Field Name | Description
:--- | :---
task-type | The task type. See [supported task types](#supported-task-types) for a list of valid values.
value | The maximum number of tasks of the `task-type` type in the cluster manager's pending task queue. Default is `-1` (no task throttling).

## Supported task types

The following task types are supported:

- `create-index`
- `update-settings`
- `cluster-update-settings`
- `auto-create`
- `delete-index`
- `delete-dangling-index`
- `create-data-stream`
- `remove-data-stream`
- `rollover-index`
- `index-aliases`
- `put-mapping`
- `create-index-template`
- `remove-index-template`
- `create-component-template`
- `remove-component-template`
- `create-index-template-v2`
- `remove-index-template-v2`
- `put-pipeline`
- `delete-pipeline`
- `create-persistent-task`
- `finish-persistent-task`
- `remove-persistent-task`
- `update-task-state`
- `put-script`
- `delete-script`
- `put-repository`
- `delete-repository`
- `create-snapshot`
- `delete-snapshot`
- `update-snapshot-state`
- `restore-snapshot`
- `cluster-reroute-api`

#### Example request

The following request sets the throttling threshold for the `put-mapping` task type to 100:

```json
PUT _cluster/settings
{
  "persistent": {
    "cluster_manager.throttling.thresholds": {
      "put-mapping": {
        "value": 100
      }
    }
  }
}
```

Set the threshold to `-1` to disable throttling for a task type.
{: .note}
