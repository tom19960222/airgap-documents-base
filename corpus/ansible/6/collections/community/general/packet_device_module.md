---
collection: ansible
version: "6"
title: "community.general.packet_device module – Manage a bare metal server in the Packet Host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/packet_device_module.html
fetched_at: 2026-07-27T17:11:40+00:00
---
# community.general.packet_device module – Manage a bare metal server in the Packet Host

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
> see [Requirements](packet_device_module.md#ansible-collections-community-general-packet-device-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.packet_device`.

- [Synopsis](packet_device_module.md#synopsis)
- [Requirements](packet_device_module.md#requirements)
- [Parameters](packet_device_module.md#parameters)
- [Notes](packet_device_module.md#notes)
- [Examples](packet_device_module.md#examples)
- [Return Values](packet_device_module.md#return-values)

## [Synopsis](packet_device_module.md#id1)

- Manage a bare metal server in the Packet Host (a “device” in the API terms).
- When the machine is created it can optionally wait for public IP address, or for active state.
- This module has a dependency on packet >= 1.0.
- API is documented at <https://www.packet.net/developers/api/devices>.

## [Requirements](packet_device_module.md#id2)

The below requirements are needed on the host that executes this module.

- packet-python >= 1.35

## [Parameters](packet_device_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **always_pxe**  boolean | Persist PXE as the first boot option.  Normally, the PXE process happens only on the first boot. Set this arg to have your device continuously boot to iPXE.  Choices:   - `false` ← (default) - `true` |
| **auth_token**  string | Packet API token. You can also supply it in env var `PACKET_API_TOKEN`. |
| **count**  integer | The number of devices to create. Count number can be included in hostname via the %d string formatter.  Default: `1` |
| **count_offset**  integer | From which number to start the count.  Default: `1` |
| **device_ids**  list / elements=string | List of device IDs on which to operate. |
| **facility**  string | Facility slug for device creation. See Packet API for current list - <https://www.packet.net/developers/api/facilities/>. |
| **features**  dictionary | Dict with “features” for device creation. See Packet API docs for details. |
| **hostnames**  aliases: name  list / elements=string | A hostname of a device, or a list of hostnames.  If given string or one-item list, you can use the `"%d"` Python string format to expand numbers from *count*.  If only one hostname, it might be expanded to list if *count*>1. |
| **ipxe_script_url**  string | URL of custom iPXE script for provisioning.  More about custom iPXE for Packet devices at <https://help.packet.net/technical/infrastructure/custom-ipxe>.  Default: `""` |
| **locked**  aliases: lock  boolean | Whether to lock a created device.  Choices:   - `false` ← (default) - `true` |
| **operating_system**  string | OS slug for device creation. See Packet API for current list - <https://www.packet.net/developers/api/operatingsystems/>. |
| **plan**  string | Plan slug for device creation. See Packet API for current list - <https://www.packet.net/developers/api/plans/>. |
| **project_id**  string / required | ID of project of the device. |
| **state**  string | Desired state of the device.  If set to `present` (the default), the module call will return immediately after the device-creating HTTP request successfully returns.  If set to `active`, the module call will block until all the specified devices are in state active due to the Packet API, or until *wait_timeout*.  Choices:   - `"present"` ← (default) - `"absent"` - `"active"` - `"inactive"` - `"rebooted"` |
| **tags**  list / elements=string  added in community.general 0.2.0 | List of device tags.  Currently implemented only for device creation. |
| **user_data**  string | Userdata blob made available to the machine |
| **wait_for_public_IPv**  integer | Whether to wait for the instance to be assigned a public IPv4/IPv6 address.  If set to 4, it will wait until IPv4 is assigned to the instance.  If set to 6, wait until public IPv6 is assigned to the instance.  Choices:   - `4` - `6` |
| **wait_timeout**  integer | How long (seconds) to wait either for automatic IP address assignment, or for the device to reach the `active` *state*.  If *wait_for_public_IPv* is set and *state* is `active`, the module will wait for both events consequently, applying the timeout twice.  Default: `900` |

## [Notes](packet_device_module.md#id4)

> **Note:**
>
> - Doesn’t support check mode.

## [Examples](packet_device_module.md#id5)

```yaml+jinja
# All the examples assume that you have your Packet API token in env var PACKET_API_TOKEN.
# You can also pass it to the auth_token parameter of the module instead.

# Creating devices

- name: Create 1 device
  hosts: localhost
  tasks:
  - community.general.packet_device:
      project_id: 89b497ee-5afc-420a-8fb5-56984898f4df
      hostnames: myserver
      tags: ci-xyz
      operating_system: ubuntu_16_04
      plan: baremetal_0
      facility: sjc1

# Create the same device and wait until it is in state "active", (when it's
# ready for other API operations). Fail if the device is not "active" in
# 10 minutes.

- name: Create device and wait up to 10 minutes for active state
  hosts: localhost
  tasks:
  - community.general.packet_device:
      project_id: 89b497ee-5afc-420a-8fb5-56984898f4df
      hostnames: myserver
      operating_system: ubuntu_16_04
      plan: baremetal_0
      facility: sjc1
      state: active
      wait_timeout: 600

- name: Create 3 ubuntu devices called server-01, server-02 and server-03
  hosts: localhost
  tasks:
  - community.general.packet_device:
      project_id: 89b497ee-5afc-420a-8fb5-56984898f4df
      hostnames: server-%02d
      count: 3
      operating_system: ubuntu_16_04
      plan: baremetal_0
      facility: sjc1

- name: Create 3 coreos devices with userdata, wait until they get IPs and then wait for SSH
  hosts: localhost
  tasks:
  - name: Create 3 devices and register their facts
    community.general.packet_device:
      hostnames: [coreos-one, coreos-two, coreos-three]
      operating_system: coreos_stable
      plan: baremetal_0
      facility: ewr1
      locked: true
      project_id: 89b497ee-5afc-420a-8fb5-56984898f4df
      wait_for_public_IPv: 4
      user_data: |
        #cloud-config
        ssh_authorized_keys:
          - {{ lookup('file', 'my_packet_sshkey') }}
        coreos:
          etcd:
            discovery: https://discovery.etcd.io/6a28e078895c5ec737174db2419bb2f3
            addr: $private_ipv4:4001
            peer-addr: $private_ipv4:7001
          fleet:
            public-ip: $private_ipv4
          units:
            - name: etcd.service
              command: start
            - name: fleet.service
              command: start
    register: newhosts

  - name: Wait for ssh
    ansible.builtin.wait_for:
      delay: 1
      host: "{{ item.public_ipv4 }}"
      port: 22
      state: started
      timeout: 500
    with_items: "{{ newhosts.devices }}"

# Other states of devices

- name: Remove 3 devices by uuid
  hosts: localhost
  tasks:
  - community.general.packet_device:
      project_id: 89b497ee-5afc-420a-8fb5-56984898f4df
      state: absent
      device_ids:
        - 1fb4faf8-a638-4ac7-8f47-86fe514c30d8
        - 2eb4faf8-a638-4ac7-8f47-86fe514c3043
        - 6bb4faf8-a638-4ac7-8f47-86fe514c301f
```

## [Return Values](packet_device_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | True if a device was altered in any way (created, modified or removed)  Returned: success  Sample: `true` |
| **devices**  list / elements=string | Information about each device that was processed  Returned: success  Sample: `[{"hostname": "my-server.com", "id": "2a5122b9-c323-4d5c-b53c-9ad3f54273e7", "locked": false, "private-ipv4": "10.0.15.12", "public_ipv4": "147.229.15.12", "public_ipv6": "2604:1380:2:5200::3", "state": "provisioning", "tags": []}]` |

### Authors

- Tomas Karasek (@t0mk)
- Matt Baldwin (@baldwinSPC)
- Thibaud Morel l’Horset (@teebes)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
