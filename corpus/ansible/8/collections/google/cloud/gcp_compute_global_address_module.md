---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_global_address module – Creates a GCP GlobalAddress"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_global_address_module.html
fetched_at: 2026-07-28T02:32:03+00:00
---
# google.cloud.gcp_compute_global_address module – Creates a GCP GlobalAddress

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
> see [Requirements](gcp_compute_global_address_module.md#ansible-collections-google-cloud-gcp-compute-global-address-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_global_address`.

- [Synopsis](gcp_compute_global_address_module.md#synopsis)
- [Requirements](gcp_compute_global_address_module.md#requirements)
- [Parameters](gcp_compute_global_address_module.md#parameters)
- [Notes](gcp_compute_global_address_module.md#notes)
- [Examples](gcp_compute_global_address_module.md#examples)
- [Return Values](gcp_compute_global_address_module.md#return-values)

## [Synopsis](gcp_compute_global_address_module.md#id1)

- Represents a Global Address resource. Global addresses are used for HTTP(S) load balancing.

## [Requirements](gcp_compute_global_address_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_global_address_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **address**  string | The static external IP address represented by this resource. |
| **address_type**  string | The type of the address to reserve.  \* EXTERNAL indicates public/external single IP address.  \* INTERNAL indicates internal IP ranges belonging to some network.  Some valid choices include: “EXTERNAL”, “INTERNAL”  **Default:** `"EXTERNAL"` |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **description**  string | An optional description of this resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **ip_version**  string | The IP Version that will be used by this address. The default value is `IPV4`.  Some valid choices include: “IPV4”, “IPV6” |
| **name**  string / required | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **network**  dictionary | The URL of the network in which to reserve the IP range. The IP range must be in RFC1918 space. The network cannot be deleted if there are any reserved IP ranges referring to it.  This should only be set when using an Internal address.  This field represents a link to a Network resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_network task and then set this network field to “{{ name-of-resource }}” |
| **prefix_length**  integer | The prefix length of the IP range. If not present, it means the address field is a single IP address.  This field is not applicable to addresses with addressType=EXTERNAL, or addressType=INTERNAL when purpose=PRIVATE_SERVICE_CONNECT . |
| **project**  string | The Google Cloud Platform project to use. |
| **purpose**  string | The purpose of the resource. Possible values include: \* VPC_PEERING - for peer networks \* PRIVATE_SERVICE_CONNECT - for ([Beta](<https://terraform.io/docs/providers/google/guides/provider_versions.html>) only) Private Service Connect networks . |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](gcp_compute_global_address_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/v1/globalAddresses>
> - Reserving a Static External IP Address: <https://cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_global_address_module.md#id5)

```yaml+jinja
- name: create a global address
  google.cloud.gcp_compute_global_address:
    name: test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_global_address_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address**  string | The static external IP address represented by this resource.  **Returned:** success |
| **addressType**  string | The type of the address to reserve.  \* EXTERNAL indicates public/external single IP address.  \* INTERNAL indicates internal IP ranges belonging to some network.  **Returned:** success |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **description**  string | An optional description of this resource.  **Returned:** success |
| **id**  integer | The unique identifier for the resource. This identifier is defined by the server.  **Returned:** success |
| **ipVersion**  string | The IP Version that will be used by this address. The default value is `IPV4`.  **Returned:** success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **network**  dictionary | The URL of the network in which to reserve the IP range. The IP range must be in RFC1918 space. The network cannot be deleted if there are any reserved IP ranges referring to it.  This should only be set when using an Internal address.  **Returned:** success |
| **prefixLength**  integer | The prefix length of the IP range. If not present, it means the address field is a single IP address.  This field is not applicable to addresses with addressType=EXTERNAL, or addressType=INTERNAL when purpose=PRIVATE_SERVICE_CONNECT .  **Returned:** success |
| **purpose**  string | The purpose of the resource. Possible values include: \* VPC_PEERING - for peer networks \* PRIVATE_SERVICE_CONNECT - for ([Beta](<https://terraform.io/docs/providers/google/guides/provider_versions.html>) only) Private Service Connect networks .  **Returned:** success |
| **region**  string | A reference to the region where the regional address resides.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
