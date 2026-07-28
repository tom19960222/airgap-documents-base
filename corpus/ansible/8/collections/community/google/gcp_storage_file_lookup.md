---
collection: ansible
version: "8"
title: "community.google.gcp_storage_file lookup – Return GC Storage content"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/google/gcp_storage_file_lookup.html
fetched_at: 2026-07-28T01:53:12+00:00
---
# community.google.gcp_storage_file lookup – Return GC Storage content

> **Note:**
>
> This lookup plugin is part of the [community.google collection](https://galaxy.ansible.com/ui/repo/published/community/google/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.google`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](gcp_storage_file_lookup.md#ansible-collections-community-google-gcp-storage-file-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.google.gcp_storage_file`.

- [Synopsis](gcp_storage_file_lookup.md#synopsis)
- [Requirements](gcp_storage_file_lookup.md#requirements)
- [Keyword parameters](gcp_storage_file_lookup.md#keyword-parameters)
- [Notes](gcp_storage_file_lookup.md#notes)
- [Examples](gcp_storage_file_lookup.md#examples)
- [Return Value](gcp_storage_file_lookup.md#return-value)

## [Synopsis](gcp_storage_file_lookup.md#id1)

- This lookup returns the contents from a file residing on Google Cloud Storage

## [Requirements](gcp_storage_file_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Keyword parameters](gcp_storage_file_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.google.gcp_storage_file', key1=value1, key2=value2, ...)` and `query('community.google.gcp_storage_file', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **bucket**  string | The name of the bucket. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used. |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **src**  string | Source location of file (may be local machine or cloud depending on action). |

## [Notes](gcp_storage_file_lookup.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the c(gcp_service_account_file) env variable.
> - for authentication, you can set service_account_contents using the c(GCP_SERVICE_ACCOUNT_CONTENTS) env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_storage_file_lookup.md#id5)

```yaml+jinja
- ansible.builtin.debug:
    msg: |
         the value of foo.txt is {{ lookup('community.google.gcp_storage_file',
         bucket='gcp-bucket', src='mydir/foo.txt', project='project-name',
         auth_kind='serviceaccount', service_account_file='/tmp/myserviceaccountfile.json') }}
```

## [Return Value](gcp_storage_file_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | base64 encoded file content  **Returned:** success |

### Authors

- Eric Anderson

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.google/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.google)
