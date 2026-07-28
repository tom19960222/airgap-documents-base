---
collection: ansible
version: "6"
title: "google.cloud.gcp_compute_global_forwarding_rule module – Creates a GCP GlobalForwardingRule"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_compute_global_forwarding_rule_module.html
fetched_at: 2026-07-27T17:47:59+00:00
---
# google.cloud.gcp_compute_global_forwarding_rule module – Creates a GCP GlobalForwardingRule

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
> see [Requirements](gcp_compute_global_forwarding_rule_module.md#ansible-collections-google-cloud-gcp-compute-global-forwarding-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_global_forwarding_rule`.

- [Synopsis](gcp_compute_global_forwarding_rule_module.md#synopsis)
- [Requirements](gcp_compute_global_forwarding_rule_module.md#requirements)
- [Parameters](gcp_compute_global_forwarding_rule_module.md#parameters)
- [Examples](gcp_compute_global_forwarding_rule_module.md#examples)
- [Return Values](gcp_compute_global_forwarding_rule_module.md#return-values)

## [Synopsis](gcp_compute_global_forwarding_rule_module.md#id1)

- Represents a GlobalForwardingRule resource. Global forwarding rules are used to forward traffic to the correct load balancer for HTTP load balancing. Global forwarding rules can only be used for HTTP load balancing.
- For more information, see <https://cloud.google.com/compute/docs/load-balancing/http/> .

## [Requirements](gcp_compute_global_forwarding_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_global_forwarding_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **description**  string | An optional description of this resource. Provide this property when you create the resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **ip_address**  string | The IP address that this forwarding rule is serving on behalf of.  Addresses are restricted based on the forwarding rule’s load balancing scheme (EXTERNAL or INTERNAL) and scope (global or regional).  When the load balancing scheme is EXTERNAL, for global forwarding rules, the address must be a global IP, and for regional forwarding rules, the address must live in the same region as the forwarding rule. If this field is empty, an ephemeral IPv4 address from the same scope (global or regional) will be assigned. A regional forwarding rule supports IPv4 only. A global forwarding rule supports either IPv4 or IPv6.  When the load balancing scheme is INTERNAL, this can only be an RFC 1918 IP address belonging to the network/subnet configured for the forwarding rule. By default, if this field is empty, an ephemeral internal IP address will be automatically allocated from the IP range of the subnet or network configured for this forwarding rule.  An address can be specified either by a literal IP address or a URL reference to an existing Address resource. The following examples are all valid: \* 100.1.2.3 \* <https://www.googleapis.com/compute/v1/projects/project/regions/region/addresses/address> \* projects/project/regions/region/addresses/address \* regions/region/addresses/address \* global/addresses/address \* address . |
| **ip_protocol**  string | The IP protocol to which this rule applies. When the load balancing scheme is INTERNAL_SELF_MANAGED, only TCP is valid.  Some valid choices include: “TCP”, “UDP”, “ESP”, “AH”, “SCTP”, “ICMP” |
| **ip_version**  string | The IP Version that will be used by this global forwarding rule.  Some valid choices include: “IPV4”, “IPV6” |
| **load_balancing_scheme**  string | This signifies what the GlobalForwardingRule will be used for.  The value of INTERNAL_SELF_MANAGED means that this will be used for Internal Global HTTP(S) LB. The value of EXTERNAL means that this will be used for External Global Load Balancing (HTTP(S) LB, External TCP/UDP LB, SSL Proxy) NOTE: Currently global forwarding rules cannot be used for INTERNAL load balancing.  Some valid choices include: “EXTERNAL”, “INTERNAL_SELF_MANAGED”  Default: `"EXTERNAL"` |
| **metadata_filters**  list / elements=dictionary | Opaque filter criteria used by Loadbalancer to restrict routing configuration to a limited set xDS compliant clients. In their xDS requests to Loadbalancer, xDS clients present node metadata. If a match takes place, the relevant routing configuration is made available to those proxies.  For each metadataFilter in this list, if its filterMatchCriteria is set to MATCH_ANY, at least one of the filterLabels must match the corresponding label provided in the metadata. If its filterMatchCriteria is set to MATCH_ALL, then all of its filterLabels must match with corresponding labels in the provided metadata.  metadataFilters specified here can be overridden by those specified in the UrlMap that this ForwardingRule references.  metadataFilters only applies to Loadbalancers that have their loadBalancingScheme set to INTERNAL_SELF_MANAGED. |
| **filter_labels**  list / elements=dictionary / required | The list of label value pairs that must match labels in the provided metadata based on filterMatchCriteria This list must not be empty and can have at the most 64 entries. |
| **name**  string / required | Name of the metadata label. The length must be between 1 and 1024 characters, inclusive. |
| **value**  string / required | The value that the label must match. The value has a maximum length of 1024 characters. |
| **filter_match_criteria**  string / required | Specifies how individual filterLabel matches within the list of filterLabels contribute towards the overall metadataFilter match.  MATCH_ANY - At least one of the filterLabels must have a matching label in the provided metadata.  MATCH_ALL - All filterLabels must have matching labels in the provided metadata.  Some valid choices include: “MATCH_ANY”, “MATCH_ALL” |
| **name**  string / required | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **network**  dictionary | This field is not used for external load balancing.  For INTERNAL_SELF_MANAGED load balancing, this field identifies the network that the load balanced IP should belong to for this global forwarding rule. If this field is not specified, the default network will be used.  This field represents a link to a Network resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_network task and then set this network field to “{{ name-of-resource }}” |
| **port_range**  string | This field is used along with the target field for TargetHttpProxy, TargetHttpsProxy, TargetSslProxy, TargetTcpProxy, TargetVpnGateway, TargetPool, TargetInstance.  Applicable only when IPProtocol is TCP, UDP, or SCTP, only packets addressed to ports in the specified range will be forwarded to target.  Forwarding rules with the same [IPAddress, IPProtocol] pair must have disjoint port ranges.  Some types of forwarding target have constraints on the acceptable ports: \* TargetHttpProxy: 80, 8080 \* TargetHttpsProxy: 443 \* TargetTcpProxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222 \* TargetSslProxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222 \* TargetVpnGateway: 500, 4500 . |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |
| **target**  string / required | The URL of the target resource to receive the matched traffic.  The forwarded traffic must be of a type appropriate to the target object.  For INTERNAL_SELF_MANAGED load balancing, only HTTP and HTTPS targets are valid. |

## [Examples](gcp_compute_global_forwarding_rule_module.md#id4)

```yaml+jinja
- name: create a global address
  google.cloud.gcp_compute_global_address:
    name: globaladdress-globalforwardingrule
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: globaladdress

- name: create a instance group
  google.cloud.gcp_compute_instance_group:
    name: instancegroup-globalforwardingrule
    zone: us-central1-a
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: instancegroup

- name: create a HTTP health check
  google.cloud.gcp_compute_http_health_check:
    name: httphealthcheck-globalforwardingrule
    healthy_threshold: 10
    port: 8080
    timeout_sec: 2
    unhealthy_threshold: 5
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: healthcheck

- name: create a backend service
  google.cloud.gcp_compute_backend_service:
    name: backendservice-globalforwardingrule
    backends:
    - group: "{{ instancegroup.selfLink }}"
    health_checks:
    - "{{ healthcheck.selfLink }}"
    enable_cdn: 'true'
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: backendservice

- name: create a URL map
  google.cloud.gcp_compute_url_map:
    name: urlmap-globalforwardingrule
    default_service: "{{ backendservice }}"
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: urlmap

- name: create a target HTTP proxy
  google.cloud.gcp_compute_target_http_proxy:
    name: targethttpproxy-globalforwardingrule
    url_map: "{{ urlmap }}"
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: httpproxy

- name: create a global forwarding rule
  google.cloud.gcp_compute_global_forwarding_rule:
    name: test_object
    ip_address: "{{ globaladdress.address }}"
    ip_protocol: TCP
    port_range: 80-80
    target: "{{ httpproxy.selfLink }}"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_global_forwarding_rule_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  Returned: success |
| **description**  string | An optional description of this resource. Provide this property when you create the resource.  Returned: success |
| **id**  integer | The unique identifier for the resource.  Returned: success |
| **IPAddress**  string | The IP address that this forwarding rule is serving on behalf of.  Addresses are restricted based on the forwarding rule’s load balancing scheme (EXTERNAL or INTERNAL) and scope (global or regional).  When the load balancing scheme is EXTERNAL, for global forwarding rules, the address must be a global IP, and for regional forwarding rules, the address must live in the same region as the forwarding rule. If this field is empty, an ephemeral IPv4 address from the same scope (global or regional) will be assigned. A regional forwarding rule supports IPv4 only. A global forwarding rule supports either IPv4 or IPv6.  When the load balancing scheme is INTERNAL, this can only be an RFC 1918 IP address belonging to the network/subnet configured for the forwarding rule. By default, if this field is empty, an ephemeral internal IP address will be automatically allocated from the IP range of the subnet or network configured for this forwarding rule.  An address can be specified either by a literal IP address or a URL reference to an existing Address resource. The following examples are all valid: \* 100.1.2.3 \* <https://www.googleapis.com/compute/v1/projects/project/regions/region/addresses/address> \* projects/project/regions/region/addresses/address \* regions/region/addresses/address \* global/addresses/address \* address .  Returned: success |
| **IPProtocol**  string | The IP protocol to which this rule applies. When the load balancing scheme is INTERNAL_SELF_MANAGED, only TCP is valid.  Returned: success |
| **ipVersion**  string | The IP Version that will be used by this global forwarding rule.  Returned: success |
| **loadBalancingScheme**  string | This signifies what the GlobalForwardingRule will be used for.  The value of INTERNAL_SELF_MANAGED means that this will be used for Internal Global HTTP(S) LB. The value of EXTERNAL means that this will be used for External Global Load Balancing (HTTP(S) LB, External TCP/UDP LB, SSL Proxy) NOTE: Currently global forwarding rules cannot be used for INTERNAL load balancing.  Returned: success |
| **metadataFilters**  complex | Opaque filter criteria used by Loadbalancer to restrict routing configuration to a limited set xDS compliant clients. In their xDS requests to Loadbalancer, xDS clients present node metadata. If a match takes place, the relevant routing configuration is made available to those proxies.  For each metadataFilter in this list, if its filterMatchCriteria is set to MATCH_ANY, at least one of the filterLabels must match the corresponding label provided in the metadata. If its filterMatchCriteria is set to MATCH_ALL, then all of its filterLabels must match with corresponding labels in the provided metadata.  metadataFilters specified here can be overridden by those specified in the UrlMap that this ForwardingRule references.  metadataFilters only applies to Loadbalancers that have their loadBalancingScheme set to INTERNAL_SELF_MANAGED.  Returned: success |
| **filterLabels**  complex | The list of label value pairs that must match labels in the provided metadata based on filterMatchCriteria This list must not be empty and can have at the most 64 entries.  Returned: success |
| **name**  string | Name of the metadata label. The length must be between 1 and 1024 characters, inclusive.  Returned: success |
| **value**  string | The value that the label must match. The value has a maximum length of 1024 characters.  Returned: success |
| **filterMatchCriteria**  string | Specifies how individual filterLabel matches within the list of filterLabels contribute towards the overall metadataFilter match.  MATCH_ANY - At least one of the filterLabels must have a matching label in the provided metadata.  MATCH_ALL - All filterLabels must have matching labels in the provided metadata.  Returned: success |
| **name**  string | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  Returned: success |
| **network**  dictionary | This field is not used for external load balancing.  For INTERNAL_SELF_MANAGED load balancing, this field identifies the network that the load balanced IP should belong to for this global forwarding rule. If this field is not specified, the default network will be used.  Returned: success |
| **portRange**  string | This field is used along with the target field for TargetHttpProxy, TargetHttpsProxy, TargetSslProxy, TargetTcpProxy, TargetVpnGateway, TargetPool, TargetInstance.  Applicable only when IPProtocol is TCP, UDP, or SCTP, only packets addressed to ports in the specified range will be forwarded to target.  Forwarding rules with the same [IPAddress, IPProtocol] pair must have disjoint port ranges.  Some types of forwarding target have constraints on the acceptable ports: \* TargetHttpProxy: 80, 8080 \* TargetHttpsProxy: 443 \* TargetTcpProxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222 \* TargetSslProxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222 \* TargetVpnGateway: 500, 4500 .  Returned: success |
| **target**  string | The URL of the target resource to receive the matched traffic.  The forwarded traffic must be of a type appropriate to the target object.  For INTERNAL_SELF_MANAGED load balancing, only HTTP and HTTPS targets are valid.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
