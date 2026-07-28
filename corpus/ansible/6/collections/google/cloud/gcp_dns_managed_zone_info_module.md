---
collection: ansible
version: "6"
title: "google.cloud.gcp_dns_managed_zone_info module – Gather info for GCP ManagedZone"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_dns_managed_zone_info_module.html
fetched_at: 2026-07-27T17:48:59+00:00
---
# google.cloud.gcp_dns_managed_zone_info module – Gather info for GCP ManagedZone

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
> see [Requirements](gcp_dns_managed_zone_info_module.md#ansible-collections-google-cloud-gcp-dns-managed-zone-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_dns_managed_zone_info`.

- [Synopsis](gcp_dns_managed_zone_info_module.md#synopsis)
- [Requirements](gcp_dns_managed_zone_info_module.md#requirements)
- [Parameters](gcp_dns_managed_zone_info_module.md#parameters)
- [Notes](gcp_dns_managed_zone_info_module.md#notes)
- [Examples](gcp_dns_managed_zone_info_module.md#examples)
- [Return Values](gcp_dns_managed_zone_info_module.md#return-values)

## [Synopsis](gcp_dns_managed_zone_info_module.md#id1)

- Gather info for GCP ManagedZone

## [Requirements](gcp_dns_managed_zone_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_dns_managed_zone_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **dns_name**  list / elements=string | Restricts the list to return only zones with this domain name. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |

## [Notes](gcp_dns_managed_zone_info_module.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_dns_managed_zone_info_module.md#id5)

```yaml+jinja
- name: get info on a managed zone
  gcp_dns_managed_zone_info:
    dns_name: test.somewild2.example.com.
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_dns_managed_zone_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  Returned: always |
| **creationTime**  string | The time that this resource was created on the server.  This is in RFC3339 text format.  Returned: success |
| **description**  string | A mutable string of at most 1024 characters associated with this resource for the user’s convenience. Has no effect on the managed zone’s function.  Returned: success |
| **dnsName**  string | The DNS name of this managed zone, for instance “example.com.”.  Returned: success |
| **dnssecConfig**  complex | DNSSEC configuration.  Returned: success |
| **defaultKeySpecs**  complex | Specifies parameters that will be used for generating initial DnsKeys for this ManagedZone. If you provide a spec for keySigning or zoneSigning, you must also provide one for the other.  default_key_specs can only be updated when the state is `off`.  Returned: success |
| **algorithm**  string | String mnemonic specifying the DNSSEC algorithm of this key.  Returned: success |
| **keyLength**  integer | Length of the keys in bits.  Returned: success |
| **keyType**  string | Specifies whether this is a key signing key (KSK) or a zone signing key (ZSK). Key signing keys have the Secure Entry Point flag set and, when active, will only be used to sign resource record sets of type DNSKEY. Zone signing keys do not have the Secure Entry Point flag set and will be used to sign all other types of resource record sets.  Returned: success |
| **kind**  string | Identifies what kind of resource this is.  Returned: success |
| **kind**  string | Identifies what kind of resource this is.  Returned: success |
| **nonExistence**  string | Specifies the mechanism used to provide authenticated denial-of-existence responses.  non_existence can only be updated when the state is `off`.  Returned: success |
| **state**  string | Specifies whether DNSSEC is enabled, and what mode it is in.  Returned: success |
| **forwardingConfig**  complex | The presence for this field indicates that outbound forwarding is enabled for this zone. The value of this field contains the set of destinations to forward to.  Returned: success |
| **targetNameServers**  complex | List of target name servers to forward to. Cloud DNS will select the best available name server if more than one target is given.  Returned: success |
| **forwardingPath**  string | Forwarding path for this TargetNameServer. If unset or `default` Cloud DNS will make forwarding decision based on address ranges, i.e. RFC1918 addresses go to the VPC, Non-RFC1918 addresses go to the Internet. When set to `private`, Cloud DNS will always send queries through VPC for this target .  Returned: success |
| **ipv4Address**  string | IPv4 address of a target name server.  Returned: success |
| **id**  integer | Unique identifier for the resource; defined by the server.  Returned: success |
| **labels**  dictionary | A set of key/value label pairs to assign to this ManagedZone.  Returned: success |
| **name**  string | User assigned name for this resource.  Must be unique within the project.  Returned: success |
| **nameServers**  list / elements=string | Delegate your managed_zone to these virtual name servers; defined by the server .  Returned: success |
| **nameServerSet**  string | Optionally specifies the NameServerSet for this ManagedZone. A NameServerSet is a set of DNS name servers that all host the same ManagedZones. Most users will leave this field unset.  Returned: success |
| **peeringConfig**  complex | The presence of this field indicates that DNS Peering is enabled for this zone. The value of this field contains the network to peer with.  Returned: success |
| **targetNetwork**  complex | The network with which to peer.  Returned: success |
| **networkUrl**  string | The fully qualified URL of the VPC network to forward queries to.  This should be formatted like `<https://www.googleapis.com/compute/v1/projects>/{project}/global/networks/{network}%60 .  Returned: success |
| **privateVisibilityConfig**  complex | For privately visible zones, the set of Virtual Private Cloud resources that the zone is visible from.  Returned: success |
| **networks**  complex | The list of VPC networks that can see this zone.  Returned: success |
| **networkUrl**  string | The fully qualified URL of the VPC network to bind to.  This should be formatted like `<https://www.googleapis.com/compute/v1/projects>/{project}/global/networks/{network}%60 .  Returned: success |
| **visibility**  string | The zone’s visibility: public zones are exposed to the Internet, while private zones are visible only to Virtual Private Cloud resources.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
