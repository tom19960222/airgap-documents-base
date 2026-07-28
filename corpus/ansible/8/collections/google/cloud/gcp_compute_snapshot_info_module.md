---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_snapshot_info module – Gather info for GCP Snapshot"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_snapshot_info_module.html
fetched_at: 2026-07-28T02:32:45+00:00
---
# google.cloud.gcp_compute_snapshot_info module – Gather info for GCP Snapshot

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
> see [Requirements](gcp_compute_snapshot_info_module.md#ansible-collections-google-cloud-gcp-compute-snapshot-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_snapshot_info`.

- [Synopsis](gcp_compute_snapshot_info_module.md#synopsis)
- [Requirements](gcp_compute_snapshot_info_module.md#requirements)
- [Parameters](gcp_compute_snapshot_info_module.md#parameters)
- [Notes](gcp_compute_snapshot_info_module.md#notes)
- [Examples](gcp_compute_snapshot_info_module.md#examples)
- [Return Values](gcp_compute_snapshot_info_module.md#return-values)

## [Synopsis](gcp_compute_snapshot_info_module.md#id1)

- Gather info for GCP Snapshot

## [Requirements](gcp_compute_snapshot_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_snapshot_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **filters**  list / elements=string | A list of filter value pairs. Available filters are listed here <https://cloud.google.com/sdk/gcloud/reference/topic/filters>.  Each additional filter in the list will act be added as an AND condition (filter1 and filter2) . |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |

## [Notes](gcp_compute_snapshot_info_module.md#id4)

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

## [Examples](gcp_compute_snapshot_info_module.md#id5)

```yaml+jinja
- name: get info on a snapshot
  gcp_compute_snapshot_info:
    filters:
    - name = test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_compute_snapshot_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  **Returned:** always |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **description**  string | An optional description of this resource.  **Returned:** success |
| **diskSizeGb**  integer | Size of the snapshot, specified in GB.  **Returned:** success |
| **id**  integer | The unique identifier for the resource.  **Returned:** success |
| **labelFingerprint**  string | The fingerprint used for optimistic locking of this resource. Used internally during updates.  **Returned:** success |
| **labels**  dictionary | Labels to apply to this Snapshot.  **Returned:** success |
| **licenses**  list / elements=string | A list of public visible licenses that apply to this snapshot. This can be because the original image had licenses attached (such as a Windows image). snapshotEncryptionKey nested object Encrypts the snapshot using a customer-supplied encryption key.  **Returned:** success |
| **name**  string | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **snapshotEncryptionKey**  complex | The customer-supplied encryption key of the snapshot. Required if the source snapshot is protected by a customer-supplied encryption key.  **Returned:** success |
| **kmsKeyName**  string | The name of the encryption key that is stored in Google Cloud KMS.  **Returned:** success |
| **kmsKeyServiceAccount**  string | The service account used for the encryption request for the given KMS key.  If absent, the Compute Engine Service Agent service account is used.  **Returned:** success |
| **rawKey**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.  **Returned:** success |
| **sha256**  string | The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.  **Returned:** success |
| **sourceDisk**  dictionary | A reference to the disk used to create this snapshot.  **Returned:** success |
| **sourceDiskEncryptionKey**  complex | The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a customer-supplied encryption key.  **Returned:** success |
| **kmsKeyName**  string | The name of the encryption key that is stored in Google Cloud KMS.  **Returned:** success |
| **kmsKeyServiceAccount**  string | The service account used for the encryption request for the given KMS key.  If absent, the Compute Engine Service Agent service account is used.  **Returned:** success |
| **rawKey**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.  **Returned:** success |
| **storageBytes**  integer | A size of the storage used by the snapshot. As snapshots share storage, this number is expected to change with snapshot creation/deletion.  **Returned:** success |
| **storageLocations**  list / elements=string | Cloud Storage bucket storage location of the snapshot (regional or multi-regional).  **Returned:** success |
| **zone**  string | A reference to the zone where the disk is hosted.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
