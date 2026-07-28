---
collection: ansible
version: "6"
title: "ngine_io.vultr.vultr_block_storage module – Manages block storage volumes on Vultr."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/vultr/vultr_block_storage_module.html
fetched_at: 2026-07-28T00:16:02+00:00
---
# ngine_io.vultr.vultr_block_storage module – Manages block storage volumes on Vultr.

> **Note:**
>
> This module is part of the [ngine_io.vultr collection](https://galaxy.ansible.com/ngine_io/vultr) (version 1.1.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.vultr`.
> You need further requirements to be able to use this module,
> see [Requirements](vultr_block_storage_module.md#ansible-collections-ngine-io-vultr-vultr-block-storage-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.vultr.vultr_block_storage`.

New in ngine_io.vultr 0.1.0

- [Synopsis](vultr_block_storage_module.md#synopsis)
- [Requirements](vultr_block_storage_module.md#requirements)
- [Parameters](vultr_block_storage_module.md#parameters)
- [Notes](vultr_block_storage_module.md#notes)
- [Examples](vultr_block_storage_module.md#examples)
- [Return Values](vultr_block_storage_module.md#return-values)

## [Synopsis](vultr_block_storage_module.md#id1)

- Manage block storage volumes on Vultr.

## [Requirements](vultr_block_storage_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](vultr_block_storage_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_account**  string | Name of the ini section in the `vultr.ini` file.  The ENV variable `VULTR_API_ACCOUNT` is used as default, when defined.  Default: `"default"` |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  The ENV variable `VULTR_API_ENDPOINT` is used as default, when defined.  Fallback value is <https://api.vultr.com> if not specified. |
| **api_key**  string | API key of the Vultr API.  The ENV variable `VULTR_API_KEY` is used as default, when defined. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  The ENV variable `VULTR_API_RETRIES` is used as default, when defined.  Fallback value is 5 retries if not specified. |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  The ENV variable `VULTR_API_RETRY_MAX_DELAY` is used as default, when defined.  Fallback value is 12 seconds. |
| **api_timeout**  integer | HTTP timeout to Vultr API.  The ENV variable `VULTR_API_TIMEOUT` is used as default, when defined.  Fallback value is 60 seconds if not specified. |
| **attached_to_SUBID**  aliases: attached_to_id  integer | The ID of the server the volume is attached to.  Required if *state* is attached. |
| **live_attachment**  boolean | Whether the volume should be attached/detached, even if the server not stopped.  Choices:   - `false` - `true` ← (default) |
| **name**  aliases: description, label  string / required | Name of the block storage volume. |
| **region**  string | Region the block storage volume is deployed into.  Required if *state* is present. |
| **size**  integer | Size of the block storage volume in GB.  Required if *state* is present.  If it’s larger than the volume’s current size, the volume will be resized. |
| **state**  string | State of the block storage volume.  Choices:   - `"present"` ← (default) - `"absent"` - `"attached"` - `"detached"` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  Choices:   - `false` - `true` ← (default) |

## [Notes](vultr_block_storage_module.md#id4)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](vultr_block_storage_module.md#id5)

```yaml+jinja
- name: Ensure a block storage volume is present
  ngine_io.vultr.vultr_block_storage:
    name: myvolume
    size: 10
    region: Amsterdam

- name: Ensure a block storage volume is absent
  ngine_io.vultr.vultr_block_storage:
    name: myvolume
    state: absent

- name: Ensure a block storage volume exists and is attached to server 114
  ngine_io.vultr.vultr_block_storage:
    name: myvolume
    state: attached
    attached_to_id: 114
    size: 10

- name: Ensure a block storage volume exists and is not attached to any server
  ngine_io.vultr.vultr_block_storage:
    name: myvolume
    state: detached
    size: 10
```

## [Return Values](vultr_block_storage_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  complex | Response from Vultr API with a few additions/modification  Returned: success |
| **api_account**  string | Account used in the ini file to select the key  Returned: success  Sample: `"default"` |
| **api_endpoint**  string | Endpoint used for the API requests  Returned: success  Sample: `"https://api.vultr.com"` |
| **api_retries**  integer | Amount of max retries for the API requests  Returned: success  Sample: `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  Returned: success  Sample: `12` |
| **api_timeout**  integer | Timeout used for the API requests  Returned: success  Sample: `60` |
| **vultr_block_storage**  complex | Response from Vultr API  Returned: success |
| **attached_to_id**  string | The ID of the server the volume is attached to  Returned: success  Sample: `"10194376"` |
| **cost_per_month**  float | Cost per month for the volume  Returned: success  Sample: `1.0` |
| **date_created**  string | Date when the volume was created  Returned: success  Sample: `"2017-08-26 12:47:48"` |
| **id**  string | ID of the block storage volume  Returned: success  Sample: `"1234abcd"` |
| **name**  string | Name of the volume  Returned: success  Sample: `"ansible-test-volume"` |
| **region**  string | Region the volume was deployed into  Returned: success  Sample: `"New Jersey"` |
| **size**  integer | Information about the volume size in GB  Returned: success  Sample: `10` |
| **status**  string | Status about the deployment of the volume  Returned: success  Sample: `"active"` |

### Authors

- Yanis Guenane (@Spredzy)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-vultr/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-vultr)
