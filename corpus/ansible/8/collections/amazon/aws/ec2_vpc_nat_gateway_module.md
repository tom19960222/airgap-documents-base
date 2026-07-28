---
collection: ansible
version: "8"
title: "amazon.aws.ec2_vpc_nat_gateway module – Manage AWS VPC NAT Gateways"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_vpc_nat_gateway_module.html
fetched_at: 2026-07-28T01:06:41+00:00
---
# amazon.aws.ec2_vpc_nat_gateway module – Manage AWS VPC NAT Gateways

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
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_vpc_nat_gateway_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **allocation_id**  string | The id of the elastic IP allocation. If this is not passed and the eip_address is not passed. An EIP is generated for this NAT Gateway. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **client_token**  string | Optional unique token to be used during create to ensure idempotency. When specifying this option, ensure you specify the eip_address parameter as well otherwise any subsequent runs will fail. |
| **connectivity_type**  string  *added in amazon.aws 5.5.0* | Indicates whether the NAT gateway supports public or private connectivity.  **Choices:**   - `"public"` ← (default) - `"private"` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **default_create**  boolean  *added in amazon.aws 6.2.0* | When *default_create=True* and *eip_address* has been set, but not yet allocated, the NAT gateway is created and a new EIP is automatically allocated.  When *default_create=False* and *eip_address* has been set, but not yet allocated, the module will fail.  If *eip_address* has not been set, this parameter has no effect.  **Choices:**   - `false` ← (default) - `true` |
| **eip_address**  string | The elastic IP address of the EIP you want attached to this NAT Gateway. If this is not passed and the allocation_id is not passed, an EIP is generated for this NAT Gateway. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **if_exist_do_not_create**  boolean | if a NAT Gateway exists already in the subnet_id, then do not create a new one.  **Choices:**   - `false` ← (default) - `true` |
| **nat_gateway_id**  string | The id AWS dynamically allocates to the NAT Gateway on creation. This is required when the absent option is present. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **release_eip**  boolean | Deallocate the EIP from the VPC.  Option is only valid with the absent state.  You should use this with the wait option. Since you can not release an address while a delete operation is happening.  **Choices:**   - `false` ← (default) - `true` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Ensure NAT Gateway is present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnet_id**  string | The id of the subnet to create the NAT Gateway in. This is required with the present option. |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Wait for operation to complete before returning.  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How many seconds to wait for an operation to complete before timing out.  **Default:** `320` |

## [Notes](ec2_vpc_nat_gateway_module.md#id4)

> **Note:**
>
> - Support for *tags* and *purge_tags* was added in release 1.4.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

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

- name: Create new nat gateway using an allocation-id and connectivity type.
  amazon.aws.ec2_vpc_nat_gateway:
    state: present
    subnet_id: subnet-12345678
    allocation_id: eipalloc-12345678
    connectivity_type: "private"
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
    wait: true
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
    purge_tags: false
    tags:
        Tag3: tag3
    wait: true
  register: update_tags_nat_gateway
```

## [Return Values](ec2_vpc_nat_gateway_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **create_time**  string | The ISO 8601 date time format in UTC.  **Returned:** In all cases.  **Sample:** `"2016-03-05T05:19:20.282000+00:00'"` |
| **nat_gateway_addresses**  string | List of dictionaries containing the public_ip, network_interface_id, private_ip, and allocation_id.  **Returned:** In all cases.  **Sample:** `"[{'allocation_id': 'eipalloc-12345', 'network_interface_id': 'eni-12345', 'private_ip': '10.0.0.100', 'public_ip': '52.52.52.52'}]"` |
| **nat_gateway_id**  string | id of the VPC NAT Gateway  **Returned:** In all cases.  **Sample:** `"nat-0d1e3a878585988f8"` |
| **state**  string | The current state of the NAT Gateway.  **Returned:** In all cases.  **Sample:** `"available"` |
| **subnet_id**  string | id of the Subnet  **Returned:** In all cases.  **Sample:** `"subnet-12345"` |
| **tags**  dictionary | The tags associated the VPC NAT Gateway.  **Returned:** When tags are present.  **Sample:** `{"tags": {"Ansible": "Test"}}` |
| **vpc_id**  string | id of the VPC.  **Returned:** In all cases.  **Sample:** `"vpc-12345"` |

### Authors

- Allen Sanabria (@linuxdynasty)
- Jon Hadfield (@jonhadfield)
- Karen Cheng (@Etherdaemon)
- Alina Buzachis (@alinabuzachis)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
