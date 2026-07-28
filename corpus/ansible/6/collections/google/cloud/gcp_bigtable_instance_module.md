---
collection: ansible
version: "6"
title: "google.cloud.gcp_bigtable_instance module – Creates a GCP Instance"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_bigtable_instance_module.html
fetched_at: 2026-07-27T17:47:38+00:00
---
# google.cloud.gcp_bigtable_instance module – Creates a GCP Instance

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
> see [Requirements](gcp_bigtable_instance_module.md#ansible-collections-google-cloud-gcp-bigtable-instance-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_bigtable_instance`.

- [Synopsis](gcp_bigtable_instance_module.md#synopsis)
- [Requirements](gcp_bigtable_instance_module.md#requirements)
- [Parameters](gcp_bigtable_instance_module.md#parameters)
- [Examples](gcp_bigtable_instance_module.md#examples)
- [Return Values](gcp_bigtable_instance_module.md#return-values)

## [Synopsis](gcp_bigtable_instance_module.md#id1)

- A collection of Bigtable Tables and the resources that serve them. All tables in an instance are served from all Clusters in the instance.

## [Requirements](gcp_bigtable_instance_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_bigtable_instance_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **clusters**  list / elements=dictionary | An array of clusters. Maximum 4. |
| **default_storage_type**  string | The type of storage used by this cluster to serve its parent instance’s tables, unless explicitly overridden.  Some valid choices include: “STORAGE_TYPE_UNSPECIFIED”, “SSD”, “HDD” |
| **location**  string | The location where this cluster’s nodes and storage reside. For best performance, clients should be located as close as possible to this cluster. Currently only zones are supported, so values should be of the form `projects/<project>/locations/<zone>`. |
| **name**  string | The unique name of the cluster. |
| **serve_nodes**  integer | The number of nodes allocated to this cluster. More nodes enable higher throughput and more consistent performance. |
| **display_name**  string | The descriptive name for this instance as it appears in UIs.  Can be changed at any time, but should be kept globally unique to avoid confusion. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **labels**  dictionary | Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer’s organizational needs and deployment strategies. They can be used to filter resources and aggregate metrics. |
| **name**  string | The unique name of the instance. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |
| **type**  string | The type of the instance. Defaults to `PRODUCTION`.  Some valid choices include: “TYPE_UNSPECIFIED”, “PRODUCTION”, “DEVELOPMENT” |

## [Examples](gcp_bigtable_instance_module.md#id4)

```yaml+jinja
- name: create a instance
  google.cloud.gcp_bigtable_instance:
    name: my-instance
    display_name: My Test Cluster
    clusters:
    - name: mycluster
      location: projects/test_project/locations/us-central1-a
      serve_nodes: 1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_bigtable_instance_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **clusters**  complex | An array of clusters. Maximum 4.  Returned: success |
| **defaultStorageType**  string | The type of storage used by this cluster to serve its parent instance’s tables, unless explicitly overridden.  Returned: success |
| **location**  string | The location where this cluster’s nodes and storage reside. For best performance, clients should be located as close as possible to this cluster. Currently only zones are supported, so values should be of the form `projects/<project>/locations/<zone>`.  Returned: success |
| **name**  string | The unique name of the cluster.  Returned: success |
| **serveNodes**  integer | The number of nodes allocated to this cluster. More nodes enable higher throughput and more consistent performance.  Returned: success |
| **state**  string | The current state of the cluster.  Returned: success |
| **displayName**  string | The descriptive name for this instance as it appears in UIs.  Can be changed at any time, but should be kept globally unique to avoid confusion.  Returned: success |
| **labels**  dictionary | Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer’s organizational needs and deployment strategies. They can be used to filter resources and aggregate metrics.  Returned: success |
| **name**  string | The unique name of the instance.  Returned: success |
| **state**  string | The current state of the instance.  Returned: success |
| **type**  string | The type of the instance. Defaults to `PRODUCTION`.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
