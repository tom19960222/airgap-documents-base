---
collection: ansible
version: "8"
title: "community.google.gce_tag module – add or remove tag(s) to/from GCE instances"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/google/gce_tag_module.html
fetched_at: 2026-07-28T01:53:10+00:00
---
# community.google.gce_tag module – add or remove tag(s) to/from GCE instances

> **Note:**
>
> This module is part of the [community.google collection](https://galaxy.ansible.com/ui/repo/published/community/google/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.google`.
> You need further requirements to be able to use this module,
> see [Requirements](gce_tag_module.md#ansible-collections-community-google-gce-tag-module-requirements) for details.
>
> To use it in a playbook, specify: `community.google.gce_tag`.

- [Synopsis](gce_tag_module.md#synopsis)
- [Requirements](gce_tag_module.md#requirements)
- [Parameters](gce_tag_module.md#parameters)
- [Notes](gce_tag_module.md#notes)
- [Examples](gce_tag_module.md#examples)

## [Synopsis](gce_tag_module.md#id1)

- This module can add or remove tags <https://cloud.google.com/compute/docs/label-or-tag-resources#tags> to/from GCE instances. Use ‘instance_pattern’ to update multiple instances in a specify zone.

## [Requirements](gce_tag_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- apache-libcloud >= 0.17.0

## [Parameters](gce_tag_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **instance_name**  string | The name of the GCE instance to add/remove tags.  Required if `instance_pattern` is not specified. |
| **instance_pattern**  string | The pattern of GCE instance names to match for adding/removing tags. Full-Python regex is supported. See <https://docs.python.org/2/library/re.html> for details.  If `instance_name` is not specified, this field is required. |
| **pem_file**  path | Path to the PEM file associated with the service account email. |
| **project_id**  string | Your GCE project ID. |
| **service_account_email**  string | Service account email. |
| **state**  string | Desired state of the tags.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tags**  list / elements=string / required | Comma-separated list of tags to add or remove. |
| **zone**  string | The zone of the disk specified by source.  **Default:** `"us-central1-a"` |

## [Notes](gce_tag_module.md#id4)

> **Note:**
>
> - Either *instance_name* or *instance_pattern* is required.

## [Examples](gce_tag_module.md#id5)

```yaml+jinja
- name: Add tags to instance
  community.google.gce_tag:
    instance_name: staging-server
    tags: http-server,https-server,staging
    zone: us-central1-a
    state: present

- name: Remove tags from instance in default zone (us-central1-a)
  community.google.gce_tag:
    instance_name: test-server
    tags: foo,bar
    state: absent

- name: Add tags to instances in zone that match pattern
  community.google.gce_tag:
    instance_pattern: test-server-*
    tags: foo,bar
    zone: us-central1-a
    state: present
```

### Authors

- Do Hoang Khiem (@dohoangkhiem) <(>
- Tom Melendez (@supertom)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.google/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.google)
