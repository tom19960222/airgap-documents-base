---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_snapshot module – Create and delete DigitalOcean snapshots"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_snapshot_module.html
fetched_at: 2026-07-27T17:06:53+00:00
---
# community.digitalocean.digital_ocean_snapshot module – Create and delete DigitalOcean snapshots

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/community/digitalocean) (version 1.22.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_snapshot`.

New in community.digitalocean 1.7.0

- [Synopsis](digital_ocean_snapshot_module.md#synopsis)
- [Parameters](digital_ocean_snapshot_module.md#parameters)
- [Examples](digital_ocean_snapshot_module.md#examples)
- [Return Values](digital_ocean_snapshot_module.md#return-values)

## [Synopsis](digital_ocean_snapshot_module.md#id1)

- This module can be used to create and delete DigitalOcean Droplet and volume snapshots.

## [Parameters](digital_ocean_snapshot_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **droplet_id**  string | Droplet ID to snapshot. |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **snapshot_id**  string | Snapshot ID to delete. |
| **snapshot_name**  string | Name of the snapshot to create. |
| **snapshot_tags**  list / elements=string | List of tags to apply to the volume snapshot.  Only applies to volume snapshots (not Droplets). |
| **snapshot_type**  string | Specifies the type of snapshot information to be create or delete.  If set to `droplet`, then a Droplet snapshot is created.  If set to `volume`, then a volume snapshot is created.  Choices:   - `"droplet"` ← (default) - `"volume"` |
| **state**  string | Whether the snapshot should be present (created) or absent (deleted).  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **volume_id**  string | Volume ID to snapshot. |
| **wait**  boolean | Wait for the snapshot to be created before returning.  Choices:   - `false` - `true` ← (default) |
| **wait_timeout**  integer | How long before wait gives up, in seconds, when creating a snapshot.  Default: `120` |

## [Examples](digital_ocean_snapshot_module.md#id3)

```yaml+jinja
- name: Snapshot a Droplet
  community.digitalocean.digital_ocean_snapshot:
    state: present
    snapshot_type: droplet
    droplet_id: 250329179
  register: result

- name: Delete a Droplet snapshot
  community.digitalocean.digital_ocean_snapshot:
    state: absent
    snapshot_type: droplet
    snapshot_id: 85905825
  register: result

- name: Snapshot a Volume
  community.digitalocean.digital_ocean_snapshot:
    state: present
    snapshot_type: volume
    snapshot_name: mysnapshot1
    volume_id: 9db5e329-cc68-11eb-b027-0a58ac144f91

- name: Delete a Volume snapshot
  community.digitalocean.digital_ocean_snapshot:
    state: absent
    snapshot_type: volume
    snapshot_id: a902cdba-cc68-11eb-a701-0a58ac145708
```

## [Return Values](digital_ocean_snapshot_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Snapshot creation or deletion action.  Returned: success  Sample: `[{"completed_at": "2021-06-14T12:36:00Z", "id": 1229119156, "region": {"available": true, "features": ["backups", "ipv6", "metadata", "install_agent", "storage", "image_transfer"], "name": "New York 1", "sizes": ["s-1vcpu-1gb", "s-1vcpu-1gb-amd", "s-1vcpu-1gb-intel", "<snip>"], "slug": "nyc1"}, "region_slug": "nyc1", "resource_id": 250445117, "resource_type": "droplet", "started_at": "2021-06-14T12:35:25Z", "status": "completed", "type": "snapshot"}, {"created_at": "2021-06-14T12:55:10Z", "id": "c06d4a86-cd0f-11eb-b13c-0a58ac145472", "min_disk_size": 1, "name": "my-snapshot-1", "regions": ["nbg1"], "resource_id": "f0adea7e-cd0d-11eb-b027-0a58ac144f91", "resource_type": "volume", "size_gigabytes": 0, "tags": ["tag1", "tag2"]}]` |

### Authors

- Mark Mercado (@mamercad)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
