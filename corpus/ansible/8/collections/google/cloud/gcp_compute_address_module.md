---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_address module – Creates a GCP Address"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_address_module.html
fetched_at: 2026-07-28T02:31:51+00:00
---
# google.cloud.gcp_compute_address module – Creates a GCP Address

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
> see [Requirements](gcp_compute_address_module.md#ansible-collections-google-cloud-gcp-compute-address-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_address`.

- [Synopsis](gcp_compute_address_module.md#synopsis)
- [Requirements](gcp_compute_address_module.md#requirements)
- [Parameters](gcp_compute_address_module.md#parameters)
- [Notes](gcp_compute_address_module.md#notes)
- [Examples](gcp_compute_address_module.md#examples)
- [Return Values](gcp_compute_address_module.md#return-values)

## [Synopsis](gcp_compute_address_module.md#id1)

- Represents an Address resource.
- Each virtual machine instance has an ephemeral internal IP address and, optionally, an external IP address. To communicate between instances on the same network, you can use an instance’s internal IP address. To communicate with the Internet and instances outside of the same network, you must specify the instance’s external IP address.
- Internal IP addresses are ephemeral and only belong to an instance for the lifetime of the instance; if the instance is deleted and recreated, the instance is assigned a new internal IP address, either by Compute Engine or by you. External IP addresses can be either ephemeral or static.

## [Requirements](gcp_compute_address_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_address_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **address**  string | The static external IP address represented by this resource. Only IPv4 is supported. An address may only be specified for INTERNAL address types. The IP address must be inside the specified subnetwork, if any. |
| **address_type**  string | The type of address to reserve.  Some valid choices include: “INTERNAL”, “EXTERNAL”  **Default:** `"EXTERNAL"` |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **description**  string | An optional description of this resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **name**  string / required | Name of the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **network**  dictionary | The URL of the network in which to reserve the address. This field can only be used with INTERNAL type with the VPC_PEERING and IPSEC_INTERCONNECT purposes.  This field represents a link to a Network resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_network task and then set this network field to “{{ name-of-resource }}” |
| **network_tier**  string | The networking tier used for configuring this address. If this field is not specified, it is assumed to be PREMIUM.  Some valid choices include: “PREMIUM”, “STANDARD” |
| **prefix_length**  integer | The prefix length if the resource represents an IP range. |
| **project**  string | The Google Cloud Platform project to use. |
| **purpose**  string | The purpose of this resource, which can be one of the following values: \* GCE_ENDPOINT for addresses that are used by VM instances, alias IP ranges, internal load balancers, and similar resources.  \* SHARED_LOADBALANCER_VIP for an address that can be used by multiple internal load balancers.  \* VPC_PEERING for addresses that are reserved for VPC peer networks.  \* IPSEC_INTERCONNECT for addresses created from a private IP range that are reserved for a VLAN attachment in an IPsec-encrypted Cloud Interconnect configuration. These addresses are regional resources.  This should only be set when using an Internal address. |
| **region**  string / required | URL of the region where the regional address resides.  This field is not applicable to global addresses. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnetwork**  dictionary | The URL of the subnetwork in which to reserve the address. If an IP address is specified, it must be within the subnetwork’s IP range.  This field can only be used with INTERNAL type with GCE_ENDPOINT/DNS_RESOLVER purposes.  This field represents a link to a Subnetwork resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_subnetwork task and then set this subnetwork field to “{{ name-of-resource }}” |

## [Notes](gcp_compute_address_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/beta/addresses>
> - Reserving a Static External IP Address: <https://cloud.google.com/compute/docs/instances-and-network>
> - Reserving a Static Internal IP Address: <https://cloud.google.com/compute/docs/ip-addresses/reserve-static-internal-ip-address>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_address_module.md#id5)

```yaml+jinja
- name: create a address
  google.cloud.gcp_compute_address:
    name: test-address1
    region: us-west1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_address_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address**  string | The static external IP address represented by this resource. Only IPv4 is supported. An address may only be specified for INTERNAL address types. The IP address must be inside the specified subnetwork, if any.  **Returned:** success |
| **addressType**  string | The type of address to reserve.  **Returned:** success |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **description**  string | An optional description of this resource.  **Returned:** success |
| **id**  integer | The unique identifier for the resource.  **Returned:** success |
| **name**  string | Name of the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **network**  dictionary | The URL of the network in which to reserve the address. This field can only be used with INTERNAL type with the VPC_PEERING and IPSEC_INTERCONNECT purposes.  **Returned:** success |
| **networkTier**  string | The networking tier used for configuring this address. If this field is not specified, it is assumed to be PREMIUM.  **Returned:** success |
| **prefixLength**  integer | The prefix length if the resource represents an IP range.  **Returned:** success |
| **purpose**  string | The purpose of this resource, which can be one of the following values: \* GCE_ENDPOINT for addresses that are used by VM instances, alias IP ranges, internal load balancers, and similar resources.  \* SHARED_LOADBALANCER_VIP for an address that can be used by multiple internal load balancers.  \* VPC_PEERING for addresses that are reserved for VPC peer networks.  \* IPSEC_INTERCONNECT for addresses created from a private IP range that are reserved for a VLAN attachment in an IPsec-encrypted Cloud Interconnect configuration. These addresses are regional resources.  This should only be set when using an Internal address.  **Returned:** success |
| **region**  string | URL of the region where the regional address resides.  This field is not applicable to global addresses.  **Returned:** success |
| **status**  string | The status of the address, which can be one of RESERVING, RESERVED, or IN_USE.  An address that is RESERVING is currently in the process of being reserved.  A RESERVED address is currently reserved and available to use. An IN_USE address is currently being used by another resource and is not available.  **Returned:** success |
| **subnetwork**  dictionary | The URL of the subnetwork in which to reserve the address. If an IP address is specified, it must be within the subnetwork’s IP range.  This field can only be used with INTERNAL type with GCE_ENDPOINT/DNS_RESOLVER purposes.  **Returned:** success |
| **users**  list / elements=string | The URLs of the resources that are using this address.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
