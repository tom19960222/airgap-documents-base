---
collection: ansible
version: "6"
title: "google.cloud.gcp_compute_node_template_info module – Gather info for GCP NodeTemplate"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_compute_node_template_info_module.html
fetched_at: 2026-07-27T17:48:18+00:00
---
# google.cloud.gcp_compute_node_template_info module – Gather info for GCP NodeTemplate

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/google/cloud) (version 1.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_compute_node_template_info_module.md#ansible-collections-google-cloud-gcp-compute-node-template-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_node_template_info`.

- [Synopsis](gcp_compute_node_template_info_module.md#synopsis)
- [Requirements](gcp_compute_node_template_info_module.md#requirements)
- [Parameters](gcp_compute_node_template_info_module.md#parameters)
- [Notes](gcp_compute_node_template_info_module.md#notes)
- [Examples](gcp_compute_node_template_info_module.md#examples)
- [Return Values](gcp_compute_node_template_info_module.md#return-values)

## [Synopsis](gcp_compute_node_template_info_module.md#id1)

- Gather info for GCP NodeTemplate

## [Requirements](gcp_compute_node_template_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_node_template_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **filters**  list / elements=string | A list of filter value pairs. Available filters are listed here <https://cloud.google.com/sdk/gcloud/reference/topic/filters>.  Each additional filter in the list will act be added as an AND condition (filter1 and filter2) . |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string / required | Region where nodes using the node template will be created . |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |

## [Notes](gcp_compute_node_template_info_module.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_node_template_info_module.md#id5)

```yaml+jinja
- name: get info on a node template
  gcp_compute_node_template_info:
    region: us-central1
    filters:
    - name = test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_compute_node_template_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  Returned: always |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  Returned: success |
| **description**  string | An optional textual description of the resource.  Returned: success |
| **name**  string | Name of the resource.  Returned: success |
| **nodeAffinityLabels**  dictionary | Labels to use for node affinity, which will be used in instance scheduling.  Returned: success |
| **nodeType**  string | Node type to use for nodes group that are created from this template.  Only one of nodeTypeFlexibility and nodeType can be specified.  Returned: success |
| **nodeTypeFlexibility**  complex | Flexible properties for the desired node type. Node groups that use this node template will create nodes of a type that matches these properties. Only one of nodeTypeFlexibility and nodeType can be specified.  Returned: success |
| **cpus**  string | Number of virtual CPUs to use.  Returned: success |
| **localSsd**  string | Use local SSD .  Returned: success |
| **memory**  string | Physical memory available to the node, defined in MB.  Returned: success |
| **region**  string | Region where nodes using the node template will be created .  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
