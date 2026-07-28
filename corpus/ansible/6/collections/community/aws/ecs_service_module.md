---
collection: ansible
version: "6"
title: "community.aws.ecs_service module – Create, terminate, start or stop a service in ECS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ecs_service_module.html
fetched_at: 2026-07-27T17:04:18+00:00
---
# community.aws.ecs_service module – Create, terminate, start or stop a service in ECS

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

- Creates or terminates ECS. services.

## [Requirements](ecs_service_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ecs_service_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **client_token**  string | Unique, case-sensitive identifier you provide to ensure the idempotency of the request. Up to 32 ASCII characters are allowed. |
| **cluster**  string | The name of the cluster in which the service exists.  If not specified, the cluster name will be `default`.  Default: `"default"` |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **delay**  integer | The time to wait before checking that the service is available.  Default: `10` |
| **deployment_configuration**  dictionary | Optional parameters that control the deployment_configuration.  Format is ‘{“maximum_percent”:<integer>, “minimum_healthy_percent”:<integer>} |
| **deployment_circuit_breaker**  dictionary | The deployment circuit breaker determines whether a service deployment will fail if the service can’t reach a steady state. |
| **enable**  boolean | If enabled, a service deployment will transition to a failed state and stop launching new tasks.  Choices:   - `false` - `true` |
| **rollback**  boolean | If enabled, ECS will roll back your service to the last completed deployment after a failure.  Choices:   - `false` - `true` |
| **maximum_percent**  integer | Upper limit on the number of tasks in a service that are allowed in the RUNNING or PENDING state during a deployment. |
| **minimum_healthy_percent**  integer | A lower limit on the number of tasks in a service that must remain in the RUNNING state during a deployment. |
| **desired_count**  integer | The count of how many instances of the service.  This parameter is required when *state=present*. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **force_deletion**  boolean  added in community.aws 2.1.0 | Forcibly delete the service. Required when deleting a service with >0 scale, or no target group.  Choices:   - `false` ← (default) - `true` |
| **force_new_deployment**  boolean | Force deployment of service even if there are no changes.  Choices:   - `false` ← (default) - `true` |
| **health_check_grace_period_seconds**  integer | Seconds to wait before health checking the freshly added/updated services. |
| **launch_type**  string | The launch type on which to run your service.  Choices:   - `"EC2"` - `"FARGATE"` |
| **load_balancers**  list / elements=dictionary | The list of ELBs defined for this service. |
| **name**  aliases: service  string / required | The name of the service. |
| **network_configuration**  dictionary | Network configuration of the service. Only applicable for task definitions created with *network_mode=awsvpc*. |
| **assign_public_ip**  boolean | Whether the task’s elastic network interface receives a public IP address.  Choices:   - `false` - `true` |
| **security_groups**  list / elements=string | A list of security group names or group IDs to associate with the task. |
| **subnets**  list / elements=string | A list of subnet IDs to associate with the task. |
| **placement_constraints**  list / elements=dictionary | The placement constraints for the tasks in the service.  See <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PlacementConstraint.html> for more details. |
| **expression**  string | A cluster query language expression to apply to the constraint. |
| **type**  string | The type of constraint. |
| **placement_strategy**  list / elements=dictionary | The placement strategy objects to use for tasks in your service. You can specify a maximum of 5 strategy rules per service. |
| **field**  string | The field to apply the placement strategy against. |
| **type**  string | The type of placement strategy. |
| **platform_version**  string  added in community.aws 1.5.0 | Numeric part of platform version or LATEST  See <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html> for more details. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **repeat**  integer | The number of times to check that the service is available.  Default: `10` |
| **role**  string | The name or full Amazon Resource Name (ARN) of the IAM role that allows your Amazon ECS container agent to make calls to your load balancer on your behalf.  This parameter is only required if you are using a load balancer with your service in a network mode other than `awsvpc`. |
| **scheduling_strategy**  string | The scheduling strategy.  Defaults to `REPLICA` if not given to preserve previous behavior.  Choices:   - `"DAEMON"` - `"REPLICA"` |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **service_registries**  list / elements=dictionary | Describes service discovery registries this service will register with. |
| **arn**  string | Service discovery registry ARN. |
| **container_name**  string | Container name for service discovery registration. |
| **container_port**  integer | Container port for service discovery registration. |
| **state**  string / required | The desired state of the service.  Choices:   - `"present"` - `"absent"` - `"deleting"` |
| **task_definition**  string | The task definition the service will run.  This parameter is required when *state=present*. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ecs_service_module.md#id4)

> **Note:**
>
> - The service role specified must be assumable. (i.e. have a trust relationship for the ecs service, ecs.amazonaws.com)
> - For details of the parameters and returns see <https://boto3.readthedocs.io/en/latest/reference/services/ecs.html>.
> - An IAM role must have been previously created.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

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
```

## [Returned Facts](ecs_service_module.md#id6)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **service**  complex | Details of deleted service.  Returned: when service existed and was deleted |
| **clusterArn**  string | The Amazon Resource Name (ARN) of the of the cluster that hosts the service.  Returned: always |
| **deploymentConfiguration**  complex | dictionary of deploymentConfiguration  Returned: always |
| **deploymentCircuitBreaker**  complex | dictionary of deploymentCircuitBreaker  Returned: always |
| **enable**  boolean | The state of the circuit breaker feature.  Returned: always |
| **rollback**  boolean | The state of the rollback feature of the circuit breaker.  Returned: always |
| **maximumPercent**  integer | maximumPercent param  Returned: always |
| **minimumHealthyPercent**  integer | minimumHealthyPercent param  Returned: always |
| **deployments**  list / elements=dictionary | list of service deployments  Returned: always |
| **desiredCount**  integer | The desired number of instantiations of the task definition to keep running on the service.  Returned: always |
| **events**  list / elements=dictionary | list of service events  Returned: always |
| **loadBalancers**  complex | A list of load balancer objects  Returned: always |
| **containerName**  string | The name of the container to associate with the load balancer.  Returned: always |
| **containerPort**  integer | The port on the container to associate with the load balancer.  Returned: always |
| **loadBalancerName**  string | the name  Returned: always |
| **pendingCount**  integer | The number of tasks in the cluster that are in the PENDING state.  Returned: always |
| **placementConstraints**  list / elements=dictionary | List of placement constraints objects  Returned: always |
| **expression**  string | A cluster query language expression to apply to the constraint. Note you cannot specify an expression if the constraint type is distinctInstance.  Returned: always |
| **type**  string | The type of constraint. Valid values are distinctInstance and memberOf.  Returned: always |
| **placementStrategy**  list / elements=dictionary | List of placement strategy objects  Returned: always |
| **field**  string | The field to apply the placement strategy against. For the spread placement strategy, valid values are instanceId (or host, which has the same effect), or any platform or custom attribute that is applied to a container instance, such as attribute:ecs.availability-zone. For the binpack placement strategy, valid values are CPU and MEMORY.  Returned: always |
| **type**  string | The type of placement strategy. Valid values are random, spread and binpack.  Returned: always |
| **runningCount**  integer | The number of tasks in the cluster that are in the RUNNING state.  Returned: always |
| **serviceArn**  string | The Amazon Resource Name (ARN) that identifies the service. The ARN contains the arn:aws:ecs namespace, followed by the region of the service, the AWS account ID of the service owner, the service namespace, and then the service name. For example, arn:aws:ecs:region :012345678910 :service/my-service .  Returned: always |
| **serviceName**  string | A user-generated string used to identify the service  Returned: always |
| **status**  string | The valid values are ACTIVE, DRAINING, or INACTIVE.  Returned: always |
| **taskDefinition**  string | The ARN of a task definition to use for tasks in the service.  Returned: always |

## [Return Values](ecs_service_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **service**  complex | Details of created service.  Returned: when creating a service |
| **clusterArn**  string | The Amazon Resource Name (ARN) of the of the cluster that hosts the service.  Returned: always |
| **deploymentConfiguration**  complex | dictionary of deploymentConfiguration  Returned: always |
| **deploymentCircuitBreaker**  complex | dictionary of deploymentCircuitBreaker  Returned: always |
| **enable**  boolean | The state of the circuit breaker feature.  Returned: always |
| **rollback**  boolean | The state of the rollback feature of the circuit breaker.  Returned: always |
| **maximumPercent**  integer | maximumPercent param  Returned: always |
| **minimumHealthyPercent**  integer | minimumHealthyPercent param  Returned: always |
| **deployments**  list / elements=dictionary | list of service deployments  Returned: always |
| **desiredCount**  integer | The desired number of instantiations of the task definition to keep running on the service.  Returned: always |
| **events**  list / elements=dictionary | list of service events  Returned: always |
| **loadBalancers**  complex | A list of load balancer objects  Returned: always |
| **containerName**  string | The name of the container to associate with the load balancer.  Returned: always |
| **containerPort**  integer | The port on the container to associate with the load balancer.  Returned: always |
| **loadBalancerName**  string | the name  Returned: always |
| **pendingCount**  integer | The number of tasks in the cluster that are in the PENDING state.  Returned: always |
| **placementConstraints**  list / elements=dictionary | List of placement constraints objects  Returned: always |
| **expression**  string | A cluster query language expression to apply to the constraint. Note you cannot specify an expression if the constraint type is distinctInstance.  Returned: always |
| **type**  string | The type of constraint. Valid values are distinctInstance and memberOf.  Returned: always |
| **placementStrategy**  list / elements=dictionary | List of placement strategy objects  Returned: always |
| **field**  string | The field to apply the placement strategy against. For the spread placement strategy, valid values are instanceId (or host, which has the same effect), or any platform or custom attribute that is applied to a container instance, such as attribute:ecs.availability-zone. For the binpack placement strategy, valid values are CPU and MEMORY.  Returned: always |
| **type**  string | The type of placement strategy. Valid values are random, spread and binpack.  Returned: always |
| **runningCount**  integer | The number of tasks in the cluster that are in the RUNNING state.  Returned: always |
| **serviceArn**  string | The Amazon Resource Name (ARN) that identifies the service. The ARN contains the arn:aws:ecs namespace, followed by the region of the service, the AWS account ID of the service owner, the service namespace, and then the service name. For example, arn:aws:ecs:region :012345678910 :service/my-service .  Returned: always |
| **serviceName**  string | A user-generated string used to identify the service  Returned: always |
| **status**  string | The valid values are ACTIVE, DRAINING, or INACTIVE.  Returned: always |
| **taskDefinition**  string | The ARN of a task definition to use for tasks in the service.  Returned: always |

### Authors

- Mark Chance (@Java1Guy)
- Darek Kaczynski (@kaczynskid)
- Stephane Maarek (@simplesteph)
- Zac Blazic (@zacblazic)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
