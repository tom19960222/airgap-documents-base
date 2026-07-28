---
collection: ansible
version: "6"
title: "community.aws.ecs_taskdefinition_info module – Describe a task definition in ECS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ecs_taskdefinition_info_module.html
fetched_at: 2026-07-27T17:04:21+00:00
---
# community.aws.ecs_taskdefinition_info module – Describe a task definition in ECS

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
> see [Requirements](ecs_taskdefinition_info_module.md#ansible-collections-community-aws-ecs-taskdefinition-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ecs_taskdefinition_info`.

New in community.aws 1.0.0

- [Synopsis](ecs_taskdefinition_info_module.md#synopsis)
- [Requirements](ecs_taskdefinition_info_module.md#requirements)
- [Parameters](ecs_taskdefinition_info_module.md#parameters)
- [Notes](ecs_taskdefinition_info_module.md#notes)
- [Examples](ecs_taskdefinition_info_module.md#examples)
- [Return Values](ecs_taskdefinition_info_module.md#return-values)

## [Synopsis](ecs_taskdefinition_info_module.md#id1)

- Describes a task definition in ECS.

## [Requirements](ecs_taskdefinition_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ecs_taskdefinition_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **task_definition**  string / required | The name of the task definition to get details for |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ecs_taskdefinition_info_module.md#id4)

> **Note:**
>
> - For details of the parameters and returns see <http://boto3.readthedocs.io/en/latest/reference/services/ecs.html#ECS.Client.describe_task_definition>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ecs_taskdefinition_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- community.aws.ecs_taskdefinition_info:
    task_definition: test-td
```

## [Return Values](ecs_taskdefinition_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **container_definitions**  complex | Returns a list of complex objects representing the containers  Returned: success |
| **command**  string | The command that is passed to the container.  Returned: when present |
| **cpu**  integer | The number of cpu units reserved for the container.  Returned: always |
| **disableNetworking**  boolean | When this parameter is true, networking is disabled within the container.  Returned: when present |
| **dnsSearchDomains**  string | A list of DNS search domains that are presented to the container.  Returned: when present |
| **dnsServers**  string | A list of DNS servers that are presented to the container.  Returned: when present |
| **dockerLabels**  string | A key/value map of labels to add to the container.  Returned: when present |
| **dockerSecurityOptions**  string | A list of strings to provide custom labels for SELinux and AppArmor multi-level security systems.  Returned: when present |
| **entryPoint**  string | The entry point that is passed to the container.  Returned: when present |
| **environment**  complex | The environment variables to pass to a container.  Returned: always |
| **name**  string | The name of the environment variable.  Returned: when present |
| **value**  string | The value of the environment variable.  Returned: when present |
| **essential**  boolean | Whether this is an essential container or not.  Returned: always |
| **extraHosts**  complex | A list of hostnames and IP address mappings to append to the /etc/hosts file on the container.  Returned: when present |
| **hostname**  string | The hostname to use in the /etc/hosts entry.  Returned: when present |
| **ipAddress**  string | The IP address to use in the /etc/hosts entry.  Returned: when present |
| **hostname**  string | The hostname to use for your container.  Returned: when present |
| **image**  string | The image used to start a container.  Returned: always |
| **links**  string | Links to other containers.  Returned: when present |
| **logConfiguration**  string | The log configuration specification for the container.  Returned: when present |
| **memoryReservation**  integer | The soft limit (in MiB) of memory to reserve for the container.  Returned: when present |
| **mountPoints**  complex | The mount points for data volumes in your container.  Returned: always |
| **containerPath**  string | The path on the container to mount the host volume at.  Returned: when present |
| **readOnly**  boolean | If this value is true , the container has read-only access to the volume. If this value is false , then the container can write to the volume.  Returned: when present |
| **sourceVolume**  string | The name of the volume to mount.  Returned: when present |
| **name**  string | The name of a container.  Returned: always |
| **options**  string | The configuration options to send to the log driver.  Returned: when present |
| **portMappings**  complex | The list of port mappings for the container.  Returned: always |
| **containerPort**  integer | The port number on the container.  Returned: when present |
| **hostPort**  integer | The port number on the container instance to reserve for your container.  Returned: when present |
| **protocol**  string | The protocol used for the port mapping.  Returned: when present |
| **privileged**  boolean | When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user).  Returned: when present |
| **readonlyRootFilesystem**  boolean | When this parameter is true, the container is given read-only access to its root file system.  Returned: when present |
| **ulimits**  complex | A list of ulimits to set in the container.  Returned: when present |
| **hardLimit**  integer | The hard limit for the ulimit type.  Returned: when present |
| **name**  string | The type of the ulimit .  Returned: when present |
| **softLimit**  integer | The soft limit for the ulimit type.  Returned: when present |
| **user**  string | The user name to use inside the container.  Returned: when present |
| **volumesFrom**  complex | Data volumes to mount from another container.  Returned: always |
| **readOnly**  boolean | If this value is true , the container has read-only access to the volume. If this value is false , then the container can write to the volume.  Returned: when present |
| **sourceContainer**  string | The name of another container within the same task definition to mount volumes from.  Returned: when present |
| **workingDirectory**  string | The working directory in which to run commands inside the container.  Returned: when present |
| **family**  string | The family of your task definition, used as the definition name  Returned: always |
| **network_mode**  string | Network mode for the containers  Returned: always |
| **placement_constraints**  complex | A list of placement constraint objects to use for tasks  Returned: always |
| **expression**  string | A cluster query language expression to apply to the constraint.  Returned: when present |
| **type**  string | The type of constraint.  Returned: when present |
| **requires_attributes**  complex | The container instance attributes required by your task  Returned: when present |
| **name**  string | The name of the attribute.  Returned: when present |
| **targetId**  string | The ID of the target.  Returned: when present |
| **targetType**  string | The type of the target with which to attach the attribute.  Returned: when present |
| **value**  string | The value of the attribute.  Returned: when present |
| **revision**  integer | Revision number that was queried  Returned: always |
| **status**  string | The status of the task definition  Returned: always |
| **task_definition_arn**  string | ARN of the task definition  Returned: always |
| **task_role_arn**  string | The ARN of the IAM role that containers in this task can assume  Returned: when role is set |
| **volumes**  complex | The list of volumes in a task  Returned: always |
| **host**  boolean | The contents of the host parameter determine whether your data volume persists on the host container instance and where it is stored.  Returned: when present |
| **name**  string | The name of the volume.  Returned: when present |
| **source_path**  string | The path on the host container instance that is presented to the container.  Returned: when present |

### Authors

- Gustavo Maia (@gurumaia)
- Mark Chance (@Java1Guy)
- Darek Kaczynski (@kaczynskid)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
