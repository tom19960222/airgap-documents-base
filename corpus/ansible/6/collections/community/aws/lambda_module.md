---
collection: ansible
version: "6"
title: "community.aws.lambda module – Manage AWS Lambda functions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/lambda_module.html
fetched_at: 2026-07-27T17:04:45+00:00
---
# community.aws.lambda module – Manage AWS Lambda functions

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
> see [Requirements](lambda_module.md#ansible-collections-community-aws-lambda-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.lambda`.

New in community.aws 1.0.0

- [Synopsis](lambda_module.md#synopsis)
- [Requirements](lambda_module.md#requirements)
- [Parameters](lambda_module.md#parameters)
- [Notes](lambda_module.md#notes)
- [Examples](lambda_module.md#examples)
- [Return Values](lambda_module.md#return-values)

## [Synopsis](lambda_module.md#id1)

- Allows for the management of Lambda functions.

## [Requirements](lambda_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](lambda_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **dead_letter_arn**  string | The parent object that contains the target Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **description**  string | A short, user-defined function description. Lambda does not use this value. Assign a meaningful description as you see fit. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **environment_variables**  dictionary | A dictionary of environment variables the Lambda function is given. |
| **handler**  string | The function within your code that Lambda calls to begin execution. |
| **kms_key_arn**  string  added in community.aws 3.3.0 | The KMS key ARN used to encrypt the function’s environment variables. |
| **memory_size**  integer | The amount of memory, in MB, your Lambda function is given.  Default: `128` |
| **name**  string / required | The name you want to assign to the function you are uploading. Cannot be changed. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **role**  string | The Amazon Resource Name (ARN) of the IAM role that Lambda assumes when it executes your function to access any other Amazon Web Services (AWS) resources. You may use the bare ARN if the role belongs to the same AWS account.  Required when *state=present*. |
| **runtime**  string | The runtime environment for the Lambda function you are uploading.  Required when creating a function. Uses parameters as described in boto3 docs.  Required when *state=present*.  For supported list of runtimes, see <https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html>. |
| **s3_bucket**  string | Amazon S3 bucket name where the .zip file containing your deployment package is stored.  If *state=present* then either *zip_file* or *s3_bucket* must be present.  *s3_bucket* and *s3_key* are required together. |
| **s3_key**  string | The Amazon S3 object (the deployment package) key name you want to upload.  *s3_bucket* and *s3_key* are required together. |
| **s3_object_version**  string | The Amazon S3 object (the deployment package) version you want to upload. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Create or delete Lambda function.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Tag dict to apply to the function. |
| **timeout**  integer | The function maximum execution time in seconds after which Lambda should terminate the function.  Default: `3` |
| **tracing_mode**  string | Set mode to ‘Active’ to sample and trace incoming requests with AWS X-Ray. Turned off (set to ‘PassThrough’) by default.  Choices:   - `"Active"` - `"PassThrough"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **vpc_security_group_ids**  list / elements=string | List of VPC security group IDs to associate with the Lambda function.  Required when *vpc_subnet_ids* is used. |
| **vpc_subnet_ids**  list / elements=string | List of subnet IDs to run Lambda function in.  Use this option if you need to access resources in your VPC. Leave empty if you don’t want to run the function in a VPC.  If set, *vpc_security_group_ids* must also be set. |
| **zip_file**  aliases: src  string | A .zip file containing your deployment package  If *state=present* then either *zip_file* or *s3_bucket* must be present. |

## [Notes](lambda_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](lambda_module.md#id5)

```yaml+jinja
# Create Lambda functions
- name: looped creation
  community.aws.lambda:
    name: '{{ item.name }}'
    state: present
    zip_file: '{{ item.zip_file }}'
    runtime: 'python2.7'
    role: 'arn:aws:iam::987654321012:role/lambda_basic_execution'
    handler: 'hello_python.my_handler'
    vpc_subnet_ids:
    - subnet-123abcde
    - subnet-edcba321
    vpc_security_group_ids:
    - sg-123abcde
    - sg-edcba321
    environment_variables: '{{ item.env_vars }}'
    tags:
      key1: 'value1'
  loop:
    - name: HelloWorld
      zip_file: hello-code.zip
      env_vars:
        key1: "first"
        key2: "second"
    - name: ByeBye
      zip_file: bye-code.zip
      env_vars:
        key1: "1"
        key2: "2"

# To remove previously added tags pass an empty dict
- name: remove tags
  community.aws.lambda:
    name: 'Lambda function'
    state: present
    zip_file: 'code.zip'
    runtime: 'python2.7'
    role: 'arn:aws:iam::987654321012:role/lambda_basic_execution'
    handler: 'hello_python.my_handler'
    tags: {}

# Basic Lambda function deletion
- name: Delete Lambda functions HelloWorld and ByeBye
  community.aws.lambda:
    name: '{{ item }}'
    state: absent
  loop:
    - HelloWorld
    - ByeBye
```

## [Return Values](lambda_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **code**  dictionary | The lambda function’s code returned by get_function in boto3.  Returned: success |
| **location**  string | The presigned URL you can use to download the function’s .zip file that you previously uploaded.  The URL is valid for up to 10 minutes.  Returned: success  Sample: `"https://prod-04-2014-tasks.s3.us-east-1.amazonaws.com/snapshots/sample"` |
| **repository_type**  string | The repository from which you can download the function.  Returned: success  Sample: `"S3"` |
| **configuration**  dictionary | the lambda function’s configuration metadata returned by get_function in boto3  Returned: success |
| **code_sha256**  string | The SHA256 hash of the function’s deployment package.  Returned: success  Sample: `"zOAGfF5JLFuzZoSNirUtOrQp+S341IOA3BcoXXoaIaU="` |
| **code_size**  integer | The size of the function’s deployment package in bytes.  Returned: success  Sample: `123` |
| **dead_letter_config**  dictionary | The function’s dead letter queue.  Returned: when the function has a dead letter queue configured  Sample: `{"target_arn": "arn:aws:lambda:us-east-1:123456789012:function:myFunction:1"}` |
| **target_arn**  string | The ARN of an SQS queue or SNS topic.  Returned: when the function has a dead letter queue configured  Sample: `"arn:aws:lambda:us-east-1:123456789012:function:myFunction:1"` |
| **description**  string | The function’s description.  Returned: success  Sample: `"My function"` |
| **environment**  dictionary | The function’s environment variables.  Returned: when environment variables exist |
| **error**  dictionary | Error message for environment variables that could not be applied.  Returned: when there is an error applying environment variables |
| **error_code**  string | The error code.  Returned: when there is an error applying environment variables |
| **message**  string | The error message.  Returned: when there is an error applying environment variables |
| **variables**  dictionary | Environment variable key-value pairs.  Returned: when environment variables exist  Sample: `{"key": "value"}` |
| **function_arn**  string | The function’s Amazon Resource Name (ARN).  Returned: on success  Sample: `"arn:aws:lambda:us-east-1:123456789012:function:myFunction:1"` |
| **function_name**  string | The function’s name.  Returned: on success  Sample: `"myFunction"` |
| **handler**  string | The function Lambda calls to begin executing your function.  Returned: on success  Sample: `"index.handler"` |
| **last_modified**  string | The date and time that the function was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ssTZD).  Returned: on success  Sample: `"2017-08-01T00:00:00.000+0000"` |
| **memory_size**  integer | The memory allocated to the function.  Returned: on success  Sample: `128` |
| **revision_id**  string | The latest updated revision of the function or alias.  Returned: on success  Sample: `"a2x9886d-d48a-4a0c-ab64-82abc005x80c"` |
| **role**  string | The function’s execution role.  Returned: on success  Sample: `"arn:aws:iam::123456789012:role/lambda_basic_execution"` |
| **runtime**  string | The funtime environment for the Lambda function.  Returned: on success  Sample: `"nodejs6.10"` |
| **timeout**  integer | The amount of time that Lambda allows a function to run before terminating it.  Returned: on success  Sample: `3` |
| **tracing_config**  dictionary | The function’s AWS X-Ray tracing configuration.  Returned: on success  Sample: `{"mode": "Active"}` |
| **mode**  string | The tracing mode.  Returned: on success  Sample: `"Active"` |
| **version**  string | The version of the Lambda function.  Returned: on success  Sample: `"1"` |
| **vpc_config**  dictionary | The function’s networking configuration.  Returned: on success  Sample: `{"security_group_ids": [], "subnet_ids": [], "vpc_id": "123"}` |

### Authors

- Steyn Huizinga (@steynovich)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
