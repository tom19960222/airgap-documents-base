---
collection: ansible
version: "6"
title: "community.aws.aws_kms_info module – Gather information about AWS KMS keys"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_kms_info_module.html
fetched_at: 2026-07-27T17:03:28+00:00
---
# community.aws.aws_kms_info module – Gather information about AWS KMS keys

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
> see [Requirements](aws_kms_info_module.md#ansible-collections-community-aws-aws-kms-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_kms_info`.

New in community.aws 1.0.0

- [Synopsis](aws_kms_info_module.md#synopsis)
- [Requirements](aws_kms_info_module.md#requirements)
- [Parameters](aws_kms_info_module.md#parameters)
- [Notes](aws_kms_info_module.md#notes)
- [Examples](aws_kms_info_module.md#examples)
- [Return Values](aws_kms_info_module.md#return-values)

## [Synopsis](aws_kms_info_module.md#id1)

- Gather information about AWS KMS keys including tags and grants

## [Requirements](aws_kms_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_kms_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alias**  aliases: key_alias  string  added in community.aws 1.4.0 | Alias for key.  Mutually exclusive with *key_id* and *filters*. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **filters**  dictionary | A dict of filters to apply. Each dict item consists of a filter key and a filter value. The filters aren’t natively supported by boto3, but are supported to provide similar functionality to other modules. Standard tag filters (`tag-key`, `tag-value` and `tag:tagName`) are available, as are `key-id` and `alias`  Mutually exclusive with *alias* and *key_id*. |
| **key_id**  aliases: key_arn  string  added in community.aws 1.4.0 | Key ID or ARN of the key.  Mutually exclusive with *alias* and *filters*. |
| **keys_attr**  boolean  added in community.aws 2.0.0 | Returning the `keys` attribute conflicted with the builtin keys() method on dictionaries and as such was deprecated.  This parameter now does nothing, and after version `4.0.0` this parameter will be removed.  Choices:   - `false` - `true` |
| **pending_deletion**  boolean | Whether to get full details (tags, grants etc.) of keys pending deletion  Choices:   - `false` ← (default) - `true` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](aws_kms_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_kms_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Gather information about all KMS keys
- community.aws.aws_kms_info:

# Gather information about all keys with a Name tag
- community.aws.aws_kms_info:
    filters:
      tag-key: Name

# Gather information about all keys with a specific name
- community.aws.aws_kms_info:
    filters:
      "tag:Name": Example
```

## [Return Values](aws_kms_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **kms_keys**  complex | list of keys  Returned: always |
| **aliases**  list / elements=string | list of aliases associated with the key  Returned: always  Sample: `["aws/acm", "aws/ebs"]` |
| **aws_account_id**  string | The AWS Account ID that the key belongs to  Returned: always  Sample: `"1234567890123"` |
| **creation_date**  string | Date of creation of the key  Returned: always  Sample: `"2017-04-18T15:12:08.551000+10:00"` |
| **description**  string | Description of the key  Returned: always  Sample: `"My Key for Protecting important stuff"` |
| **enable_key_rotation**  boolean | Whether the automatically key rotation every year is enabled. Returns None if key rotation status can’t be determined.  Returned: always  Sample: `false` |
| **enabled**  string | Whether the key is enabled. True if `KeyState` is true.  Returned: always  Sample: `"False"` |
| **grants**  complex | list of grants associated with a key  Returned: always |
| **constraints**  dictionary | Constraints on the encryption context that the grant allows. See <https://docs.aws.amazon.com/kms/latest/APIReference/API_GrantConstraints.html> for further details  Returned: always  Sample: `{"encryption_context_equals": {"aws:lambda:_function_arn": "arn:aws:lambda:ap-southeast-2:012345678912:function:xyz"}}` |
| **creation_date**  string | Date of creation of the grant  Returned: always  Sample: `"2017-04-18T15:12:08+10:00"` |
| **grant_id**  string | The unique ID for the grant  Returned: always  Sample: `"abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234"` |
| **grantee_principal**  string | The principal that receives the grant’s permissions  Returned: always  Sample: `"arn:aws:sts::0123456789012:assumed-role/lambda_xyz/xyz"` |
| **issuing_account**  string | The AWS account under which the grant was issued  Returned: always  Sample: `"arn:aws:iam::01234567890:root"` |
| **key_id**  string | The key ARN to which the grant applies.  Returned: always  Sample: `"arn:aws:kms:ap-southeast-2:123456789012:key/abcd1234-abcd-1234-5678-ef1234567890"` |
| **name**  string | The friendly name that identifies the grant  Returned: always  Sample: `"xyz"` |
| **operations**  list / elements=string | The list of operations permitted by the grant  Returned: always  Sample: `["Decrypt", "RetireGrant"]` |
| **retiring_principal**  string | The principal that can retire the grant  Returned: always  Sample: `"arn:aws:sts::0123456789012:assumed-role/lambda_xyz/xyz"` |
| **key_arn**  string | ARN of key  Returned: always  Sample: `"arn:aws:kms:ap-southeast-2:123456789012:key/abcd1234-abcd-1234-5678-ef1234567890"` |
| **key_id**  string | ID of key  Returned: always  Sample: `"abcd1234-abcd-1234-5678-ef1234567890"` |
| **key_policies**  list / elements=dictionary  added in community.aws 3.3.0 | list of policy documents for the key. Empty when access is denied even if there are policies.  Returned: always  Sample: `{"Id": "auto-ebs-2", "Statement": [{"Action": ["kms:Encrypt", "kms:Decrypt", "kms:ReEncrypt*", "kms:GenerateDataKey*", "kms:CreateGrant", "kms:DescribeKey"], "Condition": {"StringEquals": {"kms:CallerAccount": "111111111111", "kms:ViaService": "ec2.ap-southeast-2.amazonaws.com"}}, "Effect": "Allow", "Principal": {"AWS": "*"}, "Resource": "*", "Sid": "Allow access through EBS for all principals in the account that are authorized to use EBS"}, {"Action": ["kms:Describe*", "kms:Get*", "kms:List*", "kms:RevokeGrant"], "Effect": "Allow", "Principal": {"AWS": "arn:aws:iam::111111111111:root"}, "Resource": "*", "Sid": "Allow direct access to key metadata to the account"}], "Version": "2012-10-17"}` |
| **key_state**  string | The state of the key  Returned: always  Sample: `"PendingDeletion"` |
| **key_usage**  string | The cryptographic operations for which you can use the key.  Returned: always  Sample: `"ENCRYPT_DECRYPT"` |
| **origin**  string | The source of the key’s key material. When this value is `AWS_KMS`, AWS KMS created the key material. When this value is `EXTERNAL`, the key material was imported or the CMK lacks key material.  Returned: always  Sample: `"AWS_KMS"` |
| **policies**  list / elements=string | list of policy documents for the key. Empty when access is denied even if there are policies.  Returned: always  Sample: `{"Id": "auto-ebs-2", "Statement": [{"Action": ["kms:Encrypt", "kms:Decrypt", "kms:ReEncrypt*", "kms:GenerateDataKey*", "kms:CreateGrant", "kms:DescribeKey"], "Condition": {"StringEquals": {"kms:CallerAccount": "111111111111", "kms:ViaService": "ec2.ap-southeast-2.amazonaws.com"}}, "Effect": "Allow", "Principal": {"AWS": "*"}, "Resource": "*", "Sid": "Allow access through EBS for all principals in the account that are authorized to use EBS"}, {"Action": ["kms:Describe*", "kms:Get*", "kms:List*", "kms:RevokeGrant"], "Effect": "Allow", "Principal": {"AWS": "arn:aws:iam::111111111111:root"}, "Resource": "*", "Sid": "Allow direct access to key metadata to the account"}], "Version": "2012-10-17"}` |
| **tags**  dictionary | dictionary of tags applied to the key. Empty when access is denied even if there are tags.  Returned: always  Sample: `{"Name": "myKey", "Purpose": "protecting_stuff"}` |

### Authors

- Will Thames (@willthames)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
