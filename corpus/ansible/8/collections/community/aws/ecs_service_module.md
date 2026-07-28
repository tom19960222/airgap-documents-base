---
collection: ansible
version: "8"
title: "community.aws.ecs_service module – Create, terminate, start or stop a service in ECS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/ecs_service_module.html
fetched_at: 2026-07-28T01:40:57+00:00
---
# community.aws.ecs_service module – Create, terminate, start or stop a service in ECS

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
> see [Requirements](ecs_service_module.md#ansible-collections-community-aws-ecs-service-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ecs_service`.

New in community.aws 1.0.0

- [Synopsis](ecs_service_module.md#synopsis)
- [Requirements](ecs_service_module.md#requirements)
- [Parameters](ecs_service_module.md#parameters)
- [Notes](ecs_service_module.md#notes)
- [Examples](ecs_service_module.md#examples)
- [Returned Facts](ecs_service_module.md#returned-facts)
- [Return Values](ecs_service_module.md#return-values)

## [Synopsis](ecs_service_module.md#id1)

- Creates or terminates ECS services.

## [Requirements](ecs_service_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ecs_service_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **capacity_provider_strategy**  list / elements=dictionary  *added in community.aws 4.0.0* | The capacity provider strategy to use with your service. You can specify a maximum of 6 providers per strategy.  **Default:** `[]` |
| **base**  integer | How many tasks, at a minimum, should use the specified provider. |
| **capacity_provider**  string | Name of capacity provider. |
| **weight**  integer | The relative percentage of the total number of launched tasks that should use the specified provider. |
| **client_token**  string | Unique, case-sensitive identifier you provide to ensure the idempotency of the request. Up to 32 ASCII characters are allowed.  **Default:** `""` |
| **cluster**  string | The name of the cluster in which the service exists.  If not specified, the cluster name will be `default`.  **Default:** `"default"` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **delay**  integer | The time to wait before checking that the service is available.  **Default:** `10` |
| **deployment_configuration**  dictionary | Optional parameters that control the deployment_configuration.  Format is ‘{“maximum_percent”:<integer>, “minimum_healthy_percent”:<integer>}  **Default:** `{}` |
| **deployment_circuit_breaker**  dictionary | The deployment circuit breaker determines whether a service deployment will fail if the service can’t reach a steady state. |
| **enable**  boolean | If enabled, a service deployment will transition to a failed state and stop launching new tasks.  **Choices:**   - `false` - `true` |
| **rollback**  boolean | If enabled, ECS will roll back your service to the last completed deployment after a failure.  **Choices:**   - `false` - `true` |
| **maximum_percent**  integer | Upper limit on the number of tasks in a service that are allowed in the RUNNING or PENDING state during a deployment. |
| **minimum_healthy_percent**  integer | A lower limit on the number of tasks in a service that must remain in the RUNNING state during a deployment. |
| **deployment_controller**  dictionary  *added in community.aws 4.1.0* | The deployment controller to use for the service. If no deploymenet controller is specified, the ECS controller is used.  **Default:** `{}` |
| **type**  string | The deployment controller type to use.  **Choices:**   - `"ECS"` - `"CODE_DEPLOY"` - `"EXTERNAL"` |
| **desired_count**  integer | The count of how many instances of the service.  This parameter is required when *state=present*. |
| **enable_execute_command**  boolean  *added in community.aws 5.4.0* | Whether or not to enable the execute command functionality for the containers in the ECS task.  If *enable_execute_command=true* execute command functionality is enabled on all containers in the ECS task.  **Choices:**   - `false` - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **force_deletion**  boolean  *added in community.aws 2.1.0* | Forcibly delete the service. Required when deleting a service with >0 scale, or no target group.  **Choices:**   - `false` ← (default) - `true` |
| **force_new_deployment**  boolean | Force deployment of service even if there are no changes.  **Choices:**   - `false` ← (default) - `true` |
| **health_check_grace_period_seconds**  integer | Seconds to wait before health checking the freshly added/updated services. |
| **launch_type**  string | The launch type on which to run your service.  **Choices:**   - `"EC2"` - `"FARGATE"` |
| **load_balancers**  list / elements=dictionary | The list of ELBs defined for this service.  Load balancers for an existing service cannot be updated, and it is an error to do so.  When the deployment controller is CODE_DEPLOY changes to this value are simply ignored, and do not cause an error.  **Default:** `[]` |
| **name**  aliases: service  string / required | The name of the service. |
| **network_configuration**  dictionary | Network configuration of the service. Only applicable for task definitions created with *network_mode=awsvpc*. |
| **assign_public_ip**  boolean | Whether the task’s elastic network interface receives a public IP address.  **Choices:**   - `false` - `true` |
| **security_groups**  list / elements=string | A list of security group names or group IDs to associate with the task. |
| **subnets**  list / elements=string | A list of subnet IDs to associate with the task. |
| **placement_constraints**  list / elements=dictionary | The placement constraints for the tasks in the service.  See <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PlacementConstraint.html> for more details.  **Default:** `[]` |
| **expression**  string | A cluster query language expression to apply to the constraint. |
| **type**  string | The type of constraint. |
| **placement_strategy**  list / elements=dictionary | The placement strategy objects to use for tasks in your service. You can specify a maximum of 5 strategy rules per service.  **Default:** `[]` |
| **field**  string | The field to apply the placement strategy against. |
| **type**  string | The type of placement strategy. |
| **platform_version**  string  *added in community.aws 1.5.0* | Numeric part of platform version or LATEST  See <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html> for more details. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **propagate_tags**  string  *added in community.aws 4.1.0* | Propagate tags from ECS task defintition or ECS service to ECS task.  **Choices:**   - `"TASK_DEFINITION"` - `"SERVICE"` |
| **purge_placement_constraints**  boolean  *added in community.aws 5.3.0* | Toggle overwriting of existing placement constraints. This is needed for backwards compatibility.  By default *purge_placement_constraints=false*. In a release after 2024-06-01 this will be changed to *purge_placement_constraints=true*.  **Choices:**   - `false` ← (default) - `true` |
| **purge_placement_strategy**  boolean  *added in community.aws 5.3.0* | Toggle overwriting of existing placement strategy. This is needed for backwards compatibility.  By default *purge_placement_strategy=false*. In a release after 2024-06-01 this will be changed to *purge_placement_strategy=true*.  **Choices:**   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **repeat**  integer | The number of times to check that the service is available.  **Default:** `10` |
| **role**  string | The name or full Amazon Resource Name (ARN) of the IAM role that allows your Amazon ECS container agent to make calls to your load balancer on your behalf.  This parameter is only required if you are using a load balancer with your service in a network mode other than `awsvpc`.  **Default:** `""` |
| **scheduling_strategy**  string | The scheduling strategy.  Defaults to `REPLICA` if not given to preserve previous behavior.  **Choices:**   - `"DAEMON"` - `"REPLICA"` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **service_registries**  list / elements=dictionary | Describes service discovery registries this service will register with.  **Default:** `[]` |
| **arn**  string | Service discovery registry ARN. |
| **container_name**  string | Container name for service discovery registration. |
| **container_port**  integer | Container port for service discovery registration. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string / required | The desired state of the service.  **Choices:**   - `"present"` - `"absent"` - `"deleting"` |
| **tags**  dictionary  *added in community.aws 4.1.0* | A dictionary of tags to add or remove from the resource. |
| **task_definition**  string | The task definition the service will run.  This parameter is required when *state=present* unless *force_new_deployment=True*.  This parameter is ignored when updating a service with a `CODE_DEPLOY` deployment controller in which case the task definition is managed by Code Pipeline and cannot be updated. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean  *added in community.aws 4.1.0* | Whether or not to wait for the service to be inactive.  Waits only when *state* is `absent`.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ecs_service_module.md#id4)

> **Note:**
>
> - The service role specified must be assumable. (i.e. have a trust relationship for the ecs service, ecs.amazonaws.com)
> - For details of the parameters and returns see <https://boto3.readthedocs.io/en/latest/reference/services/ecs.html>.
> - An IAM role must have been previously created.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ecs_service_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.
# Basic provisioning example
- community.aws.ecs_service:
    state: present
    name: console-test-service
    cluster: new_cluster
    task_definition: 'new_cluster-task:1'
    desired_count: 0

- name: create ECS service on VPC network
  community.aws.ecs_service:
    state: present
    name: console-test-service
    cluster: new_cluster
    task_definition: 'new_cluster-task:1'
    desired_count: 0
    network_configuration:
      subnets:
      - subnet-abcd1234
      security_groups:
      - sg-aaaa1111
      - my_security_group

# Simple example to delete
- community.aws.ecs_service:
    name: default
    state: absent
    cluster: new_cluster

# With custom deployment configuration (added in version 2.3), placement constraints and strategy (added in version 2.4)
- community.aws.ecs_service:
    state: present
    name: test-service
    cluster: test-cluster
    task_definition: test-task-definition
    desired_count: 3
    deployment_configuration:
      minimum_healthy_percent: 75
      maximum_percent: 150
    placement_constraints:
      - type: memberOf
        expression: 'attribute:flavor==test'
    placement_strategy:
      - type: binpack
        field: memory

# With deployment circuit breaker (added in version 4.0)
- community.aws.ecs_service:
    state: present
    name: test-service
    cluster: test-cluster
    task_definition: test-task-definition
    desired_count: 3
    deployment_configuration:
      deployment_circuit_breaker:
        enable: True
        rollback: True

# With capacity_provider_strategy (added in version 4.0)
- community.aws.ecs_service:
    state: present
    name: test-service
    cluster: test-cluster
    task_definition: test-task-definition
    desired_count: 1
    capacity_provider_strategy:
      - capacity_provider: test-capacity-provider-1
        weight: 1
        base: 0

# With tags and tag propagation
- community.aws.ecs_service:
    state: present
    name: tags-test-service
    cluster: new_cluster
    task_definition: 'new_cluster-task:1'
    desired_count: 1
    tags:
      Firstname: jane
      lastName: doe
    propagate_tags: SERVICE
```

## [Returned Facts](ecs_service_module.md#id6)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **service**  complex | Details of deleted service.  **Returned:** when service existed and was deleted |
| **clusterArn**  string | The Amazon Resource Name (ARN) of the of the cluster that hosts the service.  **Returned:** always |
| **deploymentConfiguration**  complex | dictionary of deploymentConfiguration  **Returned:** always |
| **deploymentCircuitBreaker**  complex | dictionary of deploymentCircuitBreaker  **Returned:** always |
| **enable**  boolean | The state of the circuit breaker feature.  **Returned:** always |
| **rollback**  boolean | The state of the rollback feature of the circuit breaker.  **Returned:** always |
| **maximumPercent**  integer | maximumPercent param  **Returned:** always |
| **minimumHealthyPercent**  integer | minimumHealthyPercent param  **Returned:** always |
| **deployments**  list / elements=dictionary | list of service deployments  **Returned:** always |
| **desiredCount**  integer | The desired number of instantiations of the task definition to keep running on the service.  **Returned:** always |
| **events**  list / elements=dictionary | list of service events  **Returned:** always |
| **loadBalancers**  complex | A list of load balancer objects  **Returned:** always |
| **containerName**  string | The name of the container to associate with the load balancer.  **Returned:** always |
| **containerPort**  integer | The port on the container to associate with the load balancer.  **Returned:** always |
| **loadBalancerName**  string | the name  **Returned:** always |
| **pendingCount**  integer | The number of tasks in the cluster that are in the PENDING state.  **Returned:** always |
| **placementConstraints**  list / elements=dictionary | List of placement constraints objects  **Returned:** always |
| **expression**  string | A cluster query language expression to apply to the constraint. Note you cannot specify an expression if the constraint type is distinctInstance.  **Returned:** always |
| **type**  string | The type of constraint. Valid values are distinctInstance and memberOf.  **Returned:** always |
| **placementStrategy**  list / elements=dictionary | List of placement strategy objects  **Returned:** always |
| **field**  string | The field to apply the placement strategy against. For the spread placement strategy, valid values are instanceId (or host, which has the same effect), or any platform or custom attribute that is applied to a container instance, such as attribute:ecs.availability-zone. For the binpack placement strategy, valid values are CPU and MEMORY.  **Returned:** always |
| **type**  string | The type of placement strategy. Valid values are random, spread and binpack.  **Returned:** always |
| **propagateTags**  string | The type of tag propagation applied to the resource  **Returned:** always |
| **runningCount**  integer | The number of tasks in the cluster that are in the RUNNING state.  **Returned:** always |
| **serviceArn**  string | The Amazon Resource Name (ARN) that identifies the service. The ARN contains the arn:aws:ecs namespace, followed by the region of the service, the AWS account ID of the service owner, the service namespace, and then the service name.  **Returned:** always  **Sample:** `"arn:aws:ecs:us-east-1:123456789012:service/my-service"` |
| **serviceName**  string | A user-generated string used to identify the service  **Returned:** always |
| **status**  string | The valid values are ACTIVE, DRAINING, or INACTIVE.  **Returned:** always |
| **tags**  list / elements=dictionary | The tags applied to this resource.  **Returned:** when tags found |
| **taskDefinition**  string | The ARN of a task definition to use for tasks in the service.  **Returned:** always |

## [Return Values](ecs_service_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **service**  complex | Details of created service.  **Returned:** when creating a service |
| **capacityProviderStrategy**  complex  *added in community.aws 4.0.0* | The capacity provider strategy to use with your service.  **Returned:** always |
| **base**  integer | How many tasks, at a minimum, should use the specified provider.  **Returned:** always |
| **capacityProvider**  string | Name of capacity provider.  **Returned:** always |
| **weight**  integer | The relative percentage of the total number of launched tasks that should use the specified provider.  **Returned:** always |
| **clusterArn**  string | The Amazon Resource Name (ARN) of the of the cluster that hosts the service.  **Returned:** always |
| **deploymentConfiguration**  complex | dictionary of deploymentConfiguration  **Returned:** always |
| **deploymentCircuitBreaker**  complex | dictionary of deploymentCircuitBreaker  **Returned:** always |
| **enable**  boolean | The state of the circuit breaker feature.  **Returned:** always |
| **rollback**  boolean | The state of the rollback feature of the circuit breaker.  **Returned:** always |
| **maximumPercent**  integer | maximumPercent param  **Returned:** always |
| **minimumHealthyPercent**  integer | minimumHealthyPercent param  **Returned:** always |
| **deployments**  list / elements=dictionary | list of service deployments  **Returned:** always |
| **desiredCount**  integer | The desired number of instantiations of the task definition to keep running on the service.  **Returned:** always |
| **events**  list / elements=dictionary | list of service events  **Returned:** always |
| **loadBalancers**  complex | A list of load balancer objects  Updating the loadbalancer configuration of an existing service requires botocore>=1.24.14.  **Returned:** always |
| **containerName**  string | The name of the container to associate with the load balancer.  **Returned:** always |
| **containerPort**  integer | The port on the container to associate with the load balancer.  **Returned:** always |
| **loadBalancerName**  string | the name  **Returned:** always |
| **pendingCount**  integer | The number of tasks in the cluster that are in the PENDING state.  **Returned:** always |
| **placementConstraints**  list / elements=dictionary | List of placement constraints objects  **Returned:** always |
| **expression**  string | A cluster query language expression to apply to the constraint. Note you cannot specify an expression if the constraint type is distinctInstance.  **Returned:** always |
| **type**  string | The type of constraint. Valid values are distinctInstance and memberOf.  **Returned:** always |
| **placementStrategy**  list / elements=dictionary | List of placement strategy objects  **Returned:** always |
| **field**  string | The field to apply the placement strategy against. For the spread placement strategy, valid values are instanceId (or host, which has the same effect), or any platform or custom attribute that is applied to a container instance, such as attribute:ecs.availability-zone. For the binpack placement strategy, valid values are CPU and MEMORY.  **Returned:** always |
| **type**  string | The type of placement strategy. Valid values are random, spread and binpack.  **Returned:** always |
| **propagateTags**  string | The type of tag propagation applied to the resource.  **Returned:** always |
| **runningCount**  integer | The number of tasks in the cluster that are in the RUNNING state.  **Returned:** always |
| **serviceArn**  string | The Amazon Resource Name (ARN) that identifies the service. The ARN contains the `arn:aws:ecs` namespace, followed by the region of the service, the AWS account ID of the service owner, the service namespace, and then the service name.  **Returned:** always  **Sample:** `"arn:aws:ecs:us-east-1:123456789012:service/my-service"` |
| **serviceName**  string | A user-generated string used to identify the service  **Returned:** always |
| **status**  string | The valid values are ACTIVE, DRAINING, or INACTIVE.  **Returned:** always |
| **tags**  dictionary | The tags applied to this resource.  **Returned:** success |
| **taskDefinition**  string | The ARN of a task definition to use for tasks in the service.  **Returned:** always |

### Authors

- Mark Chance (@Java1Guy)
- Darek Kaczynski (@kaczynskid)
- Stephane Maarek (@simplesteph)
- Zac Blazic (@zacblazic)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
