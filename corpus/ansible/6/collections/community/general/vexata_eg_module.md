---
collection: ansible
version: "6"
title: "community.general.vexata_eg module – Manage export groups on Vexata VX100 storage arrays"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/vexata_eg_module.html
fetched_at: 2026-07-27T17:13:55+00:00
---
# community.general.vexata_eg module – Manage export groups on Vexata VX100 storage arrays

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](vexata_eg_module.md#ansible-collections-community-general-vexata-eg-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.vexata_eg`.

- [Synopsis](vexata_eg_module.md#synopsis)
- [Requirements](vexata_eg_module.md#requirements)
- [Parameters](vexata_eg_module.md#parameters)
- [Examples](vexata_eg_module.md#examples)

## [Synopsis](vexata_eg_module.md#id1)

- Create or delete export groups on a Vexata VX100 array.
- An export group is a tuple of a volume group, initiator group and port group that allows a set of volumes to be exposed to one or more hosts through specific array ports.

## [Requirements](vexata_eg_module.md#id2)

The below requirements are needed on the host that executes this module.

- Vexata VX100 storage array with VXOS >= v3.5.0 on storage array
- vexatapi >= 0.0.1
- python >= 2.7
- VEXATA_USER and VEXATA_PASSWORD environment variables must be set if user and password arguments are not passed to the module directly.

## [Parameters](vexata_eg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **array**  string / required | Vexata VX100 array hostname or IPv4 Address. |
| **ig**  string | Initiator group name. |
| **name**  string / required | Export group name. |
| **password**  string | Vexata API user password. |
| **pg**  string | Port group name. |
| **state**  string | Creates export group when present or delete when absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **user**  string | Vexata API user with administrative privileges. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` ← (default) - `true` |
| **vg**  string | Volume group name. |

## [Examples](vexata_eg_module.md#id4)

```yaml+jinja
- name: Create export group named db_export.
  community.general.vexata_eg:
    name: db_export
    vg: dbvols
    ig: dbhosts
    pg: pg1
    state: present
    array: vx100_ultra.test.com
    user: admin
    password: secret

- name: Delete export group named db_export
  community.general.vexata_eg:
    name: db_export
    state: absent
    array: vx100_ultra.test.com
    user: admin
    password: secret
```

### Authors

- Sandeep Kasargod (@vexata)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
