---
collection: ansible
version: "8"
title: "amazon.aws.route53_info module – Retrieves route53 details using AWS methods"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/route53_info_module.html
fetched_at: 2026-07-28T01:07:12+00:00
---
# amazon.aws.route53_info module – Retrieves route53 details using AWS methods

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
> see [Requirements](route53_info_module.md#ansible-collections-amazon-aws-route53-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.route53_info`.

New in amazon.aws 5.0.0

- [Synopsis](route53_info_module.md#synopsis)
- [Requirements](route53_info_module.md#requirements)
- [Parameters](route53_info_module.md#parameters)
- [Notes](route53_info_module.md#notes)
- [Examples](route53_info_module.md#examples)
- [Return Values](route53_info_module.md#return-values)

## [Synopsis](route53_info_module.md#id1)

- Gets various details related to Route53 zone, record set or health check details.
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](route53_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](route53_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **change_id**  string | The ID of the change batch request.  The value that you specify here is the value that ChangeResourceRecordSets returned in the Id element when you submitted the request.  Required if *query=change*. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **delegation_set_id**  string | The DNS Zone delegation set ID. |
| **dns_name**  string | The first name in the lexicographic ordering of domain names that you want the list_command to start listing from. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **health_check_id**  string | The ID of the health check.  Required if `query` is set to `health_check` and `health_check_method` is set to `details` or `status` or `failure_reason`. |
| **health_check_method**  string | This is used in conjunction with query: health_check. It allows for listing details, counts or tags of various health check details.  **Choices:**   - `"list"` ← (default) - `"details"` - `"status"` - `"failure_reason"` - `"count"` - `"tags"` |
| **hosted_zone_id**  string | The Hosted Zone ID of the DNS zone.  Required if *query* is set to *hosted_zone* and *hosted_zone_method* is set to *details*.  Required if *query* is set to *record_sets*. |
| **hosted_zone_method**  string | This is used in conjunction with query: hosted_zone. It allows for listing details, counts or tags of various hosted zone details.  **Choices:**   - `"details"` - `"list"` ← (default) - `"list_by_name"` - `"count"` - `"tags"` |
| **max_items**  integer | Maximum number of items to return for various get/list requests. |
| **next_marker**  string | Some requests such as list_command: hosted_zones will return a maximum number of entries - EG 100 or the number specified by *max_items*. If the number of entries exceeds this maximum another request can be sent using the NextMarker entry from the first response to get the next page of results. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **query**  string / required | Specifies the query action to take.  **Choices:**   - `"change"` - `"checker_ip_range"` - `"health_check"` - `"hosted_zone"` - `"record_sets"` - `"reusable_delegation_set"` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **resource_id**  aliases: resource_ids  list / elements=string | The ID/s of the specified resource/s.  Required if *query=health_check* and *health_check_method=tags*.  Required if *query=hosted_zone* and *hosted_zone_method=tags*. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **start_record_name**  string | The first name in the lexicographic ordering of domain names that you want the list_command: record_sets to start listing from. |
| **type**  string | The type of DNS record.  **Choices:**   - `"A"` - `"CNAME"` - `"MX"` - `"AAAA"` - `"TXT"` - `"PTR"` - `"SRV"` - `"SPF"` - `"CAA"` - `"NS"` - `"NAPTR"` - `"SOA"` - `"DS"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](route53_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](route53_info_module.md#id5)

```yaml+jinja
# Simple example of listing all hosted zones
- name: List all hosted zones
  amazon.aws.route53_info:
    query: hosted_zone
  register: hosted_zones

# Getting a count of hosted zones
- name: Return a count of all hosted zones
  amazon.aws.route53_info:
    query: hosted_zone
    hosted_zone_method: count
  register: hosted_zone_count

- name: List the first 20 resource record sets in a given hosted zone
  amazon.aws.route53_info:
    profile: account_name
    query: record_sets
    hosted_zone_id: ZZZ1111112222
    max_items: 20
  register: record_sets

- name: List first 20 health checks
  amazon.aws.route53_info:
    query: health_check
    health_check_method: list
    max_items: 20
  register: health_checks

- name: Get health check last failure_reason
  amazon.aws.route53_info:
    query: health_check
    health_check_method: failure_reason
    health_check_id: 00000000-1111-2222-3333-12345678abcd
  register: health_check_failure_reason

- name: Retrieve reusable delegation set details
  amazon.aws.route53_info:
    query: reusable_delegation_set
    delegation_set_id: delegation id
  register: delegation_sets

- name: setup of example for using next_marker
  amazon.aws.route53_info:
    query: hosted_zone
    max_items: 1
  register: first_info

- name: example for using next_marker
  amazon.aws.route53_info:
    query: hosted_zone
    next_marker: "{{ first_info.NextMarker }}"
    max_items: 1
  when: "{{ 'NextMarker' in first_info }}"

- name: retrieve host entries starting with host1.workshop.test.io
  block:
    - name: grab zone id
      amazon.aws.route53_zone:
        zone: "test.io"
      register: AWSINFO

    - name: grab Route53 record information
      amazon.aws.route53_info:
        type: A
        query: record_sets
        hosted_zone_id: "{{ AWSINFO.zone_id }}"
        start_record_name: "host1.workshop.test.io"
      register: RECORDS
```

## [Return Values](route53_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **checker_ip_ranges**  list / elements=string  *added in community.aws 4.1.0* | A list of IP ranges in CIDR format for Amazon Route 53 health checkers.  **Returned:** when *query=checker_ip_range* |
| **CheckerIpRanges**  list / elements=string | A deprecated CamelCased list of IP ranges in CIDR format for Amazon Route 53 health checkers.\ This list contains same elements/parameters as it’s snake_cased version mentioned abobe. \ This field is deprecated and will be removed in 6.0.0 version release.  **Returned:** when *query=checker_ip_range* |
| **delegation_sets**  list / elements=dictionary  *added in community.aws 4.1.0* | A list of dicts that contains information about the reusable delegation set.  **Returned:** when *query=reusable_delegation_set* |
| **DelegationSets**  list / elements=dictionary | A deprecated CamelCased list of dicts that contains information about the reusable delegation set. \ This list contains same elements/parameters as it’s snake_cased version mentioned above. \ This field is deprecated and will be removed in 6.0.0 version release.  **Returned:** when *query=reusable_delegation_set* |
| **health_check**  dictionary  *added in community.aws 4.1.0* | A dict of Route53 health check details returned by get_health_check in boto3.  **Returned:** when *query=health_check* and *health_check_method=details* |
| **caller_reference**  string | A unique string that you specified when you created the health check.  **Returned:** success  **Sample:** `"01d0db12-x0x9-12a3-1234-0z000z00zz0z"` |
| **health_check_config**  dictionary | A dict that contains detailed information about one health check.  **Returned:** success |
| **disabled**  boolean | Whether Route53 should stop performing health checks on a endpoint.  **Returned:** success  **Sample:** `false` |
| **enable_sni**  boolean | Whether Route53 should send value of FullyQualifiedDomainName to endpoint in client_hello message during TLS negotiation.  **Returned:** success  **Sample:** `true` |
| **failure_threshold**  integer | The number of consecutive health checks that an endpoint must pass/fail for Route53 to change current status of endpoint.  **Returned:** success  **Sample:** `3` |
| **fully_qualified_domain_name**  string | The fully qualified DNS name of the endpoint on which Route53 performs health checks.  **Returned:** success  **Sample:** `"hello"` |
| **inverted**  boolean | Whether Route53 should invert the status of a health check.  **Returned:** success  **Sample:** `false` |
| **ip_address**  string | The IPv4/IPv6 IP address of the endpoint that Route53 should perform health checks on.  **Returned:** success  **Sample:** `"192.0.2.44"` |
| **measure_latency**  boolean | Whether Route53 should measure latency between health checkers in multiple AWS regions and the endpoint.  **Returned:** success  **Sample:** `false` |
| **port**  integer | The port of the endpoint that Route53 should perform health checks on.  **Returned:** success  **Sample:** `80` |
| **request_interval**  integer | The number of seconds between the time that Route53 gets a response from endpoint and the next health check request.  **Returned:** success  **Sample:** `30` |
| **resource_path**  string | The path that Route53 requests when performing health checks.  **Returned:** success  **Sample:** `"/welcome.html"` |
| **search_string**  string | The string that Route53 uses to search for in the response body from specified resource.  **Returned:** success  **Sample:** `"test-string-to-match"` |
| **type**  string | The type of the health check.  **Returned:** success  **Sample:** `"HTTPS"` |
| **health_check_version**  string | The version of the health check.  **Returned:** success  **Sample:** `"1"` |
| **id**  string | The identifier that Amazon Route53 assigned to the health check at the time of creation.  **Returned:** success  **Sample:** `"12345cdc-2cc4-1234-bed2-123456abc1a2"` |
| **health_check_observations**  list / elements=dictionary  *added in amazon.aws 5.4.0* | A dict of Route53 health check details returned by get_health_check_status and get_health_check_last_failure_reason in boto3.  **Returned:** when *query=health_check* and *health_check_method=status* or *health_check_method=failure_reason* |
| **ip_address**  string | The IP address of the Amazon Route 53 health checker that provided the failure reason in StatusReport.  **Returned:** success  **Sample:** `"12.345.67.89"` |
| **region**  string | The region of the Amazon Route 53 health checker that provided the status in StatusReport.  **Returned:** success  **Sample:** `"us-west-1"` |
| **status_report**  dictionary | A complex type that contains the last failure reason and the time of the failed health check.  **Returned:** success |
| **checked_time**  string | The date and time that the health checker performed the health check in ISO 8601 format and Coordinated Universal Time (UTC).  **Returned:** success  **Sample:** `"2023-03-08T23:10:08.452000+00:00"` |
| **status**  string | A description of the status of the health check endpoint as reported by one of the Amazon Route 53 health checkers.  **Returned:** success  **Sample:** `"Failure: Resolved IP: 12.345.67.89. The connection was closed by the endpoint."` |
| **health_checks**  list / elements=dictionary  *added in community.aws 4.0.0* | A list of Route53 health checks returned by list_health_checks in boto3.  **Returned:** when *query=health_check* |
| **caller_reference**  string | A unique string that you specified when you created the health check.  **Returned:** success  **Sample:** `"01d0db12-x0x9-12a3-1234-0z000z00zz0z"` |
| **health_check_config**  dictionary | A dict that contains detailed information about one health check.  **Returned:** success |
| **disabled**  boolean | Whether Route53 should stop performing health checks on a endpoint.  **Returned:** success  **Sample:** `false` |
| **enable_sni**  boolean | Whether Route53 should send value of FullyQualifiedDomainName to endpoint in client_hello message during TLS negotiation.  **Returned:** success  **Sample:** `true` |
| **failure_threshold**  integer | The number of consecutive health checks that an endpoint must pass/fail for Route53 to change current status of endpoint.  **Returned:** success  **Sample:** `3` |
| **fully_qualified_domain_name**  string | The fully qualified DNS name of the endpoint on which Route53 performs health checks.  **Returned:** success  **Sample:** `"hello"` |
| **inverted**  boolean | Whether Route53 should invert the status of a health check.  **Returned:** success  **Sample:** `false` |
| **ip_address**  string | The IPv4/IPv6 IP address of the endpoint that Route53 should perform health checks on.  **Returned:** success  **Sample:** `"192.0.2.44"` |
| **measure_latency**  boolean | Whether Route53 should measure latency between health checkers in multiple AWS regions and the endpoint.  **Returned:** success  **Sample:** `false` |
| **port**  integer | The port of the endpoint that Route53 should perform health checks on.  **Returned:** success  **Sample:** `80` |
| **request_interval**  integer | The number of seconds between the time that Route53 gets a response from endpoint and the next health check request.  **Returned:** success  **Sample:** `30` |
| **resource_path**  string | The path that Route53 requests when performing health checks.  **Returned:** success  **Sample:** `"/welcome.html"` |
| **search_string**  string | The string that Route53 uses to search for in the response body from specified resource.  **Returned:** success  **Sample:** `"test-string-to-match"` |
| **type**  string | The type of the health check.  **Returned:** success  **Sample:** `"HTTPS"` |
| **health_check_version**  string | The version of the health check.  **Returned:** success  **Sample:** `"1"` |
| **id**  string | The identifier that Amazon Route53 assigned to the health check at the time of creation.  **Returned:** success  **Sample:** `"12345cdc-2cc4-1234-bed2-123456abc1a2"` |
| **HealthCheck**  dictionary | A deprecated CamelCased dict of Route53 health check details returned by get_health_check in boto3. \ This dict contains same elements/parameters as it’s snake_cased version mentioned above. \ This field is deprecated and will be removed in 6.0.0 version release.  **Returned:** when *query=health_check* and *health_check_method=details* |
| **HealthChecks**  list / elements=dictionary | A deprecated CamelCased list of Route53 health checks returned by list_health_checks in boto3. \ This list contains same elements/parameters as it’s snake_cased version mentioned above. \ This field is deprecated and will be removed in 6.0.0 version release.  **Returned:** when *query=health_check* |
| **hosted_zones**  list / elements=dictionary  *added in community.aws 4.0.0* | A list of hosted zones returned by list_hosted_zones in boto3.  **Returned:** when *query=hosted_zone* |
| **caller_reference**  string | The value specified for CallerReference at the time of hosted zone creation.  **Returned:** success  **Sample:** `"01d0db12-x0x9-12a3-1234-0z000z00zz0z"` |
| **config**  dictionary | A dict that contains Comment and PrivateZone elements.  **Returned:** success |
| **comment**  string | Any comments that included about in the hosted zone.  **Returned:** success  **Sample:** `"HostedZone created by Route53 Registrar"` |
| **private_zone**  boolean | A value that indicates whether this is a private hosted zone or not.  **Returned:** success  **Sample:** `false` |
| **id**  string | The ID of the hosted zone assigned by Amazon Route53 to the hosted zone at the creation time.  **Returned:** success  **Sample:** `"/hostedzone/Z01234567AB1234567890"` |
| **name**  string | The name of the domain.  **Returned:** success  **Sample:** `"example.io"` |
| **resource_record_set_count**  integer | The number of resource record sets in the hosted zone.  **Returned:** success  **Sample:** `3` |
| **HostedZones**  list / elements=dictionary | A deprecated CamelCased list of hosted zones returned by list_hosted_zones in boto3. \ This list contains same elements/parameters as it’s snake_cased version mentioned above. \ This field is deprecated and will be removed in 6.0.0 version release.  **Returned:** when *query=hosted_zone* |
| **resource_record_sets**  list / elements=dictionary  *added in community.aws 4.0.0* | A list of resource record sets returned by list_resource_record_sets in boto3.  **Returned:** when *query=record_sets* |
| **geo_location**  dictionary | The specified geographic location for which the Route53 responds to based on location.  **Returned:** success |
| **continent_code**  string | The two-letter code for the continent.  **Returned:** success  **Sample:** `"NA"` |
| **country_code**  string | The two-letter code for a country.  **Returned:** success  **Sample:** `"US"` |
| **subdivision_code**  string | The two-letter code for a state of the United States  **Returned:** success  **Sample:** `"NY"` |
| **name**  string | The name of a record in the specified hosted zone.  **Returned:** success  **Sample:** `"www.example.com"` |
| **resource_records**  list / elements=dictionary | Information about the resource records.  **Returned:** success |
| **value**  string | The current or new DNS record value.  **Returned:** success  **Sample:** `"ns-12.awsdns-34.com."` |
| **set_identifier**  string | An identifier that differentiates among multiple resource record sets that have the same combination of name and type.  **Returned:** success  **Sample:** `"abcd"` |
| **ttl**  integer | The resource record cache time to live (TTL), in seconds.  **Returned:** success  **Sample:** `60` |
| **type**  string | The DNS record type.  **Returned:** success  **Sample:** `"A"` |
| **ResourceRecordSets**  list / elements=dictionary | A deprecated CamelCased list of resource record sets returned by list_resource_record_sets in boto3. \ This list contains same elements/parameters as it’s snake_cased version mentioned above. \ This field is deprecated and will be removed in 6.0.0 version release.  **Returned:** when *query=record_sets* |

### Authors

- Karen Cheng (@Etherdaemon)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
