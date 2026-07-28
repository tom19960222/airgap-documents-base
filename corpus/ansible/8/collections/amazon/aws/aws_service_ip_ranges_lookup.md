---
collection: ansible
version: "8"
title: "amazon.aws.aws_service_ip_ranges lookup – Look up the IP ranges for services provided in AWS such as EC2 and S3."
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/aws_service_ip_ranges_lookup.html
fetched_at: 2026-07-28T01:07:20+00:00
---
# amazon.aws.aws_service_ip_ranges lookup – Look up the IP ranges for services provided in AWS such as EC2 and S3.

> **Note:**
>
> This lookup plugin is part of the [amazon.aws collection](https://galaxy.ansible.com/ui/repo/published/amazon/aws/) (version 6.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](aws_service_ip_ranges_lookup.md#ansible-collections-amazon-aws-aws-service-ip-ranges-lookup-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.aws_service_ip_ranges`.

- [Synopsis](aws_service_ip_ranges_lookup.md#synopsis)
- [Requirements](aws_service_ip_ranges_lookup.md#requirements)
- [Keyword parameters](aws_service_ip_ranges_lookup.md#keyword-parameters)
- [Examples](aws_service_ip_ranges_lookup.md#examples)
- [Return Value](aws_service_ip_ranges_lookup.md#return-value)

## [Synopsis](aws_service_ip_ranges_lookup.md#id1)

- AWS publishes IP ranges used on the public internet by EC2, S3, CloudFront, CodeBuild, Route53, and Route53 Health Checking.
- This module produces a list of all the ranges (by default) or can narrow down the list to the specified region or service.

## [Requirements](aws_service_ip_ranges_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- must have public internet connectivity

## [Keyword parameters](aws_service_ip_ranges_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('amazon.aws.aws_service_ip_ranges', key1=value1, key2=value2, ...)` and `query('amazon.aws.aws_service_ip_ranges', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **ipv6_prefixes**  string  *added in amazon.aws 2.1.0* | When *ipv6_prefixes=True* the lookup will return ipv6 addresses instead of ipv4 addresses |
| **region**  string | The AWS region to narrow the ranges to. Examples: us-east-1, eu-west-2, ap-southeast-1 |
| **service**  string | The service to filter ranges by. Options: EC2, S3, CLOUDFRONT, CODEbUILD, ROUTE53, ROUTE53_HEALTHCHECKS |

## [Examples](aws_service_ip_ranges_lookup.md#id4)

```yaml+jinja
vars:
  ec2_ranges: "{{ lookup('aws_service_ip_ranges', region='ap-southeast-2', service='EC2', wantlist=True) }}"
tasks:

- name: "use list return option and iterate as a loop"
  debug: msg="{% for cidr in ec2_ranges %}{{ cidr }} {% endfor %}"
# "52.62.0.0/15 52.64.0.0/17 52.64.128.0/17 52.65.0.0/16 52.95.241.0/24 52.95.255.16/28 54.66.0.0/16 "

- name: "Pull S3 IP ranges, and print the default return style"
  debug: msg="{{ lookup('aws_service_ip_ranges', region='us-east-1', service='S3') }}"
# "52.92.16.0/20,52.216.0.0/15,54.231.0.0/17"
```

## [Return Value](aws_service_ip_ranges_lookup.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | comma-separated list of CIDR ranges  **Returned:** success |

### Authors

- James Turner

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
