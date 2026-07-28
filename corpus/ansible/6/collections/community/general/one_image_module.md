---
collection: ansible
version: "6"
title: "community.general.one_image module – Manages OpenNebula images"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/one_image_module.html
fetched_at: 2026-07-27T17:11:14+00:00
---
# community.general.one_image module – Manages OpenNebula images

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
> see [Requirements](one_image_module.md#ansible-collections-community-general-one-image-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.one_image`.

- [Synopsis](one_image_module.md#synopsis)
- [Requirements](one_image_module.md#requirements)
- [Parameters](one_image_module.md#parameters)
- [Examples](one_image_module.md#examples)
- [Return Values](one_image_module.md#return-values)

## [Synopsis](one_image_module.md#id1)

- Manages OpenNebula images

## [Requirements](one_image_module.md#id2)

The below requirements are needed on the host that executes this module.

- pyone

## [Parameters](one_image_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_password**  string | Password of the user to login into OpenNebula RPC server. If not set  then the value of the `ONE_PASSWORD` environment variable is used. |
| **api_url**  string | URL of the OpenNebula RPC server.  It is recommended to use HTTPS so that the username/password are not  transferred over the network unencrypted.  If not set then the value of the `ONE_URL` environment variable is used. |
| **api_username**  string | Name of the user to login into the OpenNebula RPC server. If not set  then the value of the `ONE_USERNAME` environment variable is used. |
| **enabled**  boolean | Whether the image should be enabled or disabled.  Choices:   - `false` - `true` |
| **id**  integer | A `id` of the image you would like to manage. |
| **name**  string | A `name` of the image you would like to manage. |
| **new_name**  string | A name that will be assigned to the existing or new image.  In the case of cloning, by default `new_name` will take the name of the origin image with the prefix ‘Copy of’. |
| **state**  string | `present` - state that is used to manage the image  `absent` - delete the image  `cloned` - clone the image  `renamed` - rename the image to the `new_name`  Choices:   - `"present"` ← (default) - `"absent"` - `"cloned"` - `"renamed"` |

## [Examples](one_image_module.md#id4)

```yaml+jinja
- name: Fetch the IMAGE by id
  community.general.one_image:
    id: 45
  register: result

- name: Print the IMAGE properties
  ansible.builtin.debug:
    var: result

- name: Rename existing IMAGE
  community.general.one_image:
    id: 34
    state: renamed
    new_name: bar-image

- name: Disable the IMAGE by id
  community.general.one_image:
    id: 37
    enabled: false

- name: Enable the IMAGE by name
  community.general.one_image:
    name: bar-image
    enabled: true

- name: Clone the IMAGE by name
  community.general.one_image:
    name: bar-image
    state: cloned
    new_name: bar-image-clone
  register: result

- name: Delete the IMAGE by id
  community.general.one_image:
    id: '{{ result.id }}'
    state: absent
```

## [Return Values](one_image_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **group_id**  integer | image’s group id  Returned: success  Sample: `1` |
| **group_name**  string | image’s group name  Returned: success  Sample: `"one-users"` |
| **id**  integer | image id  Returned: success  Sample: `153` |
| **name**  string | image name  Returned: success  Sample: `"app1"` |
| **owner_id**  integer | image’s owner id  Returned: success  Sample: `143` |
| **owner_name**  string | image’s owner name  Returned: success  Sample: `"ansible-test"` |
| **running_vms**  integer | count of running vms that use this image  Returned: success  Sample: `7` |
| **state**  string | state of image instance  Returned: success  Sample: `"READY"` |
| **used**  boolean | is image in use  Returned: success  Sample: `true` |

### Authors

- Milan Ilic (@ilicmilan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
