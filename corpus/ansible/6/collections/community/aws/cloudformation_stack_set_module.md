---
collection: ansible
version: "6"
title: "community.aws.cloudformation_stack_set module – Manage groups of CloudFormation stacks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/cloudformation_stack_set_module.html
fetched_at: 2026-07-27T17:03:41+00:00
---
# community.aws.cloudformation_stack_set module – Manage groups of CloudFormation stacks

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
> see [Requirements](cloudformation_stack_set_module.md#ansible-collections-community-aws-cloudformation-stack-set-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.cloudformation_stack_set`.

New in community.aws 1.0.0

- [Synopsis](cloudformation_stack_set_module.md#synopsis)
- [Requirements](cloudformation_stack_set_module.md#requirements)
- [Parameters](cloudformation_stack_set_module.md#parameters)
- [Notes](cloudformation_stack_set_module.md#notes)
- [Examples](cloudformation_stack_set_module.md#examples)
- [Return Values](cloudformation_stack_set_module.md#return-values)

## [Synopsis](cloudformation_stack_set_module.md#id1)

- Launches/updates/deletes AWS CloudFormation Stack Sets.

## [Requirements](cloudformation_stack_set_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](cloudformation_stack_set_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accounts**  list / elements=string | A list of AWS accounts in which to create instance of CloudFormation stacks.  At least one region must be specified to create a stack set. On updates, if fewer regions are specified only the specified regions will have their stack instances updated. |
| **administration_role_arn**  aliases: admin_role_arn, admin_role, administration_role  string | ARN of the administration role, meaning the role that CloudFormation Stack Sets use to assume the roles in your child accounts.  This defaults to `arn:aws:iam::{{ account ID }}:role/AWSCloudFormationStackSetAdministrationRole` where `{{ account ID }}` is replaced with the account number of the current IAM role/user/STS credentials. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **capabilities**  list / elements=string | Capabilities allow stacks to create and modify IAM resources, which may include adding users or roles.  Currently the only available values are ‘CAPABILITY_IAM’ and ‘CAPABILITY_NAMED_IAM’. Either or both may be provided.  The following resources require that one or both of these parameters is specified: AWS::IAM::AccessKey, AWS::IAM::Group, AWS::IAM::InstanceProfile, AWS::IAM::Policy, AWS::IAM::Role, AWS::IAM::User, AWS::IAM::UserToGroupAddition  Choices:   - `"CAPABILITY_IAM"` - `"CAPABILITY_NAMED_IAM"` |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **description**  string | A description of what this stack set creates. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **execution_role_name**  aliases: exec_role_name, exec_role, execution_role  string | ARN of the execution role, meaning the role that CloudFormation Stack Sets assumes in your child accounts.  This MUST NOT be an ARN, and the roles must exist in each child account specified.  The default name for the execution role is `AWSCloudFormationStackSetExecutionRole` |
| **failure_tolerance**  dictionary | Settings to change what is considered “failed” when running stack instance updates, and how many to do at a time. |
| **fail_count**  integer | The number of accounts, per region, for which this operation can fail before CloudFormation stops the operation in that region.  You must specify one of *fail_count* and *fail_percentage*. |
| **fail_percentage**  integer | The percentage of accounts, per region, for which this stack operation can fail before CloudFormation stops the operation in that region.  You must specify one of *fail_count* and *fail_percentage*. |
| **parallel_count**  integer | The maximum number of accounts in which to perform this operation at one time.  *parallel_count* may be at most one more than the *fail_count*.  You must specify one of *parallel_count* and *parallel_percentage*.  Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual count may be lower. |
| **parallel_percentage**  integer | The maximum percentage of accounts in which to perform this operation at one time.  You must specify one of *parallel_count* and *parallel_percentage*.  Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual percentage may be lower. |
| **name**  string / required | Name of the CloudFormation stack set. |
| **parameters**  dictionary | A list of hashes of all the template variables for the stack. The value can be a string or a dict.  Dict can be used to set additional template parameter attributes like UsePreviousValue (see example).  Default: `{}` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_stacks**  boolean | Only applicable when *state=absent*. Sets whether, when deleting a stack set, the stack instances should also be deleted.  By default, instances will be deleted. To keep stacks when stack set is deleted set *purge_stacks=false*.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **regions**  list / elements=string | A list of AWS regions to create instances of a stack in. The *region* parameter chooses where the Stack Set is created, and *regions* specifies the region for stack instances.  At least one region must be specified to create a stack set. On updates, if fewer regions are specified only the specified regions will have their stack instances updated. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | If *state=present*, stack will be created. If *state=present* and if stack exists and template has changed, it will be updated. If *state=absent*, stack will be removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Dictionary of tags to associate with stack and its resources during stack creation.  Can be updated later, updating tags removes previous entries. |
| **template**  path | The local path of the CloudFormation template.  This must be the full path to the file, relative to the working directory. If using roles this may look like `roles/cloudformation/files/cloudformation-example.json`.  If *state=present* and the stack does not exist yet, either *template*, *template_body* or *template_url* must be specified (but only one of them).  If *state=present*, the stack does exist, and neither *template*, *template_body* nor *template_url* are specified, the previous template will be reused. |
| **template_body**  string | Template body. Use this to pass in the actual body of the CloudFormation template.  If *state=present* and the stack does not exist yet, either *template*, *template_body* or *template_url* must be specified (but only one of them).  If *state=present*, the stack does exist, and neither *template*, *template_body* nor *template_url* are specified, the previous template will be reused. |
| **template_url**  string | Location of file containing the template body.  The URL must point to a template (max size 307,200 bytes) located in an S3 bucket in the same region as the stack.  If *state=present* and the stack does not exist yet, either *template*, *template_body* or *template_url* must be specified (but only one of them).  If *state=present*, the stack does exist, and neither *template*, *template_body* nor *template_url* are specified, the previous template will be reused. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **wait**  boolean | Whether or not to wait for stack operation to complete. This includes waiting for stack instances to reach UPDATE_COMPLETE status.  If you choose not to wait, this module will not notify when stack operations fail because it will not wait for them to finish.  Choices:   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How long to wait (in seconds) for stacks to complete create/update/delete operations.  Default: `900` |

## [Notes](cloudformation_stack_set_module.md#id4)

> **Note:**
>
> - To make an individual stack, you want the [amazon.aws.cloudformation](../../amazon/aws/cloudformation_module.md#ansible-collections-amazon-aws-cloudformation-module) module.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](cloudformation_stack_set_module.md#id5)

```yaml+jinja
- name: Create a stack set with instances in two accounts
  community.aws.cloudformation_stack_set:
    name: my-stack
    description: Test stack in two accounts
    state: present
    template_url: https://s3.amazonaws.com/my-bucket/cloudformation.template
    accounts: [1234567890, 2345678901]
    regions:
    - us-east-1

- name: on subsequent calls, templates are optional but parameters and tags can be altered
  community.aws.cloudformation_stack_set:
    name: my-stack
    state: present
    parameters:
      InstanceName: my_stacked_instance
    tags:
      foo: bar
      test: stack
    accounts: [1234567890, 2345678901]
    regions:
    - us-east-1

- name: The same type of update, but wait for the update to complete in all stacks
  community.aws.cloudformation_stack_set:
    name: my-stack
    state: present
    wait: true
    parameters:
      InstanceName: my_restacked_instance
    tags:
      foo: bar
      test: stack
    accounts: [1234567890, 2345678901]
    regions:
    - us-east-1
```

## [Return Values](cloudformation_stack_set_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **operations**  list / elements=string | All operations initiated by this run of the cloudformation_stack_set module  Returned: always  Sample: `[{"action": "CREATE", "administration_role_arn": "arn:aws:iam::1234567890:role/AWSCloudFormationStackSetAdministrationRole", "creation_timestamp": "2018-06-18T17:40:46.372000+00:00", "end_timestamp": "2018-06-18T17:41:24.560000+00:00", "execution_role_name": "AWSCloudFormationStackSetExecutionRole", "operation_id": "Ansible-StackInstance-Create-0ff2af5b-251d-4fdb-8b89-1ee444eba8b8", "operation_preferences": {"region_order": ["us-east-1", "us-east-2"]}, "stack_set_id": "TestStackPrime:19f3f684-aae9-4e67-ba36-e09f92cf5929", "status": "FAILED"}]` |
| **operations_log**  list / elements=string | Most recent events in CloudFormation’s event log. This may be from a previous run in some cases.  Returned: always  Sample: `[{"action": "CREATE", "creation_timestamp": "2018-06-18T17:40:46.372000+00:00", "end_timestamp": "2018-06-18T17:41:24.560000+00:00", "operation_id": "Ansible-StackInstance-Create-0ff2af5b-251d-4fdb-8b89-1ee444eba8b8", "stack_instances": [{"account": "1234567890", "region": "us-east-1", "stack_set_id": "TestStackPrime:19f3f684-aae9-4e67-ba36-e09f92cf5929", "status": "OUTDATED", "status_reason": "Account 1234567890 should have 'AWSCloudFormationStackSetAdministrationRole' role with trust relationship to CloudFormation service."}], "status": "FAILED"}]` |
| **stack_instances**  list / elements=string | CloudFormation stack instances that are members of this stack set. This will also include their region and account ID.  Returned: state == present  Sample: `[{"account": "1234567890", "region": "us-east-1", "stack_set_id": "TestStackPrime:19f3f684-aae9-4e67-ba36-e09f92cf5929", "status": "OUTDATED", "status_reason": "Account 1234567890 should have 'AWSCloudFormationStackSetAdministrationRole' role with trust relationship to CloudFormation service.\n"}, {"account": "1234567890", "region": "us-east-2", "stack_set_id": "TestStackPrime:19f3f684-aae9-4e67-ba36-e09f92cf5929", "status": "OUTDATED", "status_reason": "Cancelled since failure tolerance has exceeded"}]` |
| **stack_set**  dictionary | Facts about the currently deployed stack set, its parameters, and its tags  Returned: state == present  Sample: `{"administration_role_arn": "arn:aws:iam::1234567890:role/AWSCloudFormationStackSetAdministrationRole", "capabilities": [], "description": "test stack PRIME", "execution_role_name": "AWSCloudFormationStackSetExecutionRole", "parameters": [], "stack_set_arn": "arn:aws:cloudformation:us-east-1:1234567890:stackset/TestStackPrime:19f3f684-aae9-467-ba36-e09f92cf5929", "stack_set_id": "TestStackPrime:19f3f684-aae9-4e67-ba36-e09f92cf5929", "stack_set_name": "TestStackPrime", "status": "ACTIVE", "tags": {"Some": "Thing", "an": "other"}, "template_body": "AWSTemplateFormatVersion: \"2010-09-09\"\nParameters: {}\nResources:\n  Bukkit:\n    Type: \"AWS::S3::Bucket\"\n    Properties: {}\n  other:\n    Type: \"AWS::SNS::Topic\"\n    Properties: {}\n"}` |

### Authors

- Ryan Scott Brown (@ryansb)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
