---
collection: ansible
version: "6"
title: "amazon.aws.ec2_ami_info module – Gather information about ec2 AMIs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_ami_info_module.html
fetched_at: 2026-07-27T16:43:42+00:00
---
# amazon.aws.ec2_ami_info module – Gather information about ec2 AMIs

> **Note:**
>
> This module is part of the [amazon.aws collection](https://galaxy.ansible.com/amazon/aws) (version 3.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](ec2_ami_info_module.md#ansible-collections-amazon-aws-ec2-ami-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_ami_info`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_ami_info_module.md#synopsis)
- [Requirements](ec2_ami_info_module.md#requirements)
- [Parameters](ec2_ami_info_module.md#parameters)
- [Notes](ec2_ami_info_module.md#notes)
- [Examples](ec2_ami_info_module.md#examples)
- [Return Values](ec2_ami_info_module.md#return-values)

## [Synopsis](ec2_ami_info_module.md#id1)

- Gather information about ec2 AMIs

## [Requirements](ec2_ami_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_ami_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **describe_image_attributes**  boolean | Describe attributes (like launchPermission) of the images found.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **executable_users**  aliases: executable_user  list / elements=string | Filter images by users with explicit launch permissions. Valid options are an AWS account ID, self, or all (public AMIs). |
| **filters**  dictionary | A dict of filters to apply. Each dict item consists of a filter key and a filter value.  See <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html> for possible filters.  Filter names and values are case sensitive. |
| **image_ids**  aliases: image_id  list / elements=string | One or more image IDs. |
| **owners**  aliases: owner  list / elements=string | Filter the images by the owner. Valid options are an AWS account ID, self, or an AWS owner alias ( amazon | aws-marketplace | microsoft ). |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ec2_ami_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_ami_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: gather information about an AMI using ami-id
  amazon.aws.ec2_ami_info:
    image_ids: ami-5b488823

- name: gather information about all AMIs with tag key Name and value webapp
  amazon.aws.ec2_ami_info:
    filters:
      "tag:Name": webapp

- name: gather information about an AMI with 'AMI Name' equal to foobar
  amazon.aws.ec2_ami_info:
    filters:
      name: foobar

- name: gather information about Ubuntu 17.04 AMIs published by Canonical (099720109477)
  amazon.aws.ec2_ami_info:
    owners: 099720109477
    filters:
      name: "ubuntu/images/ubuntu-zesty-17.04-*"
```

## [Return Values](ec2_ami_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **images**  list / elements=dictionary | A list of images.  Returned: always |
| **architecture**  string | The architecture of the image.  Returned: always  Sample: `"x86_64"` |
| **block_device_mappings**  list / elements=dictionary | Any block device mapping entries.  Returned: always |
| **device_name**  string | The device name exposed to the instance.  Returned: always  Sample: `"/dev/sda1"` |
| **ebs**  complex | EBS volumes  Returned: always |
| **creation_date**  string | The date and time the image was created.  Returned: always  Sample: `"2017-10-16T19:22:13.000Z"` |
| **description**  string | The description of the AMI.  Returned: always  Sample: `""` |
| **ena_support**  boolean | Whether enhanced networking with ENA is enabled.  Returned: always  Sample: `true` |
| **hypervisor**  string | The hypervisor type of the image.  Returned: always  Sample: `"xen"` |
| **image_id**  string | The ID of the AMI.  Returned: always  Sample: `"ami-5b466623"` |
| **image_location**  string | The location of the AMI.  Returned: always  Sample: `"408466080000/Webapp"` |
| **image_type**  string | The type of image.  Returned: always  Sample: `"machine"` |
| **launch_permissions**  list / elements=dictionary | A List of AWS accounts may launch the AMI.  Returned: When image is owned by calling account and *describe_image_attributes* is yes.  Sample: `[{"group": "all"}, {"user_id": "408466080000"}]` |
| **group**  string | A value of ‘all’ means the AMI is public.  Returned: success |
| **user_id**  string | An AWS account ID with permissions to launch the AMI.  Returned: success |
| **name**  string | The name of the AMI that was provided during image creation.  Returned: always  Sample: `"Webapp"` |
| **owner_id**  string | The AWS account ID of the image owner.  Returned: always  Sample: `"408466080000"` |
| **public**  boolean | Whether the image has public launch permissions.  Returned: always  Sample: `true` |
| **root_device_name**  string | The device name of the root device.  Returned: always  Sample: `"/dev/sda1"` |
| **root_device_type**  string | The type of root device used by the AMI.  Returned: always  Sample: `"ebs"` |
| **sriov_net_support**  string | Whether enhanced networking is enabled.  Returned: always  Sample: `"simple"` |
| **state**  string | The current state of the AMI.  Returned: always  Sample: `"available"` |
| **tags**  dictionary | Any tags assigned to the image.  Returned: always |
| **virtualization_type**  string | The type of virtualization of the AMI.  Returned: always  Sample: `"hvm"` |

### Authors

- Prasad Katti (@prasadkatti)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
