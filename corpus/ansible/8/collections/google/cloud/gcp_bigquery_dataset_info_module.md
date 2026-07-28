---
collection: ansible
version: "8"
title: "google.cloud.gcp_bigquery_dataset_info module – Gather info for GCP Dataset"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_bigquery_dataset_info_module.html
fetched_at: 2026-07-28T02:31:42+00:00
---
# google.cloud.gcp_bigquery_dataset_info module – Gather info for GCP Dataset

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/ui/repo/published/google/cloud/) (version 1.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_bigquery_dataset_info_module.md#ansible-collections-google-cloud-gcp-bigquery-dataset-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_bigquery_dataset_info`.

- [Synopsis](gcp_bigquery_dataset_info_module.md#synopsis)
- [Requirements](gcp_bigquery_dataset_info_module.md#requirements)
- [Parameters](gcp_bigquery_dataset_info_module.md#parameters)
- [Notes](gcp_bigquery_dataset_info_module.md#notes)
- [Examples](gcp_bigquery_dataset_info_module.md#examples)
- [Return Values](gcp_bigquery_dataset_info_module.md#return-values)

## [Synopsis](gcp_bigquery_dataset_info_module.md#id1)

- Gather info for GCP Dataset

## [Requirements](gcp_bigquery_dataset_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_bigquery_dataset_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |

## [Notes](gcp_bigquery_dataset_info_module.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_bigquery_dataset_info_module.md#id5)

```yaml+jinja
- name: get info on a dataset
  gcp_bigquery_dataset_info:
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_bigquery_dataset_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  **Returned:** always |
| **access**  complex | An array of objects that define dataset access for one or more entities.  **Returned:** success |
| **domain**  string | A domain to grant access to. Any users signed in with the domain specified will be granted the specified access .  **Returned:** success |
| **groupByEmail**  string | An email address of a Google Group to grant access to.  **Returned:** success |
| **role**  string | Describes the rights granted to the user specified by the other member of the access object. Basic, predefined, and custom roles are supported. Predefined roles that have equivalent basic roles are swapped by the API to their basic counterparts. See [official docs](<https://cloud.google.com/bigquery/docs/access-control>).  **Returned:** success |
| **specialGroup**  string | A special group to grant access to. Possible values include: \* `projectOwners`: Owners of the enclosing project.  \* `projectReaders`: Readers of the enclosing project.  \* `projectWriters`: Writers of the enclosing project.  \* `allAuthenticatedUsers`: All authenticated BigQuery users.  **Returned:** success |
| **userByEmail**  string | An email address of a user to grant access to. For example: [fred@example.com](mailto:fred%40example.com) .  **Returned:** success |
| **view**  complex | A view from a different dataset to grant access to. Queries executed against that view will have read access to tables in this dataset. The role field is not required when this field is set. If that view is updated by any user, access to the view needs to be granted again via an update operation.  **Returned:** success |
| **datasetId**  string | The ID of the dataset containing this table.  **Returned:** success |
| **projectId**  string | The ID of the project containing this table.  **Returned:** success |
| **tableId**  string | The ID of the table. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores. The maximum length is 1,024 characters.  **Returned:** success |
| **creationTime**  integer | The time when this dataset was created, in milliseconds since the epoch.  **Returned:** success |
| **datasetReference**  complex | A reference that identifies the dataset.  **Returned:** success |
| **datasetId**  string | A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores. The maximum length is 1,024 characters.  **Returned:** success |
| **projectId**  string | The ID of the project containing this dataset.  **Returned:** success |
| **defaultEncryptionConfiguration**  complex | The default encryption key for all tables in the dataset. Once this property is set, all newly-created partitioned tables in the dataset will have encryption key set to this value, unless table creation request (or query) overrides the key.  **Returned:** success |
| **kmsKeyName**  string | Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table. The BigQuery Service Account associated with your project requires access to this encryption key.  **Returned:** success |
| **defaultPartitionExpirationMs**  integer | The default partition expiration for all partitioned tables in the dataset, in milliseconds.  Once this property is set, all newly-created partitioned tables in the dataset will have an `expirationMs` property in the `timePartitioning` settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a partition will have an expiration time of its partition time plus this value.  Setting this property overrides the use of `defaultTableExpirationMs` for partitioned tables: only one of `defaultTableExpirationMs` and `defaultPartitionExpirationMs` will be used for any new partitioned table. If you provide an explicit `timePartitioning.expirationMs` when creating or updating a partitioned table, that value takes precedence over the default partition expiration time indicated by this property.  **Returned:** success |
| **defaultTableExpirationMs**  integer | The default lifetime of all tables in the dataset, in milliseconds.  The minimum value is 3600000 milliseconds (one hour).  Once this property is set, all newly-created tables in the dataset will have an `expirationTime` property set to the creation time plus the value in this property, and changing the value will only affect new tables, not existing ones. When the `expirationTime` for a given table is reached, that table will be deleted automatically.  If a table’s `expirationTime` is modified or removed before the table expires, or if you provide an explicit `expirationTime` when creating a table, that value takes precedence over the default expiration time indicated by this property.  **Returned:** success |
| **description**  string | A user-friendly description of the dataset.  **Returned:** success |
| **etag**  string | A hash of the resource.  **Returned:** success |
| **friendlyName**  string | A descriptive name for the dataset.  **Returned:** success |
| **id**  string | The fully-qualified unique name of the dataset in the format projectId:datasetId. The dataset name without the project name is given in the datasetId field .  **Returned:** success |
| **labels**  dictionary | The labels associated with this dataset. You can use these to organize and group your datasets .  **Returned:** success |
| **lastModifiedTime**  integer | The date when this dataset or any of its tables was last modified, in milliseconds since the epoch.  **Returned:** success |
| **location**  string | The geographic location where the dataset should reside.  See [official docs](<https://cloud.google.com/bigquery/docs/dataset-locations>).  There are two types of locations, regional or multi-regional. A regional location is a specific geographic place, such as Tokyo, and a multi-regional location is a large geographic area, such as the United States, that contains at least two geographic places.  The default value is multi-regional location `US`.  Changing this forces a new resource to be created.  **Returned:** success |
| **name**  string | Dataset name.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
