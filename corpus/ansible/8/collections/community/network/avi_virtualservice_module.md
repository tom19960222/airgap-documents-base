---
collection: ansible
version: "8"
title: "community.network.avi_virtualservice module – Module for setup of VirtualService Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/avi_virtualservice_module.html
fetched_at: 2026-07-28T01:55:04+00:00
---
# community.network.avi_virtualservice module – Module for setup of VirtualService Avi RESTful Object

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](avi_virtualservice_module.md#ansible-collections-community-network-avi-virtualservice-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_virtualservice`.

- [Synopsis](avi_virtualservice_module.md#synopsis)
- [Requirements](avi_virtualservice_module.md#requirements)
- [Parameters](avi_virtualservice_module.md#parameters)
- [Notes](avi_virtualservice_module.md#notes)
- [Examples](avi_virtualservice_module.md#examples)
- [Return Values](avi_virtualservice_module.md#return-values)

## [Synopsis](avi_virtualservice_module.md#id1)

- This module is used to configure VirtualService object
- more examples at <https://github.com/avinetworks/devops>

Aliases: network.avi.avi_virtualservice

## [Requirements](avi_virtualservice_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_virtualservice_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **active_standby_se_tag**  string | This configuration only applies if the virtualservice is in legacy active standby ha mode and load distribution among active standby is enabled.  This field is used to tag the virtualservice so that virtualservices with the same tag will share the same active serviceengine.  Virtualservices with different tags will have different active serviceengines.  If one of the serviceengine’s in the serviceenginegroup fails, all virtualservices will end up using the same active serviceengine.  Redistribution of the virtualservices can be either manual or automated when the failed serviceengine recovers.  Redistribution is based on the auto redistribute property of the serviceenginegroup.  Enum options - ACTIVE_STANDBY_SE_1, ACTIVE_STANDBY_SE_2.  Default value when not specified in API or module is interpreted by Avi Controller as ACTIVE_STANDBY_SE_1. |
| **allow_invalid_client_cert**  boolean | Process request even if invalid client certificate is presented.  Datascript apis need to be used for processing of such requests.  Field introduced in 18.2.3.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **analytics_policy**  string | Determines analytics settings for the application. |
| **analytics_profile_ref**  string | Specifies settings related to analytics.  It is a reference to an object of type analyticsprofile. |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  **Default:** `"16.4.4"` |
| **apic_contract_graph**  string | The name of the contract/graph associated with the virtual service.  Should be in the <contract name> <graph name> format.  This is applicable only for service integration mode with cisco apic controller.  Field introduced in 17.2.12,18.1.2. |
| **application_profile_ref**  string | Enable application layer specific features for the virtual service.  It is a reference to an object of type applicationprofile. |
| **auto_allocate_floating_ip**  boolean | Auto-allocate floating/elastic ip from the cloud infrastructure.  Field deprecated in 17.1.1.  **Choices:**   - `false` - `true` |
| **auto_allocate_ip**  boolean | Auto-allocate vip from the provided subnet.  Field deprecated in 17.1.1.  **Choices:**   - `false` - `true` |
| **availability_zone**  string | Availability-zone to place the virtual service.  Field deprecated in 17.1.1. |
| **avi_allocated_fip**  boolean | (internal-use) fip allocated by avi in the cloud infrastructure.  Field deprecated in 17.1.1.  **Choices:**   - `false` - `true` |
| **avi_allocated_vip**  boolean | (internal-use) vip allocated by avi in the cloud infrastructure.  Field deprecated in 17.1.1.  **Choices:**   - `false` - `true` |
| **avi_api_patch_op**  string | Patch operation to use when using avi_api_update_method as patch.  **Choices:**   - `"add"` - `"replace"` - `"delete"` |
| **avi_api_update_method**  string | Default method for object update is HTTP PUT.  Setting to patch will override that behavior to use HTTP PATCH.  **Choices:**   - `"put"` ← (default) - `"patch"` |
| **avi_credentials**  dictionary | Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details. |
| **api_version**  string | Avi controller version  **Default:** `"16.4.4"` |
| **controller**  string | Avi controller IP or SQDN |
| **csrftoken**  string | Avi controller API csrftoken to reuse existing session with session id  **Default:** `""` |
| **password**  string | Avi controller password |
| **port**  string | Avi controller port |
| **session_id**  string | Avi controller API session id to reuse existing session with csrftoken  **Default:** `""` |
| **tenant**  string | Avi controller tenant  **Default:** `"admin"` |
| **tenant_uuid**  string | Avi controller tenant UUID  **Default:** `""` |
| **timeout**  string | Avi controller request timeout  **Default:** `300` |
| **token**  string | Avi controller API token  **Default:** `""` |
| **username**  string | Avi controller username |
| **avi_disable_session_cache_as_fact**  boolean | It disables avi session information to be cached as a fact.  **Choices:**   - `false` ← (default) - `true` |
| **azure_availability_set**  string | (internal-use)applicable for azure only.  Azure availability set to which this vs is associated.  Internally set by the cloud connector.  Field introduced in 17.2.12, 18.1.2. |
| **bulk_sync_kvcache**  boolean | (this is a beta feature).  Sync key-value cache to the new ses when vs is scaled out.  For ex ssl sessions are stored using vs’s key-value cache.  When the vs is scaled out, the ssl session information is synced to the new se, allowing existing ssl sessions to be reused on the new se.  Field introduced in 17.2.7, 18.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **client_auth**  string | Http authentication configuration for protected resources. |
| **close_client_conn_on_config_update**  boolean | Close client connection on vs config update.  Field introduced in 17.2.4.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **cloud_config_cksum**  string | Checksum of cloud configuration for vs.  Internally set by cloud connector. |
| **cloud_ref**  string | It is a reference to an object of type cloud. |
| **cloud_type**  string | Enum options - cloud_none, cloud_vcenter, cloud_openstack, cloud_aws, cloud_vca, cloud_apic, cloud_mesos, cloud_linuxserver, cloud_docker_ucp,  cloud_rancher, cloud_oshift_k8s, cloud_azure, cloud_gcp.  Default value when not specified in API or module is interpreted by Avi Controller as CLOUD_NONE. |
| **connections_rate_limit**  string | Rate limit the incoming connections to this virtual service. |
| **content_rewrite**  string | Profile used to match and rewrite strings in request and/or response body. |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **created_by**  string | Creator name. |
| **delay_fairness**  boolean | Select the algorithm for qos fairness.  This determines how multiple virtual services sharing the same service engines will prioritize traffic over a congested network.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **description**  string | User defined description for the object. |
| **discovered_network_ref**  string | (internal-use) discovered networks providing reachability for client facing virtual service ip.  This field is deprecated.  It is a reference to an object of type network.  Field deprecated in 17.1.1. |
| **discovered_networks**  string | (internal-use) discovered networks providing reachability for client facing virtual service ip.  This field is used internally by avi, not editable by the user.  Field deprecated in 17.1.1. |
| **discovered_subnet**  string | (internal-use) discovered subnets providing reachability for client facing virtual service ip.  This field is deprecated.  Field deprecated in 17.1.1. |
| **dns_info**  string | Service discovery specific data including fully qualified domain name, type and time-to-live of the dns record.  Note that only one of fqdn and dns_info setting is allowed. |
| **dns_policies**  string | Dns policies applied on the dns traffic of the virtual service.  Field introduced in 17.1.1. |
| **east_west_placement**  boolean | Force placement on all se’s in service group (mesos mode only).  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **enable_autogw**  boolean | Response traffic to clients will be sent back to the source mac address of the connection, rather than statically sent to a default gateway.  Default value when not specified in API or module is interpreted by Avi Controller as True.  **Choices:**   - `false` - `true` |
| **enable_rhi**  boolean | Enable route health injection using the bgp config in the vrf context.  **Choices:**   - `false` - `true` |
| **enable_rhi_snat**  boolean | Enable route health injection for source nat’ted floating ip address using the bgp config in the vrf context.  **Choices:**   - `false` - `true` |
| **enabled**  boolean | Enable or disable the virtual service.  Default value when not specified in API or module is interpreted by Avi Controller as True.  **Choices:**   - `false` - `true` |
| **error_page_profile_ref**  string | Error page profile to be used for this virtualservice.this profile is used to send the custom error page to the client generated by the proxy.  It is a reference to an object of type errorpageprofile.  Field introduced in 17.2.4. |
| **floating_ip**  string | Floating ip to associate with this virtual service.  Field deprecated in 17.1.1. |
| **floating_subnet_uuid**  string | If auto_allocate_floating_ip is true and more than one floating-ip subnets exist, then the subnet for the floating ip address allocation.  This field is applicable only if the virtualservice belongs to an openstack or aws cloud.  In openstack or aws cloud it is required when auto_allocate_floating_ip is selected.  Field deprecated in 17.1.1. |
| **flow_dist**  string | Criteria for flow distribution among ses.  Enum options - LOAD_AWARE, CONSISTENT_HASH_SOURCE_IP_ADDRESS, CONSISTENT_HASH_SOURCE_IP_ADDRESS_AND_PORT.  Default value when not specified in API or module is interpreted by Avi Controller as LOAD_AWARE. |
| **flow_label_type**  string | Criteria for flow labelling.  Enum options - NO_LABEL, APPLICATION_LABEL, SERVICE_LABEL.  Default value when not specified in API or module is interpreted by Avi Controller as NO_LABEL. |
| **fqdn**  string | Dns resolvable, fully qualified domain name of the virtualservice.  Only one of ‘fqdn’ and ‘dns_info’ configuration is allowed. |
| **host_name_xlate**  string | Translate the host name sent to the servers to this value.  Translate the host name sent from servers back to the value used by the client. |
| **http_policies**  string | Http policies applied on the data traffic of the virtual service. |
| **ign_pool_net_reach**  boolean | Ignore pool servers network reachability constraints for virtual service placement.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **ip_address**  string | Ip address of the virtual service.  Field deprecated in 17.1.1. |
| **ipam_network_subnet**  string | Subnet and/or network for allocating virtualservice ip by ipam provider module.  Field deprecated in 17.1.1. |
| **l4_policies**  string | L4 policies applied to the data traffic of the virtual service.  Field introduced in 17.2.7. |
| **limit_doser**  boolean | Limit potential dos attackers who exceed max_cps_per_client significantly to a fraction of max_cps_per_client for a while.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **max_cps_per_client**  string | Maximum connections per second per client ip.  Allowed values are 10-1000.  Special values are 0- ‘unlimited’.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **microservice_ref**  string | Microservice representing the virtual service.  It is a reference to an object of type microservice. |
| **min_pools_up**  string | Minimum number of up pools to mark vs up.  Field introduced in 18.2.1, 17.2.12. |
| **name**  string / required | Name for the virtual service. |
| **network_profile_ref**  string | Determines network settings such as protocol, tcp or udp, and related options for the protocol.  It is a reference to an object of type networkprofile. |
| **network_ref**  string | Manually override the network on which the virtual service is placed.  It is a reference to an object of type network.  Field deprecated in 17.1.1. |
| **network_security_policy_ref**  string | Network security policies for the virtual service.  It is a reference to an object of type networksecuritypolicy. |
| **nsx_securitygroup**  string | A list of nsx service groups representing the clients which can access the virtual ip of the virtual service.  Field introduced in 17.1.1. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **performance_limits**  string | Optional settings that determine performance limits like max connections or bandwidth etc. |
| **pool_group_ref**  string | The pool group is an object that contains pools.  It is a reference to an object of type poolgroup. |
| **pool_ref**  string | The pool is an object that contains destination servers and related attributes such as load-balancing and persistence.  It is a reference to an object of type pool. |
| **port_uuid**  string | (internal-use) network port assigned to the virtual service ip address.  Field deprecated in 17.1.1. |
| **remove_listening_port_on_vs_down**  boolean | Remove listening port if virtualservice is down.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **requests_rate_limit**  string | Rate limit the incoming requests to this virtual service. |
| **saml_sp_config**  string | Application-specific saml config.  Field introduced in 18.2.3. |
| **scaleout_ecmp**  boolean | Disable re-distribution of flows across service engines for a virtual service.  Enable if the network itself performs flow hashing with ecmp in environments such as gcp.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **se_group_ref**  string | The service engine group to use for this virtual service.  Moving to a new se group is disruptive to existing connections for this vs.  It is a reference to an object of type serviceenginegroup. |
| **security_policy_ref**  string | Security policy applied on the traffic of the virtual service.  This policy is used to perform security actions such as distributed denial of service (ddos) attack mitigation, etc.  It is a reference to an object of type securitypolicy.  Field introduced in 18.2.1. |
| **server_network_profile_ref**  string | Determines the network settings profile for the server side of tcp proxied connections.  Leave blank to use the same settings as the client to vs side of the connection.  It is a reference to an object of type networkprofile. |
| **service_metadata**  string | Metadata pertaining to the service provided by this virtual service.  In openshift/kubernetes environments, egress pod info is stored.  Any user input to this field will be overwritten by avi vantage. |
| **service_pool_select**  string | Select pool based on destination port. |
| **services**  string | List of services defined for this virtual service. |
| **sideband_profile**  string | Sideband configuration to be used for this virtualservice.it can be used for sending traffic to sideband vips for external inspection etc. |
| **snat_ip**  string | Nat’ted floating source ip address(es) for upstream connection to servers. |
| **sp_pool_refs**  string | Gslb pools used to manage site-persistence functionality.  Each site-persistence pool contains the virtualservices in all the other sites, that is auto-generated by the gslb manager.  This is a read-only field for the user.  It is a reference to an object of type pool.  Field introduced in 17.2.2. |
| **ssl_key_and_certificate_refs**  string | Select or create one or two certificates, ec and/or rsa, that will be presented to ssl/tls terminated connections.  It is a reference to an object of type sslkeyandcertificate. |
| **ssl_profile_ref**  string | Determines the set of ssl versions and ciphers to accept for ssl/tls terminated connections.  It is a reference to an object of type sslprofile. |
| **ssl_profile_selectors**  string | Select ssl profile based on client ip address match.  Field introduced in 18.2.3. |
| **ssl_sess_cache_avg_size**  string | Expected number of ssl session cache entries (may be exceeded).  Allowed values are 1024-16383.  Default value when not specified in API or module is interpreted by Avi Controller as 1024. |
| **sso_policy**  string | Client authentication and authorization policy for the virtualservice.  Field deprecated in 18.2.3.  Field introduced in 18.2.1. |
| **sso_policy_ref**  string | The sso policy attached to the virtualservice.  It is a reference to an object of type ssopolicy.  Field introduced in 18.2.3. |
| **state**  string | The state that should be applied on the entity.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **static_dns_records**  string | List of static dns records applied to this virtual service.  These are static entries and no health monitoring is performed against the ip addresses. |
| **subnet**  string | Subnet providing reachability for client facing virtual service ip.  Field deprecated in 17.1.1. |
| **subnet_uuid**  string | It represents subnet for the virtual service ip address allocation when auto_allocate_ip is true.it is only applicable in openstack or aws cloud.  This field is required if auto_allocate_ip is true.  Field deprecated in 17.1.1. |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  **Default:** `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  **Default:** `""` |
| **topology_policies**  string | Topology policies applied on the dns traffic of the virtual service based ongslb topology algorithm.  Field introduced in 18.2.3. |
| **traffic_clone_profile_ref**  string | Server network or list of servers for cloning traffic.  It is a reference to an object of type trafficcloneprofile.  Field introduced in 17.1.1. |
| **traffic_enabled**  boolean | Knob to enable the virtual service traffic on its assigned service engines.  This setting is effective only when the enabled flag is set to true.  Field introduced in 17.2.8.  Default value when not specified in API or module is interpreted by Avi Controller as True.  **Choices:**   - `false` - `true` |
| **type**  string | Specify if this is a normal virtual service, or if it is the parent or child of an sni-enabled virtual hosted virtual service.  Enum options - VS_TYPE_NORMAL, VS_TYPE_VH_PARENT, VS_TYPE_VH_CHILD.  Default value when not specified in API or module is interpreted by Avi Controller as VS_TYPE_NORMAL. |
| **url**  string | Avi controller URL of the object. |
| **use_bridge_ip_as_vip**  boolean | Use bridge ip as vip on each host in mesos deployments.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **use_vip_as_snat**  boolean | Use the virtual ip as the snat ip for health monitoring and sending traffic to the backend servers instead of the service engine interface ip.  The caveat of enabling this option is that the virtualservice cannot be configued in an active-active ha mode.  Dns based multi vip solution has to be used for ha & non-disruptive upgrade purposes.  Field introduced in 17.1.9,17.2.3.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Uuid of the virtualservice. |
| **vh_domain_name**  string | The exact name requested from the client’s sni-enabled tls hello domain name field.  If this is a match, the parent vs will forward the connection to this child vs. |
| **vh_parent_vs_uuid**  string | Specifies the virtual service acting as virtual hosting (sni) parent. |
| **vip**  string | List of virtual service ips.  While creating a ‘shared vs’,please use vsvip_ref to point to the shared entities.  Field introduced in 17.1.1. |
| **vrf_context_ref**  string | Virtual routing context that the virtual service is bound to.  This is used to provide the isolation of the set of networks the application is attached to.  It is a reference to an object of type vrfcontext. |
| **vs_datascripts**  string | Datascripts applied on the data traffic of the virtual service. |
| **vsvip_cloud_config_cksum**  string | Checksum of cloud configuration for vsvip.  Internally set by cloud connector.  Field introduced in 17.2.9, 18.1.2. |
| **vsvip_ref**  string | Mostly used during the creation of shared vs, this field refers to entities that can be shared across virtual services.  It is a reference to an object of type vsvip.  Field introduced in 17.1.1. |
| **waf_policy_ref**  string | Waf policy for the virtual service.  It is a reference to an object of type wafpolicy.  Field introduced in 17.2.1. |
| **weight**  string | The quality of service weight to assign to traffic transmitted from this virtual service.  A higher weight will prioritize traffic versus other virtual services sharing the same service engines.  Allowed values are 1-128.  Default value when not specified in API or module is interpreted by Avi Controller as 1. |

## [Notes](avi_virtualservice_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_virtualservice_module.md#id5)

```yaml+jinja
- name: Create SSL Virtual Service using Pool testpool2
  community.network.avi_virtualservice:
    controller: 10.10.27.90
    username: admin
    password: AviNetworks123!
    name: newtestvs
    state: present
    performance_limits:
    max_concurrent_connections: 1000
    services:
        - port: 443
          enable_ssl: true
        - port: 80
    ssl_profile_ref: '/api/sslprofile?name=System-Standard'
    application_profile_ref: '/api/applicationprofile?name=System-Secure-HTTP'
    ssl_key_and_certificate_refs:
        - '/api/sslkeyandcertificate?name=System-Default-Cert'
    ip_address:
    addr: 10.90.131.103
    type: V4
    pool_ref: '/api/pool?name=testpool2'
```

## [Return Values](avi_virtualservice_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | VirtualService (api/virtualservice) object  **Returned:** success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
