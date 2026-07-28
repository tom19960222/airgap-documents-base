---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_health_check module – Creates a GCP HealthCheck"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_health_check_module.html
fetched_at: 2026-07-28T02:32:06+00:00
---
# google.cloud.gcp_compute_health_check module – Creates a GCP HealthCheck

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/ui/repo/published/google/cloud/) (version 1.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_compute_health_check_module.md#ansible-collections-google-cloud-gcp-compute-health-check-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_health_check`.

- [Synopsis](gcp_compute_health_check_module.md#synopsis)
- [Requirements](gcp_compute_health_check_module.md#requirements)
- [Parameters](gcp_compute_health_check_module.md#parameters)
- [Notes](gcp_compute_health_check_module.md#notes)
- [Examples](gcp_compute_health_check_module.md#examples)
- [Return Values](gcp_compute_health_check_module.md#return-values)

## [Synopsis](gcp_compute_health_check_module.md#id1)

- Health Checks determine whether instances are responsive and able to do work.
- They are an important part of a comprehensive load balancing configuration, as they enable monitoring instances behind load balancers.
- Health Checks poll instances at a specified interval. Instances that do not respond successfully to some number of probes in a row are marked as unhealthy. No new connections are sent to unhealthy instances, though existing connections will continue. The health check will continue to poll unhealthy instances. If an instance later responds successfully to some number of consecutive probes, it is marked healthy again and can receive new connections.
- ~>\*\*NOTE\*\*: Legacy HTTP(S) health checks must be used for target pool-based network load balancers. See the [official guide](<https://cloud.google.com/load-balancing/docs/health-check-concepts#selecting_hc>) for choosing a type of health check.

## [Requirements](gcp_compute_health_check_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_health_check_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **check_interval_sec**  integer | How often (in seconds) to send a health check. The default value is 5 seconds.  **Default:** `5` |
| **description**  string | An optional description of this resource. Provide this property when you create the resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **grpc_health_check**  dictionary | A nested object resource. |
| **grpc_service_name**  string | The gRPC service name for the health check.  The value of grpcServiceName has the following meanings by convention: - Empty serviceName means the overall status of all services at the backend.   - Non-empty serviceName means the health of that gRPC service, as defined by the owner of the service.   The grpcServiceName can only be ASCII. |
| **port**  integer | The port number for the health check request.  Must be specified if portName and portSpecification are not set or if port_specification is USE_FIXED_PORT. Valid values are 1 through 65535. |
| **port_name**  string | Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. |
| **port_specification**  string | Specifies how port is selected for health checking, can be one of the following values: \* `USE_FIXED_PORT`: The port number in `port` is used for health checking.  \* `USE_NAMED_PORT`: The `portName` is used for health checking.  \* `USE_SERVING_PORT`: For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking.  If not specified, gRPC health check follows behavior specified in `port` and `portName` fields.  Some valid choices include: “USE_FIXED_PORT”, “USE_NAMED_PORT”, “USE_SERVING_PORT” |
| **healthy_threshold**  integer | A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.  **Default:** `2` |
| **http2_health_check**  dictionary | A nested object resource. |
| **host**  string | The value of the host header in the HTTP2 health check request.  If left empty (default value), the public IP on behalf of which this health check is performed will be used. |
| **port**  integer | The TCP port number for the HTTP2 health check request.  The default value is 443. |
| **port_name**  string | Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. |
| **port_specification**  string | Specifies how port is selected for health checking, can be one of the following values: \* `USE_FIXED_PORT`: The port number in `port` is used for health checking.  \* `USE_NAMED_PORT`: The `portName` is used for health checking.  \* `USE_SERVING_PORT`: For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking.  If not specified, HTTP2 health check follows behavior specified in `port` and `portName` fields.  Some valid choices include: “USE_FIXED_PORT”, “USE_NAMED_PORT”, “USE_SERVING_PORT” |
| **proxy_header**  string | Specifies the type of proxy header to append before sending data to the backend.  Some valid choices include: “NONE”, “PROXY_V1”  **Default:** `"NONE"` |
| **request_path**  string | The request path of the HTTP2 health check request.  The default value is /.  **Default:** `"/"` |
| **response**  string | The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII. |
| **http_health_check**  dictionary | A nested object resource. |
| **host**  string | The value of the host header in the HTTP health check request.  If left empty (default value), the public IP on behalf of which this health check is performed will be used. |
| **port**  integer | The TCP port number for the HTTP health check request.  The default value is 80. |
| **port_name**  string | Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. |
| **port_specification**  string | Specifies how port is selected for health checking, can be one of the following values: \* `USE_FIXED_PORT`: The port number in `port` is used for health checking.  \* `USE_NAMED_PORT`: The `portName` is used for health checking.  \* `USE_SERVING_PORT`: For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking.  If not specified, HTTP health check follows behavior specified in `port` and `portName` fields.  Some valid choices include: “USE_FIXED_PORT”, “USE_NAMED_PORT”, “USE_SERVING_PORT” |
| **proxy_header**  string | Specifies the type of proxy header to append before sending data to the backend.  Some valid choices include: “NONE”, “PROXY_V1”  **Default:** `"NONE"` |
| **request_path**  string | The request path of the HTTP health check request.  The default value is /.  **Default:** `"/"` |
| **response**  string | The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII. |
| **https_health_check**  dictionary | A nested object resource. |
| **host**  string | The value of the host header in the HTTPS health check request.  If left empty (default value), the public IP on behalf of which this health check is performed will be used. |
| **port**  integer | The TCP port number for the HTTPS health check request.  The default value is 443. |
| **port_name**  string | Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. |
| **port_specification**  string | Specifies how port is selected for health checking, can be one of the following values: \* `USE_FIXED_PORT`: The port number in `port` is used for health checking.  \* `USE_NAMED_PORT`: The `portName` is used for health checking.  \* `USE_SERVING_PORT`: For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking.  If not specified, HTTPS health check follows behavior specified in `port` and `portName` fields.  Some valid choices include: “USE_FIXED_PORT”, “USE_NAMED_PORT”, “USE_SERVING_PORT” |
| **proxy_header**  string | Specifies the type of proxy header to append before sending data to the backend.  Some valid choices include: “NONE”, “PROXY_V1”  **Default:** `"NONE"` |
| **request_path**  string | The request path of the HTTPS health check request.  The default value is /.  **Default:** `"/"` |
| **response**  string | The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII. |
| **log_config**  dictionary | Configure logging on this health check. |
| **enable**  boolean | Indicates whether or not to export logs. This is false by default, which means no health check logging will be done.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **ssl_health_check**  dictionary | A nested object resource. |
| **port**  integer | The TCP port number for the SSL health check request.  The default value is 443. |
| **port_name**  string | Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. |
| **port_specification**  string | Specifies how port is selected for health checking, can be one of the following values: \* `USE_FIXED_PORT`: The port number in `port` is used for health checking.  \* `USE_NAMED_PORT`: The `portName` is used for health checking.  \* `USE_SERVING_PORT`: For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking.  If not specified, SSL health check follows behavior specified in `port` and `portName` fields.  Some valid choices include: “USE_FIXED_PORT”, “USE_NAMED_PORT”, “USE_SERVING_PORT” |
| **proxy_header**  string | Specifies the type of proxy header to append before sending data to the backend.  Some valid choices include: “NONE”, “PROXY_V1”  **Default:** `"NONE"` |
| **request**  string | The application data to send once the SSL connection has been established (default value is empty). If both request and response are empty, the connection establishment alone will indicate health. The request data can only be ASCII. |
| **response**  string | The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tcp_health_check**  dictionary | A nested object resource. |
| **port**  integer | The TCP port number for the TCP health check request.  The default value is 443. |
| **port_name**  string | Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. |
| **port_specification**  string | Specifies how port is selected for health checking, can be one of the following values: \* `USE_FIXED_PORT`: The port number in `port` is used for health checking.  \* `USE_NAMED_PORT`: The `portName` is used for health checking.  \* `USE_SERVING_PORT`: For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking.  If not specified, TCP health check follows behavior specified in `port` and `portName` fields.  Some valid choices include: “USE_FIXED_PORT”, “USE_NAMED_PORT”, “USE_SERVING_PORT” |
| **proxy_header**  string | Specifies the type of proxy header to append before sending data to the backend.  Some valid choices include: “NONE”, “PROXY_V1”  **Default:** `"NONE"` |
| **request**  string | The application data to send once the TCP connection has been established (default value is empty). If both request and response are empty, the connection establishment alone will indicate health. The request data can only be ASCII. |
| **response**  string | The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII. |
| **timeout_sec**  aliases: timeout_seconds  integer | How long (in seconds) to wait before claiming failure.  The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec.  **Default:** `5` |
| **type**  string | Specifies the type of the healthCheck, either TCP, SSL, HTTP or HTTPS. If not specified, the default is TCP. Exactly one of the protocol-specific health check field must be specified, which must match type field.  Some valid choices include: “TCP”, “SSL”, “HTTP”, “HTTPS”, “HTTP2” |
| **unhealthy_threshold**  integer | A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.  **Default:** `2` |

## [Notes](gcp_compute_health_check_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/rest/v1/healthChecks>
> - Official Documentation: <https://cloud.google.com/load-balancing/docs/health-checks>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_health_check_module.md#id5)

```yaml+jinja
- name: create a health check
  google.cloud.gcp_compute_health_check:
    name: test_object
    type: TCP
    tcp_health_check:
      port_name: service-health
      request: ping
      response: pong
    healthy_threshold: 10
    timeout_sec: 2
    unhealthy_threshold: 5
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_health_check_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **checkIntervalSec**  integer | How often (in seconds) to send a health check. The default value is 5 seconds.  **Returned:** success |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **description**  string | An optional description of this resource. Provide this property when you create the resource.  **Returned:** success |
| **grpcHealthCheck**  complex | A nested object resource.  **Returned:** success |
| **grpcServiceName**  string | The gRPC service name for the health check.  The value of grpcServiceName has the following meanings by convention: - Empty serviceName means the overall status of all services at the backend.   - Non-empty serviceName means the health of that gRPC service, as defined by the owner of the service.   The grpcServiceName can only be ASCII.  **Returned:** success |
| **port**  integer | The port number for the health check request.  Must be specified if portName and portSpecification are not set or if port_specification is USE_FIXED_PORT. Valid values are 1 through 65535.  **Returned:** success |
| **portName**  string | Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence.  **Returned:** success |
| **portSpecification**  string | Specifies how port is selected for health checking, can be one of the following values: \* `USE_FIXED_PORT`: The port number in `port` is used for health checking.  \* `USE_NAMED_PORT`: The `portName` is used for health checking.  \* `USE_SERVING_PORT`: For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking.  If not specified, gRPC health check follows behavior specified in `port` and `portName` fields.  **Returned:** success |
| **healthyThreshold**  integer | A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.  **Returned:** success |
| **http2HealthCheck**  complex | A nested object resource.  **Returned:** success |
| **host**  string | The value of the host header in the HTTP2 health check request.  If left empty (default value), the public IP on behalf of which this health check is performed will be used.  **Returned:** success |
| **port**  integer | The TCP port number for the HTTP2 health check request.  The default value is 443.  **Returned:** success |
| **portName**  string | Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence.  **Returned:** success |
| **portSpecification**  string | Specifies how port is selected for health checking, can be one of the following values: \* `USE_FIXED_PORT`: The port number in `port` is used for health checking.  \* `USE_NAMED_PORT`: The `portName` is used for health checking.  \* `USE_SERVING_PORT`: For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking.  If not specified, HTTP2 health check follows behavior specified in `port` and `portName` fields.  **Returned:** success |
| **proxyHeader**  string | Specifies the type of proxy header to append before sending data to the backend.  **Returned:** success |
| **requestPath**  string | The request path of the HTTP2 health check request.  The default value is /.  **Returned:** success |
| **response**  string | The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII.  **Returned:** success |
| **httpHealthCheck**  complex | A nested object resource.  **Returned:** success |
| **host**  string | The value of the host header in the HTTP health check request.  If left empty (default value), the public IP on behalf of which this health check is performed will be used.  **Returned:** success |
| **port**  integer | The TCP port number for the HTTP health check request.  The default value is 80.  **Returned:** success |
| **portName**  string | Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence.  **Returned:** success |
| **portSpecification**  string | Specifies how port is selected for health checking, can be one of the following values: \* `USE_FIXED_PORT`: The port number in `port` is used for health checking.  \* `USE_NAMED_PORT`: The `portName` is used for health checking.  \* `USE_SERVING_PORT`: For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking.  If not specified, HTTP health check follows behavior specified in `port` and `portName` fields.  **Returned:** success |
| **proxyHeader**  string | Specifies the type of proxy header to append before sending data to the backend.  **Returned:** success |
| **requestPath**  string | The request path of the HTTP health check request.  The default value is /.  **Returned:** success |
| **response**  string | The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII.  **Returned:** success |
| **httpsHealthCheck**  complex | A nested object resource.  **Returned:** success |
| **host**  string | The value of the host header in the HTTPS health check request.  If left empty (default value), the public IP on behalf of which this health check is performed will be used.  **Returned:** success |
| **port**  integer | The TCP port number for the HTTPS health check request.  The default value is 443.  **Returned:** success |
| **portName**  string | Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence.  **Returned:** success |
| **portSpecification**  string | Specifies how port is selected for health checking, can be one of the following values: \* `USE_FIXED_PORT`: The port number in `port` is used for health checking.  \* `USE_NAMED_PORT`: The `portName` is used for health checking.  \* `USE_SERVING_PORT`: For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking.  If not specified, HTTPS health check follows behavior specified in `port` and `portName` fields.  **Returned:** success |
| **proxyHeader**  string | Specifies the type of proxy header to append before sending data to the backend.  **Returned:** success |
| **requestPath**  string | The request path of the HTTPS health check request.  The default value is /.  **Returned:** success |
| **response**  string | The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII.  **Returned:** success |
| **id**  integer | The unique identifier for the resource. This identifier is defined by the server.  **Returned:** success |
| **logConfig**  complex | Configure logging on this health check.  **Returned:** success |
| **enable**  boolean | Indicates whether or not to export logs. This is false by default, which means no health check logging will be done.  **Returned:** success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **sslHealthCheck**  complex | A nested object resource.  **Returned:** success |
| **port**  integer | The TCP port number for the SSL health check request.  The default value is 443.  **Returned:** success |
| **portName**  string | Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence.  **Returned:** success |
| **portSpecification**  string | Specifies how port is selected for health checking, can be one of the following values: \* `USE_FIXED_PORT`: The port number in `port` is used for health checking.  \* `USE_NAMED_PORT`: The `portName` is used for health checking.  \* `USE_SERVING_PORT`: For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking.  If not specified, SSL health check follows behavior specified in `port` and `portName` fields.  **Returned:** success |
| **proxyHeader**  string | Specifies the type of proxy header to append before sending data to the backend.  **Returned:** success |
| **request**  string | The application data to send once the SSL connection has been established (default value is empty). If both request and response are empty, the connection establishment alone will indicate health. The request data can only be ASCII.  **Returned:** success |
| **response**  string | The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII.  **Returned:** success |
| **tcpHealthCheck**  complex | A nested object resource.  **Returned:** success |
| **port**  integer | The TCP port number for the TCP health check request.  The default value is 443.  **Returned:** success |
| **portName**  string | Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence.  **Returned:** success |
| **portSpecification**  string | Specifies how port is selected for health checking, can be one of the following values: \* `USE_FIXED_PORT`: The port number in `port` is used for health checking.  \* `USE_NAMED_PORT`: The `portName` is used for health checking.  \* `USE_SERVING_PORT`: For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking.  If not specified, TCP health check follows behavior specified in `port` and `portName` fields.  **Returned:** success |
| **proxyHeader**  string | Specifies the type of proxy header to append before sending data to the backend.  **Returned:** success |
| **request**  string | The application data to send once the TCP connection has been established (default value is empty). If both request and response are empty, the connection establishment alone will indicate health. The request data can only be ASCII.  **Returned:** success |
| **response**  string | The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII.  **Returned:** success |
| **timeoutSec**  integer | How long (in seconds) to wait before claiming failure.  The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec.  **Returned:** success |
| **type**  string | Specifies the type of the healthCheck, either TCP, SSL, HTTP or HTTPS. If not specified, the default is TCP. Exactly one of the protocol-specific health check field must be specified, which must match type field.  **Returned:** success |
| **unhealthyThreshold**  integer | A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
