---
collection: ansible
version: "6"
title: "google.cloud.gcp_compute_node_template module – Creates a GCP NodeTemplate"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_compute_node_template_module.html
fetched_at: 2026-07-27T17:48:17+00:00
---
# google.cloud.gcp_compute_node_template module – Creates a GCP NodeTemplate

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
> see [Requirements](gcp_compute_node_template_module.md#ansible-collections-google-cloud-gcp-compute-node-template-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_node_template`.

- [Synopsis](gcp_compute_node_template_module.md#synopsis)
- [Requirements](gcp_compute_node_template_module.md#requirements)
- [Parameters](gcp_compute_node_template_module.md#parameters)
- [Notes](gcp_compute_node_template_module.md#notes)
- [Examples](gcp_compute_node_template_module.md#examples)
- [Return Values](gcp_compute_node_template_module.md#return-values)

## [Synopsis](gcp_compute_node_template_module.md#id1)

- Represents a NodeTemplate resource. Node templates specify properties for creating sole-tenant nodes, such as node type, vCPU and memory requirements, node affinity labels, and region.

## [Requirements](gcp_compute_node_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_node_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **description**  string | An optional textual description of the resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **name**  string | Name of the resource. |
| **node_affinity_labels**  dictionary | Labels to use for node affinity, which will be used in instance scheduling. |
| **node_type**  string | Node type to use for nodes group that are created from this template.  Only one of nodeTypeFlexibility and nodeType can be specified. |
| **node_type_flexibility**  dictionary | Flexible properties for the desired node type. Node groups that use this node template will create nodes of a type that matches these properties. Only one of nodeTypeFlexibility and nodeType can be specified. |
| **cpus**  string | Number of virtual CPUs to use. |
| **memory**  string | Physical memory available to the node, defined in MB. |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string / required | Region where nodes using the node template will be created . |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](gcp_compute_node_template_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/rest/v1/nodeTemplates>
> - Sole-Tenant Nodes: <https://cloud.google.com/compute/docs/nodes/>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_node_template_module.md#id5)

```yaml+jinja
- name: create a node template
  google.cloud.gcp_compute_node_template:
    name: test_object
    region: us-central1
    node_type: n1-node-96-624
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_node_template_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
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
