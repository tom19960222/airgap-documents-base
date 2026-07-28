---
collection: ansible
version: "6"
title: "google.cloud.gcp_compute_target_vpn_gateway module – Creates a GCP TargetVpnGateway"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_compute_target_vpn_gateway_module.html
fetched_at: 2026-07-27T17:48:50+00:00
---
# google.cloud.gcp_compute_target_vpn_gateway module – Creates a GCP TargetVpnGateway

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
> see [Requirements](gcp_compute_target_vpn_gateway_module.md#ansible-collections-google-cloud-gcp-compute-target-vpn-gateway-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_target_vpn_gateway`.

- [Synopsis](gcp_compute_target_vpn_gateway_module.md#synopsis)
- [Requirements](gcp_compute_target_vpn_gateway_module.md#requirements)
- [Parameters](gcp_compute_target_vpn_gateway_module.md#parameters)
- [Notes](gcp_compute_target_vpn_gateway_module.md#notes)
- [Examples](gcp_compute_target_vpn_gateway_module.md#examples)
- [Return Values](gcp_compute_target_vpn_gateway_module.md#return-values)

## [Synopsis](gcp_compute_target_vpn_gateway_module.md#id1)

- Represents a VPN gateway running in GCP. This virtual device is managed by Google, but used only by you.

## [Requirements](gcp_compute_target_vpn_gateway_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_target_vpn_gateway_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **description**  string | An optional description of this resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **name**  string / required | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **network**  dictionary / required | The network this VPN gateway is accepting traffic for.  This field represents a link to a Network resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_network task and then set this network field to “{{ name-of-resource }}” |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string / required | The region this gateway should sit in. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](gcp_compute_target_vpn_gateway_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_target_vpn_gateway_module.md#id5)

```yaml+jinja
- name: create a address
  google.cloud.gcp_compute_address:
    name: address-vpngateway
    region: us-west1
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: address

- name: create a network
  google.cloud.gcp_compute_network:
    name: network-vpngateway
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: network

- name: create a target vpn gateway
  google.cloud.gcp_compute_target_vpn_gateway:
    name: test_object
    region: us-west1
    network: "{{ network }}"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_target_vpn_gateway_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  Returned: success |
| **description**  string | An optional description of this resource.  Returned: success |
| **forwardingRules**  list / elements=string | A list of references to the ForwardingRule resources associated with this VPN gateway.  Returned: success |
| **id**  integer | The unique identifier for the resource.  Returned: success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  Returned: success |
| **network**  dictionary | The network this VPN gateway is accepting traffic for.  Returned: success |
| **region**  string | The region this gateway should sit in.  Returned: success |
| **tunnels**  list / elements=string | A list of references to VpnTunnel resources associated with this VPN gateway.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
