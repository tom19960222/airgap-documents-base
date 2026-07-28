---
collection: ansible
version: "6"
title: "openstack.cloud.security_group_rule module – Add/Delete rule from an existing security group"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/security_group_rule_module.html
fetched_at: 2026-07-28T00:17:04+00:00
---
# openstack.cloud.security_group_rule module – Add/Delete rule from an existing security group

> **Note:**
>
> This module is part of the [openstack.cloud collection](https://galaxy.ansible.com/openstack/cloud) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openstack.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](security_group_rule_module.md#ansible-collections-openstack-cloud-security-group-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.security_group_rule`.

- [Synopsis](security_group_rule_module.md#synopsis)
- [Requirements](security_group_rule_module.md#requirements)
- [Parameters](security_group_rule_module.md#parameters)
- [Notes](security_group_rule_module.md#notes)
- [Examples](security_group_rule_module.md#examples)
- [Return Values](security_group_rule_module.md#return-values)

## [Synopsis](security_group_rule_module.md#id1)

- Add or Remove rule from an existing security group

## [Requirements](security_group_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](security_group_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **description**  string | Description of the rule. |
| **direction**  string | The direction in which the security group rule is applied. Not all providers support egress.  Choices:   - `"egress"` - `"ingress"` ← (default) |
| **ethertype**  string | Must be IPv4 or IPv6, and addresses represented in CIDR must match the ingress or egress rules. Not all providers support IPv6.  Choices:   - `"IPv4"` ← (default) - `"IPv6"` |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **port_range_max**  integer | Ending port |
| **port_range_min**  integer | Starting port |
| **project**  string | Unique name or ID of the project. |
| **protocol**  string | IP protocols ANY TCP UDP ICMP and others, also number in range 0-255 |
| **region_name**  string | Name of the region. |
| **remote_group**  string | Name or ID of the Security group to link (exclusive with remote_ip_prefix) |
| **remote_ip_prefix**  string | Source IP address(es) in CIDR notation (exclusive with remote_group) |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **security_group**  string / required | Name or ID of the security group |
| **state**  string | Should the resource be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](security_group_rule_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](security_group_rule_module.md#id5)

```yaml+jinja
# Create a security group rule
- openstack.cloud.security_group_rule:
    cloud: mordred
    security_group: foo
    protocol: tcp
    port_range_min: 80
    port_range_max: 80
    remote_ip_prefix: 0.0.0.0/0

# Create a security group rule for ping
- openstack.cloud.security_group_rule:
    cloud: mordred
    security_group: foo
    protocol: icmp
    remote_ip_prefix: 0.0.0.0/0

# Another way to create the ping rule
- openstack.cloud.security_group_rule:
    cloud: mordred
    security_group: foo
    protocol: icmp
    port_range_min: -1
    port_range_max: -1
    remote_ip_prefix: 0.0.0.0/0

# Create a TCP rule covering all ports
- openstack.cloud.security_group_rule:
    cloud: mordred
    security_group: foo
    protocol: tcp
    port_range_min: 1
    port_range_max: 65535
    remote_ip_prefix: 0.0.0.0/0

# Another way to create the TCP rule above (defaults to all ports)
- openstack.cloud.security_group_rule:
    cloud: mordred
    security_group: foo
    protocol: tcp
    remote_ip_prefix: 0.0.0.0/0

# Create a rule for VRRP with numbered protocol 112
- openstack.cloud.security_group_rule:
    security_group: loadbalancer_sg
    protocol: 112
    remote_group: loadbalancer-node_sg

# Create a security group rule for a given project
- openstack.cloud.security_group_rule:
    cloud: mordred
    security_group: foo
    protocol: icmp
    remote_ip_prefix: 0.0.0.0/0
    project: myproj

# Remove the default created egress rule for IPv4
- openstack.cloud.security_group_rule:
   cloud: mordred
   security_group: foo
   protocol: any
   remote_ip_prefix: 0.0.0.0/0
```

## [Return Values](security_group_rule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **direction**  string | The direction in which the security group rule is applied.  Returned: state == present  Sample: `"egress"` |
| **ethertype**  string | One of IPv4 or IPv6.  Returned: state == present  Sample: `"IPv4"` |
| **id**  string | Unique rule UUID.  Returned: state == present |
| **port_range_max**  integer | The maximum port number in the range that is matched by the security group rule.  Returned: state == present  Sample: `8000` |
| **port_range_min**  integer | The minimum port number in the range that is matched by the security group rule.  Returned: state == present  Sample: `8000` |
| **protocol**  string | The protocol that is matched by the security group rule.  Returned: state == present  Sample: `"tcp"` |
| **remote_ip_prefix**  string | The remote IP prefix to be associated with this security group rule.  Returned: state == present  Sample: `"0.0.0.0/0"` |
| **security_group_id**  string | The security group ID to associate with this security group rule.  Returned: state == present |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
