---
collection: ansible
version: "6"
title: "community.aws.aws_step_functions_state_machine_execution module – Start or stop execution of an AWS Step Functions state machine."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_step_functions_state_machine_execution_module.html
fetched_at: 2026-07-27T17:03:37+00:00
---
# community.aws.aws_step_functions_state_machine_execution module – Start or stop execution of an AWS Step Functions state machine.

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
> see [Requirements](aws_step_functions_state_machine_execution_module.md#ansible-collections-community-aws-aws-step-functions-state-machine-execution-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_step_functions_state_machine_execution`.

New in community.aws 1.0.0

- [Synopsis](aws_step_functions_state_machine_execution_module.md#synopsis)
- [Requirements](aws_step_functions_state_machine_execution_module.md#requirements)
- [Parameters](aws_step_functions_state_machine_execution_module.md#parameters)
- [Notes](aws_step_functions_state_machine_execution_module.md#notes)
- [Examples](aws_step_functions_state_machine_execution_module.md#examples)
- [Return Values](aws_step_functions_state_machine_execution_module.md#return-values)

## [Synopsis](aws_step_functions_state_machine_execution_module.md#id1)

- Start or stop execution of a state machine in AWS Step Functions.

## [Requirements](aws_step_functions_state_machine_execution_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_step_functions_state_machine_execution_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **action**  string | Desired action (start or stop) for a state machine execution.  Choices:   - `"start"` ← (default) - `"stop"` |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **cause**  string | A detailed explanation of the cause for stopping the execution.  Default: `""` |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **error**  string | The error code of the failure to pass in when stopping the execution.  Default: `""` |
| **execution_arn**  string | The ARN of the execution you wish to stop. |
| **execution_input**  json | The JSON input data for the execution.  Default: `"{}"` |
| **name**  string | Name of the execution. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state_machine_arn**  string | The ARN of the state machine that will be executed. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](aws_step_functions_state_machine_execution_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_step_functions_state_machine_execution_module.md#id5)

```yaml+jinja
- name: Start an execution of a state machine
  community.aws.aws_step_functions_state_machine_execution:
    name: an_execution_name
    execution_input: '{ "IsHelloWorldExample": true }'
    state_machine_arn: "arn:aws:states:us-west-2:682285639423:stateMachine:HelloWorldStateMachine"

- name: Stop an execution of a state machine
  community.aws.aws_step_functions_state_machine_execution:
    action: stop
    execution_arn: "arn:aws:states:us-west-2:682285639423:execution:HelloWorldStateMachineCopy:a1e8e2b5-5dfe-d40e-d9e3-6201061047c8"
    cause: "cause of task failure"
    error: "error code of the failure"
```

## [Return Values](aws_step_functions_state_machine_execution_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **execution_arn**  string | ARN of the AWS Step Functions state machine execution.  Returned: if action == start and changed == True  Sample: `"arn:aws:states:us-west-2:682285639423:execution:HelloWorldStateMachineCopy:a1e8e2b5-5dfe-d40e-d9e3-6201061047c8"` |
| **start_date**  string | The date the execution is started.  Returned: if action == start and changed == True  Sample: `"2019-11-02T22:39:49.071000-07:00"` |
| **stop_date**  string | The date the execution is stopped.  Returned: if action == stop  Sample: `"2019-11-02T22:39:49.071000-07:00"` |

### Authors

- Prasad Katti (@prasadkatti)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
