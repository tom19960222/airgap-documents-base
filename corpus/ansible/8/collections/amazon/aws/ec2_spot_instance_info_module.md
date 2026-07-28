---
collection: ansible
version: "8"
title: "amazon.aws.ec2_spot_instance_info module – Gather information about ec2 spot instance requests"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_spot_instance_info_module.html
fetched_at: 2026-07-28T01:06:33+00:00
---
# amazon.aws.ec2_spot_instance_info module – Gather information about ec2 spot instance requests

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
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_spot_instance_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **filters**  dictionary | A dict of filters to apply. Each dict item consists of a filter key and a filter value.  Filter names and values are case sensitive.  See <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotInstanceRequests.html> for possible filters.  **Default:** `{}` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **spot_instance_request_ids**  list / elements=string | One or more Spot Instance request IDs.  **Default:** `[]` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ec2_spot_instance_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

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
| **spot_request**  list / elements=dictionary | The gathered information about specified spot instance requests.  **Returned:** when success  **Sample:** `{"create_time": "2021-09-01T21:05:57+00:00", "instance_id": "i-08877936b801ac475", "instance_interruption_behavior": "terminate", "launch_specification": {"ebs_optimized": false, "image_id": "ami-0443305dabd4be2bc", "instance_type": "t2.medium", "key_name": "zuul", "monitoring": {"enabled": false}, "placement": {"availability_zone": "us-east-2b"}, "security_groups": [{"group_id": "sg-01f9833207d53b937", "group_name": "default"}], "subnet_id": "subnet-07d906b8358869bda"}, "launched_availability_zone": "us-east-2b", "product_description": "Linux/UNIX", "spot_instance_request_id": "sir-c3cp9jsk", "spot_price": "0.046400", "state": "active", "status": {"code": "fulfilled", "message": "Your spot request is fulfilled.", "update_time": "2021-09-01T21:05:59+00:00"}, "tags": {}, "type": "one-time", "valid_until": "2021-09-08T21:05:57+00:00"}` |
| **create_time**  string | The date and time when the Spot Instance request was created.  **Returned:** always |
| **instance_id**  string | The instance ID, if an instance has been launched to fulfill the Spot Instance request.  **Returned:** when instance exists |
| **instance_interruption_behavior**  string | The behavior when a Spot Instance is interruped.  **Returned:** always |
| **launch_specification**  dictionary | Additional information for launching instances.  **Returned:** always |
| **ebs_optimized**  boolean | Indicates whether the instance is optimized for EBS I/O.  **Returned:** always |
| **image_id**  string | The ID of the AMI.  **Returned:** always |
| **instance_type**  string | The instance type.  **Returned:** always |
| **key_name**  string | The name of the key pair.  **Returned:** always |
| **monitoring**  dictionary | Described the monitoring of an instance.  **Returned:** always |
| **enabled**  boolean | Indicated whether detailed monitoring is enabled.  **Returned:** always |
| **placement**  dictionary | The placement information for the instance.  **Returned:** always |
| **availability_zone**  string | The name of the availability zone.  **Returned:** always |
| **security_groups**  list / elements=dictionary | List of security groups.  **Returned:** always |
| **group_id**  string | The ID of the security group.  **Returned:** always |
| **group_name**  string | The name of the security group.  **Returned:** always |
| **subnet_id**  string | The ID of the subnet.  **Returned:** when creating a network interface when launching an instance |
| **launched_availability_zone**  string | The availability zone in which the request is launched.  **Returned:** always |
| **product_description**  string | The product description associated with the Spot Instance.  **Returned:** always |
| **spot_instance_request_id**  string | The ID of the Spot Instance request.  **Returned:** always |
| **spot_price**  string | The maximum price per hour that you are willing to pay for a Spot Instance.  **Returned:** always |
| **state**  string | The state of the Spot Instance request.  **Returned:** always |
| **status**  dictionary | Extra information about the status of the Spot Instance request.  **Returned:** always |
| **code**  string | The status code.  See <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-request-status.html#spot-instance-request-status-understand> for codes.  **Returned:** always |
| **message**  string | The description of the status code.  **Returned:** always |
| **update_time**  string | The date and time of the most recent status update in UTC format.  **Returned:** always |
| **tags**  list / elements=dictionary | List of tags associated with the resource.  **Returned:** always |
| **key**  string | The key of the tag.  **Returned:** always |
| **value**  string | The value of the tag.  **Returned:** always |
| **type**  string | The Spot Instance request type.  **Returned:** always |
| **valid_until**  string | The end date of the request in UTC format.  **Returned:** always |

### Authors

- Mandar Vijay Kulkarni (@mandar242)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
