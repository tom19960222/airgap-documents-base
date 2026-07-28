---
collection: ansible
version: "6"
title: "community.aws.ec2_metric_alarm module – Create/update or delete AWS Cloudwatch ‘metric alarms’"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ec2_metric_alarm_module.html
fetched_at: 2026-07-27T17:04:03+00:00
---
# community.aws.ec2_metric_alarm module – Create/update or delete AWS Cloudwatch ‘metric alarms’

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
> see [Requirements](ec2_metric_alarm_module.md#ansible-collections-community-aws-ec2-metric-alarm-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_metric_alarm`.

New in community.aws 1.0.0

- [Synopsis](ec2_metric_alarm_module.md#synopsis)
- [Requirements](ec2_metric_alarm_module.md#requirements)
- [Parameters](ec2_metric_alarm_module.md#parameters)
- [Notes](ec2_metric_alarm_module.md#notes)
- [Examples](ec2_metric_alarm_module.md#examples)

## [Synopsis](ec2_metric_alarm_module.md#id1)

- Can create or delete AWS metric alarms.
- Metrics you wish to alarm on must already exist.

## [Requirements](ec2_metric_alarm_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_metric_alarm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alarm_actions**  list / elements=string | A list of the names action(s) taken when the alarm is in the `alarm` status, denoted as Amazon Resource Name(s). |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **comparison**  string | Determines how the threshold value is compared  Symbolic comparison operators have been deprecated, and will be removed after 2022-06-22.  Choices:   - `"GreaterThanOrEqualToThreshold"` - `"GreaterThanThreshold"` - `"LessThanThreshold"` - `"LessThanOrEqualToThreshold"` - `"<="` - `"<"` - `">="` - `">"` |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **description**  string | A longer description of the alarm. |
| **dimensions**  dictionary | A dictionary describing which metric the alarm is applied to.  For more information see the AWS documentation:  <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension> |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **evaluation_periods**  integer | The number of times in which the metric is evaluated before final calculation. |
| **insufficient_data_actions**  list / elements=string | A list of the names of action(s) to take when the alarm is in the `insufficient_data` status. |
| **metric**  string | Name of the monitored metric (e.g. `CPUUtilization`).  Metric must already exist. |
| **name**  string / required | Unique name for the alarm. |
| **namespace**  string | Name of the appropriate namespace (`AWS/EC2`, `System/Linux`, etc.), which determines the category it will appear under in cloudwatch. |
| **ok_actions**  list / elements=string | A list of the names of action(s) to take when the alarm is in the `ok` status, denoted as Amazon Resource Name(s). |
| **period**  integer | The time (in seconds) between metric evaluations. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Register or deregister the alarm.  Choices:   - `"present"` ← (default) - `"absent"` |
| **statistic**  string | Operation applied to the metric.  Works in conjunction with *period* and *evaluation_periods* to determine the comparison value.  Choices:   - `"SampleCount"` - `"Average"` - `"Sum"` - `"Minimum"` - `"Maximum"` |
| **threshold**  float | Sets the min/max bound for triggering the alarm. |
| **treat_missing_data**  string | Sets how the alarm handles missing data points.  Choices:   - `"breaching"` - `"notBreaching"` - `"ignore"` - `"missing"` ← (default) |
| **unit**  string | The threshold’s unit of measurement.  Choices:   - `"Seconds"` - `"Microseconds"` - `"Milliseconds"` - `"Bytes"` - `"Kilobytes"` - `"Megabytes"` - `"Gigabytes"` - `"Terabytes"` - `"Bits"` - `"Kilobits"` - `"Megabits"` - `"Gigabits"` - `"Terabits"` - `"Percent"` - `"Count"` - `"Bytes/Second"` - `"Kilobytes/Second"` - `"Megabytes/Second"` - `"Gigabytes/Second"` - `"Terabytes/Second"` - `"Bits/Second"` - `"Kilobits/Second"` - `"Megabits/Second"` - `"Gigabits/Second"` - `"Terabits/Second"` - `"Count/Second"` - `"None"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ec2_metric_alarm_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_metric_alarm_module.md#id5)

```yaml+jinja
- name: create alarm
  community.aws.ec2_metric_alarm:
    state: present
    region: ap-southeast-2
    name: "cpu-low"
    metric: "CPUUtilization"
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

- name: Create an alarm to recover a failed instance
  community.aws.ec2_metric_alarm:
    state: present
    region: us-west-1
    name: "recover-instance"
    metric: "StatusCheckFailed_System"
    namespace: "AWS/EC2"
    statistic: "Minimum"
    comparison: ">="
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

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
