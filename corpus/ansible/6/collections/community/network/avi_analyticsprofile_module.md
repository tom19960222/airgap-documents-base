---
collection: ansible
version: "6"
title: "community.network.avi_analyticsprofile module – Module for setup of AnalyticsProfile Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/avi_analyticsprofile_module.html
fetched_at: 2026-07-27T17:16:29+00:00
---
# community.network.avi_analyticsprofile module – Module for setup of AnalyticsProfile Avi RESTful Object

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
> see [Requirements](avi_analyticsprofile_module.md#ansible-collections-community-network-avi-analyticsprofile-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_analyticsprofile`.

- [Synopsis](avi_analyticsprofile_module.md#synopsis)
- [Requirements](avi_analyticsprofile_module.md#requirements)
- [Parameters](avi_analyticsprofile_module.md#parameters)
- [Notes](avi_analyticsprofile_module.md#notes)
- [Examples](avi_analyticsprofile_module.md#examples)
- [Return Values](avi_analyticsprofile_module.md#return-values)

## [Synopsis](avi_analyticsprofile_module.md#id1)

- This module is used to configure AnalyticsProfile object
- more examples at <https://github.com/avinetworks/devops>

## [Requirements](avi_analyticsprofile_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_analyticsprofile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **apdex_response_threshold**  string | If a client receives an http response in less than the satisfactory latency threshold, the request is considered satisfied.  It is considered tolerated if it is not satisfied and less than tolerated latency factor multiplied by the satisfactory latency threshold.  Greater than this number and the client’s request is considered frustrated.  Allowed values are 1-30000.  Default value when not specified in API or module is interpreted by Avi Controller as 500. |
| **apdex_response_tolerated_factor**  string | Client tolerated response latency factor.  Client must receive a response within this factor times the satisfactory threshold (apdex_response_threshold) to be considered tolerated.  Allowed values are 1-1000.  Default value when not specified in API or module is interpreted by Avi Controller as 4.0. |
| **apdex_rtt_threshold**  string | Satisfactory client to avi round trip time(rtt).  Allowed values are 1-2000.  Default value when not specified in API or module is interpreted by Avi Controller as 250. |
| **apdex_rtt_tolerated_factor**  string | Tolerated client to avi round trip time(rtt) factor.  It is a multiple of apdex_rtt_tolerated_factor.  Allowed values are 1-1000.  Default value when not specified in API or module is interpreted by Avi Controller as 4.0. |
| **apdex_rum_threshold**  string | If a client is able to load a page in less than the satisfactory latency threshold, the pageload is considered satisfied.  It is considered tolerated if it is greater than satisfied but less than the tolerated latency multiplied by satisfied latency.  Greater than this number and the client’s request is considered frustrated.  A pageload includes the time for dns lookup, download of all http objects, and page render time.  Allowed values are 1-30000.  Default value when not specified in API or module is interpreted by Avi Controller as 5000. |
| **apdex_rum_tolerated_factor**  string | Virtual service threshold factor for tolerated page load time (plt) as multiple of apdex_rum_threshold.  Allowed values are 1-1000.  Default value when not specified in API or module is interpreted by Avi Controller as 4.0. |
| **apdex_server_response_threshold**  string | A server http response is considered satisfied if latency is less than the satisfactory latency threshold.  The response is considered tolerated when it is greater than satisfied but less than the tolerated latency factor \* s_latency.  Greater than this number and the server response is considered frustrated.  Allowed values are 1-30000.  Default value when not specified in API or module is interpreted by Avi Controller as 400. |
| **apdex_server_response_tolerated_factor**  string | Server tolerated response latency factor.  Servermust response within this factor times the satisfactory threshold (apdex_server_response_threshold) to be considered tolerated.  Allowed values are 1-1000.  Default value when not specified in API or module is interpreted by Avi Controller as 4.0. |
| **apdex_server_rtt_threshold**  string | Satisfactory client to avi round trip time(rtt).  Allowed values are 1-2000.  Default value when not specified in API or module is interpreted by Avi Controller as 125. |
| **apdex_server_rtt_tolerated_factor**  string | Tolerated client to avi round trip time(rtt) factor.  It is a multiple of apdex_rtt_tolerated_factor.  Allowed values are 1-1000.  Default value when not specified in API or module is interpreted by Avi Controller as 4.0. |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  Default: `"16.4.4"` |
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
| **client_log_config**  string | Configure which logs are sent to the avi controller from ses and how they are processed. |
| **client_log_streaming_config**  string | Configure to stream logs to an external server.  Field introduced in 17.1.1. |
| **conn_lossy_ooo_threshold**  string | A connection between client and avi is considered lossy when more than this percentage of out of order packets are received.  Allowed values are 1-100.  Default value when not specified in API or module is interpreted by Avi Controller as 50. |
| **conn_lossy_timeo_rexmt_threshold**  string | A connection between client and avi is considered lossy when more than this percentage of packets are retransmitted due to timeout.  Allowed values are 1-100.  Default value when not specified in API or module is interpreted by Avi Controller as 20. |
| **conn_lossy_total_rexmt_threshold**  string | A connection between client and avi is considered lossy when more than this percentage of packets are retransmitted.  Allowed values are 1-100.  Default value when not specified in API or module is interpreted by Avi Controller as 50. |
| **conn_lossy_zero_win_size_event_threshold**  string | A client connection is considered lossy when percentage of times a packet could not be transmitted due to tcp zero window is above this threshold.  Allowed values are 0-100.  Default value when not specified in API or module is interpreted by Avi Controller as 2. |
| **conn_server_lossy_ooo_threshold**  string | A connection between avi and server is considered lossy when more than this percentage of out of order packets are received.  Allowed values are 1-100.  Default value when not specified in API or module is interpreted by Avi Controller as 50. |
| **conn_server_lossy_timeo_rexmt_threshold**  string | A connection between avi and server is considered lossy when more than this percentage of packets are retransmitted due to timeout.  Allowed values are 1-100.  Default value when not specified in API or module is interpreted by Avi Controller as 20. |
| **conn_server_lossy_total_rexmt_threshold**  string | A connection between avi and server is considered lossy when more than this percentage of packets are retransmitted.  Allowed values are 1-100.  Default value when not specified in API or module is interpreted by Avi Controller as 50. |
| **conn_server_lossy_zero_win_size_event_threshold**  string | A server connection is considered lossy when percentage of times a packet could not be transmitted due to tcp zero window is above this threshold.  Allowed values are 0-100.  Default value when not specified in API or module is interpreted by Avi Controller as 2. |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **description**  string | User defined description for the object. |
| **disable_ondemand_metrics**  boolean | Virtual service (vs) metrics are processed only when there is live data traffic on the vs.  In case, vs is idle for a period of time as specified by ondemand_metrics_idle_timeout then metrics processing is suspended for that vs.  Field introduced in 18.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **disable_se_analytics**  boolean | Disable node (service engine) level analytics forvs metrics.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **disable_server_analytics**  boolean | Disable analytics on backend servers.  This may be desired in container environment when there are large number of ephemeral servers.  Additionally, no healthscore of servers is computed when server analytics is disabled.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **disable_vs_analytics**  boolean | Disable virtualservice (frontend) analytics.  This flag disables metrics and healthscore for virtualservice.  Field introduced in 18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **enable_advanced_analytics**  boolean | Enables advanced analytics features like anomaly detection.  If set to false, anomaly computation (and associated rules/events) for vs, pool and server metrics will be disabled.  However, setting it to false reduces cpu and memory requirements for analytics subsystem.  Field introduced in 17.2.13, 18.1.5, 18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **exclude_client_close_before_request_as_error**  boolean | Exclude client closed connection before an http request could be completed from being classified as an error.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **exclude_dns_policy_drop_as_significant**  boolean | Exclude dns policy drops from the list of errors.  Field introduced in 17.2.2.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **exclude_gs_down_as_error**  boolean | Exclude queries to gslb services that are operationally down from the list of errors.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **exclude_http_error_codes**  string | List of http status codes to be excluded from being classified as an error.  Error connections or responses impacts health score, are included as significant logs, and may be classified as part of a dos attack. |
| **exclude_invalid_dns_domain_as_error**  boolean | Exclude dns queries to domains outside the domains configured in the dns application profile from the list of errors.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **exclude_invalid_dns_query_as_error**  boolean | Exclude invalid dns queries from the list of errors.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **exclude_no_dns_record_as_error**  boolean | Exclude queries to domains that did not have configured services/records from the list of errors.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **exclude_no_valid_gs_member_as_error**  boolean | Exclude queries to gslb services that have no available members from the list of errors.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **exclude_persistence_change_as_error**  boolean | Exclude persistence server changed while load balancing’ from the list of errors.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **exclude_server_dns_error_as_error**  boolean | Exclude server dns error response from the list of errors.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **exclude_server_tcp_reset_as_error**  boolean | Exclude server tcp reset from errors.  It is common for applications like ms exchange.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **exclude_sip_error_codes**  string | List of sip status codes to be excluded from being classified as an error.  Field introduced in 17.2.13, 18.1.5, 18.2.1. |
| **exclude_syn_retransmit_as_error**  boolean | Exclude ‘server unanswered syns’ from the list of errors.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **exclude_tcp_reset_as_error**  boolean | Exclude tcp resets by client from the list of potential errors.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **exclude_unsupported_dns_query_as_error**  boolean | Exclude unsupported dns queries from the list of errors.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **healthscore_max_server_limit**  string | Skips health score computation of pool servers when number of servers in a pool is more than this setting.  Allowed values are 0-5000.  Special values are 0- ‘server health score is disabled’.  Field introduced in 17.2.13, 18.1.4.  Default value when not specified in API or module is interpreted by Avi Controller as 20. |
| **hs_event_throttle_window**  string | Time window (in secs) within which only unique health change events should occur.  Default value when not specified in API or module is interpreted by Avi Controller as 1209600. |
| **hs_max_anomaly_penalty**  string | Maximum penalty that may be deducted from health score for anomalies.  Allowed values are 0-100.  Default value when not specified in API or module is interpreted by Avi Controller as 10. |
| **hs_max_resources_penalty**  string | Maximum penalty that may be deducted from health score for high resource utilization.  Allowed values are 0-100.  Default value when not specified in API or module is interpreted by Avi Controller as 25. |
| **hs_max_security_penalty**  string | Maximum penalty that may be deducted from health score based on security assessment.  Allowed values are 0-100.  Default value when not specified in API or module is interpreted by Avi Controller as 100. |
| **hs_min_dos_rate**  string | Dos connection rate below which the dos security assessment will not kick in.  Default value when not specified in API or module is interpreted by Avi Controller as 1000. |
| **hs_performance_boost**  string | Adds free performance score credits to health score.  It can be used for compensating health score for known slow applications.  Allowed values are 0-100.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **hs_pscore_traffic_threshold_l4_client**  string | Threshold number of connections in 5min, below which apdexr, apdexc, rum_apdex, and other network quality metrics are not computed.  Default value when not specified in API or module is interpreted by Avi Controller as 10.0. |
| **hs_pscore_traffic_threshold_l4_server**  string | Threshold number of connections in 5min, below which apdexr, apdexc, rum_apdex, and other network quality metrics are not computed.  Default value when not specified in API or module is interpreted by Avi Controller as 10.0. |
| **hs_security_certscore_expired**  string | Score assigned when the certificate has expired.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 0.0. |
| **hs_security_certscore_gt30d**  string | Score assigned when the certificate expires in more than 30 days.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 5.0. |
| **hs_security_certscore_le07d**  string | Score assigned when the certificate expires in less than or equal to 7 days.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 2.0. |
| **hs_security_certscore_le30d**  string | Score assigned when the certificate expires in less than or equal to 30 days.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 4.0. |
| **hs_security_chain_invalidity_penalty**  string | Penalty for allowing certificates with invalid chain.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 1.0. |
| **hs_security_cipherscore_eq000b**  string | Score assigned when the minimum cipher strength is 0 bits.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 0.0. |
| **hs_security_cipherscore_ge128b**  string | Score assigned when the minimum cipher strength is greater than equal to 128 bits.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 5.0. |
| **hs_security_cipherscore_lt128b**  string | Score assigned when the minimum cipher strength is less than 128 bits.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 3.5. |
| **hs_security_encalgo_score_none**  string | Score assigned when no algorithm is used for encryption.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 0.0. |
| **hs_security_encalgo_score_rc4**  string | Score assigned when rc4 algorithm is used for encryption.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 2.5. |
| **hs_security_hsts_penalty**  string | Penalty for not enabling hsts.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 1.0. |
| **hs_security_nonpfs_penalty**  string | Penalty for allowing non-pfs handshakes.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 1.0. |
| **hs_security_selfsignedcert_penalty**  string | Deprecated.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 1.0. |
| **hs_security_ssl30_score**  string | Score assigned when supporting ssl3.0 encryption protocol.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 3.5. |
| **hs_security_tls10_score**  string | Score assigned when supporting tls1.0 encryption protocol.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 5.0. |
| **hs_security_tls11_score**  string | Score assigned when supporting tls1.1 encryption protocol.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 5.0. |
| **hs_security_tls12_score**  string | Score assigned when supporting tls1.2 encryption protocol.  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 5.0. |
| **hs_security_weak_signature_algo_penalty**  string | Penalty for allowing weak signature algorithm(s).  Allowed values are 0-5.  Default value when not specified in API or module is interpreted by Avi Controller as 1.0. |
| **name**  string / required | The name of the analytics profile. |
| **ondemand_metrics_idle_timeout**  string | This flag sets the time duration of no live data traffic after which virtual service metrics processing is suspended.  It is applicable only when disable_ondemand_metrics is set to false.  Field introduced in 18.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as 1800. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **ranges**  string | List of http status code ranges to be excluded from being classified as an error. |
| **resp_code_block**  string | Block of http response codes to be excluded from being classified as an error.  Enum options - AP_HTTP_RSP_4XX, AP_HTTP_RSP_5XX. |
| **sensitive_log_profile**  string | Rules applied to the http application log for filtering sensitive information.  Field introduced in 17.2.10, 18.1.2. |
| **sip_log_depth**  string | Maximum number of sip messages added in logs for a sip transaction.  By default, this value is 20.  Allowed values are 1-1000.  Field introduced in 17.2.13, 18.1.5, 18.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as 20. |
| **state**  string | The state that should be applied on the entity.  Choices:   - `"absent"` - `"present"` ← (default) |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  Default: `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  Default: `""` |
| **url**  string | Avi controller URL of the object. |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Uuid of the analytics profile. |

## [Notes](avi_analyticsprofile_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_analyticsprofile_module.md#id5)

```yaml+jinja
- name: Create a custom Analytics profile object
  community.network.avi_analyticsprofile:
    controller: '{{ controller }}'
    username: '{{ username }}'
    password: '{{ password }}'
    apdex_response_threshold: 500
    apdex_response_tolerated_factor: 4.0
    apdex_rtt_threshold: 250
    apdex_rtt_tolerated_factor: 4.0
    apdex_rum_threshold: 5000
    apdex_rum_tolerated_factor: 4.0
    apdex_server_response_threshold: 400
    apdex_server_response_tolerated_factor: 4.0
    apdex_server_rtt_threshold: 125
    apdex_server_rtt_tolerated_factor: 4.0
    conn_lossy_ooo_threshold: 50
    conn_lossy_timeo_rexmt_threshold: 20
    conn_lossy_total_rexmt_threshold: 50
    conn_lossy_zero_win_size_event_threshold: 2
    conn_server_lossy_ooo_threshold: 50
    conn_server_lossy_timeo_rexmt_threshold: 20
    conn_server_lossy_total_rexmt_threshold: 50
    conn_server_lossy_zero_win_size_event_threshold: 2
    disable_se_analytics: false
    disable_server_analytics: false
    exclude_client_close_before_request_as_error: false
    exclude_persistence_change_as_error: false
    exclude_server_tcp_reset_as_error: false
    exclude_syn_retransmit_as_error: false
    exclude_tcp_reset_as_error: false
    hs_event_throttle_window: 1209600
    hs_max_anomaly_penalty: 10
    hs_max_resources_penalty: 25
    hs_max_security_penalty: 100
    hs_min_dos_rate: 1000
    hs_performance_boost: 20
    hs_pscore_traffic_threshold_l4_client: 10.0
    hs_pscore_traffic_threshold_l4_server: 10.0
    hs_security_certscore_expired: 0.0
    hs_security_certscore_gt30d: 5.0
    hs_security_certscore_le07d: 2.0
    hs_security_certscore_le30d: 4.0
    hs_security_chain_invalidity_penalty: 1.0
    hs_security_cipherscore_eq000b: 0.0
    hs_security_cipherscore_ge128b: 5.0
    hs_security_cipherscore_lt128b: 3.5
    hs_security_encalgo_score_none: 0.0
    hs_security_encalgo_score_rc4: 2.5
    hs_security_hsts_penalty: 0.0
    hs_security_nonpfs_penalty: 1.0
    hs_security_selfsignedcert_penalty: 1.0
    hs_security_ssl30_score: 3.5
    hs_security_tls10_score: 5.0
    hs_security_tls11_score: 5.0
    hs_security_tls12_score: 5.0
    hs_security_weak_signature_algo_penalty: 1.0
    name: jason-analytics-profile
    tenant_ref: Demo
```

## [Return Values](avi_analyticsprofile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | AnalyticsProfile (api/analyticsprofile) object  Returned: success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
