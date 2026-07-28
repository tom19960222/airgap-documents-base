---
collection: ansible
version: "6"
title: "google.cloud.gcp_compute_vpn_tunnel module – Creates a GCP VpnTunnel"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_compute_vpn_tunnel_module.html
fetched_at: 2026-07-27T17:48:54+00:00
---
# google.cloud.gcp_compute_vpn_tunnel module – Creates a GCP VpnTunnel

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
> see [Requirements](gcp_compute_vpn_tunnel_module.md#ansible-collections-google-cloud-gcp-compute-vpn-tunnel-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_vpn_tunnel`.

- [Synopsis](gcp_compute_vpn_tunnel_module.md#synopsis)
- [Requirements](gcp_compute_vpn_tunnel_module.md#requirements)
- [Parameters](gcp_compute_vpn_tunnel_module.md#parameters)
- [Notes](gcp_compute_vpn_tunnel_module.md#notes)
- [Examples](gcp_compute_vpn_tunnel_module.md#examples)
- [Return Values](gcp_compute_vpn_tunnel_module.md#return-values)

## [Synopsis](gcp_compute_vpn_tunnel_module.md#id1)

- VPN tunnel resource.

## [Requirements](gcp_compute_vpn_tunnel_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_vpn_tunnel_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **description**  string | An optional description of this resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **ike_version**  integer | IKE protocol version to use when establishing the VPN tunnel with peer VPN gateway.  Acceptable IKE versions are 1 or 2. Default version is 2.  Default: `2` |
| **local_traffic_selector**  list / elements=string | Local traffic selector to use when establishing the VPN tunnel with peer VPN gateway. The value should be a CIDR formatted string, for example `192.168.0.0/16`. The ranges should be disjoint.  Only IPv4 is supported. |
| **name**  string / required | Name of the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **peer_external_gateway**  dictionary | URL of the peer side external VPN gateway to which this VPN tunnel is connected.  This field represents a link to a ExternalVpnGateway resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_external_vpn_gateway task and then set this peer_external_gateway field to “{{ name-of-resource }}” |
| **peer_external_gateway_interface**  integer | The interface ID of the external VPN gateway to which this VPN tunnel is connected. |
| **peer_gcp_gateway**  dictionary | URL of the peer side HA GCP VPN gateway to which this VPN tunnel is connected.  If provided, the VPN tunnel will automatically use the same vpn_gateway_interface ID in the peer GCP VPN gateway.  This field represents a link to a VpnGateway resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_vpn_gateway task and then set this peer_gcp_gateway field to “{{ name-of-resource }}” |
| **peer_ip**  string | IP address of the peer VPN gateway. Only IPv4 is supported. |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string / required | The region where the tunnel is located. |
| **remote_traffic_selector**  list / elements=string | Remote traffic selector to use when establishing the VPN tunnel with peer VPN gateway. The value should be a CIDR formatted string, for example `192.168.0.0/16`. The ranges should be disjoint.  Only IPv4 is supported. |
| **router**  dictionary | URL of router resource to be used for dynamic routing.  This field represents a link to a Router resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_router task and then set this router field to “{{ name-of-resource }}” |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **shared_secret**  string / required | Shared secret used to set the secure session between the Cloud VPN gateway and the peer VPN gateway. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |
| **target_vpn_gateway**  dictionary | URL of the Target VPN gateway with which this VPN tunnel is associated.  This field represents a link to a TargetVpnGateway resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_target_vpn_gateway task and then set this target_vpn_gateway field to “{{ name-of-resource }}” |
| **vpn_gateway**  dictionary | URL of the VPN gateway with which this VPN tunnel is associated.  This must be used if a High Availability VPN gateway resource is created.  This field represents a link to a VpnGateway resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_vpn_gateway task and then set this vpn_gateway field to “{{ name-of-resource }}” |
| **vpn_gateway_interface**  integer | The interface ID of the VPN gateway with which this VPN tunnel is associated. |

## [Notes](gcp_compute_vpn_tunnel_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels>
> - Cloud VPN Overview: <https://cloud.google.com/vpn/docs/concepts/overview>
> - Networks and Tunnel Routing: <https://cloud.google.com/vpn/docs/concepts/choosing-networks-routing>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_vpn_tunnel_module.md#id5)

```yaml+jinja
- name: create a network
  google.cloud.gcp_compute_network:
    name: network-vpn-tunnel
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: network

- name: create a router
  google.cloud.gcp_compute_router:
    name: router-vpn-tunnel
    network: "{{ network }}"
    bgp:
      asn: 64514
      advertise_mode: CUSTOM
      advertised_groups:
      - ALL_SUBNETS
      advertised_ip_ranges:
      - range: 1.2.3.4
      - range: 6.7.0.0/16
    region: us-central1
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: router

- name: create a target vpn gateway
  google.cloud.gcp_compute_target_vpn_gateway:
    name: gateway-vpn-tunnel
    region: us-west1
    network: "{{ network }}"
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: gateway

- name: create a vpn tunnel
  google.cloud.gcp_compute_vpn_tunnel:
    name: test_object
    region: us-west1
    target_vpn_gateway: "{{ gateway }}"
    router: "{{ router }}"
    shared_secret: super secret
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_vpn_tunnel_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  Returned: success |
| **description**  string | An optional description of this resource.  Returned: success |
| **id**  string | The unique identifier for the resource. This identifier is defined by the server.  Returned: success |
| **ikeVersion**  integer | IKE protocol version to use when establishing the VPN tunnel with peer VPN gateway.  Acceptable IKE versions are 1 or 2. Default version is 2.  Returned: success |
| **localTrafficSelector**  list / elements=string | Local traffic selector to use when establishing the VPN tunnel with peer VPN gateway. The value should be a CIDR formatted string, for example `192.168.0.0/16`. The ranges should be disjoint.  Only IPv4 is supported.  Returned: success |
| **name**  string | Name of the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  Returned: success |
| **peerExternalGateway**  dictionary | URL of the peer side external VPN gateway to which this VPN tunnel is connected.  Returned: success |
| **peerExternalGatewayInterface**  integer | The interface ID of the external VPN gateway to which this VPN tunnel is connected.  Returned: success |
| **peerGcpGateway**  dictionary | URL of the peer side HA GCP VPN gateway to which this VPN tunnel is connected.  If provided, the VPN tunnel will automatically use the same vpn_gateway_interface ID in the peer GCP VPN gateway.  Returned: success |
| **peerIp**  string | IP address of the peer VPN gateway. Only IPv4 is supported.  Returned: success |
| **region**  string | The region where the tunnel is located.  Returned: success |
| **remoteTrafficSelector**  list / elements=string | Remote traffic selector to use when establishing the VPN tunnel with peer VPN gateway. The value should be a CIDR formatted string, for example `192.168.0.0/16`. The ranges should be disjoint.  Only IPv4 is supported.  Returned: success |
| **router**  dictionary | URL of router resource to be used for dynamic routing.  Returned: success |
| **sharedSecret**  string | Shared secret used to set the secure session between the Cloud VPN gateway and the peer VPN gateway.  Returned: success |
| **sharedSecretHash**  string | Hash of the shared secret.  Returned: success |
| **targetVpnGateway**  dictionary | URL of the Target VPN gateway with which this VPN tunnel is associated.  Returned: success |
| **vpnGateway**  dictionary | URL of the VPN gateway with which this VPN tunnel is associated.  This must be used if a High Availability VPN gateway resource is created.  Returned: success |
| **vpnGatewayInterface**  integer | The interface ID of the VPN gateway with which this VPN tunnel is associated.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
