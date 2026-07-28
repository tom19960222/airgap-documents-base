---
collection: ansible
version: "6"
title: "cloudscale_ch.cloud.subnet module – Manages subnets on the cloudscale.ch IaaS service"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cloudscale_ch/cloud/subnet_module.html
fetched_at: 2026-07-27T17:03:08+00:00
---
# cloudscale_ch.cloud.subnet module – Manages subnets on the cloudscale.ch IaaS service

> **Note:**
>
> This module is part of the [cloudscale_ch.cloud collection](https://galaxy.ansible.com/cloudscale_ch/cloud) (version 2.2.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cloudscale_ch.cloud`.
>
> To use it in a playbook, specify: `cloudscale_ch.cloud.subnet`.

New in cloudscale_ch.cloud 1.3.0

- [Synopsis](subnet_module.md#synopsis)
- [Parameters](subnet_module.md#parameters)
- [Notes](subnet_module.md#notes)
- [Examples](subnet_module.md#examples)
- [Return Values](subnet_module.md#return-values)

## [Synopsis](subnet_module.md#id1)

- Create, update and remove subnets.

## [Parameters](subnet_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | Timeout in seconds for calls to the cloudscale.ch API.  This can also be passed in the `CLOUDSCALE_API_TIMEOUT` environment variable.  Default: `45` |
| **api_token**  string / required | cloudscale.ch API token.  This can also be passed in the `CLOUDSCALE_API_TOKEN` environment variable. |
| **api_url**  string  added in cloudscale_ch.cloud 1.3.0 | cloudscale.ch API URL.  This can also be passed in the `CLOUDSCALE_API_URL` environment variable.  Default: `"https://api.cloudscale.ch/v1"` |
| **cidr**  string | The cidr of the subnet.  Required if *state=present*. |
| **dns_servers**  list / elements=string | A list of DNS resolver IP addresses, that act as DNS servers.  If not set, the cloudscale.ch default resolvers are used. |
| **gateway_address**  string | The gateway address of the subnet. If not set, no gateway is used.  Cannot be within the DHCP range, which is the lowest .101-.254 in the subnet. |
| **network**  dictionary | The name of the network the subnet is related to.  Required if *state=present*. |
| **name**  string | The uuid of the network. |
| **uuid**  string | The uuid of the network. |
| **zone**  string | The zone the network allocated in. |
| **reset**  boolean | Resets *gateway_address* and *dns_servers* to default values by the API.  Note: Idempotency is not given.  Choices:   - `false` ← (default) - `true` |
| **state**  string | State of the subnet.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Tags associated with the subnet. Set this to `{}` to clear any tags. |
| **uuid**  string | UUID of the subnet. |

## [Notes](subnet_module.md#id3)

> **Note:**
>
> - All operations are performed using the cloudscale.ch public API v1.
> - For details consult the full API documentation: <https://www.cloudscale.ch/en/api/v1>.
> - A valid API token is required for all operations. You can create as many tokens as you like using the cloudscale.ch control panel at <https://control.cloudscale.ch>.

## [Examples](subnet_module.md#id4)

```yaml+jinja
---
- name: Ensure subnet exists
  cloudscale_ch.cloud.subnet:
    cidr: 172.16.0.0/24
    network:
      uuid: 2db69ba3-1864-4608-853a-0771b6885a3a
    api_token: xxxxxx

- name: Ensure subnet exists
  cloudscale_ch.cloud.subnet:
    cidr: 192.168.1.0/24
    gateway_address: 192.168.1.1
    dns_servers:
      - 192.168.1.10
      - 192.168.1.11
    network:
      name: private
      zone: lpg1
    api_token: xxxxxx

- name: Ensure a subnet is absent
  cloudscale_ch.cloud.subnet:
    cidr: 172.16.0.0/24
    network:
      name: private
      zone: lpg1
    state: absent
    api_token: xxxxxx
```

## [Return Values](subnet_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cidr**  string | The CIDR of the subnet.  Returned: success  Sample: `"172.16.0.0/24"` |
| **dns_servers**  list / elements=string | List of DNS resolver IP addresses.  Returned: success  Sample: `["9.9.9.9", "149.112.112.112"]` |
| **gateway_address**  string | The gateway address of the subnet.  Returned: success  Sample: `"192.168.42.1"` |
| **href**  string | API URL to get details about the subnet.  Returned: success  Sample: `"https://api.cloudscale.ch/v1/subnets/33333333-1864-4608-853a-0771b6885a3"` |
| **network**  complex | The network object of the subnet.  Returned: success |
| **href**  string | API URL to get details about the network.  Returned: success  Sample: `"https://api.cloudscale.ch/v1/networks/33333333-1864-4608-853a-0771b6885a3"` |
| **name**  string | The name of the network.  Returned: success  Sample: `"my network"` |
| **uuid**  string | The unique identifier for the network.  Returned: success  Sample: `"33333333-1864-4608-853a-0771b6885a3"` |
| **zone**  dictionary  added in cloudscale_ch.cloud 1.4.0 | The zone the network is allocated in.  Returned: success  Sample: `{"slug": "rma1"}` |
| **state**  string | State of the subnet.  Returned: success  Sample: `"present"` |
| **tags**  dictionary | Tags associated with the subnet.  Returned: success  Sample: `{"project": "my project"}` |
| **uuid**  string | The unique identifier for the subnet.  Returned: success  Sample: `"33333333-1864-4608-853a-0771b6885a3"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/cloudscale-ch/ansible-collection-cloudscale/issues)
[Repository (Sources)](https://github.com/cloudscale-ch/ansible-collection-cloudscale)
