---
collection: ansible
version: "8"
title: "google.cloud.gcp_storage_object module – Creates a GCP Object"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_storage_object_module.html
fetched_at: 2026-07-28T02:33:44+00:00
---
# google.cloud.gcp_storage_object module – Creates a GCP Object

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
> see [Requirements](gcp_storage_object_module.md#ansible-collections-google-cloud-gcp-storage-object-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_storage_object`.

- [Synopsis](gcp_storage_object_module.md#synopsis)
- [Requirements](gcp_storage_object_module.md#requirements)
- [Parameters](gcp_storage_object_module.md#parameters)
- [Examples](gcp_storage_object_module.md#examples)
- [Return Values](gcp_storage_object_module.md#return-values)

## [Synopsis](gcp_storage_object_module.md#id1)

- Upload or download a file from a GCS bucket.

## [Requirements](gcp_storage_object_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
- google-cloud-storage >= 1.2.0

## [Parameters](gcp_storage_object_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **action**  string | The actions to be taken on this object.  You can download the object, upload the object, or delete it.  **Choices:**   - `"download"` - `"upload"` - `"delete"` |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **bucket**  string | The name of the bucket. |
| **dest**  path | Destination location of file (may be local machine or cloud depending on action). Cloud location need to be urlencoded including slashes. Required for upload and download. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **src**  path / required | Source location of file (may be local machine or cloud depending on action). Cloud locations need to be urlencoded including slashes. |

## [Examples](gcp_storage_object_module.md#id4)

```yaml+jinja
- name: Download an object
  google.cloud.gcp_storage_object:
    action: download
    bucket: ansible-bucket
    src: modules.zip
    dest: "~/modules.zip"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_storage_object_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **bucket**  string | The bucket where the object is contained.  **Returned:** download, upload |
| **cache_control**  string | HTTP ‘Cache-Control’ header for this object  **Returned:** download, upload |
| **chunk_size**  string | Get the blob’s default chunk size  **Returned:** download, upload |
| **media_link**  string | The link for the media  **Returned:** download, upload |
| **self_link**  string | The self_link for the media.  **Returned:** download, upload |
| **storage_class**  string | The storage class for the object.  **Returned:** download, upload |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
