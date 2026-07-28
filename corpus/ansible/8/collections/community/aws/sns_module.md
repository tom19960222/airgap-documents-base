---
collection: ansible
version: "8"
title: "community.aws.sns module – Send Amazon Simple Notification Service messages"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/sns_module.html
fetched_at: 2026-07-28T01:41:55+00:00
---
# community.aws.sns module – Send Amazon Simple Notification Service messages

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
> see [Requirements](sns_module.md#ansible-collections-community-aws-sns-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.sns`.

New in community.aws 1.0.0

- [Synopsis](sns_module.md#synopsis)
- [Requirements](sns_module.md#requirements)
- [Parameters](sns_module.md#parameters)
- [Notes](sns_module.md#notes)
- [Examples](sns_module.md#examples)
- [Return Values](sns_module.md#return-values)

## [Synopsis](sns_module.md#id1)

- Sends a notification to a topic on your Amazon SNS account.

## [Requirements](sns_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](sns_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **application**  string | Message to send to application subscriptions. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **email**  string | Message to send to email subscriptions. |
| **email_json**  string | Message to send to email-json subscriptions. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **http**  string | Message to send to HTTP subscriptions. |
| **https**  string | Message to send to HTTPS subscriptions. |
| **lambda**  string | Message to send to Lambda subscriptions. |
| **message_attributes**  dictionary | Dictionary of message attributes. These are optional structured data entries to be sent along to the endpoint.  This is in AWS’s distinct Name/Type/Value format; see example below. |
| **message_deduplication_id**  string  *added in community.aws 5.4.0* | Only in connection with the message_group_id.  Overwrites the auto generated MessageDeduplicationId.  Can contain up to 128 alphanumeric characters and punctuation.  Messages with the same deduplication id getting recognized as the same message.  Gets overwritten by an auto generated token, if the topic has ContentBasedDeduplication set. |
| **message_group_id**  string  *added in community.aws 5.4.0* | A tag which is used to process messages that belong to the same group in a FIFO manner.  Has to be included when publishing a message to a fifo topic.  Can contain up to 128 alphanumeric characters and punctuation. |
| **message_structure**  string | The payload format to use for the message.  This must be `json` to support protocol-specific messages (`http`, `https`, `email`, `sms`, `sqs`).  It must be `string` to support *message_attributes*.  **Choices:**   - `"json"` ← (default) - `"string"` |
| **msg**  aliases: default  string / required | Default message for subscriptions without a more specific message. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **sms**  string | Message to send to SMS subscriptions. |
| **sqs**  string | Message to send to SQS subscriptions. |
| **subject**  string | Message subject |
| **topic**  string / required | The name or ARN of the topic to publish to. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](sns_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](sns_module.md#id5)

```yaml+jinja
- name: Send default notification message via SNS
  community.aws.sns:
    msg: '{{ inventory_hostname }} has completed the play.'
    subject: Deploy complete!
    topic: deploy
  delegate_to: localhost

- name: Send notification messages via SNS with short message for SMS
  community.aws.sns:
    msg: '{{ inventory_hostname }} has completed the play.'
    sms: deployed!
    subject: Deploy complete!
    topic: deploy
  delegate_to: localhost

- name: Send message with message_attributes
  community.aws.sns:
    topic: "deploy"
    msg: "message with extra details!"
    message_attributes:
      channel:
        data_type: String
        string_value: "mychannel"
      color:
        data_type: String
        string_value: "green"
  delegate_to: localhost

- name: Send message to a fifo topic
  community.aws.sns:
    topic: "deploy"
    msg: "Message with message group id"
    subject: Deploy complete!
    message_group_id: "deploy-1"
  delegate_to: localhost
```

## [Return Values](sns_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **message_id**  string | The message ID of the submitted message  **Returned:** when success  **Sample:** `"2f681ef0-6d76-5c94-99b2-4ae3996ce57b"` |
| **msg**  string | Human-readable diagnostic information  **Returned:** always  **Sample:** `"OK"` |
| **sequence_number**  string | A 128 bits long sequence number which gets assigned to the message in fifo topics  **Returned:** when success |

### Authors

- Michael J. Schultz (@mjschultz)
- Paul Arthur (@flowerysong)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
