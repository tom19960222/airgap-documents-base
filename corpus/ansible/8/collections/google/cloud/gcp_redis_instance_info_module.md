---
collection: ansible
version: "8"
title: "google.cloud.gcp_redis_instance_info module – Gather info for GCP Instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_redis_instance_info_module.html
fetched_at: 2026-07-28T02:33:26+00:00
---
# google.cloud.gcp_redis_instance_info module – Gather info for GCP Instance

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
> see [Requirements](gcp_redis_instance_info_module.md#ansible-collections-google-cloud-gcp-redis-instance-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_redis_instance_info`.

- [Synopsis](gcp_redis_instance_info_module.md#synopsis)
- [Requirements](gcp_redis_instance_info_module.md#requirements)
- [Parameters](gcp_redis_instance_info_module.md#parameters)
- [Notes](gcp_redis_instance_info_module.md#notes)
- [Examples](gcp_redis_instance_info_module.md#examples)
- [Return Values](gcp_redis_instance_info_module.md#return-values)

## [Synopsis](gcp_redis_instance_info_module.md#id1)

- Gather info for GCP Instance

## [Requirements](gcp_redis_instance_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_redis_instance_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string / required | The name of the Redis region of the instance. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |

## [Notes](gcp_redis_instance_info_module.md#id4)

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

## [Examples](gcp_redis_instance_info_module.md#id5)

```yaml+jinja
- name: get info on an instance
  gcp_redis_instance_info:
    region: us-central1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_redis_instance_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  **Returned:** always |
| **alternativeLocationId**  string | Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two zones.  If provided, it must be a different zone from the one provided in [locationId].  **Returned:** success |
| **authEnabled**  boolean | Optional. Indicates whether OSS Redis AUTH is enabled for the instance. If set to “true” AUTH is enabled on the instance.  Default value is “false” meaning AUTH is disabled.  **Returned:** success |
| **authorizedNetwork**  string | The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default network will be used.  **Returned:** success |
| **connectMode**  string | The connection mode of the Redis instance.  **Returned:** success |
| **createTime**  string | The time the instance was created in RFC3339 UTC “Zulu” format, accurate to nanoseconds.  **Returned:** success |
| **currentLocationId**  string | The current zone where the Redis endpoint is placed.  For Basic Tier instances, this will always be the same as the [locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or [alternativeLocationId] and can change after a failover event.  **Returned:** success |
| **displayName**  string | An arbitrary and optional user-provided name for the instance.  **Returned:** success |
| **host**  string | Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.  **Returned:** success |
| **labels**  dictionary | Resource labels to represent user provided metadata.  **Returned:** success |
| **locationId**  string | The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If [alternativeLocationId] is also provided, it must be different from [locationId].  **Returned:** success |
| **memorySizeGb**  integer | Redis memory size in GiB.  **Returned:** success |
| **name**  string | The ID of the instance or a fully qualified identifier for the instance.  **Returned:** success |
| **persistenceIamIdentity**  string | Output only. Cloud IAM identity used by import / export operations to transfer data to/from Cloud Storage. Format is “serviceAccount:”.  The value may change over time for a given instance so should be checked before each import/export operation.  **Returned:** success |
| **port**  integer | The port number of the exposed Redis endpoint.  **Returned:** success |
| **redisConfigs**  dictionary | Redis configuration parameters, according to <http://redis.io/topics/config>.  Please check Memorystore documentation for the list of supported parameters: <https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs> .  **Returned:** success |
| **redisVersion**  string | The version of Redis software. If not provided, latest supported version will be used. Please check the API documentation linked at the top for the latest valid values.  **Returned:** success |
| **region**  string | The name of the Redis region of the instance.  **Returned:** success |
| **reservedIpRange**  string | The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing subnets in an authorized network.  **Returned:** success |
| **serverCaCerts**  complex | List of server CA certificates for the instance.  **Returned:** success |
| **cert**  string | Serial number, as extracted from the certificate.  **Returned:** success |
| **createTime**  string | The time when the certificate was created.  **Returned:** success |
| **expireTime**  string | The time when the certificate expires.  **Returned:** success |
| **serialNumber**  string | Serial number, as extracted from the certificate.  **Returned:** success |
| **sha1Fingerprint**  string | Sha1 Fingerprint of the certificate.  **Returned:** success |
| **tier**  string | The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly available primary/replica instances .  **Returned:** success |
| **transitEncryptionMode**  string | The TLS mode of the Redis instance, If not provided, TLS is disabled for the instance.   - SERVER_AUTHENTICATION: Client to Server traffic encryption enabled with server authentcation .   **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
