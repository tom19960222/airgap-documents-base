---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_vpn_tunnel_info module – Gather info for GCP VpnTunnel"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_vpn_tunnel_info_module.html
fetched_at: 2026-07-28T02:33:03+00:00
---
# google.cloud.gcp_compute_vpn_tunnel_info module – Gather info for GCP VpnTunnel

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
> see [Requirements](gcp_compute_vpn_tunnel_info_module.md#ansible-collections-google-cloud-gcp-compute-vpn-tunnel-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_vpn_tunnel_info`.

- [Synopsis](gcp_compute_vpn_tunnel_info_module.md#synopsis)
- [Requirements](gcp_compute_vpn_tunnel_info_module.md#requirements)
- [Parameters](gcp_compute_vpn_tunnel_info_module.md#parameters)
- [Notes](gcp_compute_vpn_tunnel_info_module.md#notes)
- [Examples](gcp_compute_vpn_tunnel_info_module.md#examples)
- [Return Values](gcp_compute_vpn_tunnel_info_module.md#return-values)

## [Synopsis](gcp_compute_vpn_tunnel_info_module.md#id1)

- Gather info for GCP VpnTunnel

## [Requirements](gcp_compute_vpn_tunnel_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_vpn_tunnel_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **filters**  list / elements=string | A list of filter value pairs. Available filters are listed here <https://cloud.google.com/sdk/gcloud/reference/topic/filters>.  Each additional filter in the list will act be added as an AND condition (filter1 and filter2) . |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string / required | The region where the tunnel is located. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |

## [Notes](gcp_compute_vpn_tunnel_info_module.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_vpn_tunnel_info_module.md#id5)

```yaml+jinja
- name: get info on a vpn tunnel
  gcp_compute_vpn_tunnel_info:
    region: us-west1
    filters:
    - name = test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_compute_vpn_tunnel_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  **Returned:** always |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **description**  string | An optional description of this resource.  **Returned:** success |
| **id**  string | The unique identifier for the resource. This identifier is defined by the server.  **Returned:** success |
| **ikeVersion**  integer | IKE protocol version to use when establishing the VPN tunnel with peer VPN gateway.  Acceptable IKE versions are 1 or 2. Default version is 2.  **Returned:** success |
| **localTrafficSelector**  list / elements=string | Local traffic selector to use when establishing the VPN tunnel with peer VPN gateway. The value should be a CIDR formatted string, for example `192.168.0.0/16`. The ranges should be disjoint.  Only IPv4 is supported.  **Returned:** success |
| **name**  string | Name of the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **peerExternalGateway**  dictionary | URL of the peer side external VPN gateway to which this VPN tunnel is connected.  **Returned:** success |
| **peerExternalGatewayInterface**  integer | The interface ID of the external VPN gateway to which this VPN tunnel is connected.  **Returned:** success |
| **peerGcpGateway**  dictionary | URL of the peer side HA GCP VPN gateway to which this VPN tunnel is connected.  If provided, the VPN tunnel will automatically use the same vpn_gateway_interface ID in the peer GCP VPN gateway.  **Returned:** success |
| **peerIp**  string | IP address of the peer VPN gateway. Only IPv4 is supported.  **Returned:** success |
| **region**  string | The region where the tunnel is located.  **Returned:** success |
| **remoteTrafficSelector**  list / elements=string | Remote traffic selector to use when establishing the VPN tunnel with peer VPN gateway. The value should be a CIDR formatted string, for example `192.168.0.0/16`. The ranges should be disjoint.  Only IPv4 is supported.  **Returned:** success |
| **router**  dictionary | URL of router resource to be used for dynamic routing.  **Returned:** success |
| **sharedSecret**  string | Shared secret used to set the secure session between the Cloud VPN gateway and the peer VPN gateway.  **Returned:** success |
| **sharedSecretHash**  string | Hash of the shared secret.  **Returned:** success |
| **targetVpnGateway**  dictionary | URL of the Target VPN gateway with which this VPN tunnel is associated.  **Returned:** success |
| **vpnGateway**  dictionary | URL of the VPN gateway with which this VPN tunnel is associated.  This must be used if a High Availability VPN gateway resource is created.  **Returned:** success |
| **vpnGatewayInterface**  integer | The interface ID of the VPN gateway with which this VPN tunnel is associated.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
