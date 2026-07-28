---
collection: ansible
version: "6"
title: "community.aws.ec2_vpc_nacl module – create and delete Network ACLs."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ec2_vpc_nacl_module.html
fetched_at: 2026-07-27T17:04:08+00:00
---
# community.aws.ec2_vpc_nacl module – create and delete Network ACLs.

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
> see [Requirements](ec2_vpc_nacl_module.md#ansible-collections-community-aws-ec2-vpc-nacl-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_vpc_nacl`.

New in community.aws 1.0.0

- [Synopsis](ec2_vpc_nacl_module.md#synopsis)
- [Requirements](ec2_vpc_nacl_module.md#requirements)
- [Parameters](ec2_vpc_nacl_module.md#parameters)
- [Notes](ec2_vpc_nacl_module.md#notes)
- [Examples](ec2_vpc_nacl_module.md#examples)
- [Return Values](ec2_vpc_nacl_module.md#return-values)

## [Synopsis](ec2_vpc_nacl_module.md#id1)

- Read the AWS documentation for Network ACLS <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html>

## [Requirements](ec2_vpc_nacl_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_vpc_nacl_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **egress**  list / elements=list | A list of rules for outgoing traffic. Each rule must be specified as a list. Each rule may contain the rule number (integer 1-32766), protocol (one of [‘tcp’, ‘udp’, ‘icmp’, ‘ipv6-icmp’, ‘-1’, ‘all’]), the rule action (‘allow’ or ‘deny’) the CIDR of the IPv4 or IPv6 network range to allow or deny, the ICMP type (-1 means all types), the ICMP code (-1 means all codes), the last port in the range for TCP or UDP protocols, and the first port in the range for TCP or UDP protocols. See examples.  Default: `[]` |
| **ingress**  list / elements=list | List of rules for incoming traffic. Each rule must be specified as a list. Each rule may contain the rule number (integer 1-32766), protocol (one of [‘tcp’, ‘udp’, ‘icmp’, ‘ipv6-icmp’, ‘-1’, ‘all’]), the rule action (‘allow’ or ‘deny’) the CIDR of the IPv4 or IPv6 network range to allow or deny, the ICMP type (-1 means all types), the ICMP code (-1 means all codes), the last port in the range for TCP or UDP protocols, and the first port in the range for TCP or UDP protocols. See examples.  Default: `[]` |
| **nacl_id**  string | NACL id identifying a network ACL.  One and only one of the *name* or *nacl_id* is required. |
| **name**  string | Tagged name identifying a network ACL.  One and only one of the *name* or *nacl_id* is required. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Creates or modifies an existing NACL  Deletes a NACL and reassociates subnets to the default NACL  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnets**  list / elements=string | The list of subnets that should be associated with the network ACL.  Must be specified as a list  Each subnet can be specified as subnet ID, or its tagged name. |
| **tags**  dictionary | Dictionary of tags to look for and apply when creating a network ACL. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **vpc_id**  string | VPC id of the requesting VPC.  Required when state present. |

## [Notes](ec2_vpc_nacl_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_vpc_nacl_module.md#id5)

```yaml+jinja
# Complete example to create and delete a network ACL
# that allows SSH, HTTP and ICMP in, and all traffic out.
- name: "Create and associate production DMZ network ACL with DMZ subnets"
  community.aws.ec2_vpc_nacl:
    vpc_id: vpc-12345678
    name: prod-dmz-nacl
    region: ap-southeast-2
    subnets: ['prod-dmz-1', 'prod-dmz-2']
    tags:
      CostCode: CC1234
      Project: phoenix
      Description: production DMZ
    ingress:
        # rule no, protocol, allow/deny, cidr, icmp_type, icmp_code,
        #                                             port from, port to
        - [100, 'tcp', 'allow', '0.0.0.0/0', null, null, 22, 22]
        - [200, 'tcp', 'allow', '0.0.0.0/0', null, null, 80, 80]
        - [205, 'tcp', 'allow', '::/0', null, null, 80, 80]
        - [300, 'icmp', 'allow', '0.0.0.0/0', 0, 8]
        - [305, 'ipv6-icmp', 'allow', '::/0', 0, 8]
    egress:
        - [100, 'all', 'allow', '0.0.0.0/0', null, null, null, null]
        - [105, 'all', 'allow', '::/0', null, null, null, null]
    state: 'present'

- name: "Remove the ingress and egress rules - defaults to deny all"
  community.aws.ec2_vpc_nacl:
    vpc_id: vpc-12345678
    name: prod-dmz-nacl
    region: ap-southeast-2
    subnets:
      - prod-dmz-1
      - prod-dmz-2
    tags:
      CostCode: CC1234
      Project: phoenix
      Description: production DMZ
    state: present

- name: "Remove the NACL subnet associations and tags"
  community.aws.ec2_vpc_nacl:
    vpc_id: 'vpc-12345678'
    name: prod-dmz-nacl
    region: ap-southeast-2
    state: present

- name: "Delete nacl and subnet associations"
  community.aws.ec2_vpc_nacl:
    vpc_id: vpc-12345678
    name: prod-dmz-nacl
    state: absent

- name: "Delete nacl by its id"
  community.aws.ec2_vpc_nacl:
    nacl_id: acl-33b4ee5b
    state: absent
```

## [Return Values](ec2_vpc_nacl_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **nacl_id**  string | The id of the NACL (when creating or updating an ACL)  Returned: success  Sample: `"acl-123456789abcdef01"` |
| **task**  dictionary | The result of the create, or delete action.  Returned: success |

### Authors

- Mike Mochan (@mmochan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
