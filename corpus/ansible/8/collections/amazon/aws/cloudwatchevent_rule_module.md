---
collection: ansible
version: "8"
title: "amazon.aws.cloudwatchevent_rule module – Manage CloudWatch Event rules and targets"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/cloudwatchevent_rule_module.html
fetched_at: 2026-07-28T01:06:18+00:00
---
# amazon.aws.cloudwatchevent_rule module – Manage CloudWatch Event rules and targets

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
> see [Requirements](cloudwatchevent_rule_module.md#ansible-collections-amazon-aws-cloudwatchevent-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.cloudwatchevent_rule`.

New in amazon.aws 5.0.0

- [Synopsis](cloudwatchevent_rule_module.md#synopsis)
- [Requirements](cloudwatchevent_rule_module.md#requirements)
- [Parameters](cloudwatchevent_rule_module.md#parameters)
- [Notes](cloudwatchevent_rule_module.md#notes)
- [Examples](cloudwatchevent_rule_module.md#examples)
- [Return Values](cloudwatchevent_rule_module.md#return-values)

## [Synopsis](cloudwatchevent_rule_module.md#id1)

- This module creates and manages CloudWatch event rules and targets.
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](cloudwatchevent_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](cloudwatchevent_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | A description of the rule. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **event_pattern**  json | A string pattern that is used to match against incoming events to determine if the rule should be triggered. |
| **name**  string / required | The name of the rule you are creating, updating or deleting. No spaces or special characters allowed (i.e. must match `[\.\-_A-Za-z0-9]+`). |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **role_arn**  string | The Amazon Resource Name (ARN) of the IAM role associated with the rule. |
| **schedule_expression**  string | A cron or rate expression that defines the schedule the rule will trigger on. For example, `cron(0 20 * * ? *`), `rate(5 minutes`). |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Whether the rule is present (and enabled), disabled, or absent.  **Choices:**   - `"present"` ← (default) - `"disabled"` - `"absent"` |
| **targets**  list / elements=dictionary | A list of targets to add to or update for the rule.  **Default:** `[]` |
| **arn**  string / required | The ARN associated with the target. |
| **ecs_parameters**  dictionary | Contains the ECS task definition and task count to be used, if the event target is an ECS task. |
| **task_count**  integer | The number of tasks to create based on *task_definition*. |
| **task_definition_arn**  string / required | The full ARN of the task definition. |
| **id**  string / required | The unique target assignment ID. |
| **input**  json | A JSON object that will override the event data passed to the target.  If neither *input* nor *input_path* nor *input_transformer* is specified, then the entire event is passed to the target in JSON form. |
| **input_path**  string | A JSONPath string (e.g. `$.detail`) that specifies the part of the event data to be passed to the target.  If neither *input* nor *input_path* nor *input_transformer* is specified, then the entire event is passed to the target in JSON form. |
| **input_transformer**  dictionary  *added in community.aws 4.1.0* | Settings to support providing custom input to a target based on certain event data. |
| **input_paths_map**  dictionary | A dict that specifies the transformation of the event data to custom input parameters. |
| **input_template**  json | A string that templates the values input_paths_map extracted from the event data. It is used to produce the output you want to be sent to the target. |
| **role_arn**  string | The ARN of the IAM role to be used for this target when the rule is triggered. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cloudwatchevent_rule_module.md#id4)

> **Note:**
>
> - A rule must contain at least an *event_pattern* or *schedule_expression*. A rule can have both an *event_pattern* and a *schedule_expression*, in which case the rule will trigger on matching events as well as on a schedule.
> - When specifying targets, *input*, *input_path*, *input_paths_map* and *input_template* are mutually-exclusive and optional parameters.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](cloudwatchevent_rule_module.md#id5)

```yaml+jinja
- amazon.aws.cloudwatchevent_rule:
    name: MyCronTask
    schedule_expression: "cron(0 20 * * ? *)"
    description: Run my scheduled task
    targets:
      - id: MyTargetId
        arn: arn:aws:lambda:us-east-1:123456789012:function:MyFunction

- amazon.aws.cloudwatchevent_rule:
    name: MyDisabledCronTask
    schedule_expression: "rate(5 minutes)"
    description: Run my disabled scheduled task
    state: disabled
    targets:
      - id: MyOtherTargetId
        arn: arn:aws:lambda:us-east-1:123456789012:function:MyFunction
        input: '{"foo": "bar"}'

- amazon.aws.cloudwatchevent_rule:
    name: MyInstanceLaunchEvent
    description: "Rule for EC2 instance launch"
    state: present
    event_pattern: '{"source":["aws.ec2"],"detail-type":["EC2 Instance State-change Notification"],"detail":{"state":["pending"]}}'
    targets:
      - id: MyTargetSnsTopic
        arn: arn:aws:sns:us-east-1:123456789012:MySNSTopic
        input_transformer:
          input_paths_map:
            instance: "$.detail.instance-id"
            state: "$.detail.state"
          input_template: "<instance> is in state <state>"

- amazon.aws.cloudwatchevent_rule:
    name: MyCronTask
    state: absent
```

## [Return Values](cloudwatchevent_rule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **rule**  dictionary | CloudWatch Event rule data.  **Returned:** success  **Sample:** `{"arn": "arn:aws:events:us-east-1:123456789012:rule/MyCronTask", "description": "Run my scheduled task", "name": "MyCronTask", "schedule_expression": "cron(0 20 * * ? *)", "state": "ENABLED"}` |
| **targets**  list / elements=string | CloudWatch Event target(s) assigned to the rule.  **Returned:** success  **Sample:** `["[{ 'arn': 'arn:aws:lambda:us-east-1:123456789012:function:MyFunction'", " 'id': 'MyTargetId' }]"]` |

### Authors

- Jim Dalton (@jsdalton)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
