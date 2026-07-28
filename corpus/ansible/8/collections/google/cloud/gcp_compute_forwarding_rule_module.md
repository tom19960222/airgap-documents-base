---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_forwarding_rule module – Creates a GCP ForwardingRule"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_forwarding_rule_module.html
fetched_at: 2026-07-28T02:32:02+00:00
---
# google.cloud.gcp_compute_forwarding_rule module – Creates a GCP ForwardingRule

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
> see [Requirements](gcp_compute_forwarding_rule_module.md#ansible-collections-google-cloud-gcp-compute-forwarding-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_forwarding_rule`.

- [Synopsis](gcp_compute_forwarding_rule_module.md#synopsis)
- [Requirements](gcp_compute_forwarding_rule_module.md#requirements)
- [Parameters](gcp_compute_forwarding_rule_module.md#parameters)
- [Notes](gcp_compute_forwarding_rule_module.md#notes)
- [Examples](gcp_compute_forwarding_rule_module.md#examples)
- [Return Values](gcp_compute_forwarding_rule_module.md#return-values)

## [Synopsis](gcp_compute_forwarding_rule_module.md#id1)

- A ForwardingRule resource. A ForwardingRule resource specifies which pool of target virtual machines to forward a packet to if it matches the given [IPAddress, IPProtocol, portRange] tuple.

## [Requirements](gcp_compute_forwarding_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_forwarding_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **all_ports**  boolean | For internal TCP/UDP load balancing (i.e. load balancing scheme is INTERNAL and protocol is TCP/UDP), set this to true to allow packets addressed to any ports to be forwarded to the backends configured with this forwarding rule. Used with backend service. Cannot be set if port or portRange are set.  **Choices:**   - `false` - `true` |
| **allow_global_access**  boolean | If true, clients can access ILB from all regions.  Otherwise only allows from the local region the ILB is located at.  **Choices:**   - `false` - `true` |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **backend_service**  dictionary | A BackendService to receive the matched traffic. This is used only for INTERNAL load balancing.  This field represents a link to a BackendService resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_backend_service task and then set this backend_service field to “{{ name-of-resource }}” |
| **description**  string | An optional description of this resource. Provide this property when you create the resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **ip_address**  string | The IP address that this forwarding rule is serving on behalf of.  Addresses are restricted based on the forwarding rule’s load balancing scheme (EXTERNAL or INTERNAL) and scope (global or regional).  When the load balancing scheme is EXTERNAL, for global forwarding rules, the address must be a global IP, and for regional forwarding rules, the address must live in the same region as the forwarding rule. If this field is empty, an ephemeral IPv4 address from the same scope (global or regional) will be assigned. A regional forwarding rule supports IPv4 only. A global forwarding rule supports either IPv4 or IPv6.  When the load balancing scheme is INTERNAL, this can only be an RFC 1918 IP address belonging to the network/subnet configured for the forwarding rule. By default, if this field is empty, an ephemeral internal IP address will be automatically allocated from the IP range of the subnet or network configured for this forwarding rule.  An address can be specified either by a literal IP address or a URL reference to an existing Address resource. The following examples are all valid: \* 100.1.2.3 \* <https://www.googleapis.com/compute/v1/projects/project/regions/region/addresses/address> \* projects/project/regions/region/addresses/address \* regions/region/addresses/address \* global/addresses/address \* address . |
| **ip_protocol**  string | The IP protocol to which this rule applies.  When the load balancing scheme is INTERNAL, only TCP and UDP are valid.  Some valid choices include: “TCP”, “UDP”, “ESP”, “AH”, “SCTP”, “ICMP” |
| **is_mirroring_collector**  boolean | Indicates whether or not this load balancer can be used as a collector for packet mirroring. To prevent mirroring loops, instances behind this load balancer will not have their traffic mirrored even if a PacketMirroring rule applies to them. This can only be set to true for load balancers that have their loadBalancingScheme set to INTERNAL.  **Choices:**   - `false` - `true` |
| **load_balancing_scheme**  string | This signifies what the ForwardingRule will be used for and can be EXTERNAL, INTERNAL, or INTERNAL_MANAGED. EXTERNAL is used for Classic Cloud VPN gateways, protocol forwarding to VMs from an external IP address, and HTTP(S), SSL Proxy, TCP Proxy, and Network TCP/UDP load balancers.  INTERNAL is used for protocol forwarding to VMs from an internal IP address, and internal TCP/UDP load balancers.  INTERNAL_MANAGED is used for internal HTTP(S) load balancers.  Some valid choices include: “EXTERNAL”, “INTERNAL”, “INTERNAL_MANAGED” |
| **name**  string / required | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **network**  dictionary | For internal load balancing, this field identifies the network that the load balanced IP should belong to for this Forwarding Rule. If this field is not specified, the default network will be used.  This field is only used for INTERNAL load balancing.  This field represents a link to a Network resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_network task and then set this network field to “{{ name-of-resource }}” |
| **network_tier**  string | The networking tier used for configuring this address. If this field is not specified, it is assumed to be PREMIUM.  Some valid choices include: “PREMIUM”, “STANDARD” |
| **port_range**  string | This field is used along with the target field for TargetHttpProxy, TargetHttpsProxy, TargetSslProxy, TargetTcpProxy, TargetVpnGateway, TargetPool, TargetInstance.  Applicable only when IPProtocol is TCP, UDP, or SCTP, only packets addressed to ports in the specified range will be forwarded to target.  Forwarding rules with the same [IPAddress, IPProtocol] pair must have disjoint port ranges.  Some types of forwarding target have constraints on the acceptable ports: \* TargetHttpProxy: 80, 8080 \* TargetHttpsProxy: 443 \* TargetTcpProxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222 \* TargetSslProxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222 \* TargetVpnGateway: 500, 4500 . |
| **ports**  list / elements=string | This field is used along with the backend_service field for internal load balancing.  When the load balancing scheme is INTERNAL, a single port or a comma separated list of ports can be configured. Only packets addressed to these ports will be forwarded to the backends configured with this forwarding rule.  You may specify a maximum of up to 5 ports. |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string / required | A reference to the region where the regional forwarding rule resides.  This field is not applicable to global forwarding rules. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **service_label**  string | An optional prefix to the service name for this Forwarding Rule.  If specified, will be the first label of the fully qualified service name.  The label must be 1-63 characters long, and comply with RFC1035.  Specifically, the label must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  This field is only used for INTERNAL load balancing. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnetwork**  dictionary | The subnetwork that the load balanced IP should belong to for this Forwarding Rule. This field is only used for INTERNAL load balancing.  If the network specified is in auto subnet mode, this field is optional. However, if the network is in custom subnet mode, a subnetwork must be specified.  This field represents a link to a Subnetwork resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_subnetwork task and then set this subnetwork field to “{{ name-of-resource }}” |
| **target**  string | The URL of the target resource to receive the matched traffic.  The target must live in the same region as the forwarding rule.  The forwarded traffic must be of a type appropriate to the target object. |

## [Notes](gcp_compute_forwarding_rule_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/v1/forwardingRules>
> - Official Documentation: <https://cloud.google.com/compute/docs/load-balancing/network/forwarding-rules>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_forwarding_rule_module.md#id5)

```yaml+jinja
- name: create a address
  google.cloud.gcp_compute_address:
    name: address-forwardingrule
    region: us-west1
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: address

- name: create a target pool
  google.cloud.gcp_compute_target_pool:
    name: targetpool-forwardingrule
    region: us-west1
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: targetpool

- name: create a forwarding rule
  google.cloud.gcp_compute_forwarding_rule:
    name: test_object
    region: us-west1
    target: "{{ targetpool }}"
    ip_protocol: TCP
    port_range: 80-80
    ip_address: "{{ address.address }}"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_forwarding_rule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allowGlobalAccess**  boolean | If true, clients can access ILB from all regions.  Otherwise only allows from the local region the ILB is located at.  **Returned:** success |
| **allPorts**  boolean | For internal TCP/UDP load balancing (i.e. load balancing scheme is INTERNAL and protocol is TCP/UDP), set this to true to allow packets addressed to any ports to be forwarded to the backends configured with this forwarding rule. Used with backend service. Cannot be set if port or portRange are set.  **Returned:** success |
| **backendService**  dictionary | A BackendService to receive the matched traffic. This is used only for INTERNAL load balancing.  **Returned:** success |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **description**  string | An optional description of this resource. Provide this property when you create the resource.  **Returned:** success |
| **id**  integer | The unique identifier for the resource.  **Returned:** success |
| **IPAddress**  string | The IP address that this forwarding rule is serving on behalf of.  Addresses are restricted based on the forwarding rule’s load balancing scheme (EXTERNAL or INTERNAL) and scope (global or regional).  When the load balancing scheme is EXTERNAL, for global forwarding rules, the address must be a global IP, and for regional forwarding rules, the address must live in the same region as the forwarding rule. If this field is empty, an ephemeral IPv4 address from the same scope (global or regional) will be assigned. A regional forwarding rule supports IPv4 only. A global forwarding rule supports either IPv4 or IPv6.  When the load balancing scheme is INTERNAL, this can only be an RFC 1918 IP address belonging to the network/subnet configured for the forwarding rule. By default, if this field is empty, an ephemeral internal IP address will be automatically allocated from the IP range of the subnet or network configured for this forwarding rule.  An address can be specified either by a literal IP address or a URL reference to an existing Address resource. The following examples are all valid: \* 100.1.2.3 \* <https://www.googleapis.com/compute/v1/projects/project/regions/region/addresses/address> \* projects/project/regions/region/addresses/address \* regions/region/addresses/address \* global/addresses/address \* address .  **Returned:** success |
| **IPProtocol**  string | The IP protocol to which this rule applies.  When the load balancing scheme is INTERNAL, only TCP and UDP are valid.  **Returned:** success |
| **isMirroringCollector**  boolean | Indicates whether or not this load balancer can be used as a collector for packet mirroring. To prevent mirroring loops, instances behind this load balancer will not have their traffic mirrored even if a PacketMirroring rule applies to them. This can only be set to true for load balancers that have their loadBalancingScheme set to INTERNAL.  **Returned:** success |
| **loadBalancingScheme**  string | This signifies what the ForwardingRule will be used for and can be EXTERNAL, INTERNAL, or INTERNAL_MANAGED. EXTERNAL is used for Classic Cloud VPN gateways, protocol forwarding to VMs from an external IP address, and HTTP(S), SSL Proxy, TCP Proxy, and Network TCP/UDP load balancers.  INTERNAL is used for protocol forwarding to VMs from an internal IP address, and internal TCP/UDP load balancers.  INTERNAL_MANAGED is used for internal HTTP(S) load balancers.  **Returned:** success |
| **name**  string | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **network**  dictionary | For internal load balancing, this field identifies the network that the load balanced IP should belong to for this Forwarding Rule. If this field is not specified, the default network will be used.  This field is only used for INTERNAL load balancing.  **Returned:** success |
| **networkTier**  string | The networking tier used for configuring this address. If this field is not specified, it is assumed to be PREMIUM.  **Returned:** success |
| **portRange**  string | This field is used along with the target field for TargetHttpProxy, TargetHttpsProxy, TargetSslProxy, TargetTcpProxy, TargetVpnGateway, TargetPool, TargetInstance.  Applicable only when IPProtocol is TCP, UDP, or SCTP, only packets addressed to ports in the specified range will be forwarded to target.  Forwarding rules with the same [IPAddress, IPProtocol] pair must have disjoint port ranges.  Some types of forwarding target have constraints on the acceptable ports: \* TargetHttpProxy: 80, 8080 \* TargetHttpsProxy: 443 \* TargetTcpProxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222 \* TargetSslProxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222 \* TargetVpnGateway: 500, 4500 .  **Returned:** success |
| **ports**  list / elements=string | This field is used along with the backend_service field for internal load balancing.  When the load balancing scheme is INTERNAL, a single port or a comma separated list of ports can be configured. Only packets addressed to these ports will be forwarded to the backends configured with this forwarding rule.  You may specify a maximum of up to 5 ports.  **Returned:** success |
| **region**  string | A reference to the region where the regional forwarding rule resides.  This field is not applicable to global forwarding rules.  **Returned:** success |
| **serviceLabel**  string | An optional prefix to the service name for this Forwarding Rule.  If specified, will be the first label of the fully qualified service name.  The label must be 1-63 characters long, and comply with RFC1035.  Specifically, the label must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  This field is only used for INTERNAL load balancing.  **Returned:** success |
| **serviceName**  string | The internal fully qualified service name for this Forwarding Rule.  This field is only used for INTERNAL load balancing.  **Returned:** success |
| **subnetwork**  dictionary | The subnetwork that the load balanced IP should belong to for this Forwarding Rule. This field is only used for INTERNAL load balancing.  If the network specified is in auto subnet mode, this field is optional. However, if the network is in custom subnet mode, a subnetwork must be specified.  **Returned:** success |
| **target**  string | The URL of the target resource to receive the matched traffic.  The target must live in the same region as the forwarding rule.  The forwarded traffic must be of a type appropriate to the target object.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
