---
collection: ansible
version: "8"
title: "community.aws.sts_assume_role module – Assume a role using AWS Security Token Service and obtain temporary credentials"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/sts_assume_role_module.html
fetched_at: 2026-07-28T01:42:04+00:00
---
# community.aws.sts_assume_role module – Assume a role using AWS Security Token Service and obtain temporary credentials

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
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](sts_assume_role_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **duration_seconds**  integer | The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) to 43200 seconds (12 hours).  The max depends on the IAM role’s sessions duration setting.  By default, the value is set to 3600 seconds. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **external_id**  string | A unique identifier that is used by third parties to assume a role in their customers’ accounts. |
| **mfa_serial_number**  string | The identification number of the MFA device that is associated with the user who is making the AssumeRole call. |
| **mfa_token**  string | The value provided by the MFA device, if the trust policy of the role being assumed requires MFA. |
| **policy**  string | Supplemental policy to use in addition to assumed role’s policies. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **role_arn**  string / required | The Amazon Resource Name (ARN) of the role that the caller is assuming <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html#Identifiers_ARNs>. |
| **role_session_name**  string / required | Name of the role’s session - will be used by CloudTrail. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](sts_assume_role_module.md#id4)

> **Note:**
>
> - In order to use the assumed role in a following playbook task you must pass the *access_key*, *secret_key* and *session_token* parameters to modules that should use the assumed credentials.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](sts_assume_role_module.md#id5)

```yaml+jinja
# Assume an existing role (more details: https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)
- community.aws.sts_assume_role:
    access_key: AKIA1EXAMPLE1EXAMPLE
    secret_key: 123456789abcdefghijklmnopqrstuvwxyzABCDE
    role_arn: "arn:aws:iam::123456789012:role/someRole"
    role_session_name: "someRoleSession"
  register: assumed_role

# Use the assumed role above to tag an instance in account 123456789012
- amazon.aws.ec2_tag:
    access_key: "{{ assumed_role.sts_creds.access_key }}"
    secret_key: "{{ assumed_role.sts_creds.secret_key }}"
    session_token: "{{ assumed_role.sts_creds.session_token }}"
    resource: i-xyzxyz01
    state: present
    tags:
      MyNewTag: value
```

## [Return Values](sts_assume_role_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | True if obtaining the credentials succeeds  **Returned:** always |
| **sts_creds**  dictionary | The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) token  **Returned:** always  **Sample:** `{"access_key": "XXXXXXXXXXXXXXXXXXXX", "expiration": "2017-11-11T11:11:11+00:00", "secret_key": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", "session_token": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}` |
| **sts_user**  dictionary | The Amazon Resource Name (ARN) and the assumed role ID  **Returned:** always  **Sample:** `{"arn": "ARO123EXAMPLE123:Bob", "assumed_role_id": "arn:aws:sts::123456789012:assumed-role/demo/Bob"}` |

### Authors

- Boris Ekelchik (@bekelchik)
- Marek Piatek (@piontas)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
