---
collection: ansible
version: "6"
title: "google.cloud.gcp_compute_external_vpn_gateway_info module – Gather info for GCP ExternalVpnGateway"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_compute_external_vpn_gateway_info_module.html
fetched_at: 2026-07-27T17:47:54+00:00
---
# google.cloud.gcp_compute_external_vpn_gateway_info module – Gather info for GCP ExternalVpnGateway

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/google/cloud) (version 1.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_compute_external_vpn_gateway_info_module.md#ansible-collections-google-cloud-gcp-compute-external-vpn-gateway-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_external_vpn_gateway_info`.

- [Synopsis](gcp_compute_external_vpn_gateway_info_module.md#synopsis)
- [Requirements](gcp_compute_external_vpn_gateway_info_module.md#requirements)
- [Parameters](gcp_compute_external_vpn_gateway_info_module.md#parameters)
- [Notes](gcp_compute_external_vpn_gateway_info_module.md#notes)
- [Examples](gcp_compute_external_vpn_gateway_info_module.md#examples)
- [Return Values](gcp_compute_external_vpn_gateway_info_module.md#return-values)

## [Synopsis](gcp_compute_external_vpn_gateway_info_module.md#id1)

- Gather info for GCP ExternalVpnGateway

## [Requirements](gcp_compute_external_vpn_gateway_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_external_vpn_gateway_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **filters**  list / elements=string | A list of filter value pairs. Available filters are listed here <https://cloud.google.com/sdk/gcloud/reference/topic/filters>.  Each additional filter in the list will act be added as an AND condition (filter1 and filter2) . |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |

## [Notes](gcp_compute_external_vpn_gateway_info_module.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_external_vpn_gateway_info_module.md#id5)

```yaml+jinja
- name: get info on an external vpn gateway
  gcp_compute_external_vpn_gateway_info:
    filters:
    - name = test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_compute_external_vpn_gateway_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  Returned: always |
| **description**  string | An optional description of this resource.  Returned: success |
| **interfaces**  complex | A list of interfaces on this external VPN gateway.  Returned: success |
| **id**  integer | The numberic ID for this interface. Allowed values are based on the redundancy type of this external VPN gateway \* `0 - SINGLE_IP_INTERNALLY_REDUNDANT` \* `0, 1 - TWO_IPS_REDUNDANCY` \* `0, 1, 2, 3 - FOUR_IPS_REDUNDANCY` .  Returned: success |
| **ipAddress**  string | IP address of the interface in the external VPN gateway.  Only IPv4 is supported. This IP address can be either from your on-premise gateway or another Cloud provider’s VPN gateway, it cannot be an IP address from Google Compute Engine.  Returned: success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  Returned: success |
| **redundancyType**  string | Indicates the redundancy type of this external VPN gateway .  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
