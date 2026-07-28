---
collection: ansible
version: "6"
title: "community.general.imgadm module – Manage SmartOS images"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/imgadm_module.html
fetched_at: 2026-07-27T17:09:43+00:00
---
# community.general.imgadm module – Manage SmartOS images

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
> see [Requirements](imgadm_module.md#ansible-collections-community-general-imgadm-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.imgadm`.

- [Synopsis](imgadm_module.md#synopsis)
- [Requirements](imgadm_module.md#requirements)
- [Parameters](imgadm_module.md#parameters)
- [Examples](imgadm_module.md#examples)
- [Return Values](imgadm_module.md#return-values)

## [Synopsis](imgadm_module.md#id1)

- Manage SmartOS virtual machine images through imgadm(1M)

## [Requirements](imgadm_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](imgadm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | Force a given operation (where supported by imgadm(1M)).  Choices:   - `false` - `true` |
| **pool**  string | zpool to import to or delete images from.  Default: `"zones"` |
| **source**  string | URI for the image source. |
| **state**  string / required | State the object operated on should be in. `imported` is an alias for for `present` and `deleted` for `absent`. When set to `vacuumed` and `uuid` to `*`, it will remove all unused images.  Choices:   - `"present"` - `"absent"` - `"deleted"` - `"imported"` - `"updated"` - `"vacuumed"` |
| **type**  string | Type for image sources.  Choices:   - `"imgapi"` ← (default) - `"docker"` - `"dsapi"` |
| **uuid**  string | Image UUID. Can either be a full UUID or `*` for all images. |

## [Examples](imgadm_module.md#id4)

```yaml+jinja
- name: Import an image
  community.general.imgadm:
    uuid: '70e3ae72-96b6-11e6-9056-9737fd4d0764'
    state: imported

- name: Delete an image
  community.general.imgadm:
    uuid: '70e3ae72-96b6-11e6-9056-9737fd4d0764'
    state: deleted

- name: Update all images
  community.general.imgadm:
    uuid: '*'
    state: updated

- name: Update a single image
  community.general.imgadm:
    uuid: '70e3ae72-96b6-11e6-9056-9737fd4d0764'
    state: updated

- name: Add a source
  community.general.imgadm:
    source: 'https://datasets.project-fifo.net'
    state: present

- name: Add a Docker source
  community.general.imgadm:
    source: 'https://docker.io'
    type: docker
    state: present

- name: Remove a source
  community.general.imgadm:
    source: 'https://docker.io'
    state: absent
```

## [Return Values](imgadm_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **source**  string | Source that is managed.  Returned: When not managing an image.  Sample: `"https://datasets.project-fifo.net"` |
| **state**  string | State of the target, after execution.  Returned: success  Sample: `"present"` |
| **uuid**  string | UUID for an image operated on.  Returned: When not managing an image source.  Sample: `"70e3ae72-96b6-11e6-9056-9737fd4d0764"` |

### Authors

- Jasper Lievisse Adriaanse (@jasperla)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
