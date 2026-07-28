---
collection: ansible
version: "6"
title: "community.aws.aws_waf_web_acl module – Create and delete WAF Web ACLs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_waf_web_acl_module.html
fetched_at: 2026-07-27T17:03:40+00:00
---
# community.aws.aws_waf_web_acl module – Create and delete WAF Web ACLs

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
> see [Requirements](aws_waf_web_acl_module.md#ansible-collections-community-aws-aws-waf-web-acl-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_waf_web_acl`.

New in community.aws 1.0.0

- [Synopsis](aws_waf_web_acl_module.md#synopsis)
- [Requirements](aws_waf_web_acl_module.md#requirements)
- [Parameters](aws_waf_web_acl_module.md#parameters)
- [Notes](aws_waf_web_acl_module.md#notes)
- [Examples](aws_waf_web_acl_module.md#examples)
- [Return Values](aws_waf_web_acl_module.md#return-values)

## [Synopsis](aws_waf_web_acl_module.md#id1)

- Module for WAF classic, for WAF v2 use the *wafv2_\** modules.
- Read the AWS documentation for WAF <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>.

## [Requirements](aws_waf_web_acl_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_waf_web_acl_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **default_action**  string | The action that you want AWS WAF to take when a request doesn’t match the criteria specified in any of the Rule objects that are associated with the WebACL.  Choices:   - `"block"` - `"allow"` - `"count"` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **metric_name**  string | A friendly name or description for the metrics for this WebACL.  The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can’t contain whitespace.  You can’t change *metric_name* after you create the WebACL.  Metric name will default to *name* with disallowed characters stripped out. |
| **name**  string / required | Name of the Web Application Firewall ACL to manage. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_rules**  boolean | Whether to remove rules that aren’t passed with *rules*.  Choices:   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **rules**  list / elements=dictionary | A list of rules that the Web ACL will enforce. |
| **action**  string / required | The action to perform. |
| **name**  string / required | Name of the rule. |
| **priority**  integer / required | The priority of the action. Priorities must be unique. Lower numbered priorities are evaluated first. |
| **type**  string | The type of rule.  Choices:   - `"rate_based"` - `"regular"` |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Whether the Web ACL should be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **waf_regional**  boolean | Whether to use waf-regional module.  Choices:   - `false` ← (default) - `true` |

## [Notes](aws_waf_web_acl_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_waf_web_acl_module.md#id5)

```yaml+jinja
- name: create web ACL
  community.aws.aws_waf_web_acl:
    name: my_web_acl
    rules:
      - name: my_rule
        priority: 1
        action: block
    default_action: block
    purge_rules: yes
    state: present

- name: delete the web acl
  community.aws.aws_waf_web_acl:
    name: my_web_acl
    state: absent
```

## [Return Values](aws_waf_web_acl_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **web_acl**  complex | contents of the Web ACL.  Returned: always |
| **default_action**  dictionary | Default action taken by the Web ACL if no rules match.  Returned: always  Sample: `{"type": "BLOCK"}` |
| **metric_name**  string | Metric name used as an identifier.  Returned: always  Sample: `"mywebacl"` |
| **name**  string | Friendly name of the Web ACL.  Returned: always  Sample: `"my web acl"` |
| **rules**  complex | List of rules.  Returned: always |
| **action**  complex | Action taken by the WAF when the rule matches.  Returned: always  Sample: `{"type": "ALLOW"}` |
| **priority**  integer | priority number of the rule (lower numbers are run first).  Returned: always  Sample: `2` |
| **rule_id**  string | Rule ID.  Returned: always  Sample: `"a6fc7ab5-287b-479f-8004-7fd0399daf75"` |
| **type**  string | Type of rule (either REGULAR or RATE_BASED).  Returned: always  Sample: `"REGULAR"` |
| **web_acl_id**  string | Unique identifier of Web ACL.  Returned: always  Sample: `"10fff965-4b6b-46e2-9d78-24f6d2e2d21c"` |

### Authors

- Mike Mochan (@mmochan)
- Will Thames (@willthames)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
