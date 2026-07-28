---
collection: ansible
version: "6"
title: "community.aws.aws_ssm_parameter_store module – Manage key-value pairs in aws parameter store."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_ssm_parameter_store_module.html
fetched_at: 2026-07-27T17:03:36+00:00
---
# community.aws.aws_ssm_parameter_store module – Manage key-value pairs in aws parameter store.

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
> see [Requirements](aws_ssm_parameter_store_module.md#ansible-collections-community-aws-aws-ssm-parameter-store-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_ssm_parameter_store`.

New in community.aws 1.0.0

- [Synopsis](aws_ssm_parameter_store_module.md#synopsis)
- [Requirements](aws_ssm_parameter_store_module.md#requirements)
- [Parameters](aws_ssm_parameter_store_module.md#parameters)
- [Notes](aws_ssm_parameter_store_module.md#notes)
- [Examples](aws_ssm_parameter_store_module.md#examples)
- [Return Values](aws_ssm_parameter_store_module.md#return-values)

## [Synopsis](aws_ssm_parameter_store_module.md#id1)

- Manage key-value pairs in aws parameter store.

## [Requirements](aws_ssm_parameter_store_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_ssm_parameter_store_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **decryption**  boolean | Work with SecureString type to get plain text secrets  Choices:   - `false` - `true` ← (default) |
| **description**  string | Parameter key description. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **key_id**  string | AWS KMS key to decrypt the secrets.  The default key (`alias/aws/ssm`) is automatically generated the first time it’s requested.  Default: `"alias/aws/ssm"` |
| **name**  string / required | Parameter key name. |
| **overwrite_value**  string | Option to overwrite an existing value if it already exists.  Choices:   - `"never"` - `"changed"` ← (default) - `"always"` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Creates or modifies an existing parameter.  Deletes a parameter.  Choices:   - `"present"` ← (default) - `"absent"` |
| **string_type**  string | Parameter String type.  Choices:   - `"String"` ← (default) - `"StringList"` - `"SecureString"` |
| **tier**  string  added in community.aws 1.5.0 | Parameter store tier type.  Choices:   - `"Standard"` ← (default) - `"Advanced"` - `"Intelligent-Tiering"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **value**  string | Parameter value. |

## [Notes](aws_ssm_parameter_store_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_ssm_parameter_store_module.md#id5)

```yaml+jinja
- name: Create or update key/value pair in aws parameter store
  community.aws.aws_ssm_parameter_store:
    name: "Hello"
    description: "This is your first key"
    value: "World"

- name: Delete the key
  community.aws.aws_ssm_parameter_store:
    name: "Hello"
    state: absent

- name: Create or update secure key/value pair with default kms key (aws/ssm)
  community.aws.aws_ssm_parameter_store:
    name: "Hello"
    description: "This is your first key"
    string_type: "SecureString"
    value: "World"

- name: Create or update secure key/value pair with nominated kms key
  community.aws.aws_ssm_parameter_store:
    name: "Hello"
    description: "This is your first key"
    string_type: "SecureString"
    key_id: "alias/demo"
    value: "World"

- name: Always update a parameter store value and create a new version
  community.aws.aws_ssm_parameter_store:
    name: "overwrite_example"
    description: "This example will always overwrite the value"
    string_type: "String"
    value: "Test1234"
    overwrite_value: "always"

- name: Create or update key/value pair in aws parameter store with tier
  community.aws.aws_ssm_parameter_store:
    name: "Hello"
    description: "This is your first key"
    value: "World"
    tier: "Advanced"

- name: recommend to use with aws_ssm lookup plugin
  ansible.builtin.debug:
    msg: "{{ lookup('amazon.aws.aws_ssm', 'hello') }}"
```

## [Return Values](aws_ssm_parameter_store_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **delete_parameter**  dictionary | Delete a parameter from the system.  Returned: success |
| **put_parameter**  dictionary | Add one or more parameters to the system.  Returned: success |

### Authors

- Davinder Pal (@116davinder)
- Nathan Webster (@nathanwebsterdotme)
- Bill Wang (@ozbillwang)
- Michael De La Rue (@mikedlr)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
