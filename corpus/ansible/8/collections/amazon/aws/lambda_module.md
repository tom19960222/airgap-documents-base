---
collection: ansible
version: "8"
title: "amazon.aws.lambda module – Manage AWS Lambda functions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/lambda_module.html
fetched_at: 2026-07-28T01:06:56+00:00
---
# amazon.aws.lambda module – Manage AWS Lambda functions

> **Note:**
>
> This module is part of the [amazon.aws collection](https://galaxy.ansible.com/ui/repo/published/amazon/aws/) (version 6.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](lambda_module.md#ansible-collections-amazon-aws-lambda-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.lambda`.

New in amazon.aws 5.0.0

- [Synopsis](lambda_module.md#synopsis)
- [Requirements](lambda_module.md#requirements)
- [Parameters](lambda_module.md#parameters)
- [Notes](lambda_module.md#notes)
- [Examples](lambda_module.md#examples)
- [Return Values](lambda_module.md#return-values)

## [Synopsis](lambda_module.md#id1)

- Allows for the management of Lambda functions.
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](lambda_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](lambda_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **architecture**  aliases: architectures  string  *added in amazon.aws 5.0.0* | The instruction set architecture that the function supports.  Requires one of *s3_bucket* or *zip_file*.  **Choices:**   - `"x86_64"` - `"arm64"` |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **dead_letter_arn**  string | The parent object that contains the target Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | A short, user-defined function description. Lambda does not use this value. Assign a meaningful description as you see fit.  **Default:** `""` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **environment_variables**  dictionary | A dictionary of environment variables the Lambda function is given. |
| **handler**  string | The function within your code that Lambda calls to begin execution. |
| **kms_key_arn**  string  *added in community.aws 3.3.0* | The KMS key ARN used to encrypt the function’s environment variables. |
| **layers**  list / elements=dictionary  *added in amazon.aws 5.5.0* | A list of function layers to add to the function’s execution environment.  Specify each layer by its ARN, including the version. |
| **layer_name**  aliases: layer_arn  string | The name or Amazon Resource Name (ARN) of the layer.  Mutually exclusive with *layer_version_arn*. |
| **layer_version_arn**  string | The ARN of the layer version.  Mutually exclusive with *layer_version_arn*. |
| **version**  aliases: layer_version  integer | The version number.  Required when *layer_name* is provided, ignored if not. |
| **memory_size**  integer | The amount of memory, in MB, your Lambda function is given.  **Default:** `128` |
| **name**  string / required | The name you want to assign to the function you are uploading. Cannot be changed. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **role**  string | The Amazon Resource Name (ARN) of the IAM role that Lambda assumes when it executes your function to access any other Amazon Web Services (AWS) resources. You may use the bare ARN if the role belongs to the same AWS account.  Required when *state=present*. |
| **runtime**  string | The runtime environment for the Lambda function you are uploading.  Required when creating a function. Uses parameters as described in boto3 docs.  Required when *state=present*.  For supported list of runtimes, see <https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html>. |
| **s3_bucket**  string | Amazon S3 bucket name where the .zip file containing your deployment package is stored.  If *state=present* then either *zip_file* or *s3_bucket* must be present.  *s3_bucket* and *s3_key* are required together. |
| **s3_key**  string | The Amazon S3 object (the deployment package) key name you want to upload.  *s3_bucket* and *s3_key* are required together. |
| **s3_object_version**  string | The Amazon S3 object (the deployment package) version you want to upload. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create or delete Lambda function.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **timeout**  integer | The function maximum execution time in seconds after which Lambda should terminate the function.  **Default:** `3` |
| **tracing_mode**  string | Set mode to ‘Active’ to sample and trace incoming requests with AWS X-Ray. Turned off (set to ‘PassThrough’) by default.  **Choices:**   - `"Active"` - `"PassThrough"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **vpc_security_group_ids**  list / elements=string | List of VPC security group IDs to associate with the Lambda function.  Required when *vpc_subnet_ids* is used. |
| **vpc_subnet_ids**  list / elements=string | List of subnet IDs to run Lambda function in.  Use this option if you need to access resources in your VPC. Leave empty if you don’t want to run the function in a VPC.  If set, *vpc_security_group_ids* must also be set. |
| **zip_file**  aliases: src  string | A .zip file containing your deployment package  If *state=present* then either *zip_file* or *s3_bucket* must be present. |

## [Notes](lambda_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](lambda_module.md#id5)

```yaml+jinja
# Create Lambda functions
- name: looped creation
  amazon.aws.lambda:
    name: '{{ item.name }}'
    state: present
    zip_file: '{{ item.zip_file }}'
    runtime: 'python2.7'
    role: 'arn:aws:iam::123456789012:role/lambda_basic_execution'
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
  amazon.aws.lambda:
    name: 'Lambda function'
    state: present
    zip_file: 'code.zip'
    runtime: 'python2.7'
    role: 'arn:aws:iam::123456789012:role/lambda_basic_execution'
    handler: 'hello_python.my_handler'
    tags: {}

# Basic Lambda function deletion
- name: Delete Lambda functions HelloWorld and ByeBye
  amazon.aws.lambda:
    name: '{{ item }}'
    state: absent
  loop:
    - HelloWorld
    - ByeBye

# Create Lambda functions with function layers
- name: looped creation
  amazon.aws.lambda:
    name: 'HelloWorld'
    state: present
    zip_file: 'hello-code.zip'
    runtime: 'python2.7'
    role: 'arn:aws:iam::123456789012:role/lambda_basic_execution'
    handler: 'hello_python.my_handler'
    layers:
        - layer_version_arn: 'arn:aws:lambda:us-east-1:123456789012:layer:python27-env:7'
```

## [Return Values](lambda_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **code**  dictionary | The lambda function’s code returned by get_function in boto3.  **Returned:** success |
| **location**  string | The presigned URL you can use to download the function’s .zip file that you previously uploaded.  The URL is valid for up to 10 minutes.  **Returned:** success  **Sample:** `"https://prod-04-2014-tasks.s3.us-east-1.amazonaws.com/snapshots/sample"` |
| **repository_type**  string | The repository from which you can download the function.  **Returned:** success  **Sample:** `"S3"` |
| **configuration**  dictionary | the lambda function’s configuration metadata returned by get_function in boto3  **Returned:** success |
| **architectures**  list / elements=string | The architectures supported by the function.  **Returned:** success  **Sample:** `["arm64"]` |
| **code_sha256**  string | The SHA256 hash of the function’s deployment package.  **Returned:** success  **Sample:** `"zOAGfF5JLFuzZoSNirUtOrQp+S341IOA3BcoXXoaIaU="` |
| **code_size**  integer | The size of the function’s deployment package in bytes.  **Returned:** success  **Sample:** `123` |
| **dead_letter_config**  dictionary | The function’s dead letter queue.  **Returned:** when the function has a dead letter queue configured  **Sample:** `{"target_arn": "arn:aws:lambda:us-east-1:123456789012:function:myFunction:1"}` |
| **target_arn**  string | The ARN of an SQS queue or SNS topic.  **Returned:** when the function has a dead letter queue configured  **Sample:** `"arn:aws:lambda:us-east-1:123456789012:function:myFunction:1"` |
| **description**  string | The function’s description.  **Returned:** success  **Sample:** `"My function"` |
| **environment**  dictionary | The function’s environment variables.  **Returned:** when environment variables exist |
| **error**  dictionary | Error message for environment variables that could not be applied.  **Returned:** when there is an error applying environment variables |
| **error_code**  string | The error code.  **Returned:** when there is an error applying environment variables |
| **message**  string | The error message.  **Returned:** when there is an error applying environment variables |
| **variables**  dictionary | Environment variable key-value pairs.  **Returned:** when environment variables exist  **Sample:** `{"key": "value"}` |
| **function_arn**  string | The function’s Amazon Resource Name (ARN).  **Returned:** on success  **Sample:** `"arn:aws:lambda:us-east-1:123456789012:function:myFunction:1"` |
| **function_name**  string | The function’s name.  **Returned:** on success  **Sample:** `"myFunction"` |
| **handler**  string | The function Lambda calls to begin executing your function.  **Returned:** on success  **Sample:** `"index.handler"` |
| **last_modified**  string | The date and time that the function was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ssTZD).  **Returned:** on success  **Sample:** `"2017-08-01T00:00:00.000+0000"` |
| **layers**  complex  *added in amazon.aws 5.5.0* | The function’s layers.  **Returned:** on success |
| **arn**  string | The Amazon Resource Name (ARN) of the function layer.  **Returned:** always  **Sample:** `"active"` |
| **code_size**  string | The size of the layer archive in bytes.  **Returned:** always |
| **signing_job_arn**  string | The Amazon Resource Name (ARN) of a signing job.  **Returned:** always |
| **signing_profile_version_arn**  string | The Amazon Resource Name (ARN) for a signing profile version.  **Returned:** always |
| **memory_size**  integer | The memory allocated to the function.  **Returned:** on success  **Sample:** `128` |
| **revision_id**  string | The latest updated revision of the function or alias.  **Returned:** on success  **Sample:** `"a2x9886d-d48a-4a0c-ab64-82abc005x80c"` |
| **role**  string | The function’s execution role.  **Returned:** on success  **Sample:** `"arn:aws:iam::123456789012:role/lambda_basic_execution"` |
| **runtime**  string | The funtime environment for the Lambda function.  **Returned:** on success  **Sample:** `"nodejs6.10"` |
| **timeout**  integer | The amount of time that Lambda allows a function to run before terminating it.  **Returned:** on success  **Sample:** `3` |
| **tracing_config**  dictionary | The function’s AWS X-Ray tracing configuration.  **Returned:** on success  **Sample:** `{"mode": "Active"}` |
| **mode**  string | The tracing mode.  **Returned:** on success  **Sample:** `"Active"` |
| **version**  string | The version of the Lambda function.  **Returned:** on success  **Sample:** `"1"` |
| **vpc_config**  dictionary | The function’s networking configuration.  **Returned:** on success  **Sample:** `{"security_group_ids": [], "subnet_ids": [], "vpc_id": "123"}` |

### Authors

- Steyn Huizinga (@steynovich)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
