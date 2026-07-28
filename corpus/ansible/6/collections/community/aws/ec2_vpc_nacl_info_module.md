---
collection: ansible
version: "6"
title: "community.aws.ec2_vpc_nacl_info module – Gather information about Network ACLs in an AWS VPC"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ec2_vpc_nacl_info_module.html
fetched_at: 2026-07-27T17:04:09+00:00
---
# community.aws.ec2_vpc_nacl_info module – Gather information about Network ACLs in an AWS VPC

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
> see [Requirements](ec2_vpc_nacl_info_module.md#ansible-collections-community-aws-ec2-vpc-nacl-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_vpc_nacl_info`.

New in community.aws 1.0.0

- [Synopsis](ec2_vpc_nacl_info_module.md#synopsis)
- [Requirements](ec2_vpc_nacl_info_module.md#requirements)
- [Parameters](ec2_vpc_nacl_info_module.md#parameters)
- [Notes](ec2_vpc_nacl_info_module.md#notes)
- [Examples](ec2_vpc_nacl_info_module.md#examples)
- [Return Values](ec2_vpc_nacl_info_module.md#return-values)

## [Synopsis](ec2_vpc_nacl_info_module.md#id1)

- Gather information about Network ACLs in an AWS VPC

## [Requirements](ec2_vpc_nacl_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_vpc_nacl_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **filters**  dictionary | A dict of filters to apply. Each dict item consists of a filter key and a filter value. See <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkAcls.html> for possible filters. Filter names and values are case sensitive.  Default: `{}` |
| **nacl_ids**  aliases: nacl_id  list / elements=string | A list of Network ACL IDs to retrieve information about.  Default: `[]` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ec2_vpc_nacl_info_module.md#id4)

> **Note:**
>
> - By default, the module will return all Network ACLs.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_vpc_nacl_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Gather information about all Network ACLs:
- name: Get All NACLs
  community.aws.ec2_vpc_nacl_info:
    region: us-west-2
  register: all_nacls

# Retrieve default Network ACLs:
- name: Get Default NACLs
  community.aws.ec2_vpc_nacl_info:
    region: us-west-2
    filters:
      'default': 'true'
  register: default_nacls
```

## [Return Values](ec2_vpc_nacl_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **nacls**  complex | Returns an array of complex objects as described below.  Returned: success |
| **egress**  list / elements=list | A list of NACL egress rules with the following format.  `[rule no, protocol, allow/deny, v4 or v6 cidr, icmp_type, icmp_code, port from, port to]`  Returned: always  Sample: `[[100, "all", "allow", "0.0.0.0/0", null, null, null, null]]` |
| **ingress**  list / elements=list | A list of NACL ingress rules with the following format.  `[rule no, protocol, allow/deny, v4 or v6 cidr, icmp_type, icmp_code, port from, port to]`  Returned: always  Sample: `[[100, "tcp", "allow", "0.0.0.0/0", null, null, 22, 22]]` |
| **is_default**  boolean | True if the NACL is the default for its VPC.  Returned: always |
| **nacl_id**  string | The ID of the Network Access Control List.  Returned: always |
| **subnets**  list / elements=string | A list of subnet IDs that are associated with the NACL.  Returned: always |
| **tags**  dictionary | A dict of tags associated with the NACL.  Returned: always |
| **vpc_id**  string | The ID of the VPC that the NACL is attached to.  Returned: always |

### Authors

- Brad Davidson (@brandond)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
