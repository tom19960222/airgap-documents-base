---
collection: ansible
version: "6"
title: "community.aws.iam_policy module – Manage inline IAM policies for users, groups, and roles"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/iam_policy_module.html
fetched_at: 2026-07-27T17:04:38+00:00
---
# community.aws.iam_policy module – Manage inline IAM policies for users, groups, and roles

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
> see [Requirements](iam_policy_module.md#ansible-collections-community-aws-iam-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.iam_policy`.

New in community.aws 1.0.0

- [Synopsis](iam_policy_module.md#synopsis)
- [Requirements](iam_policy_module.md#requirements)
- [Parameters](iam_policy_module.md#parameters)
- [Notes](iam_policy_module.md#notes)
- [Examples](iam_policy_module.md#examples)
- [Return Values](iam_policy_module.md#return-values)

## [Synopsis](iam_policy_module.md#id1)

- Allows uploading or removing inline IAM policies for IAM users, groups or roles.
- To administer managed policies please see [community.aws.iam_user](iam_user_module.md#ansible-collections-community-aws-iam-user-module), [community.aws.iam_role](iam_role_module.md#ansible-collections-community-aws-iam-role-module), [community.aws.iam_group](iam_group_module.md#ansible-collections-community-aws-iam-group-module) and [community.aws.iam_managed_policy](iam_managed_policy_module.md#ansible-collections-community-aws-iam-managed-policy-module)

## [Requirements](iam_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](iam_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **iam_name**  string / required | Name of IAM resource you wish to target for policy actions. In other words, the user name, group name or role name. |
| **iam_type**  string / required | Type of IAM resource.  Choices:   - `"user"` - `"group"` - `"role"` |
| **policy_document**  string | The path to the properly json formatted policy file.  Mutually exclusive with *policy_json*.  This option has been deprecated and will be removed in a release after 2022-06-01. The existing behavior can be reproduced by using the *policy_json* option and reading the file using the lookup plugin. |
| **policy_json**  json | A properly json formatted policy as string.  Mutually exclusive with *policy_document*.  See <https://github.com/ansible/ansible/issues/7005#issuecomment-42894813> on how to use it properly. |
| **policy_name**  string / required | The name label for the policy to create or remove. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **skip_duplicates**  boolean | When *skip_duplicates=true* the module looks for any policies that match the document you pass in. If there is a match it will not make a new policy object with the same rules.  The current default is `true`. However, this behavior can be confusing and as such the default will change to `false` in a release after 2022-06-01. To maintain the existing behavior explicitly set *skip_duplicates=true*.  Choices:   - `false` - `true` |
| **state**  string | Whether to create or delete the IAM policy.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](iam_policy_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](iam_policy_module.md#id5)

```yaml+jinja
# Create a policy with the name of 'Admin' to the group 'administrators'
- name: Assign a policy called Admin to the administrators group
  community.aws.iam_policy:
    iam_type: group
    iam_name: administrators
    policy_name: Admin
    state: present
    policy_document: admin_policy.json

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
  community.aws.iam_policy:
    iam_type: group
    iam_name: "{{ item.iam_group.group.group_name }}"
    policy_name: "READ-ONLY"
    policy_json: "{{ lookup('template', 'readonly.json.j2') }}"
    state: present
  loop: "{{ new_groups.results }}"

# Create a new S3 policy with prefix per user
- name: Create S3 policy from template
  community.aws.iam_policy:
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
| **policies**  list / elements=string | A list of names of the inline policies embedded in the specified IAM resource (user, group, or role).  Returned: always |

### Authors

- Jonathan I. Davila (@defionscode)
- Dennis Podkovyrin (@sbj-ss)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
