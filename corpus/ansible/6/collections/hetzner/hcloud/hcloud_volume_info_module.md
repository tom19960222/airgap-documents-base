---
collection: ansible
version: "6"
title: "hetzner.hcloud.hcloud_volume_info module – Gather infos about your Hetzner Cloud Volumes."
source_url: https://docs.ansible.com/projects/ansible/6/collections/hetzner/hcloud/hcloud_volume_info_module.html
fetched_at: 2026-07-27T17:49:56+00:00
---
# hetzner.hcloud.hcloud_volume_info module – Gather infos about your Hetzner Cloud Volumes.

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
> see [Requirements](hcloud_volume_info_module.md#ansible-collections-hetzner-hcloud-hcloud-volume-info-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_volume_info`.

- [Synopsis](hcloud_volume_info_module.md#synopsis)
- [Requirements](hcloud_volume_info_module.md#requirements)
- [Parameters](hcloud_volume_info_module.md#parameters)
- [See Also](hcloud_volume_info_module.md#see-also)
- [Examples](hcloud_volume_info_module.md#examples)
- [Return Values](hcloud_volume_info_module.md#return-values)

## [Synopsis](hcloud_volume_info_module.md#id1)

- Gather infos about your Hetzner Cloud Volumes.

## [Requirements](hcloud_volume_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.0.0

## [Parameters](hcloud_volume_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  Default: `"https://api.hetzner.cloud/v1"` |
| **id**  integer | The ID of the Volume you want to get. |
| **label_selector**  string | The label selector for the Volume you want to get. |
| **name**  string | The name of the Volume you want to get. |

## [See Also](hcloud_volume_info_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_volume_info_module.md#id5)

```yaml+jinja
- name: Gather hcloud Volume infos
  hcloud_volume_info:
  register: output
- name: Print the gathered infos
  debug:
    var: output.hcloud_volume_info
```

## [Return Values](hcloud_volume_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_volume_info**  complex | The Volume infos as list  Returned: always |
| **delete_protection**  boolean  added in hetzner.hcloud 0.1.0 | True if the Volume is protected for deletion  Returned: always |
| **id**  integer | Numeric identifier of the Volume  Returned: always  Sample: `1937415` |
| **labels**  dictionary | User-defined labels (key-value pairs)  Returned: always |
| **linux_device**  string  added in hetzner.hcloud 0.1.0 | Path to the device that contains the Volume.  Returned: always  Sample: `"/dev/disk/by-id/scsi-0HC_Volume_12345"` |
| **location**  string | Name of the location where the Volume resides in  Returned: always  Sample: `"fsn1"` |
| **name**  string | Name of the Volume  Returned: always  Sample: `"my-volume"` |
| **server**  string | Name of the server where the Volume is attached to  Returned: always  Sample: `"my-server"` |
| **size**  string | Size of the Volume  Returned: always  Sample: `"10"` |

### Authors

- Lukas Kaemmerling (@LKaemmerling)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
[Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
