---
collection: ansible
version: "6"
title: "amazon.aws.ec2_group module – maintain an ec2 VPC security group."
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_group_module.html
fetched_at: 2026-07-27T16:43:43+00:00
---
# amazon.aws.ec2_group module – maintain an ec2 VPC security group.

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
> see [Requirements](ec2_group_module.md#ansible-collections-amazon-aws-ec2-group-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_group`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_group_module.md#synopsis)
- [Requirements](ec2_group_module.md#requirements)
- [Parameters](ec2_group_module.md#parameters)
- [Notes](ec2_group_module.md#notes)
- [Examples](ec2_group_module.md#examples)
- [Return Values](ec2_group_module.md#return-values)

## [Synopsis](ec2_group_module.md#id1)

- Maintains ec2 security groups.

## [Requirements](ec2_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **description**  string | Description of the security group. Required when `state` is `present`. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **group_id**  string | Id of group to delete (works only with absent).  One of and only one of *name* or *group_id* is required. |
| **name**  string | Name of the security group.  One of and only one of *name* or *group_id* is required.  Required if *state=present*. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_rules**  boolean | Purge existing rules on security group that are not found in rules.  Choices:   - `false` - `true` ← (default) |
| **purge_rules_egress**  boolean | Purge existing rules_egress on security group that are not found in rules_egress.  Choices:   - `false` - `true` ← (default) |
| **purge_tags**  boolean | If yes, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter. If the *tags* parameter is not set then tags will not be modified.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **rules**  list / elements=dictionary | List of firewall inbound rules to enforce in this group (see example). If none are supplied, no inbound rules will be enabled. Rules list may include its own name in *group_name*. This allows idempotent loopback additions (e.g. allow group to access itself). Rule sources list support was added in version 2.4. This allows to define multiple sources per source type as well as multiple source types per rule. Prior to 2.4 an individual source is allowed. In version 2.5 support for rule descriptions was added. |
| **cidr_ip**  string | The IPv4 CIDR range traffic is coming from.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*. |
| **cidr_ipv6**  string | The IPv6 CIDR range traffic is coming from.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*. |
| **from_port**  integer | The start of the range of ports that traffic is coming from.  A value can be between `0` to `65535`.  A value of `-1` indicates all ports (only supported when *proto=icmp*). |
| **group_desc**  string | If the *group_name* is set and the Security Group doesn’t exist a new Security Group will be created with *group_desc* as the description. |
| **group_id**  string | The ID of the Security Group that traffic is coming from.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*. |
| **group_name**  list / elements=string | Name of the Security Group that traffic is coming from.  If the Security Group doesn’t exist a new Security Group will be created with *group_desc* as the description.  *group_name* can accept values of type str and list.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*. |
| **ip_prefix**  string | The IP Prefix <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-prefix-lists.html> that traffic is coming from.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*. |
| **proto**  string | The IP protocol name (`tcp`, `udp`, `icmp`, `icmpv6`) or number (<https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers>) |
| **rule_desc**  string | A description for the rule. |
| **to_port**  integer | The end of the range of ports that traffic is coming from.  A value can be between `0` to `65535`.  A value of `-1` indicates all ports (only supported when *proto=icmp*). |
| **rules_egress**  list / elements=dictionary | List of firewall outbound rules to enforce in this group (see example). If none are supplied, a default all-out rule is assumed. If an empty list is supplied, no outbound rules will be enabled. Rule Egress sources list support was added in version 2.4. In version 2.5 support for rule descriptions was added. |
| **cidr_ip**  string | The IPv4 CIDR range traffic is going to.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*. |
| **cidr_ipv6**  string | The IPv6 CIDR range traffic is going to.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*. |
| **from_port**  integer | The start of the range of ports that traffic is going to.  A value can be between `0` to `65535`.  A value of `-1` indicates all ports (only supported when *proto=icmp*). |
| **group_desc**  string | If the *group_name* is set and the Security Group doesn’t exist a new Security Group will be created with *group_desc* as the description. |
| **group_id**  string | The ID of the Security Group that traffic is going to.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*. |
| **group_name**  string | Name of the Security Group that traffic is going to.  If the Security Group doesn’t exist a new Security Group will be created with *group_desc* as the description.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*. |
| **ip_prefix**  string | The IP Prefix <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-prefix-lists.html> that traffic is going to.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*. |
| **proto**  string | The IP protocol name (`tcp`, `udp`, `icmp`, `icmpv6`) or number (<https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers>) |
| **rule_desc**  string | A description for the rule. |
| **to_port**  integer | The end of the range of ports that traffic is going to.  A value can be between `0` to `65535`.  A value of `-1` indicates all ports (only supported when *proto=icmp*). |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Create or delete a security group.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary of one or more tags to assign to the security group. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **vpc_id**  string | ID of the VPC to create the group in. |

## [Notes](ec2_group_module.md#id4)

> **Note:**
>
> - If a rule declares a group_name and that group doesn’t exist, it will be automatically created. In that case, group_desc should be provided as well. The module will refuse to create a depended-on group without a description.
> - Preview diff mode support is added in version 2.7.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_group_module.md#id5)

```yaml+jinja
- name: example using security group rule descriptions
  amazon.aws.ec2_group:
    name: "{{ name }}"
    description: sg with rule descriptions
    vpc_id: vpc-xxxxxxxx
    profile: "{{ aws_profile }}"
    region: us-east-1
    rules:
      - proto: tcp
        ports:
        - 80
        cidr_ip: 0.0.0.0/0
        rule_desc: allow all on port 80

- name: example ec2 group
  amazon.aws.ec2_group:
    name: example
    description: an example EC2 group
    vpc_id: 12345
    region: eu-west-1
    aws_secret_key: SECRET
    aws_access_key: ACCESS
    rules:
      - proto: tcp
        from_port: 80
        to_port: 80
        cidr_ip: 0.0.0.0/0
      - proto: tcp
        from_port: 22
        to_port: 22
        cidr_ip: 10.0.0.0/8
      - proto: tcp
        from_port: 443
        to_port: 443
        # this should only be needed for EC2 Classic security group rules
        # because in a VPC an ELB will use a user-account security group
        group_id: amazon-elb/sg-87654321/amazon-elb-sg
      - proto: tcp
        from_port: 3306
        to_port: 3306
        group_id: 123412341234/sg-87654321/exact-name-of-sg
      - proto: udp
        from_port: 10050
        to_port: 10050
        cidr_ip: 10.0.0.0/8
      - proto: udp
        from_port: 10051
        to_port: 10051
        group_id: sg-12345678
      - proto: icmp
        from_port: 8 # icmp type, -1 = any type
        to_port:  -1 # icmp subtype, -1 = any subtype
        cidr_ip: 10.0.0.0/8
      - proto: all
        # the containing group name may be specified here
        group_name: example
      - proto: all
        # in the 'proto' attribute, if you specify -1 (only supported when I(proto=icmp)), all, or a protocol number other than tcp, udp, icmp, or 58 (ICMPv6),
        # traffic on all ports is allowed, regardless of any ports you specify
        from_port: 10050 # this value is ignored
        to_port: 10050 # this value is ignored
        cidr_ip: 10.0.0.0/8

    rules_egress:
      - proto: tcp
        from_port: 80
        to_port: 80
        cidr_ip: 0.0.0.0/0
        cidr_ipv6: 64:ff9b::/96
        group_name: example-other
        # description to use if example-other needs to be created
        group_desc: other example EC2 group

- name: example2 ec2 group
  amazon.aws.ec2_group:
    name: example2
    description: an example2 EC2 group
    vpc_id: 12345
    region: eu-west-1
    rules:
      # 'ports' rule keyword was introduced in version 2.4. It accepts a single port value or a list of values including ranges (from_port-to_port).
      - proto: tcp
        ports: 22
        group_name: example-vpn
      - proto: tcp
        ports:
          - 80
          - 443
          - 8080-8099
        cidr_ip: 0.0.0.0/0
      # Rule sources list support was added in version 2.4. This allows to define multiple sources per source type as well as multiple source types per rule.
      - proto: tcp
        ports:
          - 6379
          - 26379
        group_name:
          - example-vpn
          - example-redis
      - proto: tcp
        ports: 5665
        group_name: example-vpn
        cidr_ip:
          - 172.16.1.0/24
          - 172.16.17.0/24
        cidr_ipv6:
          - 2607:F8B0::/32
          - 64:ff9b::/96
        group_id:
          - sg-edcd9784
  diff: True

- name: "Delete group by its id"
  amazon.aws.ec2_group:
    region: eu-west-1
    group_id: sg-33b4ee5b
    state: absent
```

## [Return Values](ec2_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | Description of security group  Returned: on create/update  Sample: `"My Security Group"` |
| **group_id**  string | Security group id  Returned: on create/update  Sample: `"sg-abcd1234"` |
| **group_name**  string | Security group name  Returned: on create/update  Sample: `"My Security Group"` |
| **ip_permissions**  list / elements=string | Inbound rules associated with the security group.  Returned: on create/update  Sample: `[{"from_port": 8182, "ip_protocol": "tcp", "ip_ranges": [{"cidr_ip": "198.51.100.1/32"}], "ipv6_ranges": [], "prefix_list_ids": [], "to_port": 8182, "user_id_group_pairs": []}]` |
| **ip_permissions_egress**  list / elements=string | Outbound rules associated with the security group.  Returned: on create/update  Sample: `[{"ip_protocol": -1, "ip_ranges": [{"cidr_ip": "0.0.0.0/0", "ipv6_ranges": [], "prefix_list_ids": [], "user_id_group_pairs": []}]}]` |
| **owner_id**  integer | AWS Account ID of the security group  Returned: on create/update  Sample: `123456789012` |
| **tags**  dictionary | Tags associated with the security group  Returned: on create/update  Sample: `{"Name": "My Security Group", "Purpose": "protecting stuff"}` |
| **vpc_id**  string | ID of VPC to which the security group belongs  Returned: on create/update  Sample: `"vpc-abcd1234"` |

### Authors

- Andrew de Quincey (@adq)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
