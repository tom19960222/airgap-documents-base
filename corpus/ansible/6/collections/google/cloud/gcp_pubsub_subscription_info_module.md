---
collection: ansible
version: "6"
title: "google.cloud.gcp_pubsub_subscription_info module – Gather info for GCP Subscription"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_pubsub_subscription_info_module.html
fetched_at: 2026-07-27T17:49:15+00:00
---
# google.cloud.gcp_pubsub_subscription_info module – Gather info for GCP Subscription

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
> see [Requirements](gcp_pubsub_subscription_info_module.md#ansible-collections-google-cloud-gcp-pubsub-subscription-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_pubsub_subscription_info`.

- [Synopsis](gcp_pubsub_subscription_info_module.md#synopsis)
- [Requirements](gcp_pubsub_subscription_info_module.md#requirements)
- [Parameters](gcp_pubsub_subscription_info_module.md#parameters)
- [Notes](gcp_pubsub_subscription_info_module.md#notes)
- [Examples](gcp_pubsub_subscription_info_module.md#examples)
- [Return Values](gcp_pubsub_subscription_info_module.md#return-values)

## [Synopsis](gcp_pubsub_subscription_info_module.md#id1)

- Gather info for GCP Subscription

## [Requirements](gcp_pubsub_subscription_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_pubsub_subscription_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |

## [Notes](gcp_pubsub_subscription_info_module.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_pubsub_subscription_info_module.md#id5)

```yaml+jinja
- name: get info on a subscription
  gcp_pubsub_subscription_info:
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_pubsub_subscription_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  Returned: always |
| **ackDeadlineSeconds**  integer | This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an outstanding message and will not be delivered again during that time (on a best-effort basis).  For pull subscriptions, this value is used as the initial value for the ack deadline. To override this value for a given message, call subscriptions.modifyAckDeadline with the corresponding ackId if using pull. The minimum custom deadline you can specify is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes).  If this parameter is 0, a default value of 10 seconds is used.  For push delivery, this value is also used to set the request timeout for the call to the push endpoint.  If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the message.  Returned: success |
| **deadLetterPolicy**  complex | A policy that specifies the conditions for dead lettering messages in this subscription. If dead_letter_policy is not set, dead lettering is disabled.  The Cloud Pub/Sub service account associated with this subscription’s parent project (i.e., [service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com](mailto:service-{project_number}%40gcp-sa-pubsub.iam.gserviceaccount.com)) must have permission to Acknowledge() messages on this subscription.  Returned: success |
| **deadLetterTopic**  string | The name of the topic to which dead letter messages should be published.  Format is `projects/{project}/topics/{topic}`.  The Cloud Pub/Sub service account associated with the enclosing subscription’s parent project (i.e., [service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com](mailto:service-{project_number}%40gcp-sa-pubsub.iam.gserviceaccount.com)) must have permission to Publish() to this topic.  The operation will fail if the topic does not exist.  Users should ensure that there is a subscription attached to this topic since messages published to a topic with no subscriptions are lost.  Returned: success |
| **maxDeliveryAttempts**  integer | The maximum number of delivery attempts for any message. The value must be between 5 and 100.  The number of delivery attempts is defined as 1 + (the sum of number of NACKs and number of times the acknowledgement deadline has been exceeded for the message).  A NACK is any call to ModifyAckDeadline with a 0 deadline. Note that client libraries may automatically extend ack_deadlines.  This field will be honored on a best effort basis.  If this parameter is 0, a default value of 5 is used.  Returned: success |
| **enableMessageOrdering**  boolean | If `true`, messages published with the same orderingKey in PubsubMessage will be delivered to the subscribers in the order in which they are received by the Pub/Sub system. Otherwise, they may be delivered in any order.  Returned: success |
| **expirationPolicy**  complex | A policy that specifies the conditions for this subscription’s expiration.  A subscription is considered active as long as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the subscription. If expirationPolicy is not set, a default policy with ttl of 31 days will be used. If it is set but ttl is “”, the resource never expires. The minimum allowed value for expirationPolicy.ttl is 1 day.  Returned: success |
| **ttl**  string | Specifies the “time-to-live” duration for an associated resource. The resource expires if it is not active for a period of ttl.  If ttl is not set, the associated resource never expires.  A duration in seconds with up to nine fractional digits, terminated by ‘s’.  Example - “3.5s”.  Returned: success |
| **filter**  string | The subscription only delivers the messages that match the filter. Pub/Sub automatically acknowledges the messages that don’t match the filter. You can filter messages by their attributes. The maximum length of a filter is 256 bytes. After creating the subscription, you can’t modify the filter.  Returned: success |
| **labels**  dictionary | A set of key/value label pairs to assign to this Subscription.  Returned: success |
| **messageRetentionDuration**  string | How long to retain unacknowledged messages in the subscription’s backlog, from the moment a message is published. If retainAckedMessages is true, then this also configures the retention of acknowledged messages, and thus configures how far back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot be more than 7 days (`”604800s”`) or less than 10 minutes (`”600s”`).  A duration in seconds with up to nine fractional digits, terminated by ‘s’. Example: `”600.5s”`.  Returned: success |
| **name**  string | Name of the subscription.  Returned: success |
| **pushConfig**  complex | If push delivery is used with this subscription, this field is used to configure it. An empty pushConfig signifies that the subscriber will pull and ack messages using API methods.  Returned: success |
| **attributes**  dictionary | Endpoint configuration attributes.  Every endpoint has a set of API supported attributes that can be used to control different aspects of the message delivery.  The currently supported attribute is x-goog-version, which you can use to change the format of the pushed message. This attribute indicates the version of the data expected by the endpoint. This controls the shape of the pushed message (i.e., its fields and metadata). The endpoint version is based on the version of the Pub/Sub API.  If not present during the subscriptions.create call, it will default to the version of the API used to make such call. If not present during a subscriptions.modifyPushConfig call, its value will not be changed. subscriptions.get calls will always return a valid version, even if the subscription was created without this attribute.  The possible values for this attribute are: - v1beta1: uses the push format defined in the v1beta1 Pub/Sub API.   - v1 or v1beta2: uses the push format defined in the v1 Pub/Sub API.   Returned: success |
| **oidcToken**  complex | If specified, Pub/Sub will generate and attach an OIDC JWT token as an Authorization header in the HTTP request for every pushed message.  Returned: success |
| **audience**  string | Audience to be used when generating OIDC token. The audience claim identifies the recipients that the JWT is intended for. The audience value is a single case-sensitive string. Having multiple values (array) for the audience field is not supported. More info about the OIDC JWT token audience here: <https://tools.ietf.org/html/rfc7519#section-4.1.3> Note: if not specified, the Push endpoint URL will be used.  Returned: success |
| **serviceAccountEmail**  string | Service account email to be used for generating the OIDC token.  The caller (for subscriptions.create, subscriptions.patch, and subscriptions.modifyPushConfig RPCs) must have the iam.serviceAccounts.actAs permission for the service account.  Returned: success |
| **pushEndpoint**  string | A URL locating the endpoint to which messages should be pushed.  For example, a Webhook endpoint might use “<https://example.com/push%22>.  Returned: success |
| **retainAckedMessages**  boolean | Indicates whether to retain acknowledged messages. If `true`, then messages are not expunged from the subscription’s backlog, even if they are acknowledged, until they fall out of the messageRetentionDuration window.  Returned: success |
| **retryPolicy**  complex | A policy that specifies how Pub/Sub retries message delivery for this subscription.  If not set, the default retry policy is applied. This generally implies that messages will be retried as soon as possible for healthy subscribers. RetryPolicy will be triggered on NACKs or acknowledgement deadline exceeded events for a given message .  Returned: success |
| **maximumBackoff**  string | The maximum delay between consecutive deliveries of a given message. Value should be between 0 and 600 seconds. Defaults to 600 seconds. A duration in seconds with up to nine fractional digits, terminated by ‘s’. Example: “3.5s”.  Returned: success |
| **minimumBackoff**  string | The minimum delay between consecutive deliveries of a given message. Value should be between 0 and 600 seconds. Defaults to 10 seconds.  A duration in seconds with up to nine fractional digits, terminated by ‘s’. Example: “3.5s”.  Returned: success |
| **topic**  dictionary | A reference to a Topic resource.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
