---
collection: ansible
version: "8"
title: "community.aws.iam_access_key module – Manage AWS IAM User access keys"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/iam_access_key_module.html
fetched_at: 2026-07-28T01:41:19+00:00
---
# community.aws.iam_access_key module – Manage AWS IAM User access keys

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
> see [Requirements](iam_access_key_module.md#ansible-collections-community-aws-iam-access-key-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.iam_access_key`.

New in community.aws 2.1.0

- [Synopsis](iam_access_key_module.md#synopsis)
- [Requirements](iam_access_key_module.md#requirements)
- [Parameters](iam_access_key_module.md#parameters)
- [Notes](iam_access_key_module.md#notes)
- [Examples](iam_access_key_module.md#examples)
- [Return Values](iam_access_key_module.md#return-values)

## [Synopsis](iam_access_key_module.md#id1)

- Manage AWS IAM user access keys.

## [Requirements](iam_access_key_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](iam_access_key_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **active**  aliases: enabled  boolean | Whether the key should be enabled or disabled.  Defaults to `true` when creating a new key.  **Choices:**   - `false` - `true` |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **id**  string | The ID of the access key.  Required when *state=absent*.  Mutually exclusive with *rotate_keys*. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **rotate_keys**  boolean | When there are already 2 access keys attached to the IAM user the oldest key will be removed and a new key created.  Ignored if *state=absent*  Mutually exclusive with *id*.  **Choices:**   - `false` ← (default) - `true` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create or remove the access key.  When *state=present* and *id* is not defined a new key will be created.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **user_name**  aliases: username  string / required | The name of the IAM User to which the key belongs. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](iam_access_key_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](iam_access_key_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Create a new access key
  community.aws.iam_access_key:
    user_name: example_user
    state: present

- name: Delete the access_key
  community.aws.iam_access_key:
    user_name: example_user
    id: AKIA1EXAMPLE1EXAMPLE
    state: absent
```

## [Return Values](iam_access_key_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **access_key**  complex | A dictionary containing all the access key information.  **Returned:** When the key exists. |
| **access_key_id**  string | The ID for the access key.  **Returned:** success  **Sample:** `"AKIA1EXAMPLE1EXAMPLE"` |
| **create_date**  string | The date and time, in ISO 8601 date-time format, when the access key was created.  **Returned:** success  **Sample:** `"2021-10-09T13:25:42+00:00"` |
| **status**  string | The status of the key.  `Active` means it can be used.  `Inactive` means it can not be used.  **Returned:** success  **Sample:** `"Inactive"` |
| **user_name**  string | The name of the IAM user to which the key is attached.  **Returned:** success  **Sample:** `"example_user"` |
| **deleted_access_key_id**  string | The access key deleted during rotation.  **Returned:** When a key was deleted during the rotation of access keys  **Sample:** `"AKIA1EXAMPLE1EXAMPLE"` |
| **secret_access_key**  string | The secret access key.  A secret access key is the equivalent of a password which can not be changed and as such should be considered sensitive data.  Secret access keys can only be accessed at creation time.  **Returned:** When a new key is created.  **Sample:** `"example/Example+EXAMPLE+example/Example"` |

### Authors

- Mark Chappell (@tremble)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
