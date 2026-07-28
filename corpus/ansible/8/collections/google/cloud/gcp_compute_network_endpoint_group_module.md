---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_network_endpoint_group module – Creates a GCP NetworkEndpointGroup"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_network_endpoint_group_module.html
fetched_at: 2026-07-28T02:32:20+00:00
---
# google.cloud.gcp_compute_network_endpoint_group module – Creates a GCP NetworkEndpointGroup

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
> see [Requirements](gcp_compute_network_endpoint_group_module.md#ansible-collections-google-cloud-gcp-compute-network-endpoint-group-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_network_endpoint_group`.

- [Synopsis](gcp_compute_network_endpoint_group_module.md#synopsis)
- [Requirements](gcp_compute_network_endpoint_group_module.md#requirements)
- [Parameters](gcp_compute_network_endpoint_group_module.md#parameters)
- [Notes](gcp_compute_network_endpoint_group_module.md#notes)
- [Examples](gcp_compute_network_endpoint_group_module.md#examples)
- [Return Values](gcp_compute_network_endpoint_group_module.md#return-values)

## [Synopsis](gcp_compute_network_endpoint_group_module.md#id1)

- Network endpoint groups (NEGs) are zonal resources that represent collections of IP address and port combinations for GCP resources within a single subnet. Each IP address and port combination is called a network endpoint.
- Network endpoint groups can be used as backends in backend services for HTTP(S), TCP proxy, and SSL proxy load balancers. You cannot use NEGs as a backend with internal load balancers. Because NEG backends allow you to specify IP addresses and ports, you can distribute traffic in a granular fashion among applications or containers running within VM instances.
- Recreating a network endpoint group that’s in use by another resource will give a `resourceInUseByAnotherResource` error. Use `lifecycle.create_before_destroy` to avoid this type of error.

## [Requirements](gcp_compute_network_endpoint_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_network_endpoint_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **default_port**  integer | The default port used if the port number is not specified in the network endpoint. |
| **description**  string | An optional description of this resource. Provide this property when you create the resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **name**  string / required | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **network**  dictionary / required | The network to which all network endpoints in the NEG belong.  Uses “default” project network if unspecified.  This field represents a link to a Network resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_network task and then set this network field to “{{ name-of-resource }}” |
| **network_endpoint_type**  string | Type of network endpoints in this network endpoint group.  Some valid choices include: “GCE_VM_IP_PORT”  **Default:** `"GCE_VM_IP_PORT"` |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnetwork**  dictionary | Optional subnetwork to which all network endpoints in the NEG belong.  This field represents a link to a Subnetwork resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_subnetwork task and then set this subnetwork field to “{{ name-of-resource }}” |
| **zone**  string / required | Zone where the network endpoint group is located. |

## [Notes](gcp_compute_network_endpoint_group_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/rest/beta/networkEndpointGroups>
> - Official Documentation: <https://cloud.google.com/load-balancing/docs/negs/>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_network_endpoint_group_module.md#id5)

```yaml+jinja
- name: create a network
  google.cloud.gcp_compute_network:
    name: "{{ resource_name }}"
    auto_create_subnetworks: 'false'
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: network

- name: create a subnetwork
  google.cloud.gcp_compute_subnetwork:
    name: "{{ resource_name }}"
    ip_cidr_range: 10.0.0.0/16
    region: us-central1
    network: "{{ network }}"
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: subnetwork

- name: create a network endpoint group
  google.cloud.gcp_compute_network_endpoint_group:
    name: test_object
    network: "{{ network }}"
    subnetwork: "{{ subnetwork }}"
    default_port: 90
    zone: us-central1-a
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_network_endpoint_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **defaultPort**  integer | The default port used if the port number is not specified in the network endpoint.  **Returned:** success |
| **description**  string | An optional description of this resource. Provide this property when you create the resource.  **Returned:** success |
| **id**  integer | The unique identifier for the resource.  **Returned:** success |
| **name**  string | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **network**  dictionary | The network to which all network endpoints in the NEG belong.  Uses “default” project network if unspecified.  **Returned:** success |
| **networkEndpointType**  string | Type of network endpoints in this network endpoint group.  **Returned:** success |
| **size**  integer | Number of network endpoints in the network endpoint group.  **Returned:** success |
| **subnetwork**  dictionary | Optional subnetwork to which all network endpoints in the NEG belong.  **Returned:** success |
| **zone**  string | Zone where the network endpoint group is located.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
