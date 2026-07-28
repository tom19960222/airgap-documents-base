---
collection: ansible
version: "8"
title: "vultr.cloud.snapshot module – Manages snapshots on Vultr"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vultr/cloud/snapshot_module.html
fetched_at: 2026-07-28T02:58:59+00:00
---
# vultr.cloud.snapshot module – Manages snapshots on Vultr

> **Note:**
>
> This module is part of the [vultr.cloud collection](https://galaxy.ansible.com/ui/repo/published/vultr/cloud/) (version 1.11.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vultr.cloud`.
>
> To use it in a playbook, specify: `vultr.cloud.snapshot`.

New in vultr.cloud 1.7.0

- [Synopsis](snapshot_module.md#synopsis)
- [Parameters](snapshot_module.md#parameters)
- [Notes](snapshot_module.md#notes)
- [Examples](snapshot_module.md#examples)
- [Return Values](snapshot_module.md#return-values)

## [Synopsis](snapshot_module.md#id1)

- Create and remove snapshots.

## [Parameters](snapshot_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  **Default:** `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  **Default:** `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  **Default:** `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  **Default:** `180` |
| **description**  aliases: name  string / required | Description of the snapshot. |
| **instance**  string | The description or ID of the instance from which to take the snapshot.  Mutually exclusive with *url*.  *instance* or *url* is required if *state=present*. |
| **state**  string | State of the snapshot.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **url**  string | The URL of the snapshot image (RAW) to be uploaded.  Mutually exclusive with *instance*.  *instance* or *url* is required if *state=present*. |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](snapshot_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](snapshot_module.md#id4)

```yaml+jinja
- name: Ensure a snapshot is present
  vultr.cloud.snapshot:
    description: my snapshot of my instance
    instance: my instance

- name: Ensure a snapshot is present
  vultr.cloud.snapshot:
    description: debian 11 generic
    url: https://cloud.debian.org/images/cloud/bullseye/latest/debian-11-generic-amd64.raw

- name: Ensure a snapshot is absent
  vultr.cloud.snapshot:
    description: my snapshot of my instance
    state: absent
```

## [Return Values](snapshot_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  **Returned:** success |
| **api_endpoint**  string | Endpoint used for the API requests.  **Returned:** success  **Sample:** `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  **Returned:** success  **Sample:** `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  **Returned:** success  **Sample:** `12` |
| **api_timeout**  integer | Timeout used for the API requests.  **Returned:** success  **Sample:** `60` |
| **vultr_snapshot**  dictionary | Response from Vultr API.  **Returned:** success |
| **app_id**  integer | ID of the app.  **Returned:** success  **Sample:** `0` |
| **compressed_size**  integer | Compressed size of the snapshot.  **Returned:** success  **Sample:** `949678560` |
| **date_created**  string | Date the snapshot was created.  **Returned:** success  **Sample:** `"2020-10-10T01:56:20+00:00"` |
| **description**  string | Description of the snapshot.  **Returned:** success  **Sample:** `"my vpc"` |
| **id**  string | ID of the snapshot.  **Returned:** success  **Sample:** `"cb676a46-66fd-4dfb-b839-443f2e6c0b60"` |
| **os_id**  integer | ID of the OS.  **Returned:** success  **Sample:** `215` |
| **size**  integer | Size of the snapshot.  **Returned:** success  **Sample:** `42949672960` |
| **status**  string | Status of the snapshot.  **Returned:** success  **Sample:** `"complete"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
