---
collection: ansible
version: "6"
title: "community.network.avi_controllerproperties module – Module for setup of ControllerProperties Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/avi_controllerproperties_module.html
fetched_at: 2026-07-27T17:16:40+00:00
---
# community.network.avi_controllerproperties module – Module for setup of ControllerProperties Avi RESTful Object

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
> see [Requirements](avi_controllerproperties_module.md#ansible-collections-community-network-avi-controllerproperties-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_controllerproperties`.

- [Synopsis](avi_controllerproperties_module.md#synopsis)
- [Requirements](avi_controllerproperties_module.md#requirements)
- [Parameters](avi_controllerproperties_module.md#parameters)
- [Notes](avi_controllerproperties_module.md#notes)
- [Examples](avi_controllerproperties_module.md#examples)
- [Return Values](avi_controllerproperties_module.md#return-values)

## [Synopsis](avi_controllerproperties_module.md#id1)

- This module is used to configure ControllerProperties object
- more examples at <https://github.com/avinetworks/devops>

## [Requirements](avi_controllerproperties_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_controllerproperties_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_ip_forwarding**  boolean | Field introduced in 17.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **allow_unauthenticated_apis**  boolean | Allow unauthenticated access for special apis.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **allow_unauthenticated_nodes**  boolean | Boolean flag to set allow_unauthenticated_nodes.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_idle_timeout**  string | Allowed values are 0-1440.  Default value when not specified in API or module is interpreted by Avi Controller as 15. |
| **api_perf_logging_threshold**  string | Threshold to log request timing in portal_performance.log and server-timing response header.  Any stage taking longer than 1% of the threshold will be included in the server-timing header.  Field introduced in 18.1.4, 18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as 10000. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  Default: `"16.4.4"` |
| **appviewx_compat_mode**  boolean | Export configuration in appviewx compatibility mode.  Field introduced in 17.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **attach_ip_retry_interval**  string | Number of attach_ip_retry_interval.  Default value when not specified in API or module is interpreted by Avi Controller as 360. |
| **attach_ip_retry_limit**  string | Number of attach_ip_retry_limit.  Default value when not specified in API or module is interpreted by Avi Controller as 4. |
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
| **bm_use_ansible**  boolean | Use ansible for se creation in baremetal.  Field introduced in 17.2.2.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **cleanup_expired_authtoken_timeout_period**  string | Period for auth token cleanup job.  Field introduced in 18.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as 60. |
| **cleanup_sessions_timeout_period**  string | Period for sessions cleanup job.  Field introduced in 18.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as 60. |
| **cloud_reconcile**  boolean | Enable/disable periodic reconcile for all the clouds.  Field introduced in 17.2.14,18.1.5,18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **cluster_ip_gratuitous_arp_period**  string | Period for cluster ip gratuitous arp job.  Default value when not specified in API or module is interpreted by Avi Controller as 60. |
| **consistency_check_timeout_period**  string | Period for consistency check job.  Field introduced in 18.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as 60. |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **crashed_se_reboot**  string | Number of crashed_se_reboot.  Default value when not specified in API or module is interpreted by Avi Controller as 900. |
| **dead_se_detection_timer**  string | Number of dead_se_detection_timer.  Default value when not specified in API or module is interpreted by Avi Controller as 360. |
| **dns_refresh_period**  string | Period for refresh pool and gslb dns job.  Default value when not specified in API or module is interpreted by Avi Controller as 60. |
| **dummy**  string | Number of dummy. |
| **enable_api_sharding**  boolean | This setting enables the controller leader to shard api requests to the followers (if any).  Field introduced in 18.1.5, 18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **enable_memory_balancer**  boolean | Enable/disable memory balancer.  Field introduced in 17.2.8.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **fatal_error_lease_time**  string | Number of fatal_error_lease_time.  Default value when not specified in API or module is interpreted by Avi Controller as 120. |
| **max_dead_se_in_grp**  string | Number of max_dead_se_in_grp.  Default value when not specified in API or module is interpreted by Avi Controller as 1. |
| **max_pcap_per_tenant**  string | Maximum number of pcap files stored per tenant.  Default value when not specified in API or module is interpreted by Avi Controller as 4. |
| **max_seq_attach_ip_failures**  string | Maximum number of consecutive attach ip failures that halts vs placement.  Field introduced in 17.2.2.  Default value when not specified in API or module is interpreted by Avi Controller as 3. |
| **max_seq_vnic_failures**  string | Number of max_seq_vnic_failures.  Default value when not specified in API or module is interpreted by Avi Controller as 3. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **persistence_key_rotate_period**  string | Period for rotate app persistence keys job.  Allowed values are 1-1051200.  Special values are 0 - ‘disabled’.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **portal_token**  string | Token used for uploading tech-support to portal.  Field introduced in 16.4.6,17.1.2. |
| **process_locked_useraccounts_timeout_period**  string | Period for process locked user accounts job.  Field introduced in 18.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as 1. |
| **process_pki_profile_timeout_period**  string | Period for process pki profile job.  Field introduced in 18.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as 1440. |
| **query_host_fail**  string | Number of query_host_fail.  Default value when not specified in API or module is interpreted by Avi Controller as 180. |
| **safenet_hsm_version**  string | Version of the safenet package installed on the controller.  Field introduced in 16.5.2,17.2.3. |
| **se_create_timeout**  string | Number of se_create_timeout.  Default value when not specified in API or module is interpreted by Avi Controller as 900. |
| **se_failover_attempt_interval**  string | Interval between attempting failovers to an se.  Default value when not specified in API or module is interpreted by Avi Controller as 300. |
| **se_from_marketplace**  string | This setting decides whether se is to be deployed from the cloud marketplace or to be created by the controller.  The setting is applicable only when byol license is selected.  Enum options - MARKETPLACE, IMAGE.  Field introduced in 18.1.4, 18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as IMAGE. |
| **se_offline_del**  string | Number of se_offline_del.  Default value when not specified in API or module is interpreted by Avi Controller as 172000. |
| **se_vnic_cooldown**  string | Number of se_vnic_cooldown.  Default value when not specified in API or module is interpreted by Avi Controller as 120. |
| **secure_channel_cleanup_timeout**  string | Period for secure channel cleanup job.  Default value when not specified in API or module is interpreted by Avi Controller as 60. |
| **secure_channel_controller_token_timeout**  string | Number of secure_channel_controller_token_timeout.  Default value when not specified in API or module is interpreted by Avi Controller as 60. |
| **secure_channel_se_token_timeout**  string | Number of secure_channel_se_token_timeout.  Default value when not specified in API or module is interpreted by Avi Controller as 60. |
| **seupgrade_fabric_pool_size**  string | Pool size used for all fabric commands during se upgrade.  Default value when not specified in API or module is interpreted by Avi Controller as 20. |
| **seupgrade_segroup_min_dead_timeout**  string | Time to wait before marking segroup upgrade as stuck.  Default value when not specified in API or module is interpreted by Avi Controller as 360. |
| **ssl_certificate_expiry_warning_days**  string | Number of days for ssl certificate expiry warning. |
| **state**  string | The state that should be applied on the entity.  Choices:   - `"absent"` - `"present"` ← (default) |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  Default: `"admin"` |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  Default: `""` |
| **unresponsive_se_reboot**  string | Number of unresponsive_se_reboot.  Default value when not specified in API or module is interpreted by Avi Controller as 300. |
| **upgrade_dns_ttl**  string | Time to account for dns ttl during upgrade.  This is in addition to vs_scalein_timeout_for_upgrade in se_group.  Field introduced in 17.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as 5. |
| **upgrade_lease_time**  string | Number of upgrade_lease_time.  Default value when not specified in API or module is interpreted by Avi Controller as 360. |
| **url**  string | Avi controller URL of the object. |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Unique object identifier of the object. |
| **vnic_op_fail_time**  string | Number of vnic_op_fail_time.  Default value when not specified in API or module is interpreted by Avi Controller as 180. |
| **vs_apic_scaleout_timeout**  string | Time to wait for the scaled out se to become ready before marking the scaleout done, applies to apic configuration only.  Default value when not specified in API or module is interpreted by Avi Controller as 360. |
| **vs_awaiting_se_timeout**  string | Number of vs_awaiting_se_timeout.  Default value when not specified in API or module is interpreted by Avi Controller as 60. |
| **vs_key_rotate_period**  string | Period for rotate vs keys job.  Allowed values are 1-1051200.  Special values are 0 - ‘disabled’.  Default value when not specified in API or module is interpreted by Avi Controller as 360. |
| **vs_scaleout_ready_check_interval**  string | Interval for checking scaleout_ready status while controller is waiting for scaleoutready rpc from the service engine.  Field introduced in 18.2.2.  Default value when not specified in API or module is interpreted by Avi Controller as 60. |
| **vs_se_attach_ip_fail**  string | Time to wait before marking attach ip operation on an se as failed.  Field introduced in 17.2.2.  Default value when not specified in API or module is interpreted by Avi Controller as 600. |
| **vs_se_bootup_fail**  string | Number of vs_se_bootup_fail.  Default value when not specified in API or module is interpreted by Avi Controller as 480. |
| **vs_se_create_fail**  string | Number of vs_se_create_fail.  Default value when not specified in API or module is interpreted by Avi Controller as 1500. |
| **vs_se_ping_fail**  string | Number of vs_se_ping_fail.  Default value when not specified in API or module is interpreted by Avi Controller as 60. |
| **vs_se_vnic_fail**  string | Number of vs_se_vnic_fail.  Default value when not specified in API or module is interpreted by Avi Controller as 300. |
| **vs_se_vnic_ip_fail**  string | Number of vs_se_vnic_ip_fail.  Default value when not specified in API or module is interpreted by Avi Controller as 120. |
| **warmstart_se_reconnect_wait_time**  string | Number of warmstart_se_reconnect_wait_time.  Default value when not specified in API or module is interpreted by Avi Controller as 480. |
| **warmstart_vs_resync_wait_time**  string | Timeout for warmstart vs resync.  Field introduced in 18.1.4, 18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as 300. |

## [Notes](avi_controllerproperties_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_controllerproperties_module.md#id5)

```yaml+jinja
- name: Example to create ControllerProperties object
  community.network.avi_controllerproperties:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_controllerproperties
```

## [Return Values](avi_controllerproperties_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | ControllerProperties (api/controllerproperties) object  Returned: success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
