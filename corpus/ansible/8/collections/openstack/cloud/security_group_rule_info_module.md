---
collection: ansible
version: "8"
title: "openstack.cloud.security_group_rule_info module – Fetch OpenStack network (Neutron) security group rules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/security_group_rule_info_module.html
fetched_at: 2026-07-28T02:48:45+00:00
---
# openstack.cloud.security_group_rule_info module – Fetch OpenStack network (Neutron) security group rules

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
> see [Requirements](security_group_rule_info_module.md#ansible-collections-openstack-cloud-security-group-rule-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.security_group_rule_info`.

- [Synopsis](security_group_rule_info_module.md#synopsis)
- [Requirements](security_group_rule_info_module.md#requirements)
- [Parameters](security_group_rule_info_module.md#parameters)
- [Notes](security_group_rule_info_module.md#notes)
- [Examples](security_group_rule_info_module.md#examples)
- [Return Values](security_group_rule_info_module.md#return-values)

## [Synopsis](security_group_rule_info_module.md#id1)

- Fetch security group rules from OpenStack network (Neutron) API.

## [Requirements](security_group_rule_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](security_group_rule_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **description**  string | Filter the list result by the human-readable description of the resource. |
| **direction**  string | Filter the security group rule list result by the direction in which the security group rule is applied.  **Choices:**   - `"egress"` - `"ingress"` |
| **ether_type**  aliases: ethertype  string | Filter the security group rule list result by the ether_type of network traffic. The value must be IPv4 or IPv6.  **Choices:**   - `"IPv4"` - `"IPv6"` |
| **id**  aliases: rule  string | Filter the list result by the ID of the security group rule. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **port_range_max**  integer | Ending port |
| **port_range_min**  integer | Starting port |
| **project**  string | Unique name or ID of the project. |
| **protocol**  string | Filter the security group rule list result by the IP protocol. |
| **region_name**  string | Name of the region. |
| **remote_group**  string | Filter the security group rule list result by the name or ID of the remote group that associates with this security group rule. |
| **remote_ip_prefix**  string | Source IP address(es) in CIDR notation (exclusive with remote_group) |
| **revision_number**  integer | Filter the list result by the revision number of the resource. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **security_group**  string | Name or ID of the security group |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](security_group_rule_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](security_group_rule_info_module.md#id5)

```yaml+jinja
- name: Fetch all security group rules
  openstack.cloud.security_group_rule_info:
    cloud: devstack

- name: Filter security group rules for port 80 and name
  openstack.cloud.security_group_rule_info:
    cloud: devstack
    security_group: foo
    protocol: tcp
    port_range_min: 80
    port_range_max: 80
    remote_ip_prefix: 0.0.0.0/0

- name: Filter for ICMP rules
  openstack.cloud.security_group_rule_info:
    cloud: devstack
    protocol: icmp
```

## [Return Values](security_group_rule_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **security_group_rules**  list / elements=dictionary | List of dictionaries describing security group rules.  **Returned:** always |
| **created_at**  string | Timestamp when the security group rule was created.  **Returned:** success |
| **description**  string | Human-readable description of the resource.  **Returned:** success  **Sample:** `"My description."` |
| **direction**  string | The direction in which the security group rule is applied.  **Returned:** success  **Sample:** `"egress"` |
| **ether_type**  string | One of IPv4 or IPv6.  **Returned:** success  **Sample:** `"IPv4"` |
| **id**  string | Unique rule UUID.  **Returned:** success |
| **name**  string | Name of the resource.  **Returned:** success |
| **port_range_max**  integer | The maximum port number in the range that is matched by the security group rule.  **Returned:** success  **Sample:** `8000` |
| **port_range_min**  integer | The minimum port number in the range that is matched by the security group rule.  **Returned:** success  **Sample:** `8000` |
| **project_id**  string | The ID of the project.  **Returned:** success  **Sample:** `"e4f50856753b4dc6afee5fa6b9b6c550"` |
| **protocol**  string | The protocol that is matched by the security group rule.  **Returned:** success  **Sample:** `"tcp"` |
| **remote_address_group_id**  string | The remote address group ID to be associated with this security group rule.  **Returned:** success |
| **remote_group_id**  string | The remote security group ID to be associated with this security group rule.  **Returned:** success |
| **remote_ip_prefix**  string | The remote IP prefix to be associated with this security group rule.  **Returned:** success |
| **revision_number**  string | The remote IP prefix to be associated with this security group rule.  **Returned:** success  **Sample:** `"0.0.0.0/0"` |
| **security_group_id**  string | The security group ID to associate with this security group rule.  **Returned:** success  **Sample:** `"729b9660-a20a-41fe-bae6-ed8fa7f69123"` |
| **tags**  string | The security group ID to associate with this security group rule.  **Returned:** success  **Sample:** `"729b9660-a20a-41fe-bae6-ed8fa7f69123"` |
| **tenant_id**  string | The ID of the project. Deprecated.  **Returned:** success  **Sample:** `"e4f50856753b4dc6afee5fa6b9b6c550"` |
| **updated_at**  string | Time at which the resource has been updated (in UTC ISO8601 format).  **Returned:** success  **Sample:** `"2018-03-19T19:16:56Z"` |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
