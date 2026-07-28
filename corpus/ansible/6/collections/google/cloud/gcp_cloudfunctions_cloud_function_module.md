---
collection: ansible
version: "6"
title: "google.cloud.gcp_cloudfunctions_cloud_function module – Creates a GCP CloudFunction"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_cloudfunctions_cloud_function_module.html
fetched_at: 2026-07-27T17:47:41+00:00
---
# google.cloud.gcp_cloudfunctions_cloud_function module – Creates a GCP CloudFunction

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
> see [Requirements](gcp_cloudfunctions_cloud_function_module.md#ansible-collections-google-cloud-gcp-cloudfunctions-cloud-function-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_cloudfunctions_cloud_function`.

- [Synopsis](gcp_cloudfunctions_cloud_function_module.md#synopsis)
- [Requirements](gcp_cloudfunctions_cloud_function_module.md#requirements)
- [Parameters](gcp_cloudfunctions_cloud_function_module.md#parameters)
- [Examples](gcp_cloudfunctions_cloud_function_module.md#examples)
- [Return Values](gcp_cloudfunctions_cloud_function_module.md#return-values)

## [Synopsis](gcp_cloudfunctions_cloud_function_module.md#id1)

- A Cloud Function that contains user computation executed in response to an event.

## [Requirements](gcp_cloudfunctions_cloud_function_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_cloudfunctions_cloud_function_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **available_memory_mb**  integer | The amount of memory in MB available for a function. |
| **description**  string | User-provided description of a function. |
| **entry_point**  string | The name of the function (as defined in source code) that will be executed.  Defaults to the resource name suffix, if not specified. For backward compatibility, if function with given name is not found, then the system will try to use function named “function”. For Node.js this is name of a function exported by the module specified in source_location. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **environment_variables**  dictionary | Environment variables that shall be available during function execution. |
| **event_trigger**  dictionary | An HTTPS endpoint type of source that can be triggered via URL. |
| **event_type**  string / required | The type of event to observe. For example: `providers/cloud.storage/eventTypes/object.change` and `providers/cloud.pubsub/eventTypes/topic.publish`. |
| **resource**  string / required | The resource(s) from which to observe events, for example, `projects/_/buckets/myBucket.` . |
| **service**  string | The hostname of the service that should be observed. |
| **https_trigger**  dictionary | An HTTPS endpoint type of source that can be triggered via URL. |
| **labels**  dictionary | A set of key/value label pairs associated with this Cloud Function. |
| **location**  string / required | The location of this cloud function. |
| **name**  string / required | A user-defined name of the function. Function names must be unique globally and match pattern `projects/\*/locations/\*/functions/\*`. |
| **project**  string | The Google Cloud Platform project to use. |
| **runtime**  string | The runtime in which the function is going to run. If empty, defaults to Node.js 6. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **source_archive_url**  string | The Google Cloud Storage URL, starting with gs://, pointing to the zip archive which contains the function. |
| **source_repository**  dictionary | The source repository where a function is hosted. |
| **url**  string / required | The URL pointing to the hosted repository where the function is defined . |
| **source_upload_url**  string | The Google Cloud Storage signed URL used for source uploading. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  string | The function execution timeout. Execution is considered failed and can be terminated if the function is not completed at the end of the timeout period. Defaults to 60 seconds. |
| **trigger_http**  boolean | Use HTTP to trigger this function.  Choices:   - `false` - `true` |

## [Examples](gcp_cloudfunctions_cloud_function_module.md#id4)

```yaml+jinja
- name: create a cloud function
  google.cloud.gcp_cloudfunctions_cloud_function:
    name: test_object
    location: us-central1
    entry_point: helloGET
    source_archive_url: gs://ansible-cloudfunctions-bucket/function.zip
    trigger_http: 'true'
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_cloudfunctions_cloud_function_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **availableMemoryMb**  integer | The amount of memory in MB available for a function.  Returned: success |
| **description**  string | User-provided description of a function.  Returned: success |
| **entryPoint**  string | The name of the function (as defined in source code) that will be executed.  Defaults to the resource name suffix, if not specified. For backward compatibility, if function with given name is not found, then the system will try to use function named “function”. For Node.js this is name of a function exported by the module specified in source_location.  Returned: success |
| **environmentVariables**  dictionary | Environment variables that shall be available during function execution.  Returned: success |
| **eventTrigger**  complex | An HTTPS endpoint type of source that can be triggered via URL.  Returned: success |
| **eventType**  string | The type of event to observe. For example: `providers/cloud.storage/eventTypes/object.change` and `providers/cloud.pubsub/eventTypes/topic.publish`.  Returned: success |
| **resource**  string | The resource(s) from which to observe events, for example, `projects/_/buckets/myBucket.` .  Returned: success |
| **service**  string | The hostname of the service that should be observed.  Returned: success |
| **httpsTrigger**  complex | An HTTPS endpoint type of source that can be triggered via URL.  Returned: success |
| **url**  string | The deployed url for the function.  Returned: success |
| **labels**  dictionary | A set of key/value label pairs associated with this Cloud Function.  Returned: success |
| **location**  string | The location of this cloud function.  Returned: success |
| **name**  string | A user-defined name of the function. Function names must be unique globally and match pattern `projects/\*/locations/\*/functions/\*`.  Returned: success |
| **runtime**  string | The runtime in which the function is going to run. If empty, defaults to Node.js 6.  Returned: success |
| **serviceAccountEmail**  string | The email of the service account for this function.  Returned: success |
| **sourceArchiveUrl**  string | The Google Cloud Storage URL, starting with gs://, pointing to the zip archive which contains the function.  Returned: success |
| **sourceRepository**  complex | The source repository where a function is hosted.  Returned: success |
| **deployedUrl**  string | The URL pointing to the hosted repository where the function were defined at the time of deployment.  Returned: success |
| **url**  string | The URL pointing to the hosted repository where the function is defined .  Returned: success |
| **sourceUploadUrl**  string | The Google Cloud Storage signed URL used for source uploading.  Returned: success |
| **status**  string | Status of the function deployment.  Returned: success |
| **timeout**  string | The function execution timeout. Execution is considered failed and can be terminated if the function is not completed at the end of the timeout period. Defaults to 60 seconds.  Returned: success |
| **trigger_http**  boolean | Use HTTP to trigger this function.  Returned: success |
| **updateTime**  string | The last update timestamp of a Cloud Function.  Returned: success |
| **versionId**  string | The version identifier of the Cloud Function. Each deployment attempt results in a new version of a function being created.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
