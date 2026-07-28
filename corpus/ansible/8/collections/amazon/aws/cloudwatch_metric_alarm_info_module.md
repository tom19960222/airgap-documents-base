---
collection: ansible
version: "8"
title: "amazon.aws.cloudwatch_metric_alarm_info module – Gather information about the alarms for the specified metric"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/cloudwatch_metric_alarm_info_module.html
fetched_at: 2026-07-28T01:06:17+00:00
---
# amazon.aws.cloudwatch_metric_alarm_info module – Gather information about the alarms for the specified metric

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
> see [Requirements](cloudwatch_metric_alarm_info_module.md#ansible-collections-amazon-aws-cloudwatch-metric-alarm-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.cloudwatch_metric_alarm_info`.

New in amazon.aws 5.0.0

- [Synopsis](cloudwatch_metric_alarm_info_module.md#synopsis)
- [Requirements](cloudwatch_metric_alarm_info_module.md#requirements)
- [Parameters](cloudwatch_metric_alarm_info_module.md#parameters)
- [Notes](cloudwatch_metric_alarm_info_module.md#notes)
- [Examples](cloudwatch_metric_alarm_info_module.md#examples)
- [Return Values](cloudwatch_metric_alarm_info_module.md#return-values)

## [Synopsis](cloudwatch_metric_alarm_info_module.md#id1)

- Retrieves the alarms for the specified metric.

## [Requirements](cloudwatch_metric_alarm_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](cloudwatch_metric_alarm_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **action_prefix**  string | This parameter can be used to filter the results of the operation to only those alarms that use a certain alarm action. |
| **alarm_name_prefix**  string | An alarm name prefix to retrieve information about alarms that have names that start with this prefix.  Can not be used with *alarm_names*. |
| **alarm_names**  list / elements=string | The name of the metric. |
| **alarm_type**  string | Specify this to return metric alarms or composite alarms.  Module is defaulted to return metric alarms but can return composite alarms if *alarm_type=CompositeAlarm*.  **Choices:**   - `"CompositeAlarm"` - `"MetricAlarm"` ← (default) |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **children_of_alarm_name**  string | If specified returns information about the “children” alarms of the alarm name specified. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **parents_of_alarm_name**  string | If specified returns information about the “parent” alarms of the alarm name specified. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state_value**  string | If specified returns information only about alarms that are currently in the particular state.  **Choices:**   - `"OK"` - `"ALARM"` - `"INSUFFICIENT_DATA"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cloudwatch_metric_alarm_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](cloudwatch_metric_alarm_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: describe the metric alarm based on alarm names
  amazon.aws.cloudwatch_metric_alarm_info:
    alarm_names:
        - my-test-alarm-1
        - my-test-alarm-2

- name: describe the metric alarm based alarm names and state value
  amazon.aws.cloudwatch_metric_alarm_info:
    alarm_names:
        - my-test-alarm-1
        - my-test-alarm-2
    state_value: OK

- name: describe the metric alarm based alarm names prefix
  amazon.aws.cloudwatch_metric_alarm_info:
    alarm_name_prefix: my-test-
```

## [Return Values](cloudwatch_metric_alarm_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **metric_alarms**  list / elements=dictionary | The gathered information about specified metric alarms.  **Returned:** when success |
| **actions_enabled**  boolean | Indicates whether actions should be executed during any changes to the alarm state.  **Returned:** always |
| **alarm_actions**  list / elements=string | The actions to execute when this alarm transitions to an ALARM state from any other state.  **Returned:** always |
| **alarm_arn**  string | The Amazon Resource Name (ARN) of the alarm.  **Returned:** always |
| **alarm_configuration_updated_timestamp**  string | The time stamp of the last update to the alarm configuration.  **Returned:** always |
| **alarm_description**  string | The description of the alarm.  **Returned:** always |
| **alarm_name**  string | Unique name for the alarm.  **Returned:** always |
| **comparison_operator**  string | The arithmetic operation to use when comparing the specified statistic and threshold.  **Returned:** always |
| **datapoints_to_alarm**  integer | The number of data points that must be breaching to trigger the alarm.  **Returned:** always |
| **dimensions**  list / elements=dictionary | The dimensions for the metric.  **Returned:** always |
| **name**  string | The name of the dimension.  **Returned:** always |
| **value**  string | The value of the dimension.  **Returned:** always |
| **evaluate_low_sample_count_percentile**  string | Used only for alarms based on percentiles.  If *ignore*, the alarm state does not change during periods with too few data points to be statistically significant.  If *evaluate* or this parameter is not used, the alarm is always evaluated and possibly changes state.  **Returned:** always |
| **evaluation_period**  integer | The number of periods over which data is compared to the specified threshold.  **Returned:** always |
| **extended_statistic**  string | The percentile statistic for the metric associated with the alarm.  **Returned:** always |
| **insufficient_data_actions**  list / elements=string | The actions to execute when this alarm transitions to an INSUFFICIENT_DATA state from any other state.  **Returned:** always |
| **metric_name**  string | Name of the monitored metric (e.g. `CPUUtilization`).  **Returned:** always |
| **metrics**  list / elements=dictionary | An array of MetricDataQuery structures, used in an alarm based on a metric math expression.  **Returned:** always |
| **namespace**  string | Name of the appropriate namespace (`AWS/EC2`, `System/Linux`, etc.).  Determines the category it will appear under in CloudWatch.  **Returned:** always |
| **ok_actions**  list / elements=string | The actions to execute when this alarm transitions to an OK state from any other state.  **Returned:** always |
| **period**  integer | The length, in seconds, used each time the metric specified in MetricName is evaluated.  Valid values are 10, 30, and any multiple of 60.  **Returned:** always |
| **state_reason**  string | An explanation for the alarm state, in text format.  **Returned:** always |
| **state_reason_data**  string | An explanation for the alarm state, in JSON format.  **Returned:** always |
| **state_updated_timestamp**  string | The time stamp of the last update to the alarm state.  **Returned:** always |
| **state_value**  string | The state value for the alarm.  **Returned:** always |
| **statistic**  string | The statistic for the metric associated with the alarm, other than percentile.  **Returned:** always |
| **threshold**  float | The value to compare with the specified statistic.  **Returned:** always |
| **threshold_metric_id**  string | This is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.  **Returned:** always |
| **treat_missing_data**  string | Sets how alarm is to handle missing data points.  **Returned:** always |
| **unit**  string | Unit used when storing the metric  **Returned:** always |

### Authors

- Mandar Vijay Kulkarni (@mandar242)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
