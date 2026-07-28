---
collection: ansible
version: "6"
title: "community.google.gce_pd module – utilize GCE persistent disk resources"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/google/gce_pd_module.html
fetched_at: 2026-07-27T17:15:21+00:00
---
# community.google.gce_pd module – utilize GCE persistent disk resources

> **Note:**
>
> This module is part of the [community.google collection](https://galaxy.ansible.com/community/google) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.google`.
> You need further requirements to be able to use this module,
> see [Requirements](gce_pd_module.md#ansible-collections-community-google-gce-pd-module-requirements) for details.
>
> To use it in a playbook, specify: `community.google.gce_pd`.

- [Synopsis](gce_pd_module.md#synopsis)
- [Requirements](gce_pd_module.md#requirements)
- [Parameters](gce_pd_module.md#parameters)
- [Examples](gce_pd_module.md#examples)

## [Synopsis](gce_pd_module.md#id1)

- This module can create and destroy unformatted GCE persistent disks <https://developers.google.com/compute/docs/disks#persistentdisks>. It also supports attaching and detaching disks from running instances. Full install/configuration instructions for the gce\* modules can be found in the comments of ansible/test/gce_tests.py.

## [Requirements](gce_pd_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- apache-libcloud >= 0.13.3, >= 0.17.0 if using JSON credentials

## [Parameters](gce_pd_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **credentials_file**  path | path to the JSON file associated with the service account email |
| **delete_on_termination**  boolean | If `yes`, deletes the volume when instance is terminated  Choices:   - `false` - `true` |
| **detach_only**  boolean | do not destroy the disk, merely detach it from an instance  Choices:   - `false` - `true` |
| **disk_type**  string | Specify a `pd-standard` disk or `pd-ssd` for an SSD disk.  Default: `"pd-standard"` |
| **external_projects**  list / elements=string | A list of other projects (accessible with the provisioning credentials) to be searched for the image. |
| **image**  string | the source image to use for the disk |
| **image_family**  string | The image family to use to create the instance. If *image* has been used *image_family* is ignored. Cannot specify both *image* and *source*. |
| **instance_name**  string | instance name if you wish to attach or detach the disk |
| **mode**  string | GCE mount mode of disk, READ_ONLY (default) or READ_WRITE  Choices:   - `"READ_WRITE"` - `"READ_ONLY"` ← (default) |
| **name**  string / required | name of the disk |
| **pem_file**  path | path to the pem file associated with the service account email This option is deprecated. Use ‘credentials_file’. |
| **project_id**  string | your GCE project ID |
| **service_account_email**  string | service account email |
| **size_gb**  string | whole integer size of disk (in GB) to create, default is 10 GB  Default: `"10"` |
| **snapshot**  string | the source snapshot to use for the disk |
| **state**  string | desired state of the persistent disk  Available choices are: `active`, `present`, `absent`, `deleted`.  Default: `"present"` |
| **zone**  string | zone in which to create the disk  Default: `"us-central1-b"` |

## [Examples](gce_pd_module.md#id4)

```yaml+jinja
- name: Simple attachment action to an existing instance
  local_action:
    module: gce_pd
    instance_name: notlocalhost
    size_gb: 5
    name: pd
```

### Authors

- Eric Johnson (@erjohnso)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.google/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.google)
