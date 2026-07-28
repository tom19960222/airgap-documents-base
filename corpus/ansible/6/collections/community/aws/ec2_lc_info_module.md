---
collection: ansible
version: "6"
title: "community.aws.ec2_lc_info module – Gather information about AWS Autoscaling Launch Configurations."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ec2_lc_info_module.html
fetched_at: 2026-07-27T17:04:02+00:00
---
# community.aws.ec2_lc_info module – Gather information about AWS Autoscaling Launch Configurations.

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
> see [Requirements](ec2_lc_info_module.md#ansible-collections-community-aws-ec2-lc-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_lc_info`.

New in community.aws 1.0.0

- [Synopsis](ec2_lc_info_module.md#synopsis)
- [Requirements](ec2_lc_info_module.md#requirements)
- [Parameters](ec2_lc_info_module.md#parameters)
- [Notes](ec2_lc_info_module.md#notes)
- [Examples](ec2_lc_info_module.md#examples)
- [Return Values](ec2_lc_info_module.md#return-values)

## [Synopsis](ec2_lc_info_module.md#id1)

- Gather information about AWS Autoscaling Launch Configurations.

## [Requirements](ec2_lc_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_lc_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **name**  list / elements=string | A name or a list of name to match.  Default: `[]` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **sort**  string | Optional attribute which with to sort the results.  Choices:   - `"launch_configuration_name"` - `"image_id"` - `"created_time"` - `"instance_type"` - `"kernel_id"` - `"ramdisk_id"` - `"key_name"` |
| **sort_end**  integer | Which result to end with (when sorting).  Corresponds to Python slice notation. |
| **sort_order**  string | Order in which to sort results.  Only used when the ‘sort’ parameter is specified.  Choices:   - `"ascending"` ← (default) - `"descending"` |
| **sort_start**  integer | Which result to start with (when sorting).  Corresponds to Python slice notation. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ec2_lc_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_lc_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Gather information about all launch configurations
  community.aws.ec2_lc_info:

- name: Gather information about launch configuration with name "example"
  community.aws.ec2_lc_info:
    name: example

- name: Gather information sorted by created_time from most recent to least recent
  community.aws.ec2_lc_info:
    sort: created_time
    sort_order: descending
```

## [Return Values](ec2_lc_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **block_device_mapping**  list / elements=string | Block device mapping for the instances of launch configuration  Returned: always  Sample: `["[{ 'device_name': '/dev/xvda':", " 'ebs': { 'delete_on_termination': true", " 'volume_size': 8", " 'volume_type': 'gp2' }]"]` |
| **classic_link_vpc_security_groups**  string | IDs of one or more security groups for the VPC specified in classic_link_vpc_id  Returned: always |
| **created_time**  string | The creation date and time for the launch configuration  Returned: always  Sample: `"2016-05-27T13:47:44.216000+00:00"` |
| **ebs_optimized**  boolean | EBS I/O optimized (true ) or not (false )  Returned: always  Sample: `"true,"` |
| **image_id**  string | ID of the Amazon Machine Image (AMI)  Returned: always  Sample: `"ami-12345678"` |
| **instance_monitoring**  dictionary | Launched with detailed monitoring or not  Returned: always  Sample: `"{ 'enabled': true }"` |
| **instance_type**  string | Instance type  Returned: always  Sample: `"t2.micro"` |
| **kernel_id**  string | ID of the kernel associated with the AMI  Returned: always |
| **key_name**  string | Name of the key pair  Returned: always  Sample: `"user_app"` |
| **launch_configuration_arn**  string | Amazon Resource Name (ARN) of the launch configuration  Returned: always  Sample: `"arn:aws:autoscaling:us-east-1:666612345678:launchConfiguration:ba785e3a-dd42-6f02-4585-ea1a2b458b3d:launchConfigurationName/lc-app"` |
| **launch_configuration_name**  string | Name of the launch configuration  Returned: always  Sample: `"lc-app"` |
| **ramdisk_id**  string | ID of the RAM disk associated with the AMI  Returned: always |
| **security_groups**  list / elements=string | Security groups to associated  Returned: always  Sample: `["[ 'web' ]"]` |
| **user_data**  string | User data available  Returned: always |

### Authors

- Loïc Latreille (@psykotox)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
