---
collection: ansible
version: "8"
title: "google.cloud.gcp_cloudtasks_queue module – Creates a GCP Queue"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_cloudtasks_queue_module.html
fetched_at: 2026-07-28T02:31:50+00:00
---
# google.cloud.gcp_cloudtasks_queue module – Creates a GCP Queue

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
> see [Requirements](gcp_cloudtasks_queue_module.md#ansible-collections-google-cloud-gcp-cloudtasks-queue-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_cloudtasks_queue`.

- [Synopsis](gcp_cloudtasks_queue_module.md#synopsis)
- [Requirements](gcp_cloudtasks_queue_module.md#requirements)
- [Parameters](gcp_cloudtasks_queue_module.md#parameters)
- [Examples](gcp_cloudtasks_queue_module.md#examples)
- [Return Values](gcp_cloudtasks_queue_module.md#return-values)

## [Synopsis](gcp_cloudtasks_queue_module.md#id1)

- A named resource to which messages are sent by publishers.

## [Requirements](gcp_cloudtasks_queue_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_cloudtasks_queue_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **app_engine_routing_override**  dictionary | Overrides for task-level appEngineRouting. These settings apply only to App Engine tasks in this queue . |
| **instance**  string | App instance.  By default, the task is sent to an instance which is available when the task is attempted. |
| **service**  string | App service.  By default, the task is sent to the service which is the default service when the task is attempted. |
| **version**  string | App version.  By default, the task is sent to the version which is the default version when the task is attempted. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **location**  string / required | The location of the queue. |
| **name**  string | The queue name. |
| **project**  string | The Google Cloud Platform project to use. |
| **rate_limits**  dictionary | Rate limits for task dispatches.  The queue’s actual dispatch rate is the result of: \* Number of tasks in the queue \* User-specified throttling: rateLimits, retryConfig, and the queue’s state.  \* System throttling due to 429 (Too Many Requests) or 503 (Service Unavailable) responses from the worker, high error rates, or to smooth sudden large traffic spikes. |
| **max_concurrent_dispatches**  integer | The maximum number of concurrent tasks that Cloud Tasks allows to be dispatched for this queue. After this threshold has been reached, Cloud Tasks stops dispatching tasks until the number of concurrent requests decreases. |
| **max_dispatches_per_second**  string | The maximum rate at which tasks are dispatched from this queue.  If unspecified when the queue is created, Cloud Tasks will pick the default. |
| **retry_config**  dictionary | Settings that determine the retry behavior. |
| **max_attempts**  integer | Number of attempts per task.  Cloud Tasks will attempt the task maxAttempts times (that is, if the first attempt fails, then there will be maxAttempts - 1 retries). Must be >= -1.  If unspecified when the queue is created, Cloud Tasks will pick the default.  -1 indicates unlimited attempts. |
| **max_backoff**  string | A task will be scheduled for retry between minBackoff and maxBackoff duration after it fails, if the queue’s RetryConfig specifies that the task should be retried. |
| **max_doublings**  integer | The time between retries will double maxDoublings times.  A task’s retry interval starts at minBackoff, then doubles maxDoublings times, then increases linearly, and finally retries retries at intervals of maxBackoff up to maxAttempts times. |
| **max_retry_duration**  string | If positive, maxRetryDuration specifies the time limit for retrying a failed task, measured from when the task was first attempted. Once maxRetryDuration time has passed and the task has been attempted maxAttempts times, no further attempts will be made and the task will be deleted.  If zero, then the task age is unlimited. |
| **min_backoff**  string | A task will be scheduled for retry between minBackoff and maxBackoff duration after it fails, if the queue’s RetryConfig specifies that the task should be retried. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **stackdriver_logging_config**  dictionary | Configuration options for writing logs to Stackdriver Logging. |
| **sampling_ratio**  string / required | Specifies the fraction of operations to write to Stackdriver Logging.  This field may contain any value between 0.0 and 1.0, inclusive. 0.0 is the default and means that no operations are logged. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **status**  string | The current state of the queue.  Some valid choices include: “RUNNING”, “PAUSED”, “DISABLED” |

## [Examples](gcp_cloudtasks_queue_module.md#id4)

```yaml+jinja
- name: create a queue
  google.cloud.gcp_cloudtasks_queue:
    name: test_object
    location: us-central1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_cloudtasks_queue_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **appEngineRoutingOverride**  complex | Overrides for task-level appEngineRouting. These settings apply only to App Engine tasks in this queue .  **Returned:** success |
| **host**  string | The host that the task is sent to.  **Returned:** success |
| **instance**  string | App instance.  By default, the task is sent to an instance which is available when the task is attempted.  **Returned:** success |
| **service**  string | App service.  By default, the task is sent to the service which is the default service when the task is attempted.  **Returned:** success |
| **version**  string | App version.  By default, the task is sent to the version which is the default version when the task is attempted.  **Returned:** success |
| **location**  string | The location of the queue.  **Returned:** success |
| **name**  string | The queue name.  **Returned:** success |
| **rateLimits**  complex | Rate limits for task dispatches.  The queue’s actual dispatch rate is the result of: \* Number of tasks in the queue \* User-specified throttling: rateLimits, retryConfig, and the queue’s state.  \* System throttling due to 429 (Too Many Requests) or 503 (Service Unavailable) responses from the worker, high error rates, or to smooth sudden large traffic spikes.  **Returned:** success |
| **maxBurstSize**  integer | The max burst size.  Max burst size limits how fast tasks in queue are processed when many tasks are in the queue and the rate is high. This field allows the queue to have a high rate so processing starts shortly after a task is enqueued, but still limits resource usage when many tasks are enqueued in a short period of time.  **Returned:** success |
| **maxConcurrentDispatches**  integer | The maximum number of concurrent tasks that Cloud Tasks allows to be dispatched for this queue. After this threshold has been reached, Cloud Tasks stops dispatching tasks until the number of concurrent requests decreases.  **Returned:** success |
| **maxDispatchesPerSecond**  string | The maximum rate at which tasks are dispatched from this queue.  If unspecified when the queue is created, Cloud Tasks will pick the default.  **Returned:** success |
| **retryConfig**  complex | Settings that determine the retry behavior.  **Returned:** success |
| **maxAttempts**  integer | Number of attempts per task.  Cloud Tasks will attempt the task maxAttempts times (that is, if the first attempt fails, then there will be maxAttempts - 1 retries). Must be >= -1.  If unspecified when the queue is created, Cloud Tasks will pick the default.  -1 indicates unlimited attempts.  **Returned:** success |
| **maxBackoff**  string | A task will be scheduled for retry between minBackoff and maxBackoff duration after it fails, if the queue’s RetryConfig specifies that the task should be retried.  **Returned:** success |
| **maxDoublings**  integer | The time between retries will double maxDoublings times.  A task’s retry interval starts at minBackoff, then doubles maxDoublings times, then increases linearly, and finally retries retries at intervals of maxBackoff up to maxAttempts times.  **Returned:** success |
| **maxRetryDuration**  string | If positive, maxRetryDuration specifies the time limit for retrying a failed task, measured from when the task was first attempted. Once maxRetryDuration time has passed and the task has been attempted maxAttempts times, no further attempts will be made and the task will be deleted.  If zero, then the task age is unlimited.  **Returned:** success |
| **minBackoff**  string | A task will be scheduled for retry between minBackoff and maxBackoff duration after it fails, if the queue’s RetryConfig specifies that the task should be retried.  **Returned:** success |
| **purgeTime**  string | The last time this queue was purged.  **Returned:** success |
| **stackdriverLoggingConfig**  complex | Configuration options for writing logs to Stackdriver Logging.  **Returned:** success |
| **samplingRatio**  string | Specifies the fraction of operations to write to Stackdriver Logging.  This field may contain any value between 0.0 and 1.0, inclusive. 0.0 is the default and means that no operations are logged.  **Returned:** success |
| **status**  string | The current state of the queue.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
