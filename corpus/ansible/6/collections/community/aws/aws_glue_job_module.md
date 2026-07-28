---
collection: ansible
version: "6"
title: "community.aws.aws_glue_job module – Manage an AWS Glue job"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_glue_job_module.html
fetched_at: 2026-07-27T17:03:26+00:00
---
# community.aws.aws_glue_job module – Manage an AWS Glue job

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
> see [Requirements](aws_glue_job_module.md#ansible-collections-community-aws-aws-glue-job-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_glue_job`.

New in community.aws 1.0.0

- [Synopsis](aws_glue_job_module.md#synopsis)
- [Requirements](aws_glue_job_module.md#requirements)
- [Parameters](aws_glue_job_module.md#parameters)
- [Notes](aws_glue_job_module.md#notes)
- [Examples](aws_glue_job_module.md#examples)
- [Return Values](aws_glue_job_module.md#return-values)

## [Synopsis](aws_glue_job_module.md#id1)

- Manage an AWS Glue job. See <https://aws.amazon.com/glue/> for details.

## [Requirements](aws_glue_job_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_glue_job_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allocated_capacity**  integer | The number of AWS Glue data processing units (DPUs) to allocate to this Job. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **command_name**  string | The name of the job command. This must be ‘glueetl’.  Default: `"glueetl"` |
| **command_python_version**  string  added in community.aws 2.2.0 | Python version being used to execute a Python shell job.  AWS currently supports `'2'` or `'3'`. |
| **command_script_location**  string | The S3 path to a script that executes a job.  Required when *state=present*. |
| **connections**  list / elements=string | A list of Glue connections used for this job. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **default_arguments**  dictionary | A dict of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. |
| **description**  string | Description of the job being defined. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **glue_version**  string  added in community.aws 1.5.0 | Glue version determines the versions of Apache Spark and Python that AWS Glue supports. |
| **max_concurrent_runs**  integer | The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit. |
| **max_retries**  integer | The maximum number of times to retry this job if it fails. |
| **name**  string / required | The name you assign to this job definition. It must be unique in your account. |
| **number_of_workers**  integer  added in community.aws 1.5.0 | The number of workers of a defined workerType that are allocated when a job runs. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean  added in community.aws 2.2.0 | If `true`, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **role**  string | The name or ARN of the IAM role associated with this job.  Required when *state=present*. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string / required | Create or delete the AWS Glue job.  Choices:   - `"present"` - `"absent"` |
| **tags**  dictionary  added in community.aws 2.2.0 | A hash/dictionary of tags to be applied to the job.  Remove completely or specify an empty dictionary to remove all tags. |
| **timeout**  integer | The job timeout in minutes. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **worker_type**  string  added in community.aws 1.5.0 | The type of predefined worker that is allocated when a job runs.  Choices:   - `"Standard"` - `"G.1X"` - `"G.2X"` |

## [Notes](aws_glue_job_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_glue_job_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create an AWS Glue job
- community.aws.aws_glue_job:
    command_script_location: "s3://s3bucket/script.py"
    default_arguments:
      "--extra-py-files": s3://s3bucket/script-package.zip
      "--TempDir": "s3://s3bucket/temp/"
    name: my-glue-job
    role: my-iam-role
    state: present

# Delete an AWS Glue job
- community.aws.aws_glue_job:
    name: my-glue-job
    state: absent
```

## [Return Values](aws_glue_job_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allocated_capacity**  integer | The number of AWS Glue data processing units (DPUs) allocated to runs of this job. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.  Returned: when state is present  Sample: `10` |
| **command**  complex | The JobCommand that executes this job.  Returned: when state is present |
| **name**  string | The name of the job command.  Returned: when state is present  Sample: `"glueetl"` |
| **python_version**  string | Specifies the Python version.  Returned: when state is present  Sample: `"3"` |
| **script_location**  string | Specifies the S3 path to a script that executes a job.  Returned: when state is present  Sample: `"mybucket/myscript.py"` |
| **connections**  dictionary | The connections used for this job.  Returned: when state is present  Sample: `"{ Connections: [ 'list', 'of', 'connections' ] }"` |
| **created_on**  string | The time and date that this job definition was created.  Returned: when state is present  Sample: `"2018-04-21T05:19:58.326000+00:00"` |
| **default_arguments**  dictionary | The default arguments for this job, specified as name-value pairs.  Returned: when state is present  Sample: `{"mykey1": "myvalue1"}` |
| **description**  string | Description of the job being defined.  Returned: when state is present  Sample: `"My first Glue job"` |
| **execution_property**  complex | An ExecutionProperty specifying the maximum number of concurrent runs allowed for this job.  Returned: always |
| **max_concurrent_runs**  integer | The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit.  Returned: when state is present  Sample: `1` |
| **glue_version**  string | Glue version.  Returned: when state is present  Sample: `"2.0"` |
| **job_name**  string | The name of the AWS Glue job.  Returned: always  Sample: `"my-glue-job"` |
| **last_modified_on**  string | The last point in time when this job definition was modified.  Returned: when state is present  Sample: `"2018-04-21T05:19:58.326000+00:00"` |
| **max_retries**  integer | The maximum number of times to retry this job after a JobRun fails.  Returned: when state is present  Sample: `5` |
| **name**  string | The name assigned to this job definition.  Returned: when state is present  Sample: `"my-glue-job"` |
| **role**  string | The name or ARN of the IAM role associated with this job.  Returned: when state is present  Sample: `"my-iam-role"` |
| **timeout**  integer | The job timeout in minutes.  Returned: when state is present  Sample: `300` |

### Authors

- Rob White (@wimnat)
- Vijayanand Sharma (@vijayanandsharma)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
