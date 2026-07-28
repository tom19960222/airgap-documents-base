---
collection: ansible
version: "8"
title: "hetzner.hcloud.hcloud_volume module – Create and manage block Volume on the Hetzner Cloud."
source_url: https://docs.ansible.com/projects/ansible/8/collections/hetzner/hcloud/hcloud_volume_module.html
fetched_at: 2026-07-28T02:34:15+00:00
---
# hetzner.hcloud.hcloud_volume module – Create and manage block Volume on the Hetzner Cloud.

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
> see [Requirements](hcloud_volume_module.md#ansible-collections-hetzner-hcloud-hcloud-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_volume`.

- [Synopsis](hcloud_volume_module.md#synopsis)
- [Requirements](hcloud_volume_module.md#requirements)
- [Parameters](hcloud_volume_module.md#parameters)
- [See Also](hcloud_volume_module.md#see-also)
- [Examples](hcloud_volume_module.md#examples)
- [Return Values](hcloud_volume_module.md#return-values)

## [Synopsis](hcloud_volume_module.md#id1)

- Create, update and attach/detach block Volume on the Hetzner Cloud.

## [Requirements](hcloud_volume_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-dateutil >= 2.7.5
- requests >=2.20

## [Parameters](hcloud_volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **automount**  boolean | Automatically mount the Volume.  **Choices:**   - `false` ← (default) - `true` |
| **delete_protection**  boolean | Protect the Volume for deletion.  **Choices:**   - `false` - `true` |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  **Default:** `"https://api.hetzner.cloud/v1"` |
| **format**  string | Automatically Format the volume on creation  Can only be used in case the Volume does not exist.  **Choices:**   - `"xfs"` - `"ext4"` |
| **id**  integer | The ID of the Hetzner Cloud Block Volume to manage.  Only required if no volume *name* is given |
| **labels**  dictionary | User-defined key-value pairs. |
| **location**  string | Location of the Hetzner Cloud Volume.  Required if no *server* is given and Volume does not exist. |
| **name**  string | The Name of the Hetzner Cloud Block Volume to manage.  Only required if no volume *id* is given or a volume does not exist. |
| **server**  string | Server Name the Volume should be assigned to.  Required if no *location* is given and Volume does not exist. |
| **size**  integer | The size of the Block Volume in GB.  Required if volume does not yet exists. |
| **state**  string | State of the Volume.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [See Also](hcloud_volume_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_volume_module.md#id5)

```yaml+jinja
- name: Create a Volume
  hcloud_volume:
    name: my-volume
    location: fsn1
    size: 100
    state: present
- name: Create a Volume and format it with ext4
  hcloud_volume:
    name: my-volume
    location: fsn
    format: ext4
    size: 100
    state: present
- name: Mount a existing Volume and automount
  hcloud_volume:
    name: my-volume
    server: my-server
    automount: true
    state: present
- name: Mount a existing Volume and automount
  hcloud_volume:
    name: my-volume
    server: my-server
    automount: true
    state: present
- name: Ensure the Volume is absent (remove if needed)
  hcloud_volume:
    name: my-volume
    state: absent
```

## [Return Values](hcloud_volume_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_volume**  complex | The block Volume  **Returned:** Always |
| **delete_protection**  boolean  *added in hetzner.hcloud 0.1.0* | True if Volume is protected for deletion  **Returned:** always  **Sample:** `false` |
| **id**  integer | ID of the Volume  **Returned:** Always  **Sample:** `12345` |
| **labels**  dictionary | User-defined labels (key-value pairs)  **Returned:** Always  **Sample:** `{"key": "value", "mylabel": 123}` |
| **linux_device**  string  *added in hetzner.hcloud 0.1.0* | Path to the device that contains the Volume.  **Returned:** always  **Sample:** `"/dev/disk/by-id/scsi-0HC_Volume_12345"` |
| **location**  string | Location name where the Volume is located at  **Returned:** Always  **Sample:** `"fsn1"` |
| **name**  string | Name of the Volume  **Returned:** Always  **Sample:** `"my-volume"` |
| **server**  string | Server name where the Volume is attached to  **Returned:** Always  **Sample:** `"my-server"` |
| **size**  integer | Size in GB of the Volume  **Returned:** Always  **Sample:** `1337` |

### Authors

- Christopher Schmitt (@cschmitt-hcloud)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
- [Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
