---
collection: ansible
version: "6"
title: "community.aws.cloudwatchevent_rule module – Manage CloudWatch Event rules and targets"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/cloudwatchevent_rule_module.html
fetched_at: 2026-07-27T17:03:46+00:00
---
# community.aws.cloudwatchevent_rule module – Manage CloudWatch Event rules and targets

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
> see [Requirements](cloudwatchevent_rule_module.md#ansible-collections-community-aws-cloudwatchevent-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.cloudwatchevent_rule`.

New in community.aws 1.0.0

- [Synopsis](cloudwatchevent_rule_module.md#synopsis)
- [Requirements](cloudwatchevent_rule_module.md#requirements)
- [Parameters](cloudwatchevent_rule_module.md#parameters)
- [Notes](cloudwatchevent_rule_module.md#notes)
- [Examples](cloudwatchevent_rule_module.md#examples)
- [Return Values](cloudwatchevent_rule_module.md#return-values)

## [Synopsis](cloudwatchevent_rule_module.md#id1)

- This module creates and manages CloudWatch event rules and targets.

## [Requirements](cloudwatchevent_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](cloudwatchevent_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **description**  string | A description of the rule. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **event_pattern**  string | A string pattern (in valid JSON format) that is used to match against incoming events to determine if the rule should be triggered. |
| **name**  string / required | The name of the rule you are creating, updating or deleting. No spaces or special characters allowed (i.e. must match `[\.\-_A-Za-z0-9]+`). |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **role_arn**  string | The Amazon Resource Name (ARN) of the IAM role associated with the rule. |
| **schedule_expression**  string | A cron or rate expression that defines the schedule the rule will trigger on. For example, `cron(0 20 * * ? *`), `rate(5 minutes`). |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Whether the rule is present (and enabled), disabled, or absent.  Choices:   - `"present"` ← (default) - `"disabled"` - `"absent"` |
| **targets**  list / elements=dictionary | A list of targets to add to or update for the rule. |
| **arn**  string / required | The ARN associated with the target. |
| **ecs_parameters**  dictionary | Contains the ECS task definition and task count to be used, if the event target is an ECS task. |
| **task_count**  integer | The number of tasks to create based on *task_definition*. |
| **task_definition_arn**  string | The full ARN of the task definition. |
| **id**  string / required | The unique target assignment ID. |
| **input**  string | A JSON object that will override the event data when passed to the target.  If neither *input* nor *input_path* is specified, then the entire event is passed to the target in JSON form. |
| **input_path**  string | A JSONPath string (e.g. `$.detail`) that specifies the part of the event data to be passed to the target.  If neither *input* nor *input_path* is specified, then the entire event is passed to the target in JSON form. |
| **role_arn**  string | The ARN of the IAM role to be used for this target when the rule is triggered. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](cloudwatchevent_rule_module.md#id4)

> **Note:**
>
> - A rule must contain at least an *event_pattern* or *schedule_expression*. A rule can have both an *event_pattern* and a *schedule_expression*, in which case the rule will trigger on matching events as well as on a schedule.
> - When specifying targets, *input* and *input_path* are mutually-exclusive and optional parameters.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](cloudwatchevent_rule_module.md#id5)

```yaml+jinja
- community.aws.cloudwatchevent_rule:
    name: MyCronTask
    schedule_expression: "cron(0 20 * * ? *)"
    description: Run my scheduled task
    targets:
      - id: MyTargetId
        arn: arn:aws:lambda:us-east-1:123456789012:function:MyFunction

- community.aws.cloudwatchevent_rule:
    name: MyDisabledCronTask
    schedule_expression: "rate(5 minutes)"
    description: Run my disabled scheduled task
    state: disabled
    targets:
      - id: MyOtherTargetId
        arn: arn:aws:lambda:us-east-1:123456789012:function:MyFunction
        input: '{"foo": "bar"}'

- community.aws.cloudwatchevent_rule:
    name: MyCronTask
    state: absent
```

## [Return Values](cloudwatchevent_rule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **rule**  dictionary | CloudWatch Event rule data.  Returned: success  Sample: `{"arn": "arn:aws:events:us-east-1:123456789012:rule/MyCronTask", "description": "Run my scheduled task", "name": "MyCronTask", "schedule_expression": "cron(0 20 * * ? *)", "state": "ENABLED"}` |
| **targets**  list / elements=string | CloudWatch Event target(s) assigned to the rule.  Returned: success  Sample: `["[{ 'arn': 'arn:aws:lambda:us-east-1:123456789012:function:MyFunction'", " 'id': 'MyTargetId' }]"]` |

### Authors

- Jim Dalton (@jsdalton)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
