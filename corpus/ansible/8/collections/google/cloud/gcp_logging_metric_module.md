---
collection: ansible
version: "8"
title: "google.cloud.gcp_logging_metric module – Creates a GCP Metric"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_logging_metric_module.html
fetched_at: 2026-07-28T02:33:18+00:00
---
# google.cloud.gcp_logging_metric module – Creates a GCP Metric

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/ui/repo/published/google/cloud/) (version 1.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_logging_metric_module.md#ansible-collections-google-cloud-gcp-logging-metric-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_logging_metric`.

- [Synopsis](gcp_logging_metric_module.md#synopsis)
- [Requirements](gcp_logging_metric_module.md#requirements)
- [Parameters](gcp_logging_metric_module.md#parameters)
- [Notes](gcp_logging_metric_module.md#notes)
- [Examples](gcp_logging_metric_module.md#examples)
- [Return Values](gcp_logging_metric_module.md#return-values)

## [Synopsis](gcp_logging_metric_module.md#id1)

- Logs-based metric can also be used to extract values from logs and create a a distribution of the values. The distribution records the statistics of the extracted values along with an optional histogram of the values as specified by the bucket options.

## [Requirements](gcp_logging_metric_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_logging_metric_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **bucket_options**  dictionary | The bucketOptions are required when the logs-based metric is using a DISTRIBUTION value type and it describes the bucket boundaries used to create a histogram of the extracted values. |
| **explicit_buckets**  dictionary | Specifies a set of buckets with arbitrary widths. |
| **bounds**  list / elements=string / required | The values must be monotonically increasing. |
| **exponential_buckets**  dictionary | Specifies an exponential sequence of buckets that have a width that is proportional to the value of the lower bound. Each bucket represents a constant relative uncertainty on a specific value in the bucket. |
| **growth_factor**  string | Must be greater than 1. |
| **num_finite_buckets**  integer | Must be greater than 0. |
| **scale**  string | Must be greater than 0. |
| **linear_buckets**  dictionary | Specifies a linear sequence of buckets that all have the same width (except overflow and underflow).  Each bucket represents a constant absolute uncertainty on the specific value in the bucket. |
| **num_finite_buckets**  integer | Must be greater than 0. |
| **offset**  string | Lower bound of the first bucket. |
| **width**  integer | Must be greater than 0. |
| **description**  string | A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **filter**  string / required | An advanced logs filter (<https://cloud.google.com/logging/docs/view/advanced-filters>) which is used to match log entries. |
| **label_extractors**  dictionary | A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this map. The syntax of the extractor expression is the same as for the valueExtractor field. |
| **metric_descriptor**  dictionary / required | The metric descriptor associated with the logs-based metric. |
| **display_name**  string | A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example “Request count”. This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota. |
| **labels**  list / elements=dictionary | The set of labels that can be used to describe a specific instance of this metric type. For example, the appengine.googleapis.com/http/server/response_latencies metric type has a label for the HTTP response code, response_code, so you can look at latencies for successful responses or just for responses that failed. |
| **description**  string | A human-readable description for the label. |
| **key**  string / required | The label key. |
| **value_type**  string | The type of data that can be assigned to the label.  Some valid choices include: “BOOL”, “INT64”, “STRING”  **Default:** `"STRING"` |
| **metric_kind**  string / required | Whether the metric records instantaneous values, changes to a value, etc.  Some combinations of metricKind and valueType might not be supported.  For counter metrics, set this to DELTA.  Some valid choices include: “DELTA”, “GAUGE”, “CUMULATIVE” |
| **unit**  string | The unit in which the metric value is reported. It is only applicable if the valueType is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The supported units are a subset of [The Unified Code for Units of Measure](<http://unitsofmeasure.org/ucum.html>) standard .  **Default:** `"1"` |
| **value_type**  string / required | Whether the measurement is an integer, a floating-point number, etc.  Some combinations of metricKind and valueType might not be supported.  For counter metrics, set this to INT64.  Some valid choices include: “BOOL”, “INT64”, “DOUBLE”, “STRING”, “DISTRIBUTION”, “MONEY” |
| **name**  string / required | The client-assigned metric identifier. Examples - “error_count”, “nginx/requests”.  Metric identifiers are limited to 100 characters and can include only the following characters A-Z, a-z, 0-9, and the special characters _-.,+!\*’,()%/. The forward-slash character (/) denotes a hierarchy of name pieces, and it cannot be the first character of the name. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **value_extractor**  string | A valueExtractor is required when using a distribution logs-based metric to extract the values to record from a log entry. Two functions are supported for value extraction - EXTRACT(field) or REGEXP_EXTRACT(field, regex). The argument are 1. field - The name of the log entry field from which the value is to be extracted. 2. regex - A regular expression using the Google RE2 syntax (<https://github.com/google/re2/wiki/Syntax>) with a single capture group to extract data from the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error to specify a regex that does not include exactly one capture group. |

## [Notes](gcp_logging_metric_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/create>
> - Official Documentation: <https://cloud.google.com/logging/docs/apis>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_logging_metric_module.md#id5)

```yaml+jinja
- name: create a metric
  google.cloud.gcp_logging_metric:
    name: test_object
    filter: resource.type=gae_app AND severity>=ERROR
    metric_descriptor:
      metric_kind: DELTA
      value_type: DISTRIBUTION
      unit: '1'
      labels:
      - key: mass
        value_type: STRING
        description: amount of matter
    value_extractor: EXTRACT(jsonPayload.request)
    label_extractors:
      mass: EXTRACT(jsonPayload.request)
    bucket_options:
      linear_buckets:
        num_finite_buckets: 3
        width: 1
        offset: 1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_logging_metric_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **bucketOptions**  complex | The bucketOptions are required when the logs-based metric is using a DISTRIBUTION value type and it describes the bucket boundaries used to create a histogram of the extracted values.  **Returned:** success |
| **explicitBuckets**  complex | Specifies a set of buckets with arbitrary widths.  **Returned:** success |
| **bounds**  list / elements=string | The values must be monotonically increasing.  **Returned:** success |
| **exponentialBuckets**  complex | Specifies an exponential sequence of buckets that have a width that is proportional to the value of the lower bound. Each bucket represents a constant relative uncertainty on a specific value in the bucket.  **Returned:** success |
| **growthFactor**  string | Must be greater than 1.  **Returned:** success |
| **numFiniteBuckets**  integer | Must be greater than 0.  **Returned:** success |
| **scale**  string | Must be greater than 0.  **Returned:** success |
| **linearBuckets**  complex | Specifies a linear sequence of buckets that all have the same width (except overflow and underflow).  Each bucket represents a constant absolute uncertainty on the specific value in the bucket.  **Returned:** success |
| **numFiniteBuckets**  integer | Must be greater than 0.  **Returned:** success |
| **offset**  string | Lower bound of the first bucket.  **Returned:** success |
| **width**  integer | Must be greater than 0.  **Returned:** success |
| **description**  string | A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters.  **Returned:** success |
| **filter**  string | An advanced logs filter (<https://cloud.google.com/logging/docs/view/advanced-filters>) which is used to match log entries.  **Returned:** success |
| **labelExtractors**  dictionary | A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this map. The syntax of the extractor expression is the same as for the valueExtractor field.  **Returned:** success |
| **metricDescriptor**  complex | The metric descriptor associated with the logs-based metric.  **Returned:** success |
| **displayName**  string | A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example “Request count”. This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota.  **Returned:** success |
| **labels**  complex | The set of labels that can be used to describe a specific instance of this metric type. For example, the appengine.googleapis.com/http/server/response_latencies metric type has a label for the HTTP response code, response_code, so you can look at latencies for successful responses or just for responses that failed.  **Returned:** success |
| **description**  string | A human-readable description for the label.  **Returned:** success |
| **key**  string | The label key.  **Returned:** success |
| **valueType**  string | The type of data that can be assigned to the label.  **Returned:** success |
| **metricKind**  string | Whether the metric records instantaneous values, changes to a value, etc.  Some combinations of metricKind and valueType might not be supported.  For counter metrics, set this to DELTA.  **Returned:** success |
| **type**  string | The metric type, including its DNS name prefix. The type is not URL-encoded.  All user-defined metric types have the DNS name `custom.googleapis.com` or `external.googleapis.com`.  **Returned:** success |
| **unit**  string | The unit in which the metric value is reported. It is only applicable if the valueType is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The supported units are a subset of [The Unified Code for Units of Measure](<http://unitsofmeasure.org/ucum.html>) standard .  **Returned:** success |
| **valueType**  string | Whether the measurement is an integer, a floating-point number, etc.  Some combinations of metricKind and valueType might not be supported.  For counter metrics, set this to INT64.  **Returned:** success |
| **name**  string | The client-assigned metric identifier. Examples - “error_count”, “nginx/requests”.  Metric identifiers are limited to 100 characters and can include only the following characters A-Z, a-z, 0-9, and the special characters _-.,+!\*’,()%/. The forward-slash character (/) denotes a hierarchy of name pieces, and it cannot be the first character of the name.  **Returned:** success |
| **valueExtractor**  string | A valueExtractor is required when using a distribution logs-based metric to extract the values to record from a log entry. Two functions are supported for value extraction - EXTRACT(field) or REGEXP_EXTRACT(field, regex). The argument are 1. field - The name of the log entry field from which the value is to be extracted. 2. regex - A regular expression using the Google RE2 syntax (<https://github.com/google/re2/wiki/Syntax>) with a single capture group to extract data from the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error to specify a regex that does not include exactly one capture group.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
