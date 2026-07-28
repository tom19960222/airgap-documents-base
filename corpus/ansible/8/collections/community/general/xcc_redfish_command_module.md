---
collection: ansible
version: "8"
title: "community.general.xcc_redfish_command module – Manages Lenovo Out-Of-Band controllers using Redfish APIs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/xcc_redfish_command_module.html
fetched_at: 2026-07-28T01:51:29+00:00
---
# community.general.xcc_redfish_command module – Manages Lenovo Out-Of-Band controllers using Redfish APIs

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
> To use it in a playbook, specify: `community.general.xcc_redfish_command`.

New in community.general 2.4.0

- [Synopsis](xcc_redfish_command_module.md#synopsis)
- [Parameters](xcc_redfish_command_module.md#parameters)
- [Attributes](xcc_redfish_command_module.md#attributes)
- [Examples](xcc_redfish_command_module.md#examples)
- [Return Values](xcc_redfish_command_module.md#return-values)

## [Synopsis](xcc_redfish_command_module.md#id1)

- Builds Redfish URIs locally and sends them to remote OOB controllers to perform an action or get information back or update a configuration attribute.
- Manages virtual media.
- Supports getting information back via GET method.
- Supports updating a configuration attribute via PATCH method.
- Supports performing an action via POST method.

Aliases: remote_management.lenovoxcc.xcc_redfish_command

## [Parameters](xcc_redfish_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_token**  string | Security token for authentication with OOB controller |
| **baseuri**  string / required | Base URI of OOB controller. |
| **category**  string / required | Category to execute on OOB controller. |
| **command**  list / elements=string / required | List of commands to execute on OOB controller. |
| **password**  string | Password for authentication with OOB controller. |
| **request_body**  dictionary | The request body to patch or post. |
| **resource_id**  string | The ID of the System, Manager or Chassis to modify. |
| **resource_uri**  string | The resource uri to get or patch or post. |
| **timeout**  integer | Timeout in seconds for URL requests to OOB controller.  **Default:** `10` |
| **username**  string | Username for authentication with OOB controller. |
| **virtual_media**  dictionary | The options for VirtualMedia commands. |
| **image_url**  string | The URL of the image to insert or eject. |
| **inserted**  boolean | Indicates if the image is treated as inserted on command completion.  **Choices:**   - `false` - `true` ← (default) |
| **media_types**  list / elements=string | The list of media types appropriate for the image.  **Default:** `[]` |
| **password**  string | The password for accessing the image URL. |
| **transfer_method**  string | The transfer method to use with the image. |
| **transfer_protocol_type**  string | The network protocol to use with the image. |
| **username**  string | The username for accessing the image URL. |
| **write_protected**  boolean | Indicates if the media is treated as write-protected.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](xcc_redfish_command_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](xcc_redfish_command_module.md#id4)

```yaml+jinja
- name: Insert Virtual Media
  community.general.xcc_redfish_command:
    category: Manager
    command: VirtualMediaInsert
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    virtual_media:
      image_url: "http://example.com/images/SomeLinux-current.iso"
      media_types:
        - CD
        - DVD
    resource_id: "1"

- name: Eject Virtual Media
  community.general.xcc_redfish_command:
    category: Manager
    command: VirtualMediaEject
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    virtual_media:
      image_url: "http://example.com/images/SomeLinux-current.iso"
    resource_id: "1"

- name: Eject all Virtual Media
  community.general.xcc_redfish_command:
    category: Manager
    command: VirtualMediaEject
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    resource_id: "1"

- name: Get ComputeSystem Oem property SystemStatus via GetResource command
  community.general.xcc_redfish_command:
    category: Raw
    command: GetResource
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    resource_uri: "/redfish/v1/Systems/1"
  register: result
- ansible.builtin.debug:
    msg: "{{ result.redfish_facts.data.Oem.Lenovo.SystemStatus }}"

- name: Get Oem DNS setting via GetResource command
  community.general.xcc_redfish_command:
    category: Raw
    command: GetResource
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    resource_uri: "/redfish/v1/Managers/1/NetworkProtocol/Oem/Lenovo/DNS"
  register: result

- name: Print fetched information
  ansible.builtin.debug:
    msg: "{{ result.redfish_facts.data }}"

- name: Get Lenovo FoD key collection resource via GetCollectionResource command
  community.general.xcc_redfish_command:
    category: Raw
    command: GetCollectionResource
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    resource_uri: "/redfish/v1/Managers/1/Oem/Lenovo/FoD/Keys"
  register: result

- name: Print fetched information
  ansible.builtin.debug:
    msg: "{{ result.redfish_facts.data_list }}"

- name: Update ComputeSystem property AssetTag via PatchResource command
  community.general.xcc_redfish_command:
    category: Raw
    command: PatchResource
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    resource_uri: "/redfish/v1/Systems/1"
    request_body:
      AssetTag: "new_asset_tag"

- name: Perform BootToBIOSSetup action via PostResource command
  community.general.xcc_redfish_command:
    category: Raw
    command: PostResource
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    resource_uri: "/redfish/v1/Systems/1/Actions/Oem/LenovoComputerSystem.BootToBIOSSetup"
    request_body: {}

- name: Perform SecureBoot.ResetKeys action via PostResource command
  community.general.xcc_redfish_command:
    category: Raw
    command: PostResource
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    resource_uri: "/redfish/v1/Systems/1/SecureBoot/Actions/SecureBoot.ResetKeys"
    request_body:
      ResetKeysType: DeleteAllKeys

- name: Create session
  community.general.redfish_command:
    category: Sessions
    command: CreateSession
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
  register: result

- name: Update Manager DateTimeLocalOffset property using security token for auth
  community.general.xcc_redfish_command:
    category: Raw
    command: PatchResource
    baseuri: "{{ baseuri }}"
    auth_token: "{{ result.session.token }}"
    resource_uri: "/redfish/v1/Managers/1"
    request_body:
      DateTimeLocalOffset: "+08:00"

- name: Delete session using security token created by CreateSesssion above
  community.general.redfish_command:
    category: Sessions
    command: DeleteSession
    baseuri: "{{ baseuri }}"
    auth_token: "{{ result.session.token }}"
    session_uri: "{{ result.session.uri }}"
```

## [Return Values](xcc_redfish_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | A message related to the performed action(s).  **Returned:** when failure or action/update success  **Sample:** `"Action was successful"` |
| **redfish_facts**  dictionary | Resource content.  **Returned:** when command == GetResource or command == GetCollectionResource  **Sample:** `"{ \"redfish_facts\": { \"data\": { \"@odata.etag\": \"\"3179bf00d69f25a8b3c\"\", \"@odata.id\": \"/redfish/v1/Managers/1/NetworkProtocol/Oem/Lenovo/DNS\", \"@odata.type\": \"#LenovoDNS.v1_0_0.LenovoDNS\", \"DDNS\": [ { \"DDNSEnable\": true, \"DomainName\": \"\", \"DomainNameSource\": \"DHCP\" } ], \"DNSEnable\": true, \"Description\": \"This resource is used to represent a DNS resource for a Redfish implementation.\", \"IPv4Address1\": \"10.103.62.178\", \"IPv4Address2\": \"0.0.0.0\", \"IPv4Address3\": \"0.0.0.0\", \"IPv6Address1\": \"::\", \"IPv6Address2\": \"::\", \"IPv6Address3\": \"::\", \"Id\": \"LenovoDNS\", \"PreferredAddresstype\": \"IPv4\" }, \"ret\": true } }"` |

### Authors

- Yuyan Pan (@panyy3)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
