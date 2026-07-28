---
collection: ansible
version: "6"
title: "community.aws.aws_batch_job_definition module – Manage AWS Batch Job Definitions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_batch_job_definition_module.html
fetched_at: 2026-07-27T17:03:14+00:00
---
# community.aws.aws_batch_job_definition module – Manage AWS Batch Job Definitions

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
> see [Requirements](aws_batch_job_definition_module.md#ansible-collections-community-aws-aws-batch-job-definition-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_batch_job_definition`.

New in community.aws 1.0.0

- [Synopsis](aws_batch_job_definition_module.md#synopsis)
- [Requirements](aws_batch_job_definition_module.md#requirements)
- [Parameters](aws_batch_job_definition_module.md#parameters)
- [Notes](aws_batch_job_definition_module.md#notes)
- [Examples](aws_batch_job_definition_module.md#examples)
- [Return Values](aws_batch_job_definition_module.md#return-values)

## [Synopsis](aws_batch_job_definition_module.md#id1)

- This module allows the management of AWS Batch Job Definitions.
- It is idempotent and supports “Check” mode.
- Use module [community.aws.aws_batch_compute_environment](aws_batch_compute_environment_module.md#ansible-collections-community-aws-aws-batch-compute-environment-module) to manage the compute environment, [community.aws.aws_batch_job_queue](aws_batch_job_queue_module.md#ansible-collections-community-aws-aws-batch-job-queue-module) to manage job queues, [community.aws.aws_batch_job_definition](aws_batch_job_definition_module.md#ansible-collections-community-aws-aws-batch-job-definition-module) to manage job definitions.

## [Requirements](aws_batch_job_definition_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_batch_job_definition_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attempts**  integer | Retry strategy - The number of times to move a job to the RUNNABLE status. You may specify between 1 and 10 attempts. If attempts is greater than one, the job is retried if it fails until it has moved to RUNNABLE that many times. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **command**  list / elements=string | The command that is passed to the container. This parameter maps to Cmd in the Create a container section of the Docker Remote API and the COMMAND parameter to docker run. For more information, see <https://docs.docker.com/engine/reference/builder/#cmd>. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **environment**  list / elements=dictionary | The environment variables to pass to a container. This parameter maps to Env in the Create a container section of the Docker Remote API and the –env option to docker run. |
| **name**  string | The name of the key value pair. For environment variables, this is the name of the environment variable. |
| **value**  string | The value of the key value pair. For environment variables, this is the value of the environment variable. |
| **image**  string / required | The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `repository-url/image-name:tag`. Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to Image in the Create a container section of the Docker Remote API and the IMAGE parameter of docker run. |
| **job_definition_arn**  string | The ARN for the job definition. |
| **job_definition_name**  string / required | The name for the job definition. |
| **job_role_arn**  string | The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions. |
| **memory**  integer / required | The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to Memory in the Create a container section of the Docker Remote API and the –memory option to docker run. |
| **mount_points**  list / elements=dictionary | The mount points for data volumes in your container. This parameter maps to Volumes in the Create a container section of the Docker Remote API and the –volume option to docker run. |
| **containerPath**  string | The path on the container at which to mount the host volume. |
| **readOnly**  string | If this value is true , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is `false`. |
| **sourceVolume**  string | The name of the volume to mount. |
| **parameters**  dictionary | Default parameter substitution placeholders to set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a SubmitJob request override any corresponding parameter defaults from the job definition. |
| **privileged**  string | When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user). This parameter maps to Privileged in the Create a container section of the Docker Remote API and the –privileged option to docker run. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **readonly_root_filesystem**  string | When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ReadonlyRootfs in the Create a container section of the Docker Remote API and the –read-only option to docker run. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Describes the desired state.  Choices:   - `"present"` ← (default) - `"absent"` |
| **type**  string / required | The type of job definition. |
| **ulimits**  list / elements=dictionary | A list of ulimits to set in the container. This parameter maps to Ulimits in the Create a container section of the Docker Remote API and the –ulimit option to docker run. |
| **hardLimit**  string | The hard limit for the ulimit type. |
| **name**  string | The type of the ulimit. |
| **softLimit**  string | The soft limit for the ulimit type. |
| **user**  string | The user name to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the –user option to docker run. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **vcpus**  integer / required | The number of vCPUs reserved for the container. This parameter maps to CpuShares in the Create a container section of the Docker Remote API and the –cpu-shares option to docker run. Each vCPU is equivalent to 1,024 CPU shares. |
| **volumes**  list / elements=dictionary | A list of data volumes used in a job. |
| **host**  string | The contents of the host parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume, but the data is not guaranteed to persist after the containers associated with it stop running. This is a dictionary with one property, sourcePath - The path on the host container instance that is presented to the container. If this parameter is empty,then the Docker daemon has assigned a host path for you. If the host parameter contains a sourcePath file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the sourcePath value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported. |
| **name**  string | The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the sourceVolume parameter of container definition mountPoints. |

## [Notes](aws_batch_job_definition_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_batch_job_definition_module.md#id5)

```yaml+jinja
---
- hosts: localhost
  gather_facts: no
  vars:
    state: present
  tasks:
- name: My Batch Job Definition
  community.aws.aws_batch_job_definition:
    job_definition_name: My Batch Job Definition
    state: present
    type: container
    parameters:
      Param1: Val1
      Param2: Val2
    image: <Docker Image URL>
    vcpus: 1
    memory: 512
    command:
      - python
      - run_my_script.py
      - arg1
    job_role_arn: <Job Role ARN>
    attempts: 3
  register: job_definition_create_result

- name: show results
  ansible.builtin.debug: var=job_definition_create_result
```

## [Return Values](aws_batch_job_definition_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  dictionary | returns what action was taken, whether something was changed, invocation and response  Returned: always  Sample: `{"aws_batch_job_definition_action": "none", "changed": false, "response": {"job_definition_arn": "arn:aws:batch:....", "job_definition_name": "<name>", "status": "INACTIVE", "type": "container"}}` |

### Authors

- Jon Meran (@jonmer85)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
