---
collection: ansible
version: "6"
title: "amazon.aws.ec2_vpc_nat_gateway module – Manage AWS VPC NAT Gateways."
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_vpc_nat_gateway_module.html
fetched_at: 2026-07-27T16:43:51+00:00
---
# amazon.aws.ec2_vpc_nat_gateway module – Manage AWS VPC NAT Gateways.

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
> see [Requirements](ec2_vpc_nat_gateway_module.md#ansible-collections-amazon-aws-ec2-vpc-nat-gateway-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_vpc_nat_gateway`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_vpc_nat_gateway_module.md#synopsis)
- [Requirements](ec2_vpc_nat_gateway_module.md#requirements)
- [Parameters](ec2_vpc_nat_gateway_module.md#parameters)
- [Notes](ec2_vpc_nat_gateway_module.md#notes)
- [Examples](ec2_vpc_nat_gateway_module.md#examples)
- [Return Values](ec2_vpc_nat_gateway_module.md#return-values)

## [Synopsis](ec2_vpc_nat_gateway_module.md#id1)

- Ensure the state of AWS VPC NAT Gateways based on their id, allocation and subnet ids.

## [Requirements](ec2_vpc_nat_gateway_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_vpc_nat_gateway_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allocation_id**  string | The id of the elastic IP allocation. If this is not passed and the eip_address is not passed. An EIP is generated for this NAT Gateway. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **client_token**  string | Optional unique token to be used during create to ensure idempotency. When specifying this option, ensure you specify the eip_address parameter as well otherwise any subsequent runs will fail. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **eip_address**  string | The elastic IP address of the EIP you want attached to this NAT Gateway. If this is not passed and the allocation_id is not passed, an EIP is generated for this NAT Gateway. |
| **if_exist_do_not_create**  boolean | if a NAT Gateway exists already in the subnet_id, then do not create a new one.  Choices:   - `false` ← (default) - `true` |
| **nat_gateway_id**  string | The id AWS dynamically allocates to the NAT Gateway on creation. This is required when the absent option is present. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean  added in amazon.aws 1.4.0 | Remove tags not listed in *tags*.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **release_eip**  boolean | Deallocate the EIP from the VPC.  Option is only valid with the absent state.  You should use this with the wait option. Since you can not release an address while a delete operation is happening.  Choices:   - `false` ← (default) - `true` |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Ensure NAT Gateway is present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnet_id**  string | The id of the subnet to create the NAT Gateway in. This is required with the present option. |
| **tags**  aliases: resource_tags  dictionary  added in amazon.aws 1.4.0 | A dict of tags to apply to the NAT gateway.  To remove all tags set *tags={}* and *purge_tags=true*. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **wait**  boolean | Wait for operation to complete before returning.  Choices:   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How many seconds to wait for an operation to complete before timing out.  Default: `320` |

## [Notes](ec2_vpc_nat_gateway_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_vpc_nat_gateway_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Create new nat gateway with client token.
  amazon.aws.ec2_vpc_nat_gateway:
    state: present
    subnet_id: subnet-12345678
    eip_address: 52.1.1.1
    region: ap-southeast-2
    client_token: abcd-12345678
  register: new_nat_gateway

- name: Create new nat gateway using an allocation-id.
  amazon.aws.ec2_vpc_nat_gateway:
    state: present
    subnet_id: subnet-12345678
    allocation_id: eipalloc-12345678
    region: ap-southeast-2
  register: new_nat_gateway

- name: Create new nat gateway, using an EIP address  and wait for available status.
  amazon.aws.ec2_vpc_nat_gateway:
    state: present
    subnet_id: subnet-12345678
    eip_address: 52.1.1.1
    wait: true
    region: ap-southeast-2
  register: new_nat_gateway

- name: Create new nat gateway and allocate new EIP.
  amazon.aws.ec2_vpc_nat_gateway:
    state: present
    subnet_id: subnet-12345678
    wait: true
    region: ap-southeast-2
  register: new_nat_gateway

- name: Create new nat gateway and allocate new EIP if a nat gateway does not yet exist in the subnet.
  amazon.aws.ec2_vpc_nat_gateway:
    state: present
    subnet_id: subnet-12345678
    wait: true
    region: ap-southeast-2
    if_exist_do_not_create: true
  register: new_nat_gateway

- name: Delete nat gateway using discovered nat gateways from facts module.
  amazon.aws.ec2_vpc_nat_gateway:
    state: absent
    region: ap-southeast-2
    wait: true
    nat_gateway_id: "{{ item.NatGatewayId }}"
    release_eip: true
  register: delete_nat_gateway_result
  loop: "{{ gateways_to_remove.result }}"

- name: Delete nat gateway and wait for deleted status.
  amazon.aws.ec2_vpc_nat_gateway:
    state: absent
    nat_gateway_id: nat-12345678
    wait: true
    wait_timeout: 500
    region: ap-southeast-2

- name: Delete nat gateway and release EIP.
  amazon.aws.ec2_vpc_nat_gateway:
    state: absent
    nat_gateway_id: nat-12345678
    release_eip: true
    wait: yes
    wait_timeout: 300
    region: ap-southeast-2

- name: Create new nat gateway using allocation-id and tags.
  amazon.aws.ec2_vpc_nat_gateway:
    state: present
    subnet_id: subnet-12345678
    allocation_id: eipalloc-12345678
    region: ap-southeast-2
    tags:
        Tag1: tag1
        Tag2: tag2
  register: new_nat_gateway

- name: Update tags without purge
  amazon.aws.ec2_vpc_nat_gateway:
    subnet_id: subnet-12345678
    allocation_id: eipalloc-12345678
    region: ap-southeast-2
    purge_tags: no
    tags:
        Tag3: tag3
    wait: yes
  register: update_tags_nat_gateway
```

## [Return Values](ec2_vpc_nat_gateway_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **create_time**  string | The ISO 8601 date time format in UTC.  Returned: In all cases.  Sample: `"2016-03-05T05:19:20.282000+00:00'"` |
| **nat_gateway_addresses**  string | List of dictionaries containing the public_ip, network_interface_id, private_ip, and allocation_id.  Returned: In all cases.  Sample: `"[{'allocation_id': 'eipalloc-12345', 'network_interface_id': 'eni-12345', 'private_ip': '10.0.0.100', 'public_ip': '52.52.52.52'}]"` |
| **nat_gateway_id**  string | id of the VPC NAT Gateway  Returned: In all cases.  Sample: `"nat-0d1e3a878585988f8"` |
| **state**  string | The current state of the NAT Gateway.  Returned: In all cases.  Sample: `"available"` |
| **subnet_id**  string | id of the Subnet  Returned: In all cases.  Sample: `"subnet-12345"` |
| **tags**  dictionary | The tags associated the VPC NAT Gateway.  Returned: When tags are present.  Sample: `{"tags": {"Ansible": "Test"}}` |
| **vpc_id**  string | id of the VPC.  Returned: In all cases.  Sample: `"vpc-12345"` |

### Authors

- Allen Sanabria (@linuxdynasty)
- Jon Hadfield (@jonhadfield)
- Karen Cheng (@Etherdaemon)
- Alina Buzachis (@alinabuzachis)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
