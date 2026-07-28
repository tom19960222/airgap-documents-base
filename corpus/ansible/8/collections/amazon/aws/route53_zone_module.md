---
collection: ansible
version: "8"
title: "amazon.aws.route53_zone module – add or delete Route53 zones"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/route53_zone_module.html
fetched_at: 2026-07-28T01:07:13+00:00
---
# amazon.aws.route53_zone module – add or delete Route53 zones

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
> see [Requirements](route53_zone_module.md#ansible-collections-amazon-aws-route53-zone-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.route53_zone`.

New in amazon.aws 5.0.0

- [Synopsis](route53_zone_module.md#synopsis)
- [Requirements](route53_zone_module.md#requirements)
- [Parameters](route53_zone_module.md#parameters)
- [Notes](route53_zone_module.md#notes)
- [Examples](route53_zone_module.md#examples)
- [Return Values](route53_zone_module.md#return-values)

## [Synopsis](route53_zone_module.md#id1)

- Creates and deletes Route53 private and public zones.
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](route53_zone_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](route53_zone_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **comment**  string | Comment associated with the zone.  **Default:** `""` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **delegation_set_id**  string | The reusable delegation set ID to be associated with the zone.  Note that you can’t associate a reusable delegation set with a private hosted zone. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **hosted_zone_id**  string | The unique zone identifier you want to delete or “all” if there are many zones with the same domain name.  Required if there are multiple zones identified with the above options. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Whether or not the zone should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **vpc_id**  string | The VPC ID the zone should be a part of (if this is going to be a private zone). |
| **vpc_region**  string | The VPC Region the zone should be a part of (if this is going to be a private zone). |
| **vpcs**  list / elements=dictionary  *added in amazon.aws 5.3.0* | The VPCs the zone should be a part of (if this is going to be a private zone). |
| **id**  string / required | The ID of the VPC. |
| **region**  string / required | The region of the VPC. |
| **zone**  string / required | The DNS zone record (eg: foo.com.) |

## [Notes](route53_zone_module.md#id4)

> **Note:**
>
> - Support for *tags* and *purge_tags* was added in release 2.1.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](route53_zone_module.md#id5)

```yaml+jinja
- name: create a public zone
  amazon.aws.route53_zone:
    zone: example.com
    comment: this is an example

- name: delete a public zone
  amazon.aws.route53_zone:
    zone: example.com
    state: absent

- name: create a private zone
  amazon.aws.route53_zone:
    zone: devel.example.com
    vpc_id: '{{ myvpc_id }}'
    vpc_region: us-west-2
    comment: developer domain

- name: create a private zone with multiple associated VPCs
  amazon.aws.route53_zone:
    zone: crossdevel.example.com
    vpcs:
      - id: vpc-123456
        region: us-west-2
      - id: vpc-000001
        region: us-west-2
    comment: developer cross-vpc domain

- name: create a public zone associated with a specific reusable delegation set
  amazon.aws.route53_zone:
    zone: example.com
    comment: reusable delegation set example
    delegation_set_id: A1BCDEF2GHIJKL

- name: create a public zone with tags
  amazon.aws.route53_zone:
    zone: example.com
    comment: this is an example
    tags:
        Owner: Ansible Team

- name: modify a public zone, removing all previous tags and adding a new one
  amazon.aws.route53_zone:
    zone: example.com
    comment: this is an example
    tags:
        Support: Ansible Community
    purge_tags: true
```

## [Return Values](route53_zone_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **comment**  string | optional hosted zone comment  **Returned:** when hosted zone exists  **Sample:** `"Private zone"` |
| **delegation_set_id**  string | id of the associated reusable delegation set  **Returned:** for public hosted zones, if they have been associated with a reusable delegation set  **Sample:** `"A1BCDEF2GHIJKL"` |
| **name**  string | hosted zone name  **Returned:** when hosted zone exists  **Sample:** `"private.local."` |
| **private_zone**  boolean | whether hosted zone is private or public  **Returned:** when hosted zone exists  **Sample:** `true` |
| **tags**  dictionary | tags associated with the zone  **Returned:** when tags are defined |
| **vpc_id**  string | id of the first vpc attached to private hosted zone (use vpcs for associating multiple).  **Returned:** for private hosted zone  **Sample:** `"vpc-1d36c84f"` |
| **vpc_region**  string | region of the first vpc attached to private hosted zone (use vpcs for assocaiting multiple).  **Returned:** for private hosted zone  **Sample:** `"eu-west-1"` |
| **vpcs**  list / elements=dictionary  *added in amazon.aws 5.3.0* | The list of VPCs attached to the private hosted zone  **Returned:** for private hosted zone  **Sample:** `"[{'id': 'vpc-123456', 'region': 'us-west-2'}]"` |
| **id**  string | ID of the VPC  **Returned:** for private hosted zone  **Sample:** `"vpc-123456"` |
| **region**  string | Region of the VPC  **Returned:** for private hosted zone  **Sample:** `"eu-west-2"` |
| **zone_id**  string | hosted zone id  **Returned:** when hosted zone exists  **Sample:** `"Z6JQG9820BEFMW"` |

### Authors

- Christopher Troup (@minichate)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
