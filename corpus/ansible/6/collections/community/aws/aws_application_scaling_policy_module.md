---
collection: ansible
version: "6"
title: "community.aws.aws_application_scaling_policy module – Manage Application Auto Scaling Scaling Policies"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_application_scaling_policy_module.html
fetched_at: 2026-07-27T17:03:13+00:00
---
# community.aws.aws_application_scaling_policy module – Manage Application Auto Scaling Scaling Policies

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
> see [Requirements](aws_application_scaling_policy_module.md#ansible-collections-community-aws-aws-application-scaling-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_application_scaling_policy`.

New in community.aws 1.0.0

- [Synopsis](aws_application_scaling_policy_module.md#synopsis)
- [Requirements](aws_application_scaling_policy_module.md#requirements)
- [Parameters](aws_application_scaling_policy_module.md#parameters)
- [Notes](aws_application_scaling_policy_module.md#notes)
- [Examples](aws_application_scaling_policy_module.md#examples)
- [Return Values](aws_application_scaling_policy_module.md#return-values)

## [Synopsis](aws_application_scaling_policy_module.md#id1)

- Creates, updates or removes a Scaling Policy.

## [Requirements](aws_application_scaling_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_application_scaling_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **maximum_tasks**  integer | The maximum value to scale to in response to a scale out event. This parameter is required if you are creating a first new policy for the specified service. |
| **minimum_tasks**  integer | The minimum value to scale to in response to a scale in event. This parameter is required if you are creating a first new policy for the specified service. |
| **override_task_capacity**  boolean | Whether or not to override values of minimum and/or maximum tasks if it’s already set.  Defaults to `false`.  Choices:   - `false` - `true` |
| **policy_name**  string / required | The name of the scaling policy. |
| **policy_type**  string / required | The policy type.  Choices:   - `"StepScaling"` - `"TargetTrackingScaling"` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **resource_id**  string / required | The identifier of the resource associated with the scalable target. |
| **scalable_dimension**  string / required | The scalable dimension associated with the scalable target.  Choices:   - `"ecs:service:DesiredCount"` - `"ec2:spot-fleet-request:TargetCapacity"` - `"elasticmapreduce:instancegroup:InstanceCount"` - `"appstream:fleet:DesiredCapacity"` - `"dynamodb:table:ReadCapacityUnits"` - `"dynamodb:table:WriteCapacityUnits"` - `"dynamodb:index:ReadCapacityUnits"` - `"dynamodb:index:WriteCapacityUnits"` |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **service_namespace**  string / required | The namespace of the AWS service.  Choices:   - `"ecs"` - `"elasticmapreduce"` - `"ec2"` - `"appstream"` - `"dynamodb"` |
| **state**  string / required | Whether a policy should be `present` or `absent`.  Choices:   - `"absent"` - `"present"` |
| **step_scaling_policy_configuration**  dictionary | A step scaling policy. This parameter is required if you are creating a policy and *policy_type=StepScaling*. |
| **target_tracking_scaling_policy_configuration**  dictionary | A target tracking policy. This parameter is required if you are creating a new policy and *policy_type=TargetTrackingScaling*.  Full documentation of the suboptions can be found in the API documentation:  <https://docs.aws.amazon.com/autoscaling/application/APIReference/API_TargetTrackingScalingPolicyConfiguration.html> |
| **CustomizedMetricSpecification**  dictionary | The metric to use if using a customized metric. |
| **DisableScaleIn**  boolean | Whether scaling-in should be disabled.  Choices:   - `false` - `true` |
| **PredefinedMetricSpecification**  dictionary | The metric to use if using a predefined metric. |
| **ScaleInCooldown**  integer | The time (in seconds) to wait after scaling-in before another scaling action can occur. |
| **ScaleOutCooldown**  integer | The time (in seconds) to wait after scaling-out before another scaling action can occur. |
| **TargetValue**  float | The target value for the metric. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](aws_application_scaling_policy_module.md#id4)

> **Note:**
>
> - for details of the parameters and returns see <http://boto3.readthedocs.io/en/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.put_scaling_policy>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_application_scaling_policy_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create step scaling policy for ECS Service
- name: scaling_policy
  community.aws.aws_application_scaling_policy:
    state: present
    policy_name: test_policy
    service_namespace: ecs
    resource_id: service/poc-pricing/test-as
    scalable_dimension: ecs:service:DesiredCount
    policy_type: StepScaling
    minimum_tasks: 1
    maximum_tasks: 6
    step_scaling_policy_configuration:
      AdjustmentType: ChangeInCapacity
      StepAdjustments:
        - MetricIntervalUpperBound: 123
          ScalingAdjustment: 2
        - MetricIntervalLowerBound: 123
          ScalingAdjustment: -2
      Cooldown: 123
      MetricAggregationType: Average

# Create target tracking scaling policy for ECS Service
- name: scaling_policy
  community.aws.aws_application_scaling_policy:
    state: present
    policy_name: test_policy
    service_namespace: ecs
    resource_id: service/poc-pricing/test-as
    scalable_dimension: ecs:service:DesiredCount
    policy_type: TargetTrackingScaling
    minimum_tasks: 1
    maximum_tasks: 6
    target_tracking_scaling_policy_configuration:
      TargetValue: 60
      PredefinedMetricSpecification:
        PredefinedMetricType: ECSServiceAverageCPUUtilization
      ScaleOutCooldown: 60
      ScaleInCooldown: 60

# Remove scalable target for ECS Service
- name: scaling_policy
  community.aws.aws_application_scaling_policy:
    state: absent
    policy_name: test_policy
    policy_type: StepScaling
    service_namespace: ecs
    resource_id: service/cluster-name/service-name
    scalable_dimension: ecs:service:DesiredCount
```

## [Return Values](aws_application_scaling_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **alarms**  complex | List of the CloudWatch alarms associated with the scaling policy  Returned: when state present |
| **alarm_arn**  string | The Amazon Resource Name (ARN) of the alarm  Returned: when state present |
| **alarm_name**  string | The name of the alarm  Returned: when state present |
| **creation_time**  string | The Unix timestamp for when the scalable target was created.  Returned: when state present  Sample: `"2017-09-28T08:22:51.881000-03:00"` |
| **max_capacity**  integer | The maximum value to scale to in response to a scale out event. Required if *state* is `present`.  Returned: when state present  Sample: `2` |
| **min_capacity**  integer | The minimum value to scale to in response to a scale in event. Required if *state* is `present`.  Returned: when state present  Sample: `1` |
| **policy_arn**  string | The Amazon Resource Name (ARN) of the scaling policy..  Returned: when state present |
| **policy_name**  string | The name of the scaling policy.  Returned: when state present |
| **policy_type**  string | The policy type.  Returned: when state present |
| **resource_id**  string | The identifier of the resource associated with the scalable target.  Returned: when state present  Sample: `"service/cluster-name/service-name"` |
| **role_arn**  string | The ARN of an IAM role that allows Application Auto Scaling to modify the scalable target on your behalf. Required if *state* is `present`.  Returned: when state present  Sample: `"arn:aws:iam::123456789123:role/roleName"` |
| **scalable_dimension**  string | The scalable dimension associated with the scalable target.  Returned: when state present  Sample: `"ecs:service:DesiredCount"` |
| **service_namespace**  string | The namespace of the AWS service.  Returned: when state present  Sample: `"ecs"` |
| **step_scaling_policy_configuration**  complex | The step scaling policy.  Returned: when state present and the policy type is StepScaling |
| **adjustment_type**  string | The adjustment type  Returned: when state present and the policy type is StepScaling  Sample: `"ChangeInCapacity, PercentChangeInCapacity, ExactCapacity"` |
| **cooldown**  integer | The amount of time, in seconds, after a scaling activity completes where previous trigger-related scaling activities can influence future scaling events  Returned: when state present and the policy type is StepScaling  Sample: `60` |
| **metric_aggregation_type**  string | The aggregation type for the CloudWatch metrics  Returned: when state present and the policy type is StepScaling  Sample: `"Average, Minimum, Maximum"` |
| **step_adjustments**  list / elements=dictionary | A set of adjustments that enable you to scale based on the size of the alarm breach  Returned: when state present and the policy type is StepScaling |
| **target_tracking_scaling_policy_configuration**  complex | The target tracking policy.  Returned: when state present and the policy type is TargetTrackingScaling |
| **predefined_metric_specification**  complex | A predefined metric  Returned: when state present and the policy type is TargetTrackingScaling |
| **predefined_metric_type**  string | The metric type  Returned: when state present and the policy type is TargetTrackingScaling  Sample: `"ECSServiceAverageCPUUtilization, ECSServiceAverageMemoryUtilization"` |
| **resource_label**  string | Identifies the resource associated with the metric type  Returned: when metric type is ALBRequestCountPerTarget |
| **scale_in_cooldown**  integer | The amount of time, in seconds, after a scale in activity completes before another scale in activity can start  Returned: when state present and the policy type is TargetTrackingScaling  Sample: `60` |
| **scale_out_cooldown**  integer | The amount of time, in seconds, after a scale out activity completes before another scale out activity can start  Returned: when state present and the policy type is TargetTrackingScaling  Sample: `60` |
| **target_value**  integer | The target value for the metric  Returned: when state present and the policy type is TargetTrackingScaling  Sample: `70` |

### Authors

- Gustavo Maia (@gurumaia)
- Chen Leibovich (@chenl87)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
