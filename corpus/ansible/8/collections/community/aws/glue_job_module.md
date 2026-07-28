---
collection: ansible
version: "8"
title: "community.aws.glue_job module – Manage an AWS Glue job"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/glue_job_module.html
fetched_at: 2026-07-28T01:41:18+00:00
---
# community.aws.glue_job module – Manage an AWS Glue job

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
> see [Requirements](glue_job_module.md#ansible-collections-community-aws-glue-job-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.glue_job`.

New in community.aws 1.0.0

- [Synopsis](glue_job_module.md#synopsis)
- [Requirements](glue_job_module.md#requirements)
- [Parameters](glue_job_module.md#parameters)
- [Notes](glue_job_module.md#notes)
- [Examples](glue_job_module.md#examples)
- [Return Values](glue_job_module.md#return-values)

## [Synopsis](glue_job_module.md#id1)

- Manage an AWS Glue job. See <https://aws.amazon.com/glue/> for details.
- Prior to release 5.0.0 this module was called `community.aws.aws_glue_job`. The usage did not change.

Aliases: aws_glue_job

## [Requirements](glue_job_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](glue_job_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **allocated_capacity**  integer | The number of AWS Glue data processing units (DPUs) to allocate to this Job. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **command_name**  string | The name of the job command. This must be ‘glueetl’.  **Default:** `"glueetl"` |
| **command_python_version**  string  *added in community.aws 2.2.0* | Python version being used to execute a Python shell job.  AWS currently supports `'2'` or `'3'`. |
| **command_script_location**  string | The S3 path to a script that executes a job.  Required when *state=present*. |
| **connections**  list / elements=string | A list of Glue connections used for this job. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **default_arguments**  dictionary | A dict of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. |
| **description**  string | Description of the job being defined. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **glue_version**  string  *added in community.aws 1.5.0* | Glue version determines the versions of Apache Spark and Python that AWS Glue supports. |
| **max_concurrent_runs**  integer | The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit. |
| **max_retries**  integer | The maximum number of times to retry this job if it fails. |
| **name**  string / required | The name you assign to this job definition. It must be unique in your account. |
| **number_of_workers**  integer  *added in community.aws 1.5.0* | The number of workers of a defined workerType that are allocated when a job runs. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **role**  string | The name or ARN of the IAM role associated with this job.  Required when *state=present*. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string / required | Create or delete the AWS Glue job.  **Choices:**   - `"present"` - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **timeout**  integer | The job timeout in minutes. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **worker_type**  string  *added in community.aws 1.5.0* | The type of predefined worker that is allocated when a job runs.  **Choices:**   - `"Standard"` - `"G.1X"` - `"G.2X"` |

## [Notes](glue_job_module.md#id4)

> **Note:**
>
> - Support for *tags* and *purge_tags* was added in release 2.2.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](glue_job_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create an AWS Glue job
- community.aws.glue_job:
    command_script_location: "s3://s3bucket/script.py"
    default_arguments:
      "--extra-py-files": s3://s3bucket/script-package.zip
      "--TempDir": "s3://s3bucket/temp/"
    name: my-glue-job
    role: my-iam-role
    state: present

# Delete an AWS Glue job
- community.aws.glue_job:
    name: my-glue-job
    state: absent
```

## [Return Values](glue_job_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allocated_capacity**  integer | The number of AWS Glue data processing units (DPUs) allocated to runs of this job. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.  **Returned:** when state is present  **Sample:** `10` |
| **command**  complex | The JobCommand that executes this job.  **Returned:** when state is present |
| **name**  string | The name of the job command.  **Returned:** when state is present  **Sample:** `"glueetl"` |
| **python_version**  string | Specifies the Python version.  **Returned:** when state is present  **Sample:** `"3"` |
| **script_location**  string | Specifies the S3 path to a script that executes a job.  **Returned:** when state is present  **Sample:** `"mybucket/myscript.py"` |
| **connections**  dictionary | The connections used for this job.  **Returned:** when state is present  **Sample:** `"{ Connections: [ 'list', 'of', 'connections' ] }"` |
| **created_on**  string | The time and date that this job definition was created.  **Returned:** when state is present  **Sample:** `"2018-04-21T05:19:58.326000+00:00"` |
| **default_arguments**  dictionary | The default arguments for this job, specified as name-value pairs.  **Returned:** when state is present  **Sample:** `{"mykey1": "myvalue1"}` |
| **description**  string | Description of the job being defined.  **Returned:** when state is present  **Sample:** `"My first Glue job"` |
| **execution_property**  complex | An ExecutionProperty specifying the maximum number of concurrent runs allowed for this job.  **Returned:** always |
| **max_concurrent_runs**  integer | The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit.  **Returned:** when state is present  **Sample:** `1` |
| **glue_version**  string | Glue version.  **Returned:** when state is present  **Sample:** `"2.0"` |
| **job_name**  string | The name of the AWS Glue job.  **Returned:** always  **Sample:** `"my-glue-job"` |
| **last_modified_on**  string | The last point in time when this job definition was modified.  **Returned:** when state is present  **Sample:** `"2018-04-21T05:19:58.326000+00:00"` |
| **max_retries**  integer | The maximum number of times to retry this job after a JobRun fails.  **Returned:** when state is present  **Sample:** `5` |
| **name**  string | The name assigned to this job definition.  **Returned:** when state is present  **Sample:** `"my-glue-job"` |
| **role**  string | The name or ARN of the IAM role associated with this job.  **Returned:** when state is present  **Sample:** `"my-iam-role"` |
| **timeout**  integer | The job timeout in minutes.  **Returned:** when state is present  **Sample:** `300` |

### Authors

- Rob White (@wimnat)
- Vijayanand Sharma (@vijayanandsharma)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
