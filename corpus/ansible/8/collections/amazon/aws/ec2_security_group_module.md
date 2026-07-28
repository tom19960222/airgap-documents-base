---
collection: ansible
version: "8"
title: "amazon.aws.ec2_security_group module – Maintain an EC2 security group"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_security_group_module.html
fetched_at: 2026-07-28T01:06:29+00:00
---
# amazon.aws.ec2_security_group module – Maintain an EC2 security group

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
> see [Requirements](ec2_security_group_module.md#ansible-collections-amazon-aws-ec2-security-group-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_security_group`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_security_group_module.md#synopsis)
- [Requirements](ec2_security_group_module.md#requirements)
- [Parameters](ec2_security_group_module.md#parameters)
- [Notes](ec2_security_group_module.md#notes)
- [Examples](ec2_security_group_module.md#examples)
- [Return Values](ec2_security_group_module.md#return-values)

## [Synopsis](ec2_security_group_module.md#id1)

- Maintains EC2 security groups.

Aliases: ec2_group

## [Requirements](ec2_security_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_security_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | Description of the security group.  Required when *state* is `present`. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **group_id**  string | Id of group to delete (works only with absent).  One of and only one of *name* or *group_id* is required. |
| **name**  string | Name of the security group.  One of and only one of *name* or *group_id* is required.  Required if *state=present*. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_rules**  boolean | Purge existing rules on security group that are not found in rules.  **Choices:**   - `false` - `true` ← (default) |
| **purge_rules_egress**  aliases: purge_egress_rules  boolean | Purge existing rules_egress on security group that are not found in rules_egress.  **Choices:**   - `false` - `true` ← (default) |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **rules**  list / elements=dictionary | List of firewall inbound rules to enforce in this group (see example). If none are supplied, no inbound rules will be enabled. Rules list may include its own name in *group_name*. This allows idempotent loopback additions (e.g. allow group to access itself). |
| **cidr_ip**  list / elements=any | The IPv4 CIDR range traffic is coming from.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*.  Support for passing nested lists of strings to *cidr_ip* has been deprecated and will be removed in a release after 2024-12-01. |
| **cidr_ipv6**  list / elements=any | The IPv6 CIDR range traffic is coming from.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*.  Support for passing nested lists of strings to *cidr_ipv6* has been deprecated and will be removed in a release after 2024-12-01. |
| **from_port**  integer | The start of the range of ports that traffic is going to.  A value can be between `0` to `65535`.  When *proto=icmp* a value of `-1` indicates all ports.  Mutually exclusive with *icmp_code*, *icmp_type* and *ports*. |
| **group_desc**  string | If the *group_name* is set and the Security Group doesn’t exist a new Security Group will be created with *group_desc* as the description. |
| **group_id**  list / elements=string | The ID of the Security Group that traffic is coming from.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*. |
| **group_name**  list / elements=string | Name of the Security Group that traffic is coming from.  If the Security Group doesn’t exist a new Security Group will be created with *group_desc* as the description.  *group_name* can accept values of type str and list.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*. |
| **icmp_code**  integer  *added in amazon.aws 3.3.0* | The ICMP code of the packet.  A value of `-1` indicates all ICMP codes.  Requires *proto=icmp* or *proto=icmpv6*.  Mutually exclusive with *ports*, *from_port* and *to_port*. |
| **icmp_type**  integer  *added in amazon.aws 3.3.0* | The ICMP type of the packet.  A value of `-1` indicates all ICMP types.  Requires *proto=icmp* or *proto=icmpv6*.  Mutually exclusive with *ports*, *from_port* and *to_port*. |
| **ip_prefix**  list / elements=string | The IP Prefix <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-prefix-lists.html> that traffic is coming from.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*. |
| **ports**  list / elements=string | A list of ports that traffic is going to.  Elements of the list can be a single port (for example `8080`), or a range of ports specified as `<START>-<END>`, (for example `1011-1023`).  Mutually exclusive with *icmp_code*, *icmp_type*, *from_port* and *to_port*. |
| **proto**  string | The IP protocol name (`tcp`, `udp`, `icmp`, `icmpv6`) or number (<https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers>).  **Default:** `"tcp"` |
| **rule_desc**  string | A description for the rule. |
| **to_port**  integer | The end of the range of ports that traffic is going to.  A value can be between `0` to `65535`.  When *proto=icmp* a value of `-1` indicates all ports.  Mutually exclusive with *icmp_code*, *icmp_type* and *ports*. |
| **rules_egress**  aliases: egress_rules  list / elements=dictionary | List of firewall outbound rules to enforce in this group (see example). If none are supplied, a default all-out rule is assumed. If an empty list is supplied, no outbound rules will be enabled. |
| **cidr_ip**  list / elements=any | The IPv4 CIDR range traffic is going to.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*.  Support for passing nested lists of strings to *cidr_ip* has been deprecated and will be removed in a release after 2024-12-01. |
| **cidr_ipv6**  list / elements=any | The IPv6 CIDR range traffic is going to.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*.  Support for passing nested lists of strings to *cidr_ipv6* has been deprecated and will be removed in a release after 2024-12-01. |
| **from_port**  integer | The start of the range of ports that traffic is going to.  A value can be between `0` to `65535`.  When *proto=icmp* a value of `-1` indicates all ports.  Mutually exclusive with *icmp_code*, *icmp_type* and *ports*. |
| **group_desc**  string | If the *group_name* is set and the Security Group doesn’t exist a new Security Group will be created with *group_desc* as the description. |
| **group_id**  list / elements=string | The ID of the Security Group that traffic is going to.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*. |
| **group_name**  list / elements=string | Name of the Security Group that traffic is going to.  If the Security Group doesn’t exist a new Security Group will be created with *group_desc* as the description.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*. |
| **icmp_code**  integer  *added in amazon.aws 3.3.0* | The ICMP code of the packet.  A value of `-1` indicates all ICMP codes.  Requires *proto=icmp* or *proto=icmpv6*.  Mutually exclusive with *ports*, *from_port* and *to_port*. |
| **icmp_type**  integer  *added in amazon.aws 3.3.0* | The ICMP type of the packet.  A value of `-1` indicates all ICMP types.  Requires *proto=icmp* or *proto=icmpv6*.  Mutually exclusive with *ports*, *from_port* and *to_port*. |
| **ip_prefix**  list / elements=string | The IP Prefix <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-prefix-lists.html> that traffic is going to.  You can specify only one of *cidr_ip*, *cidr_ipv6*, *ip_prefix*, *group_id* and *group_name*. |
| **ports**  list / elements=string | A list of ports that traffic is going to.  Elements of the list can be a single port (for example `8080`), or a range of ports specified as `<START>-<END>`, (for example `1011-1023`).  Mutually exclusive with *icmp_code*, *icmp_type*, *from_port* and *to_port*. |
| **proto**  string | The IP protocol name (`tcp`, `udp`, `icmp`, `icmpv6`) or number (<https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers>).  **Default:** `"tcp"` |
| **rule_desc**  string | A description for the rule. |
| **to_port**  integer | The end of the range of ports that traffic is going to.  A value can be between `0` to `65535`.  When *proto=icmp* a value of `-1` indicates all ports.  Mutually exclusive with *icmp_code*, *icmp_type* and *ports*. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create or delete a security group.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **vpc_id**  string | ID of the VPC to create the group in. |

## [Notes](ec2_security_group_module.md#id4)

> **Note:**
>
> - If a rule declares a group_name and that group doesn’t exist, it will be automatically created. In that case, group_desc should be provided as well. The module will refuse to create a depended-on group without a description.
> - Prior to release 5.0.0 this module was called `amazon.aws.ec2_group_info`. The usage did not change.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_security_group_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: example using security group rule descriptions
  amazon.aws.ec2_security_group:
    name: "{{ name }}"
    description: sg with rule descriptions
    vpc_id: vpc-xxxxxxxx
    rules:
      - proto: tcp
        ports:
        - 80
        cidr_ip: 0.0.0.0/0
        rule_desc: allow all on port 80

- name: example using ICMP types and codes
  amazon.aws.ec2_security_group:
    name: "{{ name }}"
    description: sg for ICMP
    vpc_id: vpc-xxxxxxxx
    rules:
      - proto: icmp
        icmp_type: 3
        icmp_code: 1
        cidr_ip: 0.0.0.0/0

- name: example ec2 group
  amazon.aws.ec2_security_group:
    name: example
    description: an example EC2 group
    vpc_id: 12345
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
        group_id: 123456789012/sg-87654321/exact-name-of-sg
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
        # in the 'proto' attribute, if you specify -1 (only supported when I(proto=icmp)), all, or a protocol number
        # other than tcp, udp, icmp, or 58 (ICMPv6), traffic on all ports is allowed, regardless of any ports that
        # you specify.
        from_port: 10050 # this value is ignored
        to_port: 10050   # this value is ignored
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
  amazon.aws.ec2_security_group:
    name: example2
    description: an example2 EC2 group
    vpc_id: 12345
    rules:
      # 'ports' rule keyword was introduced in version 2.4. It accepts a single
      # port value or a list of values including ranges (from_port-to_port).
      - proto: tcp
        ports: 22
        group_name: example-vpn
      - proto: tcp
        ports:
          - 80
          - 443
          - 8080-8099
        cidr_ip: 0.0.0.0/0
      # Rule sources list support was added in version 2.4. This allows to
      # define multiple sources per source type as well as multiple source types per rule.
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
  amazon.aws.ec2_security_group:
    group_id: sg-33b4ee5b
    state: absent
```

## [Return Values](ec2_security_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | Description of security group  **Returned:** on create/update  **Sample:** `"My Security Group"` |
| **group_id**  string | Security group id  **Returned:** on create/update  **Sample:** `"sg-abcd1234"` |
| **group_name**  string | Security group name  **Returned:** on create/update  **Sample:** `"My Security Group"` |
| **ip_permissions**  list / elements=string | Inbound rules associated with the security group.  **Returned:** on create/update  **Sample:** `[{"from_port": 8182, "ip_protocol": "tcp", "ip_ranges": [{"cidr_ip": "198.51.100.1/32"}], "ipv6_ranges": [], "prefix_list_ids": [], "to_port": 8182, "user_id_group_pairs": []}]` |
| **ip_permissions_egress**  list / elements=string | Outbound rules associated with the security group.  **Returned:** on create/update  **Sample:** `[{"ip_protocol": -1, "ip_ranges": [{"cidr_ip": "0.0.0.0/0", "ipv6_ranges": [], "prefix_list_ids": [], "user_id_group_pairs": []}]}]` |
| **owner_id**  integer | AWS Account ID of the security group  **Returned:** on create/update  **Sample:** `123456789012` |
| **tags**  dictionary | Tags associated with the security group  **Returned:** on create/update  **Sample:** `{"Name": "My Security Group", "Purpose": "protecting stuff"}` |
| **vpc_id**  string | ID of VPC to which the security group belongs  **Returned:** on create/update  **Sample:** `"vpc-abcd1234"` |

### Authors

- Andrew de Quincey (@adq)
- Razique Mahroua (@Razique)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
