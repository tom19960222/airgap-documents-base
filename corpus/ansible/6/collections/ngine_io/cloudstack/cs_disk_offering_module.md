---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_disk_offering module – Manages disk offerings on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_disk_offering_module.html
fetched_at: 2026-07-28T00:15:24+00:00
---
# ngine_io.cloudstack.cs_disk_offering module – Manages disk offerings on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ngine_io/cloudstack) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_disk_offering_module.md#ansible-collections-ngine-io-cloudstack-cs-disk-offering-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_disk_offering`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_disk_offering_module.md#synopsis)
- [Requirements](cs_disk_offering_module.md#requirements)
- [Parameters](cs_disk_offering_module.md#parameters)
- [Notes](cs_disk_offering_module.md#notes)
- [Examples](cs_disk_offering_module.md#examples)
- [Return Values](cs_disk_offering_module.md#return-values)

## [Synopsis](cs_disk_offering_module.md#id1)

- Create and delete disk offerings for guest VMs.
- Update display_text or display_offering of existing disk offering.

## [Requirements](cs_disk_offering_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_disk_offering_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **bytes_read_rate**  integer | Bytes read rate of the disk offering. |
| **bytes_write_rate**  integer | Bytes write rate of the disk offering. |
| **customized**  boolean | Whether disk offering iops is custom or not.  Choices:   - `false` - `true` |
| **disk_size**  integer | Size of the disk offering in GB (1GB = 1,073,741,824 bytes). |
| **display_offering**  boolean | An optional field, whether to display the offering to the end user or not.  Choices:   - `false` - `true` |
| **display_text**  string | Display text of the disk offering.  If not set, `name` will be used as `display_text` while creating. |
| **domain**  string | Domain the disk offering is related to.  Public for all domains and subdomains if not set. |
| **hypervisor_snapshot_reserve**  integer | Hypervisor snapshot reserve space as a percent of a volume.  Only for managed storage using Xen or VMware. |
| **iops_max**  integer | Max. iops of the disk offering. |
| **iops_min**  integer | Min. iops of the disk offering. |
| **iops_read_rate**  integer | IO requests read rate of the disk offering. |
| **iops_write_rate**  integer | IO requests write rate of the disk offering. |
| **name**  string / required | Name of the disk offering. |
| **provisioning_type**  string | Provisioning type used to create volumes.  Choices:   - `"thin"` - `"sparse"` - `"fat"` |
| **state**  string | State of the disk offering.  Choices:   - `"present"` ← (default) - `"absent"` |
| **storage_tags**  aliases: storage_tag  list / elements=string | The storage tags for this disk offering. |
| **storage_type**  string | The storage type of the disk offering.  Choices:   - `"local"` - `"shared"` |

## [Notes](cs_disk_offering_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_disk_offering_module.md#id5)

```yaml+jinja
- name: Create a disk offering with local storage
  ngine_io.cloudstack.cs_disk_offering:
    name: small
    display_text: Small 10GB
    disk_size: 10
    storage_type: local

- name: Create or update a disk offering with shared storage
  ngine_io.cloudstack.cs_disk_offering:
    name: small
    display_text: Small 10GB
    disk_size: 10
    storage_type: shared
    storage_tags: SAN01

- name: Remove a disk offering
  ngine_io.cloudstack.cs_disk_offering:
    name: small
    state: absent
```

## [Return Values](cs_disk_offering_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **bytes_read_rate**  integer | Bytes read rate of the disk offering  Returned: success  Sample: `1000` |
| **bytes_write_rate**  integer | Bytes write rate of the disk offering  Returned: success  Sample: `1000` |
| **created**  string | Date the offering was created  Returned: success  Sample: `"2017-11-19T10:48:59+0000"` |
| **customized**  boolean | Whether the offering uses custom IOPS or not  Returned: success  Sample: `false` |
| **disk_size**  integer | Size of the disk offering in GB  Returned: success  Sample: `10` |
| **display_offering**  boolean | Whether to display the offering to the end user or not.  Returned: success  Sample: `false` |
| **display_text**  string | Display text of the offering  Returned: success  Sample: `"Small 10GB"` |
| **domain**  string | Domain the offering is into  Returned: success  Sample: `"ROOT"` |
| **id**  string | UUID of the disk offering  Returned: success  Sample: `"a6f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **iops_max**  integer | Max iops of the disk offering  Returned: success  Sample: `1000` |
| **iops_min**  integer | Min iops of the disk offering  Returned: success  Sample: `500` |
| **iops_read_rate**  integer | IO requests per second read rate of the disk offering  Returned: success  Sample: `1000` |
| **iops_write_rate**  integer | IO requests per second write rate of the disk offering  Returned: success  Sample: `1000` |
| **name**  string | Name of the system offering  Returned: success  Sample: `"Micro"` |
| **provisioning_type**  string | Provisioning type used to create volumes  Returned: success  Sample: `"thin"` |
| **storage_tags**  list / elements=string | List of storage tags  Returned: success  Sample: `["eco"]` |
| **storage_type**  string | Storage type used to create volumes  Returned: success  Sample: `"shared"` |

### Authors

- David Passante (@dpassante)
- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
