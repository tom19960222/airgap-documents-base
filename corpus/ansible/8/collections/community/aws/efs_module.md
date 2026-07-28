---
collection: ansible
version: "8"
title: "community.aws.efs module – create and maintain EFS file systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/efs_module.html
fetched_at: 2026-07-28T01:41:02+00:00
---
# community.aws.efs module – create and maintain EFS file systems

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
> see [Requirements](efs_module.md#ansible-collections-community-aws-efs-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.efs`.

New in community.aws 1.0.0

- [Synopsis](efs_module.md#synopsis)
- [Requirements](efs_module.md#requirements)
- [Parameters](efs_module.md#parameters)
- [Notes](efs_module.md#notes)
- [Examples](efs_module.md#examples)
- [Return Values](efs_module.md#return-values)

## [Synopsis](efs_module.md#id1)

- Module allows create, search and destroy Amazon EFS file systems.

## [Requirements](efs_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](efs_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **encrypt**  boolean | If *encrypt=true* creates an encrypted file system. This can not be modified after the file system is created.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **id**  string | ID of Amazon EFS. Either name or ID required for delete. |
| **kms_key_id**  string | The id of the AWS KMS CMK that will be used to protect the encrypted file system. This parameter is only required if you want to use a non-default CMK. If this parameter is not specified, the default CMK for Amazon EFS is used. The key id can be Key ID, Key ID ARN, Key Alias or Key Alias ARN. |
| **name**  string | Creation Token of Amazon EFS file system. Required for create and update. Either name or ID required for delete. |
| **performance_mode**  string | File system’s performance mode to use. Only takes effect during creation.  **Choices:**   - `"general_purpose"` ← (default) - `"max_io"` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **provisioned_throughput_in_mibps**  float | If the throughput_mode is provisioned, select the amount of throughput to provisioned in Mibps. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Allows to create, search and destroy Amazon EFS file system.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | List of tags of Amazon EFS. Should be defined as dictionary In case of ‘present’ state with list of tags and existing EFS (matched by ‘name’), tags of EFS will be replaced with provided data. |
| **targets**  list / elements=dictionary | List of mounted targets. It should be a list of dictionaries, every dictionary should include next attributes: This data may be modified for existing EFS using state ‘present’ and new list of mount targets.  **Default:** `[]` |
| **ip_address**  string | A valid IPv4 address within the address range of the specified subnet. |
| **security_groups**  list / elements=string | List of security group IDs, of the form ‘sg-xxxxxxxx’. These must be for the same VPC as subnet specified |
| **subnet_id**  string / required | The ID of the subnet to add the mount target in. |
| **throughput_mode**  string | The throughput_mode for the file system to be created.  **Choices:**   - `"bursting"` - `"provisioned"` |
| **transition_to_ia**  string  *added in community.aws 2.1.0* | How many days before objects transition to the lower-cost EFS Infrequent Access (IA) storage class.  If set to the string `None`, any existing lifecyle policy will be removed, and objects will not transition to an IA storage class.  If this parameter is absent, any existing lifecycle policy will not be affected.  **Choices:**   - `"None"` - `"7"` - `"14"` - `"30"` - `"60"` - `"90"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | In case of ‘present’ state should wait for EFS ‘available’ life cycle state (of course, if current state not ‘deleting’ or ‘deleted’) In case of ‘absent’ state should wait for EFS ‘deleted’ life cycle state  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How long the module should wait (in seconds) for desired state before returning. Zero means wait as long as necessary.  **Default:** `0` |

## [Notes](efs_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](efs_module.md#id5)

```yaml+jinja
- name: EFS provisioning
  community.aws.efs:
    state: present
    name: myTestEFS
    tags:
        Name: myTestNameTag
        purpose: file-storage
    targets:
        - subnet_id: subnet-748c5d03
          security_groups: [ "sg-1a2b3c4d" ]

- name: Modifying EFS data
  community.aws.efs:
    state: present
    name: myTestEFS
    tags:
        name: myAnotherTestTag
    targets:
        - subnet_id: subnet-7654fdca
          security_groups: [ "sg-4c5d6f7a" ]

- name: Set a lifecycle policy
  community.aws.efs:
    state: present
    name: myTestEFS
    transition_to_ia: 7
    targets:
        - subnet_id: subnet-7654fdca
          security_groups: [ "sg-4c5d6f7a" ]

- name: Remove a lifecycle policy
  community.aws.efs:
    state: present
    name: myTestEFS
    transition_to_ia: None
    targets:
        - subnet_id: subnet-7654fdca
          security_groups: [ "sg-4c5d6f7a" ]

- name: Deleting EFS
  community.aws.efs:
    state: absent
    name: myTestEFS
```

## [Return Values](efs_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **creation_time**  string | timestamp of creation date  **Returned:** always  **Sample:** `"2015-11-16 07:30:57-05:00"` |
| **creation_token**  string | EFS creation token  **Returned:** always  **Sample:** `"console-88609e04-9a0e-4a2e-912c-feaa99509961"` |
| **file_system_id**  string | ID of the file system  **Returned:** always  **Sample:** `"fs-xxxxxxxx"` |
| **filesystem_address**  string | url of file system valid for use with mount  **Returned:** always  **Sample:** `"fs-xxxxxxxx.efs.us-west-2.amazonaws.com:/"` |
| **life_cycle_state**  string | state of the EFS file system  **Returned:** always  **Sample:** `"creating, available, deleting, deleted"` |
| **mount_point**  string | url of file system with leading dot from the time when AWS EFS required to add a region suffix to the address  **Returned:** always  **Sample:** `".fs-xxxxxxxx.efs.us-west-2.amazonaws.com:/"` |
| **mount_targets**  list / elements=string | list of mount targets  **Returned:** always  **Sample:** `[{"file_system_id": "fs-a7ad440e", "ip_address": "172.31.17.173", "life_cycle_state": "available", "mount_target_id": "fsmt-d8907871", "network_interface_id": "eni-6e387e26", "owner_id": "123456789012", "security_groups": ["sg-a30b22c6"], "subnet_id": "subnet-e265c895"}, "..."]` |
| **name**  string | name of the file system  **Returned:** always  **Sample:** `"my-efs"` |
| **number_of_mount_targets**  integer | the number of targets mounted  **Returned:** always  **Sample:** `3` |
| **owner_id**  string | AWS account ID of EFS owner  **Returned:** always  **Sample:** `"XXXXXXXXXXXX"` |
| **performance_mode**  string | performance mode of the file system  **Returned:** always  **Sample:** `"generalPurpose"` |
| **size_in_bytes**  dictionary | size of the file system in bytes as of a timestamp  **Returned:** always  **Sample:** `{"timestamp": "2015-12-21 13:59:59-05:00", "value": 12288}` |
| **tags**  dictionary | tags on the efs instance  **Returned:** always  **Sample:** `{"key": "Value", "name": "my-efs"}` |

### Authors

- Ryan Sydnor (@ryansydnor)
- Artem Kazakov (@akazakov)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
