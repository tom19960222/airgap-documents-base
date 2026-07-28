---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_network module – Creates a GCP Network"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_network_module.html
fetched_at: 2026-07-28T02:32:20+00:00
---
# google.cloud.gcp_compute_network module – Creates a GCP Network

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
> see [Requirements](gcp_compute_network_module.md#ansible-collections-google-cloud-gcp-compute-network-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_network`.

- [Synopsis](gcp_compute_network_module.md#synopsis)
- [Requirements](gcp_compute_network_module.md#requirements)
- [Parameters](gcp_compute_network_module.md#parameters)
- [Notes](gcp_compute_network_module.md#notes)
- [Examples](gcp_compute_network_module.md#examples)
- [Return Values](gcp_compute_network_module.md#return-values)

## [Synopsis](gcp_compute_network_module.md#id1)

- Manages a VPC network or legacy network resource on GCP.

## [Requirements](gcp_compute_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **auto_create_subnetworks**  boolean | When set to `true`, the network is created in “auto subnet mode” and it will create a subnet for each region automatically across the `10.128.0.0/9` address range.  When set to `false`, the network is created in “custom subnet mode” so the user can explicitly connect subnetwork resources.  **Choices:**   - `false` - `true` |
| **description**  string | An optional description of this resource. The resource must be recreated to modify this field. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **mtu**  integer | Maximum Transmission Unit in bytes. The minimum value for this field is 1460 and the maximum value is 1500 bytes. |
| **name**  string / required | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **project**  string | The Google Cloud Platform project to use. |
| **routing_config**  dictionary | The network-level routing configuration for this network. Used by Cloud Router to determine what type of network-wide routing behavior to enforce. |
| **routing_mode**  string / required | The network-wide routing mode to use. If set to `REGIONAL`, this network’s cloud routers will only advertise routes with subnetworks of this network in the same region as the router. If set to `GLOBAL`, this network’s cloud routers will advertise routes with all subnetworks of this network, across regions.  Some valid choices include: “REGIONAL”, “GLOBAL” |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](gcp_compute_network_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/rest/v1/networks>
> - Official Documentation: <https://cloud.google.com/vpc/docs/vpc>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_network_module.md#id5)

```yaml+jinja
- name: create a network
  google.cloud.gcp_compute_network:
    name: test_object
    auto_create_subnetworks: 'true'
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_network_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **autoCreateSubnetworks**  boolean | When set to `true`, the network is created in “auto subnet mode” and it will create a subnet for each region automatically across the `10.128.0.0/9` address range.  When set to `false`, the network is created in “custom subnet mode” so the user can explicitly connect subnetwork resources.  **Returned:** success |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **description**  string | An optional description of this resource. The resource must be recreated to modify this field.  **Returned:** success |
| **gateway_ipv4**  string | The gateway address for default routing out of the network. This value is selected by GCP.  **Returned:** success |
| **id**  integer | The unique identifier for the resource.  **Returned:** success |
| **mtu**  integer | Maximum Transmission Unit in bytes. The minimum value for this field is 1460 and the maximum value is 1500 bytes.  **Returned:** success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **routingConfig**  complex | The network-level routing configuration for this network. Used by Cloud Router to determine what type of network-wide routing behavior to enforce.  **Returned:** success |
| **routingMode**  string | The network-wide routing mode to use. If set to `REGIONAL`, this network’s cloud routers will only advertise routes with subnetworks of this network in the same region as the router. If set to `GLOBAL`, this network’s cloud routers will advertise routes with all subnetworks of this network, across regions.  **Returned:** success |
| **subnetworks**  list / elements=string | Server-defined fully-qualified URLs for all subnetworks in this network.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
