---
collection: ansible
version: "6"
title: "community.aws.lambda_alias module – Creates, updates or deletes AWS Lambda function aliases"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/lambda_alias_module.html
fetched_at: 2026-07-27T17:04:45+00:00
---
# community.aws.lambda_alias module – Creates, updates or deletes AWS Lambda function aliases

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
> see [Requirements](lambda_alias_module.md#ansible-collections-community-aws-lambda-alias-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.lambda_alias`.

New in community.aws 1.0.0

- [Synopsis](lambda_alias_module.md#synopsis)
- [Requirements](lambda_alias_module.md#requirements)
- [Parameters](lambda_alias_module.md#parameters)
- [Notes](lambda_alias_module.md#notes)
- [Examples](lambda_alias_module.md#examples)
- [Return Values](lambda_alias_module.md#return-values)

## [Synopsis](lambda_alias_module.md#id1)

- This module allows the management of AWS Lambda functions aliases via the Ansible framework. It is idempotent and supports “Check” mode. Use module [community.aws.lambda](lambda_module.md#ansible-collections-community-aws-lambda-module) to manage the lambda function itself and [community.aws.lambda_event](lambda_event_module.md#ansible-collections-community-aws-lambda-event-module) to manage event source mappings.

## [Requirements](lambda_alias_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](lambda_alias_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **description**  string | A short, user-defined function alias description. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **function_name**  string / required | The name of the function alias. |
| **function_version**  aliases: version  integer | Version associated with the Lambda function alias. A value of 0 (or omitted parameter) sets the alias to the $LATEST version. |
| **name**  aliases: alias_name  string / required | Name of the function alias. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Describes the desired state.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](lambda_alias_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](lambda_alias_module.md#id5)

```yaml+jinja
---
# Simple example to create a lambda function and publish a version
- hosts: localhost
  gather_facts: no
  vars:
    state: present
    project_folder: /path/to/deployment/package
    deployment_package: lambda.zip
    account: 123456789012
    production_version: 5
  tasks:
  - name: AWS Lambda Function
    lambda:
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
    lambda_info:
      name: myLambdaFunction
    register: lambda_info
  - name: show results
    ansible.builtin.debug:
      msg: "{{ lambda_info['lambda_facts'] }}"

# The following will set the Dev alias to the latest version ($LATEST) since version is omitted (or = 0)
  - name: "alias 'Dev' for function {{ lambda_info.lambda_facts.FunctionName }} "
    community.aws.lambda_alias:
      state: "{{ state | default('present') }}"
      function_name: "{{ lambda_info.lambda_facts.FunctionName }}"
      name: Dev
      description: Development is $LATEST version

# The QA alias will only be created when a new version is published (i.e. not = '$LATEST')
  - name: "alias 'QA' for function {{ lambda_info.lambda_facts.FunctionName }} "
    community.aws.lambda_alias:
      state: "{{ state | default('present') }}"
      function_name: "{{ lambda_info.lambda_facts.FunctionName }}"
      name: QA
      version: "{{ lambda_info.lambda_facts.Version }}"
      description: "QA is version {{ lambda_info.lambda_facts.Version }}"
    when: lambda_info.lambda_facts.Version != "$LATEST"

# The Prod alias will have a fixed version based on a variable
  - name: "alias 'Prod' for function {{ lambda_info.lambda_facts.FunctionName }} "
    community.aws.lambda_alias:
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
| **alias_arn**  string | Full ARN of the function, including the alias  Returned: success  Sample: `"arn:aws:lambda:us-west-2:123456789012:function:myFunction:dev"` |
| **description**  string | A short description of the alias  Returned: success  Sample: `"The development stage for my hot new app"` |
| **function_version**  string | The qualifier that the alias refers to  Returned: success  Sample: `"$LATEST"` |
| **name**  string | The name of the alias assigned  Returned: success  Sample: `"dev"` |
| **revision_id**  string | A unique identifier that changes when you update the alias.  Returned: success  Sample: `"12345678-1234-1234-1234-123456789abc"` |

### Authors

- Pierre Jodouin (@pjodouin), Ryan Scott Brown (@ryansb)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
