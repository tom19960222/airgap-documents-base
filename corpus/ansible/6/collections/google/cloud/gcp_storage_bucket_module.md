---
collection: ansible
version: "6"
title: "google.cloud.gcp_storage_bucket module – Creates a GCP Bucket"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_storage_bucket_module.html
fetched_at: 2026-07-27T17:49:32+00:00
---
# google.cloud.gcp_storage_bucket module – Creates a GCP Bucket

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
> see [Requirements](gcp_storage_bucket_module.md#ansible-collections-google-cloud-gcp-storage-bucket-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_storage_bucket`.

- [Synopsis](gcp_storage_bucket_module.md#synopsis)
- [Requirements](gcp_storage_bucket_module.md#requirements)
- [Parameters](gcp_storage_bucket_module.md#parameters)
- [Examples](gcp_storage_bucket_module.md#examples)
- [Return Values](gcp_storage_bucket_module.md#return-values)

## [Synopsis](gcp_storage_bucket_module.md#id1)

- The Buckets resource represents a bucket in Google Cloud Storage. There is a single global namespace shared by all buckets. For more information, see Bucket Name Requirements.
- Buckets contain objects which can be accessed by their own methods. In addition to the acl property, buckets contain bucketAccessControls, for use in fine-grained manipulation of an existing bucket’s access controls.
- A bucket is always owned by the project team owners group.

## [Requirements](gcp_storage_bucket_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_storage_bucket_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **acl**  list / elements=dictionary | Access controls on the bucket. |
| **bucket**  dictionary / required | The name of the bucket.  This field represents a link to a Bucket resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘name’ and value of your resource’s name Alternatively, you can add `register: name-of-resource` to a gcp_storage_bucket task and then set this bucket field to “{{ name-of-resource }}” |
| **entity**  string / required | The entity holding the permission, in one of the following forms: user-userId user-email group-groupId group-email domain-domain project-team-projectId allUsers allAuthenticatedUsers Examples: The user [liz@example.com](mailto:liz%40example.com) would be [user-liz@example.com](mailto:user-liz%40example.com).  The group [example@googlegroups.com](mailto:example%40googlegroups.com) would be [group-example@googlegroups.com](mailto:group-example%40googlegroups.com).  To refer to all members of the Google Apps for Business domain example.com, the entity would be domain-example.com. |
| **entity_id**  string | The ID for the entity. |
| **project_team**  dictionary | The project team associated with the entity. |
| **project_number**  string | The project team associated with the entity. |
| **team**  string | The team.  Some valid choices include: “editors”, “owners”, “viewers” |
| **role**  string | The access permission for the entity.  Some valid choices include: “OWNER”, “READER”, “WRITER” |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **cors**  list / elements=dictionary | The bucket’s Cross-Origin Resource Sharing (CORS) configuration. |
| **max_age_seconds**  integer | The value, in seconds, to return in the Access-Control-Max-Age header used in preflight responses. |
| **method**  list / elements=string | The list of HTTP methods on which to include CORS response headers, (GET, OPTIONS, POST, etc) Note: “\*” is permitted in the list of methods, and means “any method”. |
| **origin**  list / elements=string | The list of Origins eligible to receive CORS response headers.  Note: “\*” is permitted in the list of origins, and means “any Origin”. |
| **response_header**  list / elements=string | The list of HTTP headers other than the simple response headers to give permission for the user-agent to share across domains. |
| **default_event_based_hold**  boolean | Whether or not to automatically apply an eventBasedHold to new objects added to the bucket.  Choices:   - `false` - `true` |
| **default_object_acl**  list / elements=dictionary | Default access controls to apply to new objects when no ACL is provided. |
| **bucket**  dictionary / required | The name of the bucket.  This field represents a link to a Bucket resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘name’ and value of your resource’s name Alternatively, you can add `register: name-of-resource` to a gcp_storage_bucket task and then set this bucket field to “{{ name-of-resource }}” |
| **entity**  string / required | The entity holding the permission, in one of the following forms: \* user-{{userId}} \* user-{{email}} (such as “[user-liz@example.com](mailto:user-liz%40example.com)”) \* group-{{groupId}} \* group-{{email}} (such as “[group-example@googlegroups.com](mailto:group-example%40googlegroups.com)”) \* domain-{{domain}} (such as “domain-example.com”) \* project-team-{{projectId}} \* allUsers \* allAuthenticatedUsers . |
| **object**  string | The name of the object, if applied to an object. |
| **role**  string / required | The access permission for the entity.  Some valid choices include: “OWNER”, “READER” |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **labels**  dictionary | Labels applied to this bucket. A list of key->value pairs. |
| **lifecycle**  dictionary | The bucket’s lifecycle configuration.  See <https://developers.google.com/storage/docs/lifecycle> for more information. |
| **rule**  list / elements=dictionary | A lifecycle management rule, which is made of an action to take and the condition(s) under which the action will be taken. |
| **action**  dictionary | The action to take. |
| **storage_class**  string | Target storage class. Required iff the type of the action is SetStorageClass. |
| **type**  string | Type of the action. Currently, only Delete and SetStorageClass are supported.  Some valid choices include: “Delete”, “SetStorageClass” |
| **condition**  dictionary | The condition(s) under which the action will be taken. |
| **age_days**  integer | Age of an object (in days). This condition is satisfied when an object reaches the specified age. |
| **created_before**  string | A date in RFC 3339 format with only the date part (for instance, “2013-01-15”). This condition is satisfied when an object is created before midnight of the specified date in UTC. |
| **is_live**  boolean | Relevant only for versioned objects. If the value is true, this condition matches live objects; if the value is false, it matches archived objects.  Choices:   - `false` - `true` |
| **matches_storage_class**  list / elements=string | Objects having any of the storage classes specified by this condition will be matched. Values include MULTI_REGIONAL, REGIONAL, NEARLINE, COLDLINE, ARCHIVE, STANDARD, and DURABLE_REDUCED_AVAILABILITY. |
| **num_newer_versions**  integer | Relevant only for versioned objects. If the value is N, this condition is satisfied when there are at least N versions (including the live version) newer than this version of the object. |
| **location**  string | The location of the bucket. Object data for objects in the bucket resides in physical storage within this region. Defaults to US. See the developer’s guide for the authoritative list. |
| **logging**  dictionary | The bucket’s logging configuration, which defines the destination bucket and optional name prefix for the current bucket’s logs. |
| **log_bucket**  string | The destination bucket where the current bucket’s logs should be placed. |
| **log_object_prefix**  string | A prefix for log object names. |
| **metageneration**  integer | The metadata generation of this bucket. |
| **name**  string | The name of the bucket. |
| **owner**  dictionary | The owner of the bucket. This is always the project team’s owner group. |
| **entity**  string | The entity, in the form project-owner-projectId. |
| **predefined_default_object_acl**  string | Apply a predefined set of default object access controls to this bucket.  Acceptable values are: - “authenticatedRead”: Object owner gets OWNER access, and allAuthenticatedUsers get READER access.   - “bucketOwnerFullControl”: Object owner gets OWNER access, and project team owners get OWNER access. - “bucketOwnerRead”: Object owner gets OWNER access, and project team owners get READER access. - “private”: Object owner gets OWNER access. - “projectPrivate”: Object owner gets OWNER access, and project team members get access according to their roles. - “publicRead”: Object owner gets OWNER access, and allUsers get READER access.   Some valid choices include: “authenticatedRead”, “bucketOwnerFullControl”, “bucketOwnerRead”, “private”, “projectPrivate”, “publicRead” |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |
| **storage_class**  string | The bucket’s default storage class, used whenever no storageClass is specified for a newly-created object. This defines how objects in the bucket are stored and determines the SLA and the cost of storage.  Values include MULTI_REGIONAL, REGIONAL, STANDARD, NEARLINE, COLDLINE, ARCHIVE, and DURABLE_REDUCED_AVAILABILITY. If this value is not specified when the bucket is created, it will default to STANDARD. For more information, see storage classes.  Some valid choices include: “MULTI_REGIONAL”, “REGIONAL”, “STANDARD”, “NEARLINE”, “COLDLINE”, “ARCHIVE”, “DURABLE_REDUCED_AVAILABILITY” |
| **versioning**  dictionary | The bucket’s versioning configuration. |
| **enabled**  boolean | While set to true, versioning is fully enabled for this bucket.  Choices:   - `false` - `true` |
| **website**  dictionary | The bucket’s website configuration, controlling how the service behaves when accessing bucket contents as a web site. See the Static Website Examples for more information. |
| **main_page_suffix**  string | If the requested object path is missing, the service will ensure the path has a trailing ‘/’, append this suffix, and attempt to retrieve the resulting object. This allows the creation of index.html objects to represent directory pages. |
| **not_found_page**  string | If the requested object path is missing, and any mainPageSuffix object is missing, if applicable, the service will return the named object from this bucket as the content for a 404 Not Found result. |

## [Examples](gcp_storage_bucket_module.md#id4)

```yaml+jinja
- name: create a bucket
  google.cloud.gcp_storage_bucket:
    name: ansible-storage-module
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_storage_bucket_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **acl**  complex | Access controls on the bucket.  Returned: success |
| **bucket**  dictionary | The name of the bucket.  Returned: success |
| **domain**  string | The domain associated with the entity.  Returned: success |
| **email**  string | The email address associated with the entity.  Returned: success |
| **entity**  string | The entity holding the permission, in one of the following forms: user-userId user-email group-groupId group-email domain-domain project-team-projectId allUsers allAuthenticatedUsers Examples: The user [liz@example.com](mailto:liz%40example.com) would be [user-liz@example.com](mailto:user-liz%40example.com).  The group [example@googlegroups.com](mailto:example%40googlegroups.com) would be [group-example@googlegroups.com](mailto:group-example%40googlegroups.com).  To refer to all members of the Google Apps for Business domain example.com, the entity would be domain-example.com.  Returned: success |
| **entityId**  string | The ID for the entity.  Returned: success |
| **id**  string | The ID of the access-control entry.  Returned: success |
| **projectTeam**  complex | The project team associated with the entity.  Returned: success |
| **projectNumber**  string | The project team associated with the entity.  Returned: success |
| **team**  string | The team.  Returned: success |
| **role**  string | The access permission for the entity.  Returned: success |
| **cors**  complex | The bucket’s Cross-Origin Resource Sharing (CORS) configuration.  Returned: success |
| **maxAgeSeconds**  integer | The value, in seconds, to return in the Access-Control-Max-Age header used in preflight responses.  Returned: success |
| **method**  list / elements=string | The list of HTTP methods on which to include CORS response headers, (GET, OPTIONS, POST, etc) Note: “\*” is permitted in the list of methods, and means “any method”.  Returned: success |
| **origin**  list / elements=string | The list of Origins eligible to receive CORS response headers.  Note: “\*” is permitted in the list of origins, and means “any Origin”.  Returned: success |
| **responseHeader**  list / elements=string | The list of HTTP headers other than the simple response headers to give permission for the user-agent to share across domains.  Returned: success |
| **defaultEventBasedHold**  boolean | Whether or not to automatically apply an eventBasedHold to new objects added to the bucket.  Returned: success |
| **defaultObjectAcl**  complex | Default access controls to apply to new objects when no ACL is provided.  Returned: success |
| **bucket**  dictionary | The name of the bucket.  Returned: success |
| **domain**  string | The domain associated with the entity.  Returned: success |
| **email**  string | The email address associated with the entity.  Returned: success |
| **entity**  string | The entity holding the permission, in one of the following forms: \* user-{{userId}} \* user-{{email}} (such as “[user-liz@example.com](mailto:user-liz%40example.com)”) \* group-{{groupId}} \* group-{{email}} (such as “[group-example@googlegroups.com](mailto:group-example%40googlegroups.com)”) \* domain-{{domain}} (such as “domain-example.com”) \* project-team-{{projectId}} \* allUsers \* allAuthenticatedUsers .  Returned: success |
| **entityId**  string | The ID for the entity.  Returned: success |
| **generation**  integer | The content generation of the object, if applied to an object.  Returned: success |
| **id**  string | The ID of the access-control entry.  Returned: success |
| **object**  string | The name of the object, if applied to an object.  Returned: success |
| **projectTeam**  complex | The project team associated with the entity.  Returned: success |
| **projectNumber**  string | The project team associated with the entity.  Returned: success |
| **team**  string | The team.  Returned: success |
| **role**  string | The access permission for the entity.  Returned: success |
| **id**  string | The ID of the bucket. For buckets, the id and name properities are the same.  Returned: success |
| **labels**  dictionary | Labels applied to this bucket. A list of key->value pairs.  Returned: success |
| **lifecycle**  complex | The bucket’s lifecycle configuration.  See <https://developers.google.com/storage/docs/lifecycle> for more information.  Returned: success |
| **rule**  complex | A lifecycle management rule, which is made of an action to take and the condition(s) under which the action will be taken.  Returned: success |
| **action**  complex | The action to take.  Returned: success |
| **storageClass**  string | Target storage class. Required iff the type of the action is SetStorageClass.  Returned: success |
| **type**  string | Type of the action. Currently, only Delete and SetStorageClass are supported.  Returned: success |
| **condition**  complex | The condition(s) under which the action will be taken.  Returned: success |
| **ageDays**  integer | Age of an object (in days). This condition is satisfied when an object reaches the specified age.  Returned: success |
| **createdBefore**  string | A date in RFC 3339 format with only the date part (for instance, “2013-01-15”). This condition is satisfied when an object is created before midnight of the specified date in UTC.  Returned: success |
| **isLive**  boolean | Relevant only for versioned objects. If the value is true, this condition matches live objects; if the value is false, it matches archived objects.  Returned: success |
| **matchesStorageClass**  list / elements=string | Objects having any of the storage classes specified by this condition will be matched. Values include MULTI_REGIONAL, REGIONAL, NEARLINE, COLDLINE, ARCHIVE, STANDARD, and DURABLE_REDUCED_AVAILABILITY.  Returned: success |
| **numNewerVersions**  integer | Relevant only for versioned objects. If the value is N, this condition is satisfied when there are at least N versions (including the live version) newer than this version of the object.  Returned: success |
| **location**  string | The location of the bucket. Object data for objects in the bucket resides in physical storage within this region. Defaults to US. See the developer’s guide for the authoritative list.  Returned: success |
| **logging**  complex | The bucket’s logging configuration, which defines the destination bucket and optional name prefix for the current bucket’s logs.  Returned: success |
| **logBucket**  string | The destination bucket where the current bucket’s logs should be placed.  Returned: success |
| **logObjectPrefix**  string | A prefix for log object names.  Returned: success |
| **metageneration**  integer | The metadata generation of this bucket.  Returned: success |
| **name**  string | The name of the bucket.  Returned: success |
| **owner**  complex | The owner of the bucket. This is always the project team’s owner group.  Returned: success |
| **entity**  string | The entity, in the form project-owner-projectId.  Returned: success |
| **entityId**  string | The ID for the entity.  Returned: success |
| **predefinedDefaultObjectAcl**  string | Apply a predefined set of default object access controls to this bucket.  Acceptable values are: - “authenticatedRead”: Object owner gets OWNER access, and allAuthenticatedUsers get READER access.   - “bucketOwnerFullControl”: Object owner gets OWNER access, and project team owners get OWNER access. - “bucketOwnerRead”: Object owner gets OWNER access, and project team owners get READER access. - “private”: Object owner gets OWNER access. - “projectPrivate”: Object owner gets OWNER access, and project team members get access according to their roles. - “publicRead”: Object owner gets OWNER access, and allUsers get READER access.   Returned: success |
| **project**  string | A valid API project identifier.  Returned: success |
| **projectNumber**  string | The project number of the project the bucket belongs to.  Returned: success |
| **storageClass**  string | The bucket’s default storage class, used whenever no storageClass is specified for a newly-created object. This defines how objects in the bucket are stored and determines the SLA and the cost of storage.  Values include MULTI_REGIONAL, REGIONAL, STANDARD, NEARLINE, COLDLINE, ARCHIVE, and DURABLE_REDUCED_AVAILABILITY. If this value is not specified when the bucket is created, it will default to STANDARD. For more information, see storage classes.  Returned: success |
| **timeCreated**  string | The creation time of the bucket in RFC 3339 format.  Returned: success |
| **updated**  string | The modification time of the bucket in RFC 3339 format.  Returned: success |
| **versioning**  complex | The bucket’s versioning configuration.  Returned: success |
| **enabled**  boolean | While set to true, versioning is fully enabled for this bucket.  Returned: success |
| **website**  complex | The bucket’s website configuration, controlling how the service behaves when accessing bucket contents as a web site. See the Static Website Examples for more information.  Returned: success |
| **mainPageSuffix**  string | If the requested object path is missing, the service will ensure the path has a trailing ‘/’, append this suffix, and attempt to retrieve the resulting object. This allows the creation of index.html objects to represent directory pages.  Returned: success |
| **notFoundPage**  string | If the requested object path is missing, and any mainPageSuffix object is missing, if applicable, the service will return the named object from this bucket as the content for a 404 Not Found result.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
