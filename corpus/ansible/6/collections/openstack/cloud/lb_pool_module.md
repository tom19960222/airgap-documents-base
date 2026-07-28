---
collection: ansible
version: "6"
title: "openstack.cloud.lb_pool module – Add/Delete a pool in the load balancing service from OpenStack Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/lb_pool_module.html
fetched_at: 2026-07-28T00:16:50+00:00
---
# openstack.cloud.lb_pool module – Add/Delete a pool in the load balancing service from OpenStack Cloud

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
> see [Requirements](lb_pool_module.md#ansible-collections-openstack-cloud-lb-pool-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.lb_pool`.

- [Synopsis](lb_pool_module.md#synopsis)
- [Requirements](lb_pool_module.md#requirements)
- [Parameters](lb_pool_module.md#parameters)
- [Notes](lb_pool_module.md#notes)
- [Examples](lb_pool_module.md#examples)
- [Return Values](lb_pool_module.md#return-values)

## [Synopsis](lb_pool_module.md#id1)

- Add or Remove a pool from the OpenStack load-balancer service.

## [Requirements](lb_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](lb_pool_module.md#id3)

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
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **lb_algorithm**  string | The load balancing algorithm for the pool.  Choices:   - `"LEAST_CONNECTIONS"` - `"ROUND_ROBIN"` ← (default) - `"SOURCE_IP"` |
| **listener**  string | The name or id of the listener that this pool belongs to. Either loadbalancer or listener must be specified for pool creation. |
| **loadbalancer**  string | The name or id of the load balancer that this pool belongs to. Either loadbalancer or listener must be specified for pool creation. |
| **name**  string / required | Name that has to be given to the pool |
| **protocol**  string | The protocol for the pool.  Choices:   - `"HTTP"` ← (default) - `"HTTPS"` - `"PROXY"` - `"TCP"` - `"UDP"` |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Should the resource be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The amount of time the module should wait for the pool to get into ACTIVE state.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | If the module should wait for the pool to be ACTIVE.  Choices:   - `false` - `true` ← (default) |

## [Notes](lb_pool_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](lb_pool_module.md#id5)

```yaml+jinja
# Create a pool, wait for the pool to be active.
- openstack.cloud.lb_pool:
    cloud: mycloud
    endpoint_type: admin
    state: present
    name: test-pool
    loadbalancer: test-loadbalancer
    protocol: HTTP
    lb_algorithm: ROUND_ROBIN

# Delete a pool
- openstack.cloud.lb_pool:
    cloud: mycloud
    endpoint_type: admin
    state: absent
    name: test-pool
```

## [Return Values](lb_pool_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | The pool UUID.  Returned: On success when *state* is ‘present’  Sample: `"39007a7e-ee4f-4d13-8283-b4da2e037c69"` |
| **listener**  complex | Dictionary describing the pool.  Returned: On success when *state* is ‘present’ |
| **description**  string | The pool description.  Returned: success  Sample: `"description"` |
| **id**  string | Unique UUID.  Returned: success  Sample: `"39007a7e-ee4f-4d13-8283-b4da2e037c69"` |
| **is_admin_state_up**  boolean | The administrative state of the pool.  Returned: success  Sample: `true` |
| **lb_algorithm**  string | The load balancing algorithm for the pool.  Returned: success  Sample: `"ROUND_ROBIN"` |
| **listener_id**  string | The listener ID the pool belongs to.  Returned: success  Sample: `"956aa716-9c2f-11e8-83b3-44a8422643a4"` |
| **listeners**  list / elements=string | A list of listener IDs.  Returned: success  Sample: `[{"id": "b32eef7e-d2a6-4ea4-a301-60a873f89b3b"}]` |
| **loadbalancer_id**  string | The load balancer ID the pool belongs to. This field is set when the pool doesn’t belong to any listener in the load balancer.  Returned: success  Sample: `"7c4be3f8-9c2f-11e8-83b3-44a8422643a4"` |
| **loadbalancers**  list / elements=string | A list of load balancer IDs.  Returned: success  Sample: `[{"id": "b32eef7e-d2a6-4ea4-a301-60a873f89b3b"}]` |
| **members**  list / elements=string | A list of member IDs.  Returned: success  Sample: `[{"id": "b32eef7e-d2a6-4ea4-a301-60a873f89b3b"}]` |
| **name**  string | Name given to the pool.  Returned: success  Sample: `"test"` |
| **operating_status**  string | The operating status of the pool.  Returned: success  Sample: `"ONLINE"` |
| **protocol**  string | The protocol for the pool.  Returned: success  Sample: `"HTTP"` |
| **provisioning_status**  string | The provisioning status of the pool.  Returned: success  Sample: `"ACTIVE"` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
