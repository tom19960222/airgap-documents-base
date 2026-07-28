---
collection: ansible
version: "8"
title: "community.general.redfish_command module – Manages Out-Of-Band controllers using Redfish APIs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/redfish_command_module.html
fetched_at: 2026-07-28T01:49:50+00:00
---
# community.general.redfish_command module – Manages Out-Of-Band controllers using Redfish APIs

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
> To use it in a playbook, specify: `community.general.redfish_command`.

- [Synopsis](redfish_command_module.md#synopsis)
- [Parameters](redfish_command_module.md#parameters)
- [Attributes](redfish_command_module.md#attributes)
- [Examples](redfish_command_module.md#examples)
- [Return Values](redfish_command_module.md#return-values)

## [Synopsis](redfish_command_module.md#id1)

- Builds Redfish URIs locally and sends them to remote OOB controllers to perform an action.
- Manages OOB controller ex. reboot, log management.
- Manages OOB controller users ex. add, remove, update.
- Manages system power ex. on, off, graceful and forced reboot.

Aliases: remote_management.redfish.redfish_command

## [Parameters](redfish_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **account_properties**  dictionary  *added in community.general 0.2.0* | Properties of account service to update.  **Default:** `{}` |
| **account_types**  aliases: account_accounttypes  list / elements=string  *added in community.general 7.2.0* | Array of account types to apply to a user account. |
| **auth_token**  string  *added in community.general 2.3.0* | Security token for authenticating to OOB controller. |
| **baseuri**  string / required | Base URI of OOB controller. |
| **bios_attributes**  dictionary  *added in community.general 6.4.0* | BIOS attributes that needs to be verified in the given server. |
| **boot_next**  string | BootNext target when bootdevice is “UefiBootNext”. |
| **boot_override_mode**  string  *added in community.general 3.5.0* | Boot mode when using an override.  **Choices:**   - `"Legacy"` - `"UEFI"` |
| **bootdevice**  string | Boot device when setting boot configuration. |
| **category**  string / required | Category to execute on OOB controller. |
| **command**  list / elements=string / required | List of commands to execute on OOB controller. |
| **id**  aliases: account_id  string | ID of account to delete/modify.  Can also be used in account creation to work around vendor issues where the ID of the new user is required in the POST request. |
| **new_password**  aliases: account_password  string | New password of account to add/modify. |
| **new_username**  aliases: account_username  string | Username of account to add/delete/modify. |
| **oem_account_types**  aliases: account_oemaccounttypes  list / elements=string  *added in community.general 7.2.0* | Array of OEM account types to apply to a user account. |
| **password**  string | Password for authenticating to OOB controller. |
| **resource_id**  string  *added in community.general 0.2.0* | ID of the System, Manager or Chassis to modify. |
| **roleid**  aliases: account_roleid  string | Role of account to add/modify. |
| **session_uri**  string  *added in community.general 2.3.0* | URI of the session resource. |
| **strip_etag_quotes**  boolean  *added in community.general 3.7.0* | Removes surrounding quotes of etag used in `If-Match` header of `PATCH` requests.  Only use this option to resolve bad vendor implementation where `If-Match` only matches the unquoted etag string.  **Choices:**   - `false` ← (default) - `true` |
| **timeout**  integer | Timeout in seconds for HTTP requests to OOB controller.  The default value for this param is `10` but that is being deprecated and it will be replaced with `60` in community.general 9.0.0. |
| **uefi_target**  string | UEFI boot target when bootdevice is “UefiTarget”. |
| **update_apply_time**  string  *added in community.general 6.1.0* | Time when to apply the update.  **Choices:**   - `"Immediate"` - `"OnReset"` - `"AtMaintenanceWindowStart"` - `"InMaintenanceWindowOnReset"` - `"OnStartUpdateRequest"` |
| **update_creds**  dictionary  *added in community.general 0.2.0* | Credentials for retrieving the update image. |
| **password**  string | Password for retrieving the update image. |
| **username**  string | Username for retrieving the update image. |
| **update_handle**  string  *added in community.general 6.1.0* | Handle to check the status of an update in progress. |
| **update_image_file**  path  *added in community.general 7.1.0* | Filename, with optional path, of the image for the update. |
| **update_image_uri**  string  *added in community.general 0.2.0* | URI of the image for the update. |
| **update_oem_params**  dictionary  *added in community.general 7.5.0* | Properties for HTTP Multipart Push Updates. |
| **update_protocol**  string  *added in community.general 0.2.0* | Protocol for the update. |
| **update_targets**  list / elements=string  *added in community.general 0.2.0* | List of target resource URIs to apply the update to.  **Default:** `[]` |
| **update_username**  aliases: account_updatename  string  *added in community.general 0.2.0* | New user name for updating account_username. |
| **username**  string | Username for authenticating to OOB controller. |
| **virtual_media**  dictionary  *added in community.general 0.2.0* | Options for VirtualMedia commands. |
| **image_url**  string | URL of the image to insert or eject. |
| **inserted**  boolean | Indicates that the image is treated as inserted on command completion.  **Choices:**   - `false` - `true` ← (default) |
| **media_types**  list / elements=string | List of media types appropriate for the image.  **Default:** `[]` |
| **password**  string | Password for accessing the image URL. |
| **transfer_method**  string | Transfer method to use with the image. |
| **transfer_protocol_type**  string | Network protocol to use with the image. |
| **username**  string | Username for accessing the image URL. |
| **write_protected**  boolean | Indicates that the media is treated as write-protected.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](redfish_command_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](redfish_command_module.md#id4)

```yaml+jinja
- name: Restart system power gracefully
  community.general.redfish_command:
    category: Systems
    command: PowerGracefulRestart
    resource_id: 437XR1138R2
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Turn system power off
  community.general.redfish_command:
    category: Systems
    command: PowerForceOff
    resource_id: 437XR1138R2

- name: Restart system power forcefully
  community.general.redfish_command:
    category: Systems
    command: PowerForceRestart
    resource_id: 437XR1138R2

- name: Shutdown system power gracefully
  community.general.redfish_command:
    category: Systems
    command: PowerGracefulShutdown
    resource_id: 437XR1138R2

- name: Turn system power on
  community.general.redfish_command:
    category: Systems
    command: PowerOn
    resource_id: 437XR1138R2

- name: Reboot system power
  community.general.redfish_command:
    category: Systems
    command: PowerReboot
    resource_id: 437XR1138R2

- name: Set one-time boot device to {{ bootdevice }}
  community.general.redfish_command:
    category: Systems
    command: SetOneTimeBoot
    resource_id: 437XR1138R2
    bootdevice: "{{ bootdevice }}"
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Set one-time boot device to UefiTarget of "/0x31/0x33/0x01/0x01"
  community.general.redfish_command:
    category: Systems
    command: SetOneTimeBoot
    resource_id: 437XR1138R2
    bootdevice: "UefiTarget"
    uefi_target: "/0x31/0x33/0x01/0x01"
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Set one-time boot device to BootNext target of "Boot0001"
  community.general.redfish_command:
    category: Systems
    command: SetOneTimeBoot
    resource_id: 437XR1138R2
    bootdevice: "UefiBootNext"
    boot_next: "Boot0001"
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Set persistent boot device override
  community.general.redfish_command:
    category: Systems
    command: EnableContinuousBootOverride
    resource_id: 437XR1138R2
    bootdevice: "{{ bootdevice }}"
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Set one-time boot to BiosSetup
  community.general.redfish_command:
    category: Systems
    command: SetOneTimeBoot
    boot_next: BiosSetup
    boot_override_mode: Legacy
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Disable persistent boot device override
  community.general.redfish_command:
    category: Systems
    command: DisableBootOverride

- name: Set system indicator LED to blink using security token for auth
  community.general.redfish_command:
    category: Systems
    command: IndicatorLedBlink
    resource_id: 437XR1138R2
    baseuri: "{{ baseuri }}"
    auth_token: "{{ result.session.token }}"

- name: Add user
  community.general.redfish_command:
    category: Accounts
    command: AddUser
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    new_username: "{{ new_username }}"
    new_password: "{{ new_password }}"
    roleid: "{{ roleid }}"

- name: Add user with specified account types
  community.general.redfish_command:
    category: Accounts
    command: AddUser
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    new_username: "{{ new_username }}"
    new_password: "{{ new_password }}"
    roleid: "{{ roleid }}"
    account_types:
    - Redfish
    - WebUI

- name: Add user using new option aliases
  community.general.redfish_command:
    category: Accounts
    command: AddUser
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    account_username: "{{ account_username }}"
    account_password: "{{ account_password }}"
    account_roleid: "{{ account_roleid }}"

- name: Delete user
  community.general.redfish_command:
    category: Accounts
    command: DeleteUser
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    account_username: "{{ account_username }}"

- name: Disable user
  community.general.redfish_command:
    category: Accounts
    command: DisableUser
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    account_username: "{{ account_username }}"

- name: Enable user
  community.general.redfish_command:
    category: Accounts
    command: EnableUser
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    account_username: "{{ account_username }}"

- name: Add and enable user
  community.general.redfish_command:
    category: Accounts
    command: AddUser,EnableUser
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    new_username: "{{ new_username }}"
    new_password: "{{ new_password }}"
    roleid: "{{ roleid }}"

- name: Update user password
  community.general.redfish_command:
    category: Accounts
    command: UpdateUserPassword
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    account_username: "{{ account_username }}"
    account_password: "{{ account_password }}"

- name: Update user role
  community.general.redfish_command:
    category: Accounts
    command: UpdateUserRole
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    account_username: "{{ account_username }}"
    roleid: "{{ roleid }}"

- name: Update user name
  community.general.redfish_command:
    category: Accounts
    command: UpdateUserName
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    account_username: "{{ account_username }}"
    account_updatename: "{{ account_updatename }}"

- name: Update user name
  community.general.redfish_command:
    category: Accounts
    command: UpdateUserName
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    account_username: "{{ account_username }}"
    update_username: "{{ update_username }}"

- name: Update AccountService properties
  community.general.redfish_command:
    category: Accounts
    command: UpdateAccountServiceProperties
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    account_properties:
      AccountLockoutThreshold: 5
      AccountLockoutDuration: 600

- name: Clear Manager Logs with a timeout of 20 seconds
  community.general.redfish_command:
    category: Manager
    command: ClearLogs
    resource_id: BMC
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    timeout: 20

- name: Create session
  community.general.redfish_command:
    category: Sessions
    command: CreateSession
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
  register: result

- name: Set chassis indicator LED to blink using security token for auth
  community.general.redfish_command:
    category: Chassis
    command: IndicatorLedBlink
    resource_id: 1U
    baseuri: "{{ baseuri }}"
    auth_token: "{{ result.session.token }}"

- name: Delete session using security token created by CreateSesssion above
  community.general.redfish_command:
    category: Sessions
    command: DeleteSession
    baseuri: "{{ baseuri }}"
    auth_token: "{{ result.session.token }}"
    session_uri: "{{ result.session.uri }}"

- name: Clear Sessions
  community.general.redfish_command:
    category: Sessions
    command: ClearSessions
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Simple update
  community.general.redfish_command:
    category: Update
    command: SimpleUpdate
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    update_image_uri: https://example.com/myupdate.img

- name: Simple update with additional options
  community.general.redfish_command:
    category: Update
    command: SimpleUpdate
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    update_image_uri: //example.com/myupdate.img
    update_protocol: FTP
    update_targets:
      - /redfish/v1/UpdateService/FirmwareInventory/BMC
    update_creds:
      username: operator
      password: supersecretpwd

- name: Multipart HTTP push update; timeout is 600 seconds to allow for a
    large image transfer
  community.general.redfish_command:
    category: Update
    command: MultipartHTTPPushUpdate
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    timeout: 600
    update_image_file: ~/images/myupdate.img

- name: Multipart HTTP push with additional options; timeout is 600 seconds
    to allow for a large image transfer
  community.general.redfish_command:
    category: Update
    command: MultipartHTTPPushUpdate
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    timeout: 600
    update_image_file: ~/images/myupdate.img
    update_targets:
      - /redfish/v1/UpdateService/FirmwareInventory/BMC
    update_oem_params:
      PreserveConfiguration: false

- name: Perform requested operations to continue the update
  community.general.redfish_command:
    category: Update
    command: PerformRequestedOperations
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    update_handle: /redfish/v1/TaskService/TaskMonitors/735

- name: Insert Virtual Media
  community.general.redfish_command:
    category: Systems
    command: VirtualMediaInsert
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    virtual_media:
      image_url: 'http://example.com/images/SomeLinux-current.iso'
      media_types:
        - CD
        - DVD
    resource_id: 1

- name: Insert Virtual Media
  community.general.redfish_command:
    category: Manager
    command: VirtualMediaInsert
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    virtual_media:
      image_url: 'http://example.com/images/SomeLinux-current.iso'
      media_types:
        - CD
        - DVD
    resource_id: BMC

- name: Eject Virtual Media
  community.general.redfish_command:
    category: Systems
    command: VirtualMediaEject
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    virtual_media:
      image_url: 'http://example.com/images/SomeLinux-current.iso'
    resource_id: 1

- name: Eject Virtual Media
  community.general.redfish_command:
    category: Manager
    command: VirtualMediaEject
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    virtual_media:
      image_url: 'http://example.com/images/SomeLinux-current.iso'
    resource_id: BMC

- name: Restart manager power gracefully
  community.general.redfish_command:
    category: Manager
    command: GracefulRestart
    resource_id: BMC
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Restart manager power gracefully
  community.general.redfish_command:
    category: Manager
    command: PowerGracefulRestart
    resource_id: BMC

- name: Turn manager power off
  community.general.redfish_command:
    category: Manager
    command: PowerForceOff
    resource_id: BMC

- name: Restart manager power forcefully
  community.general.redfish_command:
    category: Manager
    command: PowerForceRestart
    resource_id: BMC

- name: Shutdown manager power gracefully
  community.general.redfish_command:
    category: Manager
    command: PowerGracefulShutdown
    resource_id: BMC

- name: Turn manager power on
  community.general.redfish_command:
    category: Manager
    command: PowerOn
    resource_id: BMC

- name: Reboot manager power
  community.general.redfish_command:
    category: Manager
    command: PowerReboot
    resource_id: BMC

- name: Verify BIOS attributes
  community.general.redfish_command:
    category: Systems
    command: VerifyBiosAttributes
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    bios_attributes:
      SubNumaClustering: "Disabled"
      WorkloadProfile: "Virtualization-MaxPerformance"
```

## [Return Values](redfish_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message with action result or error description  **Returned:** always  **Sample:** `"Action was successful"` |
| **return_values**  dictionary  *added in community.general 6.1.0* | Dictionary containing command-specific response data from the action.  **Returned:** on success  **Sample:** `{"update_status": {"handle": "/redfish/v1/TaskService/TaskMonitors/735", "messages": [], "resets_requested": [], "ret": true, "status": "New"}}` |

### Authors

- Jose Delarosa (@jose-delarosa)
- T S Kushal (@TSKushal)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
