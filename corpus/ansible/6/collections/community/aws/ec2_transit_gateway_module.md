---
collection: ansible
version: "6"
title: "community.aws.ec2_transit_gateway module – Create and delete AWS Transit Gateways"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ec2_transit_gateway_module.html
fetched_at: 2026-07-27T17:04:06+00:00
---
# community.aws.ec2_transit_gateway module – Create and delete AWS Transit Gateways

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
> see [Requirements](ec2_transit_gateway_module.md#ansible-collections-community-aws-ec2-transit-gateway-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_transit_gateway`.

New in community.aws 1.0.0

- [Synopsis](ec2_transit_gateway_module.md#synopsis)
- [Requirements](ec2_transit_gateway_module.md#requirements)
- [Parameters](ec2_transit_gateway_module.md#parameters)
- [Notes](ec2_transit_gateway_module.md#notes)
- [Examples](ec2_transit_gateway_module.md#examples)
- [Return Values](ec2_transit_gateway_module.md#return-values)

## [Synopsis](ec2_transit_gateway_module.md#id1)

- Creates AWS Transit Gateways.
- Deletes AWS Transit Gateways.
- Updates tags on existing transit gateways.

## [Requirements](ec2_transit_gateway_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_transit_gateway_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **asn**  integer | A private Autonomous System Number (ASN) for the Amazon side of a BGP session.  The range is 64512 to 65534 for 16-bit ASNs and 4200000000 to 4294967294 for 32-bit ASNs. |
| **auto_associate**  boolean | Enable or disable automatic association with the default association route table.  Choices:   - `false` - `true` ← (default) |
| **auto_attach**  boolean | Enable or disable automatic acceptance of attachment requests.  Choices:   - `false` ← (default) - `true` |
| **auto_propagate**  boolean | Enable or disable automatic propagation of routes to the default propagation route table.  Choices:   - `false` - `true` ← (default) |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **description**  string | The description of the transit gateway. |
| **dns_support**  boolean | Whether to enable AWS DNS support.  Choices:   - `false` - `true` ← (default) |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean | Whether to purge existing tags not included with tags argument.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | `present` to ensure resource is created.  `absent` to remove resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | A dictionary of resource tags |
| **transit_gateway_id**  string | The ID of the transit gateway. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **vpn_ecmp_support**  boolean | Enable or disable Equal Cost Multipath Protocol support.  Choices:   - `false` - `true` ← (default) |
| **wait**  boolean | Whether to wait for status  Choices:   - `false` - `true` ← (default) |
| **wait_timeout**  integer | number of seconds to wait for status  Default: `300` |

## [Notes](ec2_transit_gateway_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_transit_gateway_module.md#id5)

```yaml+jinja
- name: Create a new transit gateway using defaults
  community.aws.ec2_transit_gateway:
    state: present
    region: us-east-1
    description: personal-testing
  register: created_tgw

- name: Create a new transit gateway with options
  community.aws.ec2_transit_gateway:
    asn: 64514
    auto_associate: no
    auto_propagate: no
    dns_support: True
    description: "nonprod transit gateway"
    purge_tags: False
    state: present
    region: us-east-1
    tags:
      Name: nonprod transit gateway
      status: testing

- name: Remove a transit gateway by description
  community.aws.ec2_transit_gateway:
    state: absent
    region: us-east-1
    description: personal-testing

- name: Remove a transit gateway by id
  community.aws.ec2_transit_gateway:
    state: absent
    region: ap-southeast-2
    transit_gateway_id: tgw-3a9aa123
  register: deleted_tgw
```

## [Return Values](ec2_transit_gateway_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **transit_gateway**  complex | The attributes of the transit gateway.  Returned: *state=present* |
| **creation_time**  string | The creation time of the transit gateway.  Returned: always  Sample: `"2019-03-06T17:13:51+00:00"` |
| **description**  string | The description of the transit gateway.  Returned: always  Sample: `"my test tgw"` |
| **options**  complex | The options attributes of the transit gateway  Returned: always |
| **amazon_side_asn**  string | A private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is 64512 to 65534 for 16-bit ASNs and 4200000000 to 4294967294 for 32-bit ASNs.  Returned: always  Sample: `"64512"` |
| **association_default_route_table_id**  string | The ID of the default association route table.  Returned: Iwhen exists  Sample: `"tgw-rtb-abc123444"` |
| **auto_accept_shared_attachements**  string | Indicates whether attachment requests are automatically accepted.  Returned: always  Sample: `"disable"` |
| **default_route_table_association**  string | Indicates whether resource attachments are automatically associated with the default association route table.  Returned: always  Sample: `"enable"` |
| **default_route_table_propagation**  string | Indicates whether resource attachments automatically propagate routes to the default propagation route table.  Returned: always  Sample: `"disable"` |
| **dns_support**  string | Indicates whether DNS support is enabled.  Returned: always  Sample: `"enable"` |
| **propagation_default_route_table_id**  string | The ID of the default propagation route table.  Returned: when exists  Sample: `"tgw-rtb-def456777"` |
| **vpn_ecmp_support**  string | Indicates whether Equal Cost Multipath Protocol support is enabled.  Returned: always  Sample: `"enable"` |
| **owner_id**  string | The account that owns the transit gateway.  Returned: always  Sample: `"123456789012"` |
| **state**  string | The state of the transit gateway.  Returned: always  Sample: `"pending"` |
| **tags**  dictionary | A dictionary of resource tags  Returned: always  Sample: `{"tags": {"Name": "nonprod_tgw"}}` |
| **transit_gateway_arn**  string | The ID of the transit_gateway.  Returned: always  Sample: `"tgw-3a9aa123"` |
| **transit_gateway_id**  string | The ID of the transit_gateway.  Returned: always  Sample: `"tgw-3a9aa123"` |

### Authors

- Bob Boldin (@BobBoldin)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
