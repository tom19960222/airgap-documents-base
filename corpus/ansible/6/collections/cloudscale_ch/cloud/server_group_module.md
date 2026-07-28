---
collection: ansible
version: "6"
title: "cloudscale_ch.cloud.server_group module – Manages server groups on the cloudscale.ch IaaS service"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cloudscale_ch/cloud/server_group_module.html
fetched_at: 2026-07-27T17:03:07+00:00
---
# cloudscale_ch.cloud.server_group module – Manages server groups on the cloudscale.ch IaaS service

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
> To use it in a playbook, specify: `cloudscale_ch.cloud.server_group`.

New in cloudscale_ch.cloud 1.0.0

- [Synopsis](server_group_module.md#synopsis)
- [Parameters](server_group_module.md#parameters)
- [Notes](server_group_module.md#notes)
- [Examples](server_group_module.md#examples)
- [Return Values](server_group_module.md#return-values)

## [Synopsis](server_group_module.md#id1)

- Create, update and remove server groups.

## [Parameters](server_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | Timeout in seconds for calls to the cloudscale.ch API.  This can also be passed in the `CLOUDSCALE_API_TIMEOUT` environment variable.  Default: `45` |
| **api_token**  string / required | cloudscale.ch API token.  This can also be passed in the `CLOUDSCALE_API_TOKEN` environment variable. |
| **api_url**  string  added in cloudscale_ch.cloud 1.3.0 | cloudscale.ch API URL.  This can also be passed in the `CLOUDSCALE_API_URL` environment variable.  Default: `"https://api.cloudscale.ch/v1"` |
| **name**  string | Name of the server group.  Either *name* or *uuid* is required. These options are mutually exclusive. |
| **state**  string | State of the server group.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Tags assosiated with the server groups. Set this to `{}` to clear any tags. |
| **type**  string | Type of the server group.  Default: `"anti-affinity"` |
| **uuid**  string | UUID of the server group.  Either *name* or *uuid* is required. These options are mutually exclusive. |
| **zone**  string | Zone slug of the server group (e.g. `lpg1` or `rma1`). |

## [Notes](server_group_module.md#id3)

> **Note:**
>
> - All operations are performed using the cloudscale.ch public API v1.
> - For details consult the full API documentation: <https://www.cloudscale.ch/en/api/v1>.
> - A valid API token is required for all operations. You can create as many tokens as you like using the cloudscale.ch control panel at <https://control.cloudscale.ch>.

## [Examples](server_group_module.md#id4)

```yaml+jinja
---
- name: Ensure server group exists
  cloudscale_ch.cloud.server_group:
    name: my-name
    type: anti-affinity
    api_token: xxxxxx

- name: Ensure server group in a specific zone
  cloudscale_ch.cloud.server_group:
    name: my-rma-group
    type: anti-affinity
    zone: lpg1
    api_token: xxxxxx

- name: Ensure a server group is absent
  cloudscale_ch.cloud.server_group:
    name: my-name
    state: absent
    api_token: xxxxxx
```

## [Return Values](server_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **href**  string | API URL to get details about this server group  Returned: if available  Sample: `"https://api.cloudscale.ch/v1/server-group/cfde831a-4e87-4a75-960f-89b0148aa2cc"` |
| **name**  string | The display name of the server group  Returned: always  Sample: `"load balancers"` |
| **servers**  list / elements=string | A list of servers that are part of the server group.  Returned: if available  Sample: `[]` |
| **state**  string | State of the server group.  Returned: always  Sample: `"present"` |
| **tags**  dictionary | Tags assosiated with the server group.  Returned: success  Sample: `{"project": "my project"}` |
| **type**  string | The type the server group  Returned: if available  Sample: `"anti-affinity"` |
| **uuid**  string | The unique identifier for this server  Returned: always  Sample: `"cfde831a-4e87-4a75-960f-89b0148aa2cc"` |
| **zone**  dictionary | The zone of the server group  Returned: success  Sample: `{"slug": "rma1"}` |

### Authors

- René Moser (@resmo)
- Denis Krienbühl (@href)

### Collection links

[Issue Tracker](https://github.com/cloudscale-ch/ansible-collection-cloudscale/issues)
[Repository (Sources)](https://github.com/cloudscale-ch/ansible-collection-cloudscale)
