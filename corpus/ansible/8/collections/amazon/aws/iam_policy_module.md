---
collection: ansible
version: "8"
title: "amazon.aws.iam_policy module – Manage inline IAM policies for users, groups, and roles"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/iam_policy_module.html
fetched_at: 2026-07-28T01:06:51+00:00
---
# amazon.aws.iam_policy module – Manage inline IAM policies for users, groups, and roles

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
> see [Requirements](iam_policy_module.md#ansible-collections-amazon-aws-iam-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.iam_policy`.

New in amazon.aws 5.0.0

- [Synopsis](iam_policy_module.md#synopsis)
- [Requirements](iam_policy_module.md#requirements)
- [Parameters](iam_policy_module.md#parameters)
- [Notes](iam_policy_module.md#notes)
- [Examples](iam_policy_module.md#examples)
- [Return Values](iam_policy_module.md#return-values)

## [Synopsis](iam_policy_module.md#id1)

- Allows uploading or removing inline IAM policies for IAM users, groups or roles.
- To administer managed policies please see [community.aws.iam_user](../../community/aws/iam_user_module.md#ansible-collections-community-aws-iam-user-module), [community.aws.iam_role](../../community/aws/iam_role_module.md#ansible-collections-community-aws-iam-role-module), [community.aws.iam_group](../../community/aws/iam_group_module.md#ansible-collections-community-aws-iam-group-module) and [community.aws.iam_managed_policy](../../community/aws/iam_managed_policy_module.md#ansible-collections-community-aws-iam-managed-policy-module)
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](iam_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](iam_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **iam_name**  string / required | Name of IAM resource you wish to target for policy actions. In other words, the user name, group name or role name. |
| **iam_type**  string / required | Type of IAM resource.  **Choices:**   - `"user"` - `"group"` - `"role"` |
| **policy_json**  json | A properly json formatted policy as string. |
| **policy_name**  string / required | The name label for the policy to create or remove. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **skip_duplicates**  boolean | When *skip_duplicates=true* the module looks for any policies that match the document you pass in. If there is a match it will not make a new policy object with the same rules.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Whether to create or delete the IAM policy.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](iam_policy_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](iam_policy_module.md#id5)

```yaml+jinja
# Advanced example, create two new groups and add a READ-ONLY policy to both
# groups.
- name: Create Two Groups, Mario and Luigi
  community.aws.iam_group:
    name: "{{ item }}"
    state: present
  loop:
     - Mario
     - Luigi
  register: new_groups

- name: Apply READ-ONLY policy to new groups that have been recently created
  amazon.aws.iam_policy:
    iam_type: group
    iam_name: "{{ item.iam_group.group.group_name }}"
    policy_name: "READ-ONLY"
    policy_json: "{{ lookup('template', 'readonly.json.j2') }}"
    state: present
  loop: "{{ new_groups.results }}"

# Create a new S3 policy with prefix per user
- name: Create S3 policy from template
  amazon.aws.iam_policy:
    iam_type: user
    iam_name: "{{ item.user }}"
    policy_name: "s3_limited_access_{{ item.prefix }}"
    state: present
    policy_json: "{{ lookup('template', 's3_policy.json.j2') }}"
    loop:
      - user: s3_user
        prefix: s3_user_prefix
```

## [Return Values](iam_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **policy_names**  list / elements=string | A list of names of the inline policies embedded in the specified IAM resource (user, group, or role).  **Returned:** always |

### Authors

- Jonathan I. Davila (@defionscode)
- Dennis Podkovyrin (@sbj-ss)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
