---
collection: ansible
version: "6"
title: "community.aws.ec2_scaling_policy module – Create or delete AWS scaling policies for Autoscaling groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ec2_scaling_policy_module.html
fetched_at: 2026-07-27T17:04:05+00:00
---
# community.aws.ec2_scaling_policy module – Create or delete AWS scaling policies for Autoscaling groups

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
> see [Requirements](ec2_scaling_policy_module.md#ansible-collections-community-aws-ec2-scaling-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_scaling_policy`.

New in community.aws 1.0.0

- [Synopsis](ec2_scaling_policy_module.md#synopsis)
- [Requirements](ec2_scaling_policy_module.md#requirements)
- [Parameters](ec2_scaling_policy_module.md#parameters)
- [Notes](ec2_scaling_policy_module.md#notes)
- [Examples](ec2_scaling_policy_module.md#examples)
- [Return Values](ec2_scaling_policy_module.md#return-values)

## [Synopsis](ec2_scaling_policy_module.md#id1)

- Can create or delete scaling policies for autoscaling groups.
- Referenced autoscaling groups must already exist.

## [Requirements](ec2_scaling_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_scaling_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **adjustment_type**  string | The type of change in capacity of the autoscaling group.  Required if *state* is `present`.  Choices:   - `"ChangeInCapacity"` - `"ExactCapacity"` - `"PercentChangeInCapacity"` |
| **asg_name**  string | Name of the associated autoscaling group.  Required if *state* is `present`. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **cooldown**  integer | The minimum period of time (in seconds) between which autoscaling actions can take place.  Only used when *policy_type* is `SimpleScaling`. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **estimated_instance_warmup**  integer | The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. |
| **metric_aggregation**  string | The aggregation type for the CloudWatch metrics.  Only used when *policy_type* is not `SimpleScaling`.  Choices:   - `"Minimum"` - `"Maximum"` - `"Average"` ← (default) |
| **min_adjustment_step**  integer | Minimum amount of adjustment when policy is triggered.  Only used when *adjustment_type* is `PercentChangeInCapacity`. |
| **name**  string / required | Unique name for the scaling policy. |
| **policy_type**  string | Auto scaling adjustment policy.  Choices:   - `"StepScaling"` - `"SimpleScaling"` ← (default) |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **scaling_adjustment**  integer | The amount by which the autoscaling group is adjusted by the policy.  A negative number has the effect of scaling down the ASG.  Units are numbers of instances for `ExactCapacity` or `ChangeInCapacity` or percent of existing instances for `PercentChangeInCapacity`.  Required when *policy_type* is `SimpleScaling`. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Register or deregister the policy.  Choices:   - `"present"` ← (default) - `"absent"` |
| **step_adjustments**  list / elements=dictionary | list of dicts containing *lower_bound*, *upper_bound* and *scaling_adjustment*  Intervals must not overlap or have a gap between them.  At most, one item can have an undefined *lower_bound*. If any item has a negative lower_bound, then there must be a step adjustment with an undefined *lower_bound*.  At most, one item can have an undefined *upper_bound*. If any item has a positive upper_bound, then there must be a step adjustment with an undefined *upper_bound*.  The bounds are the amount over the alarm threshold at which the adjustment will trigger. This means that for an alarm threshold of 50, triggering at 75 requires a lower bound of 25. See <http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_StepAdjustment.html>. |
| **lower_bound**  integer | The lower bound for the difference between the alarm threshold and the CloudWatch metric. |
| **scaling_adjustment**  integer / required | The amount by which to scale. |
| **upper_bound**  integer | The upper bound for the difference between the alarm threshold and the CloudWatch metric. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ec2_scaling_policy_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_scaling_policy_module.md#id5)

```yaml+jinja
- name: Simple Scale Down policy
  community.aws.ec2_scaling_policy:
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
- community.aws.ec2_scaling_policy:
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
```

## [Return Values](ec2_scaling_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **adjustment_type**  string | Scaling policy adjustment type  Returned: always  Sample: `"PercentChangeInCapacity"` |
| **alarms**  complex | Cloudwatch alarms related to the policy  Returned: always |
| **alarm_arn**  string | ARN of the Cloudwatch alarm  Returned: always  Sample: `"arn:aws:cloudwatch:us-east-2:1234567890:alarm:cpu-very-high"` |
| **alarm_name**  string | name of the Cloudwatch alarm  Returned: always  Sample: `"cpu-very-high"` |
| **arn**  string | ARN of the scaling policy. Provided for backward compatibility, value is the same as *policy_arn*  Returned: always  Sample: `"arn:aws:autoscaling:us-east-2:123456789012:scalingPolicy:59e37526-bd27-42cf-adca-5cd3d90bc3b9:autoScalingGroupName/app-asg:policyName/app-policy"` |
| **as_name**  string | Auto Scaling Group name. Provided for backward compatibility, value is the same as *auto_scaling_group_name*  Returned: always  Sample: `"app-asg"` |
| **auto_scaling_group_name**  string | Name of Auto Scaling Group  Returned: always  Sample: `"app-asg"` |
| **metric_aggregation_type**  string | Method used to aggregate metrics  Returned: when *policy_type* is `StepScaling`  Sample: `"Maximum"` |
| **name**  string | Name of the scaling policy. Provided for backward compatibility, value is the same as *policy_name*  Returned: always  Sample: `"app-policy"` |
| **policy_arn**  string | ARN of scaling policy.  Returned: always  Sample: `"arn:aws:autoscaling:us-east-2:123456789012:scalingPolicy:59e37526-bd27-42cf-adca-5cd3d90bc3b9:autoScalingGroupName/app-asg:policyName/app-policy"` |
| **policy_name**  string | Name of scaling policy  Returned: always  Sample: `"app-policy"` |
| **policy_type**  string | Type of auto scaling policy  Returned: always  Sample: `"StepScaling"` |
| **scaling_adjustment**  integer | Adjustment to make when alarm is triggered  Returned: When *policy_type* is `SimpleScaling`  Sample: `1` |
| **step_adjustments**  complex | List of step adjustments  Returned: always |
| **metric_interval_lower_bound**  float | Lower bound for metric interval  Returned: if step has a lower bound  Sample: `20.0` |
| **metric_interval_upper_bound**  float | Upper bound for metric interval  Returned: if step has an upper bound  Sample: `40.0` |
| **scaling_adjustment**  integer | Adjustment to make if this step is reached  Returned: always  Sample: `50` |

### Authors

- Zacharie Eakin (@zeekin)
- Will Thames (@willthames)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
