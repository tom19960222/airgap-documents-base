---
collection: ansible
version: "6"
title: "theforeman.foreman.compute_attribute module – Manage Compute Attributes"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/compute_attribute_module.html
fetched_at: 2026-07-28T00:20:30+00:00
---
# theforeman.foreman.compute_attribute module – Manage Compute Attributes

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
> see [Requirements](compute_attribute_module.md#ansible-collections-theforeman-foreman-compute-attribute-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.compute_attribute`.

New in theforeman.foreman 1.0.0

- [Synopsis](compute_attribute_module.md#synopsis)
- [Requirements](compute_attribute_module.md#requirements)
- [Parameters](compute_attribute_module.md#parameters)
- [Examples](compute_attribute_module.md#examples)
- [Return Values](compute_attribute_module.md#return-values)

## [Synopsis](compute_attribute_module.md#id1)

- Manage Compute Attributes
- This beta version can create, and update compute attributes

## [Requirements](compute_attribute_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](compute_attribute_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **compute_profile**  string / required | Name of compute profile |
| **compute_resource**  string / required | Name of compute resource |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |
| **vm_attrs**  aliases: vm_attributes  dictionary | Hash containing the data of vm_attrs |

## [Examples](compute_attribute_module.md#id4)

```yaml+jinja
- name: "Create compute attribute"
  theforeman.foreman.compute_attribute:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    compute_profile: "Test Compute Profile"
    compute_resource: "Test Compute Resource"
    vm_attrs:
      memory_mb: '2048'
      cpu: '2'
    state: present

- name: "Update compute attribute"
  theforeman.foreman.compute_attribute:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    compute_profile: "Test Compute Profile"
    compute_resource: "Test Compute Resource"
    vm_attrs:
      memory_mb: '1024'
      cpu: '1'
    state: present
```

## [Return Values](compute_attribute_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **compute_attributes**  list / elements=dictionary | List of compute attributes.  Returned: success |
| **attributes**  dictionary | Effective attributes for the given combination of compute profile and resource.  Returned: success |
| **compute_profile_id**  integer | Database id of the associated compute profile.  Returned: success |
| **compute_profile_name**  string | Name of the associated compute profile.  Returned: success |
| **compute_resource_id**  integer | Database id of the associated compute resource.  Returned: success |
| **compute_resource_name**  string | Name of the associated compute resource.  Returned: success |
| **created_at**  string | Creation date of the compute attribute.  Returned: success |
| **id**  integer | Database id of the compute_attribute.  Returned: success |
| **name**  string | Generated friendly name for the compute attribute.  Returned: success |
| **provider_friendly_name**  string | Name of the provider type of the compute resource.  Returned: success |
| **updated_at**  string | Date of last change to the compute attribute.  Returned: success |
| **vm_attrs**  dictionary | Configured attributes.  Returned: success |

### Authors

- Manisha Singhal (@Manisha15) ATIX AG

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
