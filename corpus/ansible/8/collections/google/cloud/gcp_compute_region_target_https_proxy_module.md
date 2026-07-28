---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_region_target_https_proxy module – Creates a GCP RegionTargetHttpsProxy"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_region_target_https_proxy_module.html
fetched_at: 2026-07-28T02:32:34+00:00
---
# google.cloud.gcp_compute_region_target_https_proxy module – Creates a GCP RegionTargetHttpsProxy

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
> see [Requirements](gcp_compute_region_target_https_proxy_module.md#ansible-collections-google-cloud-gcp-compute-region-target-https-proxy-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_region_target_https_proxy`.

- [Synopsis](gcp_compute_region_target_https_proxy_module.md#synopsis)
- [Requirements](gcp_compute_region_target_https_proxy_module.md#requirements)
- [Parameters](gcp_compute_region_target_https_proxy_module.md#parameters)
- [Notes](gcp_compute_region_target_https_proxy_module.md#notes)
- [Examples](gcp_compute_region_target_https_proxy_module.md#examples)
- [Return Values](gcp_compute_region_target_https_proxy_module.md#return-values)

## [Synopsis](gcp_compute_region_target_https_proxy_module.md#id1)

- Represents a RegionTargetHttpsProxy resource, which is used by one or more forwarding rules to route incoming HTTPS requests to a URL map.

## [Requirements](gcp_compute_region_target_https_proxy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_region_target_https_proxy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **description**  string | An optional description of this resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **name**  string / required | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string / required | The region where the regional proxy resides. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **ssl_certificates**  list / elements=dictionary / required | A list of RegionSslCertificate resources that are used to authenticate connections between users and the load balancer. Currently, exactly one SSL certificate must be specified. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **url_map**  dictionary / required | A reference to the RegionUrlMap resource that defines the mapping from URL to the RegionBackendService.  This field represents a link to a RegionUrlMap resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_region_url_map task and then set this url_map field to “{{ name-of-resource }}” |

## [Notes](gcp_compute_region_target_https_proxy_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpsProxies>
> - Official Documentation: <https://cloud.google.com/compute/docs/load-balancing/http/target-proxies>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_region_target_https_proxy_module.md#id5)

```yaml+jinja
- name: create a instance group
  google.cloud.gcp_compute_instance_group:
    name: instancegroup-targethttpsproxy
    zone: us-central1-a
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: instancegroup

- name: create a region health check
  google.cloud.gcp_compute_region_health_check:
    name: "{{ resource_name }}"
    type: HTTPS
    healthy_threshold: 10
    timeout_sec: 2
    unhealthy_threshold: 5
    region: us-central1
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: healthcheck

- name: create a region backend service
  google.cloud.gcp_compute_region_backend_service:
    name: backendservice-targethttpsproxy
    region: us-central1
    backends:
    - group: "{{ instancegroup.selfLink }}"
    healthchecks:
    - "{{ healthcheck.selfLink }}"
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: backendservice

- name: create a region URL map
  google.cloud.gcp_compute_region_url_map:
    name: urlmap-targethttpsproxy
    region: us-central1
    default_service: "{{ backendservice }}"
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: urlmap

- name: create a SSL certificate
  google.cloud.gcp_compute_ssl_certificate:
    name: sslcert-targethttpsproxy
    description: A certificate for testing. Do not use this certificate in production
    certificate: |-
      -----BEGIN CERTIFICATE-----
      MIICqjCCAk+gAwIBAgIJAIuJ+0352Kq4MAoGCCqGSM49BAMCMIGwMQswCQYDVQQG
      EwJVUzETMBEGA1UECAwKV2FzaGluZ3RvbjERMA8GA1UEBwwIS2lya2xhbmQxFTAT
      BgNVBAoMDEdvb2dsZSwgSW5jLjEeMBwGA1UECwwVR29vZ2xlIENsb3VkIFBsYXRm
      b3JtMR8wHQYDVQQDDBZ3d3cubXktc2VjdXJlLXNpdGUuY29tMSEwHwYJKoZIhvcN
      AQkBFhJuZWxzb25hQGdvb2dsZS5jb20wHhcNMTcwNjI4MDQ1NjI2WhcNMjcwNjI2
      MDQ1NjI2WjCBsDELMAkGA1UEBhMCVVMxEzARBgNVBAgMCldhc2hpbmd0b24xETAP
      BgNVBAcMCEtpcmtsYW5kMRUwEwYDVQQKDAxHb29nbGUsIEluYy4xHjAcBgNVBAsM
      FUdvb2dsZSBDbG91ZCBQbGF0Zm9ybTEfMB0GA1UEAwwWd3d3Lm15LXNlY3VyZS1z
      aXRlLmNvbTEhMB8GCSqGSIb3DQEJARYSbmVsc29uYUBnb29nbGUuY29tMFkwEwYH
      KoZIzj0CAQYIKoZIzj0DAQcDQgAEHGzpcRJ4XzfBJCCPMQeXQpTXwlblimODQCuQ
      4mzkzTv0dXyB750fOGN02HtkpBOZzzvUARTR10JQoSe2/5PIwaNQME4wHQYDVR0O
      BBYEFKIQC3A2SDpxcdfn0YLKineDNq/BMB8GA1UdIwQYMBaAFKIQC3A2SDpxcdfn
      0YLKineDNq/BMAwGA1UdEwQFMAMBAf8wCgYIKoZIzj0EAwIDSQAwRgIhALs4vy+O
      M3jcqgA4fSW/oKw6UJxp+M6a+nGMX+UJR3YgAiEAvvl39QRVAiv84hdoCuyON0lJ
      zqGNhIPGq2ULqXKK8BY=
      -----END CERTIFICATE-----
    private_key: |-
      -----BEGIN EC PRIVATE KEY-----
      MHcCAQEEIObtRo8tkUqoMjeHhsOh2ouPpXCgBcP+EDxZCB/tws15oAoGCCqGSM49
      AwEHoUQDQgAEHGzpcRJ4XzfBJCCPMQeXQpTXwlblimODQCuQ4mzkzTv0dXyB750f
      OGN02HtkpBOZzzvUARTR10JQoSe2/5PIwQ==
      -----END EC PRIVATE KEY-----
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: sslcert

- name: create a region target HTTPS proxy
  google.cloud.gcp_compute_region_target_https_proxy:
    name: test_object
    region: us-central1
    ssl_certificates:
    - "{{ sslcert }}"
    url_map: "{{ urlmap }}"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_region_target_https_proxy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **description**  string | An optional description of this resource.  **Returned:** success |
| **id**  integer | The unique identifier for the resource.  **Returned:** success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **region**  string | The region where the regional proxy resides.  **Returned:** success |
| **sslCertificates**  list / elements=string | A list of RegionSslCertificate resources that are used to authenticate connections between users and the load balancer. Currently, exactly one SSL certificate must be specified.  **Returned:** success |
| **urlMap**  dictionary | A reference to the RegionUrlMap resource that defines the mapping from URL to the RegionBackendService.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
