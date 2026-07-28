---
collection: ansible
version: "6"
title: "community.network.avi_serviceenginegroup module – Module for setup of ServiceEngineGroup Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/avi_serviceenginegroup_module.html
fetched_at: 2026-07-27T17:16:59+00:00
---
# community.network.avi_serviceenginegroup module – Module for setup of ServiceEngineGroup Avi RESTful Object

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
> see [Requirements](avi_serviceenginegroup_module.md#ansible-collections-community-network-avi-serviceenginegroup-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_serviceenginegroup`.

- [Synopsis](avi_serviceenginegroup_module.md#synopsis)
- [Requirements](avi_serviceenginegroup_module.md#requirements)
- [Parameters](avi_serviceenginegroup_module.md#parameters)
- [Notes](avi_serviceenginegroup_module.md#notes)
- [Examples](avi_serviceenginegroup_module.md#examples)
- [Return Values](avi_serviceenginegroup_module.md#return-values)

## [Synopsis](avi_serviceenginegroup_module.md#id1)

- This module is used to configure ServiceEngineGroup object
- more examples at <https://github.com/avinetworks/devops>

## [Requirements](avi_serviceenginegroup_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_serviceenginegroup_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accelerated_networking**  boolean | Enable accelerated networking option for azure se.  Accelerated networking enables single root i/o virtualization (sr-iov) to a se vm.  This improves networking performance.  Field introduced in 17.2.14,18.1.5,18.2.1.  Choices:   - `false` - `true` |
| **active_standby**  boolean | Service engines in active/standby mode for ha failover.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **additional_config_memory**  string | Indicates the percent of config memory used for config updates.  Allowed values are 0-90.  Field deprecated in 18.1.2.  Field introduced in 18.1.1. |
| **advertise_backend_networks**  boolean | Advertise reach-ability of backend server networks via adc through bgp for default gateway feature.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **aggressive_failure_detection**  boolean | Enable aggressive failover configuration for ha.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **algo**  string | In compact placement, virtual services are placed on existing ses until max_vs_per_se limit is reached.  Enum options - PLACEMENT_ALGO_PACKED, PLACEMENT_ALGO_DISTRIBUTED.  Default value when not specified in API or module is interpreted by Avi Controller as PLACEMENT_ALGO_PACKED. |
| **allow_burst**  boolean | Allow ses to be created using burst license.  Field introduced in 17.2.5.  Choices:   - `false` - `true` |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  Default: `"16.4.4"` |
| **app_cache_percent**  string | A percent value of total se memory reserved for application caching.  This is an se bootup property and requires se restart.  Allowed values are 0 - 100.  Special values are 0- ‘disable’.  Field introduced in 18.2.3.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **app_learning_memory_percent**  string | A percent value of total se memory reserved for application learning.  This is an se bootup property and requires se restart.  Allowed values are 0 - 10.  Field introduced in 18.2.3.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **archive_shm_limit**  string | Amount of se memory in gb until which shared memory is collected in core archive.  Field introduced in 17.1.3.  Default value when not specified in API or module is interpreted by Avi Controller as 8. |
| **async_ssl**  boolean | Ssl handshakes will be handled by dedicated ssl threads.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **async_ssl_threads**  string | Number of async ssl threads per se_dp.  Allowed values are 1-16.  Default value when not specified in API or module is interpreted by Avi Controller as 1. |
| **auto_rebalance**  boolean | If set, virtual services will be automatically migrated when load on an se is less than minimum or more than maximum thresholds.  Only alerts are generated when the auto_rebalance is not set.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **auto_rebalance_capacity_per_se**  string | Capacities of se for auto rebalance for each criteria.  Field introduced in 17.2.4. |
| **auto_rebalance_criteria**  string | Set of criteria for se auto rebalance.  Enum options - SE_AUTO_REBALANCE_CPU, SE_AUTO_REBALANCE_PPS, SE_AUTO_REBALANCE_MBPS, SE_AUTO_REBALANCE_OPEN_CONNS, SE_AUTO_REBALANCE_CPS.  Field introduced in 17.2.3. |
| **auto_rebalance_interval**  string | Frequency of rebalance, if ‘auto rebalance’ is enabled.  Default value when not specified in API or module is interpreted by Avi Controller as 300. |
| **auto_redistribute_active_standby_load**  boolean | Redistribution of virtual services from the takeover se to the replacement se can cause momentary traffic loss.  If the auto-redistribute load option is left in its default off state, any desired rebalancing requires calls to rest api.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
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
| **bgp_state_update_interval**  string | Bgp peer state update interval.  Allowed values are 5-100.  Field introduced in 17.2.14,18.1.5,18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as 10. |
| **buffer_se**  string | Excess service engine capacity provisioned for ha failover.  Default value when not specified in API or module is interpreted by Avi Controller as 1. |
| **cloud_ref**  string | It is a reference to an object of type cloud. |
| **config_debugs_on_all_cores**  boolean | Enable config debugs on all cores of se.  Field introduced in 17.2.13,18.1.5,18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **connection_memory_percentage**  string | Percentage of memory for connection state.  This will come at the expense of memory used for http in-memory cache.  Allowed values are 10-90.  Default value when not specified in API or module is interpreted by Avi Controller as 50. |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **cpu_reserve**  boolean | Boolean flag to set cpu_reserve.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **cpu_socket_affinity**  boolean | Allocate all the cpu cores for the service engine virtual machines on the same cpu socket.  Applicable only for vcenter cloud.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **custom_securitygroups_data**  string | Custom security groups to be associated with data vnics for se instances in openstack and aws clouds.  Field introduced in 17.1.3. |
| **custom_securitygroups_mgmt**  string | Custom security groups to be associated with management vnic for se instances in openstack and aws clouds.  Field introduced in 17.1.3. |
| **custom_tag**  string | Custom tag will be used to create the tags for se instance in aws.  Note this is not the same as the prefix for se name. |
| **data_network_id**  string | Subnet used to spin up the data nic for service engines, used only for azure cloud.  Overrides the cloud level setting for service engine subnet.  Field introduced in 18.2.3. |
| **datascript_timeout**  string | Number of instructions before datascript times out.  Allowed values are 0-100000000.  Field introduced in 18.2.3.  Default value when not specified in API or module is interpreted by Avi Controller as 1000000. |
| **dedicated_dispatcher_core**  boolean | Dedicate the core that handles packet receive/transmit from the network to just the dispatching function.  Don’t use it for tcp/ip and ssl functions.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **description**  string | User defined description for the object. |
| **disable_avi_securitygroups**  boolean | By default, avi creates and manages security groups along with custom sg provided by user.  Set this to true to disallow avi to create and manage new security groups.  Avi will only make use of custom security groups provided by user.  This option is only supported for aws cloud type.  Field introduced in 17.2.13,18.1.4,18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **disable_csum_offloads**  boolean | Stop using tcp/udp and ip checksum offload features of nics.  Field introduced in 17.1.14, 17.2.5, 18.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **disable_gro**  boolean | Disable generic receive offload (gro) in dpdk poll-mode driver packet receive path.  Gro is on by default on nics that do not support lro (large receive offload) or do not gain performance boost from lro.  Field introduced in 17.2.5, 18.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **disable_se_memory_check**  boolean | If set, disable the config memory check done in service engine.  Field introduced in 18.1.2.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **disable_tso**  boolean | Disable tcp segmentation offload (tso) in dpdk poll-mode driver packet transmit path.  Tso is on by default on nics that support it.  Field introduced in 17.2.5, 18.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **disk_per_se**  string | Amount of disk space for each of the service engine virtual machines.  Default value when not specified in API or module is interpreted by Avi Controller as 10. |
| **distribute_load_active_standby**  boolean | Use both the active and standby service engines for virtual service placement in the legacy active standby ha mode.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **distribute_queues**  boolean | Distributes queue ownership among cores so multiple cores handle dispatcher duties.  Field introduced in 17.2.8.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **enable_hsm_priming**  boolean | (this is a beta feature).  Enable hsm key priming.  If enabled, key handles on the hsm will be synced to se before processing client connections.  Field introduced in 17.2.7, 18.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **enable_multi_lb**  boolean | Applicable only for azure cloud with basic sku lb.  If set, additional azure lbs will be automatically created if resources in existing lb are exhausted.  Field introduced in 17.2.10, 18.1.2.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **enable_routing**  boolean | Enable routing for this serviceenginegroup .  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **enable_vip_on_all_interfaces**  boolean | Enable vip on all interfaces of se.  Field introduced in 17.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **enable_vmac**  boolean | Use virtual mac address for interfaces on which floating interface ips are placed.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **ephemeral_portrange_end**  string | End local ephemeral port number for outbound connections.  Field introduced in 17.2.13, 18.1.5, 18.2.1. |
| **ephemeral_portrange_start**  string | Start local ephemeral port number for outbound connections.  Field introduced in 17.2.13, 18.1.5, 18.2.1. |
| **extra_config_multiplier**  string | Multiplier for extra config to support large vs/pool config.  Default value when not specified in API or module is interpreted by Avi Controller as 0.0. |
| **extra_shared_config_memory**  string | Extra config memory to support large geo db configuration.  Field introduced in 17.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **floating_intf_ip**  string | If serviceenginegroup is configured for legacy 1+1 active standby ha mode, floating ip’s will be advertised only by the active se in the pair.  Virtual services in this group must be disabled/enabled for any changes to the floating ip’s to take effect.  Only active se hosting vs tagged with active standby se 1 tag will advertise this floating ip when manual load distribution is enabled. |
| **floating_intf_ip_se_2**  string | If serviceenginegroup is configured for legacy 1+1 active standby ha mode, floating ip’s will be advertised only by the active se in the pair.  Virtual services in this group must be disabled/enabled for any changes to the floating ip’s to take effect.  Only active se hosting vs tagged with active standby se 2 tag will advertise this floating ip when manual load distribution is enabled. |
| **flow_table_new_syn_max_entries**  string | Maximum number of flow table entries that have not completed tcp three-way handshake yet.  Field introduced in 17.2.5.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **free_list_size**  string | Number of entries in the free list.  Field introduced in 17.2.10, 18.1.2.  Default value when not specified in API or module is interpreted by Avi Controller as 1024. |
| **ha_mode**  string | High availability mode for all the virtual services using this service engine group.  Enum options - HA_MODE_SHARED_PAIR, HA_MODE_SHARED, HA_MODE_LEGACY_ACTIVE_STANDBY.  Default value when not specified in API or module is interpreted by Avi Controller as HA_MODE_SHARED. |
| **hardwaresecuritymodulegroup_ref**  string | It is a reference to an object of type hardwaresecuritymodulegroup. |
| **heap_minimum_config_memory**  string | Minimum required heap memory to apply any configuration.  Allowed values are 0-100.  Field introduced in 18.1.2.  Default value when not specified in API or module is interpreted by Avi Controller as 8. |
| **hm_on_standby**  boolean | Enable active health monitoring from the standby se for all placed virtual services.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **host_attribute_key**  string | Key of a (key, value) pair identifying a label for a set of nodes usually in container clouds.  Needs to be specified together with host_attribute_value.  Ses can be configured differently including ha modes across different se groups.  May also be used for isolation between different classes of virtualservices.  Virtualservices’ se group may be specified via annotations/labels.  A openshift/kubernetes namespace maybe annotated with a matching se group label as openshift.io/node-selector apptype=prod.  When multiple se groups are used in a cloud with host attributes specified,just a single se group can exist as a match-all se group without a  host_attribute_key. |
| **host_attribute_value**  string | Value of a (key, value) pair identifying a label for a set of nodes usually in container clouds.  Needs to be specified together with host_attribute_key. |
| **host_gateway_monitor**  boolean | Enable the host gateway monitor when service engine is deployed as docker container.  Disabled by default.  Field introduced in 17.2.4.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **hypervisor**  string | Override default hypervisor.  Enum options - DEFAULT, VMWARE_ESX, KVM, VMWARE_VSAN, XEN. |
| **ignore_rtt_threshold**  string | Ignore rtt samples if it is above threshold.  Field introduced in 17.1.6,17.2.2.  Default value when not specified in API or module is interpreted by Avi Controller as 5000. |
| **ingress_access_data**  string | Program se security group ingress rules to allow vip data access from remote cidr type.  Enum options - SG_INGRESS_ACCESS_NONE, SG_INGRESS_ACCESS_ALL, SG_INGRESS_ACCESS_VPC.  Field introduced in 17.1.5.  Default value when not specified in API or module is interpreted by Avi Controller as SG_INGRESS_ACCESS_ALL. |
| **ingress_access_mgmt**  string | Program se security group ingress rules to allow ssh/icmp management access from remote cidr type.  Enum options - SG_INGRESS_ACCESS_NONE, SG_INGRESS_ACCESS_ALL, SG_INGRESS_ACCESS_VPC.  Field introduced in 17.1.5.  Default value when not specified in API or module is interpreted by Avi Controller as SG_INGRESS_ACCESS_ALL. |
| **instance_flavor**  string | Instance/flavor name for se instance. |
| **iptables**  string | Iptables rules. |
| **least_load_core_selection**  boolean | Select core with least load for new flow.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **license_tier**  string | Specifies the license tier which would be used.  This field by default inherits the value from cloud.  Enum options - ENTERPRISE_16, ENTERPRISE_18.  Field introduced in 17.2.5. |
| **license_type**  string | If no license type is specified then default license enforcement for the cloud type is chosen.  Enum options - LIC_BACKEND_SERVERS, LIC_SOCKETS, LIC_CORES, LIC_HOSTS, LIC_SE_BANDWIDTH, LIC_METERED_SE_BANDWIDTH.  Field introduced in 17.2.5. |
| **log_disksz**  string | Maximum disk capacity (in mb) to be allocated to an se.  This is exclusively used for debug and log data.  Default value when not specified in API or module is interpreted by Avi Controller as 10000. |
| **max_cpu_usage**  string | When cpu usage on an se exceeds this threshold, virtual services hosted on this se may be rebalanced to other ses to reduce load.  A new se may be created as part of this process.  Allowed values are 40-90.  Default value when not specified in API or module is interpreted by Avi Controller as 80. |
| **max_memory_per_mempool**  string | Max bytes that can be allocated in a single mempool.  Field introduced in 18.1.5.  Default value when not specified in API or module is interpreted by Avi Controller as 64. |
| **max_public_ips_per_lb**  string | Applicable to azure platform only.  Maximum number of public ips per azure lb.  Field introduced in 17.2.12, 18.1.2.  Default value when not specified in API or module is interpreted by Avi Controller as 30. |
| **max_rules_per_lb**  string | Applicable to azure platform only.  Maximum number of rules per azure lb.  Field introduced in 17.2.12, 18.1.2.  Default value when not specified in API or module is interpreted by Avi Controller as 150. |
| **max_scaleout_per_vs**  string | Maximum number of active service engines for the virtual service.  Allowed values are 1-64.  Default value when not specified in API or module is interpreted by Avi Controller as 4. |
| **max_se**  string | Maximum number of services engines in this group.  Allowed values are 0-1000.  Default value when not specified in API or module is interpreted by Avi Controller as 10. |
| **max_vs_per_se**  string | Maximum number of virtual services that can be placed on a single service engine.  East west virtual services are excluded from this limit.  Allowed values are 1-1000.  Default value when not specified in API or module is interpreted by Avi Controller as 10. |
| **mem_reserve**  boolean | Boolean flag to set mem_reserve.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **memory_for_config_update**  string | Indicates the percent of memory reserved for config updates.  Allowed values are 0-100.  Field introduced in 18.1.2.  Default value when not specified in API or module is interpreted by Avi Controller as 15. |
| **memory_per_se**  string | Amount of memory for each of the service engine virtual machines.  Default value when not specified in API or module is interpreted by Avi Controller as 2048. |
| **mgmt_network_ref**  string | Management network to use for avi service engines.  It is a reference to an object of type network. |
| **mgmt_subnet**  string | Management subnet to use for avi service engines. |
| **min_cpu_usage**  string | When cpu usage on an se falls below the minimum threshold, virtual services hosted on the se may be consolidated onto other underutilized ses.  After consolidation, unused service engines may then be eligible for deletion.  Allowed values are 20-60.  Default value when not specified in API or module is interpreted by Avi Controller as 30. |
| **min_scaleout_per_vs**  string | Minimum number of active service engines for the virtual service.  Allowed values are 1-64.  Default value when not specified in API or module is interpreted by Avi Controller as 1. |
| **min_se**  string | Minimum number of services engines in this group (relevant for se autorebalance only).  Allowed values are 0-1000.  Field introduced in 17.2.13,18.1.3,18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as 1. |
| **minimum_connection_memory**  string | Indicates the percent of memory reserved for connections.  Allowed values are 0-100.  Field introduced in 18.1.2.  Default value when not specified in API or module is interpreted by Avi Controller as 20. |
| **minimum_required_config_memory**  string | Required available config memory to apply any configuration.  Allowed values are 0-90.  Field deprecated in 18.1.2.  Field introduced in 18.1.1. |
| **n_log_streaming_threads**  string | Number of threads to use for log streaming.  Allowed values are 1-100.  Field introduced in 17.2.12, 18.1.2.  Default value when not specified in API or module is interpreted by Avi Controller as 1. |
| **name**  string / required | Name of the object. |
| **non_significant_log_throttle**  string | This setting limits the number of non-significant logs generated per second per core on this se.  Default is 100 logs per second.  Set it to zero (0) to disable throttling.  Field introduced in 17.1.3.  Default value when not specified in API or module is interpreted by Avi Controller as 100. |
| **num_dispatcher_cores**  string | Number of dispatcher cores (0,1,2,4,8 or 16).  If set to 0, then number of dispatcher cores is deduced automatically.  Allowed values are 0,1,2,4,8,16.  Field introduced in 17.2.12, 18.1.3, 18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **num_flow_cores_sum_changes_to_ignore**  string | Number of changes in num flow cores sum to ignore.  Default value when not specified in API or module is interpreted by Avi Controller as 8. |
| **openstack_availability_zone**  string | Field deprecated in 17.1.1. |
| **openstack_availability_zones**  string | Field introduced in 17.1.1. |
| **openstack_mgmt_network_name**  string | Avi management network name. |
| **openstack_mgmt_network_uuid**  string | Management network uuid. |
| **os_reserved_memory**  string | Amount of extra memory to be reserved for use by the operating system on a service engine.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **per_app**  boolean | Per-app se mode is designed for deploying dedicated load balancers per app (vs).  In this mode, each se is limited to a max of 2 vss.  Vcpus in per-app ses count towards licensing usage at 25% rate.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **placement_mode**  string | If placement mode is ‘auto’, virtual services are automatically placed on service engines.  Enum options - PLACEMENT_MODE_AUTO.  Default value when not specified in API or module is interpreted by Avi Controller as PLACEMENT_MODE_AUTO. |
| **realtime_se_metrics**  string | Enable or disable real time se metrics. |
| **reboot_on_stop**  boolean | Reboot the system if the se is stopped.  Field introduced in 17.2.16,18.2.3.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **se_bandwidth_type**  string | Select the se bandwidth for the bandwidth license.  Enum options - SE_BANDWIDTH_UNLIMITED, SE_BANDWIDTH_25M, SE_BANDWIDTH_200M, SE_BANDWIDTH_1000M, SE_BANDWIDTH_10000M.  Field introduced in 17.2.5. |
| **se_deprovision_delay**  string | Duration to preserve unused service engine virtual machines before deleting them.  If traffic to a virtual service were to spike up abruptly, this se would still be available to be utilized again rather than creating a new se.  If this value is set to 0, controller will never delete any ses and administrator has to manually cleanup unused ses.  Allowed values are 0-525600.  Default value when not specified in API or module is interpreted by Avi Controller as 120. |
| **se_dos_profile**  string | Dosthresholdprofile settings for serviceenginegroup. |
| **se_dpdk_pmd**  string | Determines if dpdk pool mode driver should be used or not 0 automatically determine based on hypervisor/nic type 1 unconditionally use dpdk  poll mode driver 2 don’t use dpdk poll mode driver.  Allowed values are 0-2.  Field introduced in 18.1.3.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **se_flow_probe_retries**  string | Flow probe retry count if no replies are received.  Allowed values are 0-5.  Field introduced in 18.1.4, 18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as 2. |
| **se_flow_probe_timer**  string | Timeout in milliseconds for flow probe entries.  Allowed values are 10-200.  Field introduced in 18.1.4, 18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as 100. |
| **se_ipc_udp_port**  string | Udp port for se_dp ipc in docker bridge mode.  Field introduced in 17.1.2.  Default value when not specified in API or module is interpreted by Avi Controller as 1500. |
| **se_name_prefix**  string | Prefix to use for virtual machine name of service engines.  Default value when not specified in API or module is interpreted by Avi Controller as Avi. |
| **se_pcap_lookahead**  boolean | Enables lookahead mode of packet receive in pcap mode.  Introduced to overcome an issue with hv_netvsc driver.  Lookahead mode attempts to ensure that application and kernel’s view of the receive rings are consistent.  Field introduced in 18.2.3.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **se_pcap_reinit_frequency**  string | Frequency in seconds at which periodically a pcap reinit check is triggered.  May be used in conjunction with the configuration pcap_reinit_threshold.  (valid range 15 mins - 12 hours, 0 - disables).  Allowed values are 900-43200.  Special values are 0- ‘disable’.  Field introduced in 17.2.13, 18.1.3, 18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **se_pcap_reinit_threshold**  string | Threshold for input packet receive errors in pcap mode exceeding which a pcap reinit is triggered.  If not set, an unconditional reinit is performed.  This value is checked every pcap_reinit_frequency interval.  Field introduced in 17.2.13, 18.1.3, 18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **se_probe_port**  string | Tcp port on se where echo service will be run.  Field introduced in 17.2.2.  Default value when not specified in API or module is interpreted by Avi Controller as 7. |
| **se_remote_punt_udp_port**  string | Udp port for punted packets in docker bridge mode.  Field introduced in 17.1.2.  Default value when not specified in API or module is interpreted by Avi Controller as 1501. |
| **se_routing**  boolean | Enable routing via service engine datapath.  When disabled, routing is done by the linux kernel.  Ip routing needs to be enabled in service engine group for se routing to be effective.  Field introduced in 18.2.3.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **se_sb_dedicated_core**  boolean | Sideband traffic will be handled by a dedicated core.  Field introduced in 16.5.2, 17.1.9, 17.2.3.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **se_sb_threads**  string | Number of sideband threads per se.  Allowed values are 1-128.  Field introduced in 16.5.2, 17.1.9, 17.2.3.  Default value when not specified in API or module is interpreted by Avi Controller as 1. |
| **se_thread_multiplier**  string | Multiplier for se threads based on vcpu.  Allowed values are 1-10.  Default value when not specified in API or module is interpreted by Avi Controller as 1. |
| **se_tracert_port_range**  string | Traceroute port range.  Field introduced in 17.2.8. |
| **se_tunnel_mode**  string | Determines if dsr from secondary se is active or not 0 automatically determine based on hypervisor type.  1 disable dsr unconditionally.  2 enable dsr unconditionally.  Allowed values are 0-2.  Field introduced in 17.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **se_tunnel_udp_port**  string | Udp port for tunneled packets from secondary to primary se in docker bridge mode.  Field introduced in 17.1.3.  Default value when not specified in API or module is interpreted by Avi Controller as 1550. |
| **se_udp_encap_ipc**  string | Determines if se-se ipc messages are encapsulated in a udp header 0 automatically determine based on hypervisor type.  1 use udp encap unconditionally.  Allowed values are 0-1.  Field introduced in 17.1.2.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **se_use_dpdk**  string | Determines if dpdk library should be used or not 0 automatically determine based on hypervisor type 1 use dpdk if pcap is not enabled 2  don’t use dpdk.  Allowed values are 0-2.  Field introduced in 18.1.3.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **se_vs_hb_max_pkts_in_batch**  string | Maximum number of aggregated vs heartbeat packets to send in a batch.  Allowed values are 1-256.  Field introduced in 17.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as 64. |
| **se_vs_hb_max_vs_in_pkt**  string | Maximum number of virtualservices for which heartbeat messages are aggregated in one packet.  Allowed values are 1-1024.  Field introduced in 17.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as 256. |
| **self_se_election**  boolean | Enable ses to elect a primary amongst themselves in the absence of a connectivity to controller.  Field introduced in 18.1.2.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **service_ip6_subnets**  string | Ipv6 subnets assigned to the se group.  Required for vs group placement.  Field introduced in 18.1.1. |
| **service_ip_subnets**  string | Subnets assigned to the se group.  Required for vs group placement.  Field introduced in 17.1.1. |
| **shm_minimum_config_memory**  string | Minimum required shared memory to apply any configuration.  Allowed values are 0-100.  Field introduced in 18.1.2.  Default value when not specified in API or module is interpreted by Avi Controller as 4. |
| **significant_log_throttle**  string | This setting limits the number of significant logs generated per second per core on this se.  Default is 100 logs per second.  Set it to zero (0) to disable throttling.  Field introduced in 17.1.3.  Default value when not specified in API or module is interpreted by Avi Controller as 100. |
| **ssl_preprocess_sni_hostname**  boolean | (beta) preprocess ssl client hello for sni hostname extension.if set to true, this will apply sni child’s ssl protocol(s), if they are different  from sni parent’s allowed ssl protocol(s).  Field introduced in 17.2.12, 18.1.3.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **state**  string | The state that should be applied on the entity.  Choices:   - `"absent"` - `"present"` ← (default) |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  Default: `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  Default: `""` |
| **udf_log_throttle**  string | This setting limits the number of udf logs generated per second per core on this se.  Udf logs are generated due to the configured client log filters or the rules with logging enabled.  Default is 100 logs per second.  Set it to zero (0) to disable throttling.  Field introduced in 17.1.3.  Default value when not specified in API or module is interpreted by Avi Controller as 100. |
| **url**  string | Avi controller URL of the object. |
| **use_standard_alb**  boolean | Use standard sku azure load balancer.  By default cloud level flag is set.  If not set, it inherits/uses the use_standard_alb flag from the cloud.  Field introduced in 18.2.3.  Choices:   - `false` - `true` |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Unique object identifier of the object. |
| **vcenter_clusters**  string | Vcenterclusters settings for serviceenginegroup. |
| **vcenter_datastore_mode**  string | Enum options - vcenter_datastore_any, vcenter_datastore_local, vcenter_datastore_shared.  Default value when not specified in API or module is interpreted by Avi Controller as VCENTER_DATASTORE_ANY. |
| **vcenter_datastores**  string | List of vcenterdatastore. |
| **vcenter_datastores_include**  boolean | Boolean flag to set vcenter_datastores_include.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **vcenter_folder**  string | Folder to place all the service engine virtual machines in vcenter.  Default value when not specified in API or module is interpreted by Avi Controller as AviSeFolder. |
| **vcenter_hosts**  string | Vcenterhosts settings for serviceenginegroup. |
| **vcpus_per_se**  string | Number of vcpus for each of the service engine virtual machines.  Default value when not specified in API or module is interpreted by Avi Controller as 1. |
| **vip_asg**  string | When vip_asg is set, vip configuration will be managed by avi.user will be able to configure vip_asg or vips individually at the time of create.  Field introduced in 17.2.12, 18.1.2. |
| **vs_host_redundancy**  boolean | Ensure primary and secondary service engines are deployed on different physical hosts.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **vs_scalein_timeout**  string | Time to wait for the scaled in se to drain existing flows before marking the scalein done.  Default value when not specified in API or module is interpreted by Avi Controller as 30. |
| **vs_scalein_timeout_for_upgrade**  string | During se upgrade, time to wait for the scaled-in se to drain existing flows before marking the scalein done.  Default value when not specified in API or module is interpreted by Avi Controller as 30. |
| **vs_scaleout_timeout**  string | Time to wait for the scaled out se to become ready before marking the scaleout done.  Default value when not specified in API or module is interpreted by Avi Controller as 600. |
| **vs_se_scaleout_additional_wait_time**  string | Wait time for sending scaleout ready notification after virtual service is marked up.  In certain deployments, there may be an additional delay to accept traffic.  For example, for bgp, some time is needed for route advertisement.  Allowed values are 0-20.  Field introduced in 18.1.5,18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **vs_se_scaleout_ready_timeout**  string | Timeout in seconds for service engine to sendscaleout ready notification of a virtual service.  Allowed values are 0-60.  Field introduced in 18.1.5,18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as 25. |
| **vs_switchover_timeout**  string | During se upgrade in a legacy active/standby segroup, time to wait for the new primary se to accept flows before marking the switchover done.  Field introduced in 17.2.13,18.1.4,18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as 300. |
| **vss_placement**  string | Parameters to place virtual services on only a subset of the cores of an se.  Field introduced in 17.2.5. |
| **vss_placement_enabled**  boolean | If set, virtual services will be placed on only a subset of the cores of an se.  Field introduced in 18.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **waf_learning_interval**  string | Frequency with which se publishes waf learning.  Allowed values are 1-43200.  Field deprecated in 18.2.3.  Field introduced in 18.1.2.  Default value when not specified in API or module is interpreted by Avi Controller as 10. |
| **waf_learning_memory**  string | Amount of memory reserved on se for waf learning.  Cannot exceed 5% of se memory.  Field deprecated in 18.2.3.  Field introduced in 18.1.2.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **waf_mempool**  boolean | Enable memory pool for waf.  Field introduced in 17.2.3.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **waf_mempool_size**  string | Memory pool size used for waf.  Field introduced in 17.2.3.  Default value when not specified in API or module is interpreted by Avi Controller as 64. |

## [Notes](avi_serviceenginegroup_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_serviceenginegroup_module.md#id5)

```yaml+jinja
- name: Example to create ServiceEngineGroup object
  community.network.avi_serviceenginegroup:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_serviceenginegroup
```

## [Return Values](avi_serviceenginegroup_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | ServiceEngineGroup (api/serviceenginegroup) object  Returned: success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
