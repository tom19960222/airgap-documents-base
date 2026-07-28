---
collection: ansible
version: "6"
title: "community.aws.cloudtrail module – manage CloudTrail create, delete, update"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/cloudtrail_module.html
fetched_at: 2026-07-27T17:03:45+00:00
---
# community.aws.cloudtrail module – manage CloudTrail create, delete, update

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
> see [Requirements](cloudtrail_module.md#ansible-collections-community-aws-cloudtrail-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.cloudtrail`.

New in community.aws 1.0.0

- [Synopsis](cloudtrail_module.md#synopsis)
- [Requirements](cloudtrail_module.md#requirements)
- [Parameters](cloudtrail_module.md#parameters)
- [Notes](cloudtrail_module.md#notes)
- [Examples](cloudtrail_module.md#examples)
- [Return Values](cloudtrail_module.md#return-values)

## [Synopsis](cloudtrail_module.md#id1)

- Creates, deletes, or updates CloudTrail configuration. Ensures logging is also enabled.

## [Requirements](cloudtrail_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](cloudtrail_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **cloudwatch_logs_log_group_arn**  string | A full ARN specifying a valid CloudWatch log group to which CloudTrail logs will be delivered. The log group should already exist.  See <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.html>.  Required when `cloudwatch_logs_role_arn`. |
| **cloudwatch_logs_role_arn**  string | Specifies a full ARN for an IAM role that assigns the proper permissions for CloudTrail to create and write to the log group.  See <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.html>.  Required when `cloudwatch_logs_log_group_arn`. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **enable_log_file_validation**  aliases: log_file_validation_enabled  boolean | Specifies whether log file integrity validation is enabled.  CloudTrail will create a hash for every log file delivered and produce a signed digest file that can be used to ensure log files have not been tampered.  Choices:   - `false` - `true` |
| **enable_logging**  boolean | Start or stop the CloudTrail logging. If stopped the trail will be paused and will not record events or deliver log files.  Choices:   - `false` - `true` ← (default) |
| **include_global_events**  aliases: include_global_service_events  boolean | Record API calls from global services such as IAM and STS.  Choices:   - `false` - `true` ← (default) |
| **is_multi_region_trail**  boolean | Specify whether the trail belongs only to one region or exists in all regions.  Choices:   - `false` ← (default) - `true` |
| **kms_key_id**  string | Specifies the KMS key ID to use to encrypt the logs delivered by CloudTrail. This also has the effect of enabling log file encryption.  The value can be an alias name prefixed by “alias/”, a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.  See <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/encrypting-cloudtrail-log-files-with-aws-kms.html>. |
| **name**  string | Name for the CloudTrail.  Names are unique per-region unless the CloudTrail is a multi-region trail, in which case it is unique per-account.  Default: `"default"` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **s3_bucket_name**  string | An existing S3 bucket where CloudTrail will deliver log files.  This bucket should exist and have the proper policy.  See <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/aggregating_logs_regions_bucket_policy.html>.  Required when *state=present*. |
| **s3_key_prefix**  string | S3 Key prefix for delivered log files. A trailing slash is not necessary and will be removed. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **sns_topic_name**  string | SNS Topic name to send notifications to when a log file is delivered. |
| **state**  string | Add or remove CloudTrail configuration.  The following states have been preserved for backwards compatibility: *state=enabled* and *state=disabled*.  *state=enabled* is equivalet to *state=present*.  *state=disabled* is equivalet to *state=absent*.  Choices:   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` |
| **tags**  dictionary | A hash/dictionary of tags to be applied to the CloudTrail resource.  Remove completely or specify an empty dictionary to remove all tags.  Default: `{}` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](cloudtrail_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](cloudtrail_module.md#id5)

```yaml+jinja
- name: create single region cloudtrail
  community.aws.cloudtrail:
    state: present
    name: default
    s3_bucket_name: mylogbucket
    s3_key_prefix: cloudtrail
    region: us-east-1

- name: create multi-region trail with validation and tags
  community.aws.cloudtrail:
    state: present
    name: default
    s3_bucket_name: mylogbucket
    region: us-east-1
    is_multi_region_trail: true
    enable_log_file_validation: true
    cloudwatch_logs_role_arn: "arn:aws:iam::123456789012:role/CloudTrail_CloudWatchLogs_Role"
    cloudwatch_logs_log_group_arn: "arn:aws:logs:us-east-1:123456789012:log-group:CloudTrail/DefaultLogGroup:*"
    kms_key_id: "alias/MyAliasName"
    tags:
      environment: dev
      Name: default

- name: show another valid kms_key_id
  community.aws.cloudtrail:
    state: present
    name: default
    s3_bucket_name: mylogbucket
    kms_key_id: "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
    # simply "12345678-1234-1234-1234-123456789012" would be valid too.

- name: pause logging the trail we just created
  community.aws.cloudtrail:
    state: present
    name: default
    enable_logging: false
    s3_bucket_name: mylogbucket
    region: us-east-1
    is_multi_region_trail: true
    enable_log_file_validation: true
    tags:
      environment: dev
      Name: default

- name: delete a trail
  community.aws.cloudtrail:
    state: absent
    name: default
```

## [Return Values](cloudtrail_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **exists**  boolean | whether the resource exists  Returned: always  Sample: `true` |
| **trail**  complex | CloudTrail resource details  Returned: always  Sample: `"hash/dictionary of values"` |
| **cloud_watch_logs_log_group_arn**  string | Full ARN of the CloudWatch Logs log group where events are delivered.  Returned: success when present  Sample: `"arn:aws:logs:us-east-1:123456789012:log-group:CloudTrail/DefaultLogGroup:*"` |
| **cloud_watch_logs_role_arn**  string | Full ARN of the IAM role that CloudTrail assumes to deliver events.  Returned: success when present  Sample: `"arn:aws:iam::123456789012:role/CloudTrail_CloudWatchLogs_Role"` |
| **has_custom_event_selectors**  boolean | Whether any custom event selectors are used for this trail.  Returned: success  Sample: `false` |
| **home_region**  string | The home region where the trail was originally created and must be edited.  Returned: success  Sample: `"us-east-1"` |
| **include_global_service_events**  boolean | Whether global services (IAM, STS) are logged with this trail  Returned: success  Sample: `true` |
| **is_logging**  boolean | Whether logging is turned on or paused for the Trail  Returned: success  Sample: `true` |
| **is_multi_region_trail**  boolean | Whether the trail applies to all regions or just one  Returned: success  Sample: `true` |
| **kms_key_id**  string | Full ARN of the KMS Key used to encrypt log files.  Returned: success when present  Sample: `"arn:aws:kms::123456789012:key/12345678-1234-1234-1234-123456789012"` |
| **log_file_validation_enabled**  boolean | Whether log file validation is enabled on the trail  Returned: success  Sample: `true` |
| **name**  string | Name of the CloudTrail resource  Returned: success  Sample: `"default"` |
| **s3_bucket_name**  string | S3 bucket name where log files are delivered  Returned: success  Sample: `"myBucket"` |
| **s3_key_prefix**  string | Key prefix in bucket where log files are delivered (if any)  Returned: success when present  Sample: `"myKeyPrefix"` |
| **sns_topic_arn**  string | Full ARN of the SNS topic where log delivery notifications are sent.  Returned: success when present  Sample: `"arn:aws:sns:us-east-1:123456789012:topic/myTopic"` |
| **sns_topic_name**  string | The SNS topic name where log delivery notifications are sent.  Returned: success when present  Sample: `"myTopic"` |
| **tags**  dictionary | hash/dictionary of tags applied to this resource  Returned: success  Sample: `{"Name": "default", "environment": "dev"}` |
| **trail_arn**  string | Full ARN of the CloudTrail resource  Returned: success  Sample: `"arn:aws:cloudtrail:us-east-1:123456789012:trail/default"` |

### Authors

- Ansible Core Team
- Ted Timmons (@tedder)
- Daniel Shepherd (@shepdelacreme)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
