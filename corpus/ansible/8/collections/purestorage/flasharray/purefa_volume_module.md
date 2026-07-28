---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_volume module – Manage volumes on Pure Storage FlashArrays"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_volume_module.html
fetched_at: 2026-07-28T02:51:40+00:00
---
# purestorage.flasharray.purefa_volume module – Manage volumes on Pure Storage FlashArrays

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flasharray/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_volume_module.md#ansible-collections-purestorage-flasharray-purefa-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_volume`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_volume_module.md#synopsis)
- [Requirements](purefa_volume_module.md#requirements)
- [Parameters](purefa_volume_module.md#parameters)
- [Notes](purefa_volume_module.md#notes)
- [Examples](purefa_volume_module.md#examples)
- [Return Values](purefa_volume_module.md#return-values)

## [Synopsis](purefa_volume_module.md#id1)

- Create, delete or extend the capacity of a volume on Pure Storage FlashArray.

## [Requirements](purefa_volume_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **add_to_pgs**  list / elements=string  *added in purestorage.flasharray 1.14.0* | A new volume will be added to the specified protection groups on creation |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **bw_qos**  aliases: qos  string | Bandwidth limit for volume in M or G units. M will set MB/s G will set GB/s To clear an existing QoS setting use 0 (zero) |
| **count**  integer | Number of volumes to be created in a multiple volume creation  Only supported from Purity//FA v6.0.0 and higher |
| **digits**  integer | Number of digits to use for multiple volume count. This will pad the index number with zeros where necessary  Only supported from Purity//FA v6.0.0 and higher  Range is between 1 and 10  **Default:** `1` |
| **eradicate**  boolean | Define whether to eradicate the volume on delete or leave in trash.  **Choices:**   - `false` ← (default) - `true` |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **iops_qos**  string | IOPs limit for volume - use value or K or M K will mean 1000 M will mean 1000000 To clear an existing IOPs setting use 0 (zero) |
| **move**  string | Move a volume in and out of a pod or vgroup  Provide the name of pod or vgroup to move the volume to  Pod and Vgroup names must be unique in the array  To move to the local array, specify `local`  This is not idempotent - use `ignore_errors` in the play |
| **name**  string / required | The name of the volume.  Volume could be created in a POD with this syntax POD_NAME::VOLUME_NAME.  Volume could be created in a volume group with this syntax VG_NAME/VOLUME_NAME.  Multi-volume support available from Purity//FA 6.0.0 **\*\*\*NOTE\*\*\*** Manual deletion or eradication of individual volumes created using multi-volume will cause idempotency to fail  Multi-volume support only exists for volume creation |
| **overwrite**  boolean | Define whether to overwrite a target volume if it already exisits.  **Choices:**   - `false` ← (default) - `true` |
| **pgroup**  string  *added in purestorage.flasharray 1.8.0* | Name of exisitng, not deleted, protection group to add volume to  Only application for volume(s) creation  Superceeded from Purity//FA 6.3.4 by *add_to_pgs* |
| **priority_operator**  string  *added in purestorage.flasharray 1.13.0* | DMM Priority Adjustment operator  **Choices:**   - `"="` - `"+"` - `"-"` |
| **priority_value**  integer  *added in purestorage.flasharray 1.13.0* | DMM Priority Adjustment value  **Choices:**   - `-10` - `0` - `10` |
| **promotion_state**  string  *added in purestorage.flasharray 1.16.0* | Promote or demote the volume so that the volume starts or stops accepting write requests.  **Choices:**   - `"promoted"` - `"demoted"` |
| **rename**  string | Value to rename the specified volume to.  Rename only applies to the container the current volumes is in.  There is no requirement to specify the pod or vgroup name as this is implied. |
| **size**  string | Volume size in M, G, T or P units. |
| **start**  integer | Number at which to start the multiple volume creation index  Only supported from Purity//FA v6.0.0 and higher  **Default:** `0` |
| **state**  string | Define whether the volume should exist or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **suffix**  string | Suffix string, if required, for multiple volume create  Volume names will be formed as *<name>#I<suffix>*, where *#* is a placeholder for the volume index See associated descriptions  Only supported from Purity//FA v6.0.0 and higher  **Default:** `""` |
| **target**  string | The name of the target volume, if copying. |
| **with_default_protection**  boolean  *added in purestorage.flasharray 1.14.0* | Whether to add the default container protection groups to those specified in *add_to_pgs* as the inital protection of a new volume.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](purefa_volume_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_volume_module.md#id5)

```yaml+jinja
- name: Create new volume named foo with a QoS limit
  purestorage.flasharray.purefa_volume:
    name: foo
    size: 1T
    bw_qos: 58M
    iops_qos: 23K
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Create new volume named foo with a DMM priority (Purity//FA 6.1.2+)
  purestorage.flasharray.purefa_volume:
    name: foo
    size: 1T
    priority_operator: +
    priorty_value: 10
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Create new volume named foo in pod bar in protection group pg1
  purestorage.flasharray.purefa_volume:
    name: bar::foo
    prgoup: pg1
    size: 1T
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Create 10 volumes with index starting at 10 but padded with 3 digits
  purestorage.flasharray.purefa_volume:
    name: foo
    size: 1T
    suffix: bar
    count: 10
    start: 10
    digits: 3
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Extend the size of an existing volume named foo
  purestorage.flasharray.purefa_volume:
    name: foo
    size: 2T
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Delete and eradicate volume named foo
  purestorage.flasharray.purefa_volume:
    name: foo
    eradicate: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Create clone of volume bar named foo
  purestorage.flasharray.purefa_volume:
    name: foo
    target: bar
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Overwrite volume bar with volume foo
  purestorage.flasharray.purefa_volume:
    name: foo
    target: bar
    overwrite: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Clear volume QoS from volume foo
  purestorage.flasharray.purefa_volume:
    name: foo
    bw_qos: 0
    iops_qos: 0
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Move local volume foo from local array to pod bar
  purestorage.flasharray.purefa_volume:
    name: foo
    move: bar
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Move volume foo in pod bar to local array
  purestorage.flasharray.purefa_volume:
    name: bar::foo
    move: local
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Move volume foo in pod bar to vgroup fin
  purestorage.flasharray.purefa_volume:
    name: bar::foo
    move: fin
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

## [Return Values](purefa_volume_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **volume**  dictionary | A dictionary describing the changed volume. Only some attributes below will be returned with various actions.  **Returned:** success |
| **bandwidth_limit**  integer | Volume bandwidth limit in bytes/sec  **Returned:** success |
| **created**  string | Volume creation time  **Returned:** success  **Sample:** `"2019-03-13T22:49:24Z"` |
| **iops_limit**  integer | Volume IOPs limit  **Returned:** success |
| **name**  string | Volume name  **Returned:** success |
| **nvme_nguid**  string | Volume NVMe namespace globally unique identifier  **Returned:** success  **Sample:** `"eui.00cd6b99ef25864724a937c5000be684"` |
| **page83_naa**  string | Volume NAA canonical name  **Returned:** success  **Sample:** `"naa.624a9370361019ecace43db3000120a4"` |
| **priority_operator**  string | DMM Priority Adjustment operator  **Returned:** success |
| **priority_value**  integer | DMM Priority Adjustment value  **Returned:** success |
| **serial**  string | Volume serial number  **Returned:** success  **Sample:** `"361019ECACE43D83000120A4"` |
| **size**  integer | Volume size in bytes  **Returned:** success |
| **source**  string | Volume name of source volume used for volume copy  **Returned:** success |

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
