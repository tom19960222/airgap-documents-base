---
collection: ansible
version: "6"
title: "amazon.aws.ec2_spot_instance_info module – Gather information about ec2 spot instance requests"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_spot_instance_info_module.html
fetched_at: 2026-07-27T16:43:46+00:00
---
# amazon.aws.ec2_spot_instance_info module – Gather information about ec2 spot instance requests

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
> see [Requirements](ec2_spot_instance_info_module.md#ansible-collections-amazon-aws-ec2-spot-instance-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_spot_instance_info`.

New in amazon.aws 2.0.0

- [Synopsis](ec2_spot_instance_info_module.md#synopsis)
- [Requirements](ec2_spot_instance_info_module.md#requirements)
- [Parameters](ec2_spot_instance_info_module.md#parameters)
- [Notes](ec2_spot_instance_info_module.md#notes)
- [Examples](ec2_spot_instance_info_module.md#examples)
- [Return Values](ec2_spot_instance_info_module.md#return-values)

## [Synopsis](ec2_spot_instance_info_module.md#id1)

- Describes the specified Spot Instance requests.

## [Requirements](ec2_spot_instance_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_spot_instance_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **filters**  dictionary | A dict of filters to apply. Each dict item consists of a filter key and a filter value.  Filter names and values are case sensitive.  See <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotInstanceRequests.html> for possible filters.  Default: `{}` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **spot_instance_request_ids**  list / elements=string | One or more Spot Instance request IDs. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ec2_spot_instance_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_spot_instance_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: describe the Spot Instance requests based on request IDs
  amazon.aws.ec2_spot_instance_info:
    spot_instance_request_ids:
      - sir-12345678

- name: describe the Spot Instance requests and filter results based on instance type
  amazon.aws.ec2_spot_instance_info:
    spot_instance_request_ids:
      - sir-12345678
      - sir-13579246
      - sir-87654321
    filters:
        launch.instance-type: t3.medium

- name: describe the Spot requests filtered using multiple filters
  amazon.aws.ec2_spot_instance_info:
    filters:
        state: active
        launch.block-device-mapping.device-name: /dev/sdb
```

## [Return Values](ec2_spot_instance_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **spot_request**  dictionary | The gathered information about specified spot instance requests.  Returned: when success  Sample: `{"create_time": "2021-09-01T21:05:57+00:00", "instance_id": "i-08877936b801ac475", "instance_interruption_behavior": "terminate", "launch_specification": {"ebs_optimized": false, "image_id": "ami-0443305dabd4be2bc", "instance_type": "t2.medium", "key_name": "zuul", "monitoring": {"enabled": false}, "placement": {"availability_zone": "us-east-2b"}, "security_groups": [{"group_id": "sg-01f9833207d53b937", "group_name": "default"}], "subnet_id": "subnet-07d906b8358869bda"}, "launched_availability_zone": "us-east-2b", "product_description": "Linux/UNIX", "spot_instance_request_id": "sir-c3cp9jsk", "spot_price": "0.046400", "state": "active", "status": {"code": "fulfilled", "message": "Your spot request is fulfilled.", "update_time": "2021-09-01T21:05:59+00:00"}, "tags": {}, "type": "one-time", "valid_until": "2021-09-08T21:05:57+00:00"}` |

### Authors

- Mandar Vijay Kulkarni (@mandar242)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
