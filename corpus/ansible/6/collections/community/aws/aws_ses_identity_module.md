---
collection: ansible
version: "6"
title: "community.aws.aws_ses_identity module – Manages SES email and domain identity"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_ses_identity_module.html
fetched_at: 2026-07-27T17:03:33+00:00
---
# community.aws.aws_ses_identity module – Manages SES email and domain identity

> **Note:**
>
> This module is part of the [community.aws collection](https://galaxy.ansible.com/community/aws) (version 3.6.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](aws_ses_identity_module.md#ansible-collections-community-aws-aws-ses-identity-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_ses_identity`.

New in community.aws 1.0.0

- [Synopsis](aws_ses_identity_module.md#synopsis)
- [Requirements](aws_ses_identity_module.md#requirements)
- [Parameters](aws_ses_identity_module.md#parameters)
- [Notes](aws_ses_identity_module.md#notes)
- [Examples](aws_ses_identity_module.md#examples)
- [Return Values](aws_ses_identity_module.md#return-values)

## [Synopsis](aws_ses_identity_module.md#id1)

- This module allows the user to manage verified email and domain identity for SES.
- This covers verifying and removing identities as well as setting up complaint, bounce and delivery notification settings.

## [Requirements](aws_ses_identity_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_ses_identity_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **bounce_notifications**  dictionary | Setup the SNS topic used to report bounce notifications.  If omitted, bounce notifications will not be delivered to a SNS topic.  If bounce notifications are not delivered to a SNS topic, *feedback_forwarding* must be enabled. |
| **include_headers**  boolean | Whether or not to include headers when delivering to the SNS topic.  If *topic* is not specified this will have no impact, but the SES setting is updated even if there is no topic.  Choices:   - `false` ← (default) - `true` |
| **topic**  string | The ARN of the topic to send notifications to.  If omitted, notifications will not be delivered to a SNS topic. |
| **complaint_notifications**  dictionary | Setup the SNS topic used to report complaint notifications.  If omitted, complaint notifications will not be delivered to a SNS topic.  If complaint notifications are not delivered to a SNS topic, *feedback_forwarding* must be enabled. |
| **include_headers**  boolean | Whether or not to include headers when delivering to the SNS topic.  If *topic* is not specified this will have no impact, but the SES setting is updated even if there is no topic.  Choices:   - `false` ← (default) - `true` |
| **topic**  string | The ARN of the topic to send notifications to.  If omitted, notifications will not be delivered to a SNS topic. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **delivery_notifications**  dictionary | Setup the SNS topic used to report delivery notifications.  If omitted, delivery notifications will not be delivered to a SNS topic. |
| **include_headers**  boolean | Whether or not to include headers when delivering to the SNS topic.  If *topic* is not specified this will have no impact, but the SES setting is updated even if there is no topic.  Choices:   - `false` ← (default) - `true` |
| **topic**  string | The ARN of the topic to send notifications to.  If omitted, notifications will not be delivered to a SNS topic. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **feedback_forwarding**  boolean | Whether or not to enable feedback forwarding.  This can only be false if both *bounce_notifications* and *complaint_notifications* specify SNS topics.  Choices:   - `false` - `true` ← (default) |
| **identity**  string / required | This is the email address or domain to verify / delete.  If this contains an ‘@’ then it will be considered an email. Otherwise it will be considered a domain. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Whether to create(or update) or delete the identity.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](aws_ses_identity_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_ses_identity_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Ensure example@example.com email identity exists
  community.aws.aws_ses_identity:
    identity: example@example.com
    state: present

- name: Delete example@example.com email identity
  community.aws.aws_ses_identity:
    email: example@example.com
    state: absent

- name: Ensure example.com domain identity exists
  community.aws.aws_ses_identity:
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
  community.aws.aws_ses_identity:
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
  community.aws.aws_ses_identity:
    identity: example@example.com
    state: present
    delivery_notifications:
      topic: "{{ topic_info.sns_arn }}"
```

## [Return Values](aws_ses_identity_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **identity**  string | The identity being modified.  Returned: success  Sample: `"example@example.com"` |
| **identity_arn**  string | The arn of the identity being modified.  Returned: success  Sample: `"arn:aws:ses:us-east-1:12345678:identity/example@example.com"` |
| **notification_attributes**  complex | The notification setup for the identity.  Returned: success  Sample: `{"bounce_topic": "arn:aws:sns:....", "complaint_topic": "arn:aws:sns:....", "delivery_topic": "arn:aws:sns:....", "forwarding_enabled": false, "headers_in_bounce_notifications_enabled": true, "headers_in_complaint_notifications_enabled": true, "headers_in_delivery_notifications_enabled": true}` |
| **bounce_topic**  string | The ARN of the topic bounce notifications are delivered to.  Omitted if bounce notifications are not delivered to a topic.  Returned: success |
| **complaint_topic**  string | The ARN of the topic complaint notifications are delivered to.  Omitted if complaint notifications are not delivered to a topic.  Returned: success |
| **delivery_topic**  string | The ARN of the topic delivery notifications are delivered to.  Omitted if delivery notifications are not delivered to a topic.  Returned: success |
| **forwarding_enabled**  boolean | Whether or not feedback forwarding is enabled.  Returned: success |
| **headers_in_bounce_notifications_enabled**  boolean | Whether or not headers are included in messages delivered to the bounce topic.  Returned: success |
| **headers_in_complaint_notifications_enabled**  boolean | Whether or not headers are included in messages delivered to the complaint topic.  Returned: success |
| **headers_in_delivery_notifications_enabled**  boolean | Whether or not headers are included in messages delivered to the delivery topic.  Returned: success |
| **verification_attributes**  complex | The verification information for the identity.  Returned: success  Sample: `{"verification_status": "Pending", "verification_token": "...."}` |
| **verification_status**  string | The verification status of the identity.  Returned: success  Sample: `"Pending"` |
| **verification_token**  string | The verification token for a domain identity.  Returned: success |

### Authors

- Ed Costello (@orthanc)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
