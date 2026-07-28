---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_disk module – Creates a GCP Disk"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_disk_module.html
fetched_at: 2026-07-28T02:31:57+00:00
---
# google.cloud.gcp_compute_disk module – Creates a GCP Disk

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
> see [Requirements](gcp_compute_disk_module.md#ansible-collections-google-cloud-gcp-compute-disk-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_disk`.

- [Synopsis](gcp_compute_disk_module.md#synopsis)
- [Requirements](gcp_compute_disk_module.md#requirements)
- [Parameters](gcp_compute_disk_module.md#parameters)
- [Notes](gcp_compute_disk_module.md#notes)
- [Examples](gcp_compute_disk_module.md#examples)
- [Return Values](gcp_compute_disk_module.md#return-values)

## [Synopsis](gcp_compute_disk_module.md#id1)

- Persistent disks are durable storage devices that function similarly to the physical disks in a desktop or a server. Compute Engine manages the hardware behind these devices to ensure data redundancy and optimize performance for you. Persistent disks are available as either standard hard disk drives (HDD) or solid-state drives (SSD).
- Persistent disks are located independently from your virtual machine instances, so you can detach or move persistent disks to keep your data even after you delete your instances. Persistent disk performance scales automatically with size, so you can resize your existing persistent disks or add more persistent disks to an instance to meet your performance and storage space requirements.
- Add a persistent disk to your instance when you need reliable and affordable storage with consistent performance characteristics.

## [Requirements](gcp_compute_disk_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_disk_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **description**  string | An optional description of this resource. Provide this property when you create the resource. |
| **disk_encryption_key**  dictionary | Encrypts the disk using a customer-supplied encryption key.  After you encrypt a disk with a customer-supplied key, you must provide the same key if you use the disk later (e.g. to create a disk snapshot or an image, or to attach the disk to a virtual machine).  Customer-supplied encryption keys do not protect access to metadata of the disk.  If you do not provide an encryption key when creating the disk, then the disk will be encrypted using an automatically generated key and you do not need to provide a key to use the disk later. |
| **kms_key_name**  string | The name of the encryption key that is stored in Google Cloud KMS.  Your project’s Compute Engine System service account ([`service-{{PROJECT_NUMBER}}@compute-system.iam.gserviceaccount.com](mailto:`service-{{PROJECT_NUMBER}}%40compute-system.iam.gserviceaccount.com)`) must have `roles/cloudkms.cryptoKeyEncrypterDecrypter` to use this feature. |
| **kms_key_service_account**  string | The service account used for the encryption request for the given KMS key.  If absent, the Compute Engine Service Agent service account is used. |
| **raw_key**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **labels**  dictionary | Labels to apply to this disk. A list of key->value pairs. |
| **licenses**  list / elements=string | Any applicable publicly visible licenses. |
| **name**  string / required | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **physical_block_size_bytes**  integer | Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. Currently supported sizes are 4096 and 16384, other sizes may be added in the future.  If an unsupported value is requested, the error message will list the supported values for the caller’s project. |
| **project**  string | The Google Cloud Platform project to use. |
| **provisioned_iops**  integer | Indicates how many IOPS must be provisioned for the disk. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **size_gb**  integer | Size of the persistent disk, specified in GB. You can specify this field when creating a persistent disk using the sourceImage or sourceSnapshot parameter, or specify it alone to create an empty persistent disk.  If you specify this field along with sourceImage or sourceSnapshot, the value of sizeGb must not be less than the size of the sourceImage or the size of the snapshot. |
| **source_image**  string | The source image used to create this disk. If the source image is deleted, this field will not be set.  To create a disk with one of the public operating system images, specify the image by its family name. For example, specify family/debian-9 to use the latest Debian 9 image: projects/debian-cloud/global/images/family/debian-9 Alternatively, use a specific version of a public operating system image: projects/debian-cloud/global/images/debian-9-stretch-vYYYYMMDD To create a disk with a private image that you created, specify the image name in the following format: global/images/my-private-image You can also specify a private image by its image family, which returns the latest version of the image in that family. Replace the image name with family/family-name: global/images/family/my-private-family . |
| **source_image_encryption_key**  dictionary | The customer-supplied encryption key of the source image. Required if the source image is protected by a customer-supplied encryption key. |
| **kms_key_name**  string | The name of the encryption key that is stored in Google Cloud KMS. |
| **kms_key_service_account**  string | The service account used for the encryption request for the given KMS key.  If absent, the Compute Engine Service Agent service account is used. |
| **raw_key**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource. |
| **source_snapshot**  dictionary | The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource.  This field represents a link to a Snapshot resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_snapshot task and then set this source_snapshot field to “{{ name-of-resource }}” |
| **source_snapshot_encryption_key**  dictionary | The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a customer-supplied encryption key. |
| **kms_key_name**  string | The name of the encryption key that is stored in Google Cloud KMS. |
| **kms_key_service_account**  string | The service account used for the encryption request for the given KMS key.  If absent, the Compute Engine Service Agent service account is used. |
| **raw_key**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **type**  string | URL of the disk type resource describing which disk type to use to create the disk. Provide this when creating the disk. |
| **zone**  string / required | A reference to the zone where the disk resides. |

## [Notes](gcp_compute_disk_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/v1/disks>
> - Adding a persistent disk: <https://cloud.google.com/compute/docs/disks/add-persistent-disk>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_disk_module.md#id5)

```yaml+jinja
- name: create a disk
  google.cloud.gcp_compute_disk:
    name: test_object
    size_gb: 50
    disk_encryption_key:
      raw_key: SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0=
    zone: us-central1-a
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_disk_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **description**  string | An optional description of this resource. Provide this property when you create the resource.  **Returned:** success |
| **diskEncryptionKey**  complex | Encrypts the disk using a customer-supplied encryption key.  After you encrypt a disk with a customer-supplied key, you must provide the same key if you use the disk later (e.g. to create a disk snapshot or an image, or to attach the disk to a virtual machine).  Customer-supplied encryption keys do not protect access to metadata of the disk.  If you do not provide an encryption key when creating the disk, then the disk will be encrypted using an automatically generated key and you do not need to provide a key to use the disk later.  **Returned:** success |
| **kmsKeyName**  string | The name of the encryption key that is stored in Google Cloud KMS.  Your project’s Compute Engine System service account ([`service-{{PROJECT_NUMBER}}@compute-system.iam.gserviceaccount.com](mailto:`service-{{PROJECT_NUMBER}}%40compute-system.iam.gserviceaccount.com)`) must have `roles/cloudkms.cryptoKeyEncrypterDecrypter` to use this feature.  **Returned:** success |
| **kmsKeyServiceAccount**  string | The service account used for the encryption request for the given KMS key.  If absent, the Compute Engine Service Agent service account is used.  **Returned:** success |
| **rawKey**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.  **Returned:** success |
| **sha256**  string | The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.  **Returned:** success |
| **id**  integer | The unique identifier for the resource.  **Returned:** success |
| **labelFingerprint**  string | The fingerprint used for optimistic locking of this resource. Used internally during updates.  **Returned:** success |
| **labels**  dictionary | Labels to apply to this disk. A list of key->value pairs.  **Returned:** success |
| **lastAttachTimestamp**  string | Last attach timestamp in RFC3339 text format.  **Returned:** success |
| **lastDetachTimestamp**  string | Last detach timestamp in RFC3339 text format.  **Returned:** success |
| **licenses**  list / elements=string | Any applicable publicly visible licenses.  **Returned:** success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **physicalBlockSizeBytes**  integer | Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. Currently supported sizes are 4096 and 16384, other sizes may be added in the future.  If an unsupported value is requested, the error message will list the supported values for the caller’s project.  **Returned:** success |
| **provisionedIops**  integer | Indicates how many IOPS must be provisioned for the disk.  **Returned:** success |
| **sizeGb**  integer | Size of the persistent disk, specified in GB. You can specify this field when creating a persistent disk using the sourceImage or sourceSnapshot parameter, or specify it alone to create an empty persistent disk.  If you specify this field along with sourceImage or sourceSnapshot, the value of sizeGb must not be less than the size of the sourceImage or the size of the snapshot.  **Returned:** success |
| **sourceImage**  string | The source image used to create this disk. If the source image is deleted, this field will not be set.  To create a disk with one of the public operating system images, specify the image by its family name. For example, specify family/debian-9 to use the latest Debian 9 image: projects/debian-cloud/global/images/family/debian-9 Alternatively, use a specific version of a public operating system image: projects/debian-cloud/global/images/debian-9-stretch-vYYYYMMDD To create a disk with a private image that you created, specify the image name in the following format: global/images/my-private-image You can also specify a private image by its image family, which returns the latest version of the image in that family. Replace the image name with family/family-name: global/images/family/my-private-family .  **Returned:** success |
| **sourceImageEncryptionKey**  complex | The customer-supplied encryption key of the source image. Required if the source image is protected by a customer-supplied encryption key.  **Returned:** success |
| **kmsKeyName**  string | The name of the encryption key that is stored in Google Cloud KMS.  **Returned:** success |
| **kmsKeyServiceAccount**  string | The service account used for the encryption request for the given KMS key.  If absent, the Compute Engine Service Agent service account is used.  **Returned:** success |
| **rawKey**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.  **Returned:** success |
| **sha256**  string | The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.  **Returned:** success |
| **sourceImageId**  string | The ID value of the image used to create this disk. This value identifies the exact image that was used to create this persistent disk. For example, if you created the persistent disk from an image that was later deleted and recreated under the same name, the source image ID would identify the exact version of the image that was used.  **Returned:** success |
| **sourceSnapshot**  dictionary | The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource.  **Returned:** success |
| **sourceSnapshotEncryptionKey**  complex | The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a customer-supplied encryption key.  **Returned:** success |
| **kmsKeyName**  string | The name of the encryption key that is stored in Google Cloud KMS.  **Returned:** success |
| **kmsKeyServiceAccount**  string | The service account used for the encryption request for the given KMS key.  If absent, the Compute Engine Service Agent service account is used.  **Returned:** success |
| **rawKey**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.  **Returned:** success |
| **sha256**  string | The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.  **Returned:** success |
| **sourceSnapshotId**  string | The unique ID of the snapshot used to create this disk. This value identifies the exact snapshot that was used to create this persistent disk. For example, if you created the persistent disk from a snapshot that was later deleted and recreated under the same name, the source snapshot ID would identify the exact version of the snapshot that was used.  **Returned:** success |
| **type**  string | URL of the disk type resource describing which disk type to use to create the disk. Provide this when creating the disk.  **Returned:** success |
| **users**  list / elements=string | Links to the users of the disk (attached instances) in form: project/zones/zone/instances/instance .  **Returned:** success |
| **zone**  string | A reference to the zone where the disk resides.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
