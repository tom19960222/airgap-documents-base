---
collection: ansible
version: "6"
title: "community.google.gce_snapshot module – Create or destroy snapshots for GCE storage volumes"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/google/gce_snapshot_module.html
fetched_at: 2026-07-27T17:15:22+00:00
---
# community.google.gce_snapshot module – Create or destroy snapshots for GCE storage volumes

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
> see [Requirements](gce_snapshot_module.md#ansible-collections-community-google-gce-snapshot-module-requirements) for details.
>
> To use it in a playbook, specify: `community.google.gce_snapshot`.

- [Synopsis](gce_snapshot_module.md#synopsis)
- [Requirements](gce_snapshot_module.md#requirements)
- [Parameters](gce_snapshot_module.md#parameters)
- [Examples](gce_snapshot_module.md#examples)
- [Return Values](gce_snapshot_module.md#return-values)

## [Synopsis](gce_snapshot_module.md#id1)

- Manages snapshots for GCE instances. This module manages snapshots for the storage volumes of a GCE compute instance. If there are multiple volumes, each snapshot will be prepended with the disk name

## [Requirements](gce_snapshot_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- apache-libcloud >= 0.19.0

## [Parameters](gce_snapshot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **credentials_file**  path | The path to the credentials file associated with the service account |
| **disks**  list / elements=string | A list of disks to create snapshots for. If none is provided, all of the volumes will have snapshots created. |
| **instance_name**  string / required | The GCE instance to snapshot |
| **project_id**  string | The GCP project ID to use |
| **service_account_email**  string | GCP service account email for the project where the instance resides |
| **snapshot_name**  string / required | The name of the snapshot to manage |
| **state**  string | Whether a snapshot should be `present` or `absent`  Choices:   - `"present"` ← (default) - `"absent"` |

## [Examples](gce_snapshot_module.md#id4)

```yaml+jinja
- name: Create gce snapshot
  community.google.gce_snapshot:
    instance_name: example-instance
    snapshot_name: example-snapshot
    state: present
    service_account_email: project_name@appspot.gserviceaccount.com
    credentials_file: /path/to/credentials
    project_id: project_name
  delegate_to: localhost

- name: Delete gce snapshot
  community.google.gce_snapshot:
    instance_name: example-instance
    snapshot_name: example-snapshot
    state: absent
    service_account_email: project_name@appspot.gserviceaccount.com
    credentials_file: /path/to/credentials
    project_id: project_name
  delegate_to: localhost

# This example creates snapshots for only two of the available disks as
# disk0-example-snapshot and disk1-example-snapshot
- name: Create snapshots of specific disks
  community.google.gce_snapshot:
    instance_name: example-instance
    snapshot_name: example-snapshot
    state: present
    disks:
      - disk0
      - disk1
    service_account_email: project_name@appspot.gserviceaccount.com
    credentials_file: /path/to/credentials
    project_id: project_name
  delegate_to: localhost
```

## [Return Values](gce_snapshot_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **snapshots_absent**  list / elements=string | List of snapshots that were already absent (no-op)  Returned: When snapshots were already absent  Sample: `["[disk0-example-snapshot", " disk1-example-snapshot]"]` |
| **snapshots_created**  list / elements=string | List of newly created snapshots  Returned: When snapshots are created  Sample: `["[disk0-example-snapshot", " disk1-example-snapshot]"]` |
| **snapshots_deleted**  list / elements=string | List of destroyed snapshots  Returned: When snapshots are deleted  Sample: `["[disk0-example-snapshot", " disk1-example-snapshot]"]` |
| **snapshots_existing**  list / elements=string | List of snapshots that already existed (no-op)  Returned: When snapshots were already present  Sample: `["[disk0-example-snapshot", " disk1-example-snapshot]"]` |

### Authors

- Rob Wagner (@robwagner33)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.google/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.google)
