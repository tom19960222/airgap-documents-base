---
collection: ansible
version: "8"
title: "openstack.cloud.security_group module – Manage Neutron security groups of an OpenStack cloud."
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/security_group_module.html
fetched_at: 2026-07-28T02:48:40+00:00
---
# openstack.cloud.security_group module – Manage Neutron security groups of an OpenStack cloud.

> **Note:**
>
> This module is part of the [openstack.cloud collection](https://galaxy.ansible.com/ui/repo/published/openstack/cloud/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openstack.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](security_group_module.md#ansible-collections-openstack-cloud-security-group-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.security_group`.

- [Synopsis](security_group_module.md#synopsis)
- [Requirements](security_group_module.md#requirements)
- [Parameters](security_group_module.md#parameters)
- [Notes](security_group_module.md#notes)
- [Examples](security_group_module.md#examples)
- [Return Values](security_group_module.md#return-values)

## [Synopsis](security_group_module.md#id1)

- Add or remove Neutron security groups to/from an OpenStack cloud.

## [Requirements](security_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](security_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **description**  string | Long description of the purpose of the security group. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  string / required | Name that has to be given to the security group. This module requires that security group names be unique. |
| **project**  string | Unique name or ID of the project. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **security_group_rules**  list / elements=dictionary | List of security group rules.  When *security_group_rules* is not defined, Neutron might create this security group with a default set of rules.  Security group rules which are listed in *security_group_rules* but not defined in this security group will be created.  When *security_group_rules* is not set, existing security group rules which are not listed in *security_group_rules* will be deleted.  When updating a security group, one has to explicitly list rules from Neutron’s defaults in *security_group_rules* if those rules should be kept. Rules which are not listed in *security_group_rules* will be deleted. |
| **description**  string | Description of the security group rule. |
| **direction**  string | The direction in which the security group rule is applied.  Not all providers support `egress`.  **Choices:**   - `"egress"` - `"ingress"` ← (default) |
| **ether_type**  string | Must be IPv4 or IPv6, and addresses represented in CIDR must match the ingress or egress rules. Not all providers support IPv6.  **Choices:**   - `"IPv4"` ← (default) - `"IPv6"` |
| **port_range_max**  integer | The maximum port number in the range that is matched by the security group rule.  If the protocol is TCP, UDP, DCCP, SCTP or UDP-Lite this value must be greater than or equal to the *port_range_min* attribute value.  If the protocol is ICMP, this value must be an ICMP code. |
| **port_range_min**  integer | The minimum port number in the range that is matched by the security group rule.  If the protocol is TCP, UDP, DCCP, SCTP or UDP-Lite this value must be less than or equal to the port_range_max attribute value.  If the protocol is ICMP, this value must be an ICMP type. |
| **protocol**  string | The IP protocol can be represented by a string, an integer, or null.  Valid string or integer values are `any` or `0`, `ah` or `51`, `dccp` or `33`, `egp` or `8`, `esp` or `50`, `gre` or `47`, `icmp` or `1`, `icmpv6` or `58`, `igmp` or `2`, `ipip` or `4`, `ipv6-encap` or `41`, `ipv6-frag` or `44`, `ipv6-icmp` or `58`, `ipv6-nonxt` or `59`, `ipv6-opts` or `60`, `ipv6-route` or `43`, `ospf` or `89`, `pgm` or `113`, `rsvp` or `46`, `sctp` or `132`, `tcp` or `6`, `udp` or `17`, `udplite` or `136`, `vrrp` or `112`.  Additionally, any integer value between `[0-255]` is also valid.  The string any (or integer 0) means all IP protocols.  See the constants in neutron_lib.constants for the most up-to-date list of supported strings. |
| **remote_group**  string | Name or ID of the security group to link.  Mutually exclusive with *remote_ip_prefix*. |
| **remote_ip_prefix**  string | Source IP address(es) in CIDR notation.  When a netmask such as `/32` is missing from *remote_ip_prefix*, then this module will fail on updates with OpenStack error message `Security group rule already exists.`.  Mutually exclusive with *remote_group*. |
| **state**  string | Should the resource be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **stateful**  boolean | Should the resource be stateful or stateless.  **Choices:**   - `false` - `true` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](security_group_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](security_group_module.md#id5)

```yaml+jinja
- name: Create a security group
  openstack.cloud.security_group:
    cloud: mordred
    state: present
    name: foo
    description: security group for foo servers

- name: Create a stateless security group
  openstack.cloud.security_group:
    cloud: mordred
    state: present
    stateful: false
    name: foo
    description: stateless security group for foo servers

- name: Update the existing 'foo' security group description
  openstack.cloud.security_group:
    cloud: mordred
    state: present
    name: foo
    description: updated description for the foo security group

- name: Create a security group for a given project
  openstack.cloud.security_group:
    cloud: mordred
    state: present
    name: foo
    project: myproj

- name: Create (or update) a security group with security group rules
  openstack.cloud.security_group:
    cloud: mordred
    state: present
    name: foo
    security_group_rules:
      - ether_type: IPv6
        direction: egress
      - ether_type: IPv4
        direction: egress

- name: Create (or update) security group without security group rules
  openstack.cloud.security_group:
    cloud: mordred
    state: present
    name: foo
    security_group_rules: []
```

## [Return Values](security_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **security_group**  dictionary | Dictionary describing the security group.  **Returned:** On success when *state* is `present`. |
| **created_at**  string | Creation time of the security group  **Returned:** success  **Sample:** `"yyyy-mm-dd hh:mm:ss"` |
| **description**  string | Description of the security group  **Returned:** success  **Sample:** `"My security group"` |
| **id**  string | ID of the security group  **Returned:** success  **Sample:** `"d90e55ba-23bd-4d97-b722-8cb6fb485d69"` |
| **name**  string | Name of the security group.  **Returned:** success  **Sample:** `"my-sg"` |
| **project_id**  string | Project ID where the security group is located in.  **Returned:** success  **Sample:** `"25d24fc8-d019-4a34-9fff-0a09fde6a567"` |
| **revision_number**  integer | The revision number of the resource.  **Returned:** success |
| **security_group_rules**  list / elements=string | Specifies the security group rule list  **Returned:** success  **Sample:** `[{"description": null, "direction": "ingress", "ethertype": "IPv4", "id": "d90e55ba-23bd-4d97-b722-8cb6fb485d69", "port_range_max": null, "port_range_min": null, "protocol": null, "remote_group_id": "0431c9c5-1660-42e0-8a00-134bec7f03e2", "remote_ip_prefix": null, "security_group_id": "0431c9c5-1660-42e0-8a00-134bec7f03e2", "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c"}, {"description": null, "direction": "egress", "ethertype": "IPv4", "id": "aecff4d4-9ce9-489c-86a3-803aedec65f7", "port_range_max": null, "port_range_min": null, "protocol": null, "remote_group_id": null, "remote_ip_prefix": null, "security_group_id": "0431c9c5-1660-42e0-8a00-134bec7f03e2", "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c"}]` |
| **stateful**  boolean | Indicates if the security group is stateful or stateless.  **Returned:** success |
| **tags**  list / elements=string | The list of tags on the resource.  **Returned:** success |
| **tenant_id**  string | Tenant ID where the security group is located in. Deprecated  **Returned:** success  **Sample:** `"25d24fc8-d019-4a34-9fff-0a09fde6a567"` |
| **updated_at**  string | Update time of the security group  **Returned:** success  **Sample:** `"yyyy-mm-dd hh:mm:ss"` |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
