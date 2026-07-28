---
collection: ansible
version: "6"
title: "amazon.aws.cloudformation module – Create or delete an AWS CloudFormation stack"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/cloudformation_module.html
fetched_at: 2026-07-27T16:43:40+00:00
---
# amazon.aws.cloudformation module – Create or delete an AWS CloudFormation stack

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
> see [Requirements](cloudformation_module.md#ansible-collections-amazon-aws-cloudformation-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.cloudformation`.

New in amazon.aws 1.0.0

- [Synopsis](cloudformation_module.md#synopsis)
- [Requirements](cloudformation_module.md#requirements)
- [Parameters](cloudformation_module.md#parameters)
- [Notes](cloudformation_module.md#notes)
- [Examples](cloudformation_module.md#examples)
- [Return Values](cloudformation_module.md#return-values)

## [Synopsis](cloudformation_module.md#id1)

- Launches or updates an AWS CloudFormation stack and waits for it complete.

## [Requirements](cloudformation_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](cloudformation_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **backoff_delay**  integer | Number of seconds to wait for the next retry.  Default: `3` |
| **backoff_max_delay**  integer | Maximum amount of time to wait between retries.  Default: `30` |
| **backoff_retries**  integer | Number of times to retry operation.  AWS API throttling mechanism fails CloudFormation module so we have to retry a couple of times.  Default: `10` |
| **capabilities**  list / elements=string | Specify capabilities that stack template contains.  Valid values are `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM` and `CAPABILITY_AUTO_EXPAND`.  Default: `["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]` |
| **changeset_name**  string | Name given to the changeset when creating a changeset.  Only used when *create_changeset=true*.  By default a name prefixed with Ansible-STACKNAME is generated based on input parameters. See the AWS Change Sets docs for more information <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html> |
| **create_changeset**  boolean | If stack already exists create a changeset instead of directly applying changes. See the AWS Change Sets docs <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html>.  WARNING: if the stack does not exist, it will be created without changeset. If *state=absent*, the stack will be deleted immediately with no changeset.  Choices:   - `false` ← (default) - `true` |
| **create_timeout**  integer | The amount of time (in minutes) that can pass before the stack status becomes CREATE_FAILED |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **disable_rollback**  boolean | If a stacks fails to form, rollback will remove the stack.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **events_limit**  integer | Maximum number of CloudFormation events to fetch from a stack when creating or updating it.  Default: `200` |
| **notification_arns**  string | A comma separated list of Simple Notification Service (SNS) topic ARNs to publish stack related events. |
| **on_create_failure**  string | Action to take upon failure of stack creation. Incompatible with the *disable_rollback* option.  Choices:   - `"DO_NOTHING"` - `"ROLLBACK"` - `"DELETE"` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **role_arn**  string | The role that AWS CloudFormation assumes to create the stack. See the AWS CloudFormation Service Role docs <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-servicerole.html> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **stack_name**  string / required | Name of the CloudFormation stack. |
| **stack_policy**  string | The path of the file containing the CloudFormation stack policy. A policy cannot be removed once placed, but it can be modified. for instance, allow all updates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html#d0e9051> |
| **stack_policy_body**  json  added in amazon.aws 1.5.0 | The CloudFormation stack policy in JSON. A policy cannot be removed once placed, but it can be modified. for instance, allow all updates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html#d0e9051> |
| **stack_policy_on_update_body**  json  added in amazon.aws 1.5.0 | the body of the cloudformation stack policy only applied during this update. |
| **state**  string | If *state=present*, stack will be created.  If *state=present* and if stack exists and template has changed, it will be updated.  If *state=absent*, stack will be removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Dictionary of tags to associate with stack and its resources during stack creation.  Can be updated later, updating tags removes previous entries. |
| **template**  path | The local path of the CloudFormation template.  This must be the full path to the file, relative to the working directory. If using roles this may look like `roles/cloudformation/files/cloudformation-example.json`.  If *state=present* and the stack does not exist yet, either *template*, *template_body* or *template_url* must be specified (but only one of them).  If *state=present*, the stack does exist, and neither *template*, *template_body* nor *template_url* are specified, the previous template will be reused. |
| **template_body**  string | Template body. Use this to pass in the actual body of the CloudFormation template.  If *state=present* and the stack does not exist yet, either *template*, *template_body* or *template_url* must be specified (but only one of them).  If *state=present*, the stack does exist, and neither *template*, *template_body* nor *template_url* are specified, the previous template will be reused. |
| **template_format**  string | This parameter is ignored since Ansible 2.3 and will be removed after 2022-06-01.  Templates are now passed raw to CloudFormation regardless of format. |
| **template_parameters**  dictionary | A list of hashes of all the template variables for the stack. The value can be a string or a dict.  Dict can be used to set additional template parameter attributes like UsePreviousValue (see example).  Default: `{}` |
| **template_url**  string | Location of file containing the template body. The URL must point to a template (max size 307,200 bytes) located in an S3 bucket in the same region as the stack.  If *state=present* and the stack does not exist yet, either *template*, *template_body* or *template_url* must be specified (but only one of them).  If *state=present*, the stack does exist, and neither *template*, *template_body* nor *template_url* are specified, the previous template will be reused. |
| **termination_protection**  boolean | Enable or disable termination protection on the stack.  Choices:   - `false` - `true` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](cloudformation_module.md#id4)

> **Note:**
>
> - CloudFormation features change often, and this module tries to keep up. That means your botocore version should be fresh. The version listed in the requirements is the oldest version that works with the module as a whole. Some features may require recent versions, and we do not pinpoint a minimum version for each feature. Instead of relying on the minimum version, keep botocore up to date. AWS is always releasing features and fixing bugs.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](cloudformation_module.md#id5)

```yaml+jinja
- name: create a cloudformation stack
  amazon.aws.cloudformation:
    stack_name: "ansible-cloudformation"
    state: "present"
    region: "us-east-1"
    disable_rollback: true
    template: "files/cloudformation-example.json"
    template_parameters:
      KeyName: "jmartin"
      DiskType: "ephemeral"
      InstanceType: "m1.small"
      ClusterSize: 3
    tags:
      Stack: "ansible-cloudformation"

# Basic role example
- name: create a stack, specify role that cloudformation assumes
  amazon.aws.cloudformation:
    stack_name: "ansible-cloudformation"
    state: "present"
    region: "us-east-1"
    disable_rollback: true
    template: "roles/cloudformation/files/cloudformation-example.json"
    role_arn: 'arn:aws:iam::123456789012:role/cloudformation-iam-role'

- name: delete a stack
  amazon.aws.cloudformation:
    stack_name: "ansible-cloudformation-old"
    state: "absent"

# Create a stack, pass in template from a URL, disable rollback if stack creation fails,
# pass in some parameters to the template, provide tags for resources created
- name: create a stack, pass in the template via an URL
  amazon.aws.cloudformation:
    stack_name: "ansible-cloudformation"
    state: present
    region: us-east-1
    disable_rollback: true
    template_url: https://s3.amazonaws.com/my-bucket/cloudformation.template
    template_parameters:
      KeyName: jmartin
      DiskType: ephemeral
      InstanceType: m1.small
      ClusterSize: 3
    tags:
      Stack: ansible-cloudformation

# Create a stack, passing in template body using lookup of Jinja2 template, disable rollback if stack creation fails,
# pass in some parameters to the template, provide tags for resources created
- name: create a stack, pass in the template body via lookup template
  amazon.aws.cloudformation:
    stack_name: "ansible-cloudformation"
    state: present
    region: us-east-1
    disable_rollback: true
    template_body: "{{ lookup('template', 'cloudformation.j2') }}"
    template_parameters:
      KeyName: jmartin
      DiskType: ephemeral
      InstanceType: m1.small
      ClusterSize: 3
    tags:
      Stack: ansible-cloudformation

# Pass a template parameter which uses CloudFormation's UsePreviousValue attribute
# When use_previous_value is set to True, the given value will be ignored and
# CloudFormation will use the value from a previously submitted template.
# If use_previous_value is set to False (default) the given value is used.
- amazon.aws.cloudformation:
    stack_name: "ansible-cloudformation"
    state: "present"
    region: "us-east-1"
    template: "files/cloudformation-example.json"
    template_parameters:
      DBSnapshotIdentifier:
        use_previous_value: True
        value: arn:aws:rds:es-east-1:000000000000:snapshot:rds:my-db-snapshot
      DBName:
        use_previous_value: True
    tags:
      Stack: "ansible-cloudformation"

# Enable termination protection on a stack.
# If the stack already exists, this will update its termination protection
- name: enable termination protection during stack creation
  amazon.aws.cloudformation:
    stack_name: my_stack
    state: present
    template_url: https://s3.amazonaws.com/my-bucket/cloudformation.template
    termination_protection: yes

# Configure TimeoutInMinutes before the stack status becomes CREATE_FAILED
# In this case, if disable_rollback is not set or is set to false, the stack will be rolled back.
- name: enable termination protection during stack creation
  amazon.aws.cloudformation:
    stack_name: my_stack
    state: present
    template_url: https://s3.amazonaws.com/my-bucket/cloudformation.template
    create_timeout: 5

# Configure rollback behaviour on the unsuccessful creation of a stack allowing
# CloudFormation to clean up, or do nothing in the event of an unsuccessful
# deployment
# In this case, if on_create_failure is set to "DELETE", it will clean up the stack if
# it fails to create
- name: create stack which will delete on creation failure
  amazon.aws.cloudformation:
    stack_name: my_stack
    state: present
    template_url: https://s3.amazonaws.com/my-bucket/cloudformation.template
    on_create_failure: DELETE
```

## [Return Values](cloudformation_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **change_set_id**  string | The ID of the stack change set if one was created  Returned: *state=present* and *create_changeset=true*  Sample: `"arn:aws:cloudformation:us-east-1:012345678901:changeSet/Ansible-StackName-f4496805bd1b2be824d1e315c6884247ede41eb0"` |
| **events**  list / elements=string | Most recent events in CloudFormation’s event log. This may be from a previous run in some cases.  Returned: always  Sample: `["StackEvent AWS::CloudFormation::Stack stackname UPDATE_COMPLETE", "StackEvent AWS::CloudFormation::Stack stackname UPDATE_COMPLETE_CLEANUP_IN_PROGRESS"]` |
| **log**  list / elements=string | Debugging logs. Useful when modifying or finding an error.  Returned: always  Sample: `["updating stack"]` |
| **stack_outputs**  dictionary | A key:value dictionary of all the stack outputs currently defined. If there are no stack outputs, it is an empty dictionary.  Returned: state == present  Sample: `{"MySg": "AnsibleModuleTestYAML-CFTestSg-C8UVS567B6NS"}` |
| **stack_resources**  list / elements=string | AWS stack resources and their status. List of dictionaries, one dict per resource.  Returned: state == present  Sample: `[{"last_updated_time": "2016-10-11T19:40:14.979000+00:00", "logical_resource_id": "CFTestSg", "physical_resource_id": "cloudformation2-CFTestSg-16UQ4CYQ57O9F", "resource_type": "AWS::EC2::SecurityGroup", "status": "UPDATE_COMPLETE", "status_reason": null}]` |

### Authors

- James S. Martin (@jsmartin)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
