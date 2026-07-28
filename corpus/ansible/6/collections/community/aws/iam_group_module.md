---
collection: ansible
version: "6"
title: "community.aws.iam_group module – Manage AWS IAM groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/iam_group_module.html
fetched_at: 2026-07-27T17:04:35+00:00
---
# community.aws.iam_group module – Manage AWS IAM groups

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
> see [Requirements](iam_group_module.md#ansible-collections-community-aws-iam-group-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.iam_group`.

New in community.aws 1.0.0

- [Synopsis](iam_group_module.md#synopsis)
- [Requirements](iam_group_module.md#requirements)
- [Parameters](iam_group_module.md#parameters)
- [Notes](iam_group_module.md#notes)
- [Examples](iam_group_module.md#examples)
- [Return Values](iam_group_module.md#return-values)

## [Synopsis](iam_group_module.md#id1)

- Manage AWS IAM groups.

## [Requirements](iam_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](iam_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **managed_policies**  aliases: managed_policy  list / elements=string | A list of managed policy ARNs or friendly names to attach to the role.  To embed an inline policy, use [community.aws.iam_policy](iam_policy_module.md#ansible-collections-community-aws-iam-policy-module). |
| **name**  string / required | The name of the group to create. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_policies**  aliases: purge_policy, purge_managed_policies  boolean | When *purge_policies=true* any managed policies not listed in *managed_policies* will be detatched.  Choices:   - `false` ← (default) - `true` |
| **purge_users**  boolean | When *purge_users=true* users which are not included in *users* will be detached.  Choices:   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string / required | Create or remove the IAM group.  Choices:   - `"present"` - `"absent"` |
| **users**  list / elements=string | A list of existing users to add as members of the group. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](iam_group_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](iam_group_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Create a group
  community.aws.iam_group:
    name: testgroup1
    state: present

- name: Create a group and attach a managed policy using its ARN
  community.aws.iam_group:
    name: testgroup1
    managed_policies:
      - arn:aws:iam::aws:policy/AmazonSNSFullAccess
    state: present

- name: Create a group with users as members and attach a managed policy using its ARN
  community.aws.iam_group:
    name: testgroup1
    managed_policies:
      - arn:aws:iam::aws:policy/AmazonSNSFullAccess
    users:
      - test_user1
      - test_user2
    state: present

- name: Remove all managed policies from an existing group with an empty list
  community.aws.iam_group:
    name: testgroup1
    state: present
    purge_policies: true

- name: Remove all group members from an existing group
  community.aws.iam_group:
    name: testgroup1
    managed_policies:
      - arn:aws:iam::aws:policy/AmazonSNSFullAccess
    purge_users: true
    state: present

- name: Delete the group
  community.aws.iam_group:
    name: testgroup1
    state: absent
```

## [Return Values](iam_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **iam_group**  complex | dictionary containing all the group information including group membership  Returned: success |
| **group**  complex | dictionary containing all the group information  Returned: success |
| **arn**  string | the Amazon Resource Name (ARN) specifying the group  Returned: success  Sample: `"arn:aws:iam::1234567890:group/testgroup1"` |
| **create_date**  string | the date and time, in ISO 8601 date-time format, when the group was created  Returned: success  Sample: `"2017-02-08T04:36:28+00:00"` |
| **group_id**  string | the stable and unique string identifying the group  Returned: success  Sample: `"AGPAIDBWE12NSFINE55TM"` |
| **group_name**  string | the friendly name that identifies the group  Returned: success  Sample: `"testgroup1"` |
| **path**  string | the path to the group  Returned: success  Sample: `"/"` |
| **users**  complex | list containing all the group members  Returned: success |
| **arn**  string | the Amazon Resource Name (ARN) specifying the user  Returned: success  Sample: `"arn:aws:iam::1234567890:user/test_user1"` |
| **create_date**  string | the date and time, in ISO 8601 date-time format, when the user was created  Returned: success  Sample: `"2017-02-08T04:36:28+00:00"` |
| **path**  string | the path to the user  Returned: success  Sample: `"/"` |
| **user_id**  string | the stable and unique string identifying the user  Returned: success  Sample: `"AIDAIZTPY123YQRS22YU2"` |
| **user_name**  string | the friendly name that identifies the user  Returned: success  Sample: `"testgroup1"` |

### Authors

- Nick Aslanidis (@naslanidis)
- Maksym Postument (@infectsoldier)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
