---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.netapp_e_iscsi_target module – NetApp E-Series manage iSCSI target configuration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/netapp_e_iscsi_target_module.html
fetched_at: 2026-07-28T02:44:34+00:00
---
# netapp_eseries.santricity.netapp_e_iscsi_target module – NetApp E-Series manage iSCSI target configuration

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/ui/repo/published/netapp_eseries/santricity/) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_iscsi_target`.

New in netapp_eseries.santricity 2.7

- [Synopsis](netapp_e_iscsi_target_module.md#synopsis)
- [Parameters](netapp_e_iscsi_target_module.md#parameters)
- [Notes](netapp_e_iscsi_target_module.md#notes)
- [Examples](netapp_e_iscsi_target_module.md#examples)
- [Return Values](netapp_e_iscsi_target_module.md#return-values)

## [Synopsis](netapp_e_iscsi_target_module.md#id1)

- Configure the settings of an E-Series iSCSI target

## [Parameters](netapp_e_iscsi_target_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API. Example <https://prod-1.wahoo.acme.com/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **chap_secret**  aliases: chap, password  string | Enable Challenge-Handshake Authentication Protocol (CHAP), utilizing this value as the password.  When this value is specified, we will always trigger an update (changed=True). We have no way of verifying whether or not the password has changed.  The chap secret may only use ascii characters with values between 32 and 126 decimal.  The chap secret must be no less than 12 characters, but no greater than 57 characters in length.  The chap secret is cleared when not specified or an empty string. |
| **log_path**  string | A local path (on the Ansible controller), to a file to be used for debug logging. |
| **name**  aliases: alias  string | The name/alias to assign to the iSCSI target.  This alias is often used by the initiator software in order to make an iSCSI target easier to identify. |
| **ping**  boolean | Enable ICMP ping responses from the configured iSCSI ports.  **Choices:**   - `false` - `true` ← (default) |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  **Default:** `"1"` |
| **unnamed_discovery**  boolean | When an initiator initiates a discovery session to an initiator port, it is considered an unnamed discovery session if the iSCSI target iqn is not specified in the request.  This option may be disabled to increase security if desired.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](netapp_e_iscsi_target_module.md#id3)

> **Note:**
>
> - Check mode is supported.
> - Some of the settings are dependent on the settings applied to the iSCSI interfaces. These can be configured using **ERROR while parsing**: While parsing “M(netapp_e_iscsi_interface)” at index 115: Module name “netapp_e_iscsi_interface” is not a FQCN.
> - This module requires a Web Services API version of >= 1.3.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing “M(netapp_e_storage_system)” at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](netapp_e_iscsi_target_module.md#id4)

```yaml+jinja
- name: Enable ping responses and unnamed discovery sessions for all iSCSI ports
  netapp_e_iscsi_target:
    api_url: "https://localhost:8443/devmgr/v2"
    api_username: admin
    api_password: myPassword
    ssid: "1"
    validate_certs: no
    name: myTarget
    ping: yes
    unnamed_discovery: yes

- name: Set the target alias and the CHAP secret
  netapp_e_iscsi_target:
    ssid: "{{ ssid }}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
    name: myTarget
    chap: password1234
```

## [Return Values](netapp_e_iscsi_target_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **alias**  string | The alias assigned to the iSCSI target.  **Returned:** on success  **Sample:** `"myArray"` |
| **iqn**  string | The iqn (iSCSI Qualified Name), assigned to the iSCSI target.  **Returned:** on success  **Sample:** `"iqn.1992-08.com.netapp:2800.000a132000b006d2000000005a0e8f45"` |
| **msg**  string | Success message  **Returned:** on success  **Sample:** `"The iSCSI target settings have been updated."` |

### Authors

- Michael Price (@lmprice)

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
