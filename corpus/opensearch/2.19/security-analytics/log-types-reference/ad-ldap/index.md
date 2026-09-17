---
collection: "opensearch"
version: "2.19"
title: "AD LDAP"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security-analytics/log-types-reference/ad-ldap.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security-analytics/log-types-reference/ad-ldap.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security-analytics/log-types-reference/ad-ldap/"
canonical_url: "https://docs.opensearch.org/latest/security-analytics/log-types-reference/ad-ldap/"
canonical_route: "/security-analytics/log-types-reference/ad-ldap/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 20
parent: "Supported log types"
---
# AD LDAP

The `ad_ldap` log type tracks Active Directory logs, such as:

- Lightweight Directory Access Protocol (LDAP) queries.
- Errors from the LDAP server.
- Timeout events.
- Unsecured LDAP binds.

The following code snippet contains all `raw_field` and `ecs` mappings for this log type:

```json
 "mappings": [
   {
      "raw_field":"TargetUserName",
      "ecs":"azure.signinlogs.properties.user_id"
    },
    {
      "raw_field":"creationTime",
      "ecs":"timestamp"
    },
    {
      "raw_field":"Category",
      "ecs":"azure.activitylogs.category"
    },
    {
      "raw_field":"OperationName",
      "ecs":"azure.platformlogs.operation_name"
    },
    {
      "raw_field":"ModifiedProperties_NewValue",
      "ecs":"modified_properties.new_value"
    },
    {
      "raw_field":"ResourceProviderValue",
      "ecs":"azure.resource.provider"
    },
    {
      "raw_field":"conditionalAccessStatus",
      "ecs":"azure.signinlogs.properties.conditional_access_status"
    },
    {
      "raw_field":"SearchFilter",
      "ecs":"SearchFilter"
    },
    {
      "raw_field":"Operation",
      "ecs":"azure.platformlogs.operation_name"
    },
    {
      "raw_field":"ResultType",
      "ecs":"azure.platformlogs.result_type"
    },
    {
      "raw_field":"DeviceDetail_isCompliant",
      "ecs":"azure.signinlogs.properties.device_detail.is_compliant"
    },
    {
      "raw_field":"ResourceDisplayName",
      "ecs":"resource_display_name"
    },
    {
      "raw_field":"AuthenticationRequirement",
      "ecs":"azure.signinlogs.properties.authentication_requirement"
    },
    {
      "raw_field":"TargetResources",
      "ecs":"target_resources"
    },
    {
      "raw_field":"Workload",
      "ecs":"workload"
    },
    {
      "raw_field":"DeviceDetail.deviceId",
      "ecs":"azure.signinlogs.properties.device_detail.device_id"
    },
    {
      "raw_field":"OperationNameValue",
      "ecs":"azure.platformlogs.operation_name"
    },
    {
      "raw_field":"ResourceId",
      "ecs":"azure.signinlogs.properties.resource_id"
    },
    {
      "raw_field":"ResultDescription",
      "ecs":"azure.signinlogs.result_description"
    },
    {
      "raw_field":"EventID",
      "ecs":"EventID"
    },
    {
      "raw_field":"NetworkLocationDetails",
      "ecs":"azure.signinlogs.properties.network_location_details"
    },
    {
      "raw_field":"CategoryValue",
      "ecs":"azure.activitylogs.category"
    },
    {
      "raw_field":"ActivityDisplayName",
      "ecs":"azure.auditlogs.properties.activity_display_name"
    }
  ]
```
