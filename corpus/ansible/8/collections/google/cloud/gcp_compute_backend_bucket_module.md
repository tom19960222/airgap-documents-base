---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_backend_bucket module – Creates a GCP BackendBucket"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_backend_bucket_module.html
fetched_at: 2026-07-28T02:31:54+00:00
---
# google.cloud.gcp_compute_backend_bucket module – Creates a GCP BackendBucket

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
> see [Requirements](gcp_compute_backend_bucket_module.md#ansible-collections-google-cloud-gcp-compute-backend-bucket-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_backend_bucket`.

- [Synopsis](gcp_compute_backend_bucket_module.md#synopsis)
- [Requirements](gcp_compute_backend_bucket_module.md#requirements)
- [Parameters](gcp_compute_backend_bucket_module.md#parameters)
- [Notes](gcp_compute_backend_bucket_module.md#notes)
- [Examples](gcp_compute_backend_bucket_module.md#examples)
- [Return Values](gcp_compute_backend_bucket_module.md#return-values)

## [Synopsis](gcp_compute_backend_bucket_module.md#id1)

- Backend buckets allow you to use Google Cloud Storage buckets with HTTP(S) load balancing.
- An HTTP(S) load balancer can direct traffic to specified URLs to a backend bucket rather than a backend service. It can send requests for static content to a Cloud Storage bucket and requests for dynamic content to a virtual machine instance.

## [Requirements](gcp_compute_backend_bucket_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_backend_bucket_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **bucket_name**  string / required | Cloud Storage bucket name. |
| **cdn_policy**  dictionary | Cloud CDN configuration for this Backend Bucket. |
| **cache_mode**  string | Specifies the cache setting for all responses from this backend.  The possible values are: USE_ORIGIN_HEADERS, FORCE_CACHE_ALL and CACHE_ALL_STATIC .  Some valid choices include: “USE_ORIGIN_HEADERS”, “FORCE_CACHE_ALL”, “CACHE_ALL_STATIC” |
| **client_ttl**  integer | Specifies the maximum allowed TTL for cached content served by this origin. |
| **default_ttl**  integer | Specifies the default TTL for cached content served by this origin for responses that do not have an existing valid TTL (max-age or s-max-age). |
| **max_ttl**  integer | Specifies the maximum allowed TTL for cached content served by this origin. |
| **negative_caching**  boolean | Negative caching allows per-status code TTLs to be set, in order to apply fine-grained caching for common errors or redirects.  **Choices:**   - `false` - `true` |
| **negative_caching_policy**  list / elements=dictionary | Sets a cache TTL for the specified HTTP status code. negativeCaching must be enabled to configure negativeCachingPolicy.  Omitting the policy and leaving negativeCaching enabled will use Cloud CDN’s default cache TTLs. |
| **code**  integer | The HTTP status code to define a TTL against. Only HTTP status codes 300, 301, 308, 404, 405, 410, 421, 451 and 501 can be specified as values, and you cannot specify a status code more than once. |
| **ttl**  integer | The TTL (in seconds) for which to cache responses with the corresponding status code. The maximum allowed value is 1800s (30 minutes), noting that infrequently accessed objects may be evicted from the cache before the defined TTL. |
| **serve_while_stale**  integer | Serve existing content from the cache (if available) when revalidating content with the origin, or when an error is encountered when refreshing the cache. |
| **signed_url_cache_max_age_sec**  integer | Maximum number of seconds the response to a signed URL request will be considered fresh. After this time period, the response will be revalidated before being served.  When serving responses to signed URL requests, Cloud CDN will internally behave as though all responses from this backend had a “Cache-Control: public, max-age=[TTL]” header, regardless of any existing Cache-Control header. The actual headers served in responses will not be altered. |
| **custom_response_headers**  list / elements=string | Headers that the HTTP/S load balancer should add to proxied responses. |
| **description**  string | An optional textual description of the resource; provided by the client when the resource is created. |
| **enable_cdn**  boolean | If true, enable Cloud CDN for this BackendBucket.  **Choices:**   - `false` - `true` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **name**  string / required | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](gcp_compute_backend_bucket_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/v1/backendBuckets>
> - Using a Cloud Storage bucket as a load balancer backend: <https://cloud.google.com/compute/docs/load-balancing/http/backend-bucket>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_backend_bucket_module.md#id5)

```yaml+jinja
- name: create a bucket
  google.cloud.gcp_storage_bucket:
    name: bucket-backendbucket
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: bucket

- name: create a backend bucket
  google.cloud.gcp_compute_backend_bucket:
    name: test_object
    bucket_name: "{{ bucket.name }}"
    description: A BackendBucket to connect LNB w/ Storage Bucket
    enable_cdn: 'true'
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_backend_bucket_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **bucketName**  string | Cloud Storage bucket name.  **Returned:** success |
| **cdnPolicy**  complex | Cloud CDN configuration for this Backend Bucket.  **Returned:** success |
| **cacheMode**  string | Specifies the cache setting for all responses from this backend.  The possible values are: USE_ORIGIN_HEADERS, FORCE_CACHE_ALL and CACHE_ALL_STATIC .  **Returned:** success |
| **clientTtl**  integer | Specifies the maximum allowed TTL for cached content served by this origin.  **Returned:** success |
| **defaultTtl**  integer | Specifies the default TTL for cached content served by this origin for responses that do not have an existing valid TTL (max-age or s-max-age).  **Returned:** success |
| **maxTtl**  integer | Specifies the maximum allowed TTL for cached content served by this origin.  **Returned:** success |
| **negativeCaching**  boolean | Negative caching allows per-status code TTLs to be set, in order to apply fine-grained caching for common errors or redirects.  **Returned:** success |
| **negativeCachingPolicy**  complex | Sets a cache TTL for the specified HTTP status code. negativeCaching must be enabled to configure negativeCachingPolicy.  Omitting the policy and leaving negativeCaching enabled will use Cloud CDN’s default cache TTLs.  **Returned:** success |
| **code**  integer | The HTTP status code to define a TTL against. Only HTTP status codes 300, 301, 308, 404, 405, 410, 421, 451 and 501 can be specified as values, and you cannot specify a status code more than once.  **Returned:** success |
| **ttl**  integer | The TTL (in seconds) for which to cache responses with the corresponding status code. The maximum allowed value is 1800s (30 minutes), noting that infrequently accessed objects may be evicted from the cache before the defined TTL.  **Returned:** success |
| **serveWhileStale**  integer | Serve existing content from the cache (if available) when revalidating content with the origin, or when an error is encountered when refreshing the cache.  **Returned:** success |
| **signedUrlCacheMaxAgeSec**  integer | Maximum number of seconds the response to a signed URL request will be considered fresh. After this time period, the response will be revalidated before being served.  When serving responses to signed URL requests, Cloud CDN will internally behave as though all responses from this backend had a “Cache-Control: public, max-age=[TTL]” header, regardless of any existing Cache-Control header. The actual headers served in responses will not be altered.  **Returned:** success |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **customResponseHeaders**  list / elements=string | Headers that the HTTP/S load balancer should add to proxied responses.  **Returned:** success |
| **description**  string | An optional textual description of the resource; provided by the client when the resource is created.  **Returned:** success |
| **enableCdn**  boolean | If true, enable Cloud CDN for this BackendBucket.  **Returned:** success |
| **id**  integer | Unique identifier for the resource.  **Returned:** success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
