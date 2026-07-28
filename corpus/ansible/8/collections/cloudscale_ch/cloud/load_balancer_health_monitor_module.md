---
collection: ansible
version: "8"
title: "cloudscale_ch.cloud.load_balancer_health_monitor module – Manages load balancers on the cloudscale.ch IaaS service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cloudscale_ch/cloud/load_balancer_health_monitor_module.html
fetched_at: 2026-07-28T01:39:54+00:00
---
# cloudscale_ch.cloud.load_balancer_health_monitor module – Manages load balancers on the cloudscale.ch IaaS service

> **Note:**
>
> This module is part of the [cloudscale_ch.cloud collection](https://galaxy.ansible.com/ui/repo/published/cloudscale_ch/cloud/) (version 2.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cloudscale_ch.cloud`.
>
> To use it in a playbook, specify: `cloudscale_ch.cloud.load_balancer_health_monitor`.

New in cloudscale_ch.cloud 2.3.0

- [Synopsis](load_balancer_health_monitor_module.md#synopsis)
- [Parameters](load_balancer_health_monitor_module.md#parameters)
- [Notes](load_balancer_health_monitor_module.md#notes)
- [Examples](load_balancer_health_monitor_module.md#examples)
- [Return Values](load_balancer_health_monitor_module.md#return-values)

## [Synopsis](load_balancer_health_monitor_module.md#id1)

- Get, create, update, delete health monitors on the cloudscale.ch IaaS service.

## [Parameters](load_balancer_health_monitor_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | Timeout in seconds for calls to the cloudscale.ch API.  This can also be passed in the `CLOUDSCALE_API_TIMEOUT` environment variable.  **Default:** `45` |
| **api_token**  string / required | cloudscale.ch API token.  This can also be passed in the `CLOUDSCALE_API_TOKEN` environment variable. |
| **api_url**  string  *added in cloudscale_ch.cloud 1.3.0* | cloudscale.ch API URL.  This can also be passed in the `CLOUDSCALE_API_URL` environment variable.  **Default:** `"https://api.cloudscale.ch/v1"` |
| **delay_s**  integer | The delay between two successive checks in seconds. |
| **down_threshold**  integer | The number of checks that need to fail before the monitor_status of a pool member changes to “down”. |
| **http**  dictionary | Advanced options for health monitors with type “http” or “https”. |
| **expected_codes**  list / elements=string | The HTTP status codes allowed for a check to be considered successful.  See the [API documentation](<https://www.cloudscale.ch/en/api/v1#http-attribute-specification>) for details. |
| **host**  string | The server name in the HTTP Host header used for the check.  Requires version to be set to “1.1”. |
| **method**  string | The HTTP method used for the check. |
| **url_path**  string | The URL used for the check. |
| **version**  string | The HTTP version used for the check. |
| **pool**  string | The pool of the health monitor. |
| **state**  string | State of the load balancer health monitor.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Tags assosiated with the load balancer. Set this to `{}` to clear any tags. |
| **timeout_s**  integer | The maximum time allowed for an individual check in seconds. |
| **type**  string | The type of the health monitor.  See the [API documentation](<https://www.cloudscale.ch/en/api/v1#create-a-health-monitor>) for allowed options. |
| **up_threshold**  integer | The number of checks that need to be successful before the monitor_status of a pool member changes to “up”. |
| **uuid**  string | UUID of the load balancer health monitor. |

## [Notes](load_balancer_health_monitor_module.md#id3)

> **Note:**
>
> - Health monitors do not have names. *uuid*‘s are used to reference a health monitors.
> - All operations are performed using the cloudscale.ch public API v1.
> - For details consult the full API documentation: <https://www.cloudscale.ch/en/api/v1>.
> - A valid API token is required for all operations. You can create as many tokens as you like using the cloudscale.ch control panel at <https://control.cloudscale.ch>.

## [Examples](load_balancer_health_monitor_module.md#id4)

```yaml+jinja
# Create a simple health monitor for a pool
- name: Create a load balancer pool
  cloudscale_ch.cloud.load_balancer_pool:
    name: 'swimming-pool'
    load_balancer: '3d41b118-f95c-4897-ad74-2260fea783fc'
    algorithm: 'round_robin'
    protocol: 'tcp'
    api_token: xxxxxx
  register: load_balancer_pool

- name: Create a load balancer health monitor (ping)
  cloudscale_ch.cloud.load_balancer_health_monitor:
    pool: '{{ load_balancer_pool.uuid }}'
    type: 'ping'
    api_token: xxxxxx
  register: load_balancer_health_monitor

# Get load balancer health monitor facts by UUID
- name: Get facts of a load balancer health monitor by UUID
  cloudscale_ch.cloud.load_balancer_health_monitor:
    uuid: '{{ load_balancer_health_monitor.uuid }}'
    api_token: xxxxxx

# Update a health monitor
- name: Update HTTP method of a load balancer health monitor from GET to CONNECT
  cloudscale_ch.cloud.load_balancer_health_monitor:
    uuid: '{{ load_balancer_health_monitor_http.uuid }}'
    delay_s: 2
    timeout_s: 1
    up_threshold: 2
    down_threshold: 3
    type: 'http'
    http:
      expected_codes:
        - 200
        - 202
      method: 'CONNECT'
      url_path: '/'
      version: '1.1'
      host: 'host1'
    tags:
      project: ansible-test
      stage: production
      sla: 24-7
    api_token: xxxxxx
  register: load_balancer_health_monitor
```

## [Return Values](load_balancer_health_monitor_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **created_at**  string | The creation date and time of the load balancer health monitor  **Returned:** success when not state == absent  **Sample:** `"2023-02-22T09:55:38.285018Z"` |
| **delay_s**  integer | The delay between two successive checks in seconds  **Returned:** success when not state == absent  **Sample:** `2` |
| **down_threshold**  integer | The number of checks that need to fail before the monitor_status of a pool member changes to “down”  **Returned:** success when not state == absent  **Sample:** `3` |
| **href**  string | API URL to get details about this load balancer health monitor  **Returned:** success when not state == absent  **Sample:** `"https://api.cloudscale.ch/v1/load-balancers/health-monitors/ee4952d4-2eba-4dec-8957-7911b3ce245b"` |
| **http**  dictionary | Advanced options for health monitors with type “http” or “https”  **Returned:** success when not state == absent  **Sample:** `[{"expected_codes": ["200"], "host": null, "method": "GET", "url_path": "/", "version": "1.0"}]` |
| **pool**  dictionary | The pool of the health monitor  **Returned:** success when not state == absent  **Sample:** `[{"href": "https://api.cloudscale.ch/v1/load-balancers/pools/618a6cc8-d757-4fab-aa10-d49dc47e667b"}, {"uuid": "618a6cc8-d757-4fab-aa10-d49dc47e667b"}, {"name": "swimming pool"}]` |
| **tags**  dictionary | Tags assosiated with the load balancer  **Returned:** success  **Sample:** `{"project": "my project"}` |
| **timeout_s**  integer | The maximum time allowed for an individual check in seconds  **Returned:** success when not state == absent  **Sample:** `1` |
| **type**  string | The type of the health monitor  **Returned:** success when not state == absent |
| **up_threshold**  integer | The number of checks that need to be successful before the monitor_status of a pool member changes to “up”  **Returned:** success when not state == absent  **Sample:** `2` |
| **uuid**  string | The unique identifier for this load balancer health monitor  **Returned:** success  **Sample:** `"ee4952d4-2eba-4dec-8957-7911b3ce245b"` |

### Authors

- Gaudenz Steinlin (@gaudenz)
- Kenneth Joss (@k-304)

### Collection links

- [Issue Tracker](https://github.com/cloudscale-ch/ansible-collection-cloudscale/issues)
- [Repository (Sources)](https://github.com/cloudscale-ch/ansible-collection-cloudscale)
