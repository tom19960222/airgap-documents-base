---
collection: ansible
version: "8"
title: "community.aws.ecs_taskdefinition_info module – Describe a task definition in ECS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/ecs_taskdefinition_info_module.html
fetched_at: 2026-07-28T01:41:01+00:00
---
# community.aws.ecs_taskdefinition_info module – Describe a task definition in ECS

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
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ecs_taskdefinition_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **task_definition**  string / required | The name of the task definition to get details for |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ecs_taskdefinition_info_module.md#id4)

> **Note:**
>
> - For details of the parameters and returns see <http://boto3.readthedocs.io/en/latest/reference/services/ecs.html#ECS.Client.describe_task_definition>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

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
| **container_definitions**  complex | Returns a list of complex objects representing the containers  **Returned:** success |
| **command**  string | The command that is passed to the container.  **Returned:** when present |
| **cpu**  integer | The number of cpu units reserved for the container.  **Returned:** always |
| **disableNetworking**  boolean | When this parameter is true, networking is disabled within the container.  **Returned:** when present |
| **dnsSearchDomains**  string | A list of DNS search domains that are presented to the container.  **Returned:** when present |
| **dnsServers**  string | A list of DNS servers that are presented to the container.  **Returned:** when present |
| **dockerLabels**  string | A key/value map of labels to add to the container.  **Returned:** when present |
| **dockerSecurityOptions**  string | A list of strings to provide custom labels for SELinux and AppArmor multi-level security systems.  **Returned:** when present |
| **entryPoint**  string | The entry point that is passed to the container.  **Returned:** when present |
| **environment**  complex | The environment variables to pass to a container.  **Returned:** always |
| **name**  string | The name of the environment variable.  **Returned:** when present |
| **value**  string | The value of the environment variable.  **Returned:** when present |
| **essential**  boolean | Whether this is an essential container or not.  **Returned:** always |
| **extraHosts**  complex | A list of hostnames and IP address mappings to append to the /etc/hosts file on the container.  **Returned:** when present |
| **hostname**  string | The hostname to use in the /etc/hosts entry.  **Returned:** when present |
| **ipAddress**  string | The IP address to use in the /etc/hosts entry.  **Returned:** when present |
| **firelensConfiguration**  dictionary | The FireLens configuration for the container.  **Returned:** when present |
| **options**  dictionary | The options to use when configuring the log router.  **Returned:** success |
| **type**  string | The log router.  **Returned:** success |
| **healthCheck**  dictionary | The container health check command and associated configuration parameters for the container.  **Returned:** when present |
| **command**  list / elements=string | A string array representing the command that the container runs to determine if it is healthy.  **Returned:** success |
| **interval**  integer | The time period in seconds between each health check execution.  **Returned:** success |
| **retries**  integer | The number of times to retry a failed health check before the container is considered unhealthy.  **Returned:** success |
| **startPeriod**  integer | The optional grace period to provide containers time to bootstrap before failed.  **Returned:** success |
| **timeout**  integer | The time period in seconds to wait for a health check to succeed before it is considered a failure.  **Returned:** success |
| **hostname**  string | The hostname to use for your container.  **Returned:** when present |
| **image**  string | The image used to start a container.  **Returned:** always |
| **links**  string | Links to other containers.  **Returned:** when present |
| **logConfiguration**  string | The log configuration specification for the container.  **Returned:** when present |
| **memoryReservation**  integer | The soft limit (in MiB) of memory to reserve for the container.  **Returned:** when present |
| **mountPoints**  complex | The mount points for data volumes in your container.  **Returned:** always |
| **containerPath**  string | The path on the container to mount the host volume at.  **Returned:** when present |
| **readOnly**  boolean | If this value is true , the container has read-only access to the volume. If this value is false , then the container can write to the volume.  **Returned:** when present |
| **sourceVolume**  string | The name of the volume to mount.  **Returned:** when present |
| **name**  string | The name of a container.  **Returned:** always |
| **options**  string | The configuration options to send to the log driver.  **Returned:** when present |
| **portMappings**  complex | The list of port mappings for the container.  **Returned:** always |
| **containerPort**  integer | The port number on the container.  **Returned:** when present |
| **hostPort**  integer | The port number on the container instance to reserve for your container.  **Returned:** when present |
| **protocol**  string | The protocol used for the port mapping.  **Returned:** when present |
| **privileged**  boolean | When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user).  **Returned:** when present |
| **readonlyRootFilesystem**  boolean | When this parameter is true, the container is given read-only access to its root file system.  **Returned:** when present |
| **resourceRequirements**  dictionary | The type and amount of a resource to assign to a container.  **Returned:** when present |
| **type**  string | The type of resource to assign to a container.  **Returned:** success |
| **value**  string | The value for the specified resource type.  **Returned:** success |
| **systemControls**  dictionary | A list of namespaced kernel parameters to set in the container.  **Returned:** when present |
| **namespace**  string | TThe namespaced kernel.  **Returned:** success |
| **value**  string | The value for the namespaced kernel.  **Returned:** success |
| **ulimits**  complex | A list of ulimits to set in the container.  **Returned:** when present |
| **hardLimit**  integer | The hard limit for the ulimit type.  **Returned:** when present |
| **name**  string | The type of the ulimit .  **Returned:** when present |
| **softLimit**  integer | The soft limit for the ulimit type.  **Returned:** when present |
| **user**  string | The user name to use inside the container.  **Returned:** when present |
| **volumesFrom**  complex | Data volumes to mount from another container.  **Returned:** always |
| **readOnly**  boolean | If this value is true , the container has read-only access to the volume. If this value is false , then the container can write to the volume.  **Returned:** when present |
| **sourceContainer**  string | The name of another container within the same task definition to mount volumes from.  **Returned:** when present |
| **workingDirectory**  string | The working directory in which to run commands inside the container.  **Returned:** when present |
| **family**  string | The family of your task definition, used as the definition name  **Returned:** always |
| **network_mode**  string | Network mode for the containers  **Returned:** always |
| **placement_constraints**  complex | A list of placement constraint objects to use for tasks  **Returned:** always |
| **expression**  string | A cluster query language expression to apply to the constraint.  **Returned:** when present |
| **type**  string | The type of constraint.  **Returned:** when present |
| **requires_attributes**  complex | The container instance attributes required by your task  **Returned:** when present |
| **name**  string | The name of the attribute.  **Returned:** when present |
| **targetId**  string | The ID of the target.  **Returned:** when present |
| **targetType**  string | The type of the target with which to attach the attribute.  **Returned:** when present |
| **value**  string | The value of the attribute.  **Returned:** when present |
| **revision**  integer | Revision number that was queried  **Returned:** always |
| **status**  string | The status of the task definition  **Returned:** always |
| **task_definition_arn**  string | ARN of the task definition  **Returned:** always |
| **task_role_arn**  string | The ARN of the IAM role that containers in this task can assume  **Returned:** when role is set |
| **volumes**  complex | The list of volumes in a task  **Returned:** always |
| **host**  boolean | The contents of the host parameter determine whether your data volume persists on the host container instance and where it is stored.  **Returned:** when present |
| **name**  string | The name of the volume.  **Returned:** when present |
| **source_path**  string | The path on the host container instance that is presented to the container.  **Returned:** when present |

### Authors

- Gustavo Maia (@gurumaia)
- Mark Chance (@Java1Guy)
- Darek Kaczynski (@kaczynskid)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
