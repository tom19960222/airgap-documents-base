---
collection: ansible
version: "8"
title: "amazon.aws.cloudtrail_info module – Gather information about trails in AWS Cloud Trail."
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/cloudtrail_info_module.html
fetched_at: 2026-07-28T01:06:16+00:00
---
# amazon.aws.cloudtrail_info module – Gather information about trails in AWS Cloud Trail.

> **Note:**
>
> This module is part of the [amazon.aws collection](https://galaxy.ansible.com/ui/repo/published/amazon/aws/) (version 6.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](cloudtrail_info_module.md#ansible-collections-amazon-aws-cloudtrail-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.cloudtrail_info`.

New in amazon.aws 5.0.0

- [Synopsis](cloudtrail_info_module.md#synopsis)
- [Requirements](cloudtrail_info_module.md#requirements)
- [Parameters](cloudtrail_info_module.md#parameters)
- [Notes](cloudtrail_info_module.md#notes)
- [Examples](cloudtrail_info_module.md#examples)
- [Return Values](cloudtrail_info_module.md#return-values)

## [Synopsis](cloudtrail_info_module.md#id1)

- Gather information about trails in AWS CloudTrail.

## [Requirements](cloudtrail_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](cloudtrail_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **include_shadow_trails**  boolean | Specifies whether to include shadow trails in the response.  **Choices:**   - `false` - `true` ← (default) |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **trail_names**  list / elements=string | Specifies a list of trail names, trail ARNs, or both, of the trails to describe.  If an empty list is specified, information for the trail in the current region is returned.  **Default:** `[]` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cloudtrail_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](cloudtrail_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Gather information about all trails
- amazon.aws.cloudtrail_info:

# Gather information about a particular trail
- amazon.aws.cloudtrail_info:
    trail_names:
      - arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail
```

## [Return Values](cloudtrail_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **trail_list**  list / elements=dictionary | List of trail objects. Each element consists of a dict with all the information related to that cloudtrail.  **Returned:** always |
| **cloud_watch_logs_log_group_arn**  string | Specifies an ARN, that represents the log group to which CloudTrail logs will be delivered.  **Returned:** success  **Sample:** `"arn:aws:sns:us-east-2:123456789012:Mylog"` |
| **cloud_watch_logs_role_arn**  string | Specifies the role for the CloudWatch Logs endpoint to assume to write to a user’s log group.  **Returned:** success  **Sample:** `"arn:aws:sns:us-east-2:123456789012:Mylog"` |
| **has_custom_event_selectors**  boolean | Specifies if the trail has custom event selectors.  **Returned:** success  **Sample:** `true` |
| **has_insight_selectors**  boolean | Specifies whether a trail has insight types specified in an InsightSelector list.  **Returned:** success  **Sample:** `true` |
| **home_region**  string | The region in which the trail was created.  **Returned:** success  **Sample:** `"us-east-1"` |
| **include_global_service_events**  boolean | If True, AWS API calls from AWS global services such as IAM are included.  **Returned:** success  **Sample:** `true` |
| **is_logging**  boolean | Whether the CloudTrail is currently logging AWS API calls.  **Returned:** success  **Sample:** `true` |
| **is_multi_region_trail**  boolean | Specifies whether the trail exists only in one region or exists in all regions.  **Returned:** success  **Sample:** `true` |
| **is_organization_trail**  boolean | Specifies whether the trail is an organization trail.  **Returned:** success  **Sample:** `true` |
| **kms_key_id**  string | Specifies the KMS key ID that encrypts the logs delivered by CloudTrail.  **Returned:** success  **Sample:** `"arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012"` |
| **latest_cloud_watch_logs_delivery_error**  string | Displays any CloudWatch Logs error that CloudTrail encountered when attempting to deliver logs to CloudWatch Logs.  **Returned:** success |
| **latest_cloud_watch_logs_delivery_time**  string | Displays the most recent date and time when CloudTrail delivered logs to CloudWatch Logs.  **Returned:** success |
| **latest_delivery_error**  string | Displays any Amazon S3 error that CloudTrail encountered when attempting to deliver log files to the designated bucket.  **Returned:** success |
| **latest_delivery_time**  string | Specifies the date and time that CloudTrail last delivered log files to an account’s Amazon S3 bucket.  **Returned:** success |
| **latest_digest_delivery_error**  string | Displays any Amazon S3 error that CloudTrail encountered when attempting to deliver a digest file to the designated bucket.  **Returned:** success |
| **latest_digest_delivery_time**  string | Specifies the date and time that CloudTrail last delivered a digest file to an account’s Amazon S3 bucket.  **Returned:** success |
| **latest_notification_error**  string | Displays any Amazon SNS error that CloudTrail encountered when attempting to send a notification.  **Returned:** success |
| **log_file_validation_enabled**  boolean | Specifies whether log file validation is enabled.  **Returned:** success  **Sample:** `true` |
| **name**  string | Name of the trail.  **Returned:** success  **Sample:** `"MyTrail"` |
| **resource_id**  string | Specifies the ARN of the resource.  **Returned:** success |
| **s3_bucket_name**  string | Name of the Amazon S3 bucket into which CloudTrail delivers the trail files.  **Returned:** success  **Sample:** `"aws-cloudtrail-logs-xxxx"` |
| **s3_key_prefix**  string | Amazon S3 key prefix that comes after the name of the bucket that is designated for log file delivery.  **Returned:** success  **Sample:** `"xxxx"` |
| **sns_topic_arn**  string | ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered.  **Returned:** success  **Sample:** `"arn:aws:sns:us-east-2:123456789012:MyTopic"` |
| **start_logging_time**  string | Specifies the most recent date and time when CloudTrail started recording API calls for an AWS account.  **Returned:** success |
| **stop_logging_time**  string | Specifies the most recent date and time when CloudTrail stopped recording API calls for an AWS account.  **Returned:** success |
| **tags**  dictionary | Any tags assigned to the cloudtrail.  **Returned:** always  **Sample:** `{"my_tag_key": "my_tag_value"}` |
| **trail_arn**  string | Specifies the ARN of the trail.  **Returned:** success  **Sample:** `"arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail"` |

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
