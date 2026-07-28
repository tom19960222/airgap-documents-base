---
collection: ansible
version: "6"
title: "community.google.gce_img module – utilize GCE image resources"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/google/gce_img_module.html
fetched_at: 2026-07-27T17:15:17+00:00
---
# community.google.gce_img module – utilize GCE image resources

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
> see [Requirements](gce_img_module.md#ansible-collections-community-google-gce-img-module-requirements) for details.
>
> To use it in a playbook, specify: `community.google.gce_img`.

- [Synopsis](gce_img_module.md#synopsis)
- [Requirements](gce_img_module.md#requirements)
- [Parameters](gce_img_module.md#parameters)
- [Examples](gce_img_module.md#examples)

## [Synopsis](gce_img_module.md#id1)

- This module can create and delete GCE private images from gzipped compressed tarball containing raw disk data or from existing detached disks in any zone. <https://cloud.google.com/compute/docs/images>

## [Requirements](gce_img_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- apache-libcloud

## [Parameters](gce_img_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | an optional description |
| **family**  string | an optional family name |
| **name**  string / required | the name of the image to create or delete |
| **pem_file**  path | path to the pem file associated with the service account email |
| **project_id**  string | your GCE project ID |
| **service_account_email**  string | service account email |
| **source**  string | the source disk or the Google Cloud Storage URI to create the image from |
| **state**  string | desired state of the image  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | timeout for the operation  Default: `180` |
| **zone**  string | the zone of the disk specified by source  Default: `"us-central1-a"` |

## [Examples](gce_img_module.md#id4)

```yaml+jinja
- name: Create an image named test-image from the disk 'test-disk' in zone us-central1-a
  community.google.gce_img:
    name: test-image
    source: test-disk
    zone: us-central1-a
    state: present

- name: Create an image named test-image from a tarball in Google Cloud Storage
  community.google.gce_img:
    name: test-image
    source: https://storage.googleapis.com/bucket/path/to/image.tgz

- name: Alternatively use the gs scheme
  community.google.gce_img:
    name: test-image
    source: gs://bucket/path/to/image.tgz

- name: Delete an image named test-image
  community.google.gce_img:
    name: test-image
    state: absent
```

### Authors

- Tom Melendez (@supertom)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.google/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.google)
