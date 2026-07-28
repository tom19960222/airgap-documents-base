---
collection: ansible
version: "6"
title: "community.general.packet_volume_attachment module – Attach/detach a volume to a device in the Packet host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/packet_volume_attachment_module.html
fetched_at: 2026-07-27T17:11:43+00:00
---
# community.general.packet_volume_attachment module – Attach/detach a volume to a device in the Packet host

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](packet_volume_attachment_module.md#ansible-collections-community-general-packet-volume-attachment-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.packet_volume_attachment`.

New in community.general 0.2.0

- [Synopsis](packet_volume_attachment_module.md#synopsis)
- [Requirements](packet_volume_attachment_module.md#requirements)
- [Parameters](packet_volume_attachment_module.md#parameters)
- [Examples](packet_volume_attachment_module.md#examples)
- [Return Values](packet_volume_attachment_module.md#return-values)

## [Synopsis](packet_volume_attachment_module.md#id1)

- Attach/detach a volume to a device in the Packet host.
- API is documented at <https://www.packet.com/developers/api/volumes/>.
- This module creates the attachment route in the Packet API. In order to discover the block devices on the server, you have to run the Attach Scripts, as documented at <https://help.packet.net/technical/storage/packet-block-storage-linux>.

## [Requirements](packet_volume_attachment_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- packet-python >= 1.35

## [Parameters](packet_volume_attachment_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_token**  string | Packet API token. You can also supply it in env var `PACKET_API_TOKEN`. |
| **device**  string | Selector for the device.  It can be a UUID of the device, or a hostname.  Example values: 98a14f7a-3d27-4478-b7cf-35b5670523f3, “my device” |
| **project_id**  string / required | UUID of the project to which the device and volume belong. |
| **state**  string | Indicate desired state of the attachment.  Choices:   - `"present"` ← (default) - `"absent"` |
| **volume**  string / required | Selector for the volume.  It can be a UUID, an API-generated volume name, or user-defined description string.  Example values: 4a347482-b546-4f67-8300-fb5018ef0c5, volume-4a347482, “my volume” |

## [Examples](packet_volume_attachment_module.md#id4)

```yaml+jinja
# All the examples assume that you have your Packet API token in env var PACKET_API_TOKEN.
# You can also pass the api token in module param auth_token.

- hosts: localhost

  vars:
    volname: testvol
    devname: testdev
    project_id: 52000fb2-ee46-4673-93a8-de2c2bdba33b

  tasks:
    - name: Create volume
      packet_volume:
        description: "{{ volname }}"
        project_id: "{{ project_id }}"
        facility: ewr1
        plan: storage_1
        state: present
        size: 10
        snapshot_policy:
          snapshot_count: 10
          snapshot_frequency: 1day

    - name: Create a device
      packet_device:
        project_id: "{{ project_id }}"
        hostnames: "{{ devname }}"
        operating_system: ubuntu_16_04
        plan: baremetal_0
        facility: ewr1
        state: present

    - name: Attach testvol to testdev
      community.general.packet_volume_attachment:
        project_id: "{{ project_id }}"
        volume: "{{ volname }}"
        device: "{{ devname }}"

    - name: Detach testvol from testdev
      community.general.packet_volume_attachment:
        project_id: "{{ project_id }}"
        volume: "{{ volname }}"
        device: "{{ devname }}"
        state: absent
```

## [Return Values](packet_volume_attachment_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **device_id**  string | UUID of device addressed by the module call.  Returned: success |
| **volume_id**  string | UUID of volume addressed by the module call.  Returned: success |

### Authors

- Tomas Karasek (@t0mk)
- Nurfet Becirevic (@nurfet-becirevic)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
