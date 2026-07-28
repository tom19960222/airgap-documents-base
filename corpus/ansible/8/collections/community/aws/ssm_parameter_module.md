---
collection: ansible
version: "8"
title: "community.aws.ssm_parameter module – Manage key-value pairs in AWS Systems Manager Parameter Store"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/ssm_parameter_module.html
fetched_at: 2026-07-28T01:41:59+00:00
---
# community.aws.ssm_parameter module – Manage key-value pairs in AWS Systems Manager Parameter Store

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
> see [Requirements](ssm_parameter_module.md#ansible-collections-community-aws-ssm-parameter-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ssm_parameter`.

New in community.aws 1.0.0

- [Synopsis](ssm_parameter_module.md#synopsis)
- [Requirements](ssm_parameter_module.md#requirements)
- [Parameters](ssm_parameter_module.md#parameters)
- [Notes](ssm_parameter_module.md#notes)
- [See Also](ssm_parameter_module.md#see-also)
- [Examples](ssm_parameter_module.md#examples)
- [Return Values](ssm_parameter_module.md#return-values)

## [Synopsis](ssm_parameter_module.md#id1)

- Manage key-value pairs in AWS Systems Manager (SSM) Parameter Store.
- Prior to release 5.0.0 this module was called `community.aws.aws_ssm_parameter_store`. The usage did not change.

Aliases: aws_ssm_parameter_store

## [Requirements](ssm_parameter_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ssm_parameter_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **decryption**  boolean | Work with SecureString type to get plain text secrets  **Choices:**   - `false` - `true` ← (default) |
| **description**  string | Parameter key description. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **key_id**  string | AWS KMS key to decrypt the secrets.  The default key (`alias/aws/ssm`) is automatically generated the first time it’s requested.  **Default:** `"alias/aws/ssm"` |
| **name**  string / required | Parameter key name. |
| **overwrite_value**  string | Option to overwrite an existing value if it already exists.  **Choices:**   - `"never"` - `"changed"` ← (default) - `"always"` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Creates or modifies an existing parameter.  Deletes a parameter.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **string_type**  aliases: type  string | Parameter String type.  **Choices:**   - `"String"` ← (default) - `"StringList"` - `"SecureString"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **tier**  string  *added in community.aws 1.5.0* | Parameter store tier type.  **Choices:**   - `"Standard"` ← (default) - `"Advanced"` - `"Intelligent-Tiering"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **value**  string | Parameter value. |

## [Notes](ssm_parameter_module.md#id4)

> **Note:**
>
> - Support for *tags* and *purge_tags* was added in release 5.3.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [See Also](ssm_parameter_module.md#id5)

> **See also:**
>
> [amazon.aws.aws_ssm lookup](../../amazon/aws/aws_ssm_lookup.md#ansible-collections-amazon-aws-aws-ssm-lookup)
> :   The documentation for the `amazon.aws.aws_ssm` lookup plugin.

## [Examples](ssm_parameter_module.md#id6)

```yaml+jinja
- name: Create or update key/value pair in AWS SSM parameter store
  community.aws.ssm_parameter:
    name: "Hello"
    description: "This is your first key"
    value: "World"

- name: Delete the key
  community.aws.ssm_parameter:
    name: "Hello"
    state: absent

- name: Create or update secure key/value pair with default KMS key (aws/ssm)
  community.aws.ssm_parameter:
    name: "Hello"
    description: "This is your first key"
    string_type: "SecureString"
    value: "World"

- name: Create or update secure key/value pair with nominated KMS key
  community.aws.ssm_parameter:
    name: "Hello"
    description: "This is your first key"
    string_type: "SecureString"
    key_id: "alias/demo"
    value: "World"

- name: Always update a parameter store value and create a new version
  community.aws.ssm_parameter:
    name: "overwrite_example"
    description: "This example will always overwrite the value"
    string_type: "String"
    value: "Test1234"
    overwrite_value: "always"

- name: Create or update key/value pair in AWS SSM parameter store with tier
  community.aws.ssm_parameter:
    name: "Hello"
    description: "This is your first key"
    value: "World"
    tier: "Advanced"

- name: recommend to use with aws_ssm lookup plugin
  ansible.builtin.debug:
    msg: "{{ lookup('amazon.aws.aws_ssm', 'Hello') }}"

- name: Create or update key/value pair in AWS SSM parameter store w/ tags
  community.aws.ssm_parameter:
    name: "Hello"
    description: "This is your first key"
    value: "World"
    tags:
      Environment: "dev"
      Version: "1.0"
      Confidentiality: "low"
      Tag With Space: "foo bar"

- name: Add or update a tag on an existing parameter w/o removing existing tags
  community.aws.ssm_parameter:
    name: "Hello"
    purge_tags: false
    tags:
      Contact: "person1"

- name: Delete all tags on an existing parameter
  community.aws.ssm_parameter:
    name: "Hello"
    tags: {}
```

## [Return Values](ssm_parameter_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **parameter_metadata**  dictionary | Information about a parameter.  Does not include the value of the parameter as this can be sensitive information.  **Returned:** success |
| **data_type**  string | Parameter Data type.  **Returned:** success  **Sample:** `"text"` |
| **description**  string | Parameter key description.  **Returned:** success  **Sample:** `"This is your first key"` |
| **last_modified_date**  string | Time and date that the parameter was last modified.  **Returned:** success  **Sample:** `"2022-06-20T09:56:58.573000+00:00"` |
| **last_modified_user**  string | ARN of the last user to modify the parameter.  **Returned:** success  **Sample:** `"arn:aws:sts::123456789012:assumed-role/example-role/session=example"` |
| **name**  string | Parameter key name.  **Returned:** success  **Sample:** `"Hello"` |
| **policies**  list / elements=dictionary | A list of policies associated with a parameter.  **Returned:** success |
| **policy_status**  string | The status of the policy.  **Returned:** success  **Sample:** `"Pending"` |
| **policy_text**  string | The JSON text of the policy.  **Returned:** success |
| **policy_type**  string | The type of policy.  **Returned:** success  **Sample:** `"Expiration"` |
| **tags**  dictionary  *added in community.aws 5.3.0* | A dictionary representing the tags associated with the parameter.  **Returned:** when the parameter has tags  **Sample:** `{"MyTagName": "Some Value"}` |
| **tier**  string | Parameter tier.  **Returned:** success  **Sample:** `"Standard"` |
| **type**  string | Parameter type  **Returned:** success  **Sample:** `"String"` |
| **version**  integer | Parameter version number  **Returned:** success  **Sample:** `3` |

### Authors

- Davinder Pal (@116davinder)
- Nathan Webster (@nathanwebsterdotme)
- Bill Wang (@ozbillwang)
- Michael De La Rue (@mikedlr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
