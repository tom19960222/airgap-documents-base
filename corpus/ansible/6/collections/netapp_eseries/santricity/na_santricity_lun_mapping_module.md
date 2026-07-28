---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.na_santricity_lun_mapping module – NetApp E-Series manage lun mappings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/na_santricity_lun_mapping_module.html
fetched_at: 2026-07-28T00:14:02+00:00
---
# netapp_eseries.santricity.na_santricity_lun_mapping module – NetApp E-Series manage lun mappings

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/netapp_eseries/santricity) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_lun_mapping`.

- [Synopsis](na_santricity_lun_mapping_module.md#synopsis)
- [Parameters](na_santricity_lun_mapping_module.md#parameters)
- [Notes](na_santricity_lun_mapping_module.md#notes)
- [Examples](na_santricity_lun_mapping_module.md#examples)
- [Return Values](na_santricity_lun_mapping_module.md#return-values)

## [Synopsis](na_santricity_lun_mapping_module.md#id1)

- Create, delete, or modify mappings between a volume and a targeted host/host+ group.

## [Parameters](na_santricity_lun_mapping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **lun**  integer | The LUN value you wish to give the mapping.  If the supplied *volume_name* is associated with a different LUN, it will be updated to what is supplied here.  LUN value will be determine by the storage-system when not specified. |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **state**  string | Present will ensure the mapping exists, absent will remove the mapping.  Choices:   - `"present"` ← (default) - `"absent"` |
| **target**  string | The name of host or hostgroup you wish to assign to the mapping  If omitted, the default hostgroup is used.  If the supplied *volume_name* is associated with a different target, it will be updated to what is supplied here. |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |
| **volume_name**  aliases: volume  string / required | The name of the volume you wish to include in the mapping.  Use ACCESS_VOLUME to reference the in-band access management volume. |

## [Notes](na_santricity_lun_mapping_module.md#id3)

> **Note:**
>
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_lun_mapping_module.md#id4)

```yaml+jinja
---
    - name: Map volume1 to the host target host1
      na_santricity_lun_mapping:
        ssid: "1"
        api_url: "https://192.168.1.100:8443/devmgr/v2"
        api_username: "admin"
        api_password: "adminpass"
        validate_certs: true
        state: present
        target: host1
        volume: volume1
    - name: Delete the lun mapping between volume1 and host1
      na_santricity_lun_mapping:
        ssid: "1"
        api_url: "https://192.168.1.100:8443/devmgr/v2"
        api_username: "admin"
        api_password: "adminpass"
        validate_certs: true
        state: absent
        target: host1
        volume: volume1
```

## [Return Values](na_santricity_lun_mapping_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | success of the module  Returned: always  Sample: `"Lun mapping is complete"` |

### Authors

- Kevin Hulquest (@hulquest)
- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
