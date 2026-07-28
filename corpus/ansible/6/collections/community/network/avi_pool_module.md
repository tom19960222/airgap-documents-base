---
collection: ansible
version: "6"
title: "community.network.avi_pool module – Module for setup of Pool Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/avi_pool_module.html
fetched_at: 2026-07-27T17:16:53+00:00
---
# community.network.avi_pool module – Module for setup of Pool Avi RESTful Object

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](avi_pool_module.md#ansible-collections-community-network-avi-pool-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_pool`.

- [Synopsis](avi_pool_module.md#synopsis)
- [Requirements](avi_pool_module.md#requirements)
- [Parameters](avi_pool_module.md#parameters)
- [Notes](avi_pool_module.md#notes)
- [Examples](avi_pool_module.md#examples)
- [Return Values](avi_pool_module.md#return-values)

## [Synopsis](avi_pool_module.md#id1)

- This module is used to configure Pool object
- more examples at <https://github.com/avinetworks/devops>

## [Requirements](avi_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_pool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **a_pool**  string | Name of container cloud application that constitutes a pool in a a-b pool configuration, if different from vs app.  Field deprecated in 18.1.2. |
| **ab_pool**  string | A/b pool configuration.  Field deprecated in 18.1.2. |
| **ab_priority**  string | Priority of this pool in a a-b pool pair.  Internally used.  Field deprecated in 18.1.2. |
| **analytics_policy**  string | Determines analytics settings for the pool.  Field introduced in 18.1.5, 18.2.1. |
| **analytics_profile_ref**  string | Specifies settings related to analytics.  It is a reference to an object of type analyticsprofile.  Field introduced in 18.1.4,18.2.1. |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  Default: `"16.4.4"` |
| **apic_epg_name**  string | Synchronize cisco apic epg members with pool servers. |
| **application_persistence_profile_ref**  string | Persistence will ensure the same user sticks to the same server for a desired duration of time.  It is a reference to an object of type applicationpersistenceprofile. |
| **autoscale_launch_config_ref**  string | If configured then avi will trigger orchestration of pool server creation and deletion.  It is only supported for container clouds like mesos, openshift, kubernetes, docker, etc.  It is a reference to an object of type autoscalelaunchconfig. |
| **autoscale_networks**  string | Network ids for the launch configuration. |
| **autoscale_policy_ref**  string | Reference to server autoscale policy.  It is a reference to an object of type serverautoscalepolicy. |
| **avi_api_patch_op**  string | Patch operation to use when using avi_api_update_method as patch.  Choices:   - `"add"` - `"replace"` - `"delete"` |
| **avi_api_update_method**  string | Default method for object update is HTTP PUT.  Setting to patch will override that behavior to use HTTP PATCH.  Choices:   - `"put"` ← (default) - `"patch"` |
| **avi_credentials**  dictionary | Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details. |
| **api_version**  string | Avi controller version  Default: `"16.4.4"` |
| **controller**  string | Avi controller IP or SQDN |
| **csrftoken**  string | Avi controller API csrftoken to reuse existing session with session id  Default: `""` |
| **password**  string | Avi controller password |
| **port**  string | Avi controller port |
| **session_id**  string | Avi controller API session id to reuse existing session with csrftoken  Default: `""` |
| **tenant**  string | Avi controller tenant  Default: `"admin"` |
| **tenant_uuid**  string | Avi controller tenant UUID  Default: `""` |
| **timeout**  string | Avi controller request timeout  Default: `300` |
| **token**  string | Avi controller API token  Default: `""` |
| **username**  string | Avi controller username |
| **avi_disable_session_cache_as_fact**  boolean | It disables avi session information to be cached as a fact.  Choices:   - `false` ← (default) - `true` |
| **capacity_estimation**  boolean | Inline estimation of capacity of servers.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **capacity_estimation_ttfb_thresh**  string | The maximum time-to-first-byte of a server.  Allowed values are 1-5000.  Special values are 0 - ‘automatic’.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **cloud_config_cksum**  string | Checksum of cloud configuration for pool.  Internally set by cloud connector. |
| **cloud_ref**  string | It is a reference to an object of type cloud. |
| **conn_pool_properties**  string | Connection pool properties.  Field introduced in 18.2.1. |
| **connection_ramp_duration**  string | Duration for which new connections will be gradually ramped up to a server recently brought online.  Useful for lb algorithms that are least connection based.  Allowed values are 1-300.  Special values are 0 - ‘immediate’.  Default value when not specified in API or module is interpreted by Avi Controller as 10. |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **created_by**  string | Creator name. |
| **default_server_port**  string | Traffic sent to servers will use this destination server port unless overridden by the server’s specific port attribute.  The ssl checkbox enables avi to server encryption.  Allowed values are 1-65535.  Default value when not specified in API or module is interpreted by Avi Controller as 80. |
| **delete_server_on_dns_refresh**  boolean | Indicates whether existing ips are disabled(false) or deleted(true) on dns hostname refreshdetail – on a dns refresh, some ips set on pool may  no longer be returned by the resolver.  These ips are deleted from the pool when this knob is set to true.  They are disabled, if the knob is set to false.  Field introduced in 18.2.3.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **description**  string | A description of the pool. |
| **domain_name**  string | Comma separated list of domain names which will be used to verify the common names or subject alternative names presented by server certificates.  It is performed only when common name check host_check_enabled is enabled. |
| **east_west**  boolean | Inherited config from virtualservice.  Choices:   - `false` - `true` |
| **enabled**  boolean | Enable or disable the pool.  Disabling will terminate all open connections and pause health monitors.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **external_autoscale_groups**  string | Names of external auto-scale groups for pool servers.  Currently available only for aws and azure.  Field introduced in 17.1.2. |
| **fail_action**  string | Enable an action - close connection, http redirect or local http response - when a pool failure happens.  By default, a connection will be closed, in case the pool experiences a failure. |
| **fewest_tasks_feedback_delay**  string | Periodicity of feedback for fewest tasks server selection algorithm.  Allowed values are 1-300.  Default value when not specified in API or module is interpreted by Avi Controller as 10. |
| **graceful_disable_timeout**  string | Used to gracefully disable a server.  Virtual service waits for the specified time before terminating the existing connections to the servers that are disabled.  Allowed values are 1-7200.  Special values are 0 - ‘immediate’, -1 - ‘infinite’.  Default value when not specified in API or module is interpreted by Avi Controller as 1. |
| **gslb_sp_enabled**  boolean | Indicates if the pool is a site-persistence pool.  Field introduced in 17.2.1.  Choices:   - `false` - `true` |
| **health_monitor_refs**  string | Verify server health by applying one or more health monitors.  Active monitors generate synthetic traffic from each service engine and mark a server up or down based on the response.  The passive monitor listens only to client to server communication.  It raises or lowers the ratio of traffic destined to a server based on successful responses.  It is a reference to an object of type healthmonitor. |
| **host_check_enabled**  boolean | Enable common name check for server certificate.  If enabled and no explicit domain name is specified, avi will use the incoming host header to do the match.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **inline_health_monitor**  boolean | The passive monitor will monitor client to server connections and requests and adjust traffic load to servers based on successful responses.  This may alter the expected behavior of the lb method, such as round robin.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **ipaddrgroup_ref**  string | Use list of servers from ip address group.  It is a reference to an object of type ipaddrgroup. |
| **lb_algorithm**  string | The load balancing algorithm will pick a server within the pool’s list of available servers.  Enum options - LB_ALGORITHM_LEAST_CONNECTIONS, LB_ALGORITHM_ROUND_ROBIN, LB_ALGORITHM_FASTEST_RESPONSE, LB_ALGORITHM_CONSISTENT_HASH,  LB_ALGORITHM_LEAST_LOAD, LB_ALGORITHM_FEWEST_SERVERS, LB_ALGORITHM_RANDOM, LB_ALGORITHM_FEWEST_TASKS, LB_ALGORITHM_NEAREST_SERVER,  LB_ALGORITHM_CORE_AFFINITY, LB_ALGORITHM_TOPOLOGY.  Default value when not specified in API or module is interpreted by Avi Controller as LB_ALGORITHM_LEAST_CONNECTIONS. |
| **lb_algorithm_consistent_hash_hdr**  string | Http header name to be used for the hash key. |
| **lb_algorithm_core_nonaffinity**  string | Degree of non-affinity for core affinity based server selection.  Allowed values are 1-65535.  Field introduced in 17.1.3.  Default value when not specified in API or module is interpreted by Avi Controller as 2. |
| **lb_algorithm_hash**  string | Criteria used as a key for determining the hash between the client and server.  Enum options - LB_ALGORITHM_CONSISTENT_HASH_SOURCE_IP_ADDRESS, LB_ALGORITHM_CONSISTENT_HASH_SOURCE_IP_ADDRESS_AND_PORT,  LB_ALGORITHM_CONSISTENT_HASH_URI, LB_ALGORITHM_CONSISTENT_HASH_CUSTOM_HEADER, LB_ALGORITHM_CONSISTENT_HASH_CUSTOM_STRING,  LB_ALGORITHM_CONSISTENT_HASH_CALLID.  Default value when not specified in API or module is interpreted by Avi Controller as LB_ALGORITHM_CONSISTENT_HASH_SOURCE_IP_ADDRESS. |
| **lookup_server_by_name**  boolean | Allow server lookup by name.  Field introduced in 17.1.11,17.2.4.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **max_concurrent_connections_per_server**  string | The maximum number of concurrent connections allowed to each server within the pool.  Note applied value will be no less than the number of service engines that the pool is placed on.  If set to 0, no limit is applied.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **max_conn_rate_per_server**  string | Rate limit connections to each server. |
| **min_health_monitors_up**  string | Minimum number of health monitors in up state to mark server up.  Field introduced in 18.2.1, 17.2.12. |
| **min_servers_up**  string | Minimum number of servers in up state for marking the pool up.  Field introduced in 18.2.1, 17.2.12. |
| **name**  string / required | The name of the pool. |
| **networks**  string | (internal-use) networks designated as containing servers for this pool.  The servers may be further narrowed down by a filter.  This field is used internally by avi, not editable by the user. |
| **nsx_securitygroup**  string | A list of nsx service groups where the servers for the pool are created.  Field introduced in 17.1.1. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **pki_profile_ref**  string | Avi will validate the ssl certificate present by a server against the selected pki profile.  It is a reference to an object of type pkiprofile. |
| **placement_networks**  string | Manually select the networks and subnets used to provide reachability to the pool’s servers.  Specify the subnet using the following syntax 10-1-1-0/24.  Use static routes in vrf configuration when pool servers are not directly connected butroutable from the service engine. |
| **prst_hdr_name**  string | Header name for custom header persistence.  Field deprecated in 18.1.2. |
| **request_queue_depth**  string | Minimum number of requests to be queued when pool is full.  Default value when not specified in API or module is interpreted by Avi Controller as 128. |
| **request_queue_enabled**  boolean | Enable request queue when pool is full.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **rewrite_host_header_to_server_name**  boolean | Rewrite incoming host header to server name of the server to which the request is proxied.  Enabling this feature rewrites host header for requests to all servers in the pool.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **rewrite_host_header_to_sni**  boolean | If sni server name is specified, rewrite incoming host header to the sni server name.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **server_auto_scale**  boolean | Server autoscale.  Not used anymore.  Field deprecated in 18.1.2.  Choices:   - `false` - `true` |
| **server_count**  string | Field deprecated in 18.2.1. |
| **server_name**  string | Fully qualified dns hostname which will be used in the tls sni extension in server connections if sni is enabled.  If no value is specified, avi will use the incoming host header instead. |
| **server_reselect**  string | Server reselect configuration for http requests. |
| **server_timeout**  string | Server timeout value specifies the time within which a server connection needs to be established and a request-response exchange completes  between avi and the server.  Value of 0 results in using default timeout of 60 minutes.  Allowed values are 0-3600000.  Field introduced in 18.1.5,18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **servers**  string | The pool directs load balanced traffic to this list of destination servers.  The servers can be configured by ip address, name, network or via ip address group. |
| **service_metadata**  string | Metadata pertaining to the service provided by this pool.  In openshift/kubernetes environments, app metadata info is stored.  Any user input to this field will be overwritten by avi vantage.  Field introduced in 17.2.14,18.1.5,18.2.1. |
| **sni_enabled**  boolean | Enable tls sni for server connections.  If disabled, avi will not send the sni extension as part of the handshake.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **ssl_key_and_certificate_ref**  string | Service engines will present a client ssl certificate to the server.  It is a reference to an object of type sslkeyandcertificate. |
| **ssl_profile_ref**  string | When enabled, avi re-encrypts traffic to the backend servers.  The specific ssl profile defines which ciphers and ssl versions will be supported.  It is a reference to an object of type sslprofile. |
| **state**  string | The state that should be applied on the entity.  Choices:   - `"absent"` - `"present"` ← (default) |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  Default: `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  Default: `""` |
| **url**  string | Avi controller URL of the object. |
| **use_service_port**  boolean | Do not translate the client’s destination port when sending the connection to the server.  The pool or servers specified service port will still be used for health monitoring.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Uuid of the pool. |
| **vrf_ref**  string | Virtual routing context that the pool is bound to.  This is used to provide the isolation of the set of networks the pool is attached to.  The pool inherits the virtual routing context of the virtual service, and this field is used only internally, and is set by pb-transform.  It is a reference to an object of type vrfcontext. |

## [Notes](avi_pool_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_pool_module.md#id5)

```yaml+jinja
- name: Create a Pool with two servers and HTTP monitor
  community.network.avi_pool:
    controller: 10.10.1.20
    username: avi_user
    password: avi_password
    name: testpool1
    description: testpool1
    state: present
    health_monitor_refs:
        - '/api/healthmonitor?name=System-HTTP'
    servers:
        - ip:
            addr: 10.10.2.20
            type: V4
        - ip:
            addr: 10.10.2.21
            type: V4

- name: Patch pool with a single server using patch op and avi_credentials
  community.network.avi_pool:
    avi_api_update_method: patch
    avi_api_patch_op: delete
    avi_credentials: "{{avi_credentials}}"
    name: test-pool
    servers:
      - ip:
        addr: 10.90.64.13
        type: 'V4'
  register: pool
  when:
    - state | default("present") == "present"
```

## [Return Values](avi_pool_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | Pool (api/pool) object  Returned: success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
