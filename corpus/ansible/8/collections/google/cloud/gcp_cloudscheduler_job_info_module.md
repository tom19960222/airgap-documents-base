---
collection: ansible
version: "8"
title: "google.cloud.gcp_cloudscheduler_job_info module – Gather info for GCP Job"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_cloudscheduler_job_info_module.html
fetched_at: 2026-07-28T02:31:49+00:00
---
# google.cloud.gcp_cloudscheduler_job_info module – Gather info for GCP Job

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
> see [Requirements](gcp_cloudscheduler_job_info_module.md#ansible-collections-google-cloud-gcp-cloudscheduler-job-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_cloudscheduler_job_info`.

- [Synopsis](gcp_cloudscheduler_job_info_module.md#synopsis)
- [Requirements](gcp_cloudscheduler_job_info_module.md#requirements)
- [Parameters](gcp_cloudscheduler_job_info_module.md#parameters)
- [Notes](gcp_cloudscheduler_job_info_module.md#notes)
- [Examples](gcp_cloudscheduler_job_info_module.md#examples)
- [Return Values](gcp_cloudscheduler_job_info_module.md#return-values)

## [Synopsis](gcp_cloudscheduler_job_info_module.md#id1)

- Gather info for GCP Job

## [Requirements](gcp_cloudscheduler_job_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_cloudscheduler_job_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string / required | Region where the scheduler job resides . |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |

## [Notes](gcp_cloudscheduler_job_info_module.md#id4)

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

## [Examples](gcp_cloudscheduler_job_info_module.md#id5)

```yaml+jinja
- name: get info on a job
  gcp_cloudscheduler_job_info:
    region: us-central1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_cloudscheduler_job_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  **Returned:** always |
| **appEngineHttpTarget**  complex | App Engine HTTP target.  If the job providers a App Engine HTTP target the cron will send a request to the service instance .  **Returned:** success |
| **appEngineRouting**  complex | App Engine Routing setting for the job.  **Returned:** success |
| **instance**  string | App instance.  By default, the job is sent to an instance which is available when the job is attempted.  **Returned:** success |
| **service**  string | App service.  By default, the job is sent to the service which is the default service when the job is attempted.  **Returned:** success |
| **version**  string | App version.  By default, the job is sent to the version which is the default version when the job is attempted.  **Returned:** success |
| **body**  string | HTTP request body. A request body is allowed only if the HTTP method is POST or PUT. It will result in invalid argument error to set a body on a job with an incompatible HttpMethod.  A base64-encoded string.  **Returned:** success |
| **headers**  dictionary | HTTP request headers.  This map contains the header field names and values. Headers can be set when the job is created.  **Returned:** success |
| **httpMethod**  string | Which HTTP method to use for the request.  **Returned:** success |
| **relativeUri**  string | The relative URI.  **Returned:** success |
| **attemptDeadline**  string | The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud Scheduler will retry the job according to the RetryConfig.  The allowed duration for this deadline is: \* For HTTP targets, between 15 seconds and 30 minutes.  \* For App Engine HTTP targets, between 15 seconds and 24 hours.  \* \*\*Note\*\*: For PubSub targets, this field is ignored - setting it will introduce an unresolvable diff.  A duration in seconds with up to nine fractional digits, terminated by ‘s’. Example: “3.5s” .  **Returned:** success |
| **description**  string | A human-readable description for the job. This string must not contain more than 500 characters.  **Returned:** success |
| **httpTarget**  complex | HTTP target.  If the job providers a http_target the cron will send a request to the targeted url .  **Returned:** success |
| **body**  string | HTTP request body. A request body is allowed only if the HTTP method is POST, PUT, or PATCH. It is an error to set body on a job with an incompatible HttpMethod.  A base64-encoded string.  **Returned:** success |
| **headers**  dictionary | This map contains the header field names and values. Repeated headers are not supported, but a header value can contain commas.  **Returned:** success |
| **httpMethod**  string | Which HTTP method to use for the request.  **Returned:** success |
| **oauthToken**  complex | Contains information needed for generating an OAuth token.  This type of authorization should be used when sending requests to a GCP endpoint.  **Returned:** success |
| **scope**  string | OAuth scope to be used for generating OAuth access token. If not specified, “<https://www.googleapis.com/auth/cloud-platform%22> will be used.  **Returned:** success |
| **serviceAccountEmail**  string | Service account email to be used for generating OAuth token.  The service account must be within the same project as the job.  **Returned:** success |
| **oidcToken**  complex | Contains information needed for generating an OpenID Connect token.  This type of authorization should be used when sending requests to third party endpoints or Cloud Run.  **Returned:** success |
| **audience**  string | Audience to be used when generating OIDC token. If not specified, the URI specified in target will be used.  **Returned:** success |
| **serviceAccountEmail**  string | Service account email to be used for generating OAuth token.  The service account must be within the same project as the job.  **Returned:** success |
| **uri**  string | The full URI path that the request will be sent to.  **Returned:** success |
| **name**  string | The name of the job.  **Returned:** success |
| **pubsubTarget**  complex | Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic .  **Returned:** success |
| **attributes**  dictionary | Attributes for PubsubMessage.  Pubsub message must contain either non-empty data, or at least one attribute.  **Returned:** success |
| **data**  string | The message payload for PubsubMessage.  Pubsub message must contain either non-empty data, or at least one attribute.  A base64-encoded string.  **Returned:** success |
| **topicName**  string | The full resource name for the Cloud Pub/Sub topic to which messages will be published when a job is delivered. ~>\*\*NOTE:\*\* The topic name must be in the same format as required by PubSub’s PublishRequest.name, e.g. `projects/my-project/topics/my-topic`.  **Returned:** success |
| **region**  string | Region where the scheduler job resides .  **Returned:** success |
| **retryConfig**  complex | By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler, then it will be retried with exponential backoff according to the settings .  **Returned:** success |
| **maxBackoffDuration**  string | The maximum amount of time to wait before retrying a job after it fails.  A duration in seconds with up to nine fractional digits, terminated by ‘s’.  **Returned:** success |
| **maxDoublings**  integer | The time between retries will double maxDoublings times.  A job’s retry interval starts at minBackoffDuration, then doubles maxDoublings times, then increases linearly, and finally retries retries at intervals of maxBackoffDuration up to retryCount times.  **Returned:** success |
| **maxRetryDuration**  string | The time limit for retrying a failed job, measured from time when an execution was first attempted. If specified with retryCount, the job will be retried until both limits are reached.  A duration in seconds with up to nine fractional digits, terminated by ‘s’.  **Returned:** success |
| **minBackoffDuration**  string | The minimum amount of time to wait before retrying a job after it fails.  A duration in seconds with up to nine fractional digits, terminated by ‘s’.  **Returned:** success |
| **retryCount**  integer | The number of attempts that the system will make to run a job using the exponential backoff procedure described by maxDoublings.  Values greater than 5 and negative values are not allowed.  **Returned:** success |
| **schedule**  string | Describes the schedule on which the job will be executed.  **Returned:** success |
| **timeZone**  string | Specifies the time zone to be used in interpreting schedule.  The value of this field must be a time zone name from the tz database.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
