---
collection: ansible
version: "8"
title: "community.aws.networkfirewall_rule_group module – create, delete and modify AWS Network Firewall rule groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/networkfirewall_rule_group_module.html
fetched_at: 2026-07-28T01:41:39+00:00
---
# community.aws.networkfirewall_rule_group module – create, delete and modify AWS Network Firewall rule groups

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
> see [Requirements](networkfirewall_rule_group_module.md#ansible-collections-community-aws-networkfirewall-rule-group-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.networkfirewall_rule_group`.

New in community.aws 4.0.0

- [Synopsis](networkfirewall_rule_group_module.md#synopsis)
- [Requirements](networkfirewall_rule_group_module.md#requirements)
- [Parameters](networkfirewall_rule_group_module.md#parameters)
- [Notes](networkfirewall_rule_group_module.md#notes)
- [Examples](networkfirewall_rule_group_module.md#examples)
- [Return Values](networkfirewall_rule_group_module.md#return-values)

## [Synopsis](networkfirewall_rule_group_module.md#id1)

- A module for managing AWS Network Firewall rule groups.
- <https://docs.aws.amazon.com/network-firewall/latest/developerguide/index.html>
- Currently only supports `stateful` firewall groups.

## [Requirements](networkfirewall_rule_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](networkfirewall_rule_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **arn**  string | The ARN of the Network Firewall rule group.  Exactly one of *arn* and *name* must be provided. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **capacity**  integer | The maximum operating resources that this rule group can use.  Once a rule group is created this parameter is immutable.  See also the AWS documentation about how capacityis calculated <https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-rule-group-capacity.html>  This option is mandatory when creating a new rule group. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | A description of the AWS Network Firewall rule group. |
| **domain_list**  dictionary | Inspection criteria for a domain list rule group.  When set overwrites all Domain List settings with the new configuration.  For more information about domain name based filtering read the AWS documentation <https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-domain-names.html>.  Mutually exclusive with *rule_type=stateless*.  Mutually exclusive with *ip_variables*, *rule_list* and *rule_strings*.  Exactly one of *rule_strings*, *domain_list* or *rule_list* must be specified at creation time. |
| **action**  string / required | Action to perform on traffic that matches the rule match settings.  **Choices:**   - `"allow"` - `"deny"` |
| **domain_names**  list / elements=string / required | A list of domain names to look for in the traffic flow. |
| **filter_http**  boolean | Whether HTTP traffic should be inspected (uses the host header).  **Choices:**   - `false` ← (default) - `true` |
| **filter_https**  boolean | Whether HTTPS traffic should be inspected (uses the SNI).  **Choices:**   - `false` ← (default) - `true` |
| **source_ips**  list / elements=string | Used to expand the local network definition beyond the CIDR range of the VPC where you deploy Network Firewall. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **ip_variables**  aliases: ip_set_variables  dictionary | A dictionary mapping variable names to a list of IP addresses and address ranges, in CIDR notation.  For example `{EXAMPLE_HOSTS:["192.0.2.0/24", "203.0.113.42"]}`.  Mutually exclusive with *domain_list*. |
| **name**  string | The name of the Network Firewall rule group.  When *name* is set, *rule_type* must also be set. |
| **port_variables**  aliases: port_set_variables  dictionary | A dictionary mapping variable names to a list of ports.  For example `{SECURE_PORTS:["22", "443"]}`. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_ip_variables**  aliases: purge_ip_set_variables  boolean | Whether to purge variable names not mentioned in the *ip_variables* dictionary.  To remove all IP Set Variables it is necessary to explicitly set *ip_variables={}* and *purge_port_variables=true*.  **Choices:**   - `false` - `true` ← (default) |
| **purge_port_variables**  aliases: purge_port_set_variables  boolean | Whether to purge variable names not mentioned in the *port_variables* dictionary.  To remove all Port Set Variables it is necessary to explicitly set *port_variables={}* and *purge_port_variables=true*.  **Choices:**   - `false` - `true` ← (default) |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **rule_list**  aliases: stateful_rule_list  list / elements=dictionary | Inspection criteria to be used for a 5-tuple based rule group.  When set overwrites all existing 5-tuple rules with the new configuration.  Mutually exclusive with *domain_list* and *rule_strings*.  Mutually exclusive with *rule_type=stateless*.  Exactly one of *rule_strings*, *domain_list* or *rule_list* must be specified at creation time.  For more information about valid values see the AWS documentation <https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_StatefulRule.html> and <https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_Header.html>.  Note: Idempotency when comparing AWS Web UI and Ansiible managed rules can not be guaranteed |
| **action**  string / required | What Network Firewall should do with the packets in a traffic flow when the flow matches.  **Choices:**   - `"pass"` - `"drop"` - `"alert"` |
| **destination**  string / required | The destination IP address or address range to inspect for, in CIDR notation.  To match with any address, specify `ANY`. |
| **destination_port**  string / required | The source port to inspect for.  To match with any port, specify `ANY`. |
| **direction**  string | The direction of traffic flow to inspect.  If set to `any`, the inspection matches both traffic going from the *source* to the *destination* and from the *destination* to the *source*.  If set to `forward`, the inspection only matches traffic going from the *source* to the *destination*.  **Choices:**   - `"forward"` ← (default) - `"any"` |
| **protocol**  string / required | The protocol to inspect for. To specify all, you can use `IP`, because all traffic on AWS is `IP`. |
| **rule_options**  dictionary | Additional options for the rule.  5-tuple based rules are converted by AWS into Suricata rules, for more complex options requirements where order matters consider using *rule_strings*.  A dictionary mapping Suricata RuleOptions names to a list of values.  The examples section contains some examples of using rule_options.  For more information read the AWS documentation <https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-limitations-caveats.html> and the Suricata documentation <https://suricata.readthedocs.io/en/suricata-6.0.0/rules/intro.html>. |
| **sid**  integer / required | The signature ID of the rule.  A unique *sid* must be passed for all rules. |
| **source**  string / required | The source IP address or address range to inspect for, in CIDR notation.  To match with any address, specify `ANY`. |
| **source_port**  string / required | The source port to inspect for.  To match with any port, specify `ANY`. |
| **rule_order**  aliases: stateful_rule_order  string | Indicates how to manage the order of the rule evaluation for the rule group.  Once a rule group is created this parameter is immutable.  Mutually exclusive with *rule_type=stateless*.  For more information on how rules are evaluated read the AWS documentation <https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html>.  *rule_order* requires botocore>=1.23.23.  **Choices:**   - `"default"` - `"strict"` |
| **rule_strings**  list / elements=string | Rules in Suricata format.  If *rule_strings* is specified, it must include at least one entry.  For more information read the AWS documentation <https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-limitations-caveats.html> and the Suricata documentation <https://suricata.readthedocs.io/en/suricata-6.0.0/rules/intro.html>.  Mutually exclusive with *rule_type=stateless*.  Mutually exclusive with *domain_list* and *rule_list*.  Exactly one of *rule_strings*, *domain_list* or *rule_list* must be specified at creation time. |
| **rule_type**  aliases: type  string | Indicates whether the rule group is stateless or stateful.  Stateless rulesets are currently not supported.  Required if *name* is set.  **Choices:**   - `"stateful"` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create or remove the Network Firewall rule group.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Whether to wait for the firewall rule group to reach the `ACTIVE` or `DELETED` state before the module returns.  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  integer | Maximum time, in seconds, to wait for the firewall rule group to reach the expected state.  Defaults to 600 seconds. |

## [Notes](networkfirewall_rule_group_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](networkfirewall_rule_group_module.md#id5)

```yaml+jinja
# Create a rule group
- name: Create a minimal AWS Network Firewall Rule Group
  community.aws.networkfirewall_rule_group:
    name: 'MinimalGroup'
    type: 'stateful'
    capacity: 200
    rule_strings:
      - 'pass tcp any any -> any any (sid:1000001;)'

# Create an example rule group using rule_list
- name: Create 5-tuple Rule List based rule group
  community.aws.networkfirewall_rule_group:
    name: 'ExampleGroup'
    type: 'stateful'
    description: 'My description'
    rule_order: default
    capacity: 100
    rule_list:
      - sid: 1
        direction: forward
        action: pass
        protocol: IP
        source: any
        source_port: any
        destination: any
        destination_port: any

# Create an example rule group using rule_list
- name: Create 5-tuple Rule List based rule group
  community.aws.networkfirewall_rule_group:
    name: 'ExampleGroup'
    type: 'stateful'
    description: 'My description'
    ip_variables:
      SOURCE_IPS: ['203.0.113.0/24', '198.51.100.42']
      DESTINATION_IPS: ['192.0.2.0/24', '198.51.100.48']
    port_variables:
      HTTP_PORTS: [80, 8080]
    rule_order: default
    capacity: 100
    rule_list:
      # Allow 'Destination Unreachable' traffic
      - sid: 1
        action: pass
        protocol: icmp
        source: any
        source_port: any
        destination: any
        destination_port: any
        rule_options:
          itype: 3
      - sid: 2
        action: drop
        protocol: tcp
        source: "$SOURCE_IPS"
        source_port: any
        destination: "$DESTINATION_IPS"
        destination_port: "$HTTP_PORTS"
        rule_options:
          urilen: ["20<>40"]
          # Where only a keyword is needed, add the keword, but no value
          http_uri:
          # Settings where Suricata expects raw strings (like the content
          # keyword) will need to have the double-quotes explicitly escaped and
          # passed because there's no practical way to distinguish between them
          # and flags.
          content: '"index.php"'

# Create an example rule group using Suricata rule strings
- name: Create Suricata rule string based rule group
  community.aws.networkfirewall_rule_group:
    name: 'ExampleSuricata'
    type: 'stateful'
    description: 'My description'
    capacity: 200
    ip_variables:
      EXAMPLE_IP: ['203.0.113.0/24', '198.51.100.42']
      ANOTHER_EXAMPLE: ['192.0.2.0/24', '198.51.100.48']
    port_variables:
      EXAMPLE_PORT: [443, 22]
    rule_strings:
      - 'pass tcp any any -> $EXAMPLE_IP $EXAMPLE_PORT (sid:1000001;)'
      - 'pass udp any any -> $ANOTHER_EXAMPLE any (sid:1000002;)'

# Create an example Domain List based rule group
- name: Create Domain List based rule group
  community.aws.networkfirewall_rule_group:
    name: 'ExampleDomainList'
    type: 'stateful'
    description: 'My description'
    capacity: 100
    domain_list:
      domain_names:
        - 'example.com'
        - '.example.net'
      filter_https: True
      filter_http: True
      action: allow
      source_ips: '192.0.2.0/24'

# Update the description of a rule group
- name: Update the description of a rule group
  community.aws.networkfirewall_rule_group:
    name: 'MinimalGroup'
    type: 'stateful'
    description: 'Another description'

# Update IP Variables for a rule group
- name: Update IP Variables
  community.aws.networkfirewall_rule_group:
    name: 'ExampleGroup'
    type: 'stateful'
    ip_variables:
      EXAMPLE_IP: ['192.0.2.0/24', '203.0.113.0/24', '198.51.100.42']
    purge_ip_variables: false

# Delete a rule group
- name: Delete a rule group
  community.aws.networkfirewall_rule_group:
    name: 'MinimalGroup'
    type: 'stateful'
    state: absent
```

## [Return Values](networkfirewall_rule_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **rule_group**  dictionary | Details of the rules in the rule group  **Returned:** success |
| **rule_group**  dictionary | Details of the rules in the rule group  **Returned:** success |
| **rule_variables**  complex | Settings that are available for use in the rules in the rule group.  **Returned:** When rule variables are attached to the rule group. |
| **ip_sets**  dictionary | A dictionary mapping variable names to IP addresses in CIDR format.  **Returned:** success  **Sample:** `["192.0.2.0/24"]` |
| **port_sets**  dictionary | A dictionary mapping variable names to ports  **Returned:** success  **Sample:** `["42"]` |
| **rules_source**  dictionary | Inspection criteria used for a 5-tuple based rule group.  **Returned:** success |
| **rules_source_list**  dictionary | A description of the criteria for a domain list rule group.  **Returned:** When the rule group is “domain list” based. |
| **generated_rules_type**  string | Whether the rule group allows or denies access to the domains in the list.  **Returned:** success  **Sample:** `"ALLOWLIST"` |
| **target_types**  list / elements=string | The protocols to be inspected by the rule group.  **Returned:** success  **Sample:** `["TLS_SNI", "HTTP_HOST"]` |
| **targets**  list / elements=string | A list of domain names to be inspected for.  **Returned:** success  **Sample:** `["abc.example.com", ".example.net"]` |
| **rules_string**  string | A string describing the rules that the rule group is comprised of.  **Returned:** When the rule group is “rules string” based. |
| **stateful_rules**  list / elements=dictionary | A list of dictionaries describing the rules that the rule group is comprised of.  **Returned:** When the rule group is “rules list” based. |
| **action**  string | What action to perform when a flow matches the rule criteria.  **Returned:** success  **Sample:** `"PASS"` |
| **header**  dictionary | A description of the criteria used for the rule.  **Returned:** success |
| **destination**  string | The destination address or range of addresses to inspect for.  **Returned:** success  **Sample:** `"198.51.100.0/24"` |
| **destination_port**  string | The destination port to inspect for.  **Returned:** success  **Sample:** `"6666:6667"` |
| **direction**  string | The direction of traffic flow to inspect.  **Returned:** success  **Sample:** `"FORWARD"` |
| **protocol**  string | The protocol to inspect for.  **Returned:** success  **Sample:** `"IP"` |
| **source**  string | The source address or range of addresses to inspect for.  **Returned:** success  **Sample:** `"203.0.113.98"` |
| **source_port**  string | The source port to inspect for.  **Returned:** success  **Sample:** `"42"` |
| **rule_options**  list / elements=dictionary | Additional Suricata RuleOptions settings for the rule.  **Returned:** success |
| **keyword**  string | The keyword for the setting.  **Returned:** success  **Sample:** `"sid:1"` |
| **settings**  list / elements=string | A list of values passed to the setting.  **Returned:** When values are available |
| **stateless_rules_and_custom_actions**  dictionary | A description of the criteria for a stateless rule group.  **Returned:** When the rule group is a stateless rule group. |
| **custom_actions**  list / elements=dictionary | A list of individual custom action definitions that are available for use in stateless rules.  **Returned:** success |
| **action_definition**  dictionary | The custom action associated with the action name.  **Returned:** success |
| **publish_metric_action**  dictionary | The description of an action which publishes to CloudWatch.  **Returned:** When the action publishes to CloudWatch. |
| **dimensions**  list / elements=dictionary | The value to use in an Amazon CloudWatch custom metric dimension.  **Returned:** success |
| **value**  string | The value to use in the custom metric dimension.  **Returned:** success |
| **action_name**  string | The name for the custom action.  **Returned:** success |
| **stateless_rules**  list / elements=dictionary | A list of stateless rules for use in a stateless rule group.  **Returned:** success |
| **priority**  integer | Indicates the order in which to run this rule relative to all of the rules that are defined for a stateless rule group.  **Returned:** success |
| **rule_definition**  dictionary | Describes the stateless 5-tuple inspection criteria and actions for the rule.  **Returned:** success |
| **actions**  list / elements=string | The actions to take when a flow matches the rule.  **Returned:** success  **Sample:** `["aws:pass", "CustomActionName"]` |
| **match_attributes**  dictionary | Describes the stateless 5-tuple inspection criteria for the rule.  **Returned:** success |
| **destination_ports**  list / elements=dictionary | The destination port ranges to inspect for.  **Returned:** success |
| **from_port**  integer | The lower limit of the port range.  **Returned:** success |
| **to_port**  integer | The upper limit of the port range.  **Returned:** success |
| **destinations**  list / elements=dictionary | The destination IP addresses and address ranges to inspect for.  **Returned:** success |
| **address_definition**  string | An IP address or a block of IP addresses in CIDR notation.  **Returned:** success  **Sample:** `"192.0.2.3"` |
| **protocols**  list / elements=integer | The IANA protocol numbers of the protocols to inspect for.  **Returned:** success  **Sample:** `[6]` |
| **source_ports**  list / elements=dictionary | The source port ranges to inspect for.  **Returned:** success |
| **from_port**  integer | The lower limit of the port range.  **Returned:** success |
| **to_port**  integer | The upper limit of the port range.  **Returned:** success |
| **sources**  list / elements=dictionary | The source IP addresses and address ranges to inspect for.  **Returned:** success |
| **address_definition**  string | An IP address or a block of IP addresses in CIDR notation.  **Returned:** success  **Sample:** `"192.0.2.3"` |
| **tcp_flags**  list / elements=dictionary | The TCP flags and masks to inspect for.  **Returned:** success |
| **flags**  list / elements=string | Used with masks to define the TCP flags that flows are inspected for.  **Returned:** success |
| **masks**  list / elements=string | The set of flags considered during inspection.  **Returned:** success |
| **stateful_rule_options**  dictionary | Additional options governing how Network Firewall handles stateful rules.  **Returned:** When the rule group is either “rules string” or “rules list” based. |
| **rule_order**  string | The order in which rules will be evaluated.  **Returned:** success  **Sample:** `"DEFAULT_ACTION_ORDER"` |
| **rule_group_metadata**  dictionary | Details of the rules in the rule group  **Returned:** success |
| **capacity**  integer | The maximum operating resources that this rule group can use.  **Returned:** success |
| **consumed_capacity**  integer | The number of capacity units currently consumed by the rule group rules.  **Returned:** success |
| **description**  string | A description of the rule group.  **Returned:** success |
| **number_of_associations**  integer | The number of firewall policies that use this rule group.  **Returned:** success |
| **rule_group_arn**  integer | The ARN for the rule group  **Returned:** success  **Sample:** `"arn:aws:network-firewall:us-east-1:123456789012:stateful-rulegroup/ExampleGroup"` |
| **rule_group_id**  integer | A unique identifier for the rule group.  **Returned:** success  **Sample:** `"12345678-abcd-1234-abcd-123456789abc"` |
| **rule_group_name**  string | The name of the rule group.  **Returned:** success |
| **rule_group_status**  string | The current status of a rule group.  **Returned:** success  **Sample:** `"DELETING"` |
| **tags**  dictionary | A dictionary representing the tags associated with the rule group.  **Returned:** success |
| **type**  string | Whether the rule group is stateless or stateful.  **Returned:** success  **Sample:** `"STATEFUL"` |

### Authors

- Mark Chappell (@tremble)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
