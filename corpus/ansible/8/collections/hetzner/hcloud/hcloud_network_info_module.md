---
collection: ansible
version: "8"
title: "hetzner.hcloud.hcloud_network_info module – Gather info about your Hetzner Cloud networks."
source_url: https://docs.ansible.com/projects/ansible/8/collections/hetzner/hcloud/hcloud_network_info_module.html
fetched_at: 2026-07-28T02:34:06+00:00
---
# hetzner.hcloud.hcloud_network_info module – Gather info about your Hetzner Cloud networks.

> **Note:**
>
> This module is part of the [hetzner.hcloud collection](https://galaxy.ansible.com/ui/repo/published/hetzner/hcloud/) (version 1.16.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hetzner.hcloud`.
> You need further requirements to be able to use this module,
> see [Requirements](hcloud_network_info_module.md#ansible-collections-hetzner-hcloud-hcloud-network-info-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_network_info`.

- [Synopsis](hcloud_network_info_module.md#synopsis)
- [Requirements](hcloud_network_info_module.md#requirements)
- [Parameters](hcloud_network_info_module.md#parameters)
- [See Also](hcloud_network_info_module.md#see-also)
- [Examples](hcloud_network_info_module.md#examples)
- [Return Values](hcloud_network_info_module.md#return-values)

## [Synopsis](hcloud_network_info_module.md#id1)

- Gather info about your Hetzner Cloud networks.

## [Requirements](hcloud_network_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-dateutil >= 2.7.5
- requests >=2.20

## [Parameters](hcloud_network_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  **Default:** `"https://api.hetzner.cloud/v1"` |
| **id**  integer | The ID of the network you want to get. |
| **label_selector**  string | The label selector for the network you want to get. |
| **name**  string | The name of the network you want to get. |

## [See Also](hcloud_network_info_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_network_info_module.md#id5)

```yaml+jinja
- name: Gather hcloud network info
  local_action:
    module: hcloud_network_info

- name: Print the gathered info
  debug:
    var: hcloud_network_info
```

## [Return Values](hcloud_network_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_network_info**  complex | The network info as list  **Returned:** always |
| **delete_protection**  boolean  *added in hetzner.hcloud 0.1.0* | True if the network is protected for deletion  **Returned:** always |
| **expose_routes_to_vswitch**  boolean | Indicates if the routes from this network should be exposed to the vSwitch connection.  **Returned:** always  **Sample:** `false` |
| **id**  integer | Numeric identifier of the network  **Returned:** always  **Sample:** `1937415` |
| **ip_range**  string | IP range of the network  **Returned:** always  **Sample:** `"10.0.0.0/16"` |
| **labels**  dictionary | Labels of the network  **Returned:** always |
| **name**  string | Name of the network  **Returned:** always  **Sample:** `"awesome-network"` |
| **routes**  complex | Routes belonging to the network  **Returned:** always |
| **gateway**  string | Gateway of this route  **Returned:** always  **Sample:** `"10.0.0.1"` |
| **ip_range**  string | Destination network or host of this route.  **Returned:** always  **Sample:** `"10.0.0.0/16"` |
| **servers**  complex | Servers attached to the network  **Returned:** always |
| **backup_window**  boolean | Time window (UTC) in which the backup will run, or null if the backups are not enabled  **Returned:** always  **Sample:** `"22-02"` |
| **datacenter**  string | Name of the datacenter of the server  **Returned:** always  **Sample:** `"fsn1-dc14"` |
| **id**  integer | Numeric identifier of the server  **Returned:** always  **Sample:** `1937415` |
| **ipv4_address**  string | Public IPv4 address of the server, None if not existing  **Returned:** always  **Sample:** `"116.203.104.109"` |
| **ipv6**  string | IPv6 network of the server, None if not existing  **Returned:** always  **Sample:** `"2a01:4f8:1c1c:c140::/64"` |
| **labels**  dictionary | User-defined labels (key-value pairs)  **Returned:** always |
| **location**  string | Name of the location of the server  **Returned:** always  **Sample:** `"fsn1"` |
| **name**  string | Name of the server  **Returned:** always  **Sample:** `"my-server"` |
| **rescue_enabled**  boolean | True if rescue mode is enabled, Server will then boot into rescue system on next reboot  **Returned:** always  **Sample:** `false` |
| **server_type**  string | Name of the server type of the server  **Returned:** always  **Sample:** `"cx11"` |
| **status**  string | Status of the server  **Returned:** always  **Sample:** `"running"` |
| **subnetworks**  complex | Subnetworks belonging to the network  **Returned:** always |
| **gateway**  string | Gateway of this subnetwork  **Returned:** always  **Sample:** `"10.0.0.1"` |
| **ip_range**  string | IP range of the subnetwork  **Returned:** always  **Sample:** `"10.0.0.0/24"` |
| **network_zone**  string | Network of the subnetwork.  **Returned:** always  **Sample:** `"eu-central"` |
| **type**  string | Type of the subnetwork.  **Returned:** always  **Sample:** `"cloud"` |

### Authors

- Christopher Schmitt (@cschmitt-hcloud)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
- [Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
