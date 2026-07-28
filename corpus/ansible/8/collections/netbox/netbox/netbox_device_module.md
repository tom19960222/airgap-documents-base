---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_device module – Create, update or delete devices within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_device_module.html
fetched_at: 2026-07-28T02:44:59+00:00
---
# netbox.netbox.netbox_device module – Create, update or delete devices within NetBox

> **Note:**
>
> This module is part of the [netbox.netbox collection](https://galaxy.ansible.com/ui/repo/published/netbox/netbox/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netbox.netbox`.
> You need further requirements to be able to use this module,
> see [Requirements](netbox_device_module.md#ansible-collections-netbox-netbox-netbox-device-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_device`.

New in netbox.netbox 0.1.0

- [Synopsis](netbox_device_module.md#synopsis)
- [Requirements](netbox_device_module.md#requirements)
- [Parameters](netbox_device_module.md#parameters)
- [Notes](netbox_device_module.md#notes)
- [Examples](netbox_device_module.md#examples)
- [Return Values](netbox_device_module.md#return-values)

## [Synopsis](netbox_device_module.md#id1)

- Creates, updates or removes devices from NetBox

## [Requirements](netbox_device_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_device_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the device configuration |
| **airflow**  string  *added in netbox.netbox 3.10.0* | Airflow of the device  **Choices:**   - `"front-to-rear"` - `"rear-to-front"` - `"left-to-right"` - `"right-to-left"` - `"side-to-rear"` - `"passive"` - `"mixed"` |
| **asset_tag**  string | Asset tag that is associated to the device |
| **cluster**  any | Cluster that the device will be assigned to |
| **comments**  string | Comments that may include additional information in regards to the device |
| **custom_fields**  dictionary | must exist in NetBox |
| **description**  string  *added in netbox.netbox 3.10.0* | Description of the provider |
| **device_role**  any | Required if *state=present* and the device does not exist yet |
| **device_type**  any | Required if *state=present* and the device does not exist yet |
| **face**  string | Required if *rack* is defined  **Choices:**   - `"Front"` - `"front"` - `"Rear"` - `"rear"` |
| **local_context_data**  dictionary | Arbitrary JSON data to define the devices configuration variables. |
| **location**  any  *added in netbox.netbox 3.3.0* | The location the device will be associated to (NetBox 2.11+) |
| **name**  string / required | The name of the device |
| **oob_ip**  any  *added in netbox.netbox 3.15.0* | Out-of-band (OOB) IP address assigned to the device |
| **platform**  any | The platform of the device |
| **position**  integer | The position of the device in the rack defined above |
| **primary_ip4**  any | Primary IPv4 address assigned to the device |
| **primary_ip6**  any | Primary IPv6 address assigned to the device |
| **rack**  any | The name of the rack to assign the device to |
| **serial**  string | Serial number of the device |
| **site**  any | Required if *state=present* and the device does not exist yet |
| **status**  any | The status of the device |
| **tags**  list / elements=any | Any tags that the device may need to be associated with |
| **tenant**  any | The tenant that the device will be assigned to |
| **vc_position**  integer | Position in the assigned virtual chassis |
| **vc_priority**  integer | Priority in the assigned virtual chassis |
| **virtual_chassis**  any | Virtual chassis the device will be assigned to |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_device_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_device_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create device within NetBox with only required information
      netbox.netbox.netbox_device:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Device
          device_type: C9410R
          device_role: Core Switch
          site: Main
        state: present

    - name: Create device within NetBox with empty string name to generate UUID
      netbox.netbox.netbox_device:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: ""
          device_type: C9410R
          device_role: Core Switch
          site: Main
        state: present

    - name: Delete device within netbox
      netbox.netbox.netbox_device:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Device
        state: absent

    - name: Create device with tags
      netbox.netbox.netbox_device:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Another Test Device
          device_type: C9410R
          device_role: Core Switch
          site: Main
          local_context_data:
            bgp: "65000"
          tags:
            - Schnozzberry
        state: present

    - name: Update the rack and position of an existing device
      netbox.netbox.netbox_device:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Device
          rack: Test Rack
          position: 10
          face: Front
        state: present
```

## [Return Values](netbox_device_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **device**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** success (when *state=present*) |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |

### Authors

- Mikhail Yohman (@FragmentedPacket)
- David Gomez (@amb1s1)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
