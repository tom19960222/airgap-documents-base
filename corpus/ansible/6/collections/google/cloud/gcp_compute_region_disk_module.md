---
collection: ansible
version: "6"
title: "google.cloud.gcp_compute_region_disk module – Creates a GCP RegionDisk"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_compute_region_disk_module.html
fetched_at: 2026-07-27T17:48:21+00:00
---
# google.cloud.gcp_compute_region_disk module – Creates a GCP RegionDisk

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
> see [Requirements](gcp_compute_region_disk_module.md#ansible-collections-google-cloud-gcp-compute-region-disk-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_region_disk`.

- [Synopsis](gcp_compute_region_disk_module.md#synopsis)
- [Requirements](gcp_compute_region_disk_module.md#requirements)
- [Parameters](gcp_compute_region_disk_module.md#parameters)
- [Notes](gcp_compute_region_disk_module.md#notes)
- [Examples](gcp_compute_region_disk_module.md#examples)
- [Return Values](gcp_compute_region_disk_module.md#return-values)

## [Synopsis](gcp_compute_region_disk_module.md#id1)

- Persistent disks are durable storage devices that function similarly to the physical disks in a desktop or a server. Compute Engine manages the hardware behind these devices to ensure data redundancy and optimize performance for you. Persistent disks are available as either standard hard disk drives (HDD) or solid-state drives (SSD).
- Persistent disks are located independently from your virtual machine instances, so you can detach or move persistent disks to keep your data even after you delete your instances. Persistent disk performance scales automatically with size, so you can resize your existing persistent disks or add more persistent disks to an instance to meet your performance and storage space requirements.
- Add a persistent disk to your instance when you need reliable and affordable storage with consistent performance characteristics.

## [Requirements](gcp_compute_region_disk_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_region_disk_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **description**  string | An optional description of this resource. Provide this property when you create the resource. |
| **disk_encryption_key**  dictionary | Encrypts the disk using a customer-supplied encryption key.  After you encrypt a disk with a customer-supplied key, you must provide the same key if you use the disk later (e.g. to create a disk snapshot or an image, or to attach the disk to a virtual machine).  Customer-supplied encryption keys do not protect access to metadata of the disk.  If you do not provide an encryption key when creating the disk, then the disk will be encrypted using an automatically generated key and you do not need to provide a key to use the disk later. |
| **raw_key**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **labels**  dictionary | Labels to apply to this disk. A list of key->value pairs. |
| **licenses**  list / elements=string | Any applicable publicly visible licenses. |
| **name**  string / required | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **physical_block_size_bytes**  integer | Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. Currently supported sizes are 4096 and 16384, other sizes may be added in the future.  If an unsupported value is requested, the error message will list the supported values for the caller’s project. |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string / required | A reference to the region where the disk resides. |
| **replica_zones**  list / elements=string / required | URLs of the zones where the disk should be replicated to. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **size_gb**  integer | Size of the persistent disk, specified in GB. You can specify this field when creating a persistent disk using the sourceImage or sourceSnapshot parameter, or specify it alone to create an empty persistent disk.  If you specify this field along with sourceImage or sourceSnapshot, the value of sizeGb must not be less than the size of the sourceImage or the size of the snapshot. |
| **source_snapshot**  dictionary | The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource.  This field represents a link to a Snapshot resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_snapshot task and then set this source_snapshot field to “{{ name-of-resource }}” |
| **source_snapshot_encryption_key**  dictionary | The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a customer-supplied encryption key. |
| **raw_key**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |
| **type**  string | URL of the disk type resource describing which disk type to use to create the disk. Provide this when creating the disk. |

## [Notes](gcp_compute_region_disk_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/rest/v1/regionDisks>
> - Adding or Resizing Regional Persistent Disks: <https://cloud.google.com/compute/docs/disks/regional-persistent-disk>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_region_disk_module.md#id5)

```yaml+jinja
- name: create a region disk
  google.cloud.gcp_compute_region_disk:
    name: test_object
    size_gb: 500
    disk_encryption_key:
      raw_key: SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0=
    region: us-central1
    replica_zones:
    - https://www.googleapis.com/compute/v1/projects/google.com:graphite-playground/zones/us-central1-a
    - https://www.googleapis.com/compute/v1/projects/google.com:graphite-playground/zones/us-central1-b
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_region_disk_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  Returned: success |
| **description**  string | An optional description of this resource. Provide this property when you create the resource.  Returned: success |
| **diskEncryptionKey**  complex | Encrypts the disk using a customer-supplied encryption key.  After you encrypt a disk with a customer-supplied key, you must provide the same key if you use the disk later (e.g. to create a disk snapshot or an image, or to attach the disk to a virtual machine).  Customer-supplied encryption keys do not protect access to metadata of the disk.  If you do not provide an encryption key when creating the disk, then the disk will be encrypted using an automatically generated key and you do not need to provide a key to use the disk later.  Returned: success |
| **rawKey**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.  Returned: success |
| **sha256**  string | The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.  Returned: success |
| **id**  integer | The unique identifier for the resource.  Returned: success |
| **labelFingerprint**  string | The fingerprint used for optimistic locking of this resource. Used internally during updates.  Returned: success |
| **labels**  dictionary | Labels to apply to this disk. A list of key->value pairs.  Returned: success |
| **lastAttachTimestamp**  string | Last attach timestamp in RFC3339 text format.  Returned: success |
| **lastDetachTimestamp**  string | Last detach timestamp in RFC3339 text format.  Returned: success |
| **licenses**  list / elements=string | Any applicable publicly visible licenses.  Returned: success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  Returned: success |
| **physicalBlockSizeBytes**  integer | Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. Currently supported sizes are 4096 and 16384, other sizes may be added in the future.  If an unsupported value is requested, the error message will list the supported values for the caller’s project.  Returned: success |
| **region**  string | A reference to the region where the disk resides.  Returned: success |
| **replicaZones**  list / elements=string | URLs of the zones where the disk should be replicated to.  Returned: success |
| **sizeGb**  integer | Size of the persistent disk, specified in GB. You can specify this field when creating a persistent disk using the sourceImage or sourceSnapshot parameter, or specify it alone to create an empty persistent disk.  If you specify this field along with sourceImage or sourceSnapshot, the value of sizeGb must not be less than the size of the sourceImage or the size of the snapshot.  Returned: success |
| **sourceSnapshot**  dictionary | The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource.  Returned: success |
| **sourceSnapshotEncryptionKey**  complex | The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a customer-supplied encryption key.  Returned: success |
| **rawKey**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.  Returned: success |
| **sha256**  string | The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.  Returned: success |
| **sourceSnapshotId**  string | The unique ID of the snapshot used to create this disk. This value identifies the exact snapshot that was used to create this persistent disk. For example, if you created the persistent disk from a snapshot that was later deleted and recreated under the same name, the source snapshot ID would identify the exact version of the snapshot that was used.  Returned: success |
| **type**  string | URL of the disk type resource describing which disk type to use to create the disk. Provide this when creating the disk.  Returned: success |
| **users**  list / elements=string | Links to the users of the disk (attached instances) in form: project/zones/zone/instances/instance .  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
