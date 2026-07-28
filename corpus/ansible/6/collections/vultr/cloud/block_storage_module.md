---
collection: ansible
version: "6"
title: "vultr.cloud.block_storage module – Manages block storage volumes on Vultr"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vultr/cloud/block_storage_module.html
fetched_at: 2026-07-28T00:22:56+00:00
---
# vultr.cloud.block_storage module – Manages block storage volumes on Vultr

> **Note:**
>
> This module is part of the [vultr.cloud collection](https://galaxy.ansible.com/vultr/cloud) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vultr.cloud`.
>
> To use it in a playbook, specify: `vultr.cloud.block_storage`.

New in vultr.cloud 1.0.0

- [Synopsis](block_storage_module.md#synopsis)
- [Parameters](block_storage_module.md#parameters)
- [Notes](block_storage_module.md#notes)
- [Examples](block_storage_module.md#examples)
- [Return Values](block_storage_module.md#return-values)

## [Synopsis](block_storage_module.md#id1)

- Manage block storage volumes.

## [Parameters](block_storage_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  Default: `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  Default: `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  Default: `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  Default: `60` |
| **attached_to_instance**  string | The ID of the server instance the volume is attached to. |
| **block_type**  string  added in vultr.cloud 1.2.0 | The type of block storage volume that will be created.  Choices:   - `"high_perf"` ← (default) - `"storage_opt"` |
| **label**  aliases: name  string / required | Name of the block storage volume. |
| **live**  boolean | Whether the volume should be attached/detached without restarting the instance.  Choices:   - `false` ← (default) - `true` |
| **region**  string | Region the block storage volume is deployed into.  Required if *state* is present. |
| **size_gb**  aliases: size  integer | Size of the block storage volume in GB.  Required if *state* is present.  If it is larger than the volume’s current size, the volume will be resized. |
| **state**  string | State of the block storage volume.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  Choices:   - `false` - `true` ← (default) |

## [Notes](block_storage_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](block_storage_module.md#id4)

```yaml+jinja
---
- name: Ensure a block storage volume is present
  vultr.cloud.block_storage:
    name: myvolume
    size_gb: 10
    block_type: storage_opt
    region: ams

- name: Ensure a block storage volume is absent
  vultr.cloud.block_storage:
    name: myvolume
    state: absent

- name: Ensure a block storage volume exists and is attached a server instance
  vultr.cloud.block_storage:
    name: myvolume
    attached_to_instance: cb676a46-66fd-4dfb-b839-443f2e6c0b60
    size_gb: 50
    block_type: high_perf

- name: Ensure a block storage volume exists but is not attached to any server instance
  vultr.cloud.block_storage:
    name: myvolume
    attached_to_instance: ""
    size_gb: 50
    block_type: high_perf
```

## [Return Values](block_storage_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  Returned: success |
| **api_account**  string | Account used in the ini file to select the key.  Returned: success  Sample: `"default"` |
| **api_endpoint**  string | Endpoint used for the API requests.  Returned: success  Sample: `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  Returned: success  Sample: `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  Returned: success  Sample: `12` |
| **api_timeout**  integer | Timeout used for the API requests.  Returned: success  Sample: `60` |
| **vultr_block_storage**  dictionary | Response from Vultr API.  Returned: success |
| **attached_to_instance**  string | The ID of the server instance the volume is attached to.  Returned: success  Sample: `"cb676a46-66fd-4dfb-b839-443f2e6c0b60"` |
| **block_type**  string | HDD or NVMe (storage_opt or high_perf)  Returned: success  Sample: `"high_perf"` |
| **cost**  float | Cost per month for the volume.  Returned: success  Sample: `1.0` |
| **date_created**  string | Date when the volume was created.  Returned: success  Sample: `"2020-10-10T01:56:20+00:00"` |
| **id**  string | ID of the block storage volume.  Returned: success  Sample: `"cb676a46-66fd-4dfb-b839-443f2e6c0b60"` |
| **label**  string | Label of the volume.  Returned: success  Sample: `"my volume"` |
| **mount_id**  string | Mount ID of the volume.  Returned: success  Sample: `"ewr-2f5d7a314fe44f"` |
| **region**  string | Region the volume was deployed into.  Returned: success  Sample: `"ews"` |
| **size_gb**  integer | Information about the volume size in GB.  Returned: success  Sample: `50` |
| **status**  string | Status about the deployment of the volume.  Returned: success  Sample: `"active"` |

### Authors

- René Moser (@resmo)
- Yanis Guenane (@Spredzy)

### Collection links

[Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
[Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
