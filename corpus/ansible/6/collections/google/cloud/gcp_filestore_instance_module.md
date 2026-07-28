---
collection: ansible
version: "6"
title: "google.cloud.gcp_filestore_instance module – Creates a GCP Instance"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_filestore_instance_module.html
fetched_at: 2026-07-27T17:49:01+00:00
---
# google.cloud.gcp_filestore_instance module – Creates a GCP Instance

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
> see [Requirements](gcp_filestore_instance_module.md#ansible-collections-google-cloud-gcp-filestore-instance-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_filestore_instance`.

- [Synopsis](gcp_filestore_instance_module.md#synopsis)
- [Requirements](gcp_filestore_instance_module.md#requirements)
- [Parameters](gcp_filestore_instance_module.md#parameters)
- [Notes](gcp_filestore_instance_module.md#notes)
- [Examples](gcp_filestore_instance_module.md#examples)
- [Return Values](gcp_filestore_instance_module.md#return-values)

## [Synopsis](gcp_filestore_instance_module.md#id1)

- A Google Cloud Filestore instance.

## [Requirements](gcp_filestore_instance_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_filestore_instance_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **description**  string | A description of the instance. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **file_shares**  list / elements=dictionary / required | File system shares on the instance. For this version, only a single file share is supported. |
| **capacity_gb**  integer / required | File share capacity in GiB. This must be at least 1024 GiB for the standard tier, or 2560 GiB for the premium tier. |
| **name**  string / required | The name of the fileshare (16 characters or less) . |
| **labels**  dictionary | Resource labels to represent user-provided metadata. |
| **name**  string / required | The resource name of the instance. |
| **networks**  list / elements=dictionary / required | VPC networks to which the instance is connected. For this version, only a single network is supported. |
| **modes**  list / elements=string / required | IP versions for which the instance has IP addresses assigned. |
| **network**  string / required | The name of the GCE VPC network to which the instance is connected. |
| **reserved_ip_range**  string | A /29 CIDR block that identifies the range of IP addresses reserved for this instance. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |
| **tier**  string / required | The service tier of the instance.  Some valid choices include: “TIER_UNSPECIFIED”, “STANDARD”, “PREMIUM”, “BASIC_HDD”, “BASIC_SSD”, “HIGH_SCALE_SSD” |
| **zone**  string / required | The name of the Filestore zone of the instance. |

## [Notes](gcp_filestore_instance_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/create>
> - Official Documentation: <https://cloud.google.com/filestore/docs/creating-instances>
> - Use with Kubernetes: <https://cloud.google.com/filestore/docs/accessing-fileshares>
> - Copying Data In/Out: <https://cloud.google.com/filestore/docs/copying-data>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_filestore_instance_module.md#id5)

```yaml+jinja
- name: create a instance
  google.cloud.gcp_filestore_instance:
    name: test_object
    zone: us-central1-b
    tier: PREMIUM
    file_shares:
    - capacity_gb: 2660
      name: share1
    networks:
    - network: default
      modes:
      - MODE_IPV4
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_filestore_instance_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **createTime**  string | Creation timestamp in RFC3339 text format.  Returned: success |
| **description**  string | A description of the instance.  Returned: success |
| **etag**  string | Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.  Returned: success |
| **fileShares**  complex | File system shares on the instance. For this version, only a single file share is supported.  Returned: success |
| **capacityGb**  integer | File share capacity in GiB. This must be at least 1024 GiB for the standard tier, or 2560 GiB for the premium tier.  Returned: success |
| **name**  string | The name of the fileshare (16 characters or less) .  Returned: success |
| **labels**  dictionary | Resource labels to represent user-provided metadata.  Returned: success |
| **name**  string | The resource name of the instance.  Returned: success |
| **networks**  complex | VPC networks to which the instance is connected. For this version, only a single network is supported.  Returned: success |
| **ipAddresses**  list / elements=string | A list of IPv4 or IPv6 addresses.  Returned: success |
| **modes**  list / elements=string | IP versions for which the instance has IP addresses assigned.  Returned: success |
| **network**  string | The name of the GCE VPC network to which the instance is connected.  Returned: success |
| **reservedIpRange**  string | A /29 CIDR block that identifies the range of IP addresses reserved for this instance.  Returned: success |
| **tier**  string | The service tier of the instance.  Returned: success |
| **zone**  string | The name of the Filestore zone of the instance.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
