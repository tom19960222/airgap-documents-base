---
collection: ansible
version: "6"
title: "community.aws.sns module – Send Amazon Simple Notification Service messages"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/sns_module.html
fetched_at: 2026-07-27T17:05:05+00:00
---
# community.aws.sns module – Send Amazon Simple Notification Service messages

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
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](sns_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **application**  string | Message to send to application subscriptions. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **email**  string | Message to send to email subscriptions. |
| **email_json**  string | Message to send to email-json subscriptions. |
| **http**  string | Message to send to HTTP subscriptions. |
| **https**  string | Message to send to HTTPS subscriptions. |
| **lambda**  string | Message to send to Lambda subscriptions. |
| **message_attributes**  dictionary | Dictionary of message attributes. These are optional structured data entries to be sent along to the endpoint.  This is in AWS’s distinct Name/Type/Value format; see example below. |
| **message_structure**  string | The payload format to use for the message.  This must be ‘json’ to support protocol-specific messages (`http`, `https`, `email`, `sms`, `sqs`).  It must be ‘string’ to support *message_attributes*.  Choices:   - `"json"` ← (default) - `"string"` |
| **msg**  aliases: default  string / required | Default message for subscriptions without a more specific message. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **sms**  string | Message to send to SMS subscriptions. |
| **sqs**  string | Message to send to SQS subscriptions. |
| **subject**  string | Message subject |
| **topic**  string / required | The name or ARN of the topic to publish to. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](sns_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

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
```

## [Return Values](sns_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **message_id**  string | The message ID of the submitted message  Returned: when success  Sample: `"2f681ef0-6d76-5c94-99b2-4ae3996ce57b"` |
| **msg**  string | Human-readable diagnostic information  Returned: always  Sample: `"OK"` |

### Authors

- Michael J. Schultz (@mjschultz)
- Paul Arthur (@flowerysong)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
