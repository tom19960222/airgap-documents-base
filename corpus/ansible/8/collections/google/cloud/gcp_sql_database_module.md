---
collection: ansible
version: "8"
title: "google.cloud.gcp_sql_database module – Creates a GCP Database"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_sql_database_module.html
fetched_at: 2026-07-28T02:33:36+00:00
---
# google.cloud.gcp_sql_database module – Creates a GCP Database

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
> see [Requirements](gcp_sql_database_module.md#ansible-collections-google-cloud-gcp-sql-database-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_sql_database`.

- [Synopsis](gcp_sql_database_module.md#synopsis)
- [Requirements](gcp_sql_database_module.md#requirements)
- [Parameters](gcp_sql_database_module.md#parameters)
- [Examples](gcp_sql_database_module.md#examples)
- [Return Values](gcp_sql_database_module.md#return-values)

## [Synopsis](gcp_sql_database_module.md#id1)

- Represents a SQL database inside the Cloud SQL instance, hosted in Google’s cloud.

## [Requirements](gcp_sql_database_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_sql_database_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **charset**  string | The charset value. See MySQL’s [Supported Character Sets and Collations](<https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html>) and Postgres’ [Character Set Support](<https://www.postgresql.org/docs/9.6/static/multibyte.html>) for more details and supported values. Postgres databases only support a value of `UTF8` at creation time. |
| **collation**  string | The collation value. See MySQL’s [Supported Character Sets and Collations](<https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html>) and Postgres’ [Collation Support](<https://www.postgresql.org/docs/9.6/static/collation.html>) for more details and supported values. Postgres databases only support a value of `en_US.UTF8` at creation time. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **instance**  string / required | The name of the Cloud SQL instance. This does not include the project ID. |
| **name**  string / required | The name of the database in the Cloud SQL instance.  This does not include the project ID or instance name. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Examples](gcp_sql_database_module.md#id4)

```yaml+jinja
- name: create a instance
  google.cloud.gcp_sql_instance:
    name: "{{resource_name}}-3"
    settings:
      ip_configuration:
        authorized_networks:
        - name: google dns server
          value: 8.8.8.8/32
      tier: db-n1-standard-1
    region: us-central1
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: instance

- name: create a database
  google.cloud.gcp_sql_database:
    name: test_object
    charset: utf8
    instance: "{{ instance.name }}"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_sql_database_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **charset**  string | The charset value. See MySQL’s [Supported Character Sets and Collations](<https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html>) and Postgres’ [Character Set Support](<https://www.postgresql.org/docs/9.6/static/multibyte.html>) for more details and supported values. Postgres databases only support a value of `UTF8` at creation time.  **Returned:** success |
| **collation**  string | The collation value. See MySQL’s [Supported Character Sets and Collations](<https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html>) and Postgres’ [Collation Support](<https://www.postgresql.org/docs/9.6/static/collation.html>) for more details and supported values. Postgres databases only support a value of `en_US.UTF8` at creation time.  **Returned:** success |
| **instance**  string | The name of the Cloud SQL instance. This does not include the project ID.  **Returned:** success |
| **name**  string | The name of the database in the Cloud SQL instance.  This does not include the project ID or instance name.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
