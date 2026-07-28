---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_interconnect_attachment module – Creates a GCP InterconnectAttachment"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_interconnect_attachment_module.html
fetched_at: 2026-07-28T02:32:18+00:00
---
# google.cloud.gcp_compute_interconnect_attachment module – Creates a GCP InterconnectAttachment

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
> see [Requirements](gcp_compute_interconnect_attachment_module.md#ansible-collections-google-cloud-gcp-compute-interconnect-attachment-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_interconnect_attachment`.

- [Synopsis](gcp_compute_interconnect_attachment_module.md#synopsis)
- [Requirements](gcp_compute_interconnect_attachment_module.md#requirements)
- [Parameters](gcp_compute_interconnect_attachment_module.md#parameters)
- [Examples](gcp_compute_interconnect_attachment_module.md#examples)
- [Return Values](gcp_compute_interconnect_attachment_module.md#return-values)

## [Synopsis](gcp_compute_interconnect_attachment_module.md#id1)

- Represents an InterconnectAttachment (VLAN attachment) resource. For more information, see Creating VLAN Attachments.

## [Requirements](gcp_compute_interconnect_attachment_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_interconnect_attachment_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **admin_enabled**  boolean | Whether the VLAN attachment is enabled or disabled. When using PARTNER type this will Pre-Activate the interconnect attachment .  **Choices:**   - `false` - `true` ← (default) |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **bandwidth**  string | Provisioned bandwidth capacity for the interconnect attachment.  For attachments of type DEDICATED, the user can set the bandwidth.  For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the bandwidth.  Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED, Defaults to BPS_10G .  Some valid choices include: “BPS_50M”, “BPS_100M”, “BPS_200M”, “BPS_300M”, “BPS_400M”, “BPS_500M”, “BPS_1G”, “BPS_2G”, “BPS_5G”, “BPS_10G”, “BPS_20G”, “BPS_50G” |
| **candidate_subnets**  list / elements=string | Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and customerRouterIpAddress for this attachment.  All prefixes must be within link-local address space (169.254.0.0/16) and must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate prefix(es). The request will fail if all possible /29s are in use on Google’s edge. If not supplied, Google will randomly select an unused /29 from all of link-local space. |
| **description**  string | An optional description of this resource. |
| **edge_availability_domain**  string | Desired availability domain for the attachment. Only available for type PARTNER, at creation time. For improved reliability, customers should configure a pair of attachments with one per availability domain. The selected availability domain will be provided to the Partner via the pairing key so that the provisioned circuit will lie in the specified domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY. |
| **encryption**  string | Indicates the user-supplied encryption option of this interconnect attachment: NONE is the default value, which means that the attachment carries unencrypted traffic. VMs can send traffic to, or receive traffic from, this type of attachment.  IPSEC indicates that the attachment carries only traffic encrypted by an IPsec device such as an HA VPN gateway. VMs cannot directly send traffic to, or receive traffic from, such an attachment. To use IPsec-encrypted Cloud Interconnect create the attachment using this option.  Not currently available publicly.  Some valid choices include: “NONE”, “IPSEC”  **Default:** `"NONE"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **interconnect**  string | URL of the underlying Interconnect object that this attachment’s traffic will traverse through. Required if type is DEDICATED, must not be set if type is PARTNER. |
| **ipsec_internal_addresses**  list / elements=dictionary | URL of addresses that have been reserved for the interconnect attachment, Used only for interconnect attachment that has the encryption option as IPSEC.  The addresses must be RFC 1918 IP address ranges. When creating HA VPN gateway over the interconnect attachment, if the attachment is configured to use an RFC 1918 IP address, then the VPN gateway’s IP address will be allocated from the IP address range specified here.  For example, if the HA VPN gateway’s interface 0 is paired to this interconnect attachment, then an RFC 1918 IP address for the VPN gateway interface 0 will be allocated from the IP address specified for this interconnect attachment.  If this field is not specified for interconnect attachment that has encryption option as IPSEC, later on when creating HA VPN gateway on this interconnect attachment, the HA VPN gateway’s IP address will be allocated from regional external IP address pool. |
| **mtu**  string | Maximum Transmission Unit (MTU), in bytes, of packets passing through this interconnect attachment. Currently, only 1440 and 1500 are allowed. If not specified, the value will default to 1440. |
| **name**  string / required | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string / required | Region where the regional interconnect attachment resides. |
| **router**  dictionary / required | URL of the cloud router to be used for dynamic routing. This router must be in the same region as this InterconnectAttachment. The InterconnectAttachment will automatically connect the Interconnect to the network & region within which the Cloud Router is configured.  This field represents a link to a Router resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_router task and then set this router field to “{{ name-of-resource }}” |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **type**  string | The type of InterconnectAttachment you wish to create. Defaults to DEDICATED.  Some valid choices include: “DEDICATED”, “PARTNER”, “PARTNER_PROVIDER” |
| **vlan_tag8021q**  integer | The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When using PARTNER type this will be managed upstream. |

## [Examples](gcp_compute_interconnect_attachment_module.md#id4)

```yaml+jinja
- name: create a interconnect attachment
  google.cloud.gcp_compute_interconnect_attachment:
    name: test_object
    region: us-central1
    project: test_project
    auth_kind: serviceaccount
    interconnect: https://googleapis.com/compute/v1/projects/test_project/global/interconnects/...
    router: https://googleapis.com/compute/v1/projects/test_project/regions/us-central1/routers/...
    service_account_file: "/tmp/auth.pem"
    state: present
  register: disk
```

## [Return Values](gcp_compute_interconnect_attachment_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **adminEnabled**  boolean | Whether the VLAN attachment is enabled or disabled. When using PARTNER type this will Pre-Activate the interconnect attachment .  **Returned:** success |
| **bandwidth**  string | Provisioned bandwidth capacity for the interconnect attachment.  For attachments of type DEDICATED, the user can set the bandwidth.  For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the bandwidth.  Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED, Defaults to BPS_10G .  **Returned:** success |
| **candidateSubnets**  list / elements=string | Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and customerRouterIpAddress for this attachment.  All prefixes must be within link-local address space (169.254.0.0/16) and must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate prefix(es). The request will fail if all possible /29s are in use on Google’s edge. If not supplied, Google will randomly select an unused /29 from all of link-local space.  **Returned:** success |
| **cloudRouterIpAddress**  string | IPv4 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.  **Returned:** success |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **customerRouterIpAddress**  string | IPv4 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.  **Returned:** success |
| **description**  string | An optional description of this resource.  **Returned:** success |
| **edgeAvailabilityDomain**  string | Desired availability domain for the attachment. Only available for type PARTNER, at creation time. For improved reliability, customers should configure a pair of attachments with one per availability domain. The selected availability domain will be provided to the Partner via the pairing key so that the provisioned circuit will lie in the specified domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY.  **Returned:** success |
| **encryption**  string | Indicates the user-supplied encryption option of this interconnect attachment: NONE is the default value, which means that the attachment carries unencrypted traffic. VMs can send traffic to, or receive traffic from, this type of attachment.  IPSEC indicates that the attachment carries only traffic encrypted by an IPsec device such as an HA VPN gateway. VMs cannot directly send traffic to, or receive traffic from, such an attachment. To use IPsec-encrypted Cloud Interconnect create the attachment using this option.  Not currently available publicly.  **Returned:** success |
| **googleReferenceId**  string | Google reference ID, to be used when raising support tickets with Google or otherwise to debug backend connectivity issues.  **Returned:** success |
| **id**  string | The unique identifier for the resource. This identifier is defined by the server.  **Returned:** success |
| **interconnect**  string | URL of the underlying Interconnect object that this attachment’s traffic will traverse through. Required if type is DEDICATED, must not be set if type is PARTNER.  **Returned:** success |
| **ipsecInternalAddresses**  list / elements=string | URL of addresses that have been reserved for the interconnect attachment, Used only for interconnect attachment that has the encryption option as IPSEC.  The addresses must be RFC 1918 IP address ranges. When creating HA VPN gateway over the interconnect attachment, if the attachment is configured to use an RFC 1918 IP address, then the VPN gateway’s IP address will be allocated from the IP address range specified here.  For example, if the HA VPN gateway’s interface 0 is paired to this interconnect attachment, then an RFC 1918 IP address for the VPN gateway interface 0 will be allocated from the IP address specified for this interconnect attachment.  If this field is not specified for interconnect attachment that has encryption option as IPSEC, later on when creating HA VPN gateway on this interconnect attachment, the HA VPN gateway’s IP address will be allocated from regional external IP address pool.  **Returned:** success |
| **mtu**  string | Maximum Transmission Unit (MTU), in bytes, of packets passing through this interconnect attachment. Currently, only 1440 and 1500 are allowed. If not specified, the value will default to 1440.  **Returned:** success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **pairingKey**  string | [Output only for type PARTNER. Not present for DEDICATED]. The opaque identifier of an PARTNER attachment used to initiate provisioning with a selected partner. Of the form “XXXXX/region/domain” .  **Returned:** success |
| **partnerAsn**  string | [Output only for type PARTNER. Not present for DEDICATED]. Optional BGP ASN for the router that should be supplied by a layer 3 Partner if they configured BGP on behalf of the customer.  **Returned:** success |
| **privateInterconnectInfo**  complex | Information specific to an InterconnectAttachment. This property is populated if the interconnect that this is attached to is of type DEDICATED.  **Returned:** success |
| **tag8021q**  integer | 802.1q encapsulation tag to be used for traffic between Google and the customer, going to and from this network and region.  **Returned:** success |
| **region**  string | Region where the regional interconnect attachment resides.  **Returned:** success |
| **router**  dictionary | URL of the cloud router to be used for dynamic routing. This router must be in the same region as this InterconnectAttachment. The InterconnectAttachment will automatically connect the Interconnect to the network & region within which the Cloud Router is configured.  **Returned:** success |
| **state**  string | [Output Only] The current state of this attachment’s functionality.  **Returned:** success |
| **type**  string | The type of InterconnectAttachment you wish to create. Defaults to DEDICATED.  **Returned:** success |
| **vlanTag8021q**  integer | The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When using PARTNER type this will be managed upstream.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
