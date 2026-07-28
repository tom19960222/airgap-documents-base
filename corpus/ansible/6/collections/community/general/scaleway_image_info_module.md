---
collection: ansible
version: "6"
title: "community.general.scaleway_image_info module – Gather information about the Scaleway images available"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/scaleway_image_info_module.html
fetched_at: 2026-07-27T17:12:56+00:00
---
# community.general.scaleway_image_info module – Gather information about the Scaleway images available

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.scaleway_image_info`.

- [Synopsis](scaleway_image_info_module.md#synopsis)
- [Parameters](scaleway_image_info_module.md#parameters)
- [Notes](scaleway_image_info_module.md#notes)
- [Examples](scaleway_image_info_module.md#examples)
- [Return Values](scaleway_image_info_module.md#return-values)

## [Synopsis](scaleway_image_info_module.md#id1)

- Gather information about the Scaleway images available.

## [Parameters](scaleway_image_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  Default: `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL.  Default: `"https://api.scaleway.com"` |
| **query_parameters**  dictionary | List of parameters passed to the query string.  Default: `{}` |
| **region**  string / required | Scaleway compute zone  Choices:   - `"ams1"` - `"EMEA-NL-EVS"` - `"par1"` - `"EMEA-FR-PAR1"` - `"par2"` - `"EMEA-FR-PAR2"` - `"waw1"` - `"EMEA-PL-WAW1"` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  Choices:   - `false` - `true` ← (default) |

## [Notes](scaleway_image_info_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence `SCW_TOKEN`, `SCW_API_KEY`, `SCW_OAUTH_TOKEN` or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_image_info_module.md#id4)

```yaml+jinja
- name: Gather Scaleway images information
  community.general.scaleway_image_info:
    region: par1
  register: result

- ansible.builtin.debug:
    msg: "{{ result.scaleway_image_info }}"
```

## [Return Values](scaleway_image_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **scaleway_image_info**  list / elements=dictionary | Response from Scaleway API.  For more details please refer to: <https://developers.scaleway.com/en/products/instance/api/>.  Returned: success  Sample: `{"scaleway_image_info": [{"arch": "x86_64", "creation_date": "2018-07-17T16:18:49.276456+00:00", "default_bootscript": {"architecture": "x86_64", "bootcmdargs": "LINUX_COMMON scaleway boot=local nbd.max_part=16", "default": false, "dtb": "", "id": "15fbd2f7-a0f9-412b-8502-6a44da8d98b8", "initrd": "http://169.254.42.24/initrd/initrd-Linux-x86_64-v3.14.5.gz", "kernel": "http://169.254.42.24/kernel/x86_64-mainline-lts-4.9-4.9.93-rev1/vmlinuz-4.9.93", "organization": "11111111-1111-4111-8111-111111111111", "public": true, "title": "x86_64 mainline 4.9.93 rev1"}, "extra_volumes": [], "from_server": null, "id": "00ae4a88-3252-4eda-9feb-5f6b56bf5ef0", "modification_date": "2018-07-17T16:42:06.319315+00:00", "name": "Debian Stretch", "organization": "51b656e3-4865-41e8-adbc-0c45bdd780db", "public": true, "root_volume": {"id": "da32dfbb-c5ff-476d-ae2d-c297dd09b7dd", "name": "snapshot-2a7229dc-d431-4dc5-b66e-95db08b773af-2018-07-17_16:18", "size": 25000000000, "volume_type": "l_ssd"}, "state": "available"}]}` |

### Authors

- Yanis Guenane (@Spredzy)
- Remy Leone (@remyleone)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
