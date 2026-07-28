---
collection: ansible
version: "8"
title: "community.general.scaleway_server_info module – Gather information about the Scaleway servers available"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/scaleway_server_info_module.html
fetched_at: 2026-07-28T01:50:23+00:00
---
# community.general.scaleway_server_info module – Gather information about the Scaleway servers available

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
> To use it in a playbook, specify: `community.general.scaleway_server_info`.

- [Synopsis](scaleway_server_info_module.md#synopsis)
- [Parameters](scaleway_server_info_module.md#parameters)
- [Attributes](scaleway_server_info_module.md#attributes)
- [Notes](scaleway_server_info_module.md#notes)
- [Examples](scaleway_server_info_module.md#examples)
- [Return Values](scaleway_server_info_module.md#return-values)

## [Synopsis](scaleway_server_info_module.md#id1)

- Gather information about the Scaleway servers available.

Aliases: cloud.scaleway.scaleway_server_info

## [Parameters](scaleway_server_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  **Default:** `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL.  **Default:** `"https://api.scaleway.com"` |
| **query_parameters**  dictionary | List of parameters passed to the query string.  **Default:** `{}` |
| **region**  string / required | Scaleway region to use (for example `par1`).  **Choices:**   - `"ams1"` - `"EMEA-NL-EVS"` - `"par1"` - `"EMEA-FR-PAR1"` - `"par2"` - `"EMEA-FR-PAR2"` - `"waw1"` - `"EMEA-PL-WAW1"` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](scaleway_server_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](scaleway_server_info_module.md#id4)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence [`SCW_TOKEN`](../../environment_variables.md#envvar-SCW_TOKEN), [`SCW_API_KEY`](../../environment_variables.md#envvar-SCW_API_KEY), [`SCW_OAUTH_TOKEN`](../../environment_variables.md#envvar-SCW_OAUTH_TOKEN) or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_server_info_module.md#id5)

```yaml+jinja
- name: Gather Scaleway servers information
  community.general.scaleway_server_info:
    region: par1
  register: result

- ansible.builtin.debug:
    msg: "{{ result.scaleway_server_info }}"
```

## [Return Values](scaleway_server_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **scaleway_server_info**  list / elements=dictionary | Response from Scaleway API.  For more details please refer to: <https://developers.scaleway.com/en/products/instance/api/>.  **Returned:** success  **Sample:** `{"scaleway_server_info": [{"arch": "x86_64", "boot_type": "local", "bootscript": {"architecture": "x86_64", "bootcmdargs": "LINUX_COMMON scaleway boot=local nbd.max_part=16", "default": true, "dtb": "", "id": "b1e68c26-a19c-4eac-9222-498b22bd7ad9", "initrd": "http://169.254.42.24/initrd/initrd-Linux-x86_64-v3.14.5.gz", "kernel": "http://169.254.42.24/kernel/x86_64-mainline-lts-4.4-4.4.127-rev1/vmlinuz-4.4.127", "organization": "11111111-1111-4111-8111-111111111111", "public": true, "title": "x86_64 mainline 4.4.127 rev1"}, "commercial_type": "START1-XS", "creation_date": "2018-08-14T21:36:56.271545+00:00", "dynamic_ip_required": false, "enable_ipv6": false, "extra_networks": [], "hostname": "scw-e0d256", "id": "12f19bc7-108c-4517-954c-e6b3d0311363", "image": {"arch": "x86_64", "creation_date": "2018-04-26T12:42:21.619844+00:00", "default_bootscript": {"architecture": "x86_64", "bootcmdargs": "LINUX_COMMON scaleway boot=local nbd.max_part=16", "default": true, "dtb": "", "id": "b1e68c26-a19c-4eac-9222-498b22bd7ad9", "initrd": "http://169.254.42.24/initrd/initrd-Linux-x86_64-v3.14.5.gz", "kernel": "http://169.254.42.24/kernel/x86_64-mainline-lts-4.4-4.4.127-rev1/vmlinuz-4.4.127", "organization": "11111111-1111-4111-8111-111111111111", "public": true, "title": "x86_64 mainline 4.4.127 rev1"}, "extra_volumes": [], "from_server": null, "id": "67375eb1-f14d-4f02-bb42-6119cecbde51", "modification_date": "2018-04-26T12:49:07.573004+00:00", "name": "Ubuntu Xenial", "organization": "51b656e3-4865-41e8-adbc-0c45bdd780db", "public": true, "root_volume": {"id": "020b8d61-3867-4a0e-84a4-445c5393e05d", "name": "snapshot-87fc282d-f252-4262-adad-86979d9074cf-2018-04-26_12:42", "size": 25000000000, "volume_type": "l_ssd"}, "state": "available"}, "ipv6": null, "location": {"cluster_id": "5", "hypervisor_id": "412", "node_id": "2", "platform_id": "13", "zone_id": "par1"}, "maintenances": [], "modification_date": "2018-08-14T21:37:28.630882+00:00", "name": "scw-e0d256", "organization": "3f709602-5e6c-4619-b80c-e841c89734af", "private_ip": "10.14.222.131", "protected": false, "public_ip": {"address": "163.172.170.197", "dynamic": false, "id": "ea081794-a581-4495-8451-386ddaf0a451"}, "security_group": {"id": "a37379d2-d8b0-4668-9cfb-1233fc436f7e", "name": "Default security group"}, "state": "running", "state_detail": "booted", "tags": [], "volumes": {"0": {"creation_date": "2018-08-14T21:36:56.271545+00:00", "export_uri": "device://dev/vda", "id": "68386fae-4f55-4fbf-aabb-953036a85872", "modification_date": "2018-08-14T21:36:56.271545+00:00", "name": "snapshot-87fc282d-f252-4262-adad-86979d9074cf-2018-04-26_12:42", "organization": "3f709602-5e6c-4619-b80c-e841c89734af", "server": {"id": "12f19bc7-108c-4517-954c-e6b3d0311363", "name": "scw-e0d256"}, "size": 25000000000, "state": "available", "volume_type": "l_ssd"}}}]}` |

### Authors

- Yanis Guenane (@Spredzy)
- Remy Leone (@remyleone)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
