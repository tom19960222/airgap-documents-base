---
collection: ansible
version: "6"
title: "community.general.one_image_info module – Gather information on OpenNebula images"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/one_image_info_module.html
fetched_at: 2026-07-27T17:11:15+00:00
---
# community.general.one_image_info module – Gather information on OpenNebula images

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
> see [Requirements](one_image_info_module.md#ansible-collections-community-general-one-image-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.one_image_info`.

- [Synopsis](one_image_info_module.md#synopsis)
- [Requirements](one_image_info_module.md#requirements)
- [Parameters](one_image_info_module.md#parameters)
- [Examples](one_image_info_module.md#examples)
- [Return Values](one_image_info_module.md#return-values)

## [Synopsis](one_image_info_module.md#id1)

- Gather information on OpenNebula images.
- This module was called `one_image_facts` before Ansible 2.9. The usage did not change.

## [Requirements](one_image_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- pyone

## [Parameters](one_image_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_password**  string | Password of the user to login into OpenNebula RPC server. If not set  then the value of the `ONE_PASSWORD` environment variable is used. |
| **api_url**  string | URL of the OpenNebula RPC server.  It is recommended to use HTTPS so that the username/password are not  transferred over the network unencrypted.  If not set then the value of the `ONE_URL` environment variable is used. |
| **api_username**  string | Name of the user to login into the OpenNebula RPC server. If not set  then the value of the `ONE_USERNAME` environment variable is used. |
| **ids**  aliases: id  list / elements=string | A list of images ids whose facts you want to gather. |
| **name**  string | A `name` of the image whose facts will be gathered.  If the `name` begins with ‘~’ the `name` will be used as regex pattern  which restricts the list of images (whose facts will be returned) whose names match specified regex.  Also, if the `name` begins with ‘~\*’ case-insensitive matching will be performed.  See examples for more details. |

## [Examples](one_image_info_module.md#id4)

```yaml+jinja
- name: Gather facts about all images
  community.general.one_image_info:
  register: result

- name: Print all images facts
  ansible.builtin.debug:
    msg: result

- name: Gather facts about an image using ID
  community.general.one_image_info:
    ids:
      - 123

- name: Gather facts about an image using the name
  community.general.one_image_info:
    name: 'foo-image'
  register: foo_image

- name: Gather facts about all IMAGEs whose name matches regex 'app-image-.*'
  community.general.one_image_info:
    name: '~app-image-.*'
  register: app_images

- name: Gather facts about all IMAGEs whose name matches regex 'foo-image-.*' ignoring cases
  community.general.one_image_info:
    name: '~*foo-image-.*'
  register: foo_images
```

## [Return Values](one_image_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **images**  complex | A list of images info  Returned: success |
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
- Jan Meerkamp (@meerkampdvv)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
