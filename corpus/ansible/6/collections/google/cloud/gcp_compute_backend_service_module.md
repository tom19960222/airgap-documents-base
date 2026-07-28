---
collection: ansible
version: "6"
title: "google.cloud.gcp_compute_backend_service module – Creates a GCP BackendService"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_compute_backend_service_module.html
fetched_at: 2026-07-27T17:47:50+00:00
---
# google.cloud.gcp_compute_backend_service module – Creates a GCP BackendService

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/google/cloud) (version 1.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_compute_backend_service_module.md#ansible-collections-google-cloud-gcp-compute-backend-service-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_backend_service`.

- [Synopsis](gcp_compute_backend_service_module.md#synopsis)
- [Requirements](gcp_compute_backend_service_module.md#requirements)
- [Parameters](gcp_compute_backend_service_module.md#parameters)
- [Notes](gcp_compute_backend_service_module.md#notes)
- [Examples](gcp_compute_backend_service_module.md#examples)
- [Return Values](gcp_compute_backend_service_module.md#return-values)

## [Synopsis](gcp_compute_backend_service_module.md#id1)

- A Backend Service defines a group of virtual machines that will serve traffic for load balancing. This resource is a global backend service, appropriate for external load balancing or self-managed internal load balancing.
- For managed internal load balancing, use a regional backend service instead.
- Currently self-managed internal load balancing is only available in beta.

## [Requirements](gcp_compute_backend_service_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_backend_service_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **affinity_cookie_ttl_sec**  integer | Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day.  When the load balancing scheme is INTERNAL, this field is not used. |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **backends**  list / elements=dictionary | The set of backends that serve this BackendService. |
| **balancing_mode**  string | Specifies the balancing mode for this backend.  For global HTTP(S) or TCP/SSL load balancing, the default is UTILIZATION. Valid values are UTILIZATION, RATE (for HTTP(S)) and CONNECTION (for TCP/SSL).  Some valid choices include: “UTILIZATION”, “RATE”, “CONNECTION”  Default: `"UTILIZATION"` |
| **capacity_scaler**  string | A multiplier applied to the group’s maximum servicing capacity (based on UTILIZATION, RATE or CONNECTION).  Default value is 1, which means the group will serve up to 100% of its configured capacity (depending on balancingMode). A setting of 0 means the group is completely drained, offering 0% of its available Capacity. Valid range is [0.0,1.0].  Default: `"1.0"` |
| **description**  string | An optional description of this resource.  Provide this property when you create the resource. |
| **group**  string / required | The fully-qualified URL of an Instance Group or Network Endpoint Group resource. In case of instance group this defines the list of instances that serve traffic. Member virtual machine instances from each instance group must live in the same zone as the instance group itself. No two backends in a backend service are allowed to use same Instance Group resource.  For Network Endpoint Groups this defines list of endpoints. All endpoints of Network Endpoint Group must be hosted on instances located in the same zone as the Network Endpoint Group.  Backend services cannot mix Instance Group and Network Endpoint Group backends.  Note that you must specify an Instance Group or Network Endpoint Group resource using the fully-qualified URL, rather than a partial URL. |
| **max_connections**  integer | The max number of simultaneous connections for the group. Can be used with either CONNECTION or UTILIZATION balancing modes.  For CONNECTION mode, either maxConnections or one of maxConnectionsPerInstance or maxConnectionsPerEndpoint, as appropriate for group type, must be set. |
| **max_connections_per_endpoint**  integer | The max number of simultaneous connections that a single backend network endpoint can handle. This is used to calculate the capacity of the group. Can be used in either CONNECTION or UTILIZATION balancing modes.  For CONNECTION mode, either maxConnections or maxConnectionsPerEndpoint must be set. |
| **max_connections_per_instance**  integer | The max number of simultaneous connections that a single backend instance can handle. This is used to calculate the capacity of the group. Can be used in either CONNECTION or UTILIZATION balancing modes.  For CONNECTION mode, either maxConnections or maxConnectionsPerInstance must be set. |
| **max_rate**  integer | The max requests per second (RPS) of the group.  Can be used with either RATE or UTILIZATION balancing modes, but required if RATE mode. For RATE mode, either maxRate or one of maxRatePerInstance or maxRatePerEndpoint, as appropriate for group type, must be set. |
| **max_rate_per_endpoint**  string | The max requests per second (RPS) that a single backend network endpoint can handle. This is used to calculate the capacity of the group. Can be used in either balancing mode. For RATE mode, either maxRate or maxRatePerEndpoint must be set. |
| **max_rate_per_instance**  string | The max requests per second (RPS) that a single backend instance can handle. This is used to calculate the capacity of the group. Can be used in either balancing mode. For RATE mode, either maxRate or maxRatePerInstance must be set. |
| **max_utilization**  string | Used when balancingMode is UTILIZATION. This ratio defines the CPU utilization target for the group. The default is 0.8. Valid range is [0.0, 1.0].  Default: `"0.8"` |
| **cdn_policy**  dictionary | Cloud CDN configuration for this BackendService. |
| **cache_key_policy**  dictionary | The CacheKeyPolicy for this CdnPolicy. |
| **include_host**  boolean | If true requests to different hosts will be cached separately.  Choices:   - `false` - `true` |
| **include_protocol**  boolean | If true, http and https requests will be cached separately.  Choices:   - `false` - `true` |
| **include_query_string**  boolean | If true, include query string parameters in the cache key according to query_string_whitelist and query_string_blacklist. If neither is set, the entire query string will be included.  If false, the query string will be excluded from the cache key entirely.  Choices:   - `false` - `true` |
| **query_string_blacklist**  list / elements=string | Names of query string parameters to exclude in cache keys.  All other parameters will be included. Either specify query_string_whitelist or query_string_blacklist, not both.  ‘&’ and ‘=’ will be percent encoded and not treated as delimiters. |
| **query_string_whitelist**  list / elements=string | Names of query string parameters to include in cache keys.  All other parameters will be excluded. Either specify query_string_whitelist or query_string_blacklist, not both.  ‘&’ and ‘=’ will be percent encoded and not treated as delimiters. |
| **signed_url_cache_max_age_sec**  integer | Maximum number of seconds the response to a signed URL request will be considered fresh, defaults to 1hr (3600s). After this time period, the response will be revalidated before being served.  When serving responses to signed URL requests, Cloud CDN will internally behave as though all responses from this backend had a “Cache-Control: public, max-age=[TTL]” header, regardless of any existing Cache-Control header. The actual headers served in responses will not be altered.  Default: `3600` |
| **circuit_breakers**  dictionary | Settings controlling the volume of connections to a backend service. This field is applicable only when the load_balancing_scheme is set to INTERNAL_SELF_MANAGED. |
| **max_connections**  integer | The maximum number of connections to the backend cluster.  Defaults to 1024.  Default: `1024` |
| **max_pending_requests**  integer | The maximum number of pending requests to the backend cluster.  Defaults to 1024.  Default: `1024` |
| **max_requests**  integer | The maximum number of parallel requests to the backend cluster.  Defaults to 1024.  Default: `1024` |
| **max_requests_per_connection**  integer | Maximum requests for a single backend connection. This parameter is respected by both the HTTP/1.1 and HTTP/2 implementations. If not specified, there is no limit. Setting this parameter to 1 will effectively disable keep alive. |
| **max_retries**  integer | The maximum number of parallel retries to the backend cluster.  Defaults to 3.  Default: `3` |
| **connection_draining**  dictionary | Settings for connection draining . |
| **draining_timeout_sec**  integer | Time for which instance will be drained (not accept new connections, but still work to finish started).  Default: `300` |
| **consistent_hash**  dictionary | Consistent Hash-based load balancing can be used to provide soft session affinity based on HTTP headers, cookies or other properties. This load balancing policy is applicable only for HTTP connections. The affinity to a particular destination host will be lost when one or more hosts are added/removed from the destination service. This field specifies parameters that control consistent hashing. This field only applies if the load_balancing_scheme is set to INTERNAL_SELF_MANAGED. This field is only applicable when locality_lb_policy is set to MAGLEV or RING_HASH. |
| **http_cookie**  dictionary | Hash is based on HTTP Cookie. This field describes a HTTP cookie that will be used as the hash key for the consistent hash load balancer. If the cookie is not present, it will be generated.  This field is applicable if the sessionAffinity is set to HTTP_COOKIE. |
| **name**  string | Name of the cookie. |
| **path**  string | Path to set for the cookie. |
| **ttl**  dictionary | Lifetime of the cookie. |
| **nanos**  integer | Span of time that’s a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 seconds field and a positive nanos field. Must be from 0 to 999,999,999 inclusive. |
| **seconds**  integer / required | Span of time at a resolution of a second.  Must be from 0 to 315,576,000,000 inclusive. |
| **http_header_name**  string | The hash based on the value of the specified header field.  This field is applicable if the sessionAffinity is set to HEADER_FIELD. |
| **minimum_ring_size**  integer | The minimum number of virtual nodes to use for the hash ring.  Larger ring sizes result in more granular load distributions. If the number of hosts in the load balancing pool is larger than the ring size, each host will be assigned a single virtual node.  Defaults to 1024.  Default: `1024` |
| **custom_request_headers**  list / elements=string | Headers that the HTTP/S load balancer should add to proxied requests. |
| **description**  string | An optional description of this resource. |
| **enable_cdn**  boolean | If true, enable Cloud CDN for this BackendService.  Choices:   - `false` - `true` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **health_checks**  list / elements=string | The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently at most one health check can be specified.  A health check must be specified unless the backend service uses an internet or serverless NEG as a backend.  For internal load balancing, a URL to a HealthCheck resource must be specified instead. |
| **iap**  dictionary | Settings for enabling Cloud Identity Aware Proxy. |
| **enabled**  boolean | Enables IAP.  Choices:   - `false` - `true` |
| **oauth2_client_id**  string / required | OAuth2 Client ID for IAP . |
| **oauth2_client_secret**  string / required | OAuth2 Client Secret for IAP . |
| **load_balancing_scheme**  string | Indicates whether the backend service will be used with internal or external load balancing. A backend service created for one type of load balancing cannot be used with the other.  Some valid choices include: “EXTERNAL”, “INTERNAL_SELF_MANAGED”  Default: `"EXTERNAL"` |
| **locality_lb_policy**  string | The load balancing algorithm used within the scope of the locality.  The possible values are - \* ROUND_ROBIN - This is a simple policy in which each healthy backend is selected in round robin order.  \* LEAST_REQUEST - An `1` algorithm which selects two random healthy hosts and picks the host which has fewer active requests.  \* RING_HASH - The ring/modulo hash load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a host from a set of N hosts only affects 1/N of the requests.  \* RANDOM - The load balancer selects a random healthy host.  \* ORIGINAL_DESTINATION - Backend host is selected based on the client connection metadata, i.e., connections are opened to the same address as the destination address of the incoming connection before the connection was redirected to the load balancer.  \* MAGLEV - used as a drop in replacement for the ring hash load balancer.  Maglev is not as stable as ring hash but has faster table lookup build times and host selection times. For more information about Maglev, refer to <https://ai.google/research/pubs/pub44824> This field is applicable only when the load_balancing_scheme is set to INTERNAL_SELF_MANAGED.  Some valid choices include: “ROUND_ROBIN”, “LEAST_REQUEST”, “RING_HASH”, “RANDOM”, “ORIGINAL_DESTINATION”, “MAGLEV” |
| **log_config**  dictionary | This field denotes the logging options for the load balancer traffic served by this backend service.  If logging is enabled, logs will be exported to Stackdriver. |
| **enable**  boolean | Whether to enable logging for the load balancer traffic served by this backend service.  Choices:   - `false` - `true` |
| **sample_rate**  string | This field can only be specified if logging is enabled for this backend service. The value of the field must be in [0, 1]. This configures the sampling rate of requests to the load balancer where 1.0 means all logged requests are reported and 0.0 means no logged requests are reported.  The default value is 1.0. |
| **name**  string / required | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **outlier_detection**  dictionary | Settings controlling eviction of unhealthy hosts from the load balancing pool.  This field is applicable only when the load_balancing_scheme is set to INTERNAL_SELF_MANAGED. |
| **base_ejection_time**  dictionary | The base time that a host is ejected for. The real time is equal to the base time multiplied by the number of times the host has been ejected. Defaults to 30000ms or 30s. |
| **nanos**  integer | Span of time that’s a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive. |
| **seconds**  integer / required | Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. |
| **consecutive_errors**  integer | Number of errors before a host is ejected from the connection pool. When the backend host is accessed over HTTP, a 5xx return code qualifies as an error.  Defaults to 5.  Default: `5` |
| **consecutive_gateway_failure**  integer | The number of consecutive gateway failures (502, 503, 504 status or connection errors that are mapped to one of those status codes) before a consecutive gateway failure ejection occurs. Defaults to 5.  Default: `5` |
| **enforcing_consecutive_errors**  integer | The percentage chance that a host will be actually ejected when an outlier status is detected through consecutive 5xx. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 100.  Default: `100` |
| **enforcing_consecutive_gateway_failure**  integer | The percentage chance that a host will be actually ejected when an outlier status is detected through consecutive gateway failures. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 0. |
| **enforcing_success_rate**  integer | The percentage chance that a host will be actually ejected when an outlier status is detected through success rate statistics. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 100.  Default: `100` |
| **interval**  dictionary | Time interval between ejection sweep analysis. This can result in both new ejections as well as hosts being returned to service. Defaults to 10 seconds. |
| **nanos**  integer | Span of time that’s a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive. |
| **seconds**  integer / required | Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. |
| **max_ejection_percent**  integer | Maximum percentage of hosts in the load balancing pool for the backend service that can be ejected. Defaults to 10%.  Default: `10` |
| **success_rate_minimum_hosts**  integer | The number of hosts in a cluster that must have enough request volume to detect success rate outliers. If the number of hosts is less than this setting, outlier detection via success rate statistics is not performed for any host in the cluster. Defaults to 5.  Default: `5` |
| **success_rate_request_volume**  integer | The minimum number of total requests that must be collected in one interval (as defined by the interval duration above) to include this host in success rate based outlier detection. If the volume is lower than this setting, outlier detection via success rate statistics is not performed for that host. Defaults to 100.  Default: `100` |
| **success_rate_stdev_factor**  integer | This factor is used to determine the ejection threshold for success rate outlier ejection. The ejection threshold is the difference between the mean success rate, and the product of this factor and the standard deviation of the mean success rate: mean - (stdev \* success_rate_stdev_factor). This factor is divided by a thousand to get a double. That is, if the desired factor is 1.9, the runtime value should be 1900. Defaults to 1900.  Default: `1900` |
| **port_name**  string | Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the load balancing scheme is EXTERNAL. |
| **project**  string | The Google Cloud Platform project to use. |
| **protocol**  string | The protocol this BackendService uses to communicate with backends.  The default is HTTP. \*\*NOTE\*\*: HTTP2 is only valid for beta HTTP/2 load balancer types and may result in errors if used with the GA API.  Some valid choices include: “HTTP”, “HTTPS”, “HTTP2”, “TCP”, “SSL”, “GRPC” |
| **scopes**  list / elements=string | Array of scopes to be used |
| **security_policy**  string | The security policy associated with this backend service. |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **session_affinity**  string | Type of session affinity to use. The default is NONE. Session affinity is not applicable if the protocol is UDP.  Some valid choices include: “NONE”, “CLIENT_IP”, “CLIENT_IP_PORT_PROTO”, “CLIENT_IP_PROTO”, “GENERATED_COOKIE”, “HEADER_FIELD”, “HTTP_COOKIE” |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout_sec**  aliases: timeout_seconds  integer | How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is [1, 86400]. |

## [Notes](gcp_compute_backend_service_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/v1/backendServices>
> - Official Documentation: <https://cloud.google.com/compute/docs/load-balancing/http/backend-service>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_backend_service_module.md#id5)

```yaml+jinja
- name: create a instance group
  google.cloud.gcp_compute_instance_group:
    name: instancegroup-backendservice
    zone: us-central1-a
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: instancegroup

- name: create a HTTP health check
  google.cloud.gcp_compute_http_health_check:
    name: httphealthcheck-backendservice
    healthy_threshold: 10
    port: 8080
    timeout_sec: 2
    unhealthy_threshold: 5
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: healthcheck

- name: create a backend service
  google.cloud.gcp_compute_backend_service:
    name: test_object
    backends:
    - group: "{{ instancegroup.selfLink }}"
    health_checks:
    - "{{ healthcheck.selfLink }}"
    enable_cdn: 'true'
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_backend_service_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **affinityCookieTtlSec**  integer | Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day.  When the load balancing scheme is INTERNAL, this field is not used.  Returned: success |
| **backends**  complex | The set of backends that serve this BackendService.  Returned: success |
| **balancingMode**  string | Specifies the balancing mode for this backend.  For global HTTP(S) or TCP/SSL load balancing, the default is UTILIZATION. Valid values are UTILIZATION, RATE (for HTTP(S)) and CONNECTION (for TCP/SSL).  Returned: success |
| **capacityScaler**  string | A multiplier applied to the group’s maximum servicing capacity (based on UTILIZATION, RATE or CONNECTION).  Default value is 1, which means the group will serve up to 100% of its configured capacity (depending on balancingMode). A setting of 0 means the group is completely drained, offering 0% of its available Capacity. Valid range is [0.0,1.0].  Returned: success |
| **description**  string | An optional description of this resource.  Provide this property when you create the resource.  Returned: success |
| **group**  string | The fully-qualified URL of an Instance Group or Network Endpoint Group resource. In case of instance group this defines the list of instances that serve traffic. Member virtual machine instances from each instance group must live in the same zone as the instance group itself. No two backends in a backend service are allowed to use same Instance Group resource.  For Network Endpoint Groups this defines list of endpoints. All endpoints of Network Endpoint Group must be hosted on instances located in the same zone as the Network Endpoint Group.  Backend services cannot mix Instance Group and Network Endpoint Group backends.  Note that you must specify an Instance Group or Network Endpoint Group resource using the fully-qualified URL, rather than a partial URL.  Returned: success |
| **maxConnections**  integer | The max number of simultaneous connections for the group. Can be used with either CONNECTION or UTILIZATION balancing modes.  For CONNECTION mode, either maxConnections or one of maxConnectionsPerInstance or maxConnectionsPerEndpoint, as appropriate for group type, must be set.  Returned: success |
| **maxConnectionsPerEndpoint**  integer | The max number of simultaneous connections that a single backend network endpoint can handle. This is used to calculate the capacity of the group. Can be used in either CONNECTION or UTILIZATION balancing modes.  For CONNECTION mode, either maxConnections or maxConnectionsPerEndpoint must be set.  Returned: success |
| **maxConnectionsPerInstance**  integer | The max number of simultaneous connections that a single backend instance can handle. This is used to calculate the capacity of the group. Can be used in either CONNECTION or UTILIZATION balancing modes.  For CONNECTION mode, either maxConnections or maxConnectionsPerInstance must be set.  Returned: success |
| **maxRate**  integer | The max requests per second (RPS) of the group.  Can be used with either RATE or UTILIZATION balancing modes, but required if RATE mode. For RATE mode, either maxRate or one of maxRatePerInstance or maxRatePerEndpoint, as appropriate for group type, must be set.  Returned: success |
| **maxRatePerEndpoint**  string | The max requests per second (RPS) that a single backend network endpoint can handle. This is used to calculate the capacity of the group. Can be used in either balancing mode. For RATE mode, either maxRate or maxRatePerEndpoint must be set.  Returned: success |
| **maxRatePerInstance**  string | The max requests per second (RPS) that a single backend instance can handle. This is used to calculate the capacity of the group. Can be used in either balancing mode. For RATE mode, either maxRate or maxRatePerInstance must be set.  Returned: success |
| **maxUtilization**  string | Used when balancingMode is UTILIZATION. This ratio defines the CPU utilization target for the group. The default is 0.8. Valid range is [0.0, 1.0].  Returned: success |
| **cdnPolicy**  complex | Cloud CDN configuration for this BackendService.  Returned: success |
| **cacheKeyPolicy**  complex | The CacheKeyPolicy for this CdnPolicy.  Returned: success |
| **includeHost**  boolean | If true requests to different hosts will be cached separately.  Returned: success |
| **includeProtocol**  boolean | If true, http and https requests will be cached separately.  Returned: success |
| **includeQueryString**  boolean | If true, include query string parameters in the cache key according to query_string_whitelist and query_string_blacklist. If neither is set, the entire query string will be included.  If false, the query string will be excluded from the cache key entirely.  Returned: success |
| **queryStringBlacklist**  list / elements=string | Names of query string parameters to exclude in cache keys.  All other parameters will be included. Either specify query_string_whitelist or query_string_blacklist, not both.  ‘&’ and ‘=’ will be percent encoded and not treated as delimiters.  Returned: success |
| **queryStringWhitelist**  list / elements=string | Names of query string parameters to include in cache keys.  All other parameters will be excluded. Either specify query_string_whitelist or query_string_blacklist, not both.  ‘&’ and ‘=’ will be percent encoded and not treated as delimiters.  Returned: success |
| **signedUrlCacheMaxAgeSec**  integer | Maximum number of seconds the response to a signed URL request will be considered fresh, defaults to 1hr (3600s). After this time period, the response will be revalidated before being served.  When serving responses to signed URL requests, Cloud CDN will internally behave as though all responses from this backend had a “Cache-Control: public, max-age=[TTL]” header, regardless of any existing Cache-Control header. The actual headers served in responses will not be altered.  Returned: success |
| **circuitBreakers**  complex | Settings controlling the volume of connections to a backend service. This field is applicable only when the load_balancing_scheme is set to INTERNAL_SELF_MANAGED.  Returned: success |
| **maxConnections**  integer | The maximum number of connections to the backend cluster.  Defaults to 1024.  Returned: success |
| **maxPendingRequests**  integer | The maximum number of pending requests to the backend cluster.  Defaults to 1024.  Returned: success |
| **maxRequests**  integer | The maximum number of parallel requests to the backend cluster.  Defaults to 1024.  Returned: success |
| **maxRequestsPerConnection**  integer | Maximum requests for a single backend connection. This parameter is respected by both the HTTP/1.1 and HTTP/2 implementations. If not specified, there is no limit. Setting this parameter to 1 will effectively disable keep alive.  Returned: success |
| **maxRetries**  integer | The maximum number of parallel retries to the backend cluster.  Defaults to 3.  Returned: success |
| **connectionDraining**  complex | Settings for connection draining .  Returned: success |
| **drainingTimeoutSec**  integer | Time for which instance will be drained (not accept new connections, but still work to finish started).  Returned: success |
| **consistentHash**  complex | Consistent Hash-based load balancing can be used to provide soft session affinity based on HTTP headers, cookies or other properties. This load balancing policy is applicable only for HTTP connections. The affinity to a particular destination host will be lost when one or more hosts are added/removed from the destination service. This field specifies parameters that control consistent hashing. This field only applies if the load_balancing_scheme is set to INTERNAL_SELF_MANAGED. This field is only applicable when locality_lb_policy is set to MAGLEV or RING_HASH.  Returned: success |
| **httpCookie**  complex | Hash is based on HTTP Cookie. This field describes a HTTP cookie that will be used as the hash key for the consistent hash load balancer. If the cookie is not present, it will be generated.  This field is applicable if the sessionAffinity is set to HTTP_COOKIE.  Returned: success |
| **name**  string | Name of the cookie.  Returned: success |
| **path**  string | Path to set for the cookie.  Returned: success |
| **ttl**  complex | Lifetime of the cookie.  Returned: success |
| **nanos**  integer | Span of time that’s a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 seconds field and a positive nanos field. Must be from 0 to 999,999,999 inclusive.  Returned: success |
| **seconds**  integer | Span of time at a resolution of a second.  Must be from 0 to 315,576,000,000 inclusive.  Returned: success |
| **httpHeaderName**  string | The hash based on the value of the specified header field.  This field is applicable if the sessionAffinity is set to HEADER_FIELD.  Returned: success |
| **minimumRingSize**  integer | The minimum number of virtual nodes to use for the hash ring.  Larger ring sizes result in more granular load distributions. If the number of hosts in the load balancing pool is larger than the ring size, each host will be assigned a single virtual node.  Defaults to 1024.  Returned: success |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  Returned: success |
| **customRequestHeaders**  list / elements=string | Headers that the HTTP/S load balancer should add to proxied requests.  Returned: success |
| **description**  string | An optional description of this resource.  Returned: success |
| **enableCDN**  boolean | If true, enable Cloud CDN for this BackendService.  Returned: success |
| **fingerprint**  string | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.  Returned: success |
| **healthChecks**  list / elements=string | The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently at most one health check can be specified.  A health check must be specified unless the backend service uses an internet or serverless NEG as a backend.  For internal load balancing, a URL to a HealthCheck resource must be specified instead.  Returned: success |
| **iap**  complex | Settings for enabling Cloud Identity Aware Proxy.  Returned: success |
| **enabled**  boolean | Enables IAP.  Returned: success |
| **oauth2ClientId**  string | OAuth2 Client ID for IAP .  Returned: success |
| **oauth2ClientSecret**  string | OAuth2 Client Secret for IAP .  Returned: success |
| **oauth2ClientSecretSha256**  string | OAuth2 Client Secret SHA-256 for IAP .  Returned: success |
| **id**  integer | The unique identifier for the resource.  Returned: success |
| **loadBalancingScheme**  string | Indicates whether the backend service will be used with internal or external load balancing. A backend service created for one type of load balancing cannot be used with the other.  Returned: success |
| **localityLbPolicy**  string | The load balancing algorithm used within the scope of the locality.  The possible values are - \* ROUND_ROBIN - This is a simple policy in which each healthy backend is selected in round robin order.  \* LEAST_REQUEST - An `1` algorithm which selects two random healthy hosts and picks the host which has fewer active requests.  \* RING_HASH - The ring/modulo hash load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a host from a set of N hosts only affects 1/N of the requests.  \* RANDOM - The load balancer selects a random healthy host.  \* ORIGINAL_DESTINATION - Backend host is selected based on the client connection metadata, i.e., connections are opened to the same address as the destination address of the incoming connection before the connection was redirected to the load balancer.  \* MAGLEV - used as a drop in replacement for the ring hash load balancer.  Maglev is not as stable as ring hash but has faster table lookup build times and host selection times. For more information about Maglev, refer to <https://ai.google/research/pubs/pub44824> This field is applicable only when the load_balancing_scheme is set to INTERNAL_SELF_MANAGED.  Returned: success |
| **logConfig**  complex | This field denotes the logging options for the load balancer traffic served by this backend service.  If logging is enabled, logs will be exported to Stackdriver.  Returned: success |
| **enable**  boolean | Whether to enable logging for the load balancer traffic served by this backend service.  Returned: success |
| **sampleRate**  string | This field can only be specified if logging is enabled for this backend service. The value of the field must be in [0, 1]. This configures the sampling rate of requests to the load balancer where 1.0 means all logged requests are reported and 0.0 means no logged requests are reported.  The default value is 1.0.  Returned: success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  Returned: success |
| **outlierDetection**  complex | Settings controlling eviction of unhealthy hosts from the load balancing pool.  This field is applicable only when the load_balancing_scheme is set to INTERNAL_SELF_MANAGED.  Returned: success |
| **baseEjectionTime**  complex | The base time that a host is ejected for. The real time is equal to the base time multiplied by the number of times the host has been ejected. Defaults to 30000ms or 30s.  Returned: success |
| **nanos**  integer | Span of time that’s a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  Returned: success |
| **seconds**  integer | Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.  Returned: success |
| **consecutiveErrors**  integer | Number of errors before a host is ejected from the connection pool. When the backend host is accessed over HTTP, a 5xx return code qualifies as an error.  Defaults to 5.  Returned: success |
| **consecutiveGatewayFailure**  integer | The number of consecutive gateway failures (502, 503, 504 status or connection errors that are mapped to one of those status codes) before a consecutive gateway failure ejection occurs. Defaults to 5.  Returned: success |
| **enforcingConsecutiveErrors**  integer | The percentage chance that a host will be actually ejected when an outlier status is detected through consecutive 5xx. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 100.  Returned: success |
| **enforcingConsecutiveGatewayFailure**  integer | The percentage chance that a host will be actually ejected when an outlier status is detected through consecutive gateway failures. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 0.  Returned: success |
| **enforcingSuccessRate**  integer | The percentage chance that a host will be actually ejected when an outlier status is detected through success rate statistics. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 100.  Returned: success |
| **interval**  complex | Time interval between ejection sweep analysis. This can result in both new ejections as well as hosts being returned to service. Defaults to 10 seconds.  Returned: success |
| **nanos**  integer | Span of time that’s a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  Returned: success |
| **seconds**  integer | Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.  Returned: success |
| **maxEjectionPercent**  integer | Maximum percentage of hosts in the load balancing pool for the backend service that can be ejected. Defaults to 10%.  Returned: success |
| **successRateMinimumHosts**  integer | The number of hosts in a cluster that must have enough request volume to detect success rate outliers. If the number of hosts is less than this setting, outlier detection via success rate statistics is not performed for any host in the cluster. Defaults to 5.  Returned: success |
| **successRateRequestVolume**  integer | The minimum number of total requests that must be collected in one interval (as defined by the interval duration above) to include this host in success rate based outlier detection. If the volume is lower than this setting, outlier detection via success rate statistics is not performed for that host. Defaults to 100.  Returned: success |
| **successRateStdevFactor**  integer | This factor is used to determine the ejection threshold for success rate outlier ejection. The ejection threshold is the difference between the mean success rate, and the product of this factor and the standard deviation of the mean success rate: mean - (stdev \* success_rate_stdev_factor). This factor is divided by a thousand to get a double. That is, if the desired factor is 1.9, the runtime value should be 1900. Defaults to 1900.  Returned: success |
| **portName**  string | Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the load balancing scheme is EXTERNAL.  Returned: success |
| **protocol**  string | The protocol this BackendService uses to communicate with backends.  The default is HTTP. \*\*NOTE\*\*: HTTP2 is only valid for beta HTTP/2 load balancer types and may result in errors if used with the GA API.  Returned: success |
| **securityPolicy**  string | The security policy associated with this backend service.  Returned: success |
| **sessionAffinity**  string | Type of session affinity to use. The default is NONE. Session affinity is not applicable if the protocol is UDP.  Returned: success |
| **timeoutSec**  integer | How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is [1, 86400].  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
