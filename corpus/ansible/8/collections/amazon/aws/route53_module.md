---
collection: ansible
version: "8"
title: "amazon.aws.route53 module – add or delete entries in Amazons Route 53 DNS service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/route53_module.html
fetched_at: 2026-07-28T01:07:11+00:00
---
# amazon.aws.route53 module – add or delete entries in Amazons Route 53 DNS service

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
> see [Requirements](route53_module.md#ansible-collections-amazon-aws-route53-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.route53`.

New in amazon.aws 5.0.0

- [Synopsis](route53_module.md#synopsis)
- [Requirements](route53_module.md#requirements)
- [Parameters](route53_module.md#parameters)
- [Notes](route53_module.md#notes)
- [Examples](route53_module.md#examples)
- [Return Values](route53_module.md#return-values)

## [Synopsis](route53_module.md#id1)

- Creates and deletes DNS records in Amazons Route 53 service.
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](route53_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](route53_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **alias**  boolean | Indicates if this is an alias record.  Mutually exclusive with *ttl*.  Defaults to `false`.  **Choices:**   - `false` - `true` |
| **alias_evaluate_target_health**  boolean | Whether or not to evaluate an alias target health. Useful for aliases to Elastic Load Balancers.  **Choices:**   - `false` ← (default) - `true` |
| **alias_hosted_zone_id**  string | The hosted zone identifier. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **failover**  string | Failover resource record sets only. Whether this is the primary or secondary resource record set. Allowed values are PRIMARY and SECONDARY  Mutually exclusive with *weight* and *region*.  **Choices:**   - `"SECONDARY"` - `"PRIMARY"` |
| **geo_location**  dictionary  *added in community.aws 3.3.0* | Allows to control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query.  Two geolocation resource record sets that specify same geographic location cannot be created.  Non-geolocation resource record sets that have the same values for the Name and Type elements as geolocation resource record sets cannot be created. |
| **continent_code**  string | The two-letter code for the continent.  Specifying *continent_code* with either *country_code* or *subdivision_code* returns an InvalidInput error. |
| **country_code**  string | The two-letter code for a country.  Amazon Route 53 uses the two-letter country codes that are specified in ISO standard 3166-1 alpha-2 . |
| **subdivision_code**  string | The two-letter code for a state of the United States.  To specify *subdivision_code*, *country_code* must be set to `US`. |
| **health_check**  string | Health check to associate with this record |
| **hosted_zone_id**  string | The Hosted Zone ID of the DNS zone to modify.  This is a required parameter, if parameter *zone* is not supplied. |
| **identifier**  string | Have to be specified for Weighted, latency-based and failover resource record sets only. An identifier that differentiates among multiple resource record sets that have the same combination of DNS name and type. |
| **overwrite**  boolean | Whether an existing record should be overwritten on create if values do not match.  **Choices:**   - `false` - `true` |
| **private_zone**  boolean | If set to `true`, the private zone matching the requested name within the domain will be used if there are both public and private zones.  The default is to use the public zone.  **Choices:**   - `false` ← (default) - `true` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **record**  string / required | The full DNS record to create or delete. |
| **region**  string | Latency-based resource record sets only Among resource record sets that have the same combination of DNS name and type, a value that determines which region this should be associated with for the latency-based routing  Mutually exclusive with *weight* and *failover*. |
| **retry_interval**  integer | In the case that Route 53 is still servicing a prior request, this module will wait and try again after this many seconds. If you have many domain names, the default of `500` seconds may be too long.  **Default:** `500` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  aliases: command  string / required | Specifies the state of the resource record.  **Choices:**   - `"present"` - `"absent"` - `"get"` - `"create"` - `"delete"` |
| **ttl**  integer | The TTL, in second, to give the new record.  Mutually exclusive with *alias*.  **Default:** `3600` |
| **type**  string / required | The type of DNS record to create.  **Choices:**   - `"A"` - `"CNAME"` - `"MX"` - `"AAAA"` - `"TXT"` - `"PTR"` - `"SRV"` - `"SPF"` - `"CAA"` - `"NS"` - `"SOA"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **value**  list / elements=string | The new value when creating a DNS record. YAML lists or multiple comma-spaced values are allowed for non-alias records. |
| **vpc_id**  string | When used in conjunction with private_zone: true, this will only modify records in the private hosted zone attached to this VPC.  This allows you to have multiple private hosted zones, all with the same name, attached to different VPCs. |
| **wait**  boolean | Wait until the changes have been replicated to all Amazon Route 53 DNS servers.  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How long to wait for the changes to be replicated, in seconds.  **Default:** `300` |
| **weight**  integer | Weighted resource record sets only. Among resource record sets that have the same combination of DNS name and type, a value that determines what portion of traffic for the current resource record set is routed to the associated location.  Mutually exclusive with *region* and *failover*. |
| **zone**  string | The DNS zone to modify.  This is a required parameter, if parameter *hosted_zone_id* is not supplied. |

## [Notes](route53_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](route53_module.md#id5)

```yaml+jinja
- name: Add new.foo.com as an A record with 3 IPs and wait until the changes have been replicated
  amazon.aws.route53:
    state: present
    zone: foo.com
    record: new.foo.com
    type: A
    ttl: 7200
    value: 1.1.1.1,2.2.2.2,3.3.3.3
    wait: true
- name: Update new.foo.com as an A record with a list of 3 IPs and wait until the changes have been replicated
  amazon.aws.route53:
    state: present
    zone: foo.com
    record: new.foo.com
    type: A
    ttl: 7200
    value:
      - 1.1.1.1
      - 2.2.2.2
      - 3.3.3.3
    wait: true
- name: Retrieve the details for new.foo.com
  amazon.aws.route53:
    state: get
    zone: foo.com
    record: new.foo.com
    type: A
  register: rec
- name: Delete new.foo.com A record using the results from the get command
  amazon.aws.route53:
    state: absent
    zone: foo.com
    record: "{{ rec.set.record }}"
    ttl: "{{ rec.set.ttl }}"
    type: "{{ rec.set.type }}"
    value: "{{ rec.set.value }}"
# Add an AAAA record.  Note that because there are colons in the value
# that the IPv6 address must be quoted. Also shows using the old form command=create.
- name: Add an AAAA record
  amazon.aws.route53:
    command: create
    zone: foo.com
    record: localhost.foo.com
    type: AAAA
    ttl: 7200
    value: "::1"
# For more information on SRV records see:
# https://en.wikipedia.org/wiki/SRV_record
- name: Add a SRV record with multiple fields for a service on port 22222
  amazon.aws.route53:
    state: present
    zone: foo.com
    record: "_example-service._tcp.foo.com"
    type: SRV
    value: "0 0 22222 host1.foo.com,0 0 22222 host2.foo.com"
# Note that TXT and SPF records must be surrounded
# by quotes when sent to Route 53:
- name: Add a TXT record.
  amazon.aws.route53:
    state: present
    zone: foo.com
    record: localhost.foo.com
    type: TXT
    ttl: 7200
    value: '"bar"'
- name: Add an alias record that points to an Amazon ELB
  amazon.aws.route53:
    state: present
    zone: foo.com
    record: elb.foo.com
    type: A
    value: "{{ elb_dns_name }}"
    alias: True
    alias_hosted_zone_id: "{{ elb_zone_id }}"
- name: Retrieve the details for elb.foo.com
  amazon.aws.route53:
    state: get
    zone: foo.com
    record: elb.foo.com
    type: A
  register: rec
- name: Delete an alias record using the results from the get command
  amazon.aws.route53:
    state: absent
    zone: foo.com
    record: "{{ rec.set.record }}"
    ttl: "{{ rec.set.ttl }}"
    type: "{{ rec.set.type }}"
    value: "{{ rec.set.value }}"
    alias: True
    alias_hosted_zone_id: "{{ rec.set.alias_hosted_zone_id }}"
- name: Add an alias record that points to an Amazon ELB and evaluates it health
  amazon.aws.route53:
    state: present
    zone: foo.com
    record: elb.foo.com
    type: A
    value: "{{ elb_dns_name }}"
    alias: True
    alias_hosted_zone_id: "{{ elb_zone_id }}"
    alias_evaluate_target_health: True
- name: Add an AAAA record with Hosted Zone ID
  amazon.aws.route53:
    state: present
    zone: foo.com
    hosted_zone_id: Z2AABBCCDDEEFF
    record: localhost.foo.com
    type: AAAA
    ttl: 7200
    value: "::1"
- name: Use a routing policy to distribute traffic
  amazon.aws.route53:
    state: present
    zone: foo.com
    record: www.foo.com
    type: CNAME
    value: host1.foo.com
    ttl: 30
    # Routing policy
    identifier: "host1@www"
    weight: 100
    health_check: "d994b780-3150-49fd-9205-356abdd42e75"
- name: Add a CAA record (RFC 6844)
  amazon.aws.route53:
    state: present
    zone: example.com
    record: example.com
    type: CAA
    value:
      - 0 issue "ca.example.net"
      - 0 issuewild ";"
      - 0 iodef "mailto:security@example.com"
- name: Create a record with geo_location - country_code
  amazon.aws.route53:
    state: present
    zone: '{{ zone_one }}'
    record: 'geo-test.{{ zone_one }}'
    identifier: "geohost@www"
    type: A
    value: 1.1.1.1
    ttl: 30
    geo_location:
      country_code: US
- name: Create a record with geo_location - subdivision code
  amazon.aws.route53:
    state: present
    zone: '{{ zone_one }}'
    record: 'geo-test.{{ zone_one }}'
    identifier: "geohost@www"
    type: A
    value: 1.1.1.1
    ttl: 30
    geo_location:
      country_code: US
      subdivision_code: TX
```

## [Return Values](route53_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **nameservers**  list / elements=string | Nameservers associated with the zone.  **Returned:** when state is ‘get’  **Sample:** `["ns-1036.awsdns-00.org.", "ns-516.awsdns-00.net.", "ns-1504.awsdns-00.co.uk.", "ns-1.awsdns-00.com."]` |
| **set**  complex | Info specific to the resource record.  **Returned:** when state is ‘get’ |
| **alias**  boolean | Whether this is an alias.  **Returned:** always  **Sample:** `false` |
| **failover**  string | Whether this is the primary or secondary resource record set.  **Returned:** always  **Sample:** `"PRIMARY"` |
| **geo_location**  dictionary  *added in community.aws 3.3.0* | geograpic location based on which Route53 resonds to DNS queries.  **Returned:** when configured  **Sample:** `{"continent_code": "NA", "country_code": "US", "subdivision_code": "CA"}` |
| **health_check**  string | health_check associated with this record.  **Returned:** always |
| **identifier**  string | An identifier that differentiates among multiple resource record sets that have the same combination of DNS name and type.  **Returned:** always |
| **record**  string | Domain name for the record set.  **Returned:** always  **Sample:** `"new.foo.com."` |
| **region**  string | Which region this should be associated with for latency-based routing.  **Returned:** always  **Sample:** `"us-west-2"` |
| **ttl**  string | Resource record cache TTL.  **Returned:** always  **Sample:** `"3600"` |
| **type**  string | Resource record set type.  **Returned:** always  **Sample:** `"A"` |
| **value**  string | Record value.  **Returned:** always  **Sample:** `"52.43.18.27"` |
| **values**  list / elements=string | Record Values.  **Returned:** always  **Sample:** `["52.43.18.27"]` |
| **weight**  string | Weight of the record.  **Returned:** always  **Sample:** `"3"` |
| **zone**  string | Zone this record set belongs to.  **Returned:** always  **Sample:** `"foo.bar.com."` |
| **wait_id**  string  *added in amazon.aws 6.3.0* | The wait ID for the applied change. Can be used to wait for the change to propagate later on when *wait=false*.  **Returned:** when changed |

### Authors

- Bruce Pennypacker (@bpennypacker)
- Mike Buzzetti (@jimbydamonk)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
