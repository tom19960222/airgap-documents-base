---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_image_info module – Gather info for GCP Image"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_image_info_module.html
fetched_at: 2026-07-28T02:32:11+00:00
---
# google.cloud.gcp_compute_image_info module – Gather info for GCP Image

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
> see [Requirements](gcp_compute_image_info_module.md#ansible-collections-google-cloud-gcp-compute-image-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_image_info`.

- [Synopsis](gcp_compute_image_info_module.md#synopsis)
- [Requirements](gcp_compute_image_info_module.md#requirements)
- [Parameters](gcp_compute_image_info_module.md#parameters)
- [Notes](gcp_compute_image_info_module.md#notes)
- [Examples](gcp_compute_image_info_module.md#examples)
- [Return Values](gcp_compute_image_info_module.md#return-values)

## [Synopsis](gcp_compute_image_info_module.md#id1)

- Gather info for GCP Image

## [Requirements](gcp_compute_image_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_image_info_module.md#id3)

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

## [Notes](gcp_compute_image_info_module.md#id4)

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

## [Examples](gcp_compute_image_info_module.md#id5)

```yaml+jinja
- name: get info on an image
  gcp_compute_image_info:
    filters:
    - name = test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_compute_image_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  **Returned:** always |
| **archiveSizeBytes**  integer | Size of the image tar.gz archive stored in Google Cloud Storage (in bytes).  **Returned:** success |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **deprecated**  complex | The deprecation status associated with this image.  **Returned:** success |
| **deleted**  string | An optional RFC3339 timestamp on or after which the state of this resource is intended to change to DELETED. This is only informational and the status will not change unless the client explicitly changes it.  **Returned:** success |
| **deprecated**  string | An optional RFC3339 timestamp on or after which the state of this resource is intended to change to DEPRECATED. This is only informational and the status will not change unless the client explicitly changes it.  **Returned:** success |
| **obsolete**  string | An optional RFC3339 timestamp on or after which the state of this resource is intended to change to OBSOLETE. This is only informational and the status will not change unless the client explicitly changes it.  **Returned:** success |
| **replacement**  string | The URL of the suggested replacement for a deprecated resource.  The suggested replacement resource must be the same kind of resource as the deprecated resource.  **Returned:** success |
| **state**  string | The deprecation state of this resource. This can be DEPRECATED, OBSOLETE, or DELETED. Operations which create a new resource using a DEPRECATED resource will return successfully, but with a warning indicating the deprecated resource and recommending its replacement. Operations which use OBSOLETE or DELETED resources will be rejected and result in an error.  **Returned:** success |
| **description**  string | An optional description of this resource. Provide this property when you create the resource.  **Returned:** success |
| **diskSizeGb**  integer | Size of the image when restored onto a persistent disk (in GB).  **Returned:** success |
| **family**  string | The name of the image family to which this image belongs. You can create disks by specifying an image family instead of a specific image name. The image family always returns its latest image that is not deprecated. The name of the image family must comply with RFC1035.  **Returned:** success |
| **guestOsFeatures**  complex | A list of features to enable on the guest operating system.  Applicable only for bootable images.  **Returned:** success |
| **type**  string | The type of supported feature.  **Returned:** success |
| **id**  integer | The unique identifier for the resource. This identifier is defined by the server.  **Returned:** success |
| **imageEncryptionKey**  complex | Encrypts the image using a customer-supplied encryption key.  After you encrypt an image with a customer-supplied key, you must provide the same key if you use the image later (e.g. to create a disk from the image) .  **Returned:** success |
| **rawKey**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.  **Returned:** success |
| **sha256**  string | The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.  **Returned:** success |
| **labelFingerprint**  string | The fingerprint used for optimistic locking of this resource. Used internally during updates.  **Returned:** success |
| **labels**  dictionary | Labels to apply to this Image.  **Returned:** success |
| **licenses**  list / elements=string | Any applicable license URI.  **Returned:** success |
| **name**  string | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **rawDisk**  complex | The parameters of the raw disk image.  **Returned:** success |
| **containerType**  string | The format used to encode and transmit the block device, which should be TAR. This is just a container and transmission format and not a runtime format. Provided by the client when the disk image is created.  **Returned:** success |
| **sha1Checksum**  string | An optional SHA1 checksum of the disk image before unpackaging.  This is provided by the client when the disk image is created.  **Returned:** success |
| **source**  string | The full Google Cloud Storage URL where disk storage is stored You must provide either this property or the sourceDisk property but not both.  **Returned:** success |
| **sourceDisk**  dictionary | The source disk to create this image based on.  You must provide either this property or the rawDisk.source property but not both to create an image.  **Returned:** success |
| **sourceDiskEncryptionKey**  complex | The customer-supplied encryption key of the source disk. Required if the source disk is protected by a customer-supplied encryption key.  **Returned:** success |
| **rawKey**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.  **Returned:** success |
| **sha256**  string | The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.  **Returned:** success |
| **sourceDiskId**  string | The ID value of the disk used to create this image. This value may be used to determine whether the image was taken from the current or a previous instance of a given disk name.  **Returned:** success |
| **sourceImage**  dictionary | URL of the source image used to create this image. In order to create an image, you must provide the full or partial URL of one of the following: \* The selfLink URL \* This property \* The rawDisk.source URL \* The sourceDisk URL .  **Returned:** success |
| **sourceSnapshot**  dictionary | URL of the source snapshot used to create this image.  In order to create an image, you must provide the full or partial URL of one of the following: \* The selfLink URL \* This property \* The sourceImage URL \* The rawDisk.source URL \* The sourceDisk URL .  **Returned:** success |
| **sourceType**  string | The type of the image used to create this disk. The default and only value is RAW .  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
