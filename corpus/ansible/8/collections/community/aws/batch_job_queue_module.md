---
collection: ansible
version: "8"
title: "community.aws.batch_job_queue module – Manage AWS Batch Job Queues"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/batch_job_queue_module.html
fetched_at: 2026-07-28T01:40:17+00:00
---
# community.aws.batch_job_queue module – Manage AWS Batch Job Queues

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
> see [Requirements](batch_job_queue_module.md#ansible-collections-community-aws-batch-job-queue-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.batch_job_queue`.

New in community.aws 1.0.0

- [Synopsis](batch_job_queue_module.md#synopsis)
- [Requirements](batch_job_queue_module.md#requirements)
- [Parameters](batch_job_queue_module.md#parameters)
- [Notes](batch_job_queue_module.md#notes)
- [Examples](batch_job_queue_module.md#examples)
- [Return Values](batch_job_queue_module.md#return-values)

## [Synopsis](batch_job_queue_module.md#id1)

- This module allows the management of AWS Batch Job Queues.
- It is idempotent and supports “Check” mode.
- Use module [community.aws.batch_compute_environment](batch_compute_environment_module.md#ansible-collections-community-aws-batch-compute-environment-module) to manage the compute environment, [community.aws.batch_job_queue](batch_job_queue_module.md#ansible-collections-community-aws-batch-job-queue-module) to manage job queues, [community.aws.batch_job_definition](batch_job_definition_module.md#ansible-collections-community-aws-batch-job-definition-module) to manage job definitions.
- Prior to release 5.0.0 this module was called `community.aws.aws_batch_job_queue`. The usage did not change.

Aliases: aws_batch_job_queue

## [Requirements](batch_job_queue_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](batch_job_queue_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **compute_environment_order**  list / elements=dictionary / required | The set of compute environments mapped to a job queue and their order relative to each other. The job scheduler uses this parameter to determine which compute environment should execute a given job. Compute environments must be in the VALID state before you can associate them with a job queue. You can associate up to 3 compute environments with a job queue. |
| **compute_environment**  string | The name of the compute environment. |
| **order**  integer | The relative priority of the environment. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **job_queue_name**  string / required | The name for the job queue. |
| **job_queue_state**  string | The state of the job queue. If the job queue state is ENABLED, it is able to accept jobs.  **Choices:**   - `"ENABLED"` ← (default) - `"DISABLED"` |
| **priority**  integer / required | The priority of the job queue. Job queues with a higher priority (or a lower integer value for the priority parameter) are evaluated first when associated with same compute environment. Priority is determined in ascending order, for example, a job queue with a priority value of 1 is given scheduling preference over a job queue with a priority value of 10. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Describes the desired state.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](batch_job_queue_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](batch_job_queue_module.md#id5)

```yaml+jinja
- name: My Batch Job Queue
  community.aws.batch_job_queue:
    job_queue_name: jobQueueName
    state: present
    region: us-east-1
    job_queue_state: ENABLED
    priority: 1
    compute_environment_order:
    - order: 1
      compute_environment: my_compute_env1
    - order: 2
      compute_environment: my_compute_env2
  register: batch_job_queue_action

- name: show results
  ansible.builtin.debug:
    var: batch_job_queue_action
```

## [Return Values](batch_job_queue_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  dictionary | returns what action was taken, whether something was changed, invocation and response  **Returned:** always  **Sample:** `{"batch_job_queue_action": "updated", "changed": false, "response": {"job_queue_arn": "arn:aws:batch:....", "job_queue_name": "<name>", "priority": 1, "state": "DISABLED", "status": "UPDATING", "status_reason": "JobQueue Healthy"}}` |

### Authors

- Jon Meran (@jonmer85)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
