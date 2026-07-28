---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_iso module – Manages ISO images on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_iso_module.html
fetched_at: 2026-07-28T02:45:56+00:00
---
# ngine_io.cloudstack.cs_iso module – Manages ISO images on Apache CloudStack based clouds.

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
> see [Requirements](cs_iso_module.md#ansible-collections-ngine-io-cloudstack-cs-iso-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_iso`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_iso_module.md#synopsis)
- [Requirements](cs_iso_module.md#requirements)
- [Parameters](cs_iso_module.md#parameters)
- [Notes](cs_iso_module.md#notes)
- [Examples](cs_iso_module.md#examples)
- [Return Values](cs_iso_module.md#return-values)

## [Synopsis](cs_iso_module.md#id1)

- Register and remove ISO images.

## [Requirements](cs_iso_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_iso_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the ISO is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **bootable**  boolean | Register the ISO to be bootable. Only used if *state* is present.  **Choices:**   - `false` - `true` |
| **checksum**  string | The MD5 checksum value of this ISO. If set, we search by checksum instead of name. |
| **cross_zones**  boolean | Whether the ISO should be synced or removed across zones.  Mutually exclusive with *zone*.  **Choices:**   - `false` ← (default) - `true` |
| **display_text**  string | Display text of the ISO.  If not specified, *name* will be used. |
| **domain**  string | Domain the ISO is related to. |
| **is_dynamically_scalable**  boolean | Register the ISO having XS/VMware tools installed inorder to support dynamic scaling of VM cpu/memory. Only used if *state* is present.  **Choices:**   - `false` - `true` |
| **is_featured**  boolean | Register the ISO to be featured. Only used if *state* is present.  **Choices:**   - `false` - `true` |
| **is_public**  boolean | Register the ISO to be publicly available to all users. Only used if *state* is present.  **Choices:**   - `false` - `true` |
| **is_ready**  boolean | This flag is used for searching existing ISOs. If set to `yes`, it will only list ISO ready for deployment e.g. successfully downloaded and installed. Recommended to set it to `no`.  **Choices:**   - `false` ← (default) - `true` |
| **iso_filter**  string | Name of the filter used to search for the ISO.  **Choices:**   - `"featured"` - `"self"` ← (default) - `"selfexecutable"` - `"sharedexecutable"` - `"executable"` - `"community"` |
| **name**  string / required | Name of the ISO. |
| **os_type**  string | Name of the OS that best represents the OS of this ISO. If the iso is bootable this parameter needs to be passed. Required if *state* is present. |
| **poll_async**  boolean | Poll async jobs until job has finished.  **Choices:**   - `false` - `true` ← (default) |
| **project**  string | Name of the project the ISO to be registered in. |
| **state**  string | State of the ISO.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: tag  list / elements=dictionary | List of tags. Tags are a list of dictionaries having keys *key* and *value*.  To delete all tags, set a empty list e.g. *tags: []*. |
| **url**  string | URL where the ISO can be downloaded from. Required if *state* is present. |
| **zone**  string | Name of the zone you wish the ISO to be registered or deleted from.  Required when *cross_zones* is `no` |

## [Notes](cs_iso_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_iso_module.md#id5)

```yaml+jinja
- name: Register an ISO if ISO name does not already exist
  ngine_io.cloudstack.cs_iso:
    name: Debian 7 64-bit
    zone: zone01
    url: http://mirror.switch.ch/ftp/mirror/debian-cd/current/amd64/iso-cd/debian-7.7.0-amd64-netinst.iso
    os_type: Debian GNU/Linux 7(64-bit)

- name: Register an ISO with given name if ISO md5 checksum does not already exist
  ngine_io.cloudstack.cs_iso:
    name: Debian 7 64-bit
    zone: zone01
    url: http://mirror.switch.ch/ftp/mirror/debian-cd/current/amd64/iso-cd/debian-7.7.0-amd64-netinst.iso
    os_type: Debian GNU/Linux 7(64-bit)
    checksum: 0b31bccccb048d20b551f70830bb7ad0

- name: Remove an ISO by name
  ngine_io.cloudstack.cs_iso:
    name: Debian 7 64-bit
    zone: zone01
    state: absent

- name: Remove an ISO by checksum
  ngine_io.cloudstack.cs_iso:
    name: Debian 7 64-bit
    zone: zone01
    checksum: 0b31bccccb048d20b551f70830bb7ad0
    state: absent
```

## [Return Values](cs_iso_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the ISO is related to.  **Returned:** success  **Sample:** `"example account"` |
| **bootable**  boolean | True if the ISO is bootable.  **Returned:** success  **Sample:** `true` |
| **checksum**  string | MD5 checksum of the ISO.  **Returned:** success  **Sample:** `"0b31bccccb048d20b551f70830bb7ad0"` |
| **created**  string | Date of registering.  **Returned:** success  **Sample:** `"2015-03-29T14:57:06+0200"` |
| **cross_zones**  boolean | true if the ISO is managed across all zones, false otherwise.  **Returned:** success  **Sample:** `false` |
| **display_text**  string | Text to be displayed of the ISO.  **Returned:** success  **Sample:** `"Debian 7.7 64-bit minimal 2015-03-19"` |
| **domain**  string | Domain the ISO is related to.  **Returned:** success  **Sample:** `"example domain"` |
| **format**  string | Format of the ISO.  **Returned:** success  **Sample:** `"ISO"` |
| **id**  string | UUID of the ISO.  **Returned:** success  **Sample:** `"a6f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **is_featured**  boolean | True if the ISO is featured.  **Returned:** success  **Sample:** `true` |
| **is_public**  boolean | True if the ISO is public.  **Returned:** success  **Sample:** `true` |
| **is_ready**  boolean | True if the ISO is ready to be deployed from.  **Returned:** success  **Sample:** `true` |
| **name**  string | Name of the ISO.  **Returned:** success  **Sample:** `"Debian 7 64-bit"` |
| **os_type**  string | Typo of the OS.  **Returned:** success  **Sample:** `"CentOS 6.5 (64-bit)"` |
| **project**  string | Project the ISO is related to.  **Returned:** success  **Sample:** `"example project"` |
| **status**  string | Status of the ISO.  **Returned:** success  **Sample:** `"Successfully Installed"` |
| **tags**  dictionary | List of resource tags associated with the ISO.  **Returned:** success  **Sample:** `"[ { \"key\": \"foo\", \"value\": \"bar\" } ]"` |
| **zone**  string | Name of zone the ISO is registered in.  **Returned:** success  **Sample:** `"zuerich"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
