---
collection: ansible
version: "6"
title: "hetzner.hcloud.hcloud_server_info module – Gather infos about your Hetzner Cloud servers."
source_url: https://docs.ansible.com/projects/ansible/6/collections/hetzner/hcloud/hcloud_server_info_module.html
fetched_at: 2026-07-27T17:49:51+00:00
---
# hetzner.hcloud.hcloud_server_info module – Gather infos about your Hetzner Cloud servers.

> **Note:**
>
> This module is part of the [hetzner.hcloud collection](https://galaxy.ansible.com/hetzner/hcloud) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hetzner.hcloud`.
> You need further requirements to be able to use this module,
> see [Requirements](hcloud_server_info_module.md#ansible-collections-hetzner-hcloud-hcloud-server-info-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_server_info`.

- [Synopsis](hcloud_server_info_module.md#synopsis)
- [Requirements](hcloud_server_info_module.md#requirements)
- [Parameters](hcloud_server_info_module.md#parameters)
- [See Also](hcloud_server_info_module.md#see-also)
- [Examples](hcloud_server_info_module.md#examples)
- [Return Values](hcloud_server_info_module.md#return-values)

## [Synopsis](hcloud_server_info_module.md#id1)

- Gather infos about your Hetzner Cloud servers.
- This module was called `hcloud_server_facts` before Ansible 2.9, returning `ansible_facts` and `hcloud_server_facts`. Note that the [hetzner.hcloud.hcloud_server_info](hcloud_server_info_module.md#ansible-collections-hetzner-hcloud-hcloud-server-info-module) module no longer returns `ansible_facts` and the value was renamed to `hcloud_server_info`!

## [Requirements](hcloud_server_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.0.0

## [Parameters](hcloud_server_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  Default: `"https://api.hetzner.cloud/v1"` |
| **id**  integer | The ID of the server you want to get. |
| **label_selector**  string | The label selector for the server you want to get. |
| **name**  string | The name of the server you want to get. |

## [See Also](hcloud_server_info_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_server_info_module.md#id5)

```yaml+jinja
- name: Gather hcloud server infos
  hcloud_server_info:
  register: output

- name: Print the gathered infos
  debug:
    var: output.hcloud_server_info
```

## [Return Values](hcloud_server_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_server_info**  complex | The server infos as list  Returned: always |
| **backup_window**  boolean | Time window (UTC) in which the backup will run, or null if the backups are not enabled  Returned: always  Sample: `"22-02"` |
| **datacenter**  string | Name of the datacenter of the server  Returned: always  Sample: `"fsn1-dc14"` |
| **delete_protection**  boolean  added in hetzner.hcloud 0.1.0 | True if server is protected for deletion  Returned: always  Sample: `false` |
| **id**  integer | Numeric identifier of the server  Returned: always  Sample: `1937415` |
| **ipv4_address**  string | Public IPv4 address of the server  Returned: always  Sample: `"116.203.104.109"` |
| **ipv6**  string | IPv6 network of the server  Returned: always  Sample: `"2a01:4f8:1c1c:c140::/64"` |
| **labels**  dictionary | User-defined labels (key-value pairs)  Returned: always |
| **location**  string | Name of the location of the server  Returned: always  Sample: `"fsn1"` |
| **name**  string | Name of the server  Returned: always  Sample: `"my-server"` |
| **placement_group**  string  added in hetzner.hcloud 1.5.0 | Placement Group of the server  Returned: always  Sample: `"4711"` |
| **private_networks**  list / elements=string | List of private networks the server is attached to (name)  Returned: always  Sample: `["my-network", "another-network"]` |
| **rebuild_protection**  boolean  added in hetzner.hcloud 0.1.0 | True if server is protected for rebuild  Returned: always  Sample: `false` |
| **rescue_enabled**  boolean | True if rescue mode is enabled, Server will then boot into rescue system on next reboot  Returned: always  Sample: `false` |
| **server_type**  string | Name of the server type of the server  Returned: always  Sample: `"cx11"` |
| **status**  string | Status of the server  Returned: always  Sample: `"running"` |

### Authors

- Lukas Kaemmerling (@LKaemmerling)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
[Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
