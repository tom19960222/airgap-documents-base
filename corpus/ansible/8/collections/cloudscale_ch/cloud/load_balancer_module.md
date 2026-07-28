---
collection: ansible
version: "8"
title: "cloudscale_ch.cloud.load_balancer module – Manages load balancers on the cloudscale.ch IaaS service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cloudscale_ch/cloud/load_balancer_module.html
fetched_at: 2026-07-28T01:39:53+00:00
---
# cloudscale_ch.cloud.load_balancer module – Manages load balancers on the cloudscale.ch IaaS service

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
> To use it in a playbook, specify: `cloudscale_ch.cloud.load_balancer`.

New in cloudscale_ch.cloud 2.3.0

- [Synopsis](load_balancer_module.md#synopsis)
- [Parameters](load_balancer_module.md#parameters)
- [Notes](load_balancer_module.md#notes)
- [Examples](load_balancer_module.md#examples)
- [Return Values](load_balancer_module.md#return-values)

## [Synopsis](load_balancer_module.md#id1)

- Get, create, update, delete load balancers on the cloudscale.ch IaaS service.

## [Parameters](load_balancer_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | Timeout in seconds for calls to the cloudscale.ch API.  This can also be passed in the `CLOUDSCALE_API_TIMEOUT` environment variable.  **Default:** `45` |
| **api_token**  string / required | cloudscale.ch API token.  This can also be passed in the `CLOUDSCALE_API_TOKEN` environment variable. |
| **api_url**  string  *added in cloudscale_ch.cloud 1.3.0* | cloudscale.ch API URL.  This can also be passed in the `CLOUDSCALE_API_URL` environment variable.  **Default:** `"https://api.cloudscale.ch/v1"` |
| **flavor**  string | Flavor of the load balancer.  **Default:** `"lb-standard"` |
| **name**  string | Name of the load balancer.  Either *name* or *uuid* are required. |
| **state**  string | State of the load balancer.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Tags assosiated with the load balancer. Set this to `{}` to clear any tags. |
| **uuid**  string | UUID of the load balancer.  Either *name* or *uuid* are required. |
| **vip_addresses**  list / elements=dictionary | See the [API documentation](<https://www.cloudscale.ch/en/api/v1#vip_addresses-attribute-specification>) for details about this parameter. |
| **address**  string | Use this address.  Must be in the same range as subnet.  If empty, a radom address will be used. |
| **subnet**  string | Create a VIP address on the subnet identified by this UUID. |
| **zone**  string | Zone in which the load balancer resides (e.g. `lpg1` or `rma1`). |

## [Notes](load_balancer_module.md#id3)

> **Note:**
>
> - If *uuid* option is provided, it takes precedence over *name* for load balancer selection. This allows to update the load balancers’s name.
> - If no *uuid* option is provided, *name* is used for load balancer selection. If more than one load balancer with this name exists, execution is aborted.
> - All operations are performed using the cloudscale.ch public API v1.
> - For details consult the full API documentation: <https://www.cloudscale.ch/en/api/v1>.
> - A valid API token is required for all operations. You can create as many tokens as you like using the cloudscale.ch control panel at <https://control.cloudscale.ch>.

## [Examples](load_balancer_module.md#id4)

```yaml+jinja
# Create and start a load balancer
- name: Start cloudscale.ch load balancer
  cloudscale_ch.cloud.load_balancer:
    name: my-shiny-cloudscale-load-balancer
    flavor: lb-standard
    zone: rma1
    tags:
      project: my project
    api_token: xxxxxx

# Create and start a load balancer with specific subnet
- name: Start cloudscale.ch load balancer
  cloudscale_ch.cloud.load_balancer:
    name: my-shiny-cloudscale-load-balancer
    flavor: lb-standard
    vip_addresses:
      - subnet: d7b82c9b-5900-436c-9296-e94dca01c7a0
        address: 172.25.12.1
    zone: lpg1
    tags:
      project: my project
    api_token: xxxxxx

# Get load balancer facts by name
- name: Get facts of a load balancer
  cloudscale_ch.cloud.load_balancer:
    name: my-shiny-cloudscale-load-balancer
    api_token: xxxxxx
```

## [Return Values](load_balancer_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **created_at**  string | The creation date and time of the load balancer  **Returned:** success when not state == absent  **Sample:** `"2023-02-07T15:32:02.308041Z"` |
| **flavor**  list / elements=string | The flavor that has been used for this load balancer  **Returned:** success when not state == absent  **Sample:** `{"name": "LB-Standard", "slug": "lb-standard"}` |
| **href**  string | API URL to get details about this load balancer  **Returned:** success when not state == absent  **Sample:** `"https://api.cloudscale.ch/v1/load-balancers/0f62e0a7-f459-4fc4-9c25-9e57b6cb4b2f"` |
| **name**  string | The display name of the load balancer  **Returned:** success  **Sample:** `"web-lb"` |
| **state**  string | The current state of the load balancer  **Returned:** success  **Sample:** `"present"` |
| **status**  string | The current operational status of the load balancer  **Returned:** success  **Sample:** `"running"` |
| **tags**  dictionary | Tags assosiated with the load balancer  **Returned:** success  **Sample:** `{"project": "my project"}` |
| **uuid**  string | The unique identifier for this load balancer  **Returned:** success  **Sample:** `"cfde831a-4e87-4a75-960f-89b0148aa2cc"` |
| **vip_addresses**  dictionary | List of vip_addresses for this load balancer  **Returned:** success when not state == absent  **Sample:** `[{"address": "192.0.2.110", "subnet": [{"href": "https://api.cloudscale.ch/v1/subnets/92c70b2f-99cb-4811-8823-3d46572006e4"}, {"uuid": "92c70b2f-99cb-4811-8823-3d46572006e4"}, {"cidr": "192.0.2.0/24"}], "version": "4"}]` |
| **zone**  dictionary | The zone used for this load balancer  **Returned:** success when not state == absent  **Sample:** `{"slug": "lpg1"}` |

### Authors

- Gaudenz Steinlin (@gaudenz)
- Kenneth Joss (@k-304)

### Collection links

- [Issue Tracker](https://github.com/cloudscale-ch/ansible-collection-cloudscale/issues)
- [Repository (Sources)](https://github.com/cloudscale-ch/ansible-collection-cloudscale)
