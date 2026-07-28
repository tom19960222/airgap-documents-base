---
collection: ansible
version: "8"
title: "amazon.aws.kms_key module – Perform various KMS key management tasks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/kms_key_module.html
fetched_at: 2026-07-28T01:06:54+00:00
---
# amazon.aws.kms_key module – Perform various KMS key management tasks

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
> see [Requirements](kms_key_module.md#ansible-collections-amazon-aws-kms-key-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.kms_key`.

New in amazon.aws 5.0.0

- [Synopsis](kms_key_module.md#synopsis)
- [Requirements](kms_key_module.md#requirements)
- [Parameters](kms_key_module.md#parameters)
- [Notes](kms_key_module.md#notes)
- [Examples](kms_key_module.md#examples)
- [Return Values](kms_key_module.md#return-values)

## [Synopsis](kms_key_module.md#id1)

- Manage role/user access to a KMS key.
- Not designed for encrypting/decrypting.
- Prior to release 5.0.0 this module was called `community.aws.aws_kms`. The usage did not change.
- This module was originally added to `community.aws` in release 1.0.0.

Aliases: aws_kms

## [Requirements](kms_key_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](kms_key_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **alias**  aliases: key_alias  string | An alias for a key.  For safety, even though KMS does not require keys to have an alias, this module expects all new keys to be given an alias to make them easier to manage. Existing keys without an alias may be referred to by *key_id*. Use [amazon.aws.kms_key_info](kms_key_info_module.md#ansible-collections-amazon-aws-kms-key-info-module) to find key ids.  Note that passing a *key_id* and *alias* will only cause a new alias to be added, an alias will never be renamed.  The `alias/` prefix is optional.  Required if *key_id* is not given. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | A description of the CMK.  Use a description that helps you decide whether the CMK is appropriate for a task. |
| **enable_key_rotation**  boolean | Whether the key should be automatically rotated every year.  **Choices:**   - `false` - `true` |
| **enabled**  boolean | Whether or not a key is enabled.  **Choices:**   - `false` - `true` ← (default) |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **grants**  list / elements=dictionary | A list of grants to apply to the key. Each item must contain *grantee_principal*. Each item can optionally contain *retiring_principal*, *operations*, *constraints*, *name*.  *grantee_principal* and *retiring_principal* must be ARNs  For full documentation of suboptions see the boto3 documentation:  <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.create_grant>  **Default:** `[]` |
| **constraints**  dictionary | Constraints is a dict containing `encryption_context_subset` or `encryption_context_equals`, either or both being a dict specifying an encryption context match. See <https://docs.aws.amazon.com/kms/latest/APIReference/API_GrantConstraints.html> or <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.create_grant> |
| **grantee_principal**  string / required | The full ARN of the principal being granted permissions. |
| **operations**  list / elements=string | A list of operations that the grantee may perform using the CMK.  **Choices:**   - `"Decrypt"` - `"Encrypt"` - `"GenerateDataKey"` - `"GenerateDataKeyWithoutPlaintext"` - `"ReEncryptFrom"` - `"ReEncryptTo"` - `"CreateGrant"` - `"RetireGrant"` - `"DescribeKey"` - `"Verify"` - `"Sign"` |
| **retiring_principal**  string | The full ARN of the principal permitted to revoke/retire the grant. |
| **key_id**  aliases: key_arn  string | Key ID or ARN of the key.  One of *alias* or *key_id* are required. |
| **key_spec**  aliases: customer_master_key_spec  string  *added in community.aws 2.1.0* | Specifies the type of KMS key to create.  The specification is not changeable once the key is created.  **Choices:**   - `"SYMMETRIC_DEFAULT"` ← (default) - `"RSA_2048"` - `"RSA_3072"` - `"RSA_4096"` - `"ECC_NIST_P256"` - `"ECC_NIST_P384"` - `"ECC_NIST_P521"` - `"ECC_SECG_P256K1"` |
| **key_usage**  string  *added in community.aws 2.1.0* | Determines the cryptographic operations for which you can use the KMS key.  The usage is not changeable once the key is created.  **Choices:**   - `"ENCRYPT_DECRYPT"` ← (default) - `"SIGN_VERIFY"` |
| **multi_region**  boolean  *added in amazon.aws 5.5.0* | Whether to create a multi-Region primary key or not.  **Choices:**   - `false` ← (default) - `true` |
| **pending_window**  aliases: deletion_delay  integer  *added in community.aws 1.4.0* | The number of days between requesting deletion of the CMK and when it will actually be deleted.  Only used when *state=absent* and the CMK has not yet been deleted.  Valid values are between 7 and 30 (inclusive).  See also: <https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html#KMS-ScheduleKeyDeletion-request-PendingWindowInDays> |
| **policy**  json | policy to apply to the KMS key.  See <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html> |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_grants**  boolean | Whether the *grants* argument should cause grants not in the list to be removed.  **Choices:**   - `false` ← (default) - `true` |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Whether a key should be present or absent.  Note that making an existing key `absent` only schedules a key for deletion.  Passing a key that is scheduled for deletion with *state=present* will cancel key deletion.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](kms_key_module.md#id4)

> **Note:**
>
> - There are known inconsistencies in the amount of time required for updates of KMS keys to be fully reflected on AWS. This can cause issues when running duplicate tasks in succession or using the [amazon.aws.kms_key_info](kms_key_info_module.md#ansible-collections-amazon-aws-kms-key-info-module) module to fetch key metadata shortly after modifying keys. For this reason, it is recommended to use the return data from this module ([amazon.aws.kms_key](kms_key_module.md#ansible-collections-amazon-aws-kms-key-module)) to fetch a key’s metadata.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](kms_key_module.md#id5)

```yaml+jinja
# Create a new KMS key
- amazon.aws.kms_key:
    alias: mykey
    tags:
      Name: myKey
      Purpose: protect_stuff

# Create a new multi-region KMS key
- amazon.aws.kms_key:
    alias: mykey
    multi_region: true
    tags:
      Name: myKey
      Purpose: protect_stuff

# Update previous key with more tags
- amazon.aws.kms_key:
    alias: mykey
    tags:
      Name: myKey
      Purpose: protect_stuff
      Owner: security_team

# Update a known key with grants allowing an instance with the billing-prod IAM profile
# to decrypt data encrypted with the environment: production, application: billing
# encryption context
- amazon.aws.kms_key:
    key_id: abcd1234-abcd-1234-5678-ef1234567890
    grants:
      - name: billing_prod
        grantee_principal: arn:aws:iam::123456789012:role/billing_prod
        constraints:
          encryption_context_equals:
            environment: production
            application: billing
        operations:
          - Decrypt
          - RetireGrant

- name: Update IAM policy on an existing KMS key
  amazon.aws.kms_key:
    alias: my-kms-key
    policy: '{"Version": "2012-10-17", "Id": "my-kms-key-permissions", "Statement": [ { <SOME STATEMENT> } ]}'
    state: present

- name: Example using lookup for policy json
  amazon.aws.kms_key:
    alias: my-kms-key
    policy: "{{ lookup('template', 'kms_iam_policy_template.json.j2') }}"
    state: present
```

## [Return Values](kms_key_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **aliases**  list / elements=string | List of aliases associated with the key.  **Returned:** always  **Sample:** `["aws/acm", "aws/ebs"]` |
| **aws_account_id**  string | The AWS Account ID that the key belongs to.  **Returned:** always  **Sample:** `"1234567890123"` |
| **changes_needed**  dictionary | Grant types that would be changed/were changed.  **Returned:** always  **Sample:** `{"role": "add", "role grant": "add"}` |
| **creation_date**  string | Date and time of creation of the key.  **Returned:** always  **Sample:** `"2017-04-18T15:12:08.551000+10:00"` |
| **deletion_date**  string  *added in community.aws 3.3.0* | Date and time after which KMS deletes this KMS key.  **Returned:** when key_state is PendingDeletion  **Sample:** `"2017-04-18T15:12:08.551000+10:00"` |
| **description**  string | Description of the key.  **Returned:** always  **Sample:** `"My Key for Protecting important stuff"` |
| **enable_key_rotation**  boolean | Whether the automatic annual key rotation is enabled. Returns None if key rotation status can’t be determined.  **Returned:** always  **Sample:** `false` |
| **enabled**  boolean | Whether the key is enabled. True if *key_state* is `Enabled`.  **Returned:** always  **Sample:** `false` |
| **grants**  list / elements=dictionary | List of grants associated with a key.  **Returned:** always |
| **constraints**  dictionary | Constraints on the encryption context that the grant allows. See <https://docs.aws.amazon.com/kms/latest/APIReference/API_GrantConstraints.html> for further details  **Returned:** always  **Sample:** `{"encryption_context_equals": {"aws:lambda:_function_arn": "arn:aws:lambda:ap-southeast-2:123456789012:function:xyz"}}` |
| **creation_date**  string | Date of creation of the grant.  **Returned:** always  **Sample:** `"2017-04-18T15:12:08+10:00"` |
| **grant_id**  string | The unique ID for the grant.  **Returned:** always  **Sample:** `"abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234"` |
| **grantee_principal**  string | The principal that receives the grant’s permissions.  **Returned:** always  **Sample:** `"arn:aws:sts::123456789012:assumed-role/lambda_xyz/xyz"` |
| **issuing_account**  string | The AWS account under which the grant was issued.  **Returned:** always  **Sample:** `"arn:aws:iam::123456789012:root"` |
| **key_id**  string | The key ARN to which the grant applies.  **Returned:** always  **Sample:** `"arn:aws:kms:ap-southeast-2:123456789012:key/abcd1234-abcd-1234-5678-ef1234567890"` |
| **name**  string | The friendly name that identifies the grant.  **Returned:** always  **Sample:** `"xyz"` |
| **operations**  list / elements=string | The list of operations permitted by the grant.  **Returned:** always  **Sample:** `["Decrypt", "RetireGrant"]` |
| **retiring_principal**  string | The principal that can retire the grant.  **Returned:** always  **Sample:** `"arn:aws:sts::123456789012:assumed-role/lambda_xyz/xyz"` |
| **had_invalid_entries**  boolean | Whether there are invalid (non-ARN) entries in the KMS entry. These don’t count as a change, but will be removed if any changes are being made.  **Returned:** always |
| **key_arn**  string | ARN of key.  **Returned:** always  **Sample:** `"arn:aws:kms:ap-southeast-2:123456789012:key/abcd1234-abcd-1234-5678-ef1234567890"` |
| **key_id**  string | ID of key.  **Returned:** always  **Sample:** `"abcd1234-abcd-1234-5678-ef1234567890"` |
| **key_policies**  list / elements=dictionary  *added in community.aws 3.3.0* | List of policy documents for the key. Empty when access is denied even if there are policies.  **Returned:** always  **Sample:** `{"Id": "auto-ebs-2", "Statement": [{"Action": ["kms:Encrypt", "kms:Decrypt", "kms:ReEncrypt*", "kms:GenerateDataKey*", "kms:CreateGrant", "kms:DescribeKey"], "Condition": {"StringEquals": {"kms:CallerAccount": "123456789012", "kms:ViaService": "ec2.ap-southeast-2.amazonaws.com"}}, "Effect": "Allow", "Principal": {"AWS": "*"}, "Resource": "*", "Sid": "Allow access through EBS for all principals in the account that are authorized to use EBS"}, {"Action": ["kms:Describe*", "kms:Get*", "kms:List*", "kms:RevokeGrant"], "Effect": "Allow", "Principal": {"AWS": "arn:aws:iam::123456789012:root"}, "Resource": "*", "Sid": "Allow direct access to key metadata to the account"}], "Version": "2012-10-17"}` |
| **key_state**  string | The state of the key.  Will be one of `'Creating'`, `'Enabled'`, `'Disabled'`, `'PendingDeletion'`, `'PendingImport'`, `'PendingReplicaDeletion'`, `'Unavailable'`, or `'Updating'`.  **Returned:** always  **Sample:** `"PendingDeletion"` |
| **key_usage**  string | The cryptographic operations for which you can use the key.  **Returned:** always  **Sample:** `"ENCRYPT_DECRYPT"` |
| **multi_region**  boolean  *added in amazon.aws 5.5.0* | Indicates whether the CMK is a multi-Region `True` or regional `False` key.  This value is True for multi-Region primary and replica CMKs and False for regional CMKs.  **Returned:** always  **Sample:** `false` |
| **origin**  string | The source of the key’s key material. When this value is `AWS_KMS`, AWS KMS created the key material. When this value is `EXTERNAL`, the key material was imported or the CMK lacks key material.  **Returned:** always  **Sample:** `"AWS_KMS"` |
| **policies**  list / elements=string | List of policy documents for the key. Empty when access is denied even if there are policies.  **Returned:** always  **Sample:** `{"Id": "auto-ebs-2", "Statement": [{"Action": ["kms:Encrypt", "kms:Decrypt", "kms:ReEncrypt*", "kms:GenerateDataKey*", "kms:CreateGrant", "kms:DescribeKey"], "Condition": {"StringEquals": {"kms:CallerAccount": "123456789012", "kms:ViaService": "ec2.ap-southeast-2.amazonaws.com"}}, "Effect": "Allow", "Principal": {"AWS": "*"}, "Resource": "*", "Sid": "Allow access through EBS for all principals in the account that are authorized to use EBS"}, {"Action": ["kms:Describe*", "kms:Get*", "kms:List*", "kms:RevokeGrant"], "Effect": "Allow", "Principal": {"AWS": "arn:aws:iam::123456789012:root"}, "Resource": "*", "Sid": "Allow direct access to key metadata to the account"}], "Version": "2012-10-17"}` |
| **tags**  dictionary | Dictionary of tags applied to the key. Empty when access is denied even if there are tags.  **Returned:** always  **Sample:** `{"Name": "myKey", "Purpose": "protecting_stuff"}` |

### Authors

- Ted Timmons (@tedder)
- Will Thames (@willthames)
- Mark Chappell (@tremble)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
