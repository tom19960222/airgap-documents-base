---
collection: ansible
version: "8"
title: "community.aws.ses_identity module – Manages SES email and domain identity"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/ses_identity_module.html
fetched_at: 2026-07-28T01:41:53+00:00
---
# community.aws.ses_identity module – Manages SES email and domain identity

> **Note:**
>
> This module is part of the [community.aws collection](https://galaxy.ansible.com/ui/repo/published/community/aws/) (version 6.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](ses_identity_module.md#ansible-collections-community-aws-ses-identity-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ses_identity`.

New in community.aws 1.0.0

- [Synopsis](ses_identity_module.md#synopsis)
- [Requirements](ses_identity_module.md#requirements)
- [Parameters](ses_identity_module.md#parameters)
- [Notes](ses_identity_module.md#notes)
- [Examples](ses_identity_module.md#examples)
- [Return Values](ses_identity_module.md#return-values)

## [Synopsis](ses_identity_module.md#id1)

- This module allows the user to manage verified email and domain identity for SES.
- This covers verifying and removing identities as well as setting up complaint, bounce and delivery notification settings.
- Prior to release 5.0.0 this module was called `community.aws.aws_ses_identity`. The usage did not change.

Aliases: aws_ses_identity

## [Requirements](ses_identity_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ses_identity_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **bounce_notifications**  dictionary | Setup the SNS topic used to report bounce notifications.  If omitted, bounce notifications will not be delivered to a SNS topic.  If bounce notifications are not delivered to a SNS topic, *feedback_forwarding* must be enabled. |
| **include_headers**  boolean | Whether or not to include headers when delivering to the SNS topic.  If *topic* is not specified this will have no impact, but the SES setting is updated even if there is no topic.  **Choices:**   - `false` ← (default) - `true` |
| **topic**  string | The ARN of the topic to send notifications to.  If omitted, notifications will not be delivered to a SNS topic. |
| **complaint_notifications**  dictionary | Setup the SNS topic used to report complaint notifications.  If omitted, complaint notifications will not be delivered to a SNS topic.  If complaint notifications are not delivered to a SNS topic, *feedback_forwarding* must be enabled. |
| **include_headers**  boolean | Whether or not to include headers when delivering to the SNS topic.  If *topic* is not specified this will have no impact, but the SES setting is updated even if there is no topic.  **Choices:**   - `false` ← (default) - `true` |
| **topic**  string | The ARN of the topic to send notifications to.  If omitted, notifications will not be delivered to a SNS topic. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **delivery_notifications**  dictionary | Setup the SNS topic used to report delivery notifications.  If omitted, delivery notifications will not be delivered to a SNS topic. |
| **include_headers**  boolean | Whether or not to include headers when delivering to the SNS topic.  If *topic* is not specified this will have no impact, but the SES setting is updated even if there is no topic.  **Choices:**   - `false` ← (default) - `true` |
| **topic**  string | The ARN of the topic to send notifications to.  If omitted, notifications will not be delivered to a SNS topic. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **feedback_forwarding**  boolean | Whether or not to enable feedback forwarding.  This can only be false if both *bounce_notifications* and *complaint_notifications* specify SNS topics.  **Choices:**   - `false` - `true` ← (default) |
| **identity**  string / required | This is the email address or domain to verify / delete.  If this contains an ‘@’ then it will be considered an email. Otherwise it will be considered a domain. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Whether to create(or update) or delete the identity.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ses_identity_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ses_identity_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Ensure example@example.com email identity exists
  community.aws.ses_identity:
    identity: example@example.com
    state: present

- name: Delete example@example.com email identity
  community.aws.ses_identity:
    email: example@example.com
    state: absent

- name: Ensure example.com domain identity exists
  community.aws.ses_identity:
    identity: example.com
    state: present

# Create an SNS topic and send bounce and complaint notifications to it
# instead of emailing the identity owner
- name: Ensure complaints-topic exists
  community.aws.sns_topic:
    name: "complaints-topic"
    state: present
    purge_subscriptions: False
  register: topic_info

- name: Deliver feedback to topic instead of owner email
  community.aws.ses_identity:
    identity: example@example.com
    state: present
    complaint_notifications:
      topic: "{{ topic_info.sns_arn }}"
      include_headers: True
    bounce_notifications:
      topic: "{{ topic_info.sns_arn }}"
      include_headers: False
    feedback_forwarding: False

# Create an SNS topic for delivery notifications and leave complaints
# Being forwarded to the identity owner email
- name: Ensure delivery-notifications-topic exists
  community.aws.sns_topic:
    name: "delivery-notifications-topic"
    state: present
    purge_subscriptions: False
  register: topic_info

- name: Delivery notifications to topic
  community.aws.ses_identity:
    identity: example@example.com
    state: present
    delivery_notifications:
      topic: "{{ topic_info.sns_arn }}"
```

## [Return Values](ses_identity_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **identity**  string | The identity being modified.  **Returned:** success  **Sample:** `"example@example.com"` |
| **identity_arn**  string | The arn of the identity being modified.  **Returned:** success  **Sample:** `"arn:aws:ses:us-east-1:12345678:identity/example@example.com"` |
| **notification_attributes**  complex | The notification setup for the identity.  **Returned:** success  **Sample:** `{"bounce_topic": "arn:aws:sns:....", "complaint_topic": "arn:aws:sns:....", "delivery_topic": "arn:aws:sns:....", "forwarding_enabled": false, "headers_in_bounce_notifications_enabled": true, "headers_in_complaint_notifications_enabled": true, "headers_in_delivery_notifications_enabled": true}` |
| **bounce_topic**  string | The ARN of the topic bounce notifications are delivered to.  Omitted if bounce notifications are not delivered to a topic.  **Returned:** success |
| **complaint_topic**  string | The ARN of the topic complaint notifications are delivered to.  Omitted if complaint notifications are not delivered to a topic.  **Returned:** success |
| **delivery_topic**  string | The ARN of the topic delivery notifications are delivered to.  Omitted if delivery notifications are not delivered to a topic.  **Returned:** success |
| **forwarding_enabled**  boolean | Whether or not feedback forwarding is enabled.  **Returned:** success |
| **headers_in_bounce_notifications_enabled**  boolean | Whether or not headers are included in messages delivered to the bounce topic.  **Returned:** success |
| **headers_in_complaint_notifications_enabled**  boolean | Whether or not headers are included in messages delivered to the complaint topic.  **Returned:** success |
| **headers_in_delivery_notifications_enabled**  boolean | Whether or not headers are included in messages delivered to the delivery topic.  **Returned:** success |
| **verification_attributes**  complex | The verification information for the identity.  **Returned:** success  **Sample:** `{"verification_status": "Pending", "verification_token": "...."}` |
| **verification_status**  string | The verification status of the identity.  **Returned:** success  **Sample:** `"Pending"` |
| **verification_token**  string | The verification token for a domain identity.  **Returned:** success |

### Authors

- Ed Costello (@orthanc)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
