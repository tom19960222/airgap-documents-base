---
collection: ansible
version: "8"
title: "cisco.intersight.intersight_boot_order_policy module – Boot Order policy configuration for Cisco Intersight"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/intersight/intersight_boot_order_policy_module.html
fetched_at: 2026-07-28T01:25:56+00:00
---
# cisco.intersight.intersight_boot_order_policy module – Boot Order policy configuration for Cisco Intersight

> **Note:**
>
> This module is part of the [cisco.intersight collection](https://galaxy.ansible.com/ui/repo/published/cisco/intersight/) (version 1.0.27).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.intersight`.
>
> To use it in a playbook, specify: `cisco.intersight.intersight_boot_order_policy`.

New in cisco.intersight 2.10

- [Synopsis](intersight_boot_order_policy_module.md#synopsis)
- [Parameters](intersight_boot_order_policy_module.md#parameters)
- [Examples](intersight_boot_order_policy_module.md#examples)
- [Return Values](intersight_boot_order_policy_module.md#return-values)

## [Synopsis](intersight_boot_order_policy_module.md#id1)

- Boot Order policy configuration for Cisco Intersight.
- Used to configure Boot Order servers and timezone settings on Cisco Intersight managed devices.
- For more information see [Cisco Intersight](https://intersight.com/apidocs).

## [Parameters](intersight_boot_order_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key_id**  string / required | Public API Key ID associated with the private key.  If not set, the value of the INTERSIGHT_API_KEY_ID environment variable is used. |
| **api_private_key**  string / required | Filename (absolute path) or string of PEM formatted private key data to be used for Intersight API authentication.  If a string is used, Ansible vault should be used to encrypt string data.  Ex. ansible-vault encrypt_string –vault-id [tme@/Users/dsoper/Documents/vault_password_file](mailto:tme%40/Users/dsoper/Documents/vault_password_file) ‘—–BEGIN EC PRIVATE KEY—–  <your private key data>  —–END EC PRIVATE KEY—–’  If not set, the value of the INTERSIGHT_API_PRIVATE_KEY environment variable is used. |
| **api_uri**  string | URI used to access the Intersight API.  If not set, the value of the INTERSIGHT_API_URI environment variable is used.  **Default:** `"https://intersight.com/api/v1"` |
| **boot_devices**  list / elements=string | List of Boot Devices configured on the endpoint. |
| **bootloader_description**  string | Details of the bootloader to be used during boot from local disk.  Option is used when device_type is local_disk and configured_boot_mode is Uefi. |
| **bootloader_name**  string | Details of the bootloader to be used during boot from local disk.  Option is used when device_type is local_disk and configured_boot_mode is Uefi. |
| **bootloader_path**  string | Details of the bootloader to be used during boot from local disk.  Option is used when device_type is local_disk and configured_boot_mode is Uefi. |
| **controller_slot**  string | The slot id of the controller for the local disk device.  Option is used when device_type is local_disk.  **Choices:**   - `"1-255"` - `"M"` - `"HBA"` - `"SAS"` - `"RAID"` - `"MRAID"` - `"MSTOR-RAID"` |
| **device_name**  string / required | A name that helps identify a boot device.  It can be any string that adheres to the following constraints.  It should start and end with an alphanumeric character.  It can have underscores and hyphens.  It cannot be more than 30 characters. |
| **device_type**  string / required | Device type used with this boot option.  Choices are based on each device title in the API schema.  **Choices:**   - `"iSCSI"` - `"Local CDD"` - `"Local Disk"` - `"NVMe"` - `"PCH Storage"` - `"PXE"` - `"SAN"` - `"SD Card"` - `"UEFI Shell"` - `"USB"` - `"Virtual Media"` |
| **enabled**  boolean | Specifies if the boot device is enabled or disabled.  **Choices:**   - `false` - `true` ← (default) |
| **intefrace_name**  string | The name of the underlying virtual ethernet interface used by the PXE boot device.  Option is used when device_type is pxe and interface_source is name. |
| **interface_source**  string | Lists the supported Interface Source for PXE device.  Option is used when device_type is pxe.  **Choices:**   - `"name"` ← (default) - `"mac"` - `"port"` |
| **ip_type**  string | The IP Address family type to use during the PXE Boot process.  Option is used when device_type is pxe.  **Choices:**   - `"None"` ← (default) - `"IPv4"` - `"IPv6"` |
| **lun**  string | The Logical Unit Number (LUN) of the device.  Option is used when device_type is pch, san and sd_card.  The LUN need to be an integer from 0 to 255. |
| **mac_address**  string | The MAC Address of the underlying virtual ethernet interface used by the PXE boot device.  Option is used when device_type is pxe and interface_source is mac. |
| **network_slot**  string | The slot id of the controller for the iscsi and pxe device.  Option is used when device_type is iscsi and pxe.  **Choices:**   - `"1 - 255"` - `"MLOM"` - `"L"` - `"L1"` - `"L2"` - `"OCP"` |
| **port**  string | The port id of the controller for the iscsi and pxe device.  Option is used when device_type is iscsi and pxe.  The port id need to be an integer from 0 to 255. |
| **sd_card_subtype**  string | The subtype for the selected device type.  Option is used when device_type is sd_card.  **Choices:**   - `"None"` ← (default) - `"flex-util"` - `"flex-flash"` - `"SDCARD"` |
| **usb_subtype**  string | The subtype for the selected device type.  Option is used when device_type is usb.  **Choices:**   - `"None"` ← (default) - `"usb-cd"` - `"usb-fdd"` - `"usb-hdd"` |
| **virtual_media_subtype**  string | The subtype for the selected device type.  Option is used when device_type is virtual_media.  **Choices:**   - `"None"` ← (default) - `"cimc-mapped-dvd"` - `"cimc-mapped-hdd"` - `"kvm-mapped-dvd"` - `"kvm-mapped-hdd"` - `"kvm-mapped-fdd"` |
| **configured_boot_mode**  string | Sets the BIOS boot mode.  UEFI uses the GUID Partition Table (GPT) whereas Legacy mode uses the Master Boot Record (MBR) partitioning scheme.  **Choices:**   - `"Legacy"` ← (default) - `"Uefi"` |
| **description**  aliases: descr  string | The user-defined description of the Boot Order policy.  Description can contain letters(a-z, A-Z), numbers(0-9), hyphen(-), period(.), colon(:), or an underscore(_). |
| **name**  string / required | The name assigned to the Boot Order policy.  The name must be between 1 and 62 alphanumeric characters, allowing special characters :-_. |
| **organization**  string | The name of the Organization this resource is assigned to.  Profiles and Policies that are created within a Custom Organization are applicable only to devices in the same Organization.  **Default:** `"default"` |
| **state**  string | If `present`, will verify the resource is present and will create if needed.  If `absent`, will verify the resource is absent and will delete if needed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | List of tags in Key:<user-defined key> Value:<user-defined value> format. |
| **uefi_enable_secure_boot**  boolean | Secure boot enforces that device boots using only software that is trusted by the Original Equipment Manufacturer (OEM).  Option is only used if configured_boot_mode is set to Uefi.  **Choices:**   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Boolean control for verifying the api_uri TLS certificate  **Choices:**   - `false` - `true` ← (default) |

## [Examples](intersight_boot_order_policy_module.md#id3)

```yaml+jinja
- name: Configure Boot Order Policy
  cisco.intersight.intersight_boot_order_policy:
    api_private_key: "{{ api_private_key }}"
    api_key_id: "{{ api_key_id }}"
    organization: DevNet
    name: COS-Boot
    description: Boot Order policy for COS
    tags:
      - Key: Site
        Value: RCDN
    configured_boot_mode: legacy
    boot_devices:
      - device_type: Local Disk
        device_name: Boot-Lun
        controller_slot: MRAID

- name: Delete Boot Order Policy
  cisco.intersight.intersight_boot_policy:
    api_private_key: "{{ api_private_key }}"
    api_key_id: "{{ api_key_id }}"
    organization: DevNet
    name: COS-Boot
    state: absent
```

## [Return Values](intersight_boot_order_policy_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_repsonse**  dictionary | The API response output returned by the specified resource.  **Returned:** always  **Sample:** `{"api_response": {"Name": "COS-Boot", "ObjectType": "boot.Policy", "Tags": [{"Key": "Site", "Value": "RCDN"}]}}` |

### Authors

- Tse Kai “Kevin” Chan (@BrightScale)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/intersight-ansible)
- [Repository (Sources)](https://github.com/CiscoDevNet/intersight-ansible)
