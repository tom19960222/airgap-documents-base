---
collection: ansible
version: "6"
title: "google.cloud.gcp_bigquery_table_info module – Gather info for GCP Table"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_bigquery_table_info_module.html
fetched_at: 2026-07-27T17:47:37+00:00
---
# google.cloud.gcp_bigquery_table_info module – Gather info for GCP Table

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
> see [Requirements](gcp_bigquery_table_info_module.md#ansible-collections-google-cloud-gcp-bigquery-table-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_bigquery_table_info`.

- [Synopsis](gcp_bigquery_table_info_module.md#synopsis)
- [Requirements](gcp_bigquery_table_info_module.md#requirements)
- [Parameters](gcp_bigquery_table_info_module.md#parameters)
- [Notes](gcp_bigquery_table_info_module.md#notes)
- [Examples](gcp_bigquery_table_info_module.md#examples)
- [Return Values](gcp_bigquery_table_info_module.md#return-values)

## [Synopsis](gcp_bigquery_table_info_module.md#id1)

- Gather info for GCP Table

## [Requirements](gcp_bigquery_table_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_bigquery_table_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **dataset**  string | Name of the dataset. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |

## [Notes](gcp_bigquery_table_info_module.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_bigquery_table_info_module.md#id5)

```yaml+jinja
- name: get info on a table
  gcp_bigquery_table_info:
    dataset: example_dataset
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_bigquery_table_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  Returned: always |
| **clustering**  list / elements=string | One or more fields on which data should be clustered. Only top-level, non-repeated, simple-type fields are supported. When you cluster a table using multiple columns, the order of columns you specify is important. The order of the specified columns determines the sort order of the data.  Returned: success |
| **creationTime**  integer | The time when this dataset was created, in milliseconds since the epoch.  Returned: success |
| **dataset**  string | Name of the dataset.  Returned: success |
| **description**  string | A user-friendly description of the dataset.  Returned: success |
| **encryptionConfiguration**  complex | Custom encryption configuration.  Returned: success |
| **kmsKeyName**  string | Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table. The BigQuery Service Account associated with your project requires access to this encryption key.  Returned: success |
| **expirationTime**  integer | The time when this table expires, in milliseconds since the epoch. If not present, the table will persist indefinitely.  Returned: success |
| **externalDataConfiguration**  complex | Describes the data format, location, and other properties of a table stored outside of BigQuery. By defining these properties, the data source can then be queried as if it were a standard BigQuery table.  Returned: success |
| **autodetect**  boolean | Try to detect schema and format options automatically. Any option specified explicitly will be honored.  Returned: success |
| **bigtableOptions**  complex | Additional options if sourceFormat is set to BIGTABLE.  Returned: success |
| **columnFamilies**  complex | List of column families to expose in the table schema along with their types.  Returned: success |
| **columns**  complex | Lists of columns that should be exposed as individual fields as opposed to a list of (column name, value) pairs.  Returned: success |
| **encoding**  string | The encoding of the values when the type is not STRING.  Returned: success |
| **fieldName**  string | If the qualifier is not a valid BigQuery field identifier, a valid identifier must be provided as the column field name and is used as field name in queries.  Returned: success |
| **onlyReadLatest**  boolean | If this is set, only the latest version of value in this column are exposed .  Returned: success |
| **qualifierString**  string | Qualifier of the column.  Returned: success |
| **type**  string | The type to convert the value in cells of this column.  Returned: success |
| **encoding**  string | The encoding of the values when the type is not STRING.  Returned: success |
| **familyId**  string | Identifier of the column family.  Returned: success |
| **onlyReadLatest**  boolean | If this is set only the latest version of value are exposed for all columns in this column family .  Returned: success |
| **type**  string | The type to convert the value in cells of this column family.  Returned: success |
| **ignoreUnspecifiedColumnFamilies**  boolean | If field is true, then the column families that are not specified in columnFamilies list are not exposed in the table schema .  Returned: success |
| **readRowkeyAsString**  boolean | If field is true, then the rowkey column families will be read and converted to string.  Returned: success |
| **compression**  string | The compression type of the data source.  Returned: success |
| **csvOptions**  complex | Additional properties to set if sourceFormat is set to CSV.  Returned: success |
| **allowJaggedRows**  boolean | Indicates if BigQuery should accept rows that are missing trailing optional columns .  Returned: success |
| **allowQuotedNewlines**  boolean | Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file .  Returned: success |
| **encoding**  string | The character encoding of the data.  Returned: success |
| **fieldDelimiter**  string | The separator for fields in a CSV file.  Returned: success |
| **quote**  string | The value that is used to quote data sections in a CSV file.  Returned: success |
| **skipLeadingRows**  integer | The number of rows at the top of a CSV file that BigQuery will skip when reading the data.  Returned: success |
| **googleSheetsOptions**  complex | Additional options if sourceFormat is set to GOOGLE_SHEETS.  Returned: success |
| **skipLeadingRows**  integer | The number of rows at the top of a Google Sheet that BigQuery will skip when reading the data.  Returned: success |
| **ignoreUnknownValues**  boolean | Indicates if BigQuery should allow extra values that are not represented in the table schema .  Returned: success |
| **maxBadRecords**  integer | The maximum number of bad records that BigQuery can ignore when reading data .  Returned: success |
| **schema**  complex | The schema for the data. Schema is required for CSV and JSON formats.  Returned: success |
| **fields**  complex | Describes the fields in a table.  Returned: success |
| **description**  string | The field description.  Returned: success |
| **fields**  list / elements=string | Describes the nested schema fields if the type property is set to RECORD .  Returned: success |
| **mode**  string | Field mode.  Returned: success |
| **name**  string | Field name.  Returned: success |
| **type**  string | Field data type.  Returned: success |
| **sourceFormat**  string | The data format.  Returned: success |
| **sourceUris**  list / elements=string | The fully-qualified URIs that point to your data in Google Cloud.  For Google Cloud Storage URIs: Each URI can contain one ‘\*’ wildcard character and it must come after the ‘bucket’ name. Size limits related to load jobs apply to external data sources. For Google Cloud Bigtable URIs: Exactly one URI can be specified and it has be a fully specified and valid HTTPS URL for a Google Cloud Bigtable table. For Google Cloud Datastore backups, exactly one URI can be specified. Also, the ‘\*’ wildcard character is not allowed.  Returned: success |
| **friendlyName**  string | A descriptive name for this table.  Returned: success |
| **id**  string | An opaque ID uniquely identifying the table.  Returned: success |
| **labels**  dictionary | The labels associated with this dataset. You can use these to organize and group your datasets .  Returned: success |
| **lastModifiedTime**  integer | The time when this table was last modified, in milliseconds since the epoch.  Returned: success |
| **location**  string | The geographic location where the table resides. This value is inherited from the dataset.  Returned: success |
| **name**  string | Name of the table.  Returned: success |
| **numBytes**  integer | The size of this table in bytes, excluding any data in the streaming buffer.  Returned: success |
| **numLongTermBytes**  integer | The number of bytes in the table that are considered “long-term storage”.  Returned: success |
| **numRows**  integer | The number of rows of data in this table, excluding any data in the streaming buffer.  Returned: success |
| **requirePartitionFilter**  boolean | If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified.  Returned: success |
| **schema**  complex | Describes the schema of this table.  Returned: success |
| **fields**  complex | Describes the fields in a table.  Returned: success |
| **description**  string | The field description. The maximum length is 1,024 characters.  Returned: success |
| **fields**  list / elements=string | Describes the nested schema fields if the type property is set to RECORD.  Returned: success |
| **mode**  string | The field mode.  Returned: success |
| **name**  string | The field name.  Returned: success |
| **type**  string | The field data type.  Returned: success |
| **streamingBuffer**  complex | Contains information regarding this table’s streaming buffer, if one is present. This field will be absent if the table is not being streamed to or if there is no data in the streaming buffer.  Returned: success |
| **estimatedBytes**  integer | A lower-bound estimate of the number of bytes currently in the streaming buffer.  Returned: success |
| **estimatedRows**  integer | A lower-bound estimate of the number of rows currently in the streaming buffer.  Returned: success |
| **oldestEntryTime**  integer | Contains the timestamp of the oldest entry in the streaming buffer, in milliseconds since the epoch, if the streaming buffer is available.  Returned: success |
| **tableReference**  complex | Reference describing the ID of this table.  Returned: success |
| **datasetId**  string | The ID of the dataset containing this table.  Returned: success |
| **projectId**  string | The ID of the project containing this table.  Returned: success |
| **tableId**  string | The ID of the the table.  Returned: success |
| **timePartitioning**  complex | If specified, configures time-based partitioning for this table.  Returned: success |
| **expirationMs**  integer | Number of milliseconds for which to keep the storage for a partition.  Returned: success |
| **field**  string | If not set, the table is partitioned by pseudo column, referenced via either ‘_PARTITIONTIME’ as TIMESTAMP type, or ‘_PARTITIONDATE’ as DATE type. If field is specified, the table is instead partitioned by this field. The field must be a top-level TIMESTAMP or DATE field. Its mode must be NULLABLE or REQUIRED.  Returned: success |
| **type**  string | The only type supported is DAY, which will generate one partition per day.  Returned: success |
| **type**  string | Describes the table type.  Returned: success |
| **view**  complex | The view definition.  Returned: success |
| **useLegacySql**  boolean | Specifies whether to use BigQuery’s legacy SQL for this view .  Returned: success |
| **userDefinedFunctionResources**  complex | Describes user-defined function resources used in the query.  Returned: success |
| **inlineCode**  string | An inline resource that contains code for a user-defined function (UDF). Providing a inline code resource is equivalent to providing a URI for a file containing the same code.  Returned: success |
| **resourceUri**  string | A code resource to load from a Google Cloud Storage URI (gs://bucket/path).  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
