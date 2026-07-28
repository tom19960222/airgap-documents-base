---
collection: ansible
version: "6"
title: "community.aws.aws_secret module – Manage secrets stored in AWS Secrets Manager."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_secret_module.html
fetched_at: 2026-07-27T17:03:33+00:00
---
# community.aws.aws_secret module – Manage secrets stored in AWS Secrets Manager.

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
> see [Requirements](aws_secret_module.md#ansible-collections-community-aws-aws-secret-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_secret`.

New in community.aws 1.0.0

- [Synopsis](aws_secret_module.md#synopsis)
- [Requirements](aws_secret_module.md#requirements)
- [Parameters](aws_secret_module.md#parameters)
- [Notes](aws_secret_module.md#notes)
- [Examples](aws_secret_module.md#examples)
- [Return Values](aws_secret_module.md#return-values)

## [Synopsis](aws_secret_module.md#id1)

- Create, update, and delete secrets stored in AWS Secrets Manager.

## [Requirements](aws_secret_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_secret_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **description**  string | Specifies a user-provided description of the secret. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **kms_key_id**  string | Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the *secret* values in the versions stored in this secret. |
| **name**  string / required | Friendly name for the secret you are creating. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **recovery_window**  integer | Only used if state is absent.  Specifies the number of days that Secrets Manager waits before it can delete the secret.  If set to 0, the deletion is forced without recovery.  Default: `30` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **resource_policy**  json  added in community.aws 3.1.0 | Specifies JSON-formatted resource policy to attach to the secret. Useful when granting cross-account access to secrets. |
| **rotation_interval**  integer | Specifies the number of days between automatic scheduled rotations of the secret.  Default: `30` |
| **rotation_lambda**  string | Specifies the ARN of the Lambda function that can rotate the secret. |
| **secret**  string | Specifies string or binary data that you want to encrypt and store in the new version of the secret.  Default: `""` |
| **secret_type**  string | Specifies the type of data that you want to encrypt.  Choices:   - `"binary"` - `"string"` ← (default) |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Whether the secret should be exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Specifies a list of user-defined tags that are attached to the secret. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](aws_secret_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_secret_module.md#id5)

```yaml+jinja
- name: Add string to AWS Secrets Manager
  community.aws.aws_secret:
    name: 'test_secret_string'
    state: present
    secret_type: 'string'
    secret: "{{ super_secret_string }}"

- name: Add a secret with resource policy attached
  community.aws.aws_secret:
    name: 'test_secret_string'
    state: present
    secret_type: 'string'
    secret: "{{ super_secret_string }}"
    resource_policy: "{{ lookup('template', 'templates/resource_policy.json.j2', convert_data=False) | string }}"

- name: remove string from AWS Secrets Manager
  community.aws.aws_secret:
    name: 'test_secret_string'
    state: absent
    secret_type: 'string'
    secret: "{{ super_secret_string }}"
```

## [Return Values](aws_secret_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **secret**  complex | The secret information  Returned: always |
| **arn**  string | The ARN of the secret  Returned: always  Sample: `"arn:aws:secretsmanager:eu-west-1:xxxxxxxxxx:secret:xxxxxxxxxxx"` |
| **last_accessed_date**  string | The date the secret was last accessed  Returned: always  Sample: `"2018-11-20T01:00:00+01:00"` |
| **last_changed_date**  string | The date the secret was last modified.  Returned: always  Sample: `"2018-11-20T12:16:38.433000+01:00"` |
| **name**  string | The secret name.  Returned: always  Sample: `"my_secret"` |
| **rotation_enabled**  boolean | The secret rotation status.  Returned: always  Sample: `false` |
| **version_ids_to_stages**  dictionary | Provide the secret version ids and the associated secret stage.  Returned: always  Sample: `{"dc1ed59b-6d8e-4450-8b41-536dfe4600a9": ["AWSCURRENT"]}` |

### Authors

- REY Remi (@rrey)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
