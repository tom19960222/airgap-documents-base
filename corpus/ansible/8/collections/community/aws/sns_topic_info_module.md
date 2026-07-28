---
collection: ansible
version: "8"
title: "community.aws.sns_topic_info module – sns_topic_info module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/sns_topic_info_module.html
fetched_at: 2026-07-28T01:41:57+00:00
---
# community.aws.sns_topic_info module – sns_topic_info module

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
> see [Requirements](sns_topic_info_module.md#ansible-collections-community-aws-sns-topic-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.sns_topic_info`.

New in community.aws 3.2.0

- [Synopsis](sns_topic_info_module.md#synopsis)
- [Requirements](sns_topic_info_module.md#requirements)
- [Parameters](sns_topic_info_module.md#parameters)
- [Notes](sns_topic_info_module.md#notes)
- [Examples](sns_topic_info_module.md#examples)
- [Return Values](sns_topic_info_module.md#return-values)

## [Synopsis](sns_topic_info_module.md#id1)

- The [community.aws.sns_topic_info](sns_topic_info_module.md#ansible-collections-community-aws-sns-topic-info-module) module allows to get all AWS SNS topics or properties of a specific AWS SNS topic.

## [Requirements](sns_topic_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](sns_topic_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **topic_arn**  string | The ARN of the AWS SNS topic for which you wish to find subscriptions or list attributes. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](sns_topic_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](sns_topic_info_module.md#id5)

```yaml+jinja
- name: list all the topics
  community.aws.sns_topic_info:
  register: sns_topic_list

- name: get info on specific topic
  community.aws.sns_topic_info:
    topic_arn: "{{ sns_arn }}"
  register: sns_topic_info
```

## [Return Values](sns_topic_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  list / elements=string | The result contaning the details of one or all AWS SNS topics.  **Returned:** success |
| **sns_arn**  string | The ARN of the topic.  **Returned:** always  **Sample:** `"arn:aws:sns:us-east-2:123456789012:my_topic_name"` |
| **sns_topic**  complex | Dict of sns topic details.  **Returned:** always |
| **content_based_deduplication**  string | Whether or not content_based_deduplication was set  **Returned:** always  **Sample:** `"true"` |
| **delivery_policy**  string | Delivery policy for the SNS topic.  **Returned:** when topic is owned by this AWS account  **Sample:** `"{\"http\":{\"defaultHealthyRetryPolicy\":{\"minDelayTarget\":20,\"maxDelayTarget\":20,\"numRetries\":3,\"numMaxDelayRetries\":0, \"numNoDelayRetries\":0,\"numMinDelayRetries\":0,\"backoffFunction\":\"linear\"},\"disableSubscriptionOverrides\":false}}\n"` |
| **display_name**  string | Display name for SNS topic.  **Returned:** when topic is owned by this AWS account  **Sample:** `"My topic name"` |
| **owner**  string | AWS account that owns the topic.  **Returned:** when topic is owned by this AWS account  **Sample:** `"123456789012"` |
| **policy**  string | Policy for the SNS topic.  **Returned:** when topic is owned by this AWS account  **Sample:** `"{\"Version\":\"2012-10-17\",\"Id\":\"SomePolicyId\",\"Statement\":[{\"Sid\":\"ANewSid\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::123456789012:root\"}, \"Action\":\"sns:Subscribe\",\"Resource\":\"arn:aws:sns:us-east-2:123456789012:ansible-test-dummy-topic\",\"Condition\":{\"StringEquals\":{\"sns:Protocol\":\"email\"}}}]}\n"` |
| **subscriptions**  list / elements=string | List of subscribers to the topic in this AWS account.  **Returned:** always  **Sample:** `[]` |
| **subscriptions_added**  list / elements=string | List of subscribers added in this run.  **Returned:** always  **Sample:** `[]` |
| **subscriptions_confirmed**  string | Count of confirmed subscriptions.  **Returned:** when topic is owned by this AWS account  **Sample:** `"0"` |
| **subscriptions_deleted**  string | Count of deleted subscriptions.  **Returned:** when topic is owned by this AWS account  **Sample:** `"0"` |
| **subscriptions_existing**  list / elements=string | List of existing subscriptions.  **Returned:** always  **Sample:** `[]` |
| **subscriptions_new**  list / elements=string | List of new subscriptions.  **Returned:** always  **Sample:** `[]` |
| **subscriptions_pending**  string | Count of pending subscriptions.  **Returned:** when topic is owned by this AWS account  **Sample:** `"0"` |
| **subscriptions_purge**  boolean | Whether or not purge_subscriptions was set.  **Returned:** always  **Sample:** `true` |
| **topic_arn**  string | ARN of the SNS topic (equivalent to sns_arn).  **Returned:** when topic is owned by this AWS account  **Sample:** `"arn:aws:sns:us-east-2:123456789012:ansible-test-dummy-topic"` |
| **topic_type**  string | The type of topic.  **Returned:** success  **Sample:** `"standard"` |

### Authors

- Alina Buzachis (@alinabuzachis)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
