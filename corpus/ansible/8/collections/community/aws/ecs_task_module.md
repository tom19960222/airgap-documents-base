---
collection: ansible
version: "8"
title: "community.aws.ecs_task module – Run, start or stop a task in ECS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/ecs_task_module.html
fetched_at: 2026-07-28T01:40:59+00:00
---
# community.aws.ecs_task module – Run, start or stop a task in ECS

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
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ecs_task_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **cluster**  string | The name of the cluster to run the task on.  If not specified, the cluster name will be `default`.  **Default:** `"default"` |
| **container_instances**  list / elements=string | The list of container instances on which to deploy the task. |
| **count**  integer | How many new instances to start. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **launch_type**  string | The launch type on which to run your service.  **Choices:**   - `"EC2"` - `"FARGATE"` |
| **network_configuration**  dictionary | Network configuration of the service. Only applicable for task definitions created with *network_mode=awsvpc*. |
| **assign_public_ip**  boolean  *added in community.aws 1.5.0* | Whether the task’s elastic network interface receives a public IP address.  **Choices:**   - `false` - `true` |
| **security_groups**  list / elements=string | A list of group names or group IDs for the task. |
| **subnets**  list / elements=string | A list of subnet IDs to which the task is attached. |
| **operation**  string / required | Which task operation to execute.  When *operation=run* *task_definition* must be set.  When *operation=start* both *task_definition* and *container_instances* must be set.  When *operation=stop* both *task_definition* and *task* must be set.  **Choices:**   - `"run"` - `"start"` - `"stop"` |
| **overrides**  dictionary | A dictionary of values to pass to the new instances. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **started_by**  string | A value showing who or what started the task (for informational purposes). |
| **tags**  aliases: resource_tags  dictionary | Tags that will be added to ecs tasks on start and run |
| **task**  string | The ARN of the task to stop. |
| **task_definition**  string | The task definition to start, run or stop. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean  *added in community.aws 4.1.0* | Whether or not to wait for the desired state.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ecs_task_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

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
      task: "arn:aws:ecs:us-west-2:123456789012:task/3f8353d1-29a8-4689-bbf6-ad79937ffe8a"
      tags:
        resourceName: a_task_for_ansible_to_run
        type: long_running_task
        network: internal
        version: 1.4
      container_instances:
      - arn:aws:ecs:us-west-2:123456789012:container-instance/79c23f22-876c-438a-bddf-55c98a3538a8
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
      task: "arn:aws:ecs:us-west-2:123456789012:task/3f8353d1-29a8-4689-bbf6-ad79937ffe8a"
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
      task: "arn:aws:ecs:us-west-2:123456789012:task/3f8353d1-29a8-4689-bbf6-ad79937ffe8a"
      started_by: ansible_user
      launch_type: FARGATE
      network_configuration:
        assign_public_ip: true
        subnets:
        - subnet-abcd1234
  register: task_output

- name: Stop a task
  community.aws.ecs_task:
      operation: stop
      cluster: console-sample-app-static-cluster
      task_definition: console-sample-app-static-taskdef
      task: "arn:aws:ecs:us-west-2:123456789012:task/3f8353d1-29a8-4689-bbf6-ad79937ffe8a"
```

## [Return Values](ecs_task_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **task**  complex | details about the task that was started  **Returned:** success |
| **clusterArn**  string | The Amazon Resource Name (ARN) of the of the cluster that hosts the task.  **Returned:** only when details is true |
| **containerInstanceArn**  string | The Amazon Resource Name (ARN) of the container running the task.  **Returned:** only when details is true |
| **containers**  list / elements=dictionary | The container details.  **Returned:** only when details is true |
| **createdAt**  string | The timestamp of when the task was created.  **Returned:** only when details is true |
| **desiredStatus**  string | The desired status of the task.  **Returned:** only when details is true |
| **lastStatus**  string | The last recorded status of the task.  **Returned:** only when details is true |
| **launchType**  string | The launch type on which to run your task.  **Returned:** always |
| **overrides**  list / elements=dictionary | The container overrides set for this task.  **Returned:** only when details is true |
| **startedAt**  string | The timestamp of when the task was started.  **Returned:** only when details is true |
| **startedBy**  string | The used who started the task.  **Returned:** only when details is true |
| **stoppedAt**  string | The timestamp of when the task was stopped.  **Returned:** only when details is true |
| **stoppedReason**  string | The reason why the task was stopped.  **Returned:** only when details is true |
| **taskArn**  string | The Amazon Resource Name (ARN) that identifies the task.  **Returned:** always |
| **taskDefinitionArn**  string | The Amazon Resource Name (ARN) of the task definition.  **Returned:** only when details is true |

### Authors

- Mark Chance (@Java1Guy)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
