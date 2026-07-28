---
collection: ansible
version: "8"
title: "cloudscale_ch.cloud.load_balancer_listener module – Manages load balancer listeners on the cloudscale.ch IaaS service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cloudscale_ch/cloud/load_balancer_listener_module.html
fetched_at: 2026-07-28T01:39:55+00:00
---
# cloudscale_ch.cloud.load_balancer_listener module – Manages load balancer listeners on the cloudscale.ch IaaS service

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
> To use it in a playbook, specify: `cloudscale_ch.cloud.load_balancer_listener`.

New in cloudscale_ch.cloud 2.3.0

- [Synopsis](load_balancer_listener_module.md#synopsis)
- [Parameters](load_balancer_listener_module.md#parameters)
- [Notes](load_balancer_listener_module.md#notes)
- [Examples](load_balancer_listener_module.md#examples)
- [Return Values](load_balancer_listener_module.md#return-values)

## [Synopsis](load_balancer_listener_module.md#id1)

- Get, create, update, delete listeners on the cloudscale.ch IaaS service.

## [Parameters](load_balancer_listener_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allowed_cidrs**  list / elements=string | Restrict the allowed source IPs for this listener.  Empty means that any source IP is allowed. If the list is non-empty, traffic from source IPs not included is denied. |
| **api_timeout**  integer | Timeout in seconds for calls to the cloudscale.ch API.  This can also be passed in the `CLOUDSCALE_API_TIMEOUT` environment variable.  **Default:** `45` |
| **api_token**  string / required | cloudscale.ch API token.  This can also be passed in the `CLOUDSCALE_API_TOKEN` environment variable. |
| **api_url**  string  *added in cloudscale_ch.cloud 1.3.0* | cloudscale.ch API URL.  This can also be passed in the `CLOUDSCALE_API_URL` environment variable.  **Default:** `"https://api.cloudscale.ch/v1"` |
| **name**  string | Name of the load balancer listener.  Either *name* or *uuid* are required. |
| **pool**  string | The pool of the listener. |
| **protocol**  string | The protocol used for receiving traffic. |
| **protocol_port**  integer | The port on which traffic is received. |
| **state**  string | State of the load balancer listener.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Tags assosiated with the load balancer. Set this to `{}` to clear any tags. |
| **timeout_client_data_ms**  integer | Client inactivity timeout in milliseconds. |
| **timeout_member_connect_ms**  integer | Pool member connection timeout in milliseconds. |
| **timeout_member_data_ms**  integer | Pool member inactivity timeout in milliseconds. |
| **uuid**  string | UUID of the load balancer listener.  Either *name* or *uuid* are required. |

## [Notes](load_balancer_listener_module.md#id3)

> **Note:**
>
> - If *uuid* option is provided, it takes precedence over *name* for load balancer listener selection. This allows to update the listener’s name.
> - If no *uuid* option is provided, *name* is used for load balancer listener selection.
> - If more than one load balancer with this name exists, execution is aborted.
> - All operations are performed using the cloudscale.ch public API v1.
> - For details consult the full API documentation: <https://www.cloudscale.ch/en/api/v1>.
> - A valid API token is required for all operations. You can create as many tokens as you like using the cloudscale.ch control panel at <https://control.cloudscale.ch>.

## [Examples](load_balancer_listener_module.md#id4)

```yaml+jinja
# Create a load balancer listener for a pool using registered variables
- name: Create a load balancer pool
  cloudscale_ch.cloud.load_balancer_pool:
    name: 'swimming-pool'
    load_balancer: '3d41b118-f95c-4897-ad74-2260fea783fc'
    algorithm: 'round_robin'
    protocol: 'tcp'
    api_token: xxxxxx
  register: load_balancer_pool

- name: Create a load balancer listener
  cloudscale_ch.cloud.load_balancer_listener:
    name: 'swimming-pool-listener'
    pool: '{{ load_balancer_pool.uuid }}'
    protocol: 'tcp'
    protocol_port: 8080
    tags:
      project: ansible-test
      stage: production
      sla: 24-7
    api_token: xxxxxx

# Create a load balancer listener for a pool with restriction
- name: Create a load balancer listener with ip restriction
  cloudscale_ch.cloud.load_balancer_listener:
    name: 'new-listener2'
    pool: '618a6cc8-d757-4fab-aa10-d49dc47e667b'
    protocol: 'tcp'
    protocol_port: 8080
    allowed_cidrs:
      - '192.168.3.0/24'
      - '2001:db8:85a3:8d3::/64'
    tags:
      project: ansible-test
      stage: production
      sla: 24-7
    api_token: xxxxxx

# Get load balancer listener facts by name
- name: Get facts of a load balancer listener by name
  cloudscale_ch.cloud.load_balancer_listener:
    name: '{{ cloudscale_resource_prefix }}-test'
    api_token: xxxxxx
```

## [Return Values](load_balancer_listener_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allowed_cidrs**  list / elements=string | Restrict the allowed source IPs for this listener  **Returned:** success when not state == absent  **Sample:** `["192.168.3.0/24", "2001:db8:85a3:8d3::/64"]` |
| **created_at**  string | The creation date and time of the load balancer listener  **Returned:** success when not state == absent  **Sample:** `"2023-02-07T15:32:02.308041Z"` |
| **href**  string | API URL to get details about this load balancer lintener  **Returned:** success when not state == absent  **Sample:** `"https://api.cloudscale.ch/v1/load-balancers/listeners/9fa91f17-fdb4-431f-8a59-78473f64e661"` |
| **name**  string | The display name of the load balancer listener  **Returned:** success  **Sample:** `"new-listener"` |
| **pool**  complex | The pool of the load balancer listener  **Returned:** success when not state == absent |
| **href**  string | API URL to get details about the pool.  **Returned:** success  **Sample:** `"https://api.cloudscale.ch/v1/load-balancers/pools/618a6cc8-d757-4fab-aa10-d49dc47e667b"` |
| **name**  string | The name of the pool.  **Returned:** success  **Sample:** `"new-listener"` |
| **uuid**  string | The unique identifier for the pool.  **Returned:** success  **Sample:** `"618a6cc8-d757-4fab-aa10-d49dc47e667b"` |
| **protocol**  string | The protocol used for receiving traffic  **Returned:** success when not state == absent  **Sample:** `"tcp"` |
| **protocol_port**  integer | The port on which traffic is received  **Returned:** success when not state == absent  **Sample:** `8080` |
| **tags**  dictionary | Tags assosiated with the load balancer listener  **Returned:** success  **Sample:** `{"project": "my project"}` |
| **timeout_client_data_ms**  integer | Client inactivity timeout in milliseconds  **Returned:** success when not state == absent  **Sample:** `50000` |
| **timeout_member_connect_ms**  integer | Pool member connection timeout in milliseconds  **Returned:** success when not state == absent  **Sample:** `50000` |
| **timeout_member_data_ms**  integer | Pool member inactivity timeout in milliseconds  **Returned:** success when not state == absent  **Sample:** `50000` |
| **uuid**  string | The unique identifier for this load balancer listener  **Returned:** success  **Sample:** `"9fa91f17-fdb4-431f-8a59-78473f64e661"` |

### Authors

- Gaudenz Steinlin (@gaudenz)
- Kenneth Joss (@k-304)

### Collection links

- [Issue Tracker](https://github.com/cloudscale-ch/ansible-collection-cloudscale/issues)
- [Repository (Sources)](https://github.com/cloudscale-ch/ansible-collection-cloudscale)
