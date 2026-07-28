---
collection: ansible
version: "8"
title: "community.aws.ec2_vpc_nacl module – create and delete Network ACLs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/ec2_vpc_nacl_module.html
fetched_at: 2026-07-28T01:40:48+00:00
---
# community.aws.ec2_vpc_nacl module – create and delete Network ACLs

> **Note:**
>
> This module is part of the [community.aws collection](https://galaxy.ansible.com/ui/repo/published/community/aws/) (version 6.4.0).
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
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_vpc_nacl_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **egress**  list / elements=list | A list of rules for outgoing traffic. Each rule must be specified as a list. Each rule may contain the rule number (integer 1-32766), protocol (one of [‘tcp’, ‘udp’, ‘icmp’, ‘ipv6-icmp’, ‘-1’, ‘all’]), the rule action (‘allow’ or ‘deny’) the CIDR of the IPv4 or IPv6 network range to allow or deny, the ICMP type (-1 means all types), the ICMP code (-1 means all codes), the last port in the range for TCP or UDP protocols, and the first port in the range for TCP or UDP protocols. See examples.  **Default:** `[]` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **ingress**  list / elements=list | List of rules for incoming traffic. Each rule must be specified as a list. Each rule may contain the rule number (integer 1-32766), protocol (one of [‘tcp’, ‘udp’, ‘icmp’, ‘ipv6-icmp’, ‘-1’, ‘all’]), the rule action (‘allow’ or ‘deny’) the CIDR of the IPv4 or IPv6 network range to allow or deny, the ICMP type (-1 means all types), the ICMP code (-1 means all codes), the last port in the range for TCP or UDP protocols, and the first port in the range for TCP or UDP protocols. See examples.  **Default:** `[]` |
| **nacl_id**  string | NACL id identifying a network ACL.  One and only one of the *name* or *nacl_id* is required. |
| **name**  string | Tagged name identifying a network ACL.  One and only one of the *name* or *nacl_id* is required. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Creates or modifies an existing NACL  Deletes a NACL and reassociates subnets to the default NACL  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnets**  list / elements=string | The list of subnets that should be associated with the network ACL.  Must be specified as a list  Each subnet can be specified as subnet ID, or its tagged name.  **Default:** `[]` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **vpc_id**  string | VPC id of the requesting VPC.  Required when state present. |

## [Notes](ec2_vpc_nacl_module.md#id4)

> **Note:**
>
> - Support for *purge_tags* was added in release 4.0.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

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
| **nacl_id**  string | The id of the NACL (when creating or updating an ACL)  **Returned:** success  **Sample:** `"acl-123456789abcdef01"` |
| **task**  dictionary | The result of the create, or delete action.  **Returned:** success |

### Authors

- Mike Mochan (@mmochan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
