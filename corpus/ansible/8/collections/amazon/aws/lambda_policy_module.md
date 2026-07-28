---
collection: ansible
version: "8"
title: "amazon.aws.lambda_policy module – Creates, updates or deletes AWS Lambda policy statements."
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/lambda_policy_module.html
fetched_at: 2026-07-28T01:07:01+00:00
---
# amazon.aws.lambda_policy module – Creates, updates or deletes AWS Lambda policy statements.

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
> see [Requirements](lambda_policy_module.md#ansible-collections-amazon-aws-lambda-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.lambda_policy`.

New in amazon.aws 5.0.0

- [Synopsis](lambda_policy_module.md#synopsis)
- [Requirements](lambda_policy_module.md#requirements)
- [Parameters](lambda_policy_module.md#parameters)
- [Notes](lambda_policy_module.md#notes)
- [Examples](lambda_policy_module.md#examples)
- [Return Values](lambda_policy_module.md#return-values)

## [Synopsis](lambda_policy_module.md#id1)

- This module allows the management of AWS Lambda policy statements.
- It is idempotent and supports “Check” mode.
- Use module [amazon.aws.lambda](lambda_module.md#ansible-collections-amazon-aws-lambda-module) to manage the lambda function itself, [amazon.aws.lambda_alias](lambda_alias_module.md#ansible-collections-amazon-aws-lambda-alias-module) to manage function aliases, [amazon.aws.lambda_event](lambda_event_module.md#ansible-collections-amazon-aws-lambda-event-module) to manage event source mappings such as Kinesis streams, [community.aws.execute_lambda](../../community/aws/execute_lambda_module.md#ansible-collections-community-aws-execute-lambda-module) to execute a lambda function and [amazon.aws.lambda_info](lambda_info_module.md#ansible-collections-amazon-aws-lambda-info-module) to gather information relating to one or more lambda functions.
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](lambda_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](lambda_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **action**  string / required | The AWS Lambda action you want to allow in this statement. Each Lambda action is a string starting with lambda: followed by the API name (see Operations ). For example, `lambda:CreateFunction` . You can use wildcard (`lambda:*`) to grant permission for all AWS Lambda actions. |
| **alias**  string | Name of the function alias. Mutually exclusive with *version*. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **event_source_token**  string | Token string representing source ARN or account. Mutually exclusive with *source_arn* or *source_account*. |
| **function_name**  aliases: lambda_function_arn, function_arn  string / required | Name of the Lambda function whose resource policy you are updating by adding a new permission.  You can specify a function name (for example, Thumbnail ) or you can specify Amazon Resource Name (ARN) of the  function (for example, `arn:aws:lambda:us-west-2:account-id:function:ThumbNail` ). AWS Lambda also allows you to  specify partial ARN (for example, `account-id:Thumbnail` ). Note that the length constraint applies only to the  ARN. If you specify only the function name, it is limited to 64 character in length. |
| **principal**  string / required | The principal who is getting this permission. It can be Amazon S3 service Principal (s3.amazonaws.com ) if you want Amazon S3 to invoke the function, an AWS account ID if you are granting cross-account permission, or any valid AWS service principal such as sns.amazonaws.com . For example, you might want to allow a custom application in another AWS account to push events to AWS Lambda by invoking your function. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **source_account**  string | The AWS account ID (without a hyphen) of the source owner. For example, if *source_arn* identifies a bucket, then this is the bucket owner’s account ID. You can use this additional condition to ensure the bucket you specify is owned by a specific account (it is possible the bucket owner deleted the bucket and some other AWS account created the bucket). You can also use this condition to specify all sources (that is, you don’t specify the *source_arn* ) owned by a specific account. |
| **source_arn**  string | This is optional; however, when granting Amazon S3 permission to invoke your function, you should specify this field with the bucket Amazon Resource Name (ARN) as its value. This ensures that only events generated from the specified bucket can invoke the function. |
| **state**  string | Describes the desired state.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **statement_id**  aliases: sid  string / required | A unique statement identifier. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **version**  integer | Version of the Lambda function. Mutually exclusive with *alias*. |

## [Notes](lambda_policy_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](lambda_policy_module.md#id5)

```yaml+jinja
- name: Lambda S3 event notification
  amazon.aws.lambda_policy:
    state: present
    function_name: functionName
    alias: Dev
    statement_id: lambda-s3-myBucket-create-data-log
    action: lambda:InvokeFunction
    principal: s3.amazonaws.com
    source_arn: arn:aws:s3:eu-central-1:123456789012:bucketName
    source_account: 123456789012
  register: lambda_policy_action

- name: show results
  ansible.builtin.debug:
    var: lambda_policy_action
```

## [Return Values](lambda_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **lambda_policy_action**  string | describes what action was taken  **Returned:** success |

### Authors

- Pierre Jodouin (@pjodouin)
- Michael De La Rue (@mikedlr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
