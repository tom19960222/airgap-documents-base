---
collection: ansible
version: "8"
title: "openstack.cloud.lb_pool module – Manage load-balancer pool in a OpenStack cloud."
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/lb_pool_module.html
fetched_at: 2026-07-28T02:48:14+00:00
---
# openstack.cloud.lb_pool module – Manage load-balancer pool in a OpenStack cloud.

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

- Add, update or remove load-balancer pool from OpenStack cloud.

## [Requirements](lb_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](lb_pool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **description**  string | A human-readable description for the load-balancer pool. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **lb_algorithm**  string | The load balancing algorithm for the pool.  For example, *lb_algorithm* could be `LEAST_CONNECTIONS`, `ROUND_ROBIN`, `SOURCE_IP` or `SOURCE_IP_PORT`.  **Default:** `"ROUND_ROBIN"` |
| **listener**  string | The name or id of the listener that this pool belongs to.  Either *listener* or *loadbalancer* must be specified for pool creation.  This attribute cannot be updated. |
| **loadbalancer**  string | The name or id of the load balancer that this pool belongs to.  Either *listener* or *loadbalancer* must be specified for pool creation.  This attribute cannot be updated. |
| **name**  string / required | Name that has to be given to the pool.  This attribute cannot be updated. |
| **protocol**  string | The protocol for the pool.  For example, *protocol* could be `HTTP`, `HTTPS`, `PROXY`, `PROXYV2`, `SCTP`, `TCP` and `UDP`.  This attribute cannot be updated.  **Default:** `"HTTP"` |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Should the resource be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](lb_pool_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](lb_pool_module.md#id5)

```yaml+jinja
- name: Create a load-balander pool
  openstack.cloud.lb_pool:
    cloud: mycloud
    lb_algorithm: ROUND_ROBIN
    loadbalancer: test-loadbalancer
    name: test-pool
    protocol: HTTP
    state: present

- name: Delete a load-balander pool
  openstack.cloud.lb_pool:
    cloud: mycloud
    name: test-pool
    state: absent
```

## [Return Values](lb_pool_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **pool**  dictionary | Dictionary describing the load-balancer pool.  **Returned:** On success when *state* is `present`. |
| **alpn_protocols**  list / elements=string | List of ALPN protocols.  **Returned:** success |
| **created_at**  string | Timestamp when the pool was created.  **Returned:** success |
| **description**  string | The pool description.  **Returned:** success |
| **health_monitor_id**  string | Health Monitor ID.  **Returned:** success |
| **id**  string | Unique UUID.  **Returned:** success |
| **is_admin_state_up**  boolean | The administrative state of the pool.  **Returned:** success |
| **lb_algorithm**  string | The load balancing algorithm for the pool.  **Returned:** success |
| **listener_id**  string | The listener ID the pool belongs to.  **Returned:** success |
| **listeners**  list / elements=string | A list of listener IDs.  **Returned:** success |
| **loadbalancer_id**  string | The load balancer ID the pool belongs to. This field is set when the pool does not belong to any listener in the load balancer.  **Returned:** success |
| **loadbalancers**  list / elements=string | A list of load balancer IDs.  **Returned:** success |
| **members**  list / elements=string | A list of member IDs.  **Returned:** success |
| **name**  string | Name given to the pool.  **Returned:** success |
| **operating_status**  string | The operating status of the pool.  **Returned:** success |
| **project_id**  string | The ID of the project.  **Returned:** success |
| **protocol**  string | The protocol for the pool.  **Returned:** success |
| **provisioning_status**  string | The provisioning status of the pool.  **Returned:** success |
| **session_persistence**  dictionary | A JSON object specifying the session persistence for the pool.  **Returned:** success |
| **tags**  list / elements=string | A list of associated tags.  **Returned:** success |
| **tls_ciphers**  string | Stores a string of cipher strings in OpenSSL format.  **Returned:** success |
| **tls_enabled**  boolean | Use TLS for connections to backend member servers.  **Returned:** success |
| **tls_versions**  list / elements=string | A list of TLS protocol versions to be used in by the pool.  **Returned:** success |
| **updated_at**  string | Timestamp when the pool was updated.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
