---
collection: ansible
version: "8"
title: "community.aws.ec2_snapshot_copy module – Copies an EC2 snapshot and returns the new Snapshot ID"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/ec2_snapshot_copy_module.html
fetched_at: 2026-07-28T01:40:43+00:00
---
# community.aws.ec2_snapshot_copy module – Copies an EC2 snapshot and returns the new Snapshot ID

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
> see [Requirements](ec2_snapshot_copy_module.md#ansible-collections-community-aws-ec2-snapshot-copy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_snapshot_copy`.

New in community.aws 1.0.0

- [Synopsis](ec2_snapshot_copy_module.md#synopsis)
- [Requirements](ec2_snapshot_copy_module.md#requirements)
- [Parameters](ec2_snapshot_copy_module.md#parameters)
- [Notes](ec2_snapshot_copy_module.md#notes)
- [Examples](ec2_snapshot_copy_module.md#examples)
- [Return Values](ec2_snapshot_copy_module.md#return-values)

## [Synopsis](ec2_snapshot_copy_module.md#id1)

- Copies an EC2 Snapshot from a source region to a destination region.

## [Requirements](ec2_snapshot_copy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_snapshot_copy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | An optional human-readable string describing purpose of the new Snapshot.  **Default:** `""` |
| **encrypted**  boolean | Whether or not the destination Snapshot should be encrypted.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **kms_key_id**  string | KMS key id used to encrypt snapshot. If not specified, AWS defaults to `alias/aws/ebs`. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **source_region**  string / required | The source region the Snapshot should be copied from. |
| **source_snapshot_id**  string / required | The ID of the Snapshot in source region that should be copied. |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the newly created resource. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Wait for the copied Snapshot to be in the `Available` state before returning.  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How long before wait gives up, in seconds.  **Default:** `600` |

## [Notes](ec2_snapshot_copy_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_snapshot_copy_module.md#id5)

```yaml+jinja
- name: Basic Snapshot Copy
  community.aws.ec2_snapshot_copy:
    source_region: eu-central-1
    region: eu-west-1
    source_snapshot_id: snap-xxxxxxx

- name: Copy Snapshot and wait until available
  community.aws.ec2_snapshot_copy:
    source_region: eu-central-1
    region: eu-west-1
    source_snapshot_id: snap-xxxxxxx
    wait: true
    wait_timeout: 1200   # Default timeout is 600
  register: snapshot_id

- name: Tagged Snapshot copy
  community.aws.ec2_snapshot_copy:
    source_region: eu-central-1
    region: eu-west-1
    source_snapshot_id: snap-xxxxxxx
    tags:
        Name: Snapshot-Name

- name: Encrypted Snapshot copy
  community.aws.ec2_snapshot_copy:
    source_region: eu-central-1
    region: eu-west-1
    source_snapshot_id: snap-xxxxxxx
    encrypted: true

- name: Encrypted Snapshot copy with specified key
  community.aws.ec2_snapshot_copy:
    source_region: eu-central-1
    region: eu-west-1
    source_snapshot_id: snap-xxxxxxx
    encrypted: true
    kms_key_id: arn:aws:kms:eu-central-1:XXXXXXXXXXXX:key/746de6ea-50a4-4bcb-8fbc-e3b29f2d367b
```

## [Return Values](ec2_snapshot_copy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **snapshot_id**  string | snapshot id of the newly created snapshot  **Returned:** when snapshot copy is successful  **Sample:** `"snap-e9095e8c"` |

### Authors

- Deepak Kothandan (@Deepakkothandan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
