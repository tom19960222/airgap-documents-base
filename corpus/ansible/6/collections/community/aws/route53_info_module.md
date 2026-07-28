---
collection: ansible
version: "6"
title: "community.aws.route53_info module – Retrieves route53 details using AWS methods"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/route53_info_module.html
fetched_at: 2026-07-27T17:05:00+00:00
---
# community.aws.route53_info module – Retrieves route53 details using AWS methods

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
> see [Requirements](route53_info_module.md#ansible-collections-community-aws-route53-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.route53_info`.

New in community.aws 1.0.0

- [Synopsis](route53_info_module.md#synopsis)
- [Requirements](route53_info_module.md#requirements)
- [Parameters](route53_info_module.md#parameters)
- [Notes](route53_info_module.md#notes)
- [Examples](route53_info_module.md#examples)

## [Synopsis](route53_info_module.md#id1)

- Gets various details related to Route53 zone, record set or health check details.

## [Requirements](route53_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](route53_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **change_id**  string | The ID of the change batch request.  The value that you specify here is the value that ChangeResourceRecordSets returned in the Id element when you submitted the request.  Required if *query=change*. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **delegation_set_id**  string | The DNS Zone delegation set ID. |
| **dns_name**  string | The first name in the lexicographic ordering of domain names that you want the list_command to start listing from. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **health_check_id**  string | The ID of the health check.  Required if `query` is set to `health_check` and `health_check_method` is set to `details` or `status` or `failure_reason`. |
| **health_check_method**  string | This is used in conjunction with query: health_check. It allows for listing details, counts or tags of various health check details.  Choices:   - `"list"` ← (default) - `"details"` - `"status"` - `"failure_reason"` - `"count"` - `"tags"` |
| **hosted_zone_id**  string | The Hosted Zone ID of the DNS zone.  Required if *query* is set to *hosted_zone* and *hosted_zone_method* is set to *details*.  Required if *query* is set to *record_sets*. |
| **hosted_zone_method**  string | This is used in conjunction with query: hosted_zone. It allows for listing details, counts or tags of various hosted zone details.  Choices:   - `"details"` - `"list"` ← (default) - `"list_by_name"` - `"count"` - `"tags"` |
| **max_items**  integer | Maximum number of items to return for various get/list requests. |
| **next_marker**  string | Some requests such as list_command: hosted_zones will return a maximum number of entries - EG 100 or the number specified by *max_items*. If the number of entries exceeds this maximum another request can be sent using the NextMarker entry from the first response to get the next page of results. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **query**  string / required | Specifies the query action to take.  Choices:   - `"change"` - `"checker_ip_range"` - `"health_check"` - `"hosted_zone"` - `"record_sets"` - `"reusable_delegation_set"` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **resource_id**  aliases: resource_ids  list / elements=string | The ID/s of the specified resource/s.  Required if *query=health_check* and *health_check_method=tags*.  Required if *query=hosted_zone* and *hosted_zone_method=tags*. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **start_record_name**  string | The first name in the lexicographic ordering of domain names that you want the list_command: record_sets to start listing from. |
| **type**  string | The type of DNS record.  Choices:   - `"A"` - `"CNAME"` - `"MX"` - `"AAAA"` - `"TXT"` - `"PTR"` - `"SRV"` - `"SPF"` - `"CAA"` - `"NS"` - `"NAPTR"` - `"SOA"` - `"DS"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](route53_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](route53_info_module.md#id5)

```yaml+jinja
# Simple example of listing all hosted zones
- name: List all hosted zones
  community.aws.route53_info:
    query: hosted_zone
  register: hosted_zones

# Getting a count of hosted zones
- name: Return a count of all hosted zones
  community.aws.route53_info:
    query: hosted_zone
    hosted_zone_method: count
  register: hosted_zone_count

- name: List the first 20 resource record sets in a given hosted zone
  community.aws.route53_info:
    profile: account_name
    query: record_sets
    hosted_zone_id: ZZZ1111112222
    max_items: 20
  register: record_sets

- name: List first 20 health checks
  community.aws.route53_info:
    query: health_check
    health_check_method: list
    max_items: 20
  register: health_checks

- name: Get health check last failure_reason
  community.aws.route53_info:
    query: health_check
    health_check_method: failure_reason
    health_check_id: 00000000-1111-2222-3333-12345678abcd
  register: health_check_failure_reason

- name: Retrieve reusable delegation set details
  community.aws.route53_info:
    query: reusable_delegation_set
    delegation_set_id: delegation id
  register: delegation_sets

- name: setup of example for using next_marker
  community.aws.route53_info:
    query: hosted_zone
    max_items: 1
  register: first_info

- name: example for using next_marker
  community.aws.route53_info:
    query: hosted_zone
    next_marker: "{{ first_info.NextMarker }}"
    max_items: 1
  when: "{{ 'NextMarker' in first_info }}"

- name: retrieve host entries starting with host1.workshop.test.io
  block:
    - name: grab zone id
      community.aws.route53_zone:
        zone: "test.io"
      register: AWSINFO

    - name: grab Route53 record information
      community.aws.route53_info:
        type: A
        query: record_sets
        hosted_zone_id: "{{ AWSINFO.zone_id }}"
        start_record_name: "host1.workshop.test.io"
      register: RECORDS
```

### Authors

- Karen Cheng (@Etherdaemon)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
