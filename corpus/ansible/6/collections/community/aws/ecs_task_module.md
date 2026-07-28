---
collection: ansible
version: "6"
title: "community.aws.ecs_task module – Run, start or stop a task in ecs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ecs_task_module.html
fetched_at: 2026-07-27T17:04:20+00:00
---
# community.aws.ecs_task module – Run, start or stop a task in ecs

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
> see [Requirements](ecs_task_module.md#ansible-collections-community-aws-ecs-task-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ecs_task`.

New in community.aws 1.0.0

- [Synopsis](ecs_task_module.md#synopsis)
- [Requirements](ecs_task_module.md#requirements)
- [Parameters](ecs_task_module.md#parameters)
- [Notes](ecs_task_module.md#notes)
- [Examples](ecs_task_module.md#examples)
- [Return Values](ecs_task_module.md#return-values)

## [Synopsis](ecs_task_module.md#id1)

- Creates or deletes instances of task definitions.

## [Requirements](ecs_task_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ecs_task_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **cluster**  string | The name of the cluster to run the task on.  If not specified, the cluster name will be `default`.  Default: `"default"` |
| **container_instances**  list / elements=string | The list of container instances on which to deploy the task. |
| **count**  integer | How many new instances to start. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **launch_type**  string | The launch type on which to run your service.  Choices:   - `"EC2"` - `"FARGATE"` |
| **network_configuration**  dictionary | Network configuration of the service. Only applicable for task definitions created with *network_mode=awsvpc*. |
| **assign_public_ip**  boolean  added in community.aws 1.5.0 | Whether the task’s elastic network interface receives a public IP address.  Choices:   - `false` - `true` |
| **security_groups**  list / elements=string | A list of group names or group IDs for the task. |
| **subnets**  list / elements=string | A list of subnet IDs to which the task is attached. |
| **operation**  string / required | Which task operation to execute.  When *operation=run* *task_definition* must be set.  When *operation=start* both *task_definition* and *container_instances* must be set.  When *operation=stop* both *task_definition* and *task* must be set.  Choices:   - `"run"` - `"start"` - `"stop"` |
| **overrides**  dictionary | A dictionary of values to pass to the new instances. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **started_by**  string | A value showing who or what started the task (for informational purposes). |
| **tags**  dictionary | Tags that will be added to ecs tasks on start and run |
| **task**  string | The ARN of the task to stop. |
| **task_definition**  string | The task definition to start, run or stop. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ecs_task_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ecs_task_module.md#id5)

```yaml+jinja
# Simple example of run task
- name: Run task
  community.aws.ecs_task:
    operation: run
    cluster: console-sample-app-static-cluster
    task_definition: console-sample-app-static-taskdef
    count: 1
    started_by: ansible_user
  register: task_output

# Simple example of start task

- name: Start a task
  community.aws.ecs_task:
      operation: start
      cluster: console-sample-app-static-cluster
      task_definition: console-sample-app-static-taskdef
      task: "arn:aws:ecs:us-west-2:172139249013:task/3f8353d1-29a8-4689-bbf6-ad79937ffe8a"
      tags:
        resourceName: a_task_for_ansible_to_run
        type: long_running_task
        network: internal
        version: 1.4
      container_instances:
      - arn:aws:ecs:us-west-2:172139249013:container-instance/79c23f22-876c-438a-bddf-55c98a3538a8
      started_by: ansible_user
      network_configuration:
        subnets:
        - subnet-abcd1234
        security_groups:
        - sg-aaaa1111
        - my_security_group
  register: task_output

- name: RUN a task on Fargate
  community.aws.ecs_task:
      operation: run
      cluster: console-sample-app-static-cluster
      task_definition: console-sample-app-static-taskdef
      task: "arn:aws:ecs:us-west-2:172139249013:task/3f8353d1-29a8-4689-bbf6-ad79937ffe8a"
      started_by: ansible_user
      launch_type: FARGATE
      network_configuration:
        subnets:
        - subnet-abcd1234
        security_groups:
        - sg-aaaa1111
        - my_security_group
  register: task_output

- name: RUN a task on Fargate with public ip assigned
  community.aws.ecs_task:
      operation: run
      count: 2
      cluster: console-sample-app-static-cluster
      task_definition: console-sample-app-static-taskdef
      task: "arn:aws:ecs:us-west-2:172139249013:task/3f8353d1-29a8-4689-bbf6-ad79937ffe8a"
      started_by: ansible_user
      launch_type: FARGATE
      network_configuration:
        assign_public_ip: yes
        subnets:
        - subnet-abcd1234
  register: task_output

- name: Stop a task
  community.aws.ecs_task:
      operation: stop
      cluster: console-sample-app-static-cluster
      task_definition: console-sample-app-static-taskdef
      task: "arn:aws:ecs:us-west-2:172139249013:task/3f8353d1-29a8-4689-bbf6-ad79937ffe8a"
```

## [Return Values](ecs_task_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **task**  complex | details about the task that was started  Returned: success |
| **clusterArn**  string | The Amazon Resource Name (ARN) of the of the cluster that hosts the task.  Returned: only when details is true |
| **containerInstanceArn**  string | The Amazon Resource Name (ARN) of the container running the task.  Returned: only when details is true |
| **containers**  list / elements=dictionary | The container details.  Returned: only when details is true |
| **createdAt**  string | The timestamp of when the task was created.  Returned: only when details is true |
| **desiredStatus**  string | The desired status of the task.  Returned: only when details is true |
| **lastStatus**  string | The last recorded status of the task.  Returned: only when details is true |
| **launchType**  string | The launch type on which to run your task.  Returned: always |
| **overrides**  list / elements=dictionary | The container overrides set for this task.  Returned: only when details is true |
| **startedAt**  string | The timestamp of when the task was started.  Returned: only when details is true |
| **startedBy**  string | The used who started the task.  Returned: only when details is true |
| **stoppedAt**  string | The timestamp of when the task was stopped.  Returned: only when details is true |
| **stoppedReason**  string | The reason why the task was stopped.  Returned: only when details is true |
| **taskArn**  string | The Amazon Resource Name (ARN) that identifies the task.  Returned: always |
| **taskDefinitionArn**  string | The Amazon Resource Name (ARN) of the task definition.  Returned: only when details is true |

### Authors

- Mark Chance (@Java1Guy)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
