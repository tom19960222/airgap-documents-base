---
collection: ansible
version: "8"
title: "community.general.dimensiondata_network module – Create, update, and delete MCP 1.0 & 2.0 networks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/dimensiondata_network_module.html
fetched_at: 2026-07-28T01:45:21+00:00
---
# community.general.dimensiondata_network module – Create, update, and delete MCP 1.0 & 2.0 networks

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.dimensiondata_network`.

- [Synopsis](dimensiondata_network_module.md#synopsis)
- [Parameters](dimensiondata_network_module.md#parameters)
- [Attributes](dimensiondata_network_module.md#attributes)
- [Examples](dimensiondata_network_module.md#examples)
- [Return Values](dimensiondata_network_module.md#return-values)

## [Synopsis](dimensiondata_network_module.md#id1)

- Create, update, and delete MCP 1.0 & 2.0 networks

Aliases: cloud.dimensiondata.dimensiondata_network

## [Parameters](dimensiondata_network_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | Additional description of the network domain. |
| **location**  string / required | The target datacenter. |
| **mcp_password**  string | The password used to authenticate to the CloudControl API.  If not specified, will fall back to `MCP_PASSWORD` from environment variable or `~/.dimensiondata`.  Required if `mcp_user` is specified. |
| **mcp_user**  string | The username used to authenticate to the CloudControl API.  If not specified, will fall back to `MCP_USER` from environment variable or `~/.dimensiondata`. |
| **name**  string / required | The name of the network domain to create. |
| **region**  string | The target region.  Regions are defined in Apache libcloud project [libcloud/common/dimensiondata.py]  They are also listed in <https://libcloud.readthedocs.io/en/latest/compute/drivers/dimensiondata.html>  Note that the default value “na” stands for “North America”.  The module prepends ‘dd-’ to the region choice.  **Default:** `"na"` |
| **service_plan**  string | The service plan, either “ESSENTIALS” or “ADVANCED”.  MCP 2.0 Only.  **Choices:**   - `"ESSENTIALS"` ← (default) - `"ADVANCED"` |
| **state**  string | Should the resource be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only be used on private instances of the CloudControl API that use self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Should we wait for the task to complete before moving onto the next.  **Choices:**   - `false` ← (default) - `true` |
| **wait_poll_interval**  integer | The amount of time (in seconds) to wait between checks for task completion.  Only applicable if `wait=true`.  **Default:** `2` |
| **wait_time**  integer | The maximum amount of time (in seconds) to wait for the task to complete.  Only applicable if `wait=true`.  **Default:** `600` |

## [Attributes](dimensiondata_network_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](dimensiondata_network_module.md#id4)

```yaml+jinja
- name: Create an MCP 1.0 network
  community.general.dimensiondata_network:
    region: na
    location: NA5
    name: mynet

- name: Create an MCP 2.0 network
  community.general.dimensiondata_network:
    region: na
    mcp_user: my_user
    mcp_password: my_password
    location: NA9
    name: mynet
    service_plan: ADVANCED

- name: Delete a network
  community.general.dimensiondata_network:
    region: na
    location: NA1
    name: mynet
    state: absent
```

## [Return Values](dimensiondata_network_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **network**  complex | Dictionary describing the network.  **Returned:** On success when `state=present`. |
| **description**  string | Network description.  **Returned:** success  **Sample:** `"My network description"` |
| **id**  string | Network ID.  **Returned:** success  **Sample:** `"8c787000-a000-4050-a215-280893411a7d"` |
| **location**  string | Datacenter location.  **Returned:** success  **Sample:** `"NA3"` |
| **multicast**  boolean | Multicast enabled? (MCP 1.0 only)  **Returned:** success  **Sample:** `false` |
| **name**  string | Network name.  **Returned:** success  **Sample:** `"My network"` |
| **private_net**  string | Private network subnet. (MCP 1.0 only)  **Returned:** success  **Sample:** `"10.2.3.0"` |
| **status**  string | Network status. (MCP 2.0 only)  **Returned:** success  **Sample:** `"NORMAL"` |

### Authors

- Aimon Bustardo (@aimonb)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
