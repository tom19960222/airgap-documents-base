---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_volume module – Manages volumes on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_volume_module.html
fetched_at: 2026-07-28T02:46:36+00:00
---
# ngine_io.cloudstack.cs_volume module – Manages volumes on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ui/repo/published/ngine_io/cloudstack/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_volume_module.md#ansible-collections-ngine-io-cloudstack-cs-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_volume`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_volume_module.md#synopsis)
- [Requirements](cs_volume_module.md#requirements)
- [Parameters](cs_volume_module.md#parameters)
- [Notes](cs_volume_module.md#notes)
- [Examples](cs_volume_module.md#examples)
- [Return Values](cs_volume_module.md#return-values)

## [Synopsis](cs_volume_module.md#id1)

- Create, destroy, attach, detach, extract or upload volumes.

## [Requirements](cs_volume_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the volume is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **custom_id**  string | Custom id to the resource.  Allowed to Root Admins only. |
| **device_id**  integer | ID of the device on a VM the volume is attached to.  Only considered if *state* is `attached`. |
| **disk_offering**  string | Name of the disk offering to be used.  Required one of *disk_offering*, *snapshot* if volume is not already *state=present*. |
| **display_volume**  boolean | Whether to display the volume to the end user or not.  Allowed to Root Admins only.  **Choices:**   - `false` - `true` |
| **domain**  string | Name of the domain the volume to be deployed in. |
| **force**  boolean | Force removal of volume even it is attached to a VM.  Considered on *state=absent* only.  **Choices:**   - `false` ← (default) - `true` |
| **format**  string | The format for the volume.  Only considered if *state=uploaded*.  **Choices:**   - `"QCOW2"` - `"RAW"` - `"VHD"` - `"VHDX"` - `"OVA"` |
| **max_iops**  integer | Max iops |
| **min_iops**  integer | Min iops |
| **mode**  string | Mode for the volume extraction.  Only considered if *state=extracted*.  **Choices:**   - `"http_download"` ← (default) - `"ftp_upload"` |
| **name**  string / required | Name of the volume.  *name* can only contain ASCII letters. |
| **poll_async**  boolean | Poll async jobs until job has finished.  **Choices:**   - `false` - `true` ← (default) |
| **project**  string | Name of the project the volume to be deployed in. |
| **shrink_ok**  boolean | Whether to allow to shrink the volume.  **Choices:**   - `false` ← (default) - `true` |
| **size**  integer | Size of disk in GB |
| **snapshot**  string | The snapshot name for the disk volume.  Required one of *disk_offering*, *snapshot* if volume is not already *state=present*. |
| **state**  string | State of the volume.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"attached"` - `"detached"` - `"extracted"` - `"uploaded"` |
| **tags**  aliases: tag  list / elements=dictionary | List of tags. Tags are a list of dictionaries having keys *key* and *value*.  To delete all tags, set a empty list e.g. *tags: []*. |
| **url**  string | URL to which the volume would be extracted on *state=extracted*  or the URL where to download the volume on *state=uploaded*.  Only considered if *state* is `extracted` or `uploaded`. |
| **vm**  string | Name of the virtual machine to attach the volume to. |
| **zone**  string / required | Name of the zone in which the volume should be deployed. |

## [Notes](cs_volume_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_volume_module.md#id5)

```yaml+jinja
- name: create volume within project and zone with specified storage options
  ngine_io.cloudstack.cs_volume:
    name: web-vm-1-volume
    project: Integration
    zone: ch-zrh-ix-01
    disk_offering: PerfPlus Storage
    size: 20

- name: create/attach volume to instance
  ngine_io.cloudstack.cs_volume:
    name: web-vm-1-volume
    zone: zone01
    disk_offering: PerfPlus Storage
    size: 20
    vm: web-vm-1
    state: attached

- name: detach volume
  ngine_io.cloudstack.cs_volume:
    name: web-vm-1-volume
    zone: zone01
    state: detached

- name: remove volume
  ngine_io.cloudstack.cs_volume:
    name: web-vm-1-volume
    zone: zone01
    state: absent

- name: Extract DATA volume to make it downloadable
  ngine_io.cloudstack.cs_volume:
    state: extracted
    name: web-vm-1-volume
    zone: zone01
  register: data_vol_out

- name: Create new volume by downloading source volume
  ngine_io.cloudstack.cs_volume:
    state: uploaded
    name: web-vm-1-volume-2
    zone: zone01
    format: VHD
    url: "{{ data_vol_out.url }}"
```

## [Return Values](cs_volume_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **attached**  string | Date of the volume was attached.  **Returned:** success  **Sample:** `"2014-12-01T14:57:57+0100"` |
| **created**  string | Date of the volume was created.  **Returned:** success  **Sample:** `"2014-12-01T14:57:57+0100"` |
| **device_id**  integer | Id of the device on user vm the volume is attached to (not returned when detached)  **Returned:** success  **Sample:** `1` |
| **display_name**  string | Display name of the volume.  **Returned:** success  **Sample:** `"web-volume-01"` |
| **domain**  string | Domain the volume belongs to  **Returned:** success  **Sample:** `"example domain"` |
| **group**  string | Group the volume belongs to  **Returned:** success  **Sample:** `"web"` |
| **id**  string | ID of the volume.  **Returned:** success |
| **name**  string | Name of the volume.  **Returned:** success  **Sample:** `"web-volume-01"` |
| **project**  string | Project the volume belongs to  **Returned:** success  **Sample:** `"Production"` |
| **size**  integer | Size of disk volume.  **Returned:** success  **Sample:** `20` |
| **state**  string | State of the volume  **Returned:** success  **Sample:** `"Attached"` |
| **type**  string | Disk volume type.  **Returned:** success  **Sample:** `"DATADISK"` |
| **url**  string | The url of the uploaded volume or the download url depending extraction mode.  **Returned:** success when *state=extracted*  **Sample:** `"http://1.12.3.4/userdata/387e2c7c-7c42-4ecc-b4ed-84e8367a1965.vhd"` |
| **vm**  string | Name of the vm the volume is attached to (not returned when detached)  **Returned:** success  **Sample:** `"web-01"` |
| **zone**  string | Name of zone the volume is in.  **Returned:** success  **Sample:** `"ch-gva-2"` |

### Authors

- Jefferson Girão (@jeffersongirao)
- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
