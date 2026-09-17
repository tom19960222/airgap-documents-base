---
collection: "opensearch"
version: "2.19"
title: "Mappings APIs"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security-analytics/api-tools/mappings-api.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security-analytics/api-tools/mappings-api.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security-analytics/api-tools/mappings-api/"
canonical_url: "https://docs.opensearch.org/latest/security-analytics/api-tools/mappings-api/"
canonical_route: "/security-analytics/api-tools/mappings-api/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 45
parent: "API tools"
---
# Mappings APIs

The following APIs can be used for a number of tasks related to mappings, from creating to getting and updating mappings.

---
## Get Mappings View

This API returns a view of the fields contained in an index used as a log source.

### Request body fields

The following fields are used to get field mappings.

Field | Type | Description
:--- | :--- |:---
`index_name` | String | The name of the index used for log ingestion.
`rule_topic` | String | The log type of the index.

#### Example request

```json
GET /_plugins/_security_analytics/mappings/view

{
   "index_name": "windows",
   "rule_topic": "windows"
}
```

#### Example response

```json
{
    "properties": {
        "windows-event_data-CommandLine": {
            "path": "CommandLine",
            "type": "alias"
        },
        "event_uid": {
            "path": "EventID",
            "type": "alias"
        }
    },
    "unmapped_index_fields": [
        "windows-event_data-CommandLine",
        "unmapped_HiveName",
        "src_ip",
        "sha1",
        "processPath",
        "CallerProcessName",
        "CallTrace",
        "AuthenticationPackageName",
        "AuditSourceName",
        "AuditPolicyChanges",
        "AttributeValue",
        "AttributeLDAPDisplayName",
        "ApplicationPath",
        "Application",
        "AllowedToDelegateTo",
        "Address",
        "Action",
        "AccountType",
        "AccountName",
        "Accesses",
        "AccessMask",
        "AccessList"
    ]
}
```

---
## Create Mappings

#### Example request

```json
POST /_plugins/_security_analytics/mappings

{
   "index_name": "windows",
   "rule_topic": "windows",
   "partial": true,
   "alias_mappings": {
        "properties": {
            "event_uid": {
            "type": "alias",
            "path": "EventID"
          }
       }
   }
}
```

#### Example response

```json
{
    "acknowledged": true
}
```

---
## Get Mappings

### Path options

Field | Type | Description
:--- | :--- |:---
`index_name` | String | The name of the index used for log ingestion. Required.

#### Example request

```json
GET /_plugins/_security_analytics/mappings?index_name=windows
```

#### Example response

```json
{
    "windows": {
        "mappings": {
            "properties": {
                "windows-event_data-CommandLine": {
                    "type": "alias",
                    "path": "CommandLine"
                },
                "event_uid": {
                    "type": "alias",
                    "path": "EventID"
                }
            }
        }
    }
}
```

---
## Update Mappings

#### Example request

```json
PUT /_plugins/_security_analytics/mappings

{
   "index_name": "windows",
   "field": "CommandLine",
   "alias": "windows-event_data-CommandLine"
}
```

#### Example response

```json
{
    "acknowledged": true
}
```
