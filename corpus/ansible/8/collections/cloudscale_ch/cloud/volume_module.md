---
collection: ansible
version: "8"
title: "cloudscale_ch.cloud.volume module – Manages volumes on the cloudscale.ch IaaS service."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cloudscale_ch/cloud/volume_module.html
fetched_at: 2026-07-28T01:40:01+00:00
---
# cloudscale_ch.cloud.volume module – Manages volumes on the cloudscale.ch IaaS service.

> **Note:**
>
> This module is part of the [cloudscale_ch.cloud collection](https://galaxy.ansible.com/ui/repo/published/cloudscale_ch/cloud/) (version 2.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cloudscale_ch.cloud`.
>
> To use it in a playbook, specify: `cloudscale_ch.cloud.volume`.

New in cloudscale_ch.cloud 1.0.0

- [Synopsis](volume_module.md#synopsis)
- [Parameters](volume_module.md#parameters)
- [Notes](volume_module.md#notes)
- [Examples](volume_module.md#examples)
- [Return Values](volume_module.md#return-values)

## [Synopsis](volume_module.md#id1)

- Create, attach/detach, update and delete volumes on the cloudscale.ch IaaS service.

Aliases: cloudscale_volume

## [Parameters](volume_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | Timeout in seconds for calls to the cloudscale.ch API.  This can also be passed in the `CLOUDSCALE_API_TIMEOUT` environment variable.  **Default:** `45` |
| **api_token**  string / required | cloudscale.ch API token.  This can also be passed in the `CLOUDSCALE_API_TOKEN` environment variable. |
| **api_url**  string  *added in cloudscale_ch.cloud 1.3.0* | cloudscale.ch API URL.  This can also be passed in the `CLOUDSCALE_API_URL` environment variable.  **Default:** `"https://api.cloudscale.ch/v1"` |
| **name**  string | Name of the volume. Either name or UUID must be present to change an existing volume. |
| **servers**  aliases: server_uuids, server_uuid  list / elements=string | UUIDs of the servers this volume is attached to. Set this to `[]` to detach the volume. Currently a volume can only be attached to a single server.  The aliases `server_uuids` and `server_uuid` are deprecated and will be removed in version 3.0.0 of this collection. |
| **size_gb**  integer | Size of the volume in GB. |
| **state**  string | State of the volume.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Tags associated with the volume. Set this to `{}` to clear any tags. |
| **type**  string | Type of the volume. Cannot be changed after creating the volume. Defaults to `ssd` on volume creation.  **Choices:**   - `"ssd"` - `"bulk"` |
| **uuid**  string | UUID of the volume. Either name or UUID must be present to change an existing volume. |
| **zone**  string | Zone in which the volume resides (e.g. `lpg1` or `rma1`). Cannot be changed after creating the volume. Defaults to the project default zone. |

## [Notes](volume_module.md#id3)

> **Note:**
>
> - To create a new volume at least the *name* and *size_gb* options are required.
> - A volume can be created and attached to a server in the same task.
> - All operations are performed using the cloudscale.ch public API v1.
> - For details consult the full API documentation: <https://www.cloudscale.ch/en/api/v1>.
> - A valid API token is required for all operations. You can create as many tokens as you like using the cloudscale.ch control panel at <https://control.cloudscale.ch>.

## [Examples](volume_module.md#id4)

```yaml+jinja
# Create a new SSD volume
- name: Create an SSD volume
  cloudscale_ch.cloud.volume:
    name: my_ssd_volume
    zone: 'lpg1'
    size_gb: 50
    api_token: xxxxxx
  register: my_ssd_volume

# Attach an existing volume to a server
- name: Attach volume to server
  cloudscale_ch.cloud.volume:
    uuid: "{{ my_ssd_volume.uuid }}"
    servers:
      - ea3b39a3-77a8-4d0b-881d-0bb00a1e7f48
    api_token: xxxxxx

# Create and attach a volume to a server
- name: Create and attach volume to server
  cloudscale_ch.cloud.volume:
    name: my_ssd_volume
    zone: 'lpg1'
    size_gb: 50
    servers:
      - ea3b39a3-77a8-4d0b-881d-0bb00a1e7f48
    api_token: xxxxxx

# Detach volume from server
- name: Detach volume from server
  cloudscale_ch.cloud.volume:
    uuid: "{{ my_ssd_volume.uuid }}"
    servers: []
    api_token: xxxxxx

# Delete a volume
- name: Delete volume
  cloudscale_ch.cloud.volume:
    name: my_ssd_volume
    state: absent
    api_token: xxxxxx
```

## [Return Values](volume_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **href**  string | The API URL to get details about this volume.  **Returned:** state == present  **Sample:** `"https://api.cloudscale.ch/v1/volumes/2db69ba3-1864-4608-853a-0771b6885a3a"` |
| **name**  string | The display name of the volume.  **Returned:** state == present  **Sample:** `"my_ssd_volume"` |
| **server_uuids**  list / elements=string | The UUIDs of the servers this volume is attached to. This return value is deprecated and will disappear in the future when the field is removed from the API.  **Returned:** state == present  **Sample:** `["47cec963-fcd2-482f-bdb6-24461b2d47b1"]` |
| **servers**  list / elements=string | The list of servers this volume is attached to.  **Returned:** state == present  **Sample:** `[{"href": "https://api.cloudscale.ch/v1/servers/47cec963-fcd2-482f-bdb6-24461b2d47b1", "name": "my_server", "uuid": "47cec963-fcd2-482f-bdb6-24461b2d47b1"}]` |
| **size_gb**  string | The size of the volume in GB.  **Returned:** state == present  **Sample:** `"50"` |
| **state**  string | The current status of the volume.  **Returned:** success  **Sample:** `"present"` |
| **tags**  dictionary | Tags associated with the volume.  **Returned:** state == present  **Sample:** `{"project": "my project"}` |
| **type**  string | The type of the volume.  **Returned:** state == present  **Sample:** `"bulk"` |
| **uuid**  string | The unique identifier for this volume.  **Returned:** state == present  **Sample:** `"2db69ba3-1864-4608-853a-0771b6885a3a"` |
| **zone**  dictionary | The zone of the volume.  **Returned:** state == present  **Sample:** `{"slug": "lpg1"}` |

### Authors

- Gaudenz Steinlin (@gaudenz)
- René Moser (@resmo)
- Denis Krienbühl (@href)

### Collection links

- [Issue Tracker](https://github.com/cloudscale-ch/ansible-collection-cloudscale/issues)
- [Repository (Sources)](https://github.com/cloudscale-ch/ansible-collection-cloudscale)
