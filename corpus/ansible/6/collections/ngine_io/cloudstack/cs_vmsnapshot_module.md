---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_vmsnapshot module – Manages VM snapshots on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_vmsnapshot_module.html
fetched_at: 2026-07-28T00:15:53+00:00
---
# ngine_io.cloudstack.cs_vmsnapshot module – Manages VM snapshots on Apache CloudStack based clouds.

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
> see [Requirements](cs_vmsnapshot_module.md#ansible-collections-ngine-io-cloudstack-cs-vmsnapshot-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_vmsnapshot`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_vmsnapshot_module.md#synopsis)
- [Requirements](cs_vmsnapshot_module.md#requirements)
- [Parameters](cs_vmsnapshot_module.md#parameters)
- [Notes](cs_vmsnapshot_module.md#notes)
- [Examples](cs_vmsnapshot_module.md#examples)
- [Return Values](cs_vmsnapshot_module.md#return-values)

## [Synopsis](cs_vmsnapshot_module.md#id1)

- Create, remove and revert VM from snapshots.

## [Requirements](cs_vmsnapshot_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_vmsnapshot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the VM snapshot is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **description**  string | Description of the snapshot. |
| **domain**  string | Domain the VM snapshot is related to. |
| **name**  aliases: display_name  string / required | Unique Name of the snapshot. In CloudStack terms display name. |
| **poll_async**  boolean | Poll async jobs until job has finished.  Choices:   - `false` - `true` ← (default) |
| **project**  string | Name of the project the VM is assigned to. |
| **snapshot_memory**  boolean | Snapshot memory if set to true.  Choices:   - `false` ← (default) - `true` |
| **state**  string | State of the snapshot.  Choices:   - `"present"` ← (default) - `"absent"` - `"revert"` |
| **tags**  aliases: tag  list / elements=dictionary | List of tags. Tags are a list of dictionaries having keys *key* and *value*.  To delete all tags, set a empty list e.g. *tags: []*. |
| **vm**  string / required | Name of the virtual machine. |
| **zone**  string / required | Name of the zone in which the VM is in. If not set. |

## [Notes](cs_vmsnapshot_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_vmsnapshot_module.md#id5)

```yaml+jinja
- name: Create a VM snapshot of disk and memory before an upgrade
  ngine_io.cloudstack.cs_vmsnapshot:
    name: Snapshot before upgrade
    vm: web-01
    zone: zone01
    snapshot_memory: yes

- name: Revert a VM to a snapshot after a failed upgrade
  ngine_io.cloudstack.cs_vmsnapshot:
    name: Snapshot before upgrade
    vm: web-01
    zone: zone01
    state: revert

- name: Remove a VM snapshot after successful upgrade
  ngine_io.cloudstack.cs_vmsnapshot:
    name: Snapshot before upgrade
    vm: web-01
    zone: zone01
    state: absent
```

## [Return Values](cs_vmsnapshot_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the vm snapshot is related to.  Returned: success  Sample: `"example account"` |
| **created**  string | date of the snapshot.  Returned: success  Sample: `"2015-03-29T14:57:06+0200"` |
| **current**  boolean | true if the snapshot is current  Returned: success  Sample: `true` |
| **description**  string | description of vm snapshot  Returned: success  Sample: `"snapshot brought to you by Ansible"` |
| **display_name**  string | Display name of the snapshot.  Returned: success  Sample: `"snapshot before update"` |
| **domain**  string | Domain the vm snapshot is related to.  Returned: success  Sample: `"example domain"` |
| **id**  string | UUID of the snapshot.  Returned: success  Sample: `"a6f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **name**  string | Name of the snapshot.  Returned: success  Sample: `"snapshot before update"` |
| **project**  string | Name of project the vm snapshot is related to.  Returned: success  Sample: `"Production"` |
| **state**  string | state of the vm snapshot  Returned: success  Sample: `"Allocated"` |
| **type**  string | type of vm snapshot  Returned: success  Sample: `"DiskAndMemory"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
