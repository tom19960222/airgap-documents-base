---
collection: ansible
version: "6"
title: "openstack.cloud.lb_member module – Add/Delete a member for a pool in load balancer from OpenStack Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/lb_member_module.html
fetched_at: 2026-07-28T00:16:49+00:00
---
# openstack.cloud.lb_member module – Add/Delete a member for a pool in load balancer from OpenStack Cloud

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
> see [Requirements](lb_member_module.md#ansible-collections-openstack-cloud-lb-member-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.lb_member`.

- [Synopsis](lb_member_module.md#synopsis)
- [Requirements](lb_member_module.md#requirements)
- [Parameters](lb_member_module.md#parameters)
- [Notes](lb_member_module.md#notes)
- [Examples](lb_member_module.md#examples)
- [Return Values](lb_member_module.md#return-values)

## [Synopsis](lb_member_module.md#id1)

- Add or Remove a member for a pool from the OpenStack load-balancer service.

## [Requirements](lb_member_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](lb_member_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string | The IP address of the member. |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **monitor_address**  string | IP address used to monitor this member |
| **monitor_port**  integer | Port used to monitor this member |
| **name**  string / required | Name that has to be given to the member |
| **pool**  string / required | The name or id of the pool that this member belongs to. |
| **protocol_port**  integer | The protocol port number for the member.  Default: `80` |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Should the resource be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnet_id**  string | The subnet ID the member service is accessible from. |
| **timeout**  integer | The amount of time the module should wait for the load balancer to get into ACTIVE state.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | If the module should wait for the load balancer to be ACTIVE.  Choices:   - `false` - `true` ← (default) |

## [Notes](lb_member_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](lb_member_module.md#id5)

```yaml+jinja
# Create a member, wait for the member to be created.
- openstack.cloud.lb_member:
    cloud: mycloud
    endpoint_type: admin
    state: present
    name: test-member
    pool: test-pool
    address: 192.168.10.3
    protocol_port: 8080

# Delete a listener
- openstack.cloud.lb_member:
    cloud: mycloud
    endpoint_type: admin
    state: absent
    name: test-member
    pool: test-pool
```

## [Return Values](lb_member_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | The member UUID.  Returned: On success when *state* is ‘present’  Sample: `"39007a7e-ee4f-4d13-8283-b4da2e037c69"` |
| **member**  complex | Dictionary describing the member.  Returned: On success when *state* is ‘present’ |
| **address**  string | The IP address of the backend member server.  Returned: success  Sample: `"192.168.2.10"` |
| **description**  string | The member description.  Returned: success  Sample: `"description"` |
| **id**  string | Unique UUID.  Returned: success  Sample: `"39007a7e-ee4f-4d13-8283-b4da2e037c69"` |
| **is_admin_state_up**  boolean | The administrative state of the member.  Returned: success  Sample: `true` |
| **name**  string | Name given to the member.  Returned: success  Sample: `"test"` |
| **operating_status**  string | The operating status of the member.  Returned: success  Sample: `"ONLINE"` |
| **protocol_port**  integer | The protocol port number for the member.  Returned: success  Sample: `80` |
| **provisioning_status**  string | The provisioning status of the member.  Returned: success  Sample: `"ACTIVE"` |
| **subnet_id**  string | The subnet ID the member service is accessible from.  Returned: success  Sample: `"489247fa-9c25-11e8-9679-00224d6b7bc1"` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
