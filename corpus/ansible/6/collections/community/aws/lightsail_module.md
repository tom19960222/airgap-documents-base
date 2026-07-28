---
collection: ansible
version: "6"
title: "community.aws.lightsail module – Manage instances in AWS Lightsail"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/lightsail_module.html
fetched_at: 2026-07-27T17:04:48+00:00
---
# community.aws.lightsail module – Manage instances in AWS Lightsail

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
> see [Requirements](lightsail_module.md#ansible-collections-community-aws-lightsail-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.lightsail`.

New in community.aws 1.0.0

- [Synopsis](lightsail_module.md#synopsis)
- [Requirements](lightsail_module.md#requirements)
- [Parameters](lightsail_module.md#parameters)
- [Notes](lightsail_module.md#notes)
- [Examples](lightsail_module.md#examples)
- [Return Values](lightsail_module.md#return-values)

## [Synopsis](lightsail_module.md#id1)

- Manage instances in AWS Lightsail.
- Instance tagging is not yet supported in this module.

## [Requirements](lightsail_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](lightsail_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **blueprint_id**  string | ID of the instance blueprint image.  Required when *state=present* |
| **bundle_id**  string | Bundle of specification info for the instance.  Required when *state=present*. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **key_pair_name**  string | Name of the key pair to use with the instance.  If *state=present* and a key_pair_name is not provided, the default keypair from the region will be used. |
| **name**  string / required | Name of the instance. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Indicate desired state of the target.  *rebooted* and *restarted* are aliases.  Choices:   - `"present"` ← (default) - `"absent"` - `"running"` - `"restarted"` - `"rebooted"` - `"stopped"` |
| **user_data**  string | Launch script that can configure the instance with additional data. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **wait**  boolean | Wait for the instance to be in state ‘running’ before returning.  If *wait=false* an ip_address may not be returned.  Has no effect when *state=rebooted* or *state=absent*.  Choices:   - `false` - `true` ← (default) |
| **wait_timeout**  integer | How long before *wait* gives up, in seconds.  Default: `300` |
| **zone**  string | AWS availability zone in which to launch the instance.  Required when *state=present* |

## [Notes](lightsail_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](lightsail_module.md#id5)

```yaml+jinja
- name: Create a new Lightsail instance
  community.aws.lightsail:
    state: present
    name: my_instance
    region: us-east-1
    zone: us-east-1a
    blueprint_id: ubuntu_16_04
    bundle_id: nano_1_0
    key_pair_name: id_rsa
    user_data: " echo 'hello world' > /home/ubuntu/test.txt"
  register: my_instance

- name: Delete an instance
  community.aws.lightsail:
    state: absent
    region: us-east-1
    name: my_instance
```

## [Return Values](lightsail_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | if a snapshot has been modified/created  Returned: always  Sample: `{"changed": true}` |
| **instance**  dictionary | instance data  Returned: always  Sample: `{"arn": "arn:aws:lightsail:us-east-1:448830907657:Instance/1fef0175-d6c8-480e-84fa-214f969cda87", "blueprint_id": "ubuntu_16_04", "blueprint_name": "Ubuntu", "bundle_id": "nano_1_0", "created_at": "2017-03-27T08:38:59.714000-04:00", "hardware": {"cpu_count": 1, "ram_size_in_gb": 0.5}, "is_static_ip": false, "location": {"availability_zone": "us-east-1a", "region_name": "us-east-1"}, "name": "my_instance", "networking": {"monthly_transfer": {"gb_per_month_allocated": 1024}, "ports": [{"access_direction": "inbound", "access_from": "Anywhere (0.0.0.0/0)", "access_type": "public", "common_name": "", "from_port": 80, "protocol": "tcp", "to_port": 80}, {"access_direction": "inbound", "access_from": "Anywhere (0.0.0.0/0)", "access_type": "public", "common_name": "", "from_port": 22, "protocol": "tcp", "to_port": 22}]}, "private_ip_address": "172.26.8.14", "public_ip_address": "34.207.152.202", "resource_type": "Instance", "ssh_key_name": "keypair", "state": {"code": 16, "name": "running"}, "support_code": "588307843083/i-0997c97831ee21e33", "username": "ubuntu"}` |

### Authors

- Nick Ball (@nickball)
- Prasad Katti (@prasadkatti)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
