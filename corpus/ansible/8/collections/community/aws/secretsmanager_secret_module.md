---
collection: ansible
version: "8"
title: "community.aws.secretsmanager_secret module – Manage secrets stored in AWS Secrets Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/secretsmanager_secret_module.html
fetched_at: 2026-07-28T01:41:52+00:00
---
# community.aws.secretsmanager_secret module – Manage secrets stored in AWS Secrets Manager

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
> see [Requirements](secretsmanager_secret_module.md#ansible-collections-community-aws-secretsmanager-secret-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.secretsmanager_secret`.

New in community.aws 1.0.0

- [Synopsis](secretsmanager_secret_module.md#synopsis)
- [Requirements](secretsmanager_secret_module.md#requirements)
- [Parameters](secretsmanager_secret_module.md#parameters)
- [Notes](secretsmanager_secret_module.md#notes)
- [Examples](secretsmanager_secret_module.md#examples)
- [Return Values](secretsmanager_secret_module.md#return-values)

## [Synopsis](secretsmanager_secret_module.md#id1)

- Create, update, and delete secrets stored in AWS Secrets Manager.
- Prior to release 5.0.0 this module was called `community.aws.aws_secret`. The usage did not change.

Aliases: aws_secret

## [Requirements](secretsmanager_secret_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](secretsmanager_secret_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | Specifies a user-provided description of the secret.  **Default:** `""` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **json_secret**  json  *added in community.aws 4.1.0* | Specifies JSON-formatted data that you want to encrypt and store in the new version of the secret.  Mutually exclusive with the *secret* option. |
| **kms_key_id**  string | Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the *secret* values in the versions stored in this secret. |
| **name**  string / required | Friendly name for the secret you are creating. |
| **overwrite**  boolean  *added in community.aws 5.3.0* | Whether to overwrite an existing secret with the same name.  If set to `True`, an existing secret with the same *name* will be overwritten.  If set to `False`, a secret with the given *name* will only be created if none exists.  **Choices:**   - `false` - `true` ← (default) |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **recovery_window**  integer | Only used if state is absent.  Specifies the number of days that Secrets Manager waits before it can delete the secret.  If set to 0, the deletion is forced without recovery.  **Default:** `30` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **replica**  list / elements=dictionary  *added in community.aws 5.3.0* | Specifies a list of regions and kms_key_ids (optional) to replicate the secret to |
| **kms_key_id**  string | Specifies the ARN or alias of the AWS KMS customer master key (CMK) in the destination region to be used (alias/aws/secretsmanager is assumed if not specified) |
| **region**  string / required | Region to replicate secret to. |
| **resource_policy**  json  *added in community.aws 3.1.0* | Specifies JSON-formatted resource policy to attach to the secret. Useful when granting cross-account access to secrets. |
| **rotation_interval**  integer | Specifies the number of days between automatic scheduled rotations of the secret.  **Default:** `30` |
| **rotation_lambda**  string | Specifies the ARN of the Lambda function that can rotate the secret. |
| **secret**  string | Specifies string or binary data that you want to encrypt and store in the new version of the secret.  Mutually exclusive with the *json_secret* option.  **Default:** `""` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_type**  string | Specifies the type of data that you want to encrypt.  **Choices:**   - `"binary"` - `"string"` ← (default) |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Whether the secret should be exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](secretsmanager_secret_module.md#id4)

> **Note:**
>
> - Support for *purge_tags* was added in release 4.0.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](secretsmanager_secret_module.md#id5)

```yaml+jinja
- name: Add string to AWS Secrets Manager
  community.aws.secretsmanager_secret:
    name: 'test_secret_string'
    state: present
    secret_type: 'string'
    secret: "{{ super_secret_string }}"

- name: Add a secret with resource policy attached
  community.aws.secretsmanager_secret:
    name: 'test_secret_string'
    state: present
    secret_type: 'string'
    secret: "{{ super_secret_string }}"
    resource_policy: "{{ lookup('template', 'templates/resource_policy.json.j2', convert_data=False) | string }}"

- name: remove string from AWS Secrets Manager
  community.aws.secretsmanager_secret:
    name: 'test_secret_string'
    state: absent
    secret_type: 'string'
    secret: "{{ super_secret_string }}"

- name: Only create a new secret, but do not update if alredy exists by name
  community.aws.secretsmanager_secret:
    name: 'random_string'
    state: present
    secret_type: 'string'
    secret: "{{ lookup('community.general.random_string', length=16, special=false) }}"
    overwrite: false
```

## [Return Values](secretsmanager_secret_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **secret**  complex | The secret information  **Returned:** always |
| **arn**  string | The ARN of the secret.  **Returned:** always  **Sample:** `"arn:aws:secretsmanager:eu-west-1:xxxxxxxxxx:secret:xxxxxxxxxxx"` |
| **description**  string | A description of the secret.  **Returned:** when the secret has a description  **Sample:** `"An example description"` |
| **last_accessed_date**  string | The date the secret was last accessed.  **Returned:** always  **Sample:** `"2018-11-20T01:00:00+01:00"` |
| **last_changed_date**  string | The date the secret was last modified.  **Returned:** always  **Sample:** `"2018-11-20T12:16:38.433000+01:00"` |
| **name**  string | The secret name.  **Returned:** always  **Sample:** `"my_secret"` |
| **rotation_enabled**  boolean | The secret rotation status.  **Returned:** always  **Sample:** `false` |
| **tags**  list / elements=dictionary | A list of dictionaries representing the tags associated with the secret in the standard boto3 format.  **Returned:** when the secret has tags |
| **key**  string | The name or key of the tag.  **Returned:** success  **Sample:** `"MyTag"` |
| **value**  string | The value of the tag.  **Returned:** success  **Sample:** `"Some value."` |
| **tags_dict**  dictionary  *added in community.aws 4.0.0* | A dictionary representing the tags associated with the secret.  **Returned:** when the secret has tags  **Sample:** `{"MyTagName": "Some Value"}` |
| **version_ids_to_stages**  dictionary | Provide the secret version ids and the associated secret stage.  **Returned:** always  **Sample:** `{"dc1ed59b-6d8e-4450-8b41-536dfe4600a9": ["AWSCURRENT"]}` |

### Authors

- REY Remi (@rrey)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
