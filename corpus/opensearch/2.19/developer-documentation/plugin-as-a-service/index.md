---
collection: "opensearch"
version: "2.19"
title: "Plugin as a service"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_developer-documentation/plugin-as-a-service/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_developer-documentation/plugin-as-a-service/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/developer-documentation/plugin-as-a-service/"
canonical_url: "https://docs.opensearch.org/latest/developer-documentation/plugin-as-a-service/index/"
canonical_route: "/developer-documentation/plugin-as-a-service/"
redirect_from: ["/developer-documentation/plugin-as-a-service/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
has_toc: false
layout: "default"
nav_order: 5
---
# Plugin as a service
Introduced 2.19
{: .label .label-purple }

To extend core features, OpenSearch uses plugins, which have several limitations:
- They operate in the same JVM as a cluster, sharing storage, memory, and state.
- They require strict version compatibility.
- They are restricted to a single tenant.

To address these challenges, you can use a _remote metadata SDK client_, which enables stateless OpenSearch plugins using external data stores, such as a remote OpenSearch cluster or cloud storage services. Using the client improves scalability and makes plugins more adaptable for large workloads. For more information about the client, see [SDK Client Repository](https://github.com/opensearch-project/opensearch-remote-metadata-sdk).

## Remote metadata storage

Remote metadata storage allows OpenSearch plugins to operate in a stateless manner, without relying on local JVM or cluster resources, by using external storage solutions. Instead of storing metadata within the OpenSearch cluster, plugins can save it in remote locations such as other OpenSearch clusters or cloud storage services. This approach improves scalability, reduces resource contention, and enables plugins to function independently of the core OpenSearch cluster.

Remote metadata storage offers the following benefits:

- **Scalability**: Offloading metadata storage to an external system reduces OpenSearch cluster memory and CPU usage.
- **Multi-tenancy support**: Tenant-based storage separation enables cloud providers to offer more flexible plugin solutions, logically separating resources using tenant IDs.

### Supported storage backends

Remote metadata storage can be configured to use the following external backends:

- Remote OpenSearch clusters
- Amazon DynamoDB

## Enabling multi-tenancy

To enable multi-tenancy in a plugin, update the following static settings. After the update, restart the cluster in order for the changes to take effect. For more information about ways to update the settings, see [Configuring OpenSearch](../../install-and-configure/configuring-opensearch/index.md).

###  Multi-tenancy setting

The following table lists the multi-tenancy setting.

| Setting | Data type | Description |
|:---|:---|:---|
| `multi_tenancy_enabled` | Boolean | Enables multi-tenancy for the plugin. |

###  Remote metadata storage settings

The following table lists settings related to remote metadata storage configuration.

| Setting | Data type | Description |
|:---|:---|:---|
| `remote_metadata_type` | String | The remote metadata storage type. Valid values are: <br> - `RemoteOpenSearch`: A remote OpenSearch cluster compatible with OpenSearch Java Client. <br> - `AWSDynamoDB` : Amazon DynamoDB with zero-ETL replication to OpenSearch. <br> - `AWSOpenSearchService`: Amazon OpenSearch Service using AWS SDK v2. |
| `remote_metadata_endpoint` | String | The remote metadata endpoint URL. |
| `remote_metadata_region` | String | The AWS region in which metadata is stored. |
| `remote_metadata_service_name` | String | The remote metadata service name. |

## Example

The following configuration enables multi-tenancy using a remote OpenSearch cluster:

```yaml
plugins.<plugin_name>.multi_tenancy_enabled: true
plugins.<plugin_name>.remote_metadata_type: "opensearch"
plugins.<plugin_name>.remote_metadata_endpoint: "https://remote-store.example.com"
plugins.<plugin_name>.remote_metadata_region: "us-west-2"
plugins.<plugin_name>.remote_metadata_service_name: "remote-store-service"
```

## Supported plugins

OpenSearch supports multi-tenancy for the following plugins.

### ML Commons

The ML Commons plugin supports multi-tenancy for the following components:

- [Connectors](../../ml-commons-plugin/remote-models/connectors/index.md)
- [Model groups](../../ml-commons-plugin/model-access-control/index.md#model-groups)
- [Models](../../ml-commons-plugin/integrating-ml-models/index.md) (externally hosted only)
- [Agents](../../ml-commons-plugin/agents-tools/index.md#agents)
- [Tasks](../../ml-commons-plugin/api/tasks-apis/index.md)

The following example configures multi-tenancy for the ML Commons plugin:

```yaml
plugins.ml_commons.multi_tenancy_enabled: true
plugins.ml_commons.remote_metadata_type: AWSDynamoDB
plugins.ml_commons.remote_metadata_endpoint: <REMOTE_ENDPOINT>
plugins.ml_commons.remote_metadata_region: <AWS_REGION>
plugins.ml_commons.remote_metadata_service_name: <SERVICE_NAME>
```

### Flow Framework

The following example configures multi-tenancy for the Flow Framework plugin:

```yaml
plugins.flow_framework.multi_tenancy_enabled: true
plugins.flow_framework.remote_metadata_type: AWSDynamoDB
plugins.flow_framework.remote_metadata_endpoint: <REMOTE_ENDPOINT>
plugins.flow_framework.remote_metadata_region: <AWS_REGION>
plugins.flow_framework.remote_metadata_service_name: <SERVICE_NAME>
```
