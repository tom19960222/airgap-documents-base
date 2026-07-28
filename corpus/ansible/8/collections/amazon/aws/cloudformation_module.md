---
collection: ansible
version: "8"
title: "amazon.aws.cloudformation module – Create or delete an AWS CloudFormation stack"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/cloudformation_module.html
fetched_at: 2026-07-28T01:06:13+00:00
---
# amazon.aws.cloudformation module – Create or delete an AWS CloudFormation stack

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
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](cloudformation_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **backoff_delay**  integer | Number of seconds to wait for the next retry.  **Default:** `3` |
| **backoff_max_delay**  integer | Maximum amount of time to wait between retries.  **Default:** `30` |
| **backoff_retries**  integer | Number of times to retry operation.  AWS API throttling mechanism fails CloudFormation module so we have to retry a couple of times.  **Default:** `10` |
| **capabilities**  list / elements=string | Specify capabilities that stack template contains.  Valid values are `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM` and `CAPABILITY_AUTO_EXPAND`.  **Default:** `["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]` |
| **changeset_name**  string | Name given to the changeset when creating a changeset.  Only used when *create_changeset=true*.  By default a name prefixed with Ansible-STACKNAME is generated based on input parameters. See the AWS Change Sets docs for more information <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html> |
| **create_changeset**  boolean | If stack already exists create a changeset instead of directly applying changes. See the AWS Change Sets docs <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html>.  WARNING: if the stack does not exist, it will be created without changeset. If *state=absent*, the stack will be deleted immediately with no changeset.  **Choices:**   - `false` ← (default) - `true` |
| **create_timeout**  integer | The amount of time (in minutes) that can pass before the stack status becomes CREATE_FAILED |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **disable_rollback**  boolean | If a stacks fails to form, rollback will remove the stack.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **events_limit**  integer | Maximum number of CloudFormation events to fetch from a stack when creating or updating it.  **Default:** `200` |
| **notification_arns**  string | A comma separated list of Simple Notification Service (SNS) topic ARNs to publish stack related events. |
| **on_create_failure**  string | Action to take upon failure of stack creation. Incompatible with the *disable_rollback* option.  **Choices:**   - `"DO_NOTHING"` - `"ROLLBACK"` - `"DELETE"` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **role_arn**  string | The role that AWS CloudFormation assumes to create the stack. See the AWS CloudFormation Service Role docs <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-servicerole.html> |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **stack_name**  string / required | Name of the CloudFormation stack. |
| **stack_policy**  string | The path of the file containing the CloudFormation stack policy. A policy cannot be removed once placed, but it can be modified. for instance, allow all updates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html#d0e9051> |
| **stack_policy_body**  json  *added in amazon.aws 1.5.0* | The CloudFormation stack policy in JSON. A policy cannot be removed once placed, but it can be modified. for instance, allow all updates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html#d0e9051> |
| **stack_policy_on_update_body**  json  *added in amazon.aws 1.5.0* | the body of the cloudformation stack policy only applied during this update. |
| **state**  string | If *state=present*, stack will be created.  If *state=present* and if stack exists and template has changed, it will be updated.  If *state=absent*, stack will be removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Dictionary of tags to associate with stack and its resources during stack creation.  Can be updated later, updating tags removes previous entries. |
| **template**  path | The local path of the CloudFormation template.  This must be the full path to the file, relative to the working directory. If using roles this may look like `roles/cloudformation/files/cloudformation-example.json`.  If *state=present* and the stack does not exist yet, either *template*, *template_body* or *template_url* must be specified (but only one of them).  If *state=present*, the stack does exist, and neither *template*, *template_body* nor *template_url* are specified, the previous template will be reused. |
| **template_body**  string | Template body. Use this to pass in the actual body of the CloudFormation template.  If *state=present* and the stack does not exist yet, either *template*, *template_body* or *template_url* must be specified (but only one of them).  If *state=present*, the stack does exist, and neither *template*, *template_body* nor *template_url* are specified, the previous template will be reused. |
| **template_parameters**  dictionary | A list of hashes of all the template variables for the stack. The value can be a string or a dict.  Dict can be used to set additional template parameter attributes like UsePreviousValue (see example).  **Default:** `{}` |
| **template_url**  string | Location of file containing the template body. The URL must point to a template (max size 307,200 bytes) located in an S3 bucket in the same region as the stack.  If *state=present* and the stack does not exist yet, either *template*, *template_body* or *template_url* must be specified (but only one of them).  If *state=present*, the stack does exist, and neither *template*, *template_body* nor *template_url* are specified, the previous template will be reused. |
| **termination_protection**  boolean | Enable or disable termination protection on the stack.  **Choices:**   - `false` - `true` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cloudformation_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

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
        value: arn:aws:rds:es-east-1:123456789012:snapshot:rds:my-db-snapshot
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
    termination_protection: true

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
| **change_set_id**  string | The ID of the stack change set if one was created  **Returned:** *state=present* and *create_changeset=true*  **Sample:** `"arn:aws:cloudformation:us-east-1:123456789012:changeSet/Ansible-StackName-f4496805bd1b2be824d1e315c6884247ede41eb0"` |
| **events**  list / elements=string | Most recent events in CloudFormation’s event log. This may be from a previous run in some cases.  **Returned:** always  **Sample:** `["StackEvent AWS::CloudFormation::Stack stackname UPDATE_COMPLETE", "StackEvent AWS::CloudFormation::Stack stackname UPDATE_COMPLETE_CLEANUP_IN_PROGRESS"]` |
| **log**  list / elements=string | Debugging logs. Useful when modifying or finding an error.  **Returned:** always  **Sample:** `["updating stack"]` |
| **stack_outputs**  dictionary | A key:value dictionary of all the stack outputs currently defined. If there are no stack outputs, it is an empty dictionary.  **Returned:** state == present  **Sample:** `{"MySg": "AnsibleModuleTestYAML-CFTestSg-C8UVS567B6NS"}` |
| **stack_resources**  list / elements=string | AWS stack resources and their status. List of dictionaries, one dict per resource.  **Returned:** state == present  **Sample:** `[{"last_updated_time": "2016-10-11T19:40:14.979000+00:00", "logical_resource_id": "CFTestSg", "physical_resource_id": "cloudformation2-CFTestSg-16UQ4CYQ57O9F", "resource_type": "AWS::EC2::SecurityGroup", "status": "UPDATE_COMPLETE", "status_reason": null}]` |

### Authors

- James S. Martin (@jsmartin)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
