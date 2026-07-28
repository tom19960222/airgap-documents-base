---
collection: ansible
version: "6"
title: "community.aws.route53_health_check module – Manage health-checks in Amazons Route53 DNS service"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/route53_health_check_module.html
fetched_at: 2026-07-27T17:04:59+00:00
---
# community.aws.route53_health_check module – Manage health-checks in Amazons Route53 DNS service

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
> see [Requirements](route53_health_check_module.md#ansible-collections-community-aws-route53-health-check-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.route53_health_check`.

New in community.aws 1.0.0

- [Synopsis](route53_health_check_module.md#synopsis)
- [Requirements](route53_health_check_module.md#requirements)
- [Parameters](route53_health_check_module.md#parameters)
- [Notes](route53_health_check_module.md#notes)
- [Examples](route53_health_check_module.md#examples)
- [Return Values](route53_health_check_module.md#return-values)

## [Synopsis](route53_health_check_module.md#id1)

- Creates and deletes DNS Health checks in Amazons Route53 service.
- Only the port, resource_path, string_match and request_interval are considered when updating existing health-checks.

## [Requirements](route53_health_check_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](route53_health_check_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **disabled**  boolean  added in community.aws 2.1.0 | Stops Route 53 from performing health checks.  See the AWS documentation for more details on the exact implications. <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-values.html>  Defaults to `true` when creating a new health check.  Choices:   - `false` - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **failure_threshold**  integer | The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa.  Will default to `3` if not specified on creation.  Choices:   - `1` - `2` - `3` - `4` - `5` - `6` - `7` - `8` - `9` - `10` |
| **fqdn**  string | Domain name of the endpoint to check. Either this or *ip_address* has to be provided. When both are given the *fqdn* is used in the `Host:` header of the HTTP request. |
| **ip_address**  string | IP address of the end-point to check. Either this or *fqdn* has to be provided.  IP addresses must be publicly routable. |
| **port**  integer | The port on the endpoint on which you want Amazon Route 53 to perform health checks. Required for TCP checks. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean  added in community.aws 2.1.0 | Delete any tags not specified in *tags*.  Choices:   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **request_interval**  integer | The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.  Choices:   - `10` - `30` ← (default) |
| **resource_path**  string | The path that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example the file /docs/route53-health-check.html.  Mutually exclusive with *type=’TCP’*.  The path must begin with a /  Maximum 255 characters. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Specifies the action to take.  Choices:   - `"present"` ← (default) - `"absent"` |
| **string_match**  string | If the check type is HTTP_STR_MATCH or HTTP_STR_MATCH, the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the first 5120 bytes of the response body, Amazon Route 53 considers the resource healthy. |
| **tags**  dictionary  added in community.aws 2.1.0 | A hash/dictionary of tags to set on the health check. |
| **type**  string / required | The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.  Choices:   - `"HTTP"` - `"HTTPS"` - `"HTTP_STR_MATCH"` - `"HTTPS_STR_MATCH"` - `"TCP"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](route53_health_check_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](route53_health_check_module.md#id5)

```yaml+jinja
- name: Create a health-check for host1.example.com and use it in record
  community.aws.route53_health_check:
    state: present
    fqdn: host1.example.com
    type: HTTP_STR_MATCH
    resource_path: /
    string_match: "Hello"
    request_interval: 10
    failure_threshold: 2
  register: my_health_check

- community.aws.route53:
    action: create
    zone: "example.com"
    type: CNAME
    record: "www.example.com"
    value: host1.example.com
    ttl: 30
    # Routing policy
    identifier: "host1@www"
    weight: 100
    health_check: "{{ my_health_check.health_check.id }}"

- name: Delete health-check
  community.aws.route53_health_check:
    state: absent
    fqdn: host1.example.com
```

## [Return Values](route53_health_check_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **health_check**  dictionary | Information about the health check.  Returned: success |
| **action**  string | The action performed by the module.  Returned: When a change is or would be made.  Sample: `"updated"` |
| **health_check_config**  dictionary | Detailed information about the health check.  May contain additional values from Route 53 health check features not yet supported by this module.  Returned: When the health check exists. |
| **disabled**  boolean | Whether the health check has been disabled or not.  Returned: When the health check exists.  Sample: `false` |
| **failure_threshold**  integer | The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa.  Returned: When the health check exists.  Sample: `3` |
| **fully_qualified_domain_name**  string | The FQDN configured for the health check to test.  Returned: When the health check exists and an FQDN is configured.  Sample: `"updated"` |
| **ip_address**  string | The IPv4 or IPv6 IP address of the endpoint to be queried.  Returned: When the health check exists and a specific IP address is configured.  Sample: `""` |
| **port**  string | The port on the endpoint that the health check will query.  Returned: When the health check exists.  Sample: `"updated"` |
| **request_interval**  integer | The number of seconds between health check queries.  Returned: When the health check exists.  Sample: `30` |
| **resource_path**  string | The URI path to query when performing an HTTP/HTTPS based health check.  Returned: When the health check exists and a resource path has been configured.  Sample: `"/healthz"` |
| **search_string**  string | A string that must be present in the response for a health check to be considered successful.  Returned: When the health check exists and a search string has been configured.  Sample: `"ALIVE"` |
| **type**  string | The type of the health check.  Returned: When the health check exists.  Sample: `"HTTPS_STR_MATCH"` |
| **health_check_version**  integer | The version number of the health check.  Returned: When the health check exists.  Sample: `14` |
| **id**  string | The Unique ID assigned by AWS to the health check.  Returned: When the health check exists.  Sample: `"50ec8a13-9623-4c66-9834-dd8c5aedc9ba"` |
| **tags**  dictionary | A dictionary representing the tags on the health check.  Returned: When the health check exists.  Sample: `{"my_key": "my_value"}` |

### Authors

- zimbatm (@zimbatm)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
