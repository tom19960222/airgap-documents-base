---
collection: ansible
version: "6"
title: "community.aws.efs module – create and maintain EFS file systems"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/efs_module.html
fetched_at: 2026-07-27T17:04:22+00:00
---
# community.aws.efs module – create and maintain EFS file systems

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
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](efs_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **encrypt**  boolean | If *encrypt=true* creates an encrypted file system. This can not be modified after the file system is created.  Choices:   - `false` ← (default) - `true` |
| **id**  string | ID of Amazon EFS. Either name or ID required for delete. |
| **kms_key_id**  string | The id of the AWS KMS CMK that will be used to protect the encrypted file system. This parameter is only required if you want to use a non-default CMK. If this parameter is not specified, the default CMK for Amazon EFS is used. The key id can be Key ID, Key ID ARN, Key Alias or Key Alias ARN. |
| **name**  string | Creation Token of Amazon EFS file system. Required for create and update. Either name or ID required for delete. |
| **performance_mode**  string | File system’s performance mode to use. Only takes effect during creation.  Choices:   - `"general_purpose"` ← (default) - `"max_io"` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **provisioned_throughput_in_mibps**  float | If the throughput_mode is provisioned, select the amount of throughput to provisioned in Mibps. |
| **purge_tags**  boolean | If yes, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter. If the *tags* parameter is not set then tags will not be modified.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Allows to create, search and destroy Amazon EFS file system.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | List of tags of Amazon EFS. Should be defined as dictionary In case of ‘present’ state with list of tags and existing EFS (matched by ‘name’), tags of EFS will be replaced with provided data. |
| **targets**  list / elements=dictionary | List of mounted targets. It should be a list of dictionaries, every dictionary should include next attributes: This data may be modified for existing EFS using state ‘present’ and new list of mount targets. |
| **ip_address**  string | A valid IPv4 address within the address range of the specified subnet. |
| **security_groups**  list / elements=string | List of security group IDs, of the form ‘sg-xxxxxxxx’. These must be for the same VPC as subnet specified |
| **subnet_id**  string / required | The ID of the subnet to add the mount target in. |
| **throughput_mode**  string | The throughput_mode for the file system to be created.  Choices:   - `"bursting"` - `"provisioned"` |
| **transition_to_ia**  string  added in community.aws 2.1.0 | How many days before objects transition to the lower-cost EFS Infrequent Access (IA) storage class.  If set to the string `None`, any existing lifecyle policy will be removed, and objects will not transition to an IA storage class.  If this parameter is absent, any existing lifecycle policy will not be affected.  Choices:   - `"None"` - `"7"` - `"14"` - `"30"` - `"60"` - `"90"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **wait**  boolean | In case of ‘present’ state should wait for EFS ‘available’ life cycle state (of course, if current state not ‘deleting’ or ‘deleted’) In case of ‘absent’ state should wait for EFS ‘deleted’ life cycle state  Choices:   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How long the module should wait (in seconds) for desired state before returning. Zero means wait as long as necessary.  Default: `0` |

## [Notes](efs_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

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
| **creation_time**  string | timestamp of creation date  Returned: always  Sample: `"2015-11-16 07:30:57-05:00"` |
| **creation_token**  string | EFS creation token  Returned: always  Sample: `"console-88609e04-9a0e-4a2e-912c-feaa99509961"` |
| **file_system_id**  string | ID of the file system  Returned: always  Sample: `"fs-xxxxxxxx"` |
| **filesystem_address**  string | url of file system valid for use with mount  Returned: always  Sample: `"fs-xxxxxxxx.efs.us-west-2.amazonaws.com:/"` |
| **life_cycle_state**  string | state of the EFS file system  Returned: always  Sample: `"creating, available, deleting, deleted"` |
| **mount_point**  string | url of file system with leading dot from the time when AWS EFS required to add a region suffix to the address  Returned: always  Sample: `".fs-xxxxxxxx.efs.us-west-2.amazonaws.com:/"` |
| **mount_targets**  list / elements=string | list of mount targets  Returned: always  Sample: `[{"file_system_id": "fs-a7ad440e", "ip_address": "172.31.17.173", "life_cycle_state": "available", "mount_target_id": "fsmt-d8907871", "network_interface_id": "eni-6e387e26", "owner_id": "740748460359", "security_groups": ["sg-a30b22c6"], "subnet_id": "subnet-e265c895"}, "..."]` |
| **name**  string | name of the file system  Returned: always  Sample: `"my-efs"` |
| **number_of_mount_targets**  integer | the number of targets mounted  Returned: always  Sample: `3` |
| **owner_id**  string | AWS account ID of EFS owner  Returned: always  Sample: `"XXXXXXXXXXXX"` |
| **performance_mode**  string | performance mode of the file system  Returned: always  Sample: `"generalPurpose"` |
| **size_in_bytes**  dictionary | size of the file system in bytes as of a timestamp  Returned: always  Sample: `{"timestamp": "2015-12-21 13:59:59-05:00", "value": 12288}` |
| **tags**  dictionary | tags on the efs instance  Returned: always  Sample: `{"key": "Value", "name": "my-efs"}` |

### Authors

- Ryan Sydnor (@ryansydnor)
- Artem Kazakov (@akazakov)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
