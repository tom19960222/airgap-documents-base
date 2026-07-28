---
collection: ansible
version: "8"
title: "cloudscale_ch.cloud.load_balancer_pool_member module – Manages load balancer pool members on the cloudscale.ch IaaS service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cloudscale_ch/cloud/load_balancer_pool_member_module.html
fetched_at: 2026-07-28T01:39:56+00:00
---
# cloudscale_ch.cloud.load_balancer_pool_member module – Manages load balancer pool members on the cloudscale.ch IaaS service

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
> To use it in a playbook, specify: `cloudscale_ch.cloud.load_balancer_pool_member`.

New in cloudscale_ch.cloud 2.3.0

- [Synopsis](load_balancer_pool_member_module.md#synopsis)
- [Parameters](load_balancer_pool_member_module.md#parameters)
- [Notes](load_balancer_pool_member_module.md#notes)
- [Examples](load_balancer_pool_member_module.md#examples)
- [Return Values](load_balancer_pool_member_module.md#return-values)

## [Synopsis](load_balancer_pool_member_module.md#id1)

- Get, create, update, delete pool members on the cloudscale.ch IaaS service.

## [Parameters](load_balancer_pool_member_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string | The IP address to which traffic is sent. |
| **api_timeout**  integer | Timeout in seconds for calls to the cloudscale.ch API.  This can also be passed in the `CLOUDSCALE_API_TIMEOUT` environment variable.  **Default:** `45` |
| **api_token**  string / required | cloudscale.ch API token.  This can also be passed in the `CLOUDSCALE_API_TOKEN` environment variable. |
| **api_url**  string  *added in cloudscale_ch.cloud 1.3.0* | cloudscale.ch API URL.  This can also be passed in the `CLOUDSCALE_API_URL` environment variable.  **Default:** `"https://api.cloudscale.ch/v1"` |
| **enabled**  boolean | Pool member will not receive traffic if false. Default is true.  **Choices:**   - `false` - `true` ← (default) |
| **load_balancer_pool**  string | UUID of the load balancer pool. |
| **monitor_port**  integer | The port to which health monitor checks are sent.  If not specified, protocol_port will be used. Default is null. |
| **name**  string | Name of the load balancer pool member.  Either *name* or *uuid* are required. |
| **protocol_port**  integer | The port to which actual traffic is sent. |
| **state**  string | State of the load balancer pool member.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnet**  string | The subnet of the address must be specified here. |
| **tags**  dictionary | Tags assosiated with the load balancer. Set this to `{}` to clear any tags. |
| **uuid**  string | UUID of the load balancer.  Either *name* or *uuid* are required. |

## [Notes](load_balancer_pool_member_module.md#id3)

> **Note:**
>
> - If *uuid* option is provided, it takes precedence over *name* for pool member selection. This allows to update the member’s name.
> - If no *uuid* option is provided, *name* is used for pool member selection. If more than one load balancer with this name exists, execution is aborted.
> - All operations are performed using the cloudscale.ch public API v1.
> - For details consult the full API documentation: <https://www.cloudscale.ch/en/api/v1>.
> - A valid API token is required for all operations. You can create as many tokens as you like using the cloudscale.ch control panel at <https://control.cloudscale.ch>.

## [Examples](load_balancer_pool_member_module.md#id4)

```yaml+jinja
# Create a pool member for a load balancer pool using registered variables
- name: Create a load balancer pool
  cloudscale_ch.cloud.load_balancer_pool:
    name: 'swimming-pool'
    load_balancer: '514064c2-cfd4-4b0c-8a4b-c68c552ff84f'
    algorithm: 'round_robin'
    protocol: 'tcp'
    tags:
      project: ansible-test
      stage: production
      sla: 24-7
    api_token: xxxxxx
  register: load_balancer_pool

- name: Create a load balancer pool member
  cloudscale_ch.cloud.load_balancer_pool_member:
    name: 'my-shiny-swimming-pool-member'
    load_balancer_pool: '{{ load_balancer_pool.uuid }}'
    enabled: true
    protocol_port: 8080
    monitor_port: 8081
    subnet: '70d282ab-2a01-4abb-ada5-34e56a5a7eee'
    address: '172.16.0.100'
    tags:
      project: ansible-test
      stage: production
      sla: 24-7
    api_token: xxxxxx

# Get load balancer pool member facts by name
- name: Get facts of a load balancer pool member by name
  cloudscale_ch.cloud.load_balancer_pool_member:
    name: 'my-shiny-swimming-pool-member'
    api_token: xxxxxx
```

## [Return Values](load_balancer_pool_member_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address**  string | The IP address to which traffic is sent  **Returned:** success  **Sample:** `"10.11.12.3"` |
| **created_at**  string | The creation date and time of the load balancer pool member  **Returned:** success when not state == absent  **Sample:** `"2023-02-07T15:32:02.308041Z"` |
| **enabled**  boolean | THe status of the load balancer pool member  **Returned:** success  **Sample:** `true` |
| **href**  string | API URL to get details about this load balancer  **Returned:** success when not state == absent  **Sample:** `"https://api.cloudscale.ch/v1/load-balancers/pools/20a7eb11-3e17-4177-b46d-36e13b101d1c/members/b9991773-857d-47f6-b20b-0a03709529a9"` |
| **monitor_port**  integer | The port to which health monitor checks are sent  **Returned:** success  **Sample:** `8081` |
| **monitor_status**  string | The status of the pool’s health monitor check for this member  **Returned:** success  **Sample:** `"up"` |
| **name**  string | The display name of the load balancer pool member  **Returned:** success  **Sample:** `"web-lb-pool"` |
| **pool**  dictionary | The pool of the pool member  **Returned:** success  **Sample:** `{"href": "https://api.cloudscale.ch/v1/load-balancers/pools/20a7eb11-3e17-4177-b46d-36e13b101d1c", "name": "web-lb-pool", "uuid": "20a7eb11-3e17-4177-b46d-36e13b101d1c"}` |
| **protocol_port**  integer | The port to which actual traffic is sent  **Returned:** success  **Sample:** `8080` |
| **subnet**  dictionary | The subnet in a private network in which address is located  **Returned:** success  **Sample:** `{"cidr": "10.11.12.0/24", "href": "https://api.cloudscale.ch/v1/subnets/70d282ab-2a01-4abb-ada5-34e56a5a7eee", "uuid": "70d282ab-2a01-4abb-ada5-34e56a5a7eee"}` |
| **tags**  dictionary | Tags assosiated with the load balancer  **Returned:** success  **Sample:** `{"project": "my project"}` |
| **uuid**  string | The unique identifier for this load balancer pool member  **Returned:** success  **Sample:** `"cfde831a-4e87-4a75-960f-89b0148aa2cc"` |

### Authors

- Gaudenz Steinlin (@gaudenz)
- Kenneth Joss (@k-304)

### Collection links

- [Issue Tracker](https://github.com/cloudscale-ch/ansible-collection-cloudscale/issues)
- [Repository (Sources)](https://github.com/cloudscale-ch/ansible-collection-cloudscale)
