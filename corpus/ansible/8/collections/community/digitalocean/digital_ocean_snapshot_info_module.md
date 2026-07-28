---
collection: ansible
version: "8"
title: "community.digitalocean.digital_ocean_snapshot_info module – Gather information about DigitalOcean Snapshot"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/digitalocean/digital_ocean_snapshot_info_module.html
fetched_at: 2026-07-28T01:43:13+00:00
---
# community.digitalocean.digital_ocean_snapshot_info module – Gather information about DigitalOcean Snapshot

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/ui/repo/published/community/digitalocean/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
> You need further requirements to be able to use this module,
> see [Requirements](digital_ocean_snapshot_info_module.md#ansible-collections-community-digitalocean-digital-ocean-snapshot-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_snapshot_info`.

- [Synopsis](digital_ocean_snapshot_info_module.md#synopsis)
- [Requirements](digital_ocean_snapshot_info_module.md#requirements)
- [Parameters](digital_ocean_snapshot_info_module.md#parameters)
- [Examples](digital_ocean_snapshot_info_module.md#examples)
- [Return Values](digital_ocean_snapshot_info_module.md#return-values)

## [Synopsis](digital_ocean_snapshot_info_module.md#id1)

- This module can be used to gather information about snapshot information based upon provided values such as droplet, volume and snapshot id.
- This module was called `digital_ocean_snapshot_facts` before Ansible 2.9. The usage did not change.

Aliases: digital_ocean_snapshot_facts

## [Requirements](digital_ocean_snapshot_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](digital_ocean_snapshot_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  **Default:** `"https://api.digitalocean.com/v2"` |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **snapshot_id**  string | To retrieve information about a snapshot, please specify this as a snapshot id.  If set to actual snapshot id, then information are gathered related to that particular snapshot only.  This is required parameter, if `snapshot_type` is set to `by_id`. |
| **snapshot_type**  string | Specifies the type of snapshot information to be retrieved.  If set to `droplet`, then information are gathered related to snapshots based on Droplets only.  If set to `volume`, then information are gathered related to snapshots based on volumes only.  If set to `by_id`, then information are gathered related to snapshots based on snapshot id only.  If not set to any of the above, then information are gathered related to all snapshots.  **Choices:**   - `"all"` ← (default) - `"droplet"` - `"volume"` - `"by_id"` |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  **Default:** `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](digital_ocean_snapshot_info_module.md#id4)

```yaml+jinja
- name: Gather information about all snapshots
  community.digitalocean.digital_ocean_snapshot_info:
    snapshot_type: all
    oauth_token: "{{ oauth_token }}"

- name: Gather information about droplet snapshots
  community.digitalocean.digital_ocean_snapshot_info:
    snapshot_type: droplet
    oauth_token: "{{ oauth_token }}"

- name: Gather information about volume snapshots
  community.digitalocean.digital_ocean_snapshot_info:
    snapshot_type: volume
    oauth_token: "{{ oauth_token }}"

- name: Gather information about snapshot by snapshot id
  community.digitalocean.digital_ocean_snapshot_info:
    snapshot_type: by_id
    snapshot_id: 123123123
    oauth_token: "{{ oauth_token }}"

- name: Get information about snapshot named big-data-snapshot1
  community.digitalocean.digital_ocean_snapshot_info:
  register: resp_out
- set_fact:
    snapshot_id: "{{ item.id }}"
  loop: "{{ resp_out.data | community.general.json_query(name) }}"
  vars:
    name: "[?name=='big-data-snapshot1']"
- debug:
    var: snapshot_id
```

## [Return Values](digital_ocean_snapshot_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  list / elements=dictionary | DigitalOcean snapshot information  **Returned:** success  **Sample:** `[{"created_at": "2016-09-28T23:14:30Z", "id": "4f60fc64-85d1-11e6-a004-000f53315871", "min_disk_size": 10, "name": "big-data-snapshot1", "regions": ["nyc1"], "resource_id": "89bcc42f-85cf-11e6-a004-000f53315871", "resource_type": "volume", "size_gigabytes": 0}]` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
