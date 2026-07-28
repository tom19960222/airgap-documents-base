---
collection: ansible
version: "8"
title: "community.general.redfish_config module – Manages Out-Of-Band controllers using Redfish APIs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/redfish_config_module.html
fetched_at: 2026-07-28T01:49:51+00:00
---
# community.general.redfish_config module – Manages Out-Of-Band controllers using Redfish APIs

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
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
- [Attributes](redfish_config_module.md#attributes)
- [Examples](redfish_config_module.md#examples)
- [Return Values](redfish_config_module.md#return-values)

## [Synopsis](redfish_config_module.md#id1)

- Builds Redfish URIs locally and sends them to remote OOB controllers to set or update a configuration attribute.
- Manages BIOS configuration settings.
- Manages OOB controller configuration settings.

Aliases: remote_management.redfish.redfish_config

## [Parameters](redfish_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_token**  string  *added in community.general 2.3.0* | Security token for authenticating to OOB controller. |
| **baseuri**  string / required | Base URI of OOB controller. |
| **bios_attributes**  dictionary  *added in community.general 0.2.0* | Dictionary of BIOS attributes to update.  **Default:** `{}` |
| **boot_order**  list / elements=string  *added in community.general 0.2.0* | List of BootOptionReference strings specifying the BootOrder.  **Default:** `[]` |
| **category**  string / required | Category to execute on OOB controller. |
| **command**  list / elements=string / required | List of commands to execute on OOB controller. |
| **hostinterface_config**  dictionary  *added in community.general 4.1.0* | Setting dict of HostInterface on OOB controller.  **Default:** `{}` |
| **hostinterface_id**  string  *added in community.general 4.1.0* | Redfish HostInterface instance ID if multiple HostInterfaces are present. |
| **network_protocols**  dictionary  *added in community.general 0.2.0* | Setting dict of manager services to update.  **Default:** `{}` |
| **nic_addr**  string  *added in community.general 0.2.0* | EthernetInterface Address string on OOB controller.  **Default:** `"null"` |
| **nic_config**  dictionary  *added in community.general 0.2.0* | Setting dict of EthernetInterface on OOB controller.  **Default:** `{}` |
| **password**  string | Password for authenticating to OOB controller. |
| **resource_id**  string  *added in community.general 0.2.0* | ID of the System, Manager or Chassis to modify. |
| **secure_boot_enable**  boolean  *added in community.general 7.5.0* | Setting parameter to enable or disable SecureBoot.  **Choices:**   - `false` - `true` ← (default) |
| **sessions_config**  dictionary  *added in community.general 5.7.0* | Setting dict of Sessions.  **Default:** `{}` |
| **storage_subsystem_id**  string  *added in community.general 7.3.0* | Id of the Storage Subsystem on which the volume is to be created.  **Default:** `""` |
| **strip_etag_quotes**  boolean  *added in community.general 3.7.0* | Removes surrounding quotes of etag used in `If-Match` header of `PATCH` requests.  Only use this option to resolve bad vendor implementation where `If-Match` only matches the unquoted etag string.  **Choices:**   - `false` ← (default) - `true` |
| **timeout**  integer | Timeout in seconds for HTTP requests to OOB controller.  The default value for this param is `10` but that is being deprecated and it will be replaced with `60` in community.general 9.0.0. |
| **username**  string | Username for authenticating to OOB controller. |
| **volume_details**  dictionary  *added in community.general 7.5.0* | Setting dict of volume to be created.  **Default:** `{}` |
| **volume_ids**  list / elements=string  *added in community.general 7.3.0* | List of IDs of volumes to be deleted.  **Default:** `[]` |

## [Attributes](redfish_config_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](redfish_config_module.md#id4)

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

- name: Enable SecureBoot
  community.general.redfish_config:
    category: Systems
    command: EnableSecureBoot
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Set SecureBoot
  community.general.redfish_config:
    category: Systems
    command: SetSecureBoot
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    secure_boot_enable: True

- name: Delete All Volumes
  community.general.redfish_config:
    category: Systems
    command: DeleteVolumes
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    storage_subsystem_id: "DExxxxxx"
    volume_ids: ["volume1", "volume2"]

- name: Create Volume
  community.general.redfish_config:
    category: Systems
    command: CreateVolume
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    storage_subsystem_id: "DExxxxxx"
    volume_details:
      Name: "MR Volume"
      RAIDType: "RAID0"
      Drives:
        - "/redfish/v1/Systems/1/Storage/DE00B000/Drives/1"
```

## [Return Values](redfish_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message with action result or error description  **Returned:** always  **Sample:** `"Action was successful"` |

### Authors

- Jose Delarosa (@jose-delarosa)
- T S Kushal (@TSKushal)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
