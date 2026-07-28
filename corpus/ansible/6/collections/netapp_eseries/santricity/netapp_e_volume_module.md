---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.netapp_e_volume module – NetApp E-Series manage storage volumes (standard and thin)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/netapp_e_volume_module.html
fetched_at: 2026-07-28T00:14:27+00:00
---
# netapp_eseries.santricity.netapp_e_volume module – NetApp E-Series manage storage volumes (standard and thin)

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
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_volume`.

New in netapp_eseries.santricity 2.2

- [Synopsis](netapp_e_volume_module.md#synopsis)
- [Parameters](netapp_e_volume_module.md#parameters)
- [Notes](netapp_e_volume_module.md#notes)
- [Examples](netapp_e_volume_module.md#examples)
- [Return Values](netapp_e_volume_module.md#return-values)

## [Synopsis](netapp_e_volume_module.md#id1)

- Create or remove volumes (standard and thin) for NetApp E/EF-series storage arrays.

## [Parameters](netapp_e_volume_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API. Example <https://prod-1.wahoo.acme.com/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **cache_without_batteries**  boolean  added in netapp_eseries.santricity 2.9 | Indicates whether caching should be used without battery backup.  Warning, **ERROR while parsing**: While parsing M() at index 10: Module name “cache_without_batteries==true” is not a FQCN and the storage system looses power and there is no battery backup, data will be lost!  Choices:   - `false` ← (default) - `true` |
| **data_assurance_enabled**  boolean | Determines whether data assurance (DA) should be enabled for the volume  Only available when creating a new volume and on a storage pool with drives supporting the DA capability.  Choices:   - `false` ← (default) - `true` |
| **initialization_timeout**  integer  added in netapp_eseries.santricity 2.9 | Duration in seconds before the wait_for_initialization operation will terminate.  **ERROR while parsing**: While parsing M() at index 1: Module name “wait_for_initialization==True” is not a FQCN to have any effect on module’s operations. |
| **metadata**  dictionary  added in netapp_eseries.santricity 2.8 | Dictionary containing meta data for the use, user, location, etc of the volume (dictionary is arbitrarily defined for whatever the user deems useful)  When *workload_name* exists on the storage array but the metadata is different then the workload definition will be updated. (Changes will update all associated volumes!)  *workload_name* must be specified when *metadata* are defined. |
| **name**  string / required | The name of the volume to manage. |
| **owning_controller**  string  added in netapp_eseries.santricity 2.9 | Specifies which controller will be the primary owner of the volume  Not specifying will allow the controller to choose ownership.  Choices:   - `"A"` - `"B"` |
| **read_ahead_enable**  boolean  added in netapp_eseries.santricity 2.8 | Indicates whether or not automatic cache read-ahead is enabled.  This option has no effect on thinly provisioned volumes since the architecture for thin volumes cannot benefit from read ahead caching.  Choices:   - `false` - `true` ← (default) |
| **read_cache_enable**  boolean  added in netapp_eseries.santricity 2.8 | Indicates whether read caching should be enabled for the volume.  Choices:   - `false` - `true` ← (default) |
| **segment_size_kb**  integer | Segment size of the volume  All values are in kibibytes.  Some common choices include ‘8’, ‘16’, ‘32’, ‘64’, ‘128’, ‘256’, and ‘512’ but options are system dependent.  Retrieve the definitive system list from **ERROR while parsing**: While parsing M() at index 42: Module name “netapp_e_facts” is not a FQCN under segment_sizes.  When the storage pool is a raidDiskPool then the segment size must be 128kb.  Segment size migrations are not allowed in this module  Default: `128` |
| **size**  float / required | Required only when *state==’present’*.  Size of the volume in *size_unit*.  Size of the virtual volume in the case of a thin volume in *size_unit*.  Maximum virtual volume size of a thin provisioned volume is 256tb; however other OS-level restrictions may exist. |
| **size_unit**  string | The unit used to interpret the size parameter  Choices:   - `"bytes"` - `"b"` - `"kb"` - `"mb"` - `"gb"` ← (default) - `"tb"` - `"pb"` - `"eb"` - `"zb"` - `"yb"` |
| **ssd_cache_enabled**  boolean | Whether an existing SSD cache should be enabled on the volume (fails if no SSD cache defined)  The default value is to ignore existing SSD cache setting.  Choices:   - `false` ← (default) - `true` |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **state**  string / required | Whether the specified volume should exist  Choices:   - `"present"` - `"absent"` |
| **storage_pool_name**  string | Required only when requested *state==’present’*.  Name of the storage pool wherein the volume should reside. |
| **thin_provision**  boolean | Whether the volume should be thin provisioned.  Thin volumes can only be created when *raid_level==”raidDiskPool”*.  Generally, use of thin-provisioning is not recommended due to performance impacts.  Choices:   - `false` ← (default) - `true` |
| **thin_volume_expansion_policy**  string  added in netapp_eseries.santricity 2.8 | This is the thin volume expansion policy.  When *thin_volume_expansion_policy==”automatic”* and *thin_volume_growth_alert_threshold* is exceed the *thin_volume_max_repo_size* will be automatically expanded.  When *thin_volume_expansion_policy==”manual”* and *thin_volume_growth_alert_threshold* is exceeded the storage system will wait for manual intervention.  The thin volume_expansion policy can not be modified on existing thin volumes in this module.  Generally speaking you should almost always use *thin_volume_expansion_policy==”automatic*.  Choices:   - `"automatic"` ← (default) - `"manual"` |
| **thin_volume_growth_alert_threshold**  integer  added in netapp_eseries.santricity 2.8 | This is the thin provision repository utilization threshold (in percent).  When the percentage of used storage of the maximum repository size exceeds this value then a alert will be issued and the *thin_volume_expansion_policy* will be executed.  Values must be between or equal to 10 and 99.  Default: `95` |
| **thin_volume_max_repo_size**  float | This is the maximum amount the thin volume repository will be allowed to grow.  Only has significance when *thin_volume_expansion_policy==”automatic”*.  When the percentage *thin_volume_repo_size* of *thin_volume_max_repo_size* exceeds *thin_volume_growth_alert_threshold* then a warning will be issued and the storage array will execute the *thin_volume_expansion_policy* policy.  Expansion operations when *thin_volume_expansion_policy==”automatic”* will increase the maximum repository size.  The default will be the same as size (in size_unit) |
| **thin_volume_repo_size**  integer | This value (in size_unit) sets the allocated space for the thin provisioned repository.  Initial value must between or equal to 4gb and 256gb in increments of 4gb.  During expansion operations the increase must be between or equal to 4gb and 256gb in increments of 4gb.  This option has no effect during expansion if *thin_volume_expansion_policy==”automatic”*.  Generally speaking you should almost always use *thin_volume_expansion_policy==”automatic*. |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |
| **wait_for_initialization**  boolean  added in netapp_eseries.santricity 2.8 | Forces the module to wait for expansion operations to complete before continuing.  Choices:   - `false` ← (default) - `true` |
| **workload_name**  string  added in netapp_eseries.santricity 2.8 | Label for the workload defined by the metadata.  When *workload_name* and *metadata* are specified then the defined workload will be added to the storage array.  When *workload_name* exists on the storage array but the metadata is different then the workload definition will be updated. (Changes will update all associated volumes!)  Existing workloads can be retrieved using **ERROR while parsing**: While parsing M() at index 43: Module name “netapp_e_facts” is not a FQCN. |
| **write_cache_enable**  boolean  added in netapp_eseries.santricity 2.8 | Indicates whether write-back caching should be enabled for the volume.  Choices:   - `false` - `true` ← (default) |

## [Notes](netapp_e_volume_module.md#id3)

> **Note:**
>
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](netapp_e_volume_module.md#id4)

```yaml+jinja
- name: Create simple volume with workload tags (volume meta data)
  netapp_e_volume:
    ssid: "{{ ssid }}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
    validate_certs: "{{ netapp_api_validate_certs }}"
    state: present
    name: volume
    storage_pool_name: storage_pool
    size: 300
    size_unit: gb
    workload_name: volume_tag
    metadata:
      key1: value1
      key2: value2
- name: Create a thin volume
  netapp_e_volume:
    ssid: "{{ ssid }}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
    validate_certs: "{{ netapp_api_validate_certs }}"
    state: present
    name: volume1
    storage_pool_name: storage_pool
    size: 131072
    size_unit: gb
    thin_provision: true
    thin_volume_repo_size: 32
    thin_volume_max_repo_size: 1024
- name: Expand thin volume's virtual size
  netapp_e_volume:
    ssid: "{{ ssid }}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
    validate_certs: "{{ netapp_api_validate_certs }}"
    state: present
    name: volume1
    storage_pool_name: storage_pool
    size: 262144
    size_unit: gb
    thin_provision: true
    thin_volume_repo_size: 32
    thin_volume_max_repo_size: 1024
- name: Expand thin volume's maximum repository size
  netapp_e_volume:
    ssid: "{{ ssid }}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
    validate_certs: "{{ netapp_api_validate_certs }}"
    state: present
    name: volume1
    storage_pool_name: storage_pool
    size: 262144
    size_unit: gb
    thin_provision: true
    thin_volume_repo_size: 32
    thin_volume_max_repo_size: 2048
- name: Delete volume
  netapp_e_volume:
    ssid: "{{ ssid }}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
    validate_certs: "{{ netapp_api_validate_certs }}"
    state: absent
    name: volume
```

## [Return Values](netapp_e_volume_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | State of volume  Returned: always  Sample: `"Standard volume [workload_vol_1] has been created."` |

### Authors

- Kevin Hulquest (@hulquest)
- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
