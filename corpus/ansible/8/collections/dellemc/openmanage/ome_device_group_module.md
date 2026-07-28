---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_device_group module – Add or remove device(s) from a static device group on OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_device_group_module.html
fetched_at: 2026-07-28T02:04:26+00:00
---
# dellemc.openmanage.ome_device_group module – Add or remove device(s) from a static device group on OpenManage Enterprise

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](ome_device_group_module.md#ansible-collections-dellemc-openmanage-ome-device-group-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_device_group`.

New in dellemc.openmanage 3.3.0

- [Synopsis](ome_device_group_module.md#synopsis)
- [Requirements](ome_device_group_module.md#requirements)
- [Parameters](ome_device_group_module.md#parameters)
- [Notes](ome_device_group_module.md#notes)
- [Examples](ome_device_group_module.md#examples)
- [Return Values](ome_device_group_module.md#return-values)

## [Synopsis](ome_device_group_module.md#id1)

- This module allows to add or remove device(s) from a static device group on OpenManage Enterprise.

## [Requirements](ome_device_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6
- netaddr >= 0.7.19

## [Parameters](ome_device_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **device_ids**  list / elements=integer | List of ID(s) of the device(s) to be added or removed from the device group.  *device_ids* is mutually exclusive with *device_service_tags* and *ip_addresses*. |
| **device_service_tags**  list / elements=string | List of service tag(s) of the device(s) to be added or removed from the device group.  *device_service_tags* is mutually exclusive with *device_ids* and *ip_addresses*. |
| **group_id**  integer | ID of the static device.  *group_id* is mutually exclusive with *name*. |
| **hostname**  string / required | OpenManage Enterprise IP address or hostname. |
| **ip_addresses**  list / elements=string | List of IPs of the device(s) to be added or removed from the device group.  *ip_addresses* is mutually exclusive with *device_ids* and *device_service_tags*.  Supported IP address range formats:  - 192.35.0.1 - 10.36.0.0-192.36.0.255 - 192.37.0.0/24 - fe80::ffff:ffff:ffff:ffff - fe80::ffff:192.0.2.0/125 - fe80::ffff:ffff:ffff:1111-fe80::ffff:ffff:ffff:ffff  `NOTE` Hostname is not supported.  `NOTE` *ip_addresses* requires python’s netaddr packages to work on IP Addresses.  `NOTE` This module reports success even if one of the IP addresses provided in the *ip_addresses* list is available in OpenManage Enterprise.The module reports failure only if none of the IP addresses provided in the list are available in OpenManage Enterprise. |
| **name**  string | Name of the static group.  *name* is mutually exclusive with *group_id*. |
| **password**  string / required | OpenManage Enterprise password. |
| **port**  integer | OpenManage Enterprise HTTPS port.  **Default:** `443` |
| **state**  string | `present` allows to add the device(s) to a static device group.  `absent` allows to remove the device(s) from a static device group.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_device_group_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_device_group_module.md#id5)

```yaml+jinja
---
- name: Add devices to a static device group by using the group name and device IDs
  dellemc.openmanage.ome_device_group:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    name: "Storage Services"
    device_ids:
      - 11111
      - 11112
      - 11113

- name: Add devices to a static device group by using the group name and device service tags
  dellemc.openmanage.ome_device_group:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    name: "Storage Services"
    device_service_tags:
      - GHRT2RL
      - KJHDF3S
      - LKIJNG6

- name: Add devices to a static device group by using the group ID and device service tags
  dellemc.openmanage.ome_device_group:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    group_id: 12345
    device_service_tags:
      - GHRT2RL
      - KJHDF3S

- name: Add devices to a static device group by using the group name and IPv4 addresses
  dellemc.openmanage.ome_device_group:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    name: "Storage Services"
    ip_addresses:
      - 192.35.0.1
      - 192.35.0.5

- name: Add devices to a static device group by using the group ID and IPv6 addresses
  dellemc.openmanage.ome_device_group:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    group_id: 12345
    ip_addresses:
      - fe80::ffff:ffff:ffff:ffff
      - fe80::ffff:ffff:ffff:2222

- name: Add devices to a static device group by using the group ID and supported IPv4 and IPv6 address formats.
  dellemc.openmanage.ome_device_group:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    group_id: 12345
    ip_addresses:
      - 192.35.0.1
      - 10.36.0.0-192.36.0.255
      - 192.37.0.0/24
      - fe80::ffff:ffff:ffff:ffff
      - ::ffff:192.0.2.0/125
      - fe80::ffff:ffff:ffff:1111-fe80::ffff:ffff:ffff:ffff

- name: Remove devices from a static device group by using the group name and device IDs
  dellemc.openmanage.ome_device_group:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "absent"
    name: "Storage Services"
    device_ids:
      - 11111
      - 11112
      - 11113

- name: Remove devices from a static device group by using the group name and device service tags
  dellemc.openmanage.ome_device_group:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "absent"
    name: "Storage Services"
    device_service_tags:
      - GHRT2RL
      - KJHDF3S
      - LKIJNG6

- name: Remove devices from a static device group by using the group ID and device service tags
  dellemc.openmanage.ome_device_group:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "absent"
    group_id: 12345
    device_service_tags:
      - GHRT2RL
      - KJHDF3S

- name: Remove devices from a static device group by using the group name and IPv4 addresses
  dellemc.openmanage.ome_device_group:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "absent"
    name: "Storage Services"
    ip_addresses:
      - 192.35.0.1
      - 192.35.0.5

- name: Remove devices from a static device group by using the group ID and IPv6 addresses
  dellemc.openmanage.ome_device_group:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "absent"
    group_id: 12345
    ip_addresses:
      - fe80::ffff:ffff:ffff:ffff
      - fe80::ffff:ffff:ffff:2222

- name: Remove devices from a static device group by using the group ID and supported IPv4 and IPv6 address formats.
  dellemc.openmanage.ome_device_group:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "absent"
    group_id: 12345
    ip_addresses:
      - 192.35.0.1
      - 10.36.0.0-192.36.0.255
      - 192.37.0.0/24
      - fe80::ffff:ffff:ffff:ffff
      - ::ffff:192.0.2.0/125
      - fe80::ffff:ffff:ffff:1111-fe80::ffff:ffff:ffff:ffff
```

## [Return Values](ome_device_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **group_id**  integer | ID of the group.  **Returned:** success  **Sample:** `21078` |
| **ip_addresses_added**  list / elements=string | IP Addresses which are added to the device group.  **Returned:** success  **Sample:** `["21078"]` |
| **msg**  string | Overall status of the device group settings.  **Returned:** always  **Sample:** `"['Successfully added member(s) to the device group.']"` |

### Authors

- Felix Stephen (@felixs88)
- Sajna Shetty(@Sajna-Shetty)
- Abhishek Sinha (@Abhishek-Dell)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
