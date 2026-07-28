---
collection: ansible
version: "6"
title: "google.cloud.gcp_compute_subnetwork module – Creates a GCP Subnetwork"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_compute_subnetwork_module.html
fetched_at: 2026-07-27T17:48:40+00:00
---
# google.cloud.gcp_compute_subnetwork module – Creates a GCP Subnetwork

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
> see [Requirements](gcp_compute_subnetwork_module.md#ansible-collections-google-cloud-gcp-compute-subnetwork-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_subnetwork`.

- [Synopsis](gcp_compute_subnetwork_module.md#synopsis)
- [Requirements](gcp_compute_subnetwork_module.md#requirements)
- [Parameters](gcp_compute_subnetwork_module.md#parameters)
- [Notes](gcp_compute_subnetwork_module.md#notes)
- [Examples](gcp_compute_subnetwork_module.md#examples)
- [Return Values](gcp_compute_subnetwork_module.md#return-values)

## [Synopsis](gcp_compute_subnetwork_module.md#id1)

- A VPC network is a virtual version of the traditional physical networks that exist within and between physical data centers. A VPC network provides connectivity for your Compute Engine virtual machine (VM) instances, Container Engine containers, App Engine Flex services, and other network-related resources.
- Each GCP project contains one or more VPC networks. Each VPC network is a global entity spanning all GCP regions. This global VPC network allows VM instances and other resources to communicate with each other via internal, private IP addresses.
- Each VPC network is subdivided into subnets, and each subnet is contained within a single region. You can have more than one subnet in a region for a given VPC network. Each subnet has a contiguous private RFC1918 IP space. You create instances, containers, and the like in these subnets.
- When you create an instance, you must create it in a subnet, and the instance draws its internal IP address from that subnet.
- Virtual machine (VM) instances in a VPC network can communicate with instances in all other subnets of the same VPC network, regardless of region, using their RFC1918 private IP addresses. You can isolate portions of the network, even entire subnets, using firewall rules.

## [Requirements](gcp_compute_subnetwork_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_subnetwork_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **description**  string | An optional description of this resource. Provide this property when you create the resource. This field can be set only at resource creation time. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **ip_cidr_range**  string / required | The range of internal addresses that are owned by this subnetwork.  Provide this property when you create the subnetwork. For example, 10.0.0.0/8 or 192.168.0.0/16. Ranges must be unique and non-overlapping within a network. Only IPv4 is supported. |
| **name**  string / required | The name of the resource, provided by the client when initially creating the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **network**  dictionary / required | The network this subnet belongs to.  Only networks that are in the distributed mode can have subnetworks.  This field represents a link to a Network resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_network task and then set this network field to “{{ name-of-resource }}” |
| **private_ip_google_access**  boolean | When enabled, VMs in this subnetwork without external IP addresses can access Google APIs and services by using Private Google Access.  Choices:   - `false` - `true` |
| **private_ipv6_google_access**  string | The private IPv6 google access type for the VMs in this subnet. |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string / required | The GCP region for this subnetwork. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **secondary_ip_ranges**  list / elements=dictionary | An array of configurations for secondary IP ranges for VM instances contained in this subnetwork. The primary IP of such VM must belong to the primary ipCidrRange of the subnetwork. The alias IPs may belong to either primary or secondary ranges. |
| **ip_cidr_range**  string / required | The range of IP addresses belonging to this subnetwork secondary range. Provide this property when you create the subnetwork.  Ranges must be unique and non-overlapping with all primary and secondary IP ranges within a network. Only IPv4 is supported. |
| **range_name**  string / required | The name associated with this subnetwork secondary range, used when adding an alias IP range to a VM instance. The name must be 1-63 characters long, and comply with RFC1035. The name must be unique within the subnetwork. |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](gcp_compute_subnetwork_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/rest/v1/subnetworks>
> - Private Google Access: <https://cloud.google.com/vpc/docs/configure-private-google-access>
> - Cloud Networking: <https://cloud.google.com/vpc/docs/using-vpc>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_subnetwork_module.md#id5)

```yaml+jinja
- name: create a network
  google.cloud.gcp_compute_network:
    name: network-subnetwork
    auto_create_subnetworks: 'true'
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: network

- name: create a subnetwork
  google.cloud.gcp_compute_subnetwork:
    name: ansiblenet
    region: us-west1
    network: "{{ network }}"
    ip_cidr_range: 172.16.0.0/16
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_subnetwork_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  Returned: success |
| **description**  string | An optional description of this resource. Provide this property when you create the resource. This field can be set only at resource creation time.  Returned: success |
| **gatewayAddress**  string | The gateway address for default routes to reach destination addresses outside this subnetwork.  Returned: success |
| **id**  integer | The unique identifier for the resource.  Returned: success |
| **ipCidrRange**  string | The range of internal addresses that are owned by this subnetwork.  Provide this property when you create the subnetwork. For example, 10.0.0.0/8 or 192.168.0.0/16. Ranges must be unique and non-overlapping within a network. Only IPv4 is supported.  Returned: success |
| **name**  string | The name of the resource, provided by the client when initially creating the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  Returned: success |
| **network**  dictionary | The network this subnet belongs to.  Only networks that are in the distributed mode can have subnetworks.  Returned: success |
| **privateIpGoogleAccess**  boolean | When enabled, VMs in this subnetwork without external IP addresses can access Google APIs and services by using Private Google Access.  Returned: success |
| **privateIpv6GoogleAccess**  string | The private IPv6 google access type for the VMs in this subnet.  Returned: success |
| **region**  string | The GCP region for this subnetwork.  Returned: success |
| **secondaryIpRanges**  complex | An array of configurations for secondary IP ranges for VM instances contained in this subnetwork. The primary IP of such VM must belong to the primary ipCidrRange of the subnetwork. The alias IPs may belong to either primary or secondary ranges.  Returned: success |
| **ipCidrRange**  string | The range of IP addresses belonging to this subnetwork secondary range. Provide this property when you create the subnetwork.  Ranges must be unique and non-overlapping with all primary and secondary IP ranges within a network. Only IPv4 is supported.  Returned: success |
| **rangeName**  string | The name associated with this subnetwork secondary range, used when adding an alias IP range to a VM instance. The name must be 1-63 characters long, and comply with RFC1035. The name must be unique within the subnetwork.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
