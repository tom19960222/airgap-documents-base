---
collection: ansible
version: "8"
title: "cloudscale_ch.cloud.load_balancer_pool module – Manages load balancer pools on the cloudscale.ch IaaS service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cloudscale_ch/cloud/load_balancer_pool_module.html
fetched_at: 2026-07-28T01:39:56+00:00
---
# cloudscale_ch.cloud.load_balancer_pool module – Manages load balancer pools on the cloudscale.ch IaaS service

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
> To use it in a playbook, specify: `cloudscale_ch.cloud.load_balancer_pool`.

New in cloudscale_ch.cloud 2.3.0

- [Synopsis](load_balancer_pool_module.md#synopsis)
- [Parameters](load_balancer_pool_module.md#parameters)
- [Notes](load_balancer_pool_module.md#notes)
- [Examples](load_balancer_pool_module.md#examples)
- [Return Values](load_balancer_pool_module.md#return-values)

## [Synopsis](load_balancer_pool_module.md#id1)

- Get, create, update, delete pools on the cloudscale.ch IaaS service.

## [Parameters](load_balancer_pool_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **algorithm**  string | The algorithm according to which the incoming traffic is distributed between the pool members.  See the [API documentation](<https://www.cloudscale.ch/en/api/v1#pool-algorithms>) for supported distribution algorithms. |
| **api_timeout**  integer | Timeout in seconds for calls to the cloudscale.ch API.  This can also be passed in the `CLOUDSCALE_API_TIMEOUT` environment variable.  **Default:** `45` |
| **api_token**  string / required | cloudscale.ch API token.  This can also be passed in the `CLOUDSCALE_API_TOKEN` environment variable. |
| **api_url**  string  *added in cloudscale_ch.cloud 1.3.0* | cloudscale.ch API URL.  This can also be passed in the `CLOUDSCALE_API_URL` environment variable.  **Default:** `"https://api.cloudscale.ch/v1"` |
| **load_balancer**  string | UUID of the load balancer for this pool. |
| **name**  string | Name of the load balancer pool. |
| **protocol**  string | The protocol used for traffic between the load balancer and the pool members.  See the [API documentation](<https://www.cloudscale.ch/en/api/v1#pool-protocols>) for supported protocols. |
| **state**  string | State of the load balancer pool.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Tags assosiated with the load balancer. Set this to `{}` to clear any tags. |
| **uuid**  string | UUID of the load balancer pool.  Either *name* or *uuid* are required. |

## [Notes](load_balancer_pool_module.md#id3)

> **Note:**
>
> - If *uuid* option is provided, it takes precedence over *name* for pool selection. This allows to update the load balancer pool’s name.
> - If no *uuid* option is provided, *name* is used for pool selection. If more than one pool with this name exists, execution is aborted.
> - All operations are performed using the cloudscale.ch public API v1.
> - For details consult the full API documentation: <https://www.cloudscale.ch/en/api/v1>.
> - A valid API token is required for all operations. You can create as many tokens as you like using the cloudscale.ch control panel at <https://control.cloudscale.ch>.

## [Examples](load_balancer_pool_module.md#id4)

```yaml+jinja
# Create a pool for a load balancer using registered variables
- name: Create a running load balancer
  cloudscale_ch.cloud.load_balancer:
    name: 'lb1'
    flavor: 'lb-standard'
    zone: 'lpg1'
    tags:
      project: ansible-test
      stage: production
      sla: 24-7
    api_token: xxxxxx
  register: load_balancer

- name: Create a load balancer pool
  cloudscale_ch.cloud.load_balancer_pool:
    name: 'swimming-pool'
    load_balancer: '{{ load_balancer.uuid }}'
    algorithm: 'round_robin'
    protocol: 'tcp'
    tags:
      project: ansible-test
      stage: production
      sla: 24-7
    api_token: xxxxxx
  register: load_balancer_pool

# Create a load balancer pool with algorithm: round_robin and protocol: tcp
- name: Create a load balancer pool
  cloudscale_ch.cloud.load_balancer_pool:
    name: 'cloudscale-loadbalancer-pool1'
    load_balancer: '3766c579-3012-4a85-8192-2bbb4ef85b5f'
    algorithm: 'round_robin'
    protocol: 'tcp'
    tags:
      project: ansible-test
      stage: production
      sla: 24-7
    api_token: xxxxxx

# Get load balancer pool facts by name
- name: Get facts of a load balancer pool
  cloudscale_ch.cloud.load_balancer_pool:
    name: cloudscale-loadbalancer-pool1
    api_token: xxxxxx
```

## [Return Values](load_balancer_pool_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **algorithm**  string | The algorithm according to which the incoming traffic is distributed between the pool members  **Returned:** success  **Sample:** `"round_robin"` |
| **created_at**  string | The creation date and time of the load balancer pool  **Returned:** success when not state == absent  **Sample:** `"2023-02-07T15:32:02.308041Z"` |
| **href**  string | API URL to get details about this load balancer  **Returned:** success when not state == absent  **Sample:** `"https://api.cloudscale.ch/v1/load-balancers/pools/"` |
| **load_balancer**  list / elements=string | The load balancer this pool is connected to  **Returned:** success when not state == absent  **Sample:** `{"href": "https://api.cloudscale.ch/v1/load-balancers/15264769-ac69-4809-a8e4-4d73f8f92496", "name": "web-lb", "uuid": "15264769-ac69-4809-a8e4-4d73f8f92496"}` |
| **name**  string | The display name of the load balancer pool  **Returned:** success  **Sample:** `"web-lb-pool1"` |
| **protocol**  string | The protocol used for traffic between the load balancer and the pool members  **Returned:** success  **Sample:** `"tcp"` |
| **state**  string | The current state of the load balancer pool  **Returned:** success  **Sample:** `"present"` |
| **tags**  dictionary | Tags assosiated with the load balancer  **Returned:** success  **Sample:** `{"project": "my project"}` |
| **uuid**  string | The unique identifier for this load balancer pool  **Returned:** success  **Sample:** `"3766c579-3012-4a85-8192-2bbb4ef85b5f"` |

### Authors

- Gaudenz Steinlin (@gaudenz)
- Kenneth Joss (@k-304)

### Collection links

- [Issue Tracker](https://github.com/cloudscale-ch/ansible-collection-cloudscale/issues)
- [Repository (Sources)](https://github.com/cloudscale-ch/ansible-collection-cloudscale)
