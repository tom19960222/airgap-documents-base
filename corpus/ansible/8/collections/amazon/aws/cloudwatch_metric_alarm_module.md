---
collection: ansible
version: "8"
title: "amazon.aws.cloudwatch_metric_alarm module – Create/update or delete AWS CloudWatch ‘metric alarms’"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/cloudwatch_metric_alarm_module.html
fetched_at: 2026-07-28T01:06:16+00:00
---
# amazon.aws.cloudwatch_metric_alarm module – Create/update or delete AWS CloudWatch ‘metric alarms’

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
> see [Requirements](cloudwatch_metric_alarm_module.md#ansible-collections-amazon-aws-cloudwatch-metric-alarm-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.cloudwatch_metric_alarm`.

New in amazon.aws 5.0.0

- [Synopsis](cloudwatch_metric_alarm_module.md#synopsis)
- [Requirements](cloudwatch_metric_alarm_module.md#requirements)
- [Parameters](cloudwatch_metric_alarm_module.md#parameters)
- [Notes](cloudwatch_metric_alarm_module.md#notes)
- [Examples](cloudwatch_metric_alarm_module.md#examples)

## [Synopsis](cloudwatch_metric_alarm_module.md#id1)

- Can create or delete AWS CloudWatch metric alarms.
- Metrics you wish to alarm on must already exist.
- Prior to release 5.0.0 this module was called `community.aws.ec2_metric_alarm`. The usage did not change.
- This module was originally added to `community.aws` in release 1.0.0.

Aliases: ec2_metric_alarm

## [Requirements](cloudwatch_metric_alarm_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](cloudwatch_metric_alarm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **alarm_actions**  list / elements=string | A list of the names action(s) taken when the alarm is in the `alarm` status, denoted as Amazon Resource Name(s).  **Default:** `[]` |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **comparison**  string | Determines how the threshold value is compared  **Choices:**   - `"GreaterThanOrEqualToThreshold"` - `"GreaterThanThreshold"` - `"LessThanThreshold"` - `"LessThanOrEqualToThreshold"` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | A longer description of the alarm. |
| **dimensions**  dictionary | A dictionary describing which metric the alarm is applied to.  For more information see the AWS documentation:  <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension> |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **evaluation_periods**  integer | The number of times in which the metric is evaluated before final calculation. |
| **extended_statistic**  string  *added in amazon.aws 5.5.0* | The percentile statistic for the metric specified in the metric name. |
| **insufficient_data_actions**  list / elements=string | A list of the names of action(s) to take when the alarm is in the `insufficient_data` status.  **Default:** `[]` |
| **metric_name**  aliases: metric  string | Name of the monitored metric (e.g. `CPUUtilization`).  Metric must already exist. |
| **metrics**  list / elements=dictionary  *added in amazon.aws 5.5.0* | An array of MetricDataQuery structures that enable you to create an alarm based on the result of a metric math expression.  **Default:** `[]` |
| **account_id**  string | The ID of the account where the metrics are located, if this is a cross-account alarm. |
| **expression**  string | This field can contain either a Metrics Insights query, or a metric math expression to be performed on the returned data. |
| **id**  string / required | A short name used to tie this object to the results in the response. |
| **label**  string | A human-readable label for this metric or expression. |
| **metric_stat**  dictionary | The metric to be returned, along with statistics, period, and units. |
| **metric**  dictionary | The metric to return, including the metric name, namespace, and dimensions. |
| **dimensions**  list / elements=dictionary | a name/value pair that is part of the identity of a metric. |
| **name**  string / required | The name of the dimension. |
| **value**  string / required | The value of the dimension. |
| **metric_name**  string / required | The name of the metric. |
| **namespace**  string | The namespace of the metric. |
| **period**  integer / required | The granularity, in seconds, of the returned data points. |
| **stat**  string / required | The statistic to return. It can include any CloudWatch statistic or extended statistic. |
| **unit**  string | Unit to use when storing the metric. |
| **period**  integer | The granularity, in seconds, of the returned data points. |
| **return_data**  boolean | This option indicates whether to return the timestamps and raw data values of this metric.  **Choices:**   - `false` - `true` |
| **name**  string / required | Unique name for the alarm. |
| **namespace**  string | Name of the appropriate namespace (`AWS/EC2`, `System/Linux`, etc.), which determines the category it will appear under in CloudWatch. |
| **ok_actions**  list / elements=string | A list of the names of action(s) to take when the alarm is in the `ok` status, denoted as Amazon Resource Name(s).  **Default:** `[]` |
| **period**  integer | The time (in seconds) between metric evaluations. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Register or deregister the alarm.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **statistic**  string | Operation applied to the metric.  Works in conjunction with *period* and *evaluation_periods* to determine the comparison value.  **Choices:**   - `"SampleCount"` - `"Average"` - `"Sum"` - `"Minimum"` - `"Maximum"` |
| **threshold**  float | Sets the min/max bound for triggering the alarm. |
| **treat_missing_data**  string | Sets how the alarm handles missing data points.  **Choices:**   - `"breaching"` - `"notBreaching"` - `"ignore"` - `"missing"` ← (default) |
| **unit**  string | The threshold’s unit of measurement.  **Choices:**   - `"Seconds"` - `"Microseconds"` - `"Milliseconds"` - `"Bytes"` - `"Kilobytes"` - `"Megabytes"` - `"Gigabytes"` - `"Terabytes"` - `"Bits"` - `"Kilobits"` - `"Megabits"` - `"Gigabits"` - `"Terabits"` - `"Percent"` - `"Count"` - `"Bytes/Second"` - `"Kilobytes/Second"` - `"Megabytes/Second"` - `"Gigabytes/Second"` - `"Terabytes/Second"` - `"Bits/Second"` - `"Kilobits/Second"` - `"Megabits/Second"` - `"Gigabits/Second"` - `"Terabits/Second"` - `"Count/Second"` - `"None"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cloudwatch_metric_alarm_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](cloudwatch_metric_alarm_module.md#id5)

```yaml+jinja
- name: create alarm
  amazon.aws.cloudwatch_metric_alarm:
    state: present
    region: ap-southeast-2
    name: "cpu-low"
    metric_name: "CPUUtilization"
    namespace: "AWS/EC2"
    statistic: Average
    comparison: "LessThanOrEqualToThreshold"
    threshold: 5.0
    period: 300
    evaluation_periods: 3
    unit: "Percent"
    description: "This will alarm when a instance's CPU usage average is lower than 5% for 15 minutes"
    dimensions: {'InstanceId':'i-XXX'}
    alarm_actions: ["action1","action2"]

- name: create alarm with metrics
  amazon.aws.cloudwatch_metric_alarm:
    state: present
    region: ap-southeast-2
    name: "cpu-low"
    metrics:
      - id: 'CPU'
        metric_stat:
            metric:
                dimensions:
                    name: "InstanceId"
                    value: "i-xx"
                metric_name: "CPUUtilization"
                namespace: "AWS/EC2"
            period: "300"
            stat: "Average"
            unit: "Percent"
        return_data: False
    alarm_actions: ["action1","action2"]

- name: Create an alarm to recover a failed instance
  amazon.aws.cloudwatch_metric_alarm:
    state: present
    region: us-west-1
    name: "recover-instance"
    metric: "StatusCheckFailed_System"
    namespace: "AWS/EC2"
    statistic: "Minimum"
    comparison: "GreaterThanOrEqualToThreshold"
    threshold: 1.0
    period: 60
    evaluation_periods: 2
    unit: "Count"
    description: "This will recover an instance when it fails"
    dimensions: {"InstanceId":'i-XXX'}
    alarm_actions: ["arn:aws:automate:us-west-1:ec2:recover"]
```

### Authors

- Zacharie Eakin (@Zeekin)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
