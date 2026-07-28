---
collection: ansible
version: "6"
title: "community.general.redfish_config module – Manages Out-Of-Band controllers using Redfish APIs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/redfish_config_module.html
fetched_at: 2026-07-27T17:12:37+00:00
---
# community.general.redfish_config module – Manages Out-Of-Band controllers using Redfish APIs

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.redfish_config`.

- [Synopsis](redfish_config_module.md#synopsis)
- [Parameters](redfish_config_module.md#parameters)
- [Examples](redfish_config_module.md#examples)
- [Return Values](redfish_config_module.md#return-values)

## [Synopsis](redfish_config_module.md#id1)

- Builds Redfish URIs locally and sends them to remote OOB controllers to set or update a configuration attribute.
- Manages BIOS configuration settings.
- Manages OOB controller configuration settings.

## [Parameters](redfish_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_token**  string  added in community.general 2.3.0 | Security token for authenticating to OOB controller. |
| **baseuri**  string / required | Base URI of OOB controller. |
| **bios_attributes**  dictionary  added in community.general 0.2.0 | Dictionary of BIOS attributes to update.  Default: `{}` |
| **boot_order**  list / elements=string  added in community.general 0.2.0 | List of BootOptionReference strings specifying the BootOrder.  Default: `[]` |
| **category**  string / required | Category to execute on OOB controller. |
| **command**  list / elements=string / required | List of commands to execute on OOB controller. |
| **hostinterface_config**  dictionary  added in community.general 4.1.0 | Setting dict of HostInterface on OOB controller.  Default: `{}` |
| **hostinterface_id**  string  added in community.general 4.1.0 | Redfish HostInterface instance ID if multiple HostInterfaces are present. |
| **network_protocols**  dictionary  added in community.general 0.2.0 | Setting dict of manager services to update.  Default: `{}` |
| **nic_addr**  string  added in community.general 0.2.0 | EthernetInterface Address string on OOB controller.  Default: `"null"` |
| **nic_config**  dictionary  added in community.general 0.2.0 | Setting dict of EthernetInterface on OOB controller.  Default: `{}` |
| **password**  string | Password for authenticating to OOB controller. |
| **resource_id**  string  added in community.general 0.2.0 | ID of the System, Manager or Chassis to modify. |
| **sessions_config**  dictionary  added in community.general 5.7.0 | Setting dict of Sessions.  Default: `{}` |
| **strip_etag_quotes**  boolean  added in community.general 3.7.0 | Removes surrounding quotes of etag used in `If-Match` header of `PATCH` requests.  Only use this option to resolve bad vendor implementation where `If-Match` only matches the unquoted etag string.  Choices:   - `false` ← (default) - `true` |
| **timeout**  integer | Timeout in seconds for HTTP requests to OOB controller.  Default: `10` |
| **username**  string | Username for authenticating to OOB controller. |

## [Examples](redfish_config_module.md#id3)

```yaml+jinja
- name: Set BootMode to UEFI
  community.general.redfish_config:
    category: Systems
    command: SetBiosAttributes
    resource_id: 437XR1138R2
    bios_attributes:
      BootMode: "Uefi"
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Set multiple BootMode attributes
  community.general.redfish_config:
    category: Systems
    command: SetBiosAttributes
    resource_id: 437XR1138R2
    bios_attributes:
      BootMode: "Bios"
      OneTimeBootMode: "Enabled"
      BootSeqRetry: "Enabled"
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Enable PXE Boot for NIC1
  community.general.redfish_config:
    category: Systems
    command: SetBiosAttributes
    resource_id: 437XR1138R2
    bios_attributes:
      PxeDev1EnDis: Enabled
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Set BIOS default settings with a timeout of 20 seconds
  community.general.redfish_config:
    category: Systems
    command: SetBiosDefaultSettings
    resource_id: 437XR1138R2
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    timeout: 20

- name: Set boot order
  community.general.redfish_config:
    category: Systems
    command: SetBootOrder
    boot_order:
      - Boot0002
      - Boot0001
      - Boot0000
      - Boot0003
      - Boot0004
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Set boot order to the default
  community.general.redfish_config:
    category: Systems
    command: SetDefaultBootOrder
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Set Manager Network Protocols
  community.general.redfish_config:
    category: Manager
    command: SetNetworkProtocols
    network_protocols:
      SNMP:
        ProtocolEnabled: true
        Port: 161
      HTTP:
        ProtocolEnabled: false
        Port: 8080
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Set Manager NIC
  community.general.redfish_config:
    category: Manager
    command: SetManagerNic
    nic_config:
      DHCPv4:
        DHCPEnabled: false
      IPv4StaticAddresses:
        Address: 192.168.1.3
        Gateway: 192.168.1.1
        SubnetMask: 255.255.255.0
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Disable Host Interface
  community.general.redfish_config:
    category: Manager
    command: SetHostInterface
    hostinterface_config:
      InterfaceEnabled: false
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Enable Host Interface for HostInterface resource ID '2'
  community.general.redfish_config:
    category: Manager
    command: SetHostInterface
    hostinterface_config:
      InterfaceEnabled: true
    hostinterface_id: "2"
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Set SessionService Session Timeout to 30 minutes
  community.general.redfish_config:
    category: Sessions
    command: SetSessionService
    sessions_config:
      SessionTimeout: 1800
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
```

## [Return Values](redfish_config_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message with action result or error description  Returned: always  Sample: `"Action was successful"` |

### Authors

- Jose Delarosa (@jose-delarosa)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
