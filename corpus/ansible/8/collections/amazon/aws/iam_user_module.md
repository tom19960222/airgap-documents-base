---
collection: ansible
version: "8"
title: "amazon.aws.iam_user module – Manage AWS IAM users"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/iam_user_module.html
fetched_at: 2026-07-28T01:06:53+00:00
---
# amazon.aws.iam_user module – Manage AWS IAM users

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
> see [Requirements](iam_user_module.md#ansible-collections-amazon-aws-iam-user-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.iam_user`.

New in amazon.aws 5.0.0

- [Synopsis](iam_user_module.md#synopsis)
- [Requirements](iam_user_module.md#requirements)
- [Parameters](iam_user_module.md#parameters)
- [Notes](iam_user_module.md#notes)
- [Examples](iam_user_module.md#examples)
- [Return Values](iam_user_module.md#return-values)

## [Synopsis](iam_user_module.md#id1)

- A module to manage AWS IAM users.
- The module does not manage groups that users belong to, groups memberships can be managed using [community.aws.iam_group](../../community/aws/iam_group_module.md#ansible-collections-community-aws-iam-group-module).
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](iam_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](iam_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **managed_policies**  aliases: managed_policy  list / elements=string | A list of managed policy ARNs or friendly names to attach to the user.  To embed an inline policy, use [community.aws.iam_policy](../../community/aws/iam_policy_module.md#ansible-collections-community-aws-iam-policy-module).  **Default:** `[]` |
| **name**  string / required | The name of the user to create. |
| **password**  string  *added in community.aws 2.2.0* | The password to apply to the user. |
| **password_reset_required**  boolean  *added in community.aws 3.1.0* | Defines if the user is required to set a new password after login.  **Choices:**   - `false` ← (default) - `true` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_policies**  aliases: purge_policy, purge_managed_policies  boolean | When *purge_policies=true* any managed policies not listed in *managed_policies* will be detached.  **Choices:**   - `false` ← (default) - `true` |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **remove_password**  boolean  *added in community.aws 2.2.0* | Option to delete user login passwords.  This field is mutually exclusive to *password*.  **Choices:**   - `false` - `true` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string / required | Create or remove the IAM user.  **Choices:**   - `"present"` - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **update_password**  string  *added in community.aws 2.2.0* | When to update user passwords.  *update_password=always* will ensure the password is set to *password*.  *update_password=on_create* will only set the password for newly created users.  **Choices:**   - `"always"` ← (default) - `"on_create"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean  *added in community.aws 2.2.0* | When *wait=True* the module will wait for up to *wait_timeout* seconds for IAM user creation before returning.  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  integer  *added in community.aws 2.2.0* | How long (in seconds) to wait for creation / updates to complete.  **Default:** `120` |

## [Notes](iam_user_module.md#id4)

> **Note:**
>
> - Support for *tags* and *purge_tags* was added in release 2.1.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](iam_user_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.
# Note: This module does not allow management of groups that users belong to.
#       Groups should manage their membership directly using community.aws.iam_group,
#       as users belong to them.

- name: Create a user
  amazon.aws.iam_user:
    name: testuser1
    state: present

- name: Create a user with a password
  amazon.aws.iam_user:
    name: testuser1
    password: SomeSecurePassword
    state: present

- name: Create a user and attach a managed policy using its ARN
  amazon.aws.iam_user:
    name: testuser1
    managed_policies:
      - arn:aws:iam::aws:policy/AmazonSNSFullAccess
    state: present

- name: Remove all managed policies from an existing user with an empty list
  amazon.aws.iam_user:
    name: testuser1
    state: present
    purge_policies: true

- name: Create user with tags
  amazon.aws.iam_user:
    name: testuser1
    state: present
    tags:
      Env: Prod

- name: Delete the user
  amazon.aws.iam_user:
    name: testuser1
    state: absent
```

## [Return Values](iam_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **user**  complex | dictionary containing all the user information  **Returned:** success |
| **arn**  string | the Amazon Resource Name (ARN) specifying the user  **Returned:** success  **Sample:** `"arn:aws:iam::123456789012:user/testuser1"` |
| **create_date**  string | the date and time, in ISO 8601 date-time format, when the user was created  **Returned:** success  **Sample:** `"2017-02-08T04:36:28+00:00"` |
| **path**  string | the path to the user  **Returned:** success  **Sample:** `"/"` |
| **tags**  dictionary | user tags  **Returned:** always  **Sample:** `{"Env": "Prod"}` |
| **user_id**  string | the stable and unique string identifying the user  **Returned:** success  **Sample:** `"AGPA12345EXAMPLE54321"` |
| **user_name**  string | the friendly name that identifies the user  **Returned:** success  **Sample:** `"testuser1"` |

### Authors

- Josh Souza (@joshsouza)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
