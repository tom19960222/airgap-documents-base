---
collection: ansible
version: "6"
title: "theforeman.foreman.image module – Manage Images"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/image_module.html
fetched_at: 2026-07-28T00:20:49+00:00
---
# theforeman.foreman.image module – Manage Images

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/theforeman/foreman) (version 3.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](image_module.md#ansible-collections-theforeman-foreman-image-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.image`.

New in theforeman.foreman 1.0.0

- [Synopsis](image_module.md#synopsis)
- [Requirements](image_module.md#requirements)
- [Parameters](image_module.md#parameters)
- [Examples](image_module.md#examples)
- [Return Values](image_module.md#return-values)

## [Synopsis](image_module.md#id1)

- Create, update, and delete Images

## [Requirements](image_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](image_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **architecture**  string / required | architecture of the image |
| **compute_resource**  string / required | Compute resource the image is assigned to |
| **image_password**  string | Password that is used to login into the operating system |
| **image_username**  string / required | Username that is used to login into the operating system |
| **name**  string / required | Image name |
| **operatingsystem**  string / required | Operating systems are looked up by their title which is composed as “<name> <major>.<minor>”.  You can omit the version part as long as you only have one operating system by that name. |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  Choices:   - `"present"` ← (default) - `"absent"` |
| **user_data**  boolean | Image supports user_data  Choices:   - `false` - `true` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **uuid**  aliases: image_uuid  string / required | UUID or Marketplace URN of the operatingsystem image |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](image_module.md#id4)

```yaml+jinja
- name: create Image for EC2
  theforeman.foreman.image:
     name: CentOS
     image_uuid: "ami-0ff760d16d9497662"
     image_username: "centos"
     operatingsystem: "CentOS 7"
     compute_resource: "AWS"
     architecture: "x86_64"
```

## [Return Values](image_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **images**  list / elements=dictionary | List of images.  Returned: success |

### Authors

- Mark Hlawatschek (@hlawatschek) ATIX AG

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
