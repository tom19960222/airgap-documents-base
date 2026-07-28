---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.na_santricity_global module – NetApp E-Series manage global settings configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/na_santricity_global_module.html
fetched_at: 2026-07-28T00:13:57+00:00
---
# netapp_eseries.santricity.na_santricity_global module – NetApp E-Series manage global settings configuration

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
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_global`.

- [Synopsis](na_santricity_global_module.md#synopsis)
- [Parameters](na_santricity_global_module.md#parameters)
- [Notes](na_santricity_global_module.md#notes)
- [Examples](na_santricity_global_module.md#examples)
- [Return Values](na_santricity_global_module.md#return-values)

## [Synopsis](na_santricity_global_module.md#id1)

- Allow the user to configure several of the global settings associated with an E-Series storage-system

## [Parameters](na_santricity_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **automatic_load_balancing**  string | Enable automatic load balancing to allow incoming traffic from the hosts to be dynamically managed and balanced across both controllers.  Automatic load balancing requires host connectivity reporting to be enabled.  Choices:   - `"enabled"` - `"disabled"` |
| **cache_block_size**  integer | Size of the cache’s block size.  All volumes on the storage system share the same cache space; therefore, the volumes can have only one cache block size.  See **ERROR while parsing**: While parsing M() at index 5: Module name “na_santricity_facts” is not a FQCN for available sizes. |
| **cache_flush_threshold**  integer | This is the percentage threshold of the amount of unwritten data that is allowed to remain on the storage array’s cache before flushing. |
| **controller_shelf_id**  integer | This is the identifier for the drive enclosure containing the controllers.  Default: `0` |
| **default_host_type**  string | Default host type for the storage system.  Either one of the following names can be specified, Linux DM-MP, VMWare, Windows, Windows Clustered, or a host type index which can be found in **ERROR while parsing**: While parsing M() at index 145: Module name “na_santricity_facts” is not a FQCN |
| **host_connectivity_reporting**  string | Enable host connectivity reporting to allow host connections to be monitored for connection and multipath driver problems.  When **ERROR while parsing**: While parsing M() at index 6: Module name “automatic_load_balancing==enabled” is not a FQCN then **ERROR while parsing**: While parsing M() at index 48: Module name “host_connectivity_reporting” is not a FQCN must be enabled  Choices:   - `"enabled"` - `"disabled"` |
| **login_banner_message**  string | Text message that appears prior to the login page.  *login_banner_message==””* will delete any existing banner message. |
| **name**  aliases: label  string | Set the name of the E-Series storage-system  This label/name doesn’t have to be unique.  May be up to 30 characters in length. |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_santricity_global_module.md#id3)

> **Note:**
>
> - Check mode is supported.
> - This module requires Web Services API v1.3 or newer.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_global_module.md#id4)

```yaml+jinja
- name: Set the storage-system name
  na_santricity_global:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    name: myArrayName
    cache_block_size: 32768
    cache_flush_threshold: 80
    automatic_load_balancing: enabled
    default_host_type: Linux DM-MP
- name: Set the storage-system name
  na_santricity_global:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    name: myOtherArrayName
    cache_block_size: 8192
    cache_flush_threshold: 60
    automatic_load_balancing: disabled
    default_host_type: 28
```

## [Return Values](na_santricity_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **array_name**  string | Current storage array’s name  Returned: on success  Sample: `"arrayName"` |
| **automatic_load_balancing**  string | Whether automatic load balancing feature has been enabled  Returned: on success  Sample: `"enabled"` |
| **cache_settings**  dictionary | Current cache block size and flushing threshold values  Returned: on success  Sample: `{"cache_block_size": 32768, "cache_flush_threshold": 80}` |
| **changed**  boolean | Whether global settings were changed  Returned: on success  Sample: `true` |
| **controller_shelf_id**  integer | Identifier for the drive enclosure containing the controllers.  Returned: on success  Sample: `99` |
| **default_host_type_index**  integer | Current default host type index  Returned: on success  Sample: `28` |
| **host_connectivity_reporting**  string | Whether host connectivity reporting feature has been enabled  Returned: on success  Sample: `"enabled"` |
| **login_banner_message**  string | Current banner message  Returned: on success  Sample: `"Banner message here!"` |

### Authors

- Michael Price (@lmprice)
- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
