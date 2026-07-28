---
collection: ansible
version: "8"
title: "hetzner.hcloud.hcloud_iso_info module – Gather infos about the Hetzner Cloud ISO list."
source_url: https://docs.ansible.com/projects/ansible/8/collections/hetzner/hcloud/hcloud_iso_info_module.html
fetched_at: 2026-07-28T02:33:59+00:00
---
# hetzner.hcloud.hcloud_iso_info module – Gather infos about the Hetzner Cloud ISO list.

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
> see [Requirements](hcloud_iso_info_module.md#ansible-collections-hetzner-hcloud-hcloud-iso-info-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_iso_info`.

- [Synopsis](hcloud_iso_info_module.md#synopsis)
- [Requirements](hcloud_iso_info_module.md#requirements)
- [Parameters](hcloud_iso_info_module.md#parameters)
- [See Also](hcloud_iso_info_module.md#see-also)
- [Examples](hcloud_iso_info_module.md#examples)
- [Return Values](hcloud_iso_info_module.md#return-values)

## [Synopsis](hcloud_iso_info_module.md#id1)

- Gather infos about the Hetzner Cloud ISO list.

## [Requirements](hcloud_iso_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-dateutil >= 2.7.5
- requests >=2.20

## [Parameters](hcloud_iso_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **architecture**  string | Filter ISOs with compatible architecture.  **Choices:**   - `"x86"` - `"arm"` |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  **Default:** `"https://api.hetzner.cloud/v1"` |
| **id**  integer | The ID of the ISO image you want to get. |
| **include_architecture_wildcard**  boolean | Include ISOs with wildcard architecture (architecture is null).  Works only if architecture filter is specified.  **Choices:**   - `false` - `true` |
| **name**  string | The name of the ISO you want to get. |

## [See Also](hcloud_iso_info_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_iso_info_module.md#id5)

```yaml+jinja
- name: Gather hcloud ISO type infos
  hcloud_iso_info:
  register: output

- name: Print the gathered infos
  debug:
    var: output.hcloud_iso_info
```

## [Return Values](hcloud_iso_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_iso_info**  complex | The ISO type infos as list  **Returned:** always |
| **architecture**  string | Type of cpu architecture this ISO is compatible with. None indicates no restriction on the architecture (wildcard).  **Returned:** when supported  **Sample:** `"x86"` |
| **deprecated**  string | ISO 8601 timestamp of deprecation, None if ISO is still available. After the deprecation time it will no longer be possible to attach the ISO to servers.  **Returned:** always  **Sample:** `"2024-12-01T00:00:00+00:00"` |
| **description**  string | Description of the ISO  **Returned:** always  **Sample:** `"Debian 12.0 (amd64/netinstall)"` |
| **id**  integer | ID of the ISO  **Returned:** always  **Sample:** `22110` |
| **name**  string | Unique identifier of the ISO. Only set for public ISOs  **Returned:** always  **Sample:** `"debian-12.0.0-amd64-netinst.iso"` |
| **type**  string | Type of the ISO, can be one of `public`, `private`.  **Returned:** always  **Sample:** `"public"` |

### Authors

- Patrice Le Guyader (@patlegu)
- Lukas Kaemmerling (@LKaemmerling)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
- [Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
