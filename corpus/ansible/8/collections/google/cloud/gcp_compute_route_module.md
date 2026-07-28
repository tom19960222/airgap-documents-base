---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_route module – Creates a GCP Route"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_route_module.html
fetched_at: 2026-07-28T02:32:41+00:00
---
# google.cloud.gcp_compute_route module – Creates a GCP Route

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
> see [Requirements](gcp_compute_route_module.md#ansible-collections-google-cloud-gcp-compute-route-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_route`.

- [Synopsis](gcp_compute_route_module.md#synopsis)
- [Requirements](gcp_compute_route_module.md#requirements)
- [Parameters](gcp_compute_route_module.md#parameters)
- [Notes](gcp_compute_route_module.md#notes)
- [Examples](gcp_compute_route_module.md#examples)
- [Return Values](gcp_compute_route_module.md#return-values)

## [Synopsis](gcp_compute_route_module.md#id1)

- Represents a Route resource.
- A route is a rule that specifies how certain packets should be handled by the virtual network. Routes are associated with virtual machines by tag, and the set of routes for a particular virtual machine is called its routing table. For each packet leaving a virtual machine, the system searches that virtual machine’s routing table for a single best matching route.
- Routes match packets by destination IP address, preferring smaller or more specific ranges over larger ones. If there is a tie, the system selects the route with the smallest priority value. If there is still a tie, it uses the layer three and four packet headers to select just one of the remaining matching routes. The packet is then forwarded as specified by the next_hop field of the winning route – either to another virtual machine destination, a virtual machine gateway or a Compute Engine-operated gateway. Packets that do not match any route in the sending virtual machine’s routing table will be dropped.
- A Route resource must have exactly one specification of either nextHopGateway, nextHopInstance, nextHopIp, nextHopVpnTunnel, or nextHopIlb.

## [Requirements](gcp_compute_route_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_route_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **description**  string | An optional description of this resource. Provide this property when you create the resource. |
| **dest_range**  string / required | The destination range of outgoing packets that this route applies to.  Only IPv4 is supported. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **name**  string / required | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **network**  dictionary / required | The network that this route applies to.  This field represents a link to a Network resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_network task and then set this network field to “{{ name-of-resource }}” |
| **next_hop_gateway**  string | URL to a gateway that should handle matching packets.  Currently, you can only specify the internet gateway, using a full or partial valid URL: \* <https://www.googleapis.com/compute/v1/projects/project/global/gateways/default-internet-gateway> \* projects/project/global/gateways/default-internet-gateway \* global/gateways/default-internet-gateway . |
| **next_hop_ilb**  dictionary | The URL to a forwarding rule of type loadBalancingScheme=INTERNAL that should handle matching packets.  You can only specify the forwarding rule as a partial or full URL. For example, the following are all valid URLs: <https://www.googleapis.com/compute/v1/projects/project/regions/region/forwardingRules/forwardingRule> regions/region/forwardingRules/forwardingRule Note that this can only be used when the destinationRange is a public (non-RFC 1918) IP CIDR range.  This field represents a link to a ForwardingRule resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_forwarding_rule task and then set this next_hop_ilb field to “{{ name-of-resource }}” |
| **next_hop_instance**  dictionary | URL to an instance that should handle matching packets.  You can specify this as a full or partial URL. For example: \* <https://www.googleapis.com/compute/v1/projects/project/zones/zone/> instances/instance \* projects/project/zones/zone/instances/instance \* zones/zone/instances/instance .  This field represents a link to a Instance resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_instance task and then set this next_hop_instance field to “{{ name-of-resource }}” |
| **next_hop_ip**  string | Network IP address of an instance that should handle matching packets. |
| **next_hop_vpn_tunnel**  dictionary | URL to a VpnTunnel that should handle matching packets.  This field represents a link to a VpnTunnel resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_vpn_tunnel task and then set this next_hop_vpn_tunnel field to “{{ name-of-resource }}” |
| **priority**  integer | The priority of this route. Priority is used to break ties in cases where there is more than one matching route of equal prefix length.  In the case of two routes with equal prefix length, the one with the lowest-numbered priority value wins.  Default value is 1000. Valid range is 0 through 65535. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | A list of instance tags to which this route applies. |

## [Notes](gcp_compute_route_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/rest/v1/routes>
> - Using Routes: <https://cloud.google.com/vpc/docs/using-routes>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_route_module.md#id5)

```yaml+jinja
- name: create a network
  google.cloud.gcp_compute_network:
    name: network-route
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: network

- name: create a route
  google.cloud.gcp_compute_route:
    name: test_object
    dest_range: 192.168.6.0/24
    next_hop_gateway: global/gateways/default-internet-gateway
    network: "{{ network }}"
    tags:
    - backends
    - databases
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_route_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | An optional description of this resource. Provide this property when you create the resource.  **Returned:** success |
| **destRange**  string | The destination range of outgoing packets that this route applies to.  Only IPv4 is supported.  **Returned:** success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **network**  dictionary | The network that this route applies to.  **Returned:** success |
| **nextHopGateway**  string | URL to a gateway that should handle matching packets.  Currently, you can only specify the internet gateway, using a full or partial valid URL: \* <https://www.googleapis.com/compute/v1/projects/project/global/gateways/default-internet-gateway> \* projects/project/global/gateways/default-internet-gateway \* global/gateways/default-internet-gateway .  **Returned:** success |
| **nextHopIlb**  dictionary | The URL to a forwarding rule of type loadBalancingScheme=INTERNAL that should handle matching packets.  You can only specify the forwarding rule as a partial or full URL. For example, the following are all valid URLs: <https://www.googleapis.com/compute/v1/projects/project/regions/region/forwardingRules/forwardingRule> regions/region/forwardingRules/forwardingRule Note that this can only be used when the destinationRange is a public (non-RFC 1918) IP CIDR range.  **Returned:** success |
| **nextHopInstance**  dictionary | URL to an instance that should handle matching packets.  You can specify this as a full or partial URL. For example: \* <https://www.googleapis.com/compute/v1/projects/project/zones/zone/> instances/instance \* projects/project/zones/zone/instances/instance \* zones/zone/instances/instance .  **Returned:** success |
| **nextHopIp**  string | Network IP address of an instance that should handle matching packets.  **Returned:** success |
| **nextHopNetwork**  string | URL to a Network that should handle matching packets.  **Returned:** success |
| **nextHopVpnTunnel**  dictionary | URL to a VpnTunnel that should handle matching packets.  **Returned:** success |
| **priority**  integer | The priority of this route. Priority is used to break ties in cases where there is more than one matching route of equal prefix length.  In the case of two routes with equal prefix length, the one with the lowest-numbered priority value wins.  Default value is 1000. Valid range is 0 through 65535.  **Returned:** success |
| **tags**  list / elements=string | A list of instance tags to which this route applies.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
