---
collection: ansible
version: "6"
title: "theforeman.foreman.compute_profile module – Manage Compute Profiles"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/compute_profile_module.html
fetched_at: 2026-07-28T00:20:31+00:00
---
# theforeman.foreman.compute_profile module – Manage Compute Profiles

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
> see [Requirements](compute_profile_module.md#ansible-collections-theforeman-foreman-compute-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.compute_profile`.

New in theforeman.foreman 1.0.0

- [Synopsis](compute_profile_module.md#synopsis)
- [Requirements](compute_profile_module.md#requirements)
- [Parameters](compute_profile_module.md#parameters)
- [Examples](compute_profile_module.md#examples)
- [Return Values](compute_profile_module.md#return-values)

## [Synopsis](compute_profile_module.md#id1)

- Create, update, and delete Compute Profiles

## [Requirements](compute_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](compute_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **compute_attributes**  list / elements=dictionary | Compute attributes related to this compute profile. Some of these attributes are specific to the underlying compute resource type |
| **compute_resource**  string | Name of the compute resource the attribute should be for |
| **vm_attrs**  aliases: vm_attributes  dictionary | Hash containing the data of vm_attrs |
| **name**  string / required | compute profile name |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  Choices:   - `"present"` ← (default) - `"absent"` |
| **updated_name**  string | new compute profile name |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](compute_profile_module.md#id4)

```yaml+jinja
- name: compute profile
  theforeman.foreman.compute_profile:
    name: example_compute_profile
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: another compute profile
  theforeman.foreman.compute_profile:
    name: another_example_compute_profile
    compute_attributes:
    - compute_resource: ovirt_compute_resource1
      vm_attrs:
        cluster: 'a96d44a4-f14a-1015-82c6-f80354acdf01'
        template: 'c88af4b7-a24a-453b-9ac2-bc647ca2ef99'
        instance_type: 'cb8927e7-a404-40fb-a6c1-06cbfc92e077'
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: compute profile2
  theforeman.foreman.compute_profile:
    name: example_compute_profile2
    compute_attributes:
    - compute_resource: ovirt_compute_resource01
      vm_attrs:
        cluster: a96d44a4-f14a-1015-82c6-f80354acdf01
        cores: 1
        sockets: 1
        memory: 1073741824
        ha: 0
        interfaces_attributes:
          0:
            name: ""
            network: 390666e1-dab3-4c99-9f96-006b2e2fd801
            interface: virtio
        volumes_attributes:
          0:
            size_gb: 16
            storage_domain: 19c50090-1ab4-4023-a63f-75ee1018ed5e
            preallocate: '1'
            wipe_after_delete: '0'
            interface: virtio_scsi
            bootable: 'true'
    - compute_resource: libvirt_compute_resource03
      vm_attrs:
        cpus: 1
        memory: 2147483648
        nics_attributes:
          0:
            type: bridge
            bridge: ""
            model: virtio
        volumes_attributes:
          0:
            pool_name: default
            capacity: 16G
            allocation: 16G
            format_type: raw
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: Remove compute profile
  theforeman.foreman.compute_profile:
    name: example_compute_profile2
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: absent
```

## [Return Values](compute_profile_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **compute_profiles**  list / elements=dictionary | List of compute profiles.  Returned: success |
| **compute_attributes**  list / elements=string | Attributes for this compute profile.  Returned: success |
| **id**  integer | Database id of the compute profile.  Returned: success |
| **name**  string | Name of the compute profile.  Returned: success |

### Authors

- Philipp Joos (@philippj)
- Baptiste Agasse (@bagasse)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
