---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_firewall module – Creates a GCP Firewall"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_firewall_module.html
fetched_at: 2026-07-28T02:32:00+00:00
---
# google.cloud.gcp_compute_firewall module – Creates a GCP Firewall

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
> see [Requirements](gcp_compute_firewall_module.md#ansible-collections-google-cloud-gcp-compute-firewall-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_firewall`.

- [Synopsis](gcp_compute_firewall_module.md#synopsis)
- [Requirements](gcp_compute_firewall_module.md#requirements)
- [Parameters](gcp_compute_firewall_module.md#parameters)
- [Notes](gcp_compute_firewall_module.md#notes)
- [Examples](gcp_compute_firewall_module.md#examples)
- [Return Values](gcp_compute_firewall_module.md#return-values)

## [Synopsis](gcp_compute_firewall_module.md#id1)

- Each network has its own firewall controlling access to and from the instances.
- All traffic to instances, even from other instances, is blocked by the firewall unless firewall rules are created to allow it.
- The default network has automatically created firewall rules that are shown in default firewall rules. No manually created network has automatically created firewall rules except for a default “allow” rule for outgoing traffic and a default “deny” for incoming traffic. For all networks except the default network, you must create any firewall rules you need.

## [Requirements](gcp_compute_firewall_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_firewall_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **allowed**  list / elements=dictionary | The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a permitted connection. |
| **ip_protocol**  string / required | The IP protocol to which this rule applies. The protocol type is required when creating a firewall rule. This value can either be one of the following well known protocol strings (tcp, udp, icmp, esp, ah, sctp, ipip, all), or the IP protocol number. |
| **ports**  list / elements=string | An optional list of ports to which this rule applies. This field is only applicable for UDP or TCP protocol. Each entry must be either an integer or a range. If not specified, this rule applies to connections through any port.  Example inputs include: [“22”], [“80”,”443”], and [“12345-12349”]. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **denied**  list / elements=dictionary | The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a denied connection. |
| **ip_protocol**  string / required | The IP protocol to which this rule applies. The protocol type is required when creating a firewall rule. This value can either be one of the following well known protocol strings (tcp, udp, icmp, esp, ah, sctp, ipip, all), or the IP protocol number. |
| **ports**  list / elements=string | An optional list of ports to which this rule applies. This field is only applicable for UDP or TCP protocol. Each entry must be either an integer or a range. If not specified, this rule applies to connections through any port.  Example inputs include: [“22”], [“80”,”443”], and [“12345-12349”]. |
| **description**  string | An optional description of this resource. Provide this property when you create the resource. |
| **destination_ranges**  list / elements=string | If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported. |
| **direction**  string | Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify sourceRanges OR sourceTags.  Some valid choices include: “INGRESS”, “EGRESS” |
| **disabled**  boolean | Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true, the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall rule will be enabled.  **Choices:**   - `false` - `true` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **log_config**  dictionary | This field denotes the logging options for a particular firewall rule.  If logging is enabled, logs will be exported to Cloud Logging. |
| **enable**  boolean | This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be exported to Stackdriver.  **Choices:**   - `false` - `true` |
| **metadata**  string | This field denotes whether to include or exclude metadata for firewall logs.  Some valid choices include: “EXCLUDE_ALL_METADATA”, “INCLUDE_ALL_METADATA” |
| **name**  string / required | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **network**  dictionary | URL of the network resource for this firewall rule. If not specified when creating a firewall rule, the default network is used: global/networks/default If you choose to specify this property, you can specify the network as a full or partial URL. For example, the following are all valid URLs: <https://www.googleapis.com/compute/v1/projects/myproject/global/> networks/my-network projects/myproject/global/networks/my-network global/networks/default .  This field represents a link to a Network resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_network task and then set this network field to “{{ name-of-resource }}”  **Default:** `{"selfLink": "global/networks/default"}` |
| **priority**  integer | Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is 1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence (eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW rules having equal priority.  **Default:** `1000` |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **source_ranges**  list / elements=string | If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges. These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to apply. Only IPv4 is supported. |
| **source_service_accounts**  list / elements=string | If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a service account in this list. Source service accounts cannot be used to control traffic to an instance’s external IP address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time as sourceTags or targetTags. |
| **source_tags**  list / elements=string | If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in source tags. Source tags cannot be used to control traffic to an instance’s external IP address. Because tags are associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to apply. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **target_service_accounts**  list / elements=string | A list of service accounts indicating sets of instances located in the network that may make network connections as specified in allowed[].  targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network. |
| **target_tags**  list / elements=string | A list of instance tags indicating sets of instances located in the network that may make network connections as specified in allowed[].  If no targetTags are specified, the firewall rule applies to all instances on the specified network. |

## [Notes](gcp_compute_firewall_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/v1/firewalls>
> - Official Documentation: <https://cloud.google.com/vpc/docs/firewalls>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_firewall_module.md#id5)

```yaml+jinja
- name: create a firewall
  google.cloud.gcp_compute_firewall:
    name: test_object
    allowed:
    - ip_protocol: tcp
      ports:
      - '22'
    target_tags:
    - test-ssh-server
    - staging-ssh-server
    source_tags:
    - test-ssh-clients
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_firewall_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allowed**  complex | The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a permitted connection.  **Returned:** success |
| **ip_protocol**  string | The IP protocol to which this rule applies. The protocol type is required when creating a firewall rule. This value can either be one of the following well known protocol strings (tcp, udp, icmp, esp, ah, sctp, ipip, all), or the IP protocol number.  **Returned:** success |
| **ports**  list / elements=string | An optional list of ports to which this rule applies. This field is only applicable for UDP or TCP protocol. Each entry must be either an integer or a range. If not specified, this rule applies to connections through any port.  Example inputs include: [“22”], [“80”,”443”], and [“12345-12349”].  **Returned:** success |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **denied**  complex | The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a denied connection.  **Returned:** success |
| **ip_protocol**  string | The IP protocol to which this rule applies. The protocol type is required when creating a firewall rule. This value can either be one of the following well known protocol strings (tcp, udp, icmp, esp, ah, sctp, ipip, all), or the IP protocol number.  **Returned:** success |
| **ports**  list / elements=string | An optional list of ports to which this rule applies. This field is only applicable for UDP or TCP protocol. Each entry must be either an integer or a range. If not specified, this rule applies to connections through any port.  Example inputs include: [“22”], [“80”,”443”], and [“12345-12349”].  **Returned:** success |
| **description**  string | An optional description of this resource. Provide this property when you create the resource.  **Returned:** success |
| **destinationRanges**  list / elements=string | If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported.  **Returned:** success |
| **direction**  string | Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify sourceRanges OR sourceTags.  **Returned:** success |
| **disabled**  boolean | Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true, the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall rule will be enabled.  **Returned:** success |
| **id**  integer | The unique identifier for the resource.  **Returned:** success |
| **logConfig**  complex | This field denotes the logging options for a particular firewall rule.  If logging is enabled, logs will be exported to Cloud Logging.  **Returned:** success |
| **enable**  boolean | This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be exported to Stackdriver.  **Returned:** success |
| **metadata**  string | This field denotes whether to include or exclude metadata for firewall logs.  **Returned:** success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **network**  dictionary | URL of the network resource for this firewall rule. If not specified when creating a firewall rule, the default network is used: global/networks/default If you choose to specify this property, you can specify the network as a full or partial URL. For example, the following are all valid URLs: <https://www.googleapis.com/compute/v1/projects/myproject/global/> networks/my-network projects/myproject/global/networks/my-network global/networks/default .  **Returned:** success |
| **priority**  integer | Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is 1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence (eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW rules having equal priority.  **Returned:** success |
| **sourceRanges**  list / elements=string | If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges. These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to apply. Only IPv4 is supported.  **Returned:** success |
| **sourceServiceAccounts**  list / elements=string | If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a service account in this list. Source service accounts cannot be used to control traffic to an instance’s external IP address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time as sourceTags or targetTags.  **Returned:** success |
| **sourceTags**  list / elements=string | If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in source tags. Source tags cannot be used to control traffic to an instance’s external IP address. Because tags are associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to apply.  **Returned:** success |
| **targetServiceAccounts**  list / elements=string | A list of service accounts indicating sets of instances located in the network that may make network connections as specified in allowed[].  targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network.  **Returned:** success |
| **targetTags**  list / elements=string | A list of instance tags indicating sets of instances located in the network that may make network connections as specified in allowed[].  If no targetTags are specified, the firewall rule applies to all instances on the specified network.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
