---
collection: ansible
version: "6"
title: "community.aws.ec2_asg module – Create or delete AWS AutoScaling Groups (ASGs)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ec2_asg_module.html
fetched_at: 2026-07-27T17:03:53+00:00
---
# community.aws.ec2_asg module – Create or delete AWS AutoScaling Groups (ASGs)

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
> see [Requirements](ec2_asg_module.md#ansible-collections-community-aws-ec2-asg-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_asg`.

New in community.aws 1.0.0

- [Synopsis](ec2_asg_module.md#synopsis)
- [Requirements](ec2_asg_module.md#requirements)
- [Parameters](ec2_asg_module.md#parameters)
- [Notes](ec2_asg_module.md#notes)
- [Examples](ec2_asg_module.md#examples)
- [Return Values](ec2_asg_module.md#return-values)

## [Synopsis](ec2_asg_module.md#id1)

- Can create or delete AWS AutoScaling Groups.
- Can be used with the [community.aws.ec2_lc](ec2_lc_module.md#ansible-collections-community-aws-ec2-lc-module) module to manage Launch Configurations.

## [Requirements](ec2_asg_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_asg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **availability_zones**  list / elements=string | List of availability zone names in which to create the group.  Defaults to all the availability zones in the region if *vpc_zone_identifier* is not set. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **decrement_desired_capacity**  boolean  added in community.aws 3.2.0 | Indicates whether the AutoScalingGroup decrements the desired capacity value by the number of instances detached.  Choices:   - `false` ← (default) - `true` |
| **default_cooldown**  integer | The number of seconds after a scaling activity completes before another can begin.  Default: `300` |
| **desired_capacity**  integer | Desired number of instances in group, if unspecified then the current group value will be used. |
| **detach_instances**  list / elements=string  added in community.aws 3.2.0 | Removes one or more instances from the specified AutoScalingGroup.  If *decrement_desired_capacity* flag is not set, new instance(s) are launched to replace the detached instance(s).  If a Classic Load Balancer is attached to the AutoScalingGroup, the instances are also deregistered from the load balancer.  If there are target groups attached to the AutoScalingGroup, the instances are also deregistered from the target groups. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **health_check_period**  integer | Length of time in seconds after a new EC2 instance comes into service that Auto Scaling starts checking its health.  Default: `300` |
| **health_check_type**  string | The service you want the health status from, Amazon EC2 or Elastic Load Balancer.  Choices:   - `"EC2"` ← (default) - `"ELB"` |
| **launch_config_name**  string | Name of the Launch configuration to use for the group. See the community.aws.ec2_lc) module for managing these.  If unspecified then the current group value will be used. One of *launch_config_name* or *launch_template* must be provided. |
| **launch_template**  dictionary | Dictionary describing the Launch Template to use |
| **launch_template_id**  string | The id of the launch template. Only one of *launch_template_name* or *launch_template_id* is required. |
| **launch_template_name**  string | The name of the launch template. Only one of *launch_template_name* or *launch_template_id* is required. |
| **version**  string | The version number of the launch template to use.  Defaults to latest version if not provided. |
| **lc_check**  boolean | Check to make sure instances that are being replaced with *replace_instances* do not already have the current *launch_config*.  Choices:   - `false` - `true` ← (default) |
| **load_balancers**  list / elements=string | List of ELB names to use for the group. Use for classic load balancers. |
| **lt_check**  boolean | Check to make sure instances that are being replaced with *replace_instances* do not already have the current *launch_template or I(launch_template* *version*.  Choices:   - `false` - `true` ← (default) |
| **max_instance_lifetime**  integer | The maximum amount of time, in seconds, that an instance can be in service.  Maximum instance lifetime must be equal to 0, between 604800 and 31536000 seconds (inclusive), or not specified.  Value of 0 removes lifetime restriction. |
| **max_size**  integer | Maximum number of instances in group, if unspecified then the current group value will be used. |
| **metrics_collection**  boolean | Enable ASG metrics collection.  Choices:   - `false` ← (default) - `true` |
| **metrics_granularity**  string | When *metrics_collection=true* this will determine the granularity of metrics collected by CloudWatch.  Default: `"1Minute"` |
| **metrics_list**  list / elements=string | List of autoscaling metrics to collect when *metrics_collection=true*.  Default: `["GroupMinSize", "GroupMaxSize", "GroupDesiredCapacity", "GroupInServiceInstances", "GroupPendingInstances", "GroupStandbyInstances", "GroupTerminatingInstances", "GroupTotalInstances"]` |
| **min_size**  integer | Minimum number of instances in group, if unspecified then the current group value will be used. |
| **mixed_instances_policy**  dictionary | A mixed instance policy to use for the ASG.  Only used when the ASG is configured to use a Launch Template (*launch_template*).  See also <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-mixedinstancespolicy.html> |
| **instance_types**  list / elements=string | A list of instance_types. |
| **instances_distribution**  dictionary  added in community.aws 1.5.0 | Specifies the distribution of On-Demand Instances and Spot Instances, the maximum price to pay for Spot Instances, and how the Auto Scaling group allocates instance types to fulfill On-Demand and Spot capacity.  See also <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstancesDistribution.html> |
| **on_demand_allocation_strategy**  string  added in community.aws 1.5.0 | Indicates how to allocate instance types to fulfill On-Demand capacity. |
| **on_demand_base_capacity**  integer  added in community.aws 1.5.0 | The minimum amount of the Auto Scaling group’s capacity that must be fulfilled by On-Demand Instances. This base portion is provisioned first as your group scales.  Default if not set is 0. If you leave it set to 0, On-Demand Instances are launched as a percentage of the Auto Scaling group’s desired capacity, per the OnDemandPercentageAboveBaseCapacity setting. |
| **on_demand_percentage_above_base_capacity**  integer  added in community.aws 1.5.0 | Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond OnDemandBaseCapacity.  Default if not set is 100. If you leave it set to 100, the percentages are 100% for On-Demand Instances and 0% for Spot Instances.  Valid range: 0 to 100 |
| **spot_allocation_strategy**  string  added in community.aws 1.5.0 | Indicates how to allocate instances across Spot Instance pools. |
| **spot_instance_pools**  integer  added in community.aws 1.5.0 | The number of Spot Instance pools across which to allocate your Spot Instances. The Spot pools are determined from the different instance types in the Overrides array of LaunchTemplate. Default if not set is 2.  Used only when the Spot allocation strategy is lowest-price.  Valid Range: Minimum value of 1. Maximum value of 20. |
| **spot_max_price**  string  added in community.aws 1.5.0 | The maximum price per unit hour that you are willing to pay for a Spot Instance.  If you leave the value of this parameter blank (which is the default), the maximum Spot price is set at the On-Demand price.  To remove a value that you previously set, include the parameter but leave the value blank. |
| **name**  string / required | Unique name for group to be created or deleted. |
| **notification_topic**  string | A SNS topic ARN to send auto scaling notifications to. |
| **notification_types**  list / elements=string | A list of auto scaling events to trigger notifications on.  Default: `["autoscaling:EC2_INSTANCE_LAUNCH", "autoscaling:EC2_INSTANCE_LAUNCH_ERROR", "autoscaling:EC2_INSTANCE_TERMINATE", "autoscaling:EC2_INSTANCE_TERMINATE_ERROR"]` |
| **placement_group**  string | Physical location of your cluster placement group created in Amazon EC2. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean  added in community.aws 3.2.0 | If `true`, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified.  Choices:   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **replace_all_instances**  boolean | In a rolling fashion, replace all instances that used the old launch configuration with one from the new launch configuration. It increases the ASG size by *replace_batch_size*, waits for the new instances to be up and running. After that, it terminates a batch of old instances, waits for the replacements, and repeats, until all old instances are replaced. Once that’s done the ASG size is reduced back to the expected size.  Choices:   - `false` ← (default) - `true` |
| **replace_batch_size**  integer | Number of instances you’d like to replace at a time. Used with *replace_all_instances*.  Default: `1` |
| **replace_instances**  list / elements=string | List of *instance_ids* belonging to the named AutoScalingGroup that you would like to terminate and be replaced with instances matching the current launch configuration. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Register or deregister the instance.  Choices:   - `"present"` ← (default) - `"absent"` |
| **suspend_processes**  list / elements=string | A list of scaling processes to suspend.  Valid values include:  `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`  Full documentation of valid values can be found in the AWS documentation:  <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html>  Default: `[]` |
| **tags**  list / elements=dictionary | A list of tags to add to the Auto Scale Group.  Optional key is *propagate_at_launch*, which defaults to true.  When *propagate_at_launch* is true the tags will be propagated to the Instances created. |
| **target_group_arns**  list / elements=string | List of target group ARNs to use for the group. Use for application load balancers. |
| **termination_policies**  list / elements=string | An ordered list of criteria used for selecting instances to be removed from the Auto Scaling group when reducing capacity.  Using *termination_policies=Default* when modifying an existing AutoScalingGroup will result in the existing policy being retained instead of changed to `Default`.  Valid values include: `Default`, `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`  Full documentation of valid values can be found in the AWS documentation:  <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html#custom-termination-policy>  Default: `["Default"]` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **vpc_zone_identifier**  list / elements=string | List of VPC subnets to use |
| **wait_for_instances**  boolean | Wait for the ASG instances to be in a ready state before exiting. If instances are behind an ELB, it will wait until the ELB determines all instances have a lifecycle_state of “InService” and a health_status of “Healthy”.  Choices:   - `false` - `true` ← (default) |
| **wait_timeout**  integer | How long to wait for instances to become viable when replaced. If you experience the error “Waited too long for ELB instances to be healthy”, try increasing this value.  Default: `300` |

## [Notes](ec2_asg_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_asg_module.md#id5)

```yaml+jinja
# Basic configuration with Launch Configuration

- community.aws.ec2_asg:
    name: special
    load_balancers: [ 'lb1', 'lb2' ]
    availability_zones: [ 'eu-west-1a', 'eu-west-1b' ]
    launch_config_name: 'lc-1'
    min_size: 1
    max_size: 10
    desired_capacity: 5
    vpc_zone_identifier: [ 'subnet-abcd1234', 'subnet-1a2b3c4d' ]
    tags:
      - environment: production
        propagate_at_launch: no

# Rolling ASG Updates

# Below is an example of how to assign a new launch config to an ASG and terminate old instances.
#
# All instances in "myasg" that do not have the launch configuration named "my_new_lc" will be terminated in
# a rolling fashion with instances using the current launch configuration, "my_new_lc".
#
# This could also be considered a rolling deploy of a pre-baked AMI.
#
# If this is a newly created group, the instances will not be replaced since all instances
# will have the current launch configuration.

- name: create launch config
  community.aws.ec2_lc:
    name: my_new_lc
    image_id: ami-lkajsf
    key_name: mykey
    region: us-east-1
    security_groups: sg-23423
    instance_type: m1.small
    assign_public_ip: yes

- community.aws.ec2_asg:
    name: myasg
    launch_config_name: my_new_lc
    health_check_period: 60
    health_check_type: ELB
    replace_all_instances: yes
    min_size: 5
    max_size: 5
    desired_capacity: 5
    region: us-east-1

# To only replace a couple of instances instead of all of them, supply a list
# to "replace_instances":

- community.aws.ec2_asg:
    name: myasg
    launch_config_name: my_new_lc
    health_check_period: 60
    health_check_type: ELB
    replace_instances:
    - i-b345231
    - i-24c2931
    min_size: 5
    max_size: 5
    desired_capacity: 5
    region: us-east-1

# Basic Configuration with Launch Template

- community.aws.ec2_asg:
    name: special
    load_balancers: [ 'lb1', 'lb2' ]
    availability_zones: [ 'eu-west-1a', 'eu-west-1b' ]
    launch_template:
        version: '1'
        launch_template_name: 'lt-example'
        launch_template_id: 'lt-123456'
    min_size: 1
    max_size: 10
    desired_capacity: 5
    vpc_zone_identifier: [ 'subnet-abcd1234', 'subnet-1a2b3c4d' ]
    tags:
      - environment: production
        propagate_at_launch: no

# Basic Configuration with Launch Template using mixed instance policy

- community.aws.ec2_asg:
    name: special
    load_balancers: [ 'lb1', 'lb2' ]
    availability_zones: [ 'eu-west-1a', 'eu-west-1b' ]
    launch_template:
        version: '1'
        launch_template_name: 'lt-example'
        launch_template_id: 'lt-123456'
    mixed_instances_policy:
        instance_types:
            - t3a.large
            - t3.large
            - t2.large
        instances_distribution:
            on_demand_percentage_above_base_capacity: 0
            spot_allocation_strategy: capacity-optimized
    min_size: 1
    max_size: 10
    desired_capacity: 5
    vpc_zone_identifier: [ 'subnet-abcd1234', 'subnet-1a2b3c4d' ]
    tags:
      - environment: production
        propagate_at_launch: no
```

## [Return Values](ec2_asg_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **auto_scaling_group_arn**  string | The unique ARN of the autoscaling group  Returned: success  Sample: `"arn:aws:autoscaling:us-east-1:123456789012:autoScalingGroup:6a09ad6d-eeee-1234-b987-ee123ced01ad:autoScalingGroupName/myasg"` |
| **auto_scaling_group_name**  string | The unique name of the auto scaling group  Returned: success  Sample: `"myasg"` |
| **availability_zones**  list / elements=string | The availability zones for the auto scaling group  Returned: success  Sample: `["us-east-1d"]` |
| **created_time**  string | Timestamp of create time of the auto scaling group  Returned: success  Sample: `"2017-11-08T14:41:48.272000+00:00"` |
| **default_cooldown**  integer | The default cooldown time in seconds.  Returned: success  Sample: `300` |
| **desired_capacity**  integer | The number of EC2 instances that should be running in this group.  Returned: success  Sample: `3` |
| **healthcheck_period**  integer | Length of time in seconds after a new EC2 instance comes into service that Auto Scaling starts checking its health.  Returned: success  Sample: `30` |
| **healthcheck_type**  string | The service you want the health status from, one of “EC2” or “ELB”.  Returned: success  Sample: `"ELB"` |
| **healthy_instances**  integer | Number of instances in a healthy state  Returned: success  Sample: `5` |
| **in_service_instances**  integer | Number of instances in service  Returned: success  Sample: `3` |
| **instance_facts**  dictionary | Dictionary of EC2 instances and their status as it relates to the ASG.  Returned: success  Sample: `{"i-0123456789012": {"health_status": "Healthy", "launch_config_name": "public-webapp-production-1", "lifecycle_state": "InService"}}` |
| **instances**  list / elements=string | list of instance IDs in the ASG  Returned: success  Sample: `["i-0123456789012"]` |
| **launch_config_name**  string | Name of launch configuration associated with the ASG. Same as launch_configuration_name, provided for compatibility with ec2_asg module.  Returned: success  Sample: `"public-webapp-production-1"` |
| **load_balancers**  list / elements=string | List of load balancers names attached to the ASG.  Returned: success  Sample: `["elb-webapp-prod"]` |
| **max_instance_lifetime**  integer | The maximum amount of time, in seconds, that an instance can be in service.  Returned: success  Sample: `604800` |
| **max_size**  integer | Maximum size of group  Returned: success  Sample: `3` |
| **metrics_collection**  list / elements=string | List of enabled AutosSalingGroup metrics  Returned: success  Sample: `[{"Granularity": "1Minute", "Metric": "GroupInServiceInstances"}]` |
| **min_size**  integer | Minimum size of group  Returned: success  Sample: `1` |
| **mixed_instances_policy**  list / elements=string | Returns the list of instance types if a mixed instances policy is set.  Returned: success  Sample: `["t3.micro", "t3a.micro"]` |
| **mixed_instances_policy_full**  dictionary | Returns the full dictionary representation of the mixed instances policy if a mixed instances policy is set.  Returned: success  Sample: `{"instances_distribution": {"on_demand_allocation_strategy": "prioritized", "on_demand_base_capacity": 0, "on_demand_percentage_above_base_capacity": 0, "spot_allocation_strategy": "capacity-optimized"}, "launch_template": {"launch_template_specification": {"launch_template_id": "lt-53c2425cffa544c23", "launch_template_name": "random-LaunchTemplate", "version": "2"}, "overrides": [{"instance_type": "m5.xlarge"}, {"instance_type": "m5a.xlarge"}]}}` |
| **pending_instances**  integer | Number of instances in pending state  Returned: success  Sample: `1` |
| **tags**  list / elements=string | List of tags for the ASG, and whether or not each tag propagates to instances at launch.  Returned: success  Sample: `[{"key": "Name", "propagate_at_launch": "true", "resource_id": "public-webapp-production-1", "resource_type": "auto-scaling-group", "value": "public-webapp-production-1"}, {"key": "env", "propagate_at_launch": "true", "resource_id": "public-webapp-production-1", "resource_type": "auto-scaling-group", "value": "production"}]` |
| **target_group_arns**  list / elements=string | List of ARNs of the target groups that the ASG populates  Returned: success  Sample: `["arn:aws:elasticloadbalancing:ap-southeast-2:123456789012:targetgroup/target-group-host-hello/1a2b3c4d5e6f1a2b", "arn:aws:elasticloadbalancing:ap-southeast-2:123456789012:targetgroup/target-group-path-world/abcd1234abcd1234"]` |
| **target_group_names**  list / elements=string | List of names of the target groups that the ASG populates  Returned: success  Sample: `["target-group-host-hello", "target-group-path-world"]` |
| **termination_policies**  list / elements=string | A list of termination policies for the group.  Returned: success  Sample: `["Default"]` |
| **unhealthy_instances**  integer | Number of instances in an unhealthy state  Returned: success  Sample: `0` |
| **viable_instances**  integer | Number of instances in a viable state  Returned: success  Sample: `1` |
| **vpc_zone_identifier**  string | VPC zone ID / subnet id for the auto scaling group  Returned: success  Sample: `"subnet-a31ef45f"` |

### Authors

- Gareth Rushgrove (@garethr)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
