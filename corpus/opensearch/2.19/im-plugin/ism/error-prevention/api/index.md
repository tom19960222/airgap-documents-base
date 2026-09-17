---
collection: "opensearch"
version: "2.19"
title: "ISM Error Prevention API"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_im-plugin/ism/error-prevention/api.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_im-plugin/ism/error-prevention/api.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/im-plugin/ism/error-prevention/api/"
canonical_url: "https://docs.opensearch.org/latest/im-plugin/ism/error-prevention/api/"
canonical_route: "/im-plugin/ism/error-prevention/api/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Index State Management"
layout: "default"
nav_order: 10
parent: "ISM Error Prevention"
---
# ISM Error Prevention API

The ISM Error Prevention API allows you to enable Index State Management (ISM) error prevention and check the validation status and message.

## Enable error prevention validation

You can configure error prevention validation by setting the `plugins.index_state_management.action_validation.enabled` parameter.

#### Example request

```bash
PUT _cluster/settings
{
   "persistent":{
      "plugins.index_state_management.action_validation.enabled": true
   }
}
```

#### Example response

```json
{
  "acknowledged" : true,
  "persistent" : {
    "plugins" : {
      "index_state_management" : {
        "validation_action" : {
          "enabled" : "true"
        }
      }
    }
  },
  "transient" : { }
}
```

## Check validation status and message via the Explain API

Pass the `validate_action=true` path parameter in the Explain API URI to see the validation status and message.

#### Example request

```bash
GET _plugins/_ism/explain/test-000001?validate_action=true
```

#### Example response

```json
{
  "test-000001" : {
    "index.plugins.index_state_management.policy_id" : "test_rollover",
    "index.opendistro.index_state_management.policy_id" : "test_rollover",
    "index" : "test-000001",
    "index_uuid" : "CgKsxFmQSIa8dWqpbSJmyA",
    "policy_id" : "test_rollover",
    "policy_seq_no" : -2,
    "policy_primary_term" : 0,
    "rolled_over" : false,
    "index_creation_date" : 1667410460649,
    "state" : {
      "name" : "rollover",
      "start_time" : 1667410766045
    },
    "action" : {
      "name" : "rollover",
      "start_time" : 1667411127803,
      "index" : 0,
      "failed" : false,
      "consumed_retries" : 0,
      "last_retry_time" : 0
    },
    "step" : {
      "name" : "attempt_rollover",
      "start_time" : 1667411127803,
      "step_status" : "starting"
    },
    "retry_info" : {
      "failed" : true,
      "consumed_retries" : 0
    },
    "info" : {
      "message" : "Previous action was not able to update IndexMetaData."
    },
    "enabled" : false,
    "validate" : {
      "validation_message" : "Missing rollover_alias index setting [index=test-000001]",
      "validation_status" : "re_validating"
    }
  },
  "total_managed_indices" : 1
}
```

If you pass the parameter without a value or false, then it doesn't return the validation status and message. Only if you pass `validate_action=true` will the response will return the validation status and message.

#### Example request

```bash
GET _plugins/_ism/explain/test-000001?validate_action=false
 --- OR ---
GET _plugins/_ism/explain/test-000001
```

#### Example response

```json
{
  "test-000001" : {
    "index.plugins.index_state_management.policy_id" : "test_rollover",
    "index.opendistro.index_state_management.policy_id" : "test_rollover",
    "index" : "test-000001",
    "index_uuid" : "CgKsxFmQSIa8dWqpbSJmyA",
    "policy_id" : "test_rollover",
    "policy_seq_no" : -2,
    "policy_primary_term" : 0,
    "rolled_over" : false,
    "index_creation_date" : 1667410460649,
    "state" : {
      "name" : "rollover",
      "start_time" : 1667410766045
    },
    "action" : {
      "name" : "rollover",
      "start_time" : 1667411127803,
      "index" : 0,
      "failed" : false,
      "consumed_retries" : 0,
      "last_retry_time" : 0
    },
    "step" : {
      "name" : "attempt_rollover",
      "start_time" : 1667411127803,
      "step_status" : "starting"
    },
    "retry_info" : {
      "failed" : true,
      "consumed_retries" : 0
    },
    "info" : {
      "message" : "Previous action was not able to update IndexMetaData."
    },
    "enabled" : false
  },
  "total_managed_indices" : 1
}
```
