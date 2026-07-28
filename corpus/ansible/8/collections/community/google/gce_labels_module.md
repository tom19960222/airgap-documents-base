---
collection: ansible
version: "8"
title: "community.google.gce_labels module – Create, Update or Destroy GCE Labels."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/google/gce_labels_module.html
fetched_at: 2026-07-28T01:53:05+00:00
---
# community.google.gce_labels module – Create, Update or Destroy GCE Labels.

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
> see [Requirements](gce_labels_module.md#ansible-collections-community-google-gce-labels-module-requirements) for details.
>
> To use it in a playbook, specify: `community.google.gce_labels`.

- [Synopsis](gce_labels_module.md#synopsis)
- [Requirements](gce_labels_module.md#requirements)
- [Parameters](gce_labels_module.md#parameters)
- [Notes](gce_labels_module.md#notes)
- [Examples](gce_labels_module.md#examples)
- [Return Values](gce_labels_module.md#return-values)

## [Synopsis](gce_labels_module.md#id1)

- Create, Update or Destroy GCE Labels on instances, disks, snapshots, etc. When specifying the GCE resource, users may specify the full URL for the resource (its ‘self_link’), or the individual parameters of the resource (type, location, name). Examples for the two options can be seen in the documentation. See <https://cloud.google.com/compute/docs/label-or-tag-resources> for more information about GCE Labels. Labels are gradually being added to more GCE resources, so this module will need to be updated as new resources are added to the GCE (v1) API.

## [Requirements](gce_labels_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- google-api-python-client >= 1.6.2
- google-auth >= 1.0.0
- google-auth-httplib2 >= 0.0.2

## [Parameters](gce_labels_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **credentials_file**  string | The path to the JSON file associated with the service account email. |
| **labels**  dictionary | A list of labels (key/value pairs) to add or remove for the resource. |
| **pem_file**  string | The path to the PEM file associated with the service account email.  This option is deprecated and may be removed in a future release. Use *credentials_file* instead. |
| **project_id**  string | The Google Cloud Platform project ID to use. |
| **resource_location**  string | The location of resource (global, us-central1-f, etc.) |
| **resource_name**  string | The name of resource. |
| **resource_type**  string | The type of resource (instances, disks, snapshots, images) |
| **resource_url**  string | The ‘self_link’ for the resource (instance, disk, snapshot, etc) |
| **service_account_email**  string | service account email |
| **service_account_permissions**  list / elements=string | service account email |
| **state**  string | The state the labels should be in. `present` or `absent` are the only valid options.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](gce_labels_module.md#id4)

> **Note:**
>
> - Labels support resources such as instances, disks, images, etc. See <https://cloud.google.com/compute/docs/labeling-resources> for the list of resources available in the GCE v1 API (not alpha or beta).

## [Examples](gce_labels_module.md#id5)

```yaml+jinja
- name: Add labels on an existing instance (using resource_url)
  community.google.gce_labels:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    labels:
      webserver-frontend: homepage
      environment: test
      experiment-name: kennedy
    resource_url: https://www.googleapis.com/compute/beta/projects/myproject/zones/us-central1-f/instances/example-instance
    state: present
- name: Add labels on an image (using resource params)
  community.google.gce_labels:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    labels:
      webserver-frontend: homepage
      environment: test
      experiment-name: kennedy
    resource_type: images
    resource_location: global
    resource_name: my-custom-image
    state: present
- name: Remove specified labels from the GCE instance
  community.google.gce_labels:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    labels:
      environment: prod
      experiment-name: kennedy
    resource_url: https://www.googleapis.com/compute/beta/projects/myproject/zones/us-central1-f/instances/example-instance
    state: absent
```

## [Return Values](gce_labels_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **labels**  dictionary | List of labels that exist on the resource.  **Returned:** Always.  **Sample:** `[{"environment": "test", "environment-name": "kennedy", "webserver-frontend": "homepage"}]` |
| **resource_location**  string | The location of the GCE resource.  **Returned:** Always.  **Sample:** `"us-central1-f"` |
| **resource_name**  string | The name of the GCE resource.  **Returned:** Always.  **Sample:** `"my-happy-little-instance"` |
| **resource_type**  string | The type of the GCE resource.  **Returned:** Always.  **Sample:** `"instances"` |
| **resource_url**  string | The ‘self_link’ of the GCE resource.  **Returned:** Always.  **Sample:** `"https://www.googleapis.com/compute/beta/projects/myproject/zones/us-central1-f/instances/example-instance"` |
| **state**  string | state of the labels  **Returned:** Always.  **Sample:** `"present"` |

### Authors

- Eric Johnson (@erjohnso)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.google/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.google)
