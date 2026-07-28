---
collection: ansible
version: "6"
title: "hetzner.hcloud.hcloud_load_balancer_service module – Create and manage the services of cloud Load Balancers on the Hetzner Cloud."
source_url: https://docs.ansible.com/projects/ansible/6/collections/hetzner/hcloud/hcloud_load_balancer_service_module.html
fetched_at: 2026-07-27T17:49:43+00:00
---
# hetzner.hcloud.hcloud_load_balancer_service module – Create and manage the services of cloud Load Balancers on the Hetzner Cloud.

> **Note:**
>
> This module is part of the [hetzner.hcloud collection](https://galaxy.ansible.com/hetzner/hcloud) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hetzner.hcloud`.
> You need further requirements to be able to use this module,
> see [Requirements](hcloud_load_balancer_service_module.md#ansible-collections-hetzner-hcloud-hcloud-load-balancer-service-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_load_balancer_service`.

New in hetzner.hcloud 0.1.0

- [Synopsis](hcloud_load_balancer_service_module.md#synopsis)
- [Requirements](hcloud_load_balancer_service_module.md#requirements)
- [Parameters](hcloud_load_balancer_service_module.md#parameters)
- [See Also](hcloud_load_balancer_service_module.md#see-also)
- [Examples](hcloud_load_balancer_service_module.md#examples)
- [Return Values](hcloud_load_balancer_service_module.md#return-values)

## [Synopsis](hcloud_load_balancer_service_module.md#id1)

- Create, update and manage the services of cloud Load Balancers on the Hetzner Cloud.

## [Requirements](hcloud_load_balancer_service_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.0.0
- hcloud-python >= 1.8.1

## [Parameters](hcloud_load_balancer_service_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **destination_port**  integer | The port traffic is forwarded to, i.e. the port the targets are listening and accepting connections on.  Required if services does not exist and protocol is tcp. |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  Default: `"https://api.hetzner.cloud/v1"` |
| **health_check**  dictionary | Configuration for health checks |
| **http**  dictionary | Additional Configuration of health checks with protocol http/https |
| **domain**  string | Domain we will set within the HTTP HOST header |
| **path**  string | Path we will try to access |
| **response**  string | Response we expect, if response is not within the health check response the target is unhealthy |
| **status_codes**  list / elements=string | List of HTTP status codes we expect to get when we perform the health check. |
| **tls**  boolean | Verify the TLS certificate, only available if health check protocol is https  Choices:   - `false` ← (default) - `true` |
| **interval**  integer | Interval of health checks, in seconds |
| **port**  integer | Port the health check will be performed on |
| **protocol**  string | Protocol the health checks will be performed over  Choices:   - `"http"` - `"https"` - `"tcp"` |
| **retries**  integer | Number of retries until a target is marked as unhealthy |
| **timeout**  integer | Timeout of health checks, in seconds |
| **http**  dictionary | Configuration for HTTP and HTTPS services |
| **certificates**  list / elements=string | List of Names or IDs of certificates |
| **cookie_lifetime**  integer | Lifetime of the cookie which will be set when you enable sticky sessions, in seconds |
| **cookie_name**  string | Name of the cookie which will be set when you enable sticky sessions |
| **redirect_http**  boolean | Redirect Traffic from Port 80 to Port 443, only available if protocol is https  Choices:   - `false` ← (default) - `true` |
| **sticky_sessions**  boolean | Enable or disable sticky_sessions  Choices:   - `false` ← (default) - `true` |
| **listen_port**  integer / required | The port the service listens on, i.e. the port users can connect to. |
| **load_balancer**  string / required | The Name of the Hetzner Cloud Load Balancer the service belongs to |
| **protocol**  string | Protocol of the service.  Required if Load Balancer does not exist.  Choices:   - `"http"` - `"https"` - `"tcp"` |
| **proxyprotocol**  boolean | Enable the PROXY protocol.  Choices:   - `false` ← (default) - `true` |
| **state**  string | State of the Load Balancer.  Choices:   - `"absent"` - `"present"` ← (default) |

## [See Also](hcloud_load_balancer_service_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_load_balancer_service_module.md#id5)

```yaml+jinja
- name: Create a basic Load Balancer service with Port 80
  hcloud_load_balancer_service:
    load_balancer: my-load-balancer
    protocol: http
    listen_port: 80
    state: present

- name: Ensure the Load Balancer is absent (remove if needed)
  hcloud_load_balancer_service:
    load_balancer: my-Load Balancer
    protocol: http
    listen_port: 80
    state: absent
```

## [Return Values](hcloud_load_balancer_service_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_load_balancer_service**  complex | The Load Balancer service instance  Returned: Always |
| **destination_port**  integer | The port traffic is forwarded to, i.e. the port the targets are listening and accepting connections on.  Returned: always  Sample: `80` |
| **health_check**  complex | Configuration for health checks  Returned: always |
| **http**  complex | Additional Configuration of health checks with protocol http/https  Returned: always |
| **domain**  string | Domain we will set within the HTTP HOST header  Returned: always  Sample: `"example.com"` |
| **path**  string | Path we will try to access  Returned: always  Sample: `"/"` |
| **response**  string | Response we expect, if response is not within the health check response the target is unhealthy  Returned: always |
| **status_codes**  list / elements=string | List of HTTP status codes we expect to get when we perform the health check.  Returned: always  Sample: `["2??", "3??"]` |
| **tls**  boolean | Verify the TLS certificate, only available if health check protocol is https  Returned: always  Sample: `false` |
| **interval**  integer | Interval of health checks, in seconds  Returned: always  Sample: `15` |
| **port**  integer | Port the health check will be performed on  Returned: always  Sample: `80` |
| **protocol**  string | Protocol the health checks will be performed over  Returned: always  Sample: `"http"` |
| **retries**  integer | Number of retries until a target is marked as unhealthy  Returned: always  Sample: `3` |
| **timeout**  integer | Timeout of health checks, in seconds  Returned: always  Sample: `10` |
| **http**  complex | Configuration for HTTP and HTTPS services  Returned: always |
| **certificates**  list / elements=string | List of Names or IDs of certificates  Returned: always |
| **cookie_lifetime**  integer | Lifetime of the cookie which will be set when you enable sticky sessions, in seconds  Returned: always  Sample: `3600` |
| **cookie_name**  string | Name of the cookie which will be set when you enable sticky sessions  Returned: always  Sample: `"HCLBSTICKY"` |
| **redirect_http**  boolean | Redirect Traffic from Port 80 to Port 443, only available if protocol is https  Returned: always  Sample: `false` |
| **sticky_sessions**  boolean | Enable or disable sticky_sessions  Returned: always  Sample: `true` |
| **listen_port**  integer | The port the service listens on, i.e. the port users can connect to.  Returned: always  Sample: `443` |
| **load_balancer**  string | The name of the Load Balancer where the service belongs to  Returned: always  Sample: `"my-load-balancer"` |
| **protocol**  string | Protocol of the service  Returned: always  Sample: `"http"` |
| **proxyprotocol**  boolean | Enable the PROXY protocol.  Returned: always  Sample: `false` |

### Authors

- Lukas Kaemmerling (@LKaemmerling)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
[Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
