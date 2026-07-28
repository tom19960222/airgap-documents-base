---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_ssl_policy module – Creates a GCP SslPolicy"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_ssl_policy_module.html
fetched_at: 2026-07-28T02:32:47+00:00
---
# google.cloud.gcp_compute_ssl_policy module – Creates a GCP SslPolicy

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
> see [Requirements](gcp_compute_ssl_policy_module.md#ansible-collections-google-cloud-gcp-compute-ssl-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_ssl_policy`.

- [Synopsis](gcp_compute_ssl_policy_module.md#synopsis)
- [Requirements](gcp_compute_ssl_policy_module.md#requirements)
- [Parameters](gcp_compute_ssl_policy_module.md#parameters)
- [Notes](gcp_compute_ssl_policy_module.md#notes)
- [Examples](gcp_compute_ssl_policy_module.md#examples)
- [Return Values](gcp_compute_ssl_policy_module.md#return-values)

## [Synopsis](gcp_compute_ssl_policy_module.md#id1)

- Represents a SSL policy. SSL policies give you the ability to control the features of SSL that your SSL proxy or HTTPS load balancer negotiates.

## [Requirements](gcp_compute_ssl_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_ssl_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **custom_features**  list / elements=string | A list of features enabled when the selected profile is CUSTOM. The method returns the set of features that can be specified in this list. This field must be empty if the profile is not CUSTOM. |
| **description**  string | An optional description of this resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **min_tls_version**  string | The minimum version of SSL protocol that can be used by the clients to establish a connection with the load balancer.  Some valid choices include: “TLS_1_0”, “TLS_1_1”, “TLS_1_2” |
| **name**  string / required | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **profile**  string | Profile specifies the set of SSL features that can be used by the load balancer when negotiating SSL with clients. If using `CUSTOM`, the set of SSL features to enable must be specified in the `customFeatures` field.  Some valid choices include: “COMPATIBLE”, “MODERN”, “RESTRICTED”, “CUSTOM” |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](gcp_compute_ssl_policy_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/rest/v1/sslPolicies>
> - Using SSL Policies: <https://cloud.google.com/compute/docs/load-balancing/ssl-policies>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_ssl_policy_module.md#id5)

```yaml+jinja
- name: create a SSL policy
  google.cloud.gcp_compute_ssl_policy:
    name: test_object
    profile: CUSTOM
    min_tls_version: TLS_1_2
    custom_features:
    - TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
    - TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_ssl_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **customFeatures**  list / elements=string | A list of features enabled when the selected profile is CUSTOM. The method returns the set of features that can be specified in this list. This field must be empty if the profile is not CUSTOM.  **Returned:** success |
| **description**  string | An optional description of this resource.  **Returned:** success |
| **enabledFeatures**  list / elements=string | The list of features enabled in the SSL policy.  **Returned:** success |
| **fingerprint**  string | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.  **Returned:** success |
| **id**  integer | The unique identifier for the resource.  **Returned:** success |
| **minTlsVersion**  string | The minimum version of SSL protocol that can be used by the clients to establish a connection with the load balancer.  **Returned:** success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **profile**  string | Profile specifies the set of SSL features that can be used by the load balancer when negotiating SSL with clients. If using `CUSTOM`, the set of SSL features to enable must be specified in the `customFeatures` field.  **Returned:** success |
| **warnings**  complex | If potential misconfigurations are detected for this SSL policy, this field will be populated with warning messages.  **Returned:** success |
| **code**  string | A warning code, if applicable.  **Returned:** success |
| **message**  string | A human-readable description of the warning code.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
