---
collection: ansible
version: "8"
title: "amazon.aws.lambda_alias module – Creates, updates or deletes AWS Lambda function aliases"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/lambda_alias_module.html
fetched_at: 2026-07-28T01:06:57+00:00
---
# amazon.aws.lambda_alias module – Creates, updates or deletes AWS Lambda function aliases

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
> see [Requirements](lambda_alias_module.md#ansible-collections-amazon-aws-lambda-alias-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.lambda_alias`.

New in amazon.aws 5.0.0

- [Synopsis](lambda_alias_module.md#synopsis)
- [Requirements](lambda_alias_module.md#requirements)
- [Parameters](lambda_alias_module.md#parameters)
- [Notes](lambda_alias_module.md#notes)
- [Examples](lambda_alias_module.md#examples)
- [Return Values](lambda_alias_module.md#return-values)

## [Synopsis](lambda_alias_module.md#id1)

- This module allows the management of AWS Lambda functions aliases via the Ansible framework. It is idempotent and supports “Check” mode. Use module [amazon.aws.lambda](lambda_module.md#ansible-collections-amazon-aws-lambda-module) to manage the lambda function itself and [amazon.aws.lambda_event](lambda_event_module.md#ansible-collections-amazon-aws-lambda-event-module) to manage event source mappings.
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](lambda_alias_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](lambda_alias_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | A short, user-defined function alias description. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **function_name**  string / required | The name of the function alias. |
| **function_version**  aliases: version  integer | Version associated with the Lambda function alias. A value of 0 (or omitted parameter) sets the alias to the $LATEST version.  **Default:** `0` |
| **name**  aliases: alias_name  string / required | Name of the function alias. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Describes the desired state.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](lambda_alias_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](lambda_alias_module.md#id5)

```yaml+jinja
---
# Simple example to create a lambda function and publish a version
- hosts: localhost
  gather_facts: false
  vars:
    state: present
    project_folder: /path/to/deployment/package
    deployment_package: lambda.zip
    account: 123456789012
    production_version: 5
  tasks:
  - name: AWS Lambda Function
    amazon.aws.lambda:
      state: "{{ state | default('present') }}"
      name: myLambdaFunction
      publish: True
      description: lambda function description
      code_s3_bucket: package-bucket
      code_s3_key: "lambda/{{ deployment_package }}"
      local_path: "{{ project_folder }}/{{ deployment_package }}"
      runtime: python2.7
      timeout: 5
      handler: lambda.handler
      memory_size: 128
      role: "arn:aws:iam::{{ account }}:role/API2LambdaExecRole"

  - name: Get information
    amazon.aws.lambda_info:
      name: myLambdaFunction
    register: lambda_info
  - name: show results
    ansible.builtin.debug:
      msg: "{{ lambda_info['lambda_facts'] }}"

# The following will set the Dev alias to the latest version ($LATEST) since version is omitted (or = 0)
  - name: "alias 'Dev' for function {{ lambda_info.lambda_facts.FunctionName }} "
    amazon.aws.lambda_alias:
      state: "{{ state | default('present') }}"
      function_name: "{{ lambda_info.lambda_facts.FunctionName }}"
      name: Dev
      description: Development is $LATEST version

# The QA alias will only be created when a new version is published (i.e. not = '$LATEST')
  - name: "alias 'QA' for function {{ lambda_info.lambda_facts.FunctionName }} "
    amazon.aws.lambda_alias:
      state: "{{ state | default('present') }}"
      function_name: "{{ lambda_info.lambda_facts.FunctionName }}"
      name: QA
      version: "{{ lambda_info.lambda_facts.Version }}"
      description: "QA is version {{ lambda_info.lambda_facts.Version }}"
    when: lambda_info.lambda_facts.Version != "$LATEST"

# The Prod alias will have a fixed version based on a variable
  - name: "alias 'Prod' for function {{ lambda_info.lambda_facts.FunctionName }} "
    amazon.aws.lambda_alias:
      state: "{{ state | default('present') }}"
      function_name: "{{ lambda_info.lambda_facts.FunctionName }}"
      name: Prod
      version: "{{ production_version }}"
      description: "Production is version {{ production_version }}"
```

## [Return Values](lambda_alias_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **alias_arn**  string | Full ARN of the function, including the alias  **Returned:** success  **Sample:** `"arn:aws:lambda:us-west-2:123456789012:function:myFunction:dev"` |
| **description**  string | A short description of the alias  **Returned:** success  **Sample:** `"The development stage for my hot new app"` |
| **function_version**  string | The qualifier that the alias refers to  **Returned:** success  **Sample:** `"$LATEST"` |
| **name**  string | The name of the alias assigned  **Returned:** success  **Sample:** `"dev"` |
| **revision_id**  string | A unique identifier that changes when you update the alias.  **Returned:** success  **Sample:** `"12345678-1234-1234-1234-123456789abc"` |

### Authors

- Pierre Jodouin (@pjodouin)
- Ryan Scott Brown (@ryansb)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
