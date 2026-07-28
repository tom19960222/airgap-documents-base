---
collection: ansible
version: "6"
title: "community.aws.aws_batch_compute_environment module – Manage AWS Batch Compute Environments"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_batch_compute_environment_module.html
fetched_at: 2026-07-27T17:03:14+00:00
---
# community.aws.aws_batch_compute_environment module – Manage AWS Batch Compute Environments

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
> see [Requirements](aws_batch_compute_environment_module.md#ansible-collections-community-aws-aws-batch-compute-environment-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_batch_compute_environment`.

New in community.aws 1.0.0

- [Synopsis](aws_batch_compute_environment_module.md#synopsis)
- [Requirements](aws_batch_compute_environment_module.md#requirements)
- [Parameters](aws_batch_compute_environment_module.md#parameters)
- [Notes](aws_batch_compute_environment_module.md#notes)
- [Examples](aws_batch_compute_environment_module.md#examples)
- [Return Values](aws_batch_compute_environment_module.md#return-values)

## [Synopsis](aws_batch_compute_environment_module.md#id1)

- This module allows the management of AWS Batch Compute Environments.
- It is idempotent and supports “Check” mode.
- Use module [community.aws.aws_batch_compute_environment](aws_batch_compute_environment_module.md#ansible-collections-community-aws-aws-batch-compute-environment-module) to manage the compute environment, [community.aws.aws_batch_job_queue](aws_batch_job_queue_module.md#ansible-collections-community-aws-aws-batch-job-queue-module) to manage job queues, [community.aws.aws_batch_job_definition](aws_batch_job_definition_module.md#ansible-collections-community-aws-aws-batch-job-definition-module) to manage job definitions.

## [Requirements](aws_batch_compute_environment_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_batch_compute_environment_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **bid_percentage**  integer | The minimum percentage that a Spot Instance price must be when compared with the On-Demand price for that instance type before instances are launched.  For example, if your bid percentage is 20%, then the Spot price must be below 20% of the current On-Demand price for that EC2 instance. |
| **compute_environment_name**  string / required | The name for your compute environment.  Up to 128 letters (uppercase and lowercase), numbers, and underscores are allowed. |
| **compute_environment_state**  string | The state of the compute environment.  If the state is `ENABLED`, then the compute environment accepts jobs from a queue and can scale out automatically based on queues.  Choices:   - `"ENABLED"` ← (default) - `"DISABLED"` |
| **compute_resource_type**  string / required | The type of compute resource.  Choices:   - `"EC2"` - `"SPOT"` |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **desiredv_cpus**  integer | The desired number of EC2 vCPUS in the compute environment. |
| **ec2_key_pair**  string | The EC2 key pair that is used for instances launched in the compute environment. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **image_id**  string | The Amazon Machine Image (AMI) ID used for instances launched in the compute environment. |
| **instance_role**  string / required | The Amazon ECS instance role applied to Amazon EC2 instances in a compute environment. |
| **instance_types**  list / elements=string / required | The instance types that may be launched. |
| **maxv_cpus**  integer / required | The maximum number of EC2 vCPUs that an environment can reach. |
| **minv_cpus**  integer / required | The minimum number of EC2 vCPUs that an environment should maintain. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_group_ids**  list / elements=string / required | The EC2 security groups that are associated with instances launched in the compute environment. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **service_role**  string / required | The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf. |
| **spot_iam_fleet_role**  string | The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a SPOT compute environment. |
| **state**  string | Describes the desired state.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnets**  list / elements=string / required | The VPC subnets into which the compute resources are launched. |
| **tags**  dictionary | Key-value pair tags to be applied to resources that are launched in the compute environment. |
| **type**  string / required | The type of the compute environment.  Choices:   - `"MANAGED"` - `"UNMANAGED"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](aws_batch_compute_environment_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_batch_compute_environment_module.md#id5)

```yaml+jinja
- name: My Batch Compute Environment
  community.aws.aws_batch_compute_environment:
    compute_environment_name: computeEnvironmentName
    state: present
    region: us-east-1
    compute_environment_state: ENABLED
    type: MANAGED
    compute_resource_type: EC2
    minv_cpus: 0
    maxv_cpus: 2
    desiredv_cpus: 1
    instance_types:
      - optimal
    subnets:
      - my-subnet1
      - my-subnet2
    security_group_ids:
      - my-sg1
      - my-sg2
    instance_role: arn:aws:iam::<account>:instance-profile/<role>
    tags:
      tag1: value1
      tag2: value2
    service_role: arn:aws:iam::<account>:role/service-role/<role>
  register: aws_batch_compute_environment_action

- name: show results
  ansible.builtin.debug:
    var: aws_batch_compute_environment_action
```

## [Return Values](aws_batch_compute_environment_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  dictionary | returns what action was taken, whether something was changed, invocation and response  Returned: always  Sample: `{"batch_compute_environment_action": "none", "changed": false, "invocation": {"module_args": {"aws_access_key": null, "aws_secret_key": null, "bid_percentage": null, "compute_environment_name": "<name>", "compute_environment_state": "ENABLED", "compute_resource_type": "EC2", "desiredv_cpus": 0, "ec2_key_pair": null, "ec2_url": null, "image_id": null, "instance_role": "arn:aws:iam::...", "instance_types": ["optimal"], "maxv_cpus": 8, "minv_cpus": 0, "profile": null, "region": "us-east-1", "security_group_ids": ["*******"], "security_token": null, "service_role": "arn:aws:iam::....", "spot_iam_fleet_role": null, "state": "present", "subnets": ["******"], "tags": {"Environment": "<name>", "Name": "<name>"}, "type": "MANAGED", "validate_certs": true}}, "response": {"computeEnvironmentArn": "arn:aws:batch:....", "computeEnvironmentName": "<name>", "computeResources": {"desiredvCpus": 0, "instanceRole": "arn:aws:iam::...", "instanceTypes": ["optimal"], "maxvCpus": 8, "minvCpus": 0, "securityGroupIds": ["******"], "subnets": ["*******"], "tags": {"Environment": "<name>", "Name": "<name>"}, "type": "EC2"}, "ecsClusterArn": "arn:aws:ecs:.....", "serviceRole": "arn:aws:iam::...", "state": "ENABLED", "status": "VALID", "statusReason": "ComputeEnvironment Healthy", "type": "MANAGED"}}` |

### Authors

- Jon Meran (@jonmer85)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
