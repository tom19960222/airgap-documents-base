---
collection: ansible
version: "8"
title: "cloudscale_ch.cloud.floating_ip module – Manages floating IPs on the cloudscale.ch IaaS service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cloudscale_ch/cloud/floating_ip_module.html
fetched_at: 2026-07-28T01:39:53+00:00
---
# cloudscale_ch.cloud.floating_ip module – Manages floating IPs on the cloudscale.ch IaaS service

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
> To use it in a playbook, specify: `cloudscale_ch.cloud.floating_ip`.

New in cloudscale_ch.cloud 1.0.0

- [Synopsis](floating_ip_module.md#synopsis)
- [Parameters](floating_ip_module.md#parameters)
- [Notes](floating_ip_module.md#notes)
- [Examples](floating_ip_module.md#examples)
- [Return Values](floating_ip_module.md#return-values)

## [Synopsis](floating_ip_module.md#id1)

- Create, assign and delete floating IPs on the cloudscale.ch IaaS service.

Aliases: cloudscale_floating_ip

## [Parameters](floating_ip_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | Timeout in seconds for calls to the cloudscale.ch API.  This can also be passed in the `CLOUDSCALE_API_TIMEOUT` environment variable.  **Default:** `45` |
| **api_token**  string / required | cloudscale.ch API token.  This can also be passed in the `CLOUDSCALE_API_TOKEN` environment variable. |
| **api_url**  string  *added in cloudscale_ch.cloud 1.3.0* | cloudscale.ch API URL.  This can also be passed in the `CLOUDSCALE_API_URL` environment variable.  **Default:** `"https://api.cloudscale.ch/v1"` |
| **ip_version**  integer | IP protocol version of the floating IP.  Required when assigning a new floating IP.  **Choices:**   - `4` - `6` |
| **name**  string  *added in cloudscale_ch.cloud 1.3.0* | Name to identifiy the floating IP address for idempotency.  One of *network* or *name* is required to identify the floating IP.  Required for assigning a new floating IP. |
| **network**  aliases: ip  string | Floating IP address to change.  One of *network* or *name* is required to identify the floating IP. |
| **prefix_length**  integer | Only valid if *ip_version* is 6.  Prefix length for the IPv6 network. Currently only a prefix of /56 can be requested. If no *prefix_length* is present, a single address is created.  **Choices:**   - `56` |
| **region**  string | Region in which the floating IP resides (e.g. `lpg` or `rma`). If omitted, the region of the project default zone is used. This parameter must be omitted if *type* is set to `global`. |
| **reverse_ptr**  string | Reverse PTR entry for this address.  You cannot set a reverse PTR entry for IPv6 floating networks. Reverse PTR entries are only allowed for single addresses. |
| **server**  string | UUID of the server assigned to this floating IP. |
| **state**  string | State of the floating IP.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary  *added in cloudscale_ch.cloud 1.1.0* | Tags associated with the floating IP. Set this to `{}` to clear any tags. |
| **type**  string | The type of the floating IP.  **Choices:**   - `"regional"` ← (default) - `"global"` |

## [Notes](floating_ip_module.md#id3)

> **Note:**
>
> - Once a floating_ip is created, all parameters except `server`, `reverse_ptr` and `tags` are read-only.
> - All operations are performed using the cloudscale.ch public API v1.
> - For details consult the full API documentation: <https://www.cloudscale.ch/en/api/v1>.
> - A valid API token is required for all operations. You can create as many tokens as you like using the cloudscale.ch control panel at <https://control.cloudscale.ch>.

## [Examples](floating_ip_module.md#id4)

```yaml+jinja
# Request a new floating IP without assignment to a server
- name: Request a floating IP
  cloudscale_ch.cloud.floating_ip:
    name: IP to my server
    ip_version: 4
    reverse_ptr: my-server.example.com
    api_token: xxxxxx

# Request a new floating IP with assignment
- name: Request a floating IP
  cloudscale_ch.cloud.floating_ip:
    name: web
    ip_version: 4
    server: 47cec963-fcd2-482f-bdb6-24461b2d47b1
    reverse_ptr: my-server.example.com
    api_token: xxxxxx

# Assign an existing floating IP to a different server by its IP address
- name: Move floating IP to backup server
  cloudscale_ch.cloud.floating_ip:
    ip: 192.0.2.123
    server: ea3b39a3-77a8-4d0b-881d-0bb00a1e7f48
    api_token: xxxxxx

# Assign an existing floating IP to a different server by name
- name: Move floating IP to backup server
  cloudscale_ch.cloud.floating_ip:
    name: IP to my server
    server: ea3b39a3-77a8-4d0b-881d-0bb00a1e7f48
    api_token: xxxxxx

# Request a new floating IPv6 network
- name: Request a floating IP
  cloudscale_ch.cloud.floating_ip:
    name: IPv6 to my server
    ip_version: 6
    prefix_length: 56
    server: 47cec963-fcd2-482f-bdb6-24461b2d47b1
    api_token: xxxxxx
    region: lpg1

# Assign an existing floating network to a different server
- name: Move floating IP to backup server
  cloudscale_ch.cloud.floating_ip:
    ip: '{{ floating_ip.ip }}'
    server: ea3b39a3-77a8-4d0b-881d-0bb00a1e7f48
    api_token: xxxxxx

# Remove a floating IP
- name: Release floating IP
  cloudscale_ch.cloud.floating_ip:
    ip: 192.0.2.123
    state: absent
    api_token: xxxxxx

# Remove a floating IP by name
- name: Release floating IP
  cloudscale_ch.cloud.floating_ip:
    name: IP to my server
    state: absent
    api_token: xxxxxx
```

## [Return Values](floating_ip_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **href**  string | The API URL to get details about this floating IP.  **Returned:** success when state == present  **Sample:** `"https://api.cloudscale.ch/v1/floating-ips/2001:db8::cafe"` |
| **ip**  string | The floating IP address.  **Returned:** success when state == present  **Sample:** `"185.98.122.176"` |
| **name**  string  *added in cloudscale_ch.cloud 1.3.0* | The name of the floating IP.  **Returned:** success  **Sample:** `"my floating ip"` |
| **network**  string | The CIDR notation of the network that is routed to your server.  **Returned:** success  **Sample:** `"2001:db8::cafe/128"` |
| **next_hop**  string | Your floating IP is routed to this IP address.  **Returned:** success when state == present  **Sample:** `"2001:db8:dead:beef::42"` |
| **region**  dictionary | The region of the floating IP.  **Returned:** success when state == present  **Sample:** `{"slug": "lpg"}` |
| **reverse_ptr**  string | The reverse pointer for this floating IP address.  **Returned:** success when state == present  **Sample:** `"185-98-122-176.cust.cloudscale.ch"` |
| **server**  string | The floating IP is routed to this server.  **Returned:** success when state == present  **Sample:** `"47cec963-fcd2-482f-bdb6-24461b2d47b1"` |
| **state**  string | The current status of the floating IP.  **Returned:** success  **Sample:** `"present"` |
| **tags**  dictionary  *added in cloudscale_ch.cloud 1.1.0* | Tags assosiated with the floating IP.  **Returned:** success  **Sample:** `{"project": "my project"}` |

### Authors

- Gaudenz Steinlin (@gaudenz)
- Denis Krienbühl (@href)
- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/cloudscale-ch/ansible-collection-cloudscale/issues)
- [Repository (Sources)](https://github.com/cloudscale-ch/ansible-collection-cloudscale)
