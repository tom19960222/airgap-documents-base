---
collection: ansible
version: "6"
title: "community.aws.ec2_asg_instance_refresh module – Start or cancel an EC2 Auto Scaling Group (ASG) instance refresh in AWS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ec2_asg_instance_refresh_module.html
fetched_at: 2026-07-27T17:03:54+00:00
---
# community.aws.ec2_asg_instance_refresh module – Start or cancel an EC2 Auto Scaling Group (ASG) instance refresh in AWS

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
> see [Requirements](ec2_asg_instance_refresh_module.md#ansible-collections-community-aws-ec2-asg-instance-refresh-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_asg_instance_refresh`.

New in community.aws 3.2.0

- [Synopsis](ec2_asg_instance_refresh_module.md#synopsis)
- [Requirements](ec2_asg_instance_refresh_module.md#requirements)
- [Parameters](ec2_asg_instance_refresh_module.md#parameters)
- [Notes](ec2_asg_instance_refresh_module.md#notes)
- [Examples](ec2_asg_instance_refresh_module.md#examples)
- [Return Values](ec2_asg_instance_refresh_module.md#return-values)

## [Synopsis](ec2_asg_instance_refresh_module.md#id1)

- Start or cancel an EC2 Auto Scaling Group instance refresh in AWS.
- Can be used with [community.aws.ec2_asg_instance_refresh_info](ec2_asg_instance_refresh_info_module.md#ansible-collections-community-aws-ec2-asg-instance-refresh-info-module) to track the subsequent progress.

## [Requirements](ec2_asg_instance_refresh_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_asg_instance_refresh_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **name**  string / required | The name of the auto scaling group you are searching for. |
| **preferences**  dictionary | Set of preferences associated with the instance refresh request.  If not provided, the default values are used.  For *min_healthy_percentage*, the default value is `90`.  For *instance_warmup*, the default is to use the value specified for the health check grace period for the Auto Scaling group.  Can not be specified when *state* is set to ‘cancelled’. |
| **instance_warmup**  integer | The number of seconds until a newly launched instance is configured and ready to use.  During this time, Amazon EC2 Auto Scaling does not immediately move on to the next replacement.  The default is to use the value for the health check grace period defined for the group. |
| **min_healthy_percentage**  integer | Total percent of capacity in ASG that must remain healthy during instance refresh to allow operation to continue.  It is rounded up to the nearest integer.  Default: `90` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string / required | Desired state of the ASG.  Choices:   - `"started"` - `"cancelled"` |
| **strategy**  string | The strategy to use for the instance refresh. The only valid value is `Rolling`.  A rolling update is an update that is applied to all instances in an Auto Scaling group until all instances have been updated.  A rolling update can fail due to failed health checks or if instances are on standby or are protected from scale in.  If the rolling update process fails, any instances that were already replaced are not rolled back to their previous configuration.  Default: `"Rolling"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ec2_asg_instance_refresh_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_asg_instance_refresh_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Start a refresh
  community.aws.ec2_asg_instance_refresh:
    name: some-asg
    state: started

- name: Cancel a refresh
  community.aws.ec2_asg_instance_refresh:
    name: some-asg
    state: cancelled

- name: Start a refresh and pass preferences
  community.aws.ec2_asg_instance_refresh:
    name: some-asg
    state: started
    preferences:
      min_healthy_percentage: 91
      instance_warmup: 60
```

## [Return Values](ec2_asg_instance_refresh_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **auto_scaling_group_name**  string | Name of autoscaling group  Returned: success  Sample: `"public-webapp-production-1"` |
| **end_time**  string | The date and time this ASG was created, in ISO 8601 format.  Returned: success  Sample: `"2015-11-25T00:05:36.309Z"` |
| **instance_refresh_id**  string | instance refresh id  Returned: success  Sample: `"08b91cf7-8fa6-48af-b6a6-d227f40f1b9b"` |
| **instances_to_update**  integer | num. of instance to update  Returned: success  Sample: `5` |
| **percentage_complete**  integer | the % of completeness  Returned: success  Sample: `100` |
| **start_time**  string | The date and time this ASG was created, in ISO 8601 format.  Returned: success  Sample: `"2015-11-25T00:05:36.309Z"` |
| **status**  string | The current state of the group when DeleteAutoScalingGroup is in progress.  The following are the possible statuses  Pending – The request was created, but the operation has not started.  InProgress – The operation is in progress.  Successful – The operation completed successfully.  Failed – The operation failed to complete. You can troubleshoot using the status reason and the scaling activities.  Cancelling –  An ongoing operation is being cancelled.  Cancellation does not roll back any replacements that have already been completed,  but it prevents new replacements from being started.  Cancelled – The operation is cancelled.  Returned: success  Sample: `"Pending"` |

### Authors

- Dan Khersonsky (@danquixote)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
