---
collection: ansible
version: "6"
title: "cloudscale_ch.cloud.network module – Manages networks on the cloudscale.ch IaaS service"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cloudscale_ch/cloud/network_module.html
fetched_at: 2026-07-27T17:03:05+00:00
---
# cloudscale_ch.cloud.network module – Manages networks on the cloudscale.ch IaaS service

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
> To use it in a playbook, specify: `cloudscale_ch.cloud.network`.

New in cloudscale_ch.cloud 1.2.0

- [Synopsis](network_module.md#synopsis)
- [Parameters](network_module.md#parameters)
- [Notes](network_module.md#notes)
- [Examples](network_module.md#examples)
- [Return Values](network_module.md#return-values)

## [Synopsis](network_module.md#id1)

- Create, update and remove networks.

## [Parameters](network_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | Timeout in seconds for calls to the cloudscale.ch API.  This can also be passed in the `CLOUDSCALE_API_TIMEOUT` environment variable.  Default: `45` |
| **api_token**  string / required | cloudscale.ch API token.  This can also be passed in the `CLOUDSCALE_API_TOKEN` environment variable. |
| **api_url**  string  added in cloudscale_ch.cloud 1.3.0 | cloudscale.ch API URL.  This can also be passed in the `CLOUDSCALE_API_URL` environment variable.  Default: `"https://api.cloudscale.ch/v1"` |
| **auto_create_ipv4_subnet**  boolean | Whether to automatically create an IPv4 subnet in the network or not.  Choices:   - `false` - `true` ← (default) |
| **mtu**  integer | The MTU of the network.  Default: `9000` |
| **name**  string | Name of the network.  Either *name* or *uuid* is required. |
| **state**  string | State of the network.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Tags assosiated with the networks. Set this to `{}` to clear any tags. |
| **uuid**  string | UUID of the network.  Either *name* or *uuid* is required. |
| **zone**  string | Zone slug of the network (e.g. `lpg1` or `rma1`). |

## [Notes](network_module.md#id3)

> **Note:**
>
> - All operations are performed using the cloudscale.ch public API v1.
> - For details consult the full API documentation: <https://www.cloudscale.ch/en/api/v1>.
> - A valid API token is required for all operations. You can create as many tokens as you like using the cloudscale.ch control panel at <https://control.cloudscale.ch>.

## [Examples](network_module.md#id4)

```yaml+jinja
---
- name: Ensure network exists
  cloudscale_ch.cloud.network:
    name: my network
    api_token: xxxxxx

- name: Ensure network in a specific zone
  cloudscale_ch.cloud.network:
    name: my network
    zone: lpg1
    api_token: xxxxxx

- name: Ensure a network is absent
  cloudscale_ch.cloud.network:
    name: my network
    state: absent
    api_token: xxxxxx
```

## [Return Values](network_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **created_at**  string | The creation date and time of the network.  Returned: success  Sample: `"2019-05-29T13:18:42.511407Z"` |
| **href**  string | API URL to get details about this network.  Returned: success  Sample: `"https://api.cloudscale.ch/v1/networks/cfde831a-4e87-4a75-960f-89b0148aa2cc"` |
| **mtu**  integer | The MTU of the network.  Returned: success  Sample: `9000` |
| **name**  string | The name of the network.  Returned: success  Sample: `"my network"` |
| **state**  string | State of the network.  Returned: success  Sample: `"present"` |
| **subnets**  complex | A list of subnets objects of the network.  Returned: success |
| **cidr**  string | The CIDR of the subnet.  Returned: success  Sample: `"172.16.0.0/24"` |
| **href**  string | API URL to get details about the subnet.  Returned: success  Sample: `"https://api.cloudscale.ch/v1/subnets/33333333-1864-4608-853a-0771b6885a3"` |
| **uuid**  string | The unique identifier for the subnet.  Returned: success  Sample: `"33333333-1864-4608-853a-0771b6885a3"` |
| **tags**  dictionary | Tags assosiated with the network.  Returned: success  Sample: `{"project": "my project"}` |
| **uuid**  string | The unique identifier for the network.  Returned: success  Sample: `"cfde831a-4e87-4a75-960f-89b0148aa2cc"` |
| **zone**  dictionary | The zone of the network.  Returned: success  Sample: `{"slug": "rma1"}` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/cloudscale-ch/ansible-collection-cloudscale/issues)
[Repository (Sources)](https://github.com/cloudscale-ch/ansible-collection-cloudscale)
