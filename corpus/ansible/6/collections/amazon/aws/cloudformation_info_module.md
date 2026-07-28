---
collection: ansible
version: "6"
title: "amazon.aws.cloudformation_info module – Obtain information about an AWS CloudFormation stack"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/cloudformation_info_module.html
fetched_at: 2026-07-27T16:43:40+00:00
---
# amazon.aws.cloudformation_info module – Obtain information about an AWS CloudFormation stack

> **Note:**
>
> This module is part of the [amazon.aws collection](https://galaxy.ansible.com/amazon/aws) (version 3.5.0).
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
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](cloudformation_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **all_facts**  boolean | Get all stack information for the stack.  Choices:   - `false` ← (default) - `true` |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **stack_change_sets**  boolean | Get stack change sets for the stack  Choices:   - `false` ← (default) - `true` |
| **stack_events**  boolean | Get stack events for the stack.  Choices:   - `false` ← (default) - `true` |
| **stack_name**  string | The name or id of the CloudFormation stack. Gathers information on all stacks by default. |
| **stack_policy**  boolean | Get stack policy for the stack.  Choices:   - `false` ← (default) - `true` |
| **stack_resources**  boolean | Get stack resources for the stack.  Choices:   - `false` ← (default) - `true` |
| **stack_template**  boolean | Get stack template body for the stack.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](cloudformation_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](cloudformation_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

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
    all_facts: yes
  failed_when: cloudformation['nonexistent-stack'] is undefined
```

## [Return Values](cloudformation_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **stack_change_sets**  list / elements=string | A list of stack change sets. Each item in the list represents the details of a specific changeset  Returned: only if all_facts or stack_change_sets is true and the stack exists |
| **stack_description**  dictionary | Summary facts about the stack  Returned: if the stack exists |
| **stack_events**  list / elements=string | All stack events for the stack  Returned: only if all_facts or stack_events is true and the stack exists |
| **stack_outputs**  dictionary | Dictionary of stack outputs keyed by the value of each output ‘OutputKey’ parameter and corresponding value of each output ‘OutputValue’ parameter  Returned: if the stack exists  Sample: `{"ApplicationDatabaseName": "dazvlpr01xj55a.ap-southeast-2.rds.amazonaws.com"}` |
| **stack_parameters**  dictionary | Dictionary of stack parameters keyed by the value of each parameter ‘ParameterKey’ parameter and corresponding value of each parameter ‘ParameterValue’ parameter  Returned: if the stack exists  Sample: `{"DatabaseEngine": "mysql", "DatabasePassword": "***"}` |
| **stack_policy**  dictionary | Describes the stack policy for the stack  Returned: only if all_facts or stack_policy is true and the stack exists |
| **stack_resource_list**  list / elements=string | Describes stack resources for the stack  Returned: only if all_facts or stack_resources is true and the stack exists |
| **stack_resources**  dictionary | Dictionary of stack resources keyed by the value of each resource ‘LogicalResourceId’ parameter and corresponding value of each resource ‘PhysicalResourceId’ parameter  Returned: only if all_facts or stack_resources is true and the stack exists  Sample: `{"ApplicationDatabase": "dazvlpr01xj55a", "AutoScalingGroup": "dev-someapp-AutoscalingGroup-1SKEXXBCAN0S7", "AutoScalingSecurityGroup": "sg-abcd1234"}` |
| **stack_template**  dictionary | Describes the stack template for the stack  Returned: only if all_facts or stack_template is true and the stack exists |

### Authors

- Justin Menga (@jmenga)
- Kevin Coming (@waffie1)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
