---
collection: ansible
version: "8"
title: "community.aws.autoscaling_policy module – Create or delete AWS scaling policies for Autoscaling groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/autoscaling_policy_module.html
fetched_at: 2026-07-28T01:40:13+00:00
---
# community.aws.autoscaling_policy module – Create or delete AWS scaling policies for Autoscaling groups

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
> see [Requirements](autoscaling_policy_module.md#ansible-collections-community-aws-autoscaling-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.autoscaling_policy`.

New in community.aws 1.0.0

- [Synopsis](autoscaling_policy_module.md#synopsis)
- [Requirements](autoscaling_policy_module.md#requirements)
- [Parameters](autoscaling_policy_module.md#parameters)
- [Notes](autoscaling_policy_module.md#notes)
- [Examples](autoscaling_policy_module.md#examples)
- [Return Values](autoscaling_policy_module.md#return-values)

## [Synopsis](autoscaling_policy_module.md#id1)

- Can create or delete scaling policies for autoscaling groups.
- Referenced autoscaling groups must already exist.
- Prior to release 5.0.0 this module was called `community.aws.ec2_scaling_policy`. The usage did not change.

Aliases: ec2_scaling_policy

## [Requirements](autoscaling_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](autoscaling_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **adjustment_type**  string | The type of change in capacity of the autoscaling group.  Required if *state* is `present`.  **Choices:**   - `"ChangeInCapacity"` - `"ExactCapacity"` - `"PercentChangeInCapacity"` |
| **asg_name**  string | Name of the associated autoscaling group.  Required if *state* is `present`. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **cooldown**  integer | The minimum period of time (in seconds) between which autoscaling actions can take place.  Only used when *policy_type* is `SimpleScaling`. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **estimated_instance_warmup**  integer | The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. |
| **metric_aggregation**  string | The aggregation type for the CloudWatch metrics.  Only used when *policy_type* is not `SimpleScaling`.  **Choices:**   - `"Minimum"` - `"Maximum"` - `"Average"` ← (default) |
| **min_adjustment_step**  integer | Minimum amount of adjustment when policy is triggered.  Only used when *adjustment_type* is `PercentChangeInCapacity`. |
| **name**  string / required | Unique name for the scaling policy. |
| **policy_type**  string | Auto scaling adjustment policy.  **Choices:**   - `"StepScaling"` - `"SimpleScaling"` ← (default) - `"TargetTrackingScaling"` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **scaling_adjustment**  integer | The amount by which the autoscaling group is adjusted by the policy.  A negative number has the effect of scaling down the ASG.  Units are numbers of instances for `ExactCapacity` or `ChangeInCapacity` or percent of existing instances for `PercentChangeInCapacity`.  Required when *policy_type* is `SimpleScaling`. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Register or deregister the policy.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **step_adjustments**  list / elements=dictionary | List of dicts containing *lower_bound*, *upper_bound* and *scaling_adjustment*.  Intervals must not overlap or have a gap between them.  At most, one item can have an undefined *lower_bound*. If any item has a negative lower_bound, then there must be a step adjustment with an undefined *lower_bound*.  At most, one item can have an undefined *upper_bound*. If any item has a positive upper_bound, then there must be a step adjustment with an undefined *upper_bound*.  The bounds are the amount over the alarm threshold at which the adjustment will trigger. This means that for an alarm threshold of 50, triggering at 75 requires a lower bound of 25. See <http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_StepAdjustment.html>. |
| **lower_bound**  integer | The lower bound for the difference between the alarm threshold and the CloudWatch metric. |
| **scaling_adjustment**  integer / required | The amount by which to scale. |
| **upper_bound**  integer | The upper bound for the difference between the alarm threshold and the CloudWatch metric. |
| **target_tracking_config**  dictionary  *added in community.aws 4.1.0* | Allows you to specify a *target_tracking_config* for autoscaling policies in AWS.  *target_tracking_config* can accept nested dicts for *customized_metric_spec* or *predefined_metric_spec*. Each specification aligns with their boto3 equivalent.  Required when *TargetTrackingScaling* policy is specified. |
| **customized_metric_spec**  dictionary | Specify a dict will be passed in as a call for `TargetTrackingConfiguration`. |
| **dimensions**  list / elements=dictionary | The dimensions of the metric. The element of the list should be a dict. |
| **metric_name**  string / required | The name of the metric. |
| **namespace**  string / required | The namespace of the metric. |
| **statistic**  string / required | The statistic of the metric.  **Choices:**   - `"Average"` - `"Minimum"` - `"Maximum"` - `"SampleCount"` - `"Sum"` |
| **unit**  string | The unit of the metric. Reference AmazonCloudWatch API for valid Units. |
| **disable_scalein**  boolean | Indicate whether scaling in by the target tracking scaling policy is disabled.  **Choices:**   - `false` - `true` |
| **predefined_metric_spec**  dictionary | Specify a dict will be passed in as a call for *TargetTrackingConfiguration*. |
| **predefined_metric_type**  string / required | Required if `predefined_metric_spec` is used.  **Choices:**   - `"ASGAverageCPUUtilization"` - `"ASGAverageNetworkIn"` - `"ASGAverageNetworkOut"` - `"ALBRequestCountPerTarget"` |
| **resource_label**  string | Uniquely identifies a specific ALB target group from which to determine the average request count served by your Auto Scaling group.  You can’t specify a resource label unless the target group is attached to the Auto Scaling group. |
| **target_value**  float / required | Specify a float number for target utilization.  Required when *target_tracking_config* is specified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](autoscaling_policy_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](autoscaling_policy_module.md#id5)

```yaml+jinja
- name: Simple Scale Down policy
  community.aws.autoscaling_policy:
    state: present
    region: US-XXX
    name: "scaledown-policy"
    adjustment_type: "ChangeInCapacity"
    asg_name: "application-asg"
    scaling_adjustment: -1
    min_adjustment_step: 1
    cooldown: 300

# For an alarm with a breach threshold of 20, the
# following creates a stepped policy:
# From 20-40 (0-20 above threshold), increase by 50% of existing capacity
# From 41-infinity, increase by 100% of existing capacity
- community.aws.autoscaling_policy:
    state: present
    region: US-XXX
    name: "step-scale-up-policy"
    policy_type: StepScaling
    metric_aggregation: Maximum
    step_adjustments:
      - upper_bound: 20
        scaling_adjustment: 50
      - lower_bound: 20
        scaling_adjustment: 100
    adjustment_type: "PercentChangeInCapacity"
    asg_name: "application-asg"

- name: create TargetTracking predefined policy
  community.aws.autoscaling_policy:
    name: "predefined-policy-1"
    policy_type: TargetTrackingScaling
    target_tracking_config:
      predefined_metric_spec:
        predefined_metric_type: ASGAverageCPUUtilization
      target_value: 98.0
    asg_name: "asg-test-1"
  register: result

- name: create TargetTracking predefined policy with resource_label
  community.aws.autoscaling_policy:
    name: "predefined-policy-1"
    policy_type: TargetTrackingScaling
    target_tracking_config:
      predefined_metric_spec:
        predefined_metric_type: ALBRequestCountPerTarget
        resource_label: app/my-alb/778d41231d141a0f/targetgroup/my-alb-target-group/942f017f100becff
      target_value: 98.0
    asg_name: "asg-test-1"
  register: result

- name: create TargetTrackingScaling custom policy
  community.aws.autoscaling_policy:
    name: "custom-policy-1"
    policy_type: TargetTrackingScaling
    target_tracking_config:
      customized_metric_spec:
        metric_name: metric_1
        namespace: namespace_1
        statistic: Minimum
        unit: Gigabits
        dimensions: [{'Name': 'dimension1', 'Value': 'value1'}]
      disable_scalein: true
      target_value: 98.0
    asg_name: asg-test-1
  register: result
```

## [Return Values](autoscaling_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **adjustment_type**  string | Scaling policy adjustment type.  **Returned:** always  **Sample:** `"PercentChangeInCapacity"` |
| **alarms**  complex | Cloudwatch alarms related to the policy.  **Returned:** always |
| **alarm_arn**  string | ARN of the Cloudwatch alarm.  **Returned:** always  **Sample:** `"arn:aws:cloudwatch:us-east-2:1234567890:alarm:cpu-very-high"` |
| **alarm_name**  string | Name of the Cloudwatch alarm.  **Returned:** always  **Sample:** `"cpu-very-high"` |
| **arn**  string | ARN of the scaling policy. Provided for backward compatibility, value is the same as *policy_arn*.  **Returned:** always  **Sample:** `"arn:aws:autoscaling:us-east-2:123456789012:scalingPolicy:59e37526-bd27-42cf-adca-5cd3d90bc3b9:autoScalingGroupName/app-asg:policyName/app-policy"` |
| **as_name**  string | Auto Scaling Group name. Provided for backward compatibility, value is the same as *auto_scaling_group_name*.  **Returned:** always  **Sample:** `"app-asg"` |
| **auto_scaling_group_name**  string | Name of Auto Scaling Group.  **Returned:** always  **Sample:** `"app-asg"` |
| **metric_aggregation_type**  string | Method used to aggregate metrics.  **Returned:** when *policy_type* is `StepScaling`  **Sample:** `"Maximum"` |
| **name**  string | Name of the scaling policy. Provided for backward compatibility, value is the same as *policy_name*.  **Returned:** always  **Sample:** `"app-policy"` |
| **policy_arn**  string | ARN of scaling policy.  **Returned:** always  **Sample:** `"arn:aws:autoscaling:us-east-2:123456789012:scalingPolicy:59e37526-bd27-42cf-adca-5cd3d90bc3b9:autoScalingGroupName/app-asg:policyName/app-policy"` |
| **policy_name**  string | Name of scaling policy.  **Returned:** always  **Sample:** `"app-policy"` |
| **policy_type**  string | Type of auto scaling policy.  **Returned:** always  **Sample:** `"StepScaling"` |
| **scaling_adjustment**  integer | Adjustment to make when alarm is triggered.  **Returned:** When *policy_type* is `SimpleScaling`  **Sample:** `1` |
| **step_adjustments**  complex | List of step adjustments.  **Returned:** always |
| **metric_interval_lower_bound**  float | Lower bound for metric interval.  **Returned:** if step has a lower bound  **Sample:** `20.0` |
| **metric_interval_upper_bound**  float | Upper bound for metric interval.  **Returned:** if step has an upper bound  **Sample:** `40.0` |
| **scaling_adjustment**  integer | Adjustment to make if this step is reached.  **Returned:** always  **Sample:** `50` |

### Authors

- Zacharie Eakin (@zeekin)
- Will Thames (@willthames)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
