---
collection: ansible
version: "6"
title: "community.aws.sns_topic module – Manages AWS SNS topics and subscriptions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/sns_topic_module.html
fetched_at: 2026-07-27T17:05:06+00:00
---
# community.aws.sns_topic module – Manages AWS SNS topics and subscriptions

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
> see [Requirements](sns_topic_module.md#ansible-collections-community-aws-sns-topic-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.sns_topic`.

New in community.aws 1.0.0

- [Synopsis](sns_topic_module.md#synopsis)
- [Requirements](sns_topic_module.md#requirements)
- [Parameters](sns_topic_module.md#parameters)
- [Notes](sns_topic_module.md#notes)
- [Examples](sns_topic_module.md#examples)
- [Return Values](sns_topic_module.md#return-values)

## [Synopsis](sns_topic_module.md#id1)

- The [community.aws.sns_topic](sns_topic_module.md#ansible-collections-community-aws-sns-topic-module) module allows you to create, delete, and manage subscriptions for AWS SNS topics.
- As of 2.6, this module can be use to subscribe and unsubscribe to topics outside of your AWS account.

## [Requirements](sns_topic_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](sns_topic_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **delivery_policy**  dictionary | Delivery policy to apply to the SNS topic. |
| **http**  dictionary | Delivery policy for HTTP(S) messages.  See <https://docs.aws.amazon.com/sns/latest/dg/sns-message-delivery-retries.html> for more information. |
| **defaultHealthyRetryPolicy**  dictionary / required | Retry policy for HTTP(S) messages. |
| **backoffFunction**  string / required | The function for backoff between retries.  Choices:   - `"arithmetic"` - `"exponential"` - `"geometric"` - `"linear"` |
| **maxDelayTarget**  integer / required | The maximum delay for a retry. |
| **minDelayTarget**  integer / required | The minimum delay for a retry. |
| **numMaxDelayRetries**  integer / required | The number of retries with the maximum delay between them. |
| **numMinDelayRetries**  integer / required | The number of retries with just the minimum delay between them. |
| **numNoDelayRetries**  integer / required | The number of retries to be performmed immediately. |
| **numRetries**  integer / required | The total number of retries. |
| **defaultThrottlePolicy**  dictionary | Throttle the rate of messages sent to subsriptions. |
| **maxReceivesPerSecond**  integer / required | The maximum number of deliveries per second per subscription. |
| **disableSubscriptionOverrides**  boolean | Applies this policy to all subscriptions, even if they have their own policies.  Choices:   - `false` - `true` |
| **display_name**  string | Display name of the topic. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **name**  string / required | The name or ARN of the SNS topic to manage. |
| **policy**  dictionary | Policy to apply to the SNS topic.  Policy body can be YAML or JSON.  This is required for certain use cases for example with S3 bucket notifications. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_subscriptions**  boolean | Whether to purge any subscriptions not listed here. NOTE: AWS does not allow you to purge any PendingConfirmation subscriptions, so if any exist and would be purged, they are silently skipped. This means that somebody could come back later and confirm the subscription. Sorry. Blame Amazon.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Whether to create or destroy an SNS topic.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subscriptions**  list / elements=dictionary | List of subscriptions to apply to the topic. Note that AWS requires subscriptions to be confirmed, so you will need to confirm any new subscriptions.  Default: `[]` |
| **endpoint**  string / required | Endpoint of subscription. |
| **protocol**  string / required | Protocol of subscription. |
| **topic_type**  string  added in community.aws 2.0.0 | The type of topic that should be created. Either Standard for FIFO (first-in, first-out)  Choices:   - `"standard"` ← (default) - `"fifo"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](sns_topic_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](sns_topic_module.md#id5)

```yaml+jinja
- name: Create alarm SNS topic
  community.aws.sns_topic:
    name: "alarms"
    state: present
    display_name: "alarm SNS topic"
    delivery_policy:
      http:
        defaultHealthyRetryPolicy:
          minDelayTarget: 2
          maxDelayTarget: 4
          numRetries: 9
          numMaxDelayRetries: 5
          numMinDelayRetries: 2
          numNoDelayRetries: 2
          backoffFunction: "linear"
        disableSubscriptionOverrides: True
        defaultThrottlePolicy:
          maxReceivesPerSecond: 10
    subscriptions:
      - endpoint: "my_email_address@example.com"
        protocol: "email"
      - endpoint: "my_mobile_number"
        protocol: "sms"

- name: Create a topic permitting S3 bucket notifications
  community.aws.sns_topic:
    name: "S3Notifications"
    state: present
    display_name: "S3 notifications SNS topic"
    policy:
      Id: s3-topic-policy
      Version: 2012-10-17
      Statement:
        - Sid: Statement-id
          Effect: Allow
          Resource: "arn:aws:sns:*:*:S3Notifications"
          Principal:
            Service: s3.amazonaws.com
          Action: sns:Publish
          Condition:
            ArnLike:
              aws:SourceArn: "arn:aws:s3:*:*:SomeBucket"

- name: Example deleting a topic
  community.aws.sns_topic:
    name: "ExampleTopic"
    state: absent
```

## [Return Values](sns_topic_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **sns_arn**  string | The ARN of the topic you are modifying  Returned: always  Sample: `"arn:aws:sns:us-east-2:111111111111:my_topic_name"` |
| **sns_topic**  complex | Dict of sns topic details  Returned: always |
| **attributes_set**  list / elements=string | list of attributes set during this run  Returned: always  Sample: `[]` |
| **check_mode**  boolean | whether check mode was on  Returned: always  Sample: `false` |
| **delivery_policy**  string | Delivery policy for the SNS topic  Returned: when topic is owned by this AWS account  Sample: `"{\"http\":{\"defaultHealthyRetryPolicy\":{\"minDelayTarget\":20,\"maxDelayTarget\":20,\"numRetries\":3,\"numMaxDelayRetries\":0, \"numNoDelayRetries\":0,\"numMinDelayRetries\":0,\"backoffFunction\":\"linear\"},\"disableSubscriptionOverrides\":false}}\n"` |
| **display_name**  string | Display name for SNS topic  Returned: when topic is owned by this AWS account  Sample: `"My topic name"` |
| **name**  string | Topic name  Returned: always  Sample: `"ansible-test-dummy-topic"` |
| **owner**  string | AWS account that owns the topic  Returned: when topic is owned by this AWS account  Sample: `"111111111111"` |
| **policy**  string | Policy for the SNS topic  Returned: when topic is owned by this AWS account  Sample: `"{\"Version\":\"2012-10-17\",\"Id\":\"SomePolicyId\",\"Statement\":[{\"Sid\":\"ANewSid\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::111111111111:root\"}, \"Action\":\"sns:Subscribe\",\"Resource\":\"arn:aws:sns:us-east-2:111111111111:ansible-test-dummy-topic\",\"Condition\":{\"StringEquals\":{\"sns:Protocol\":\"email\"}}}]}\n"` |
| **state**  string | whether the topic is present or absent  Returned: always  Sample: `"present"` |
| **subscriptions**  list / elements=string | List of subscribers to the topic in this AWS account  Returned: always  Sample: `[]` |
| **subscriptions_added**  list / elements=string | List of subscribers added in this run  Returned: always  Sample: `[]` |
| **subscriptions_confirmed**  string | Count of confirmed subscriptions  Returned: when topic is owned by this AWS account  Sample: `"0"` |
| **subscriptions_deleted**  string | Count of deleted subscriptions  Returned: when topic is owned by this AWS account  Sample: `"0"` |
| **subscriptions_existing**  list / elements=string | List of existing subscriptions  Returned: always  Sample: `[]` |
| **subscriptions_new**  list / elements=string | List of new subscriptions  Returned: always  Sample: `[]` |
| **subscriptions_pending**  string | Count of pending subscriptions  Returned: when topic is owned by this AWS account  Sample: `"0"` |
| **subscriptions_purge**  boolean | Whether or not purge_subscriptions was set  Returned: always  Sample: `true` |
| **topic_arn**  string | ARN of the SNS topic (equivalent to sns_arn)  Returned: when topic is owned by this AWS account  Sample: `"arn:aws:sns:us-east-2:111111111111:ansible-test-dummy-topic"` |
| **topic_created**  boolean | Whether the topic was created  Returned: always  Sample: `false` |
| **topic_deleted**  boolean | Whether the topic was deleted  Returned: always  Sample: `false` |

### Authors

- Joel Thompson (@joelthompson)
- Fernando Jose Pando (@nand0p)
- Will Thames (@willthames)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
