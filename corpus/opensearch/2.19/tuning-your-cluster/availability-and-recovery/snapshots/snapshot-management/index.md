---
collection: "opensearch"
version: "2.19"
title: "Snapshot management"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_tuning-your-cluster/availability-and-recovery/snapshots/snapshot-management.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_tuning-your-cluster/availability-and-recovery/snapshots/snapshot-management.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/tuning-your-cluster/availability-and-recovery/snapshots/snapshot-management/"
canonical_url: "https://docs.opensearch.org/latest/tuning-your-cluster/availability-and-recovery/snapshots/snapshot-management/"
canonical_route: "/tuning-your-cluster/availability-and-recovery/snapshots/snapshot-management/"
redirect_from: ["/opensearch/snapshots/snapshot-management/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Availability and recovery"
has_children: false
layout: "default"
nav_order: 20
parent: "Snapshots"
---
# Snapshot management

Snapshot management (SM) lets you automate [taking snapshots](../snapshot-restore/index.md#take-snapshots). To use this feature, you need to install the [Index Management (IM) Plugin](../../../../im-plugin/index.md). Snapshots store only incremental changes since the last snapshot. Thus, while taking an initial snapshot may be a heavy operation, subsequent snapshots have minimal overhead. To set up automatic snapshots, you have to create an SM policy with a desired SM schedule and configuration.

When you create an SM policy, its document ID is given the name `<policy_name>-sm-policy`. Because of this, SM policies have to obey the following rules:

- SM policies must have unique names.

- You cannot update the policy name after its creation.

SM-created snapshots have names in the format `<policy_name>-<date>-<random number>`. Two snapshots created by different policies at the same time always have different names because of the `<policy_name>` prefix. To avoid name collisions within the same policy, each snapshot's name contains a random string suffix.

Each policy has associated metadata that stores the policy status. Snapshot management saves SM policies and metadata in the system index and reads them from the system index. Thus, Snapshot Management depends on the OpenSearch cluster's indexing and searching functions. The policy's metadata keeps information about the latest creation and deletion only. The metadata is read before running every scheduled job so that SM can continue execution from the previous job's state. You can view the metadata using the [explain API](../sm-api/index.md#explain).

An SM schedule is a custom [cron](../../../../observing-your-data/alerting/cron/index.md) expression. It consists of two parts: a creation schedule and a deletion schedule. You must set up a creation schedule that specifies the frequency and timing of snapshot creation. Optionally, you can set up a separate schedule for deleting snapshots.

An SM configuration includes the indexes and repository for the snapshots and supports all parameters you can define when [creating a snapshot](../snapshot-restore/index.md#take-snapshots) using the API. Additionally, you can specify the format and time zone for the date used in the snapshot's name.

## Performance

One snapshot can contain as many indexes as there are in the cluster. We expect at most dozens of SM policies in one cluster, but a snapshot repository can safely scale to thousands of snapshots. However, to manage its metadata, a large repository requires more memory on the cluster manager node.

Snapshot Management depends on the Job Scheduler plugin to schedule a job that is run periodically. Each SM policy corresponds to one SM-scheduled job. The scheduled job is lightweight, so the burden of SM depends on the snapshot creation frequency and the burden of running the snapshot operation itself.

## Concurrency

An SM policy does not support concurrent snapshot operations, since too many such operations may degrade the cluster. Snapshot operations (creation or deletion) are performed asynchronously. SM does not start a new operation until the previous asynchronous operation finishes.

We don't recommend creating several SM policies with the same schedule and overlapping indexes in one cluster because it leads to concurrent snapshot creation on the same indexes and hinders performance.
{: .warning }

We don't recommend setting up the same repository for multiple SM policies with same schedule in different clusters, since it may cause a sudden spike of burden in this repository.
{: .warning }

## Failure management

If a snapshot operation fails, it is retried a maximum of three times. The failure message is saved in `metadata.latest_execution` and is overwritten when a subsequent snapshot operation starts. You can view the failure message using the [explain API](../sm-api/index.md#explain). When using OpenSearch Dashboards, you can view the failure message on the [policy details page](https://docs.opensearch.org/latest/dashboards/admin-ui-index/sm-dashboards#view-edit-or-delete-an-sm-policy) <!-- unresolved-cross-corpus-link: collection=opensearch-dashboards route=/dashboards/admin-ui-index/sm-dashboards/ -->. Possible reasons for failure include red index status and shard reallocation.

## Security

The Security plugin has two built-in roles for Snapshot Management actions: `snapshot_management_full_access` and `snapshot_management_read_access`. For descriptions of each, see [Predefined roles](../../../../security/access-control/users-roles/index.md#predefined-roles).

The following table lists the required permissions for each Snapshot Management API.

Function | API | Permission
:--- | :--- | :---
Get policy | GET _plugins/_sm/policies<br>GET _plugins/_sm/policies/`policy_name` | cluster:admin/opensearch/snapshot_management/policy/get<br>cluster:admin/opensearch/snapshot_management/policy/search
Create/update policy | POST _plugins/_sm/policies/`policy_name`<br> PUT _plugins/_sm/policies/`policy_name`?if_seq_no=1&if_primary_term=1 | cluster:admin/opensearch/snapshot_management/policy/write
Delete policy | DELETE  _plugins/_sm/policies/`policy_name` | cluster:admin/opensearch/snapshot_management/policy/delete
Explain | GET _plugins/_sm/policies/`policy_names`/_explain | cluster:admin/opensearch/snapshot_management/policy/explain
Start | POST  _plugins/_sm/policies/`policy_name`/_start | cluster:admin/opensearch/snapshot_management/policy/start
Stop| POST  _plugins/_sm/policies/`policy_name`/_stop | cluster:admin/opensearch/snapshot_management/policy/stop

## API

The following table lists all [Snapshot Management API](../sm-api/index.md) functions.

Function | API | Description
:--- | :--- | :---
[Create policy](../sm-api/index.md#create-or-update-a-policy) | POST _plugins/_sm/policies/`policy_name` | Creates an SM policy.
[Update policy](../sm-api/index.md#create-or-update-a-policy) | PUT _plugins/_sm/policies/`policy_name`?if_seq_no=`sequence_number`&if_primary_term=`primary_term` | Modifies the `policy_name` policy.
[Get all policies](../sm-api/index.md#get-policies) | GET _plugins/_sm/policies | Returns all SM policies.
[Get the policy `policy_name`](../sm-api/index.md#get-policies) | GET _plugins/_sm/policies/`policy_name` | Returns the `policy_name` SM policy.
[Delete policy](../sm-api/index.md#delete-a-policy) | DELETE  _plugins/_sm/policies/`policy_name` | Deletes the `policy_name` policy.
[Explain](../sm-api/index.md#explain) | GET _plugins/_sm/policies/`policy_names`/_explain | Provides the enabled/disabled status and the metadata for all policies specified by `policy_names`.
[Start policy](../sm-api/index.md#start-a-policy) | POST  _plugins/_sm/policies/`policy_name`/_start | Starts the `policy_name` policy.
[Stop policy](../sm-api/index.md#stop-a-policy)| POST  _plugins/_sm/policies/`policy_name`/_stop | Stops the `policy_name` policy.
