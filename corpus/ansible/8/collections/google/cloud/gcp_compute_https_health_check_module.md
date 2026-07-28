---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_https_health_check module – Creates a GCP HttpsHealthCheck"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_https_health_check_module.html
fetched_at: 2026-07-28T02:32:09+00:00
---
# google.cloud.gcp_compute_https_health_check module – Creates a GCP HttpsHealthCheck

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
> see [Requirements](gcp_compute_https_health_check_module.md#ansible-collections-google-cloud-gcp-compute-https-health-check-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_https_health_check`.

- [Synopsis](gcp_compute_https_health_check_module.md#synopsis)
- [Requirements](gcp_compute_https_health_check_module.md#requirements)
- [Parameters](gcp_compute_https_health_check_module.md#parameters)
- [Notes](gcp_compute_https_health_check_module.md#notes)
- [Examples](gcp_compute_https_health_check_module.md#examples)
- [Return Values](gcp_compute_https_health_check_module.md#return-values)

## [Synopsis](gcp_compute_https_health_check_module.md#id1)

- An HttpsHealthCheck resource. This resource defines a template for how individual VMs should be checked for health, via HTTPS.

## [Requirements](gcp_compute_https_health_check_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_https_health_check_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **check_interval_sec**  integer | How often (in seconds) to send a health check. The default value is 5 seconds. |
| **description**  string | An optional description of this resource. Provide this property when you create the resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **healthy_threshold**  integer | A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2. |
| **host**  string | The value of the host header in the HTTPS health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used. |
| **name**  string / required | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **port**  integer | The TCP port number for the HTTPS health check request.  The default value is 443. |
| **project**  string | The Google Cloud Platform project to use. |
| **request_path**  string | The request path of the HTTPS health check request.  The default value is /. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout_sec**  aliases: timeout_seconds  integer | How long (in seconds) to wait before claiming failure.  The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec. |
| **unhealthy_threshold**  integer | A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2. |

## [Notes](gcp_compute_https_health_check_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/v1/httpsHealthChecks>
> - Adding Health Checks: <https://cloud.google.com/compute/docs/load-balancing/health-checks#legacy_health_checks>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_https_health_check_module.md#id5)

```yaml+jinja
- name: create a HTTPS health check
  google.cloud.gcp_compute_https_health_check:
    name: test_object
    healthy_threshold: 10
    port: 8080
    timeout_sec: 2
    unhealthy_threshold: 5
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_https_health_check_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **checkIntervalSec**  integer | How often (in seconds) to send a health check. The default value is 5 seconds.  **Returned:** success |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **description**  string | An optional description of this resource. Provide this property when you create the resource.  **Returned:** success |
| **healthyThreshold**  integer | A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.  **Returned:** success |
| **host**  string | The value of the host header in the HTTPS health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used.  **Returned:** success |
| **id**  integer | The unique identifier for the resource. This identifier is defined by the server.  **Returned:** success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **port**  integer | The TCP port number for the HTTPS health check request.  The default value is 443.  **Returned:** success |
| **requestPath**  string | The request path of the HTTPS health check request.  The default value is /.  **Returned:** success |
| **timeoutSec**  integer | How long (in seconds) to wait before claiming failure.  The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec.  **Returned:** success |
| **unhealthyThreshold**  integer | A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
