---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.netapp_e_flashcache module – NetApp E-Series manage SSD caches"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/netapp_e_flashcache_module.html
fetched_at: 2026-07-28T02:44:30+00:00
---
# netapp_eseries.santricity.netapp_e_flashcache module – NetApp E-Series manage SSD caches

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
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_flashcache`.

New in netapp_eseries.santricity 2.2

- [Synopsis](netapp_e_flashcache_module.md#synopsis)
- [Parameters](netapp_e_flashcache_module.md#parameters)
- [Examples](netapp_e_flashcache_module.md#examples)
- [Return Values](netapp_e_flashcache_module.md#return-values)

## [Synopsis](netapp_e_flashcache_module.md#id1)

- Create or remove SSD caches on a NetApp E-Series storage array.

## [Parameters](netapp_e_flashcache_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity WebServices Proxy or embedded REST API. |
| **api_url**  string / required | The url to the SANtricity WebServices Proxy or embedded REST API. |
| **api_username**  string / required | The username to authenticate with the SANtricity WebServices Proxy or embedded REST API. |
| **cache_size_min**  integer | The minimum size (in size_units) of the ssd cache. The cache will be expanded if this exceeds the current size of the cache. |
| **criteria_disk_phy_type**  string | Type of physical disk  **Choices:**   - `"sas"` - `"sas4k"` - `"fibre"` - `"fibre520b"` - `"scsi"` - `"sata"` - `"pata"` |
| **disk_count**  integer | The minimum number of disks to use for building the cache. The cache will be expanded if this number exceeds the number of disks already in place |
| **disk_refs**  list / elements=string | List of disk references |
| **io_type**  string | The type of workload to optimize the cache for.  **Choices:**   - `"filesystem"` ← (default) - `"database"` - `"media"` |
| **log_mode**  string | Log mode |
| **log_path**  string | Log path |
| **name**  string / required | The name of the SSD cache to manage |
| **size_unit**  string | The unit to be applied to size arguments  **Choices:**   - `"bytes"` - `"b"` - `"kb"` - `"mb"` - `"gb"` ← (default) - `"tb"` - `"pb"` - `"eb"` - `"zb"` - `"yb"` |
| **ssid**  string / required | The ID of the array to manage (as configured on the web services proxy). |
| **state**  string / required | Whether the specified SSD cache should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Examples](netapp_e_flashcache_module.md#id3)

```yaml+jinja
- name: Flash Cache
  netapp_e_flashcache:
    ssid: "{{ ssid }}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
    validate_certs: "{{ netapp_api_validate_certs }}"
    name: SSDCacheBuiltByAnsible
```

## [Return Values](netapp_e_flashcache_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  **Returned:** success  **Sample:** `"json for newly created flash cache"` |

### Authors

- Kevin Hulquest (@hulquest)

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
