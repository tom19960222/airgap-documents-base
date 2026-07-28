---
collection: ansible
version: "8"
title: "community.general.packet_volume module – Create/delete a volume in Packet host"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/packet_volume_module.html
fetched_at: 2026-07-28T01:48:51+00:00
---
# community.general.packet_volume module – Create/delete a volume in Packet host

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](packet_volume_module.md#ansible-collections-community-general-packet-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.packet_volume`.

New in community.general 0.2.0

- [Synopsis](packet_volume_module.md#synopsis)
- [Requirements](packet_volume_module.md#requirements)
- [Parameters](packet_volume_module.md#parameters)
- [Attributes](packet_volume_module.md#attributes)
- [Examples](packet_volume_module.md#examples)
- [Return Values](packet_volume_module.md#return-values)

## [Synopsis](packet_volume_module.md#id1)

- Create/delete a volume in Packet host.
- API is documented at <https://www.packet.com/developers/api/#volumes>.

Aliases: cloud.packet.packet_volume

## [Requirements](packet_volume_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- packet-python >= 1.35

## [Parameters](packet_volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_token**  string | Packet API token. You can also supply it in environment variable `PACKET_API_TOKEN`. |
| **billing_cycle**  string | Billing cycle for new volume.  **Choices:**   - `"hourly"` ← (default) - `"monthly"` |
| **description**  string | User-defined description attribute for Packet volume.  It is used used as idempotent identifier - if volume with given description exists, new one is not created. |
| **facility**  string | Location of the volume.  Volumes can only be attached to device in the same location. |
| **id**  string | UUID of a volume. |
| **locked**  boolean | Create new volume locked.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | Selector for API-generated name of the volume |
| **plan**  string | storage_1 for standard tier, storage_2 for premium (performance) tier.  Tiers are described at <https://www.packet.com/cloud/storage/>.  **Choices:**   - `"storage_1"` ← (default) - `"storage_2"` |
| **project_id**  string / required | ID of project of the device. |
| **size**  integer | Size of the volume in gigabytes. |
| **snapshot_policy**  dictionary | Snapshot policy for new volume. |
| **snapshot_count**  integer / required | How many snapshots to keep, a positive integer. |
| **snapshot_frequency**  string / required | Frequency of snapshots.  **Choices:**   - `"15min"` - `"1hour"` - `"1day"` - `"1week"` - `"1month"` - `"1year"` |
| **state**  string | Desired state of the volume.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Attributes](packet_volume_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](packet_volume_module.md#id5)

```yaml+jinja
# All the examples assume that you have your Packet API token in env var PACKET_API_TOKEN.
# You can also pass the api token in module param auth_token.

- hosts: localhost
  vars:
    volname: testvol123
    project_id: 53000fb2-ee46-4673-93a8-de2c2bdba33b

  tasks:
    - name: Create volume
      community.general.packet_volume:
        description: "{{ volname }}"
        project_id: "{{ project_id }}"
        facility: 'ewr1'
        plan: 'storage_1'
        state: present
        size: 10
        snapshot_policy:
          snapshot_count: 10
          snapshot_frequency: 1day
      register: result_create

    - name: Delete volume
      community.general.packet_volume:
        id: "{{ result_create.id }}"
        project_id: "{{ project_id }}"
        state: absent
```

## [Return Values](packet_volume_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | The user-defined description of the volume resource.  **Returned:** success  **Sample:** `"Just another volume"` |
| **id**  string | UUID of specified volume  **Returned:** success  **Sample:** `"53000fb2-ee46-4673-93a8-de2c2bdba33c"` |
| **name**  string | The API-generated name of the volume resource.  **Returned:** if volume is attached/detached to/from some device  **Sample:** `"volume-a91dc506"` |

### Authors

- Tomas Karasek (@t0mk)
- Nurfet Becirevic (@nurfet-becirevic)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
