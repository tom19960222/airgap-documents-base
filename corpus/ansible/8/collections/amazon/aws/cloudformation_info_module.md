---
collection: ansible
version: "8"
title: "amazon.aws.cloudformation_info module – Obtain information about an AWS CloudFormation stack"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/cloudformation_info_module.html
fetched_at: 2026-07-28T01:06:14+00:00
---
# amazon.aws.cloudformation_info module – Obtain information about an AWS CloudFormation stack

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
> see [Requirements](cloudformation_info_module.md#ansible-collections-amazon-aws-cloudformation-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.cloudformation_info`.

New in amazon.aws 1.0.0

- [Synopsis](cloudformation_info_module.md#synopsis)
- [Requirements](cloudformation_info_module.md#requirements)
- [Parameters](cloudformation_info_module.md#parameters)
- [Notes](cloudformation_info_module.md#notes)
- [Examples](cloudformation_info_module.md#examples)
- [Return Values](cloudformation_info_module.md#return-values)

## [Synopsis](cloudformation_info_module.md#id1)

- Gets information about an AWS CloudFormation stack.

## [Requirements](cloudformation_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](cloudformation_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **all_facts**  boolean | Get all stack information for the stack.  **Choices:**   - `false` ← (default) - `true` |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **stack_change_sets**  boolean | Get stack change sets for the stack  **Choices:**   - `false` ← (default) - `true` |
| **stack_events**  boolean | Get stack events for the stack.  **Choices:**   - `false` ← (default) - `true` |
| **stack_name**  string | The name or id of the CloudFormation stack. Gathers information on all stacks by default. |
| **stack_policy**  boolean | Get stack policy for the stack.  **Choices:**   - `false` ← (default) - `true` |
| **stack_resources**  boolean | Get stack resources for the stack.  **Choices:**   - `false` ← (default) - `true` |
| **stack_template**  boolean | Get stack template body for the stack.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cloudformation_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](cloudformation_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Get information on all stacks
  amazon.aws.cloudformation_info:
  register: all_stacks_output

- name: Get summary information about a stack
  amazon.aws.cloudformation_info:
    stack_name: my-cloudformation-stack
  register: output

- debug:
    msg: "{{ output['cloudformation']['my-cloudformation-stack'] }}"

# Get stack outputs, when you have the stack name available as a fact
- set_fact:
    stack_name: my-awesome-stack

- amazon.aws.cloudformation_info:
    stack_name: "{{ stack_name }}"
  register: my_stack

- debug:
    msg: "{{ my_stack.cloudformation[stack_name].stack_outputs }}"

# Get all stack information about a stack
- amazon.aws.cloudformation_info:
    stack_name: my-cloudformation-stack
    all_facts: true

# Get stack resource and stack policy information about a stack
- amazon.aws.cloudformation_info:
    stack_name: my-cloudformation-stack
    stack_resources: true
    stack_policy: true

# Fail if the stack doesn't exist
- name: try to get info about a stack but fail if it doesn't exist
  amazon.aws.cloudformation_info:
    stack_name: nonexistent-stack
    all_facts: true
  failed_when: cloudformation['nonexistent-stack'] is undefined
```

## [Return Values](cloudformation_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cloudformation**  dictionary | Dictionary of dictionaries containing info of stack(s).  Keys are *stack_name*s.  **Returned:** always |
| **stack_change_sets**  list / elements=string | A list of stack change sets. Each item in the list represents the details of a specific changeset.  **Returned:** only if all_facts or stack_change_sets is true and the stack exists |
| **stack_description**  dictionary | Summary facts about the stack.  **Returned:** if the stack exists |
| **capabilities**  list / elements=string | The capabilities allowed in the stack.  **Returned:** always |
| **creation_time**  string | The time at which the stack was created.  **Returned:** if stack exists |
| **deletion_time**  string | The time at which the stack was deleted.  **Returned:** if stack was deleted |
| **description**  string | The user-defined description associated with the stack.  **Returned:** always |
| **disable_rollback**  boolean | Whether or not rollback on stack creation failures is enabled.  **Returned:** always |
| **drift_information**  dictionary | Information about whether a stack’s actual configuration differs, or has drifted, from it’s expected configuration, as defined in the stack template and any values specified as template parameters.  **Returned:** always |
| **last_check_timestamp**  string | Most recent time when a drift detection operation was initiated on the stack, or any of its individual resources that support drift detection.  **Returned:** if a drift was detected |
| **stack_drift_status**  string | Status of the stack’s actual configuration compared to its expected template configuration.  **Returned:** always |
| **enable_termination_protection**  boolean | Whether termination protection is enabled for the stack.  **Returned:** always |
| **notification_arns**  list / elements=string | Amazon SNS topic ARNs to which stack related events are published.  **Returned:** always |
| **outputs**  list / elements=dictionary | A list of output dicts.  **Returned:** always |
| **output_key**  string | The key associated with the output.  **Returned:** always |
| **output_value**  string | The value associated with the output.  **Returned:** always |
| **parameters**  list / elements=dictionary | A list of parameter dicts.  **Returned:** always |
| **parameter_key**  string | The key associated with the parameter.  **Returned:** always |
| **parameter_value**  string | The value associated with the parameter.  **Returned:** always |
| **rollback_configuration**  dictionary | The rollback triggers for CloudFormation to monitor during stack creation and updating operations.  **Returned:** always |
| **rollback_triggers**  list / elements=dictionary | The triggers to monitor during stack creation or update actions.  **Returned:** when rollback triggers exist |
| **arn**  string | The ARN of the rollback trigger.  **Returned:** always |
| **type**  string | The resource type of the rollback trigger.  **Returned:** always |
| **stack_id**  string | The unique ID of the stack.  **Returned:** always |
| **stack_name**  string | The name of the stack.  **Returned:** always |
| **stack_status**  string | The status of the stack.  **Returned:** always |
| **tags**  list / elements=dictionary | A list of tags associated with the stack.  **Returned:** always |
| **key**  string | Key of tag.  **Returned:** always |
| **value**  string | Value of tag.  **Returned:** always |
| **stack_events**  list / elements=string | All stack events for the stack.  **Returned:** only if all_facts or stack_events is true and the stack exists |
| **stack_outputs**  dictionary | Dictionary of stack outputs keyed by the value of each output ‘OutputKey’ parameter and corresponding value of each output ‘OutputValue’ parameter.  **Returned:** if the stack exists  **Sample:** `{"ApplicationDatabaseName": "dazvlpr01xj55a.ap-southeast-2.rds.amazonaws.com"}` |
| **stack_parameters**  dictionary | Dictionary of stack parameters keyed by the value of each parameter ‘ParameterKey’ parameter and corresponding value of each parameter ‘ParameterValue’ parameter.  **Returned:** if the stack exists  **Sample:** `{"DatabaseEngine": "mysql", "DatabasePassword": "***"}` |
| **stack_policy**  dictionary | Describes the stack policy for the stack.  **Returned:** only if all_facts or stack_policy is true and the stack exists |
| **stack_resource_list**  list / elements=string | Describes stack resources for the stack.  **Returned:** only if all_facts or stack_resources is true and the stack exists |
| **stack_resources**  dictionary | Dictionary of stack resources keyed by the value of each resource ‘LogicalResourceId’ parameter and corresponding value of each resource ‘PhysicalResourceId’ parameter.  **Returned:** only if all_facts or stack_resources is true and the stack exists  **Sample:** `{"ApplicationDatabase": "dazvlpr01xj55a", "AutoScalingGroup": "dev-someapp-AutoscalingGroup-1SKEXXBCAN0S7", "AutoScalingSecurityGroup": "sg-abcd1234"}` |
| **stack_tags**  dictionary | Dictionary of key value pairs of tags.  **Returned:** only if all_facts or stack_resources is true and the stack exists  **Sample:** `{"TagOne": "ValueOne", "TagTwo": "ValueTwo"}` |
| **stack_template**  dictionary | Describes the stack template for the stack.  **Returned:** only if all_facts or stack_template is true and the stack exists |

### Authors

- Justin Menga (@jmenga)
- Kevin Coming (@waffie1)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
