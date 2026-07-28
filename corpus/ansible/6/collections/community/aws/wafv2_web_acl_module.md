---
collection: ansible
version: "6"
title: "community.aws.wafv2_web_acl module – Create and delete WAF Web ACLs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/wafv2_web_acl_module.html
fetched_at: 2026-07-27T17:05:14+00:00
---
# community.aws.wafv2_web_acl module – Create and delete WAF Web ACLs

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
> see [Requirements](wafv2_web_acl_module.md#ansible-collections-community-aws-wafv2-web-acl-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.wafv2_web_acl`.

New in community.aws 1.5.0

- [Synopsis](wafv2_web_acl_module.md#synopsis)
- [Requirements](wafv2_web_acl_module.md#requirements)
- [Parameters](wafv2_web_acl_module.md#parameters)
- [Notes](wafv2_web_acl_module.md#notes)
- [Examples](wafv2_web_acl_module.md#examples)
- [Return Values](wafv2_web_acl_module.md#return-values)

## [Synopsis](wafv2_web_acl_module.md#id1)

- Create, modify or delete AWS WAF v2 web ACLs (not for classic WAF).
- See docs at <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>

## [Requirements](wafv2_web_acl_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](wafv2_web_acl_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **cloudwatch_metrics**  boolean | Enable cloudwatch metric for wafv2 web acl.  Choices:   - `false` - `true` ← (default) |
| **custom_response_bodies**  dictionary  added in community.aws 3.1.0 | A map of custom response keys and content bodies. Define response bodies here and reference them in the rules by providing  the key of the body dictionary element.  Each element must have a unique dict key and in the dict two keys for *content_type* and *content*.  Requires botocore >= 1.20.40 |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **default_action**  string | Default action of the wafv2 web acl.  Choices:   - `"Block"` - `"Allow"` |
| **description**  string | Description of wafv2 web acl. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **metric_name**  string | Name of cloudwatch metrics.  If not given and cloudwatch_metrics is enabled, the name of the web acl itself will be taken. |
| **name**  string / required | The name of the web acl. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_rules**  boolean | When set to `no`, keep the existing load balancer rules in place. Will modify and add, but will not delete.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **rules**  list / elements=dictionary | The Rule statements used to identify the web requests that you want to allow, block, or count.  For a list of managed rules see <https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-list.html>. |
| **action**  dictionary | Wether a rule is blocked, allowed or counted. |
| **name**  string | The name of the wafv2 rule |
| **priority**  integer | The rule priority |
| **statement**  dictionary | Rule configuration. |
| **visibility_config**  dictionary | Visibility of single wafv2 rule. |
| **sampled_requests**  boolean | Whether to store a sample of the web requests, true or false.  Choices:   - `false` ← (default) - `true` |
| **scope**  string / required | Geographical scope of the web acl.  Choices:   - `"CLOUDFRONT"` - `"REGIONAL"` |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string / required | Whether the rule is present or absent.  Choices:   - `"present"` - `"absent"` |
| **tags**  dictionary | tags for wafv2 web acl. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](wafv2_web_acl_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](wafv2_web_acl_module.md#id5)

```yaml+jinja
- name: Create test web acl
  community.aws.wafv2_web_acl:
    name: test05
    description: hallo eins
    scope: REGIONAL
    default_action: Allow
    sampled_requests: no
    cloudwatch_metrics: yes
    metric_name: test05-acl-metric
    rules:
      - name: zwei
        priority: 0
        action:
          block: {}
        visibility_config:
          sampled_requests_enabled: yes
          cloud_watch_metrics_enabled: yes
          metric_name: ddos
        statement:
          xss_match_statement:
            field_to_match:
              body: {}
            text_transformations:
              - type: NONE
                priority: 0
      - name: admin_protect
        priority: 1
        override_action:
          none: {}
        visibility_config:
          sampled_requests_enabled: yes
          cloud_watch_metrics_enabled: yes
          metric_name: fsd
        statement:
          managed_rule_group_statement:
            vendor_name: AWS
            name: AWSManagedRulesAdminProtectionRuleSet

      # AWS Managed Bad Input Rule Set
      # but allow PROPFIND_METHOD used e.g. by webdav
      - name: bad_input_protect_whitelist_webdav
        priority: 2
        override_action:
          none: {}
        visibility_config:
          sampled_requests_enabled: yes
          cloud_watch_metrics_enabled: yes
          metric_name: bad_input_protect
        statement:
          managed_rule_group_statement:
            vendor_name: AWS
            name: AWSManagedRulesKnownBadInputsRuleSet
            excluded_rules:
              - name: PROPFIND_METHOD

      # Rate Limit example. 1500 req/5min
      # counted for two domains via or_statement. login.mydomain.tld and api.mydomain.tld
      - name: rate_limit_example
        priority: 3
        action:
          block: {}
        visibility_config:
          sampled_requests_enabled: yes
          cloud_watch_metrics_enabled: yes
          metric_name: mydomain-ratelimit
        statement:
          rate_based_statement:
            limit: 1500
            aggregate_key_type: IP
            scope_down_statement:
              or_statement:
                statements:
                  - byte_match_statement:
                      search_string: login.mydomain.tld
                      positional_constraint: CONTAINS
                      field_to_match:
                        single_header:
                          name: host
                      text_transformations:
                        - type: LOWERCASE
                          priority: 0
                  - byte_match_dtatement:
                      search_string: api.mydomain.tld
                      positional_constraint: CONTAINS
                      field_to_match:
                        single_header:
                          name: host
                      text_transformations:
                        - type: LOWERCASE
                          priority: 0
    purge_rules: yes
    tags:
      A: B
      C: D
    state: present

- name: Create IP filtering web ACL
  community.aws.wafv2_web_acl:
    name: ip-filtering-traffic
    description: ACL that filters web traffic based on rate limits and whitelists some IPs
    scope: REGIONAL
    default_action: Allow
    sampled_requests: yes
    cloudwatch_metrics: yes
    metric_name: ip-filtering-traffic
    rules:
      - name: whitelist-own-IPs
        priority: 0
        action:
          allow: {}
        statement:
          ip_set_reference_statement:
            arn: 'arn:aws:wafv2:us-east-1:520789123123:regional/ipset/own-public-ips/1c4bdfc4-0f77-3b23-5222-123123123'
        visibility_config:
          sampled_requests_enabled: yes
          cloud_watch_metrics_enabled: yes
          metric_name: waf-acl-rule-whitelist-own-IPs
      - name: rate-limit-per-IP
        priority: 1
        action:
          block:
            custom_response:
              response_code: 429
              custom_response_body_key: too_many_requests
        statement:
          rate_based_statement:
            limit: 5000
            aggregate_key_type: IP
        visibility_config:
          sampled_requests_enabled: yes
          cloud_watch_metrics_enabled: yes
          metric_name: waf-acl-rule-rate-limit-per-IP
        purge_rules: yes
    custom_response_bodies:
      too_many_requests:
        content_type: APPLICATION_JSON
        content: '{ message: "Your request has been blocked due to too many HTTP requests coming from your IP" }'
    region: us-east-1
    state: present
```

## [Return Values](wafv2_web_acl_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **arn**  string | web acl arn  Returned: Always, as long as the web acl exists  Sample: `"arn:aws:wafv2:eu-central-1:11111111:regional/webacl/test05/318c1ab9-fa74-4b3b-a974-f92e25106f61"` |
| **capacity**  integer | Current capacity of the web acl  Returned: Always, as long as the web acl exists  Sample: `140` |
| **custom_response_bodies**  dictionary | Custom response body configurations to be used in rules  Returned: Always, as long as the web acl exists  Sample: `{"too_many_requests": {"content": "{ message: \"Your request has been blocked due to too many HTTP requests coming from your IP\" }", "content_type": "APPLICATION_JSON"}}` |
| **default_action**  dictionary | Default action of ACL  Returned: Always, as long as the web acl exists  Sample: `{"allow": {}}` |
| **description**  string | Description of the web acl  Returned: Always, as long as the web acl exists  Sample: `"Some web acl description"` |
| **name**  string | Web acl name  Returned: Always, as long as the web acl exists  Sample: `"test02"` |
| **rules**  list / elements=string | Current rules of the web acl  Returned: Always, as long as the web acl exists  Sample: `[{"name": "admin_protect", "override_action": {"none": {}}, "priority": 1, "statement": {"managed_rule_group_statement": {"name": "AWSManagedRulesAdminProtectionRuleSet", "vendor_name": "AWS"}}, "visibility_config": {"cloud_watch_metrics_enabled": true, "metric_name": "admin_protect", "sampled_requests_enabled": true}}]` |
| **visibility_config**  dictionary | Visibility config of the web acl  Returned: Always, as long as the web acl exists  Sample: `{"cloud_watch_metrics_enabled": true, "metric_name": "blub", "sampled_requests_enabled": false}` |

### Authors

- Markus Bergholz (@markuman)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
