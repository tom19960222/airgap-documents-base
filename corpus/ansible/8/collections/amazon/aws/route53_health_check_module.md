---
collection: ansible
version: "8"
title: "amazon.aws.route53_health_check module – Manage health-checks in Amazons Route53 DNS service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/route53_health_check_module.html
fetched_at: 2026-07-28T01:07:12+00:00
---
# amazon.aws.route53_health_check module – Manage health-checks in Amazons Route53 DNS service

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
> see [Requirements](route53_health_check_module.md#ansible-collections-amazon-aws-route53-health-check-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.route53_health_check`.

New in amazon.aws 5.0.0

- [Synopsis](route53_health_check_module.md#synopsis)
- [Requirements](route53_health_check_module.md#requirements)
- [Parameters](route53_health_check_module.md#parameters)
- [Notes](route53_health_check_module.md#notes)
- [Examples](route53_health_check_module.md#examples)
- [Return Values](route53_health_check_module.md#return-values)

## [Synopsis](route53_health_check_module.md#id1)

- Creates and deletes DNS Health checks in Amazons Route53 service.
- Only the port, resource_path, string_match and request_interval are considered when updating existing health-checks.
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](route53_health_check_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](route53_health_check_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **child_health_checks**  list / elements=string  *added in amazon.aws 6.3.0* | The child health checks used for a calculated health check.  This parameter takes in the child health checks ids. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **disabled**  boolean  *added in community.aws 2.1.0* | Stops Route 53 from performing health checks.  See the AWS documentation for more details on the exact implications. <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-values.html>  Defaults to `true` when creating a new health check.  **Choices:**   - `false` - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **failure_threshold**  integer | The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa.  Will default to `3` if not specified on creation.  **Choices:**   - `1` - `2` - `3` - `4` - `5` - `6` - `7` - `8` - `9` - `10` |
| **fqdn**  string | Domain name of the endpoint to check. Either this or *ip_address* has to be provided. When both are given the *fqdn* is used in the `Host:` header of the HTTP request. |
| **health_check_id**  aliases: id  string  *added in community.aws 4.1.0* | ID of the health check to be update or deleted.  If provided, a health check can be updated or deleted based on the ID as unique identifier. |
| **health_check_name**  aliases: name  string  *added in community.aws 4.1.0* | Name of the Health Check.  Used together with *use_unique_names* to set/make use of *health_check_name* as a unique identifier. |
| **health_threshold**  integer  *added in amazon.aws 6.3.0* | The minimum number of healthy child health checks for a calculated health check to be considered healthy.  **Default:** `1` |
| **ip_address**  string | IP address of the end-point to check. Either this or *fqdn* has to be provided.  IP addresses must be publicly routable. |
| **measure_latency**  boolean  *added in amazon.aws 5.4.0* | To enable/disable latency graphs to monitor the latency between health checkers in multiple Amazon Web Services regions and your endpoint.  Value of *measure_latency* is immutable and can not be modified after creating a health check. See <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-health-check-latency.html>  **Choices:**   - `false` - `true` |
| **port**  integer | The port on the endpoint on which you want Amazon Route 53 to perform health checks. Required for TCP checks. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **request_interval**  integer | The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.  **Choices:**   - `10` - `30` ← (default) |
| **resource_path**  string | The path that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example the file /docs/route53-health-check.html.  Mutually exclusive with *type=’TCP’*.  The path must begin with a /  Maximum 255 characters. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Specifies the action to take.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **string_match**  string | If the check type is HTTP_STR_MATCH or HTTP_STR_MATCH, the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the first 5120 bytes of the response body, Amazon Route 53 considers the resource healthy. |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **type**  string | The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.  Once health_check is created, type can not be changed.  The CALCULATED choice was added in 6.3.0.  **Choices:**   - `"HTTP"` - `"HTTPS"` - `"HTTP_STR_MATCH"` - `"HTTPS_STR_MATCH"` - `"TCP"` - `"CALCULATED"` |
| **use_unique_names**  boolean  *added in community.aws 4.1.0* | Used together with *health_check_name* to set/make use of *health_check_name* as a unique identifier.  **Choices:**   - `false` - `true` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](route53_health_check_module.md#id4)

> **Note:**
>
> - Support for *tags* and *purge_tags* was added in release 2.1.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](route53_health_check_module.md#id5)

```yaml+jinja
- name: Create a health-check for host1.example.com and use it in record
  amazon.aws.route53_health_check:
    state: present
    fqdn: host1.example.com
    type: HTTP_STR_MATCH
    resource_path: /
    string_match: "Hello"
    request_interval: 10
    failure_threshold: 2
  register: my_health_check

- amazon.aws.route53:
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

- name: create a simple health check with health_check_name as unique identifier
  amazon.aws.route53_health_check:
    state: present
    health_check_name: ansible
    fqdn: ansible.com
    port: 443
    type: HTTPS
    use_unique_names: true

- name: create a TCP health check with latency graphs enabled
  amazon.aws.route53_health_check:
    state: present
    health_check_name: ansible
    fqdn: ansible.com
    port: 443
    type: HTTPS
    use_unique_names: true
    measure_latency: true

- name: Delete health-check
  amazon.aws.route53_health_check:
    state: absent
    fqdn: host1.example.com

- name: Update Health check by ID - update ip_address
  amazon.aws.route53_health_check:
    id: 12345678-abcd-abcd-abcd-0fxxxxxxxxxx
    ip_address: 1.2.3.4

- name: Update Health check by ID - update port
  amazon.aws.route53_health_check:
    id: 12345678-abcd-abcd-abcd-0fxxxxxxxxxx
    ip_address: 8080

- name: Delete Health check by ID
  amazon.aws.route53_health_check:
    state: absent
    id: 12345678-abcd-abcd-abcd-0fxxxxxxxxxx
```

## [Return Values](route53_health_check_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **health_check**  dictionary | Information about the health check.  **Returned:** success |
| **action**  string | The action performed by the module.  **Returned:** When a change is or would be made.  **Sample:** `"updated"` |
| **health_check_config**  dictionary | Detailed information about the health check.  May contain additional values from Route 53 health check features not yet supported by this module.  **Returned:** When the health check exists. |
| **disabled**  boolean | Whether the health check has been disabled or not.  **Returned:** When the health check exists.  **Sample:** `false` |
| **failure_threshold**  integer | The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa.  **Returned:** When the health check exists.  **Sample:** `3` |
| **fully_qualified_domain_name**  string | The FQDN configured for the health check to test.  **Returned:** When the health check exists and an FQDN is configured.  **Sample:** `"updated"` |
| **ip_address**  string | The IPv4 or IPv6 IP address of the endpoint to be queried.  **Returned:** When the health check exists and a specific IP address is configured.  **Sample:** `""` |
| **port**  string | The port on the endpoint that the health check will query.  **Returned:** When the health check exists.  **Sample:** `"updated"` |
| **request_interval**  integer | The number of seconds between health check queries.  **Returned:** When the health check exists.  **Sample:** `30` |
| **resource_path**  string | The URI path to query when performing an HTTP/HTTPS based health check.  **Returned:** When the health check exists and a resource path has been configured.  **Sample:** `"/healthz"` |
| **search_string**  string | A string that must be present in the response for a health check to be considered successful.  **Returned:** When the health check exists and a search string has been configured.  **Sample:** `"ALIVE"` |
| **type**  string | The type of the health check.  **Returned:** When the health check exists.  **Sample:** `"HTTPS_STR_MATCH"` |
| **health_check_version**  integer | The version number of the health check.  **Returned:** When the health check exists.  **Sample:** `14` |
| **id**  string | The Unique ID assigned by AWS to the health check.  **Returned:** When the health check exists.  **Sample:** `"50ec8a13-9623-4c66-9834-dd8c5aedc9ba"` |
| **tags**  dictionary | A dictionary representing the tags on the health check.  **Returned:** When the health check exists.  **Sample:** `{"my_key": "my_value"}` |

### Authors

- zimbatm (@zimbatm)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
