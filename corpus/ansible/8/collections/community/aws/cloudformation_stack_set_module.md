---
collection: ansible
version: "8"
title: "community.aws.cloudformation_stack_set module – Manage groups of CloudFormation stacks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/cloudformation_stack_set_module.html
fetched_at: 2026-07-28T01:40:19+00:00
---
# community.aws.cloudformation_stack_set module – Manage groups of CloudFormation stacks

> **Note:**
>
> This module is part of the [community.aws collection](https://galaxy.ansible.com/ui/repo/published/community/aws/) (version 6.4.0).
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
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](cloudformation_stack_set_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **accounts**  list / elements=string | A list of AWS accounts in which to create instance of CloudFormation stacks.  At least one region must be specified to create a stack set. On updates, if fewer regions are specified only the specified regions will have their stack instances updated. |
| **administration_role_arn**  aliases: admin_role_arn, admin_role, administration_role  string | ARN of the administration role, meaning the role that CloudFormation Stack Sets use to assume the roles in your child accounts.  This defaults to `arn:aws:iam::{{ account ID }}:role/AWSCloudFormationStackSetAdministrationRole` where `{{ account ID }}` is replaced with the account number of the current IAM role/user/STS credentials. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **capabilities**  list / elements=string | Capabilities allow stacks to create and modify IAM resources, which may include adding users or roles.  Currently the only available values are ‘CAPABILITY_IAM’ and ‘CAPABILITY_NAMED_IAM’. Either or both may be provided.  The following resources require that one or both of these parameters is specified: AWS::IAM::AccessKey, AWS::IAM::Group, AWS::IAM::InstanceProfile, AWS::IAM::Policy, AWS::IAM::Role, AWS::IAM::User, AWS::IAM::UserToGroupAddition  **Choices:**   - `"CAPABILITY_IAM"` - `"CAPABILITY_NAMED_IAM"` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | A description of what this stack set creates. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **execution_role_name**  aliases: exec_role_name, exec_role, execution_role  string | ARN of the execution role, meaning the role that CloudFormation Stack Sets assumes in your child accounts.  This MUST NOT be an ARN, and the roles must exist in each child account specified.  The default name for the execution role is `AWSCloudFormationStackSetExecutionRole` |
| **failure_tolerance**  dictionary | Settings to change what is considered “failed” when running stack instance updates, and how many to do at a time.  **Default:** `{}` |
| **fail_count**  integer | The number of accounts, per region, for which this operation can fail before CloudFormation stops the operation in that region.  You must specify one of *fail_count* and *fail_percentage*. |
| **fail_percentage**  integer | The percentage of accounts, per region, for which this stack operation can fail before CloudFormation stops the operation in that region.  You must specify one of *fail_count* and *fail_percentage*. |
| **parallel_count**  integer | The maximum number of accounts in which to perform this operation at one time.  *parallel_count* may be at most one more than the *fail_count*.  You must specify one of *parallel_count* and *parallel_percentage*.  Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual count may be lower. |
| **parallel_percentage**  integer | The maximum percentage of accounts in which to perform this operation at one time.  You must specify one of *parallel_count* and *parallel_percentage*.  Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual percentage may be lower. |
| **name**  string / required | Name of the CloudFormation stack set. |
| **parameters**  dictionary | A list of hashes of all the template variables for the stack. The value can be a string or a dict.  Dict can be used to set additional template parameter attributes like UsePreviousValue (see example).  **Default:** `{}` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_stacks**  boolean | Only applicable when *state=absent*. Sets whether, when deleting a stack set, the stack instances should also be deleted.  By default, instances will be deleted. To keep stacks when stack set is deleted set *purge_stacks=false*.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **regions**  list / elements=string | A list of AWS regions to create instances of a stack in. The *region* parameter chooses where the Stack Set is created, and *regions* specifies the region for stack instances.  At least one region must be specified to create a stack set. On updates, if fewer regions are specified only the specified regions will have their stack instances updated. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | If *state=present*, stack will be created. If *state=present* and if stack exists and template has changed, it will be updated. If *state=absent*, stack will be removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Dictionary of tags to associate with stack and its resources during stack creation.  Can be updated later, updating tags removes previous entries. |
| **template**  path | The local path of the CloudFormation template.  This must be the full path to the file, relative to the working directory. If using roles this may look like `roles/cloudformation/files/cloudformation-example.json`.  If *state=present* and the stack does not exist yet, either *template*, *template_body* or *template_url* must be specified (but only one of them).  If *state=present*, the stack does exist, and neither *template*, *template_body* nor *template_url* are specified, the previous template will be reused. |
| **template_body**  string | Template body. Use this to pass in the actual body of the CloudFormation template.  If *state=present* and the stack does not exist yet, either *template*, *template_body* or *template_url* must be specified (but only one of them).  If *state=present*, the stack does exist, and neither *template*, *template_body* nor *template_url* are specified, the previous template will be reused. |
| **template_url**  string | Location of file containing the template body.  The URL must point to a template (max size 307,200 bytes) located in an S3 bucket in the same region as the stack.  If *state=present* and the stack does not exist yet, either *template*, *template_body* or *template_url* must be specified (but only one of them).  If *state=present*, the stack does exist, and neither *template*, *template_body* nor *template_url* are specified, the previous template will be reused. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Whether or not to wait for stack operation to complete. This includes waiting for stack instances to reach UPDATE_COMPLETE status.  If you choose not to wait, this module will not notify when stack operations fail because it will not wait for them to finish.  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How long to wait (in seconds) for stacks to complete create/update/delete operations.  **Default:** `900` |

## [Notes](cloudformation_stack_set_module.md#id4)

> **Note:**
>
> - To make an individual stack, you want the [amazon.aws.cloudformation](../../amazon/aws/cloudformation_module.md#ansible-collections-amazon-aws-cloudformation-module) module.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](cloudformation_stack_set_module.md#id5)

```yaml+jinja
- name: Create a stack set with instances in two accounts
  community.aws.cloudformation_stack_set:
    name: my-stack
    description: Test stack in two accounts
    state: present
    template_url: https://s3.amazonaws.com/my-bucket/cloudformation.template
    accounts:
      - 123456789012
      - 234567890123
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
    accounts:
      - 123456789012
      - 234567890123
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
    accounts:
      - 123456789012
      - 234567890123
    regions:
    - us-east-1

- name: Register new accounts (create new stack instances) with an existing stack set.
  community.aws.cloudformation_stack_set:
    name: my-stack
    state: present
    wait: true
    parameters:
      InstanceName: my_restacked_instance
    tags:
      foo: bar
      test: stack
    accounts:
      - 123456789012
      - 234567890123
      - 345678901234
    regions:
    - us-east-1
```

## [Return Values](cloudformation_stack_set_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **operations**  list / elements=string | All operations initiated by this run of the cloudformation_stack_set module  **Returned:** always  **Sample:** `[{"action": "CREATE", "administration_role_arn": "arn:aws:iam::1234567890:role/AWSCloudFormationStackSetAdministrationRole", "creation_timestamp": "2018-06-18T17:40:46.372000+00:00", "end_timestamp": "2018-06-18T17:41:24.560000+00:00", "execution_role_name": "AWSCloudFormationStackSetExecutionRole", "operation_id": "Ansible-StackInstance-Create-0ff2af5b-251d-4fdb-8b89-1ee444eba8b8", "operation_preferences": {"region_order": ["us-east-1", "us-east-2"]}, "stack_set_id": "TestStackPrime:19f3f684-aae9-4e67-ba36-e09f92cf5929", "status": "FAILED"}]` |
| **operations_log**  list / elements=string | Most recent events in CloudFormation’s event log. This may be from a previous run in some cases.  **Returned:** always  **Sample:** `[{"action": "CREATE", "creation_timestamp": "2018-06-18T17:40:46.372000+00:00", "end_timestamp": "2018-06-18T17:41:24.560000+00:00", "operation_id": "Ansible-StackInstance-Create-0ff2af5b-251d-4fdb-8b89-1ee444eba8b8", "stack_instances": [{"account": "1234567890", "region": "us-east-1", "stack_set_id": "TestStackPrime:19f3f684-aae9-4e67-ba36-e09f92cf5929", "status": "OUTDATED", "status_reason": "Account 1234567890 should have 'AWSCloudFormationStackSetAdministrationRole' role with trust relationship to CloudFormation service."}], "status": "FAILED"}]` |
| **stack_instances**  list / elements=string | CloudFormation stack instances that are members of this stack set. This will also include their region and account ID.  **Returned:** state == present  **Sample:** `[{"account": "1234567890", "region": "us-east-1", "stack_set_id": "TestStackPrime:19f3f684-aae9-4e67-ba36-e09f92cf5929", "status": "OUTDATED", "status_reason": "Account 1234567890 should have 'AWSCloudFormationStackSetAdministrationRole' role with trust relationship to CloudFormation service.\n"}, {"account": "1234567890", "region": "us-east-2", "stack_set_id": "TestStackPrime:19f3f684-aae9-4e67-ba36-e09f92cf5929", "status": "OUTDATED", "status_reason": "Cancelled since failure tolerance has exceeded"}]` |
| **stack_set**  dictionary | Facts about the currently deployed stack set, its parameters, and its tags  **Returned:** state == present  **Sample:** `{"administration_role_arn": "arn:aws:iam::1234567890:role/AWSCloudFormationStackSetAdministrationRole", "capabilities": [], "description": "test stack PRIME", "execution_role_name": "AWSCloudFormationStackSetExecutionRole", "parameters": [], "stack_set_arn": "arn:aws:cloudformation:us-east-1:1234567890:stackset/TestStackPrime:19f3f684-aae9-467-ba36-e09f92cf5929", "stack_set_id": "TestStackPrime:19f3f684-aae9-4e67-ba36-e09f92cf5929", "stack_set_name": "TestStackPrime", "status": "ACTIVE", "tags": {"Some": "Thing", "an": "other"}, "template_body": "AWSTemplateFormatVersion: \"2010-09-09\"\nParameters: {}\nResources:\n  Bukkit:\n    Type: \"AWS::S3::Bucket\"\n    Properties: {}\n  other:\n    Type: \"AWS::SNS::Topic\"\n    Properties: {}\n"}` |

### Authors

- Ryan Scott Brown (@ryansb)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
