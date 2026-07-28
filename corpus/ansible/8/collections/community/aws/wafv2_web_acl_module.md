---
collection: ansible
version: "8"
title: "community.aws.wafv2_web_acl module – Create and delete WAF Web ACLs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/wafv2_web_acl_module.html
fetched_at: 2026-07-28T01:42:13+00:00
---
# community.aws.wafv2_web_acl module – Create and delete WAF Web ACLs

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
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](wafv2_web_acl_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **cloudwatch_metrics**  boolean | Enable cloudwatch metric for wafv2 web acl.  **Choices:**   - `false` - `true` ← (default) |
| **custom_response_bodies**  dictionary  *added in community.aws 3.1.0* | A map of custom response keys and content bodies. Define response bodies here and reference them in the rules by providing  the key of the body dictionary element.  Each element must have a unique dict key and in the dict two keys for *content_type* and *content*.  Requires botocore >= 1.20.40 |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **default_action**  string | Default action of the wafv2 web acl.  **Choices:**   - `"Block"` - `"Allow"` |
| **description**  string | Description of wafv2 web acl. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **metric_name**  string | Name of cloudwatch metrics.  If not given and cloudwatch_metrics is enabled, the name of the web acl itself will be taken. |
| **name**  string / required | The name of the web acl. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_rules**  boolean | When set to `no`, keep the existing load balancer rules in place. Will modify and add, but will not delete.  **Choices:**   - `false` - `true` ← (default) |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **rules**  list / elements=dictionary | The Rule statements used to identify the web requests that you want to allow, block, or count.  For a list of managed rules see <https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-list.html>. |
| **action**  dictionary | Wether a rule is blocked, allowed or counted. |
| **name**  string | The name of the wafv2 rule |
| **priority**  integer | The rule priority |
| **statement**  dictionary | Rule configuration. |
| **visibility_config**  dictionary | Visibility of single wafv2 rule. |
| **sampled_requests**  boolean | Whether to store a sample of the web requests, true or false.  **Choices:**   - `false` ← (default) - `true` |
| **scope**  string / required | Geographical scope of the web acl.  **Choices:**   - `"CLOUDFRONT"` - `"REGIONAL"` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string / required | Whether the rule is present or absent.  **Choices:**   - `"present"` - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](wafv2_web_acl_module.md#id4)

> **Note:**
>
> - Support for the *purge_tags* parameter was added in release 4.0.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](wafv2_web_acl_module.md#id5)

```yaml+jinja
- name: Create test web acl
  community.aws.wafv2_web_acl:
    name: test05
    description: hallo eins
    scope: REGIONAL
    default_action: Allow
    sampled_requests: false
    cloudwatch_metrics: true
    metric_name: test05-acl-metric
    rules:
      - name: zwei
        priority: 0
        action:
          block: {}
        visibility_config:
          sampled_requests_enabled: true
          cloud_watch_metrics_enabled: true
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
          sampled_requests_enabled: true
          cloud_watch_metrics_enabled: true
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
          sampled_requests_enabled: true
          cloud_watch_metrics_enabled: true
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
          sampled_requests_enabled: true
          cloud_watch_metrics_enabled: true
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
    purge_rules: true
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
    sampled_requests: true
    cloudwatch_metrics: true
    metric_name: ip-filtering-traffic
    rules:
      - name: whitelist-own-IPs
        priority: 0
        action:
          allow: {}
        statement:
          ip_set_reference_statement:
            arn: 'arn:aws:wafv2:us-east-1:123456789012:regional/ipset/own-public-ips/1c4bdfc4-0f77-3b23-5222-123123123'
        visibility_config:
          sampled_requests_enabled: true
          cloud_watch_metrics_enabled: true
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
          sampled_requests_enabled: true
          cloud_watch_metrics_enabled: true
          metric_name: waf-acl-rule-rate-limit-per-IP
        purge_rules: true
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
| **arn**  string | web acl arn  **Returned:** Always, as long as the web acl exists  **Sample:** `"arn:aws:wafv2:eu-central-1:123456789012:regional/webacl/test05/318c1ab9-fa74-4b3b-a974-f92e25106f61"` |
| **capacity**  integer | Current capacity of the web acl  **Returned:** Always, as long as the web acl exists  **Sample:** `140` |
| **custom_response_bodies**  dictionary | Custom response body configurations to be used in rules  **Returned:** Always, as long as the web acl exists  **Sample:** `{"too_many_requests": {"content": "{ message: \"Your request has been blocked due to too many HTTP requests coming from your IP\" }", "content_type": "APPLICATION_JSON"}}` |
| **default_action**  dictionary | Default action of ACL  **Returned:** Always, as long as the web acl exists  **Sample:** `{"allow": {}}` |
| **description**  string | Description of the web acl  **Returned:** Always, as long as the web acl exists  **Sample:** `"Some web acl description"` |
| **name**  string | Web acl name  **Returned:** Always, as long as the web acl exists  **Sample:** `"test02"` |
| **rules**  list / elements=string | Current rules of the web acl  **Returned:** Always, as long as the web acl exists  **Sample:** `[{"name": "admin_protect", "override_action": {"none": {}}, "priority": 1, "statement": {"managed_rule_group_statement": {"name": "AWSManagedRulesAdminProtectionRuleSet", "vendor_name": "AWS"}}, "visibility_config": {"cloud_watch_metrics_enabled": true, "metric_name": "admin_protect", "sampled_requests_enabled": true}}]` |
| **visibility_config**  dictionary | Visibility config of the web acl  **Returned:** Always, as long as the web acl exists  **Sample:** `{"cloud_watch_metrics_enabled": true, "metric_name": "blub", "sampled_requests_enabled": false}` |

### Authors

- Markus Bergholz (@markuman)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
