---
collection: ansible
version: "8"
title: "community.aws.ecs_taskdefinition module – register a task definition in ecs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/ecs_taskdefinition_module.html
fetched_at: 2026-07-28T01:41:00+00:00
---
# community.aws.ecs_taskdefinition module – register a task definition in ecs

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
> see [Requirements](ecs_taskdefinition_module.md#ansible-collections-community-aws-ecs-taskdefinition-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ecs_taskdefinition`.

New in community.aws 1.0.0

- [Synopsis](ecs_taskdefinition_module.md#synopsis)
- [Requirements](ecs_taskdefinition_module.md#requirements)
- [Parameters](ecs_taskdefinition_module.md#parameters)
- [Notes](ecs_taskdefinition_module.md#notes)
- [Examples](ecs_taskdefinition_module.md#examples)
- [Return Values](ecs_taskdefinition_module.md#return-values)

## [Synopsis](ecs_taskdefinition_module.md#id1)

- Registers or deregisters task definitions in the Amazon Web Services (AWS) EC2 Container Service (ECS).

## [Requirements](ecs_taskdefinition_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ecs_taskdefinition_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **arn**  string | The ARN of the task description to delete. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **containers**  list / elements=dictionary / required | A list of containers definitions.  See <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html> for a complete list of parameters. |
| **command**  list / elements=string | The command that is passed to the container. If there are multiple arguments, each argument is a separated string in the array. |
| **cpu**  integer | The number of cpu units reserved for the container. |
| **dependsOn**  list / elements=dictionary | The dependencies defined for container startup and shutdown.  When a dependency is defined for container startup, for container shutdown it is reversed. |
| **condition**  string / required | The dependency condition of the container.  **Choices:**   - `"start"` - `"complete"` - `"success"` - `"healthy"` |
| **containerName**  string / required | The name of a container. |
| **disableNetworking**  boolean | When this parameter is `True`, networking is disabled within the container.  **Choices:**   - `false` - `true` |
| **dnsSearchDomains**  list / elements=string | A list of DNS search domains that are presented to the container.  This parameter is not supported for Windows containers. |
| **dnsServers**  list / elements=string | A list of DNS servers that are presented to the container.  This parameter is not supported for Windows containers. |
| **dockerLabels**  dictionary | A key/value map of labels to add to the container. |
| **dockerSecurityOptions**  list / elements=string | A list of strings to provide custom labels for SELinux and AppArmor multi-level security systems.  This parameter is not supported for Windows containers. |
| **entryPoint**  string | The entry point that is passed to the container. |
| **environment**  list / elements=dictionary | The environment variables to pass to a container. |
| **name**  string | The name of the key-value pair. |
| **value**  string | The value of the key-value pair. |
| **environmentFiles**  list / elements=dictionary | A list of files containing the environment variables to pass to a container. |
| **type**  string | The file type to use. The only supported value is `s3`. |
| **value**  string | The Amazon Resource Name (ARN) of the Amazon S3 object containing the environment variable file. |
| **essential**  boolean | If *essential=True*, and the container fails or stops for any reason, all other containers that are part of the task are stopped.  **Choices:**   - `false` - `true` |
| **extraHosts**  list / elements=dictionary | A list of hostnames and IP address mappings to append to the /etc/hosts file on the container.  This parameter is not supported for Windows containers or tasks that use *network_mode=awsvpc*. |
| **hostname**  string | The hostname to use in the /etc/hosts entry. |
| **ipAddress**  string | The IP address to use in the /etc/hosts entry. |
| **firelensConfiguration**  dictionary | The FireLens configuration for the container.  This is used to specify and configure a log router for container logs. |
| **options**  dictionary | The options to use when configuring the log router.  This field is optional and can be used to specify a custom configuration file or to add additional metadata, such as the task, task definition, cluster, and container instance details to the log event.  If specified, the syntax to use is `{"enable-ecs-log-metadata":"true|false","config-file-type:"s3|file","config-file-value":"arn:aws:s3:::mybucket/fluent.conf|filepath"}`.  For more information, see <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html#firelens-taskdef>. |
| **type**  string | The log router to use. The valid values are `fluentd` or `fluentbit`.  **Choices:**   - `"fluentd"` - `"fluentbit"` |
| **healthCheck**  dictionary | The health check command and associated configuration parameters for the container. |
| **command**  list / elements=string | A string array representing the command that the container runs to determine if it is healthy.  The string array must start with CMD to run the command arguments directly, or CMD-SHELL to run the command with the container’s default shell.  An exit code of 0 indicates success, and non-zero exit code indicates failure. |
| **interval**  integer | The time period in seconds between each health check execution.  You may specify between 5 and 300 seconds. The default value is 30 seconds.  **Default:** `30` |
| **retries**  integer | The number of times to retry a failed health check before the container is considered unhealthy.  You may specify between 1 and 10 retries. The default value is 3.  **Default:** `3` |
| **startPeriod**  integer | The optional grace period to provide containers time to bootstrap before failed health checks count towards the maximum number of retries.  You can specify between 0 and 300 seconds. By default, the startPeriod is disabled.  Note: If a health check succeeds within the startPeriod, then the container is considered healthy and any subsequent failures count toward the maximum number of retries. |
| **timeout**  integer | The time period in seconds to wait for a health check to succeed before it is considered a failure.  You may specify between 2 and 60 seconds. The default value is 5.  **Default:** `5` |
| **hostname**  string | The hostname to use for your container.  This parameter is not supported if *network_mode=awsvpc*. |
| **image**  string | The image used to start a container. |
| **interactive**  boolean | When *interactive=True*, it allows to deploy containerized applications that require stdin or a tty to be allocated.  **Choices:**   - `false` - `true` |
| **links**  list / elements=string | Allows containers to communicate with each other without the need for port mappings.  This parameter is only supported if *network_mode=bridge*. |
| **linuxParameters**  dictionary | Linux-specific modifications that are applied to the container, such as Linux kernel capabilities. |
| **capabilities**  dictionary | The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker. |
| **add**  list / elements=string | The Linux capabilities for the container that have been added to the default configuration provided by Docker.  If *launch_type=FARGATE*, this parameter is not supported.  **Choices:**   - `"ALL"` - `"AUDIT_CONTROL"` - `"AUDIT_WRITE"` - `"BLOCK_SUSPEND"` - `"CHOWN"` - `"DAC_OVERRIDE"` - `"DAC_READ_SEARCH"` - `"FOWNER"` - `"FSETID"` - `"IPC_LOCK"` - `"IPC_OWNER"` - `"KILL"` - `"LEASE"` - `"LINUX_IMMUTABLE"` - `"MAC_ADMIN"` - `"MAC_OVERRIDE"` - `"MKNOD"` - `"NET_ADMIN"` - `"NET_BIND_SERVICE"` - `"NET_BROADCAST"` - `"NET_RAW"` - `"SETFCAP"` - `"SETGID"` - `"SETPCAP"` - `"SETUID"` - `"SYS_ADMIN"` - `"SYS_BOOT"` - `"SYS_CHROOT"` - `"SYS_MODULE"` - `"SYS_NICE"` - `"SYS_PACCT"` - `"SYS_PTRACE"` - `"SYS_RAWIO"` - `"SYS_RESOURCE"` - `"SYS_TIME"` - `"SYS_TTY_CONFIG"` - `"SYSLOG"` - `"WAKE_ALARM"` |
| **drop**  list / elements=string | The Linux capabilities for the container that have been removed from the default configuration provided by Docker.  **Choices:**   - `"ALL"` - `"AUDIT_CONTROL"` - `"AUDIT_WRITE"` - `"BLOCK_SUSPEND"` - `"CHOWN"` - `"DAC_OVERRIDE"` - `"DAC_READ_SEARCH"` - `"FOWNER"` - `"FSETID"` - `"IPC_LOCK"` - `"IPC_OWNER"` - `"KILL"` - `"LEASE"` - `"LINUX_IMMUTABLE"` - `"MAC_ADMIN"` - `"MAC_OVERRIDE"` - `"MKNOD"` - `"NET_ADMIN"` - `"NET_BIND_SERVICE"` - `"NET_BROADCAST"` - `"NET_RAW"` - `"SETFCAP"` - `"SETGID"` - `"SETPCAP"` - `"SETUID"` - `"SYS_ADMIN"` - `"SYS_BOOT"` - `"SYS_CHROOT"` - `"SYS_MODULE"` - `"SYS_NICE"` - `"SYS_PACCT"` - `"SYS_PTRACE"` - `"SYS_RAWIO"` - `"SYS_RESOURCE"` - `"SYS_TIME"` - `"SYS_TTY_CONFIG"` - `"SYSLOG"` - `"WAKE_ALARM"` |
| **devices**  list / elements=dictionary | Any host devices to expose to the container.  If *launch_type=FARGATE*, this parameter is not supported. |
| **containerPath**  string | The path inside the container at which to expose the host device. |
| **hostPath**  string / required | The path for the device on the host container instance. |
| **permissions**  list / elements=string | The explicit permissions to provide to the container for the device. |
| **initProcessEnabled**  boolean | Run an init process inside the container that forwards signals and reaps processes.  **Choices:**   - `false` - `true` |
| **maxSwap**  integer | The total amount of swap memory (in MiB) a container can use.  If *launch_type=FARGATE*, this parameter is not supported. |
| **sharedMemorySize**  integer | The value for the size (in MiB) of the /dev/shm volume.  If *launch_type=FARGATE*, this parameter is not supported. |
| **swappiness**  integer | This allows you to tune a container’s memory swappiness behavior.  If *launch_type=FARGATE*, this parameter is not supported. |
| **tmpfs**  list / elements=dictionary | The container path, mount options, and size (in MiB) of the tmpfs mount.  If *launch_type=FARGATE*, this parameter is not supported. |
| **containerPath**  string / required | The absolute file path where the tmpfs volume is to be mounted. |
| **mountOptions**  list / elements=string | The list of tmpfs volume mount options.  **Choices:**   - `"defaults"` - `"ro"` - `"rw"` - `"suid"` - `"nosuid"` - `"dev"` - `"nodev"` - `"exec"` - `"noexec"` - `"sync"` - `"async"` - `"dirsync"` - `"remount"` - `"mand"` - `"nomand"` - `"atime"` - `"noatime"` - `"diratime"` - `"nodiratime"` - `"bind"` - `"rbind"` - `"unbindable"` - `"runbindable"` - `"private"` - `"rprivate"` - `"shared"` - `"rshared"` - `"slave"` - `"rslave"` - `"relatime"` - `"norelatime"` - `"strictatime"` - `"nostrictatime"` - `"mode"` - `"uid"` - `"gid"` - `"nr_inodes"` - `"nr_blocks"` - `"mpol"` |
| **size**  integer / required | The size (in MiB) of the tmpfs volume. |
| **logConfiguration**  dictionary | The log configuration specification for the container. |
| **logDriver**  string | The log driver to use for the container.  For tasks on AWS Fargate, the supported log drivers are `awslogs`, `splunk`, and `awsfirelens`.  For tasks hosted on Amazon EC2 instances, the supported log drivers are `awslogs`, `fluentd`, `gelf`, `json-file`, `journald`, `logentries`, `syslog`, `splunk`, and `awsfirelens`. |
| **memory**  integer | The amount (in MiB) of memory to present to the container. |
| **memoryReservation**  integer | The soft limit (in MiB) of memory to reserve for the container. |
| **mountPoints**  list / elements=dictionary | The mount points for data volumes in your container. |
| **containerPath**  string | The path on the container to mount the host volume at. |
| **readOnly**  boolean | If this value is `True`, the container has read-only access to the volume.  If this value is `False`, then the container can write to the volume.  **Choices:**   - `false` ← (default) - `true` |
| **sourceVolume**  string | The name of the volume to mount. |
| **name**  string | The name of a container. |
| **options**  string | The configuration options to send to the log driver. |
| **portMappings**  list / elements=dictionary | The list of port mappings for the container. |
| **containerPort**  integer | The port number on the container that is bound to the user-specified or automatically assigned host port. |
| **hostPort**  integer | The port number on the container instance to reserve for your container. |
| **protocol**  string | The protocol used for the port mapping.  **Choices:**   - `"tcp"` ← (default) - `"udp"` |
| **privileged**  boolean | When this parameter is `True`, the container is given elevated privileges on the host container instance.  **Choices:**   - `false` - `true` |
| **pseudoTerminal**  boolean | When this parameter is `True`, a TTY is allocated.  **Choices:**   - `false` - `true` |
| **readonlyRootFilesystem**  boolean | When this parameter is `True`, the container is given read-only access to its root file system.  **Choices:**   - `false` - `true` |
| **repositoryCredentials**  dictionary | The private repository authentication credentials to use. |
| **credentialsParameter**  string / required | The Amazon Resource Name (ARN) of the secret containing the private repository credentials. |
| **resourceRequirements**  list / elements=dictionary | The type and amount of a resource to assign to a container.  The only supported resources are `GPU` and `InferenceAccelerator`. |
| **type**  string | The type of resource to assign to a container.  **Choices:**   - `"GPU"` - `"InferenceAccelerator"` |
| **value**  string | The value for the specified resource type. |
| **secretOptions**  list / elements=dictionary | The secrets to pass to the log configuration. |
| **name**  string | The name of the secret. |
| **valueFrom**  string | The secret to expose to the container. |
| **secrets**  list / elements=dictionary | The secrets to pass to the container. |
| **name**  string / required | The value to set as the environment variable on the container. |
| **size**  string / required | The secret to expose to the container. |
| **startTimeout**  integer | Time duration (in seconds) to wait before giving up on resolving dependencies for a container. |
| **stopTimeout**  integer | Time duration (in seconds) to wait before the container is forcefully killed if it doesn’t exit normally on its own. |
| **systemControls**  list / elements=dictionary | A list of namespaced kernel parameters to set in the container. |
| **namespace**  string | The namespaced kernel parameter to set a `value` for. |
| **value**  string | The value for the namespaced kernel parameter that’s specified in `namespace`. |
| **ulimits**  list / elements=dictionary | A list of ulimits to set in the container.  This parameter is not supported for Windows containers. |
| **hardLimit**  integer | The hard limit for the ulimit type. |
| **name**  string | The type of the ulimit.  **Choices:**   - `"core"` - `"cpu"` - `"data"` - `"fsize"` - `"locks"` - `"memlock"` - `"msgqueue"` - `"nice"` - `"nofile"` - `"nproc"` - `"rss"` - `"rtprio"` - `"rttime"` - `"sigpending"` - `"stack"` |
| **softLimit**  integer | The soft limit for the ulimit type. |
| **user**  string | The user to use inside the container.  This parameter is not supported for Windows containers. |
| **volumesFrom**  list / elements=dictionary | Data volumes to mount from another container. |
| **readOnly**  boolean | If this value is `True`, the container has read-only access to the volume.  If this value is `False`, then the container can write to the volume.  **Choices:**   - `false` ← (default) - `true` |
| **sourceContainer**  string | The name of another container within the same task definition from which to mount volumes. |
| **workingDirectory**  string | The working directory in which to run commands inside the container. |
| **cpu**  string | The number of cpu units used by the task. If *launch_type=EC2*, this field is optional and any value can be used.  If *launch_type=FARGATE*, this field is required and you must use one of `256`, `512`, `1024`, `2048`, `4096`. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **execution_role_arn**  string | The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.  **Default:** `""` |
| **family**  string | A Name that would be given to the task definition. |
| **force_create**  boolean | Always create new task definition.  **Choices:**   - `false` ← (default) - `true` |
| **launch_type**  string | The launch type on which to run your task.  **Choices:**   - `"EC2"` - `"FARGATE"` |
| **memory**  string | The amount (in MiB) of memory used by the task. If *launch_type=EC2*, this field is optional and any value can be used.  If *launch_type=FARGATE*, this field is required and is limited by the CPU. |
| **network_mode**  string | The Docker networking mode to use for the containers in the task.  Windows containers must use *network_mode=default*, which will utilize docker NAT networking.  Setting *network_mode=default* for a Linux container will use `bridge` mode.  **Choices:**   - `"default"` - `"bridge"` ← (default) - `"host"` - `"none"` - `"awsvpc"` |
| **placement_constraints**  list / elements=dictionary  *added in community.aws 2.1.0* | Placement constraint objects to use for the task.  You can specify a maximum of 10 constraints per task.  Task placement constraints are not supported for tasks run on Fargate. |
| **expression**  string | A cluster query language expression to apply to the constraint. |
| **type**  string | The type of constraint. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **revision**  integer | A revision number for the task definition. |
| **runtime_platform**  dictionary  *added in community.aws 6.4.0* | runtime platform configuration for the task  **Default:** `{"cpuArchitecture": "X86_64", "operatingSystemFamily": "LINUX"}` |
| **cpuArchitecture**  string | The CPU Architecture type to be used by the task  **Choices:**   - `"X86_64"` - `"ARM64"` |
| **operatingSystemFamily**  string | OS type to be used by the task  **Choices:**   - `"LINUX"` - `"WINDOWS_SERVER_2019_FULL"` - `"WINDOWS_SERVER_2019_CORE"` - `"WINDOWS_SERVER_2022_FULL"` - `"WINDOWS_SERVER_2022_CORE"` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string / required | State whether the task definition should exist or be deleted.  **Choices:**   - `"present"` - `"absent"` |
| **task_role_arn**  string | The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.  **Default:** `""` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **volumes**  list / elements=dictionary | A list of names of volumes to be attached. |
| **name**  string / required | The name of the volume. |

## [Notes](ecs_taskdefinition_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ecs_taskdefinition_module.md#id5)

```yaml+jinja
- name: Create task definition
  community.aws.ecs_taskdefinition:
    containers:
    - name: simple-app
      cpu: 10
      essential: true
      image: "httpd:2.4"
      memory: 300
      mountPoints:
      - containerPath: /usr/local/apache2/htdocs
        sourceVolume: my-vol
      portMappings:
      - containerPort: 80
        hostPort: 80
      logConfiguration:
        logDriver: awslogs
        options:
          awslogs-group: /ecs/test-cluster-taskdef
          awslogs-region: us-west-2
          awslogs-stream-prefix: ecs
    - name: busybox
      command:
        - >
          /bin/sh -c "while true; do echo '<html><head><title>Amazon ECS Sample App</title></head><body><div><h1>Amazon ECS Sample App</h1><h2>Congratulations!
          </h2><p>Your application is now running on a container in Amazon ECS.</p>' > top; /bin/date > date ; echo '</div></body></html>' > bottom;
          cat top date bottom > /usr/local/apache2/htdocs/index.html ; sleep 1; done"
      cpu: 10
      entryPoint:
      - sh
      - "-c"
      essential: false
      image: busybox
      memory: 200
      volumesFrom:
      - sourceContainer: simple-app
    volumes:
    - name: my-vol
    family: test-cluster-taskdef
    state: present
  register: task_output

- name: Create task definition
  community.aws.ecs_taskdefinition:
    family: nginx
    containers:
    - name: nginx
      essential: true
      image: "nginx"
      portMappings:
      - containerPort: 8080
        hostPort: 8080
      cpu: 512
      memory: 1024
    state: present

- name: Create task definition
  community.aws.ecs_taskdefinition:
    family: nginx
    containers:
    - name: nginx
      essential: true
      image: "nginx"
      portMappings:
      - containerPort: 8080
        hostPort: 8080
    launch_type: FARGATE
    cpu: 512
    memory: 1024
    state: present
    network_mode: awsvpc

- name: Create task definition
  community.aws.ecs_taskdefinition:
    family: nginx
    containers:
    - name: nginx
      essential: true
      image: "nginx"
      portMappings:
      - containerPort: 8080
        hostPort: 8080
      cpu: 512
      memory: 1024
      dependsOn:
      - containerName: "simple-app"
        condition: "start"

# Create Task Definition with Environment Variables and Secrets
- name: Create task definition
  community.aws.ecs_taskdefinition:
    family: nginx
    containers:
    - name: nginx
      essential: true
      image: "nginx"
      environment:
        - name: "PORT"
          value: "8080"
      secrets:
        # For variables stored in Secrets Manager
        - name: "NGINX_HOST"
          valueFrom: "arn:aws:secretsmanager:us-west-2:123456789012:secret:nginx/NGINX_HOST"
        # For variables stored in Parameter Store
        - name: "API_KEY"
          valueFrom: "arn:aws:ssm:us-west-2:123456789012:parameter/nginx/API_KEY"
    launch_type: FARGATE
    cpu: 512
    memory: 1GB
    state: present
    network_mode: awsvpc

# Create Task Definition with health check
- name: Create task definition
  community.aws.ecs_taskdefinition:
    family: nginx
    containers:
    - name: nginx
      essential: true
      image: "nginx"
      portMappings:
      - containerPort: 8080
        hostPort: 8080
      cpu: 512
      memory: 1024
      healthCheck:
        command:
            - CMD-SHELL
            - /app/healthcheck.py
        interval: 60
        retries: 3
        startPeriod: 15
        timeout: 15
    state: present
```

## [Return Values](ecs_taskdefinition_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **taskdefinition**  dictionary | a reflection of the input parameters  **Returned:** always |

### Authors

- Mark Chance (@Java1Guy)
- Alina Buzachis (@alinabuzachis)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
