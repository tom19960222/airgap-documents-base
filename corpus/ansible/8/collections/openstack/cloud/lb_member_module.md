---
collection: ansible
version: "8"
title: "openstack.cloud.lb_member module – Manage members in a OpenStack load-balancer pool"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/lb_member_module.html
fetched_at: 2026-07-28T02:48:11+00:00
---
# openstack.cloud.lb_member module – Manage members in a OpenStack load-balancer pool

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

- Add, update or remove member from OpenStack load-balancer pool.

## [Requirements](lb_member_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](lb_member_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string | The IP address of the member.  Required when *state* is `present`.  This attribute cannot be updated. |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **monitor_address**  string | IP address used to monitor this member. |
| **monitor_port**  integer | Port used to monitor this member. |
| **name**  string / required | Name that has to be given to the member. |
| **pool**  string / required | The name or id of the pool that this member belongs to.  This attribute cannot be updated. |
| **protocol_port**  integer | The protocol port number for the member.  Required when *state* is `present`.  This attribute cannot be updated. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Should the resource be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnet_id**  string | The subnet ID the member service is accessible from.  This attribute cannot be updated. |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |
| **weight**  integer | The weight of a member determines the portion of requests or connections it services compared to the other members of the pool.  For example, a member with a weight of 10 receives five times as many requests as a member with a weight of 2. A value of 0 means the member does not receive new connections but continues to service existing connections. A valid value is from 0 to 256.  Octavia’s default for *weight* is `1`. |

## [Notes](lb_member_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](lb_member_module.md#id5)

```yaml+jinja
- name: Create member in a load-balancer pool
  openstack.cloud.lb_member:
    address: 192.168.10.3
    cloud: mycloud
    name: test-member
    pool: test-pool
    protocol_port: 8080
    state: present

- name: Delete member from a load-balancer pool
  openstack.cloud.lb_member:
    cloud: mycloud
    name: test-member
    pool: test-pool
    state: absent
```

## [Return Values](lb_member_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **member**  dictionary | Dictionary describing the load-balancer pool member.  **Returned:** On success when *state* is `present`. |
| **address**  string | The IP address of the backend member server.  **Returned:** success |
| **backup**  boolean | A bool value that indicates whether the member is a backup or not. Backup members only receive traffic when all non-backup members are down.  **Returned:** success |
| **created_at**  string | Timestamp when the member was created.  **Returned:** success |
| **id**  string | Unique UUID.  **Returned:** success |
| **is_admin_state_up**  boolean | The administrative state of the member.  **Returned:** success |
| **monitor_address**  string | IP address used to monitor this member.  **Returned:** success |
| **monitor_port**  integer | Port used to monitor this member.  **Returned:** success |
| **name**  string | Name given to the member.  **Returned:** success |
| **operating_status**  string | Operating status of the member.  **Returned:** success |
| **project_id**  string | The ID of the project this member is associated with.  **Returned:** success |
| **protocol_port**  integer | The protocol port number for the member.  **Returned:** success |
| **provisioning_status**  string | The provisioning status of the member.  **Returned:** success |
| **subnet_id**  string | The subnet ID the member service is accessible from.  **Returned:** success |
| **tags**  list / elements=string | A list of associated tags.  **Returned:** success |
| **updated_at**  string | Timestamp when the member was last updated.  **Returned:** success |
| **weight**  integer | A positive integer value that indicates the relative portion of traffic that this member should receive from the pool. For example, a member with a weight of 10 receives five times as much traffic as a member with weight of 2.  **Returned:** success |
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
