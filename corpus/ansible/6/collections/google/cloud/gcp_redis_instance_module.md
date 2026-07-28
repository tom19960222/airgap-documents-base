---
collection: ansible
version: "6"
title: "google.cloud.gcp_redis_instance module – Creates a GCP Instance"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_redis_instance_module.html
fetched_at: 2026-07-27T17:49:17+00:00
---
# google.cloud.gcp_redis_instance module – Creates a GCP Instance

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
> see [Requirements](gcp_redis_instance_module.md#ansible-collections-google-cloud-gcp-redis-instance-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_redis_instance`.

- [Synopsis](gcp_redis_instance_module.md#synopsis)
- [Requirements](gcp_redis_instance_module.md#requirements)
- [Parameters](gcp_redis_instance_module.md#parameters)
- [Notes](gcp_redis_instance_module.md#notes)
- [Examples](gcp_redis_instance_module.md#examples)
- [Return Values](gcp_redis_instance_module.md#return-values)

## [Synopsis](gcp_redis_instance_module.md#id1)

- A Google Cloud Redis instance.

## [Requirements](gcp_redis_instance_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_redis_instance_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alternative_location_id**  string | Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two zones.  If provided, it must be a different zone from the one provided in [locationId]. |
| **auth_enabled**  boolean | Optional. Indicates whether OSS Redis AUTH is enabled for the instance. If set to “true” AUTH is enabled on the instance.  Default value is “false” meaning AUTH is disabled.  Choices:   - `false` ← (default) - `true` |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **authorized_network**  string | The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default network will be used. |
| **connect_mode**  string | The connection mode of the Redis instance.  Some valid choices include: “DIRECT_PEERING”, “PRIVATE_SERVICE_ACCESS”  Default: `"DIRECT_PEERING"` |
| **display_name**  string | An arbitrary and optional user-provided name for the instance. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **labels**  dictionary | Resource labels to represent user provided metadata. |
| **location_id**  string | The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If [alternativeLocationId] is also provided, it must be different from [locationId]. |
| **memory_size_gb**  integer / required | Redis memory size in GiB. |
| **name**  string / required | The ID of the instance or a fully qualified identifier for the instance. |
| **project**  string | The Google Cloud Platform project to use. |
| **redis_configs**  dictionary | Redis configuration parameters, according to <http://redis.io/topics/config>.  Please check Memorystore documentation for the list of supported parameters: <https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs> . |
| **redis_version**  string | The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values are: - REDIS_5_0 for Redis 5.0 compatibility - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility . |
| **region**  string / required | The name of the Redis region of the instance. |
| **reserved_ip_range**  string | The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing subnets in an authorized network. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |
| **tier**  string | The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly available primary/replica instances .  Some valid choices include: “BASIC”, “STANDARD_HA”  Default: `"BASIC"` |

## [Notes](gcp_redis_instance_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/memorystore/docs/redis/reference/rest/>
> - Official Documentation: <https://cloud.google.com/memorystore/docs/redis/>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_redis_instance_module.md#id5)

```yaml+jinja
- name: create a network
  google.cloud.gcp_compute_network:
    name: network-instance
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: network

- name: create a instance
  google.cloud.gcp_redis_instance:
    name: instance37
    tier: STANDARD_HA
    memory_size_gb: 1
    region: us-central1
    location_id: us-central1-a
    redis_version: REDIS_3_2
    display_name: Ansible Test Instance
    reserved_ip_range: 192.168.0.0/29
    labels:
      my_key: my_val
      other_key: other_val
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_redis_instance_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **alternativeLocationId**  string | Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two zones.  If provided, it must be a different zone from the one provided in [locationId].  Returned: success |
| **authEnabled**  boolean | Optional. Indicates whether OSS Redis AUTH is enabled for the instance. If set to “true” AUTH is enabled on the instance.  Default value is “false” meaning AUTH is disabled.  Returned: success |
| **authorizedNetwork**  string | The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default network will be used.  Returned: success |
| **connectMode**  string | The connection mode of the Redis instance.  Returned: success |
| **createTime**  string | The time the instance was created in RFC3339 UTC “Zulu” format, accurate to nanoseconds.  Returned: success |
| **currentLocationId**  string | The current zone where the Redis endpoint is placed.  For Basic Tier instances, this will always be the same as the [locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or [alternativeLocationId] and can change after a failover event.  Returned: success |
| **displayName**  string | An arbitrary and optional user-provided name for the instance.  Returned: success |
| **host**  string | Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.  Returned: success |
| **labels**  dictionary | Resource labels to represent user provided metadata.  Returned: success |
| **locationId**  string | The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If [alternativeLocationId] is also provided, it must be different from [locationId].  Returned: success |
| **memorySizeGb**  integer | Redis memory size in GiB.  Returned: success |
| **name**  string | The ID of the instance or a fully qualified identifier for the instance.  Returned: success |
| **persistenceIamIdentity**  string | Output only. Cloud IAM identity used by import / export operations to transfer data to/from Cloud Storage. Format is “serviceAccount:”.  The value may change over time for a given instance so should be checked before each import/export operation.  Returned: success |
| **port**  integer | The port number of the exposed Redis endpoint.  Returned: success |
| **redisConfigs**  dictionary | Redis configuration parameters, according to <http://redis.io/topics/config>.  Please check Memorystore documentation for the list of supported parameters: <https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs> .  Returned: success |
| **redisVersion**  string | The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values are: - REDIS_5_0 for Redis 5.0 compatibility - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility .  Returned: success |
| **region**  string | The name of the Redis region of the instance.  Returned: success |
| **reservedIpRange**  string | The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing subnets in an authorized network.  Returned: success |
| **tier**  string | The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly available primary/replica instances .  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
