---
collection: ansible
version: "6"
title: "community.aws.ec2_customer_gateway module – Manage an AWS customer gateway"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ec2_customer_gateway_module.html
fetched_at: 2026-07-27T17:03:57+00:00
---
# community.aws.ec2_customer_gateway module – Manage an AWS customer gateway

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
> see [Requirements](ec2_customer_gateway_module.md#ansible-collections-community-aws-ec2-customer-gateway-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_customer_gateway`.

New in community.aws 1.0.0

- [Synopsis](ec2_customer_gateway_module.md#synopsis)
- [Requirements](ec2_customer_gateway_module.md#requirements)
- [Parameters](ec2_customer_gateway_module.md#parameters)
- [Notes](ec2_customer_gateway_module.md#notes)
- [Examples](ec2_customer_gateway_module.md#examples)
- [Return Values](ec2_customer_gateway_module.md#return-values)

## [Synopsis](ec2_customer_gateway_module.md#id1)

- Manage an AWS customer gateway.

## [Requirements](ec2_customer_gateway_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_customer_gateway_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **bgp_asn**  integer | Border Gateway Protocol (BGP) Autonomous System Number (ASN).  Defaults to `65000` if not specified when *state=present*. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **ip_address**  string / required | Internet-routable IP address for customers gateway, must be a static address. |
| **name**  string / required | Name of the customer gateway. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **routing**  string | The type of routing.  Choices:   - `"static"` - `"dynamic"` ← (default) |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Create or terminate the Customer Gateway.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ec2_customer_gateway_module.md#id4)

> **Note:**
>
> - You cannot create more than one customer gateway with the same IP address. If you run an identical request more than one time, the first request creates the customer gateway, and subsequent requests return information about the existing customer gateway. The subsequent requests do not create new customer gateway resources.
> - Return values contain customer_gateway and customer_gateways keys which are identical dicts. You should use customer_gateway. See <https://github.com/ansible/ansible-modules-extras/issues/2773> for details.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_customer_gateway_module.md#id5)

```yaml+jinja
- name: Create Customer Gateway
  community.aws.ec2_customer_gateway:
    bgp_asn: 12345
    ip_address: 1.2.3.4
    name: IndianapolisOffice
    region: us-east-1
  register: cgw

- name: Delete Customer Gateway
  community.aws.ec2_customer_gateway:
    ip_address: 1.2.3.4
    name: IndianapolisOffice
    state: absent
    region: us-east-1
  register: cgw
```

## [Return Values](ec2_customer_gateway_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **gateway.customer_gateways**  complex | details about the gateway that was created.  Returned: success |
| **bgp_asn**  string | The Border Gateway Autonomous System Number.  Returned: when exists and gateway is available.  Sample: `"65123"` |
| **customer_gateway_id**  string | gateway id assigned by amazon.  Returned: when exists and gateway is available.  Sample: `"cgw-cb6386a2"` |
| **ip_address**  string | ip address of your gateway device.  Returned: when exists and gateway is available.  Sample: `"1.2.3.4"` |
| **state**  string | state of gateway.  Returned: when gateway exists and is available.  Sample: `"available"` |
| **tags**  list / elements=string | Any tags on the gateway.  Returned: when gateway exists and is available, and when tags exist. |
| **type**  string | encryption type.  Returned: when gateway exists and is available.  Sample: `"ipsec.1"` |

### Authors

- Michael Baydoun (@MichaelBaydoun)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
