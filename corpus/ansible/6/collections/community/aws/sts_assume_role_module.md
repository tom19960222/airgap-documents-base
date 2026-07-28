---
collection: ansible
version: "6"
title: "community.aws.sts_assume_role module – Assume a role using AWS Security Token Service and obtain temporary credentials"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/sts_assume_role_module.html
fetched_at: 2026-07-27T17:05:08+00:00
---
# community.aws.sts_assume_role module – Assume a role using AWS Security Token Service and obtain temporary credentials

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
> see [Requirements](sts_assume_role_module.md#ansible-collections-community-aws-sts-assume-role-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.sts_assume_role`.

New in community.aws 1.0.0

- [Synopsis](sts_assume_role_module.md#synopsis)
- [Requirements](sts_assume_role_module.md#requirements)
- [Parameters](sts_assume_role_module.md#parameters)
- [Notes](sts_assume_role_module.md#notes)
- [Examples](sts_assume_role_module.md#examples)
- [Return Values](sts_assume_role_module.md#return-values)

## [Synopsis](sts_assume_role_module.md#id1)

- Assume a role using AWS Security Token Service and obtain temporary credentials.

## [Requirements](sts_assume_role_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](sts_assume_role_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **duration_seconds**  integer | The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) to 43200 seconds (12 hours).  The max depends on the IAM role’s sessions duration setting.  By default, the value is set to 3600 seconds. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **external_id**  string | A unique identifier that is used by third parties to assume a role in their customers’ accounts. |
| **mfa_serial_number**  string | The identification number of the MFA device that is associated with the user who is making the AssumeRole call. |
| **mfa_token**  string | The value provided by the MFA device, if the trust policy of the role being assumed requires MFA. |
| **policy**  string | Supplemental policy to use in addition to assumed role’s policies. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **role_arn**  string / required | The Amazon Resource Name (ARN) of the role that the caller is assuming <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html#Identifiers_ARNs>. |
| **role_session_name**  string / required | Name of the role’s session - will be used by CloudTrail. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](sts_assume_role_module.md#id4)

> **Note:**
>
> - In order to use the assumed role in a following playbook task you must pass the access_key, access_secret and access_token.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](sts_assume_role_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Assume an existing role (more details: https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)
- community.aws.sts_assume_role:
    role_arn: "arn:aws:iam::123456789012:role/someRole"
    role_session_name: "someRoleSession"
  register: assumed_role

# Use the assumed role above to tag an instance in account 123456789012
- amazon.aws.ec2_tag:
    aws_access_key: "{{ assumed_role.sts_creds.access_key }}"
    aws_secret_key: "{{ assumed_role.sts_creds.secret_key }}"
    security_token: "{{ assumed_role.sts_creds.session_token }}"
    resource: i-xyzxyz01
    state: present
    tags:
      MyNewTag: value
```

## [Return Values](sts_assume_role_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | True if obtaining the credentials succeeds  Returned: always |
| **sts_creds**  dictionary | The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) token  Returned: always  Sample: `{"access_key": "XXXXXXXXXXXXXXXXXXXX", "expiration": "2017-11-11T11:11:11+00:00", "secret_key": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", "session_token": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}` |
| **sts_user**  dictionary | The Amazon Resource Name (ARN) and the assumed role ID  Returned: always  Sample: `{"arn": "ARO123EXAMPLE123:Bob", "assumed_role_id": "arn:aws:sts::123456789012:assumed-role/demo/Bob"}` |

### Authors

- Boris Ekelchik (@bekelchik)
- Marek Piatek (@piontas)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
