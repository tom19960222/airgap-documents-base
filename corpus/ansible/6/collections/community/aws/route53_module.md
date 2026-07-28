---
collection: ansible
version: "6"
title: "community.aws.route53 module – add or delete entries in Amazons Route 53 DNS service"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/route53_module.html
fetched_at: 2026-07-27T17:04:58+00:00
---
# community.aws.route53 module – add or delete entries in Amazons Route 53 DNS service

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
> see [Requirements](route53_module.md#ansible-collections-community-aws-route53-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.route53`.

New in community.aws 1.0.0

- [Synopsis](route53_module.md#synopsis)
- [Requirements](route53_module.md#requirements)
- [Parameters](route53_module.md#parameters)
- [Notes](route53_module.md#notes)
- [Examples](route53_module.md#examples)
- [Return Values](route53_module.md#return-values)

## [Synopsis](route53_module.md#id1)

- Creates and deletes DNS records in Amazons Route 53 service.

## [Requirements](route53_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](route53_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alias**  boolean | Indicates if this is an alias record.  Mutually exclusive with *ttl*.  Defaults to `false`.  Choices:   - `false` - `true` |
| **alias_evaluate_target_health**  boolean | Whether or not to evaluate an alias target health. Useful for aliases to Elastic Load Balancers.  Choices:   - `false` ← (default) - `true` |
| **alias_hosted_zone_id**  string | The hosted zone identifier. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **failover**  string | Failover resource record sets only. Whether this is the primary or secondary resource record set. Allowed values are PRIMARY and SECONDARY  Mutually exclusive with *weight* and *region*.  Choices:   - `"SECONDARY"` - `"PRIMARY"` |
| **geo_location**  dictionary  added in community.aws 3.3.0 | Allows to control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query.  Two geolocation resource record sets that specify same geographic location cannot be created.  Non-geolocation resource record sets that have the same values for the Name and Type elements as geolocation resource record sets cannot be created. |
| **continent_code**  string | The two-letter code for the continent.  Specifying *continent_code* with either *country_code* or *subdivision_code* returns an InvalidInput error. |
| **country_code**  string | The two-letter code for a country.  Amazon Route 53 uses the two-letter country codes that are specified in ISO standard 3166-1 alpha-2 . |
| **subdivision_code**  string | The two-letter code for a state of the United States.  To specify *subdivision_code*, *country_code* must be set to `US`. |
| **health_check**  string | Health check to associate with this record |
| **hosted_zone_id**  string | The Hosted Zone ID of the DNS zone to modify.  This is a required parameter, if parameter *zone* is not supplied. |
| **identifier**  string | Have to be specified for Weighted, latency-based and failover resource record sets only. An identifier that differentiates among multiple resource record sets that have the same combination of DNS name and type. |
| **overwrite**  boolean | Whether an existing record should be overwritten on create if values do not match.  Choices:   - `false` - `true` |
| **private_zone**  boolean | If set to `true`, the private zone matching the requested name within the domain will be used if there are both public and private zones.  The default is to use the public zone.  Choices:   - `false` ← (default) - `true` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **record**  string / required | The full DNS record to create or delete. |
| **region**  string | Latency-based resource record sets only Among resource record sets that have the same combination of DNS name and type, a value that determines which region this should be associated with for the latency-based routing  Mutually exclusive with *weight* and *failover*. |
| **retry_interval**  integer | In the case that Route 53 is still servicing a prior request, this module will wait and try again after this many seconds. If you have many domain names, the default of `500` seconds may be too long.  Default: `500` |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  aliases: command  string / required | Specifies the state of the resource record.  Choices:   - `"present"` - `"absent"` - `"get"` - `"create"` - `"delete"` |
| **ttl**  integer | The TTL, in second, to give the new record.  Mutually exclusive with *alias*.  Default: `3600` |
| **type**  string / required | The type of DNS record to create.  Choices:   - `"A"` - `"CNAME"` - `"MX"` - `"AAAA"` - `"TXT"` - `"PTR"` - `"SRV"` - `"SPF"` - `"CAA"` - `"NS"` - `"SOA"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **value**  list / elements=string | The new value when creating a DNS record. YAML lists or multiple comma-spaced values are allowed for non-alias records. |
| **vpc_id**  string | When used in conjunction with private_zone: true, this will only modify records in the private hosted zone attached to this VPC.  This allows you to have multiple private hosted zones, all with the same name, attached to different VPCs. |
| **wait**  boolean | Wait until the changes have been replicated to all Amazon Route 53 DNS servers.  Choices:   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How long to wait for the changes to be replicated, in seconds.  Default: `300` |
| **weight**  integer | Weighted resource record sets only. Among resource record sets that have the same combination of DNS name and type, a value that determines what portion of traffic for the current resource record set is routed to the associated location.  Mutually exclusive with *region* and *failover*. |
| **zone**  string | The DNS zone to modify.  This is a required parameter, if parameter *hosted_zone_id* is not supplied. |

## [Notes](route53_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](route53_module.md#id5)

```yaml+jinja
- name: Add new.foo.com as an A record with 3 IPs and wait until the changes have been replicated
  community.aws.route53:
    state: present
    zone: foo.com
    record: new.foo.com
    type: A
    ttl: 7200
    value: 1.1.1.1,2.2.2.2,3.3.3.3
    wait: yes
- name: Update new.foo.com as an A record with a list of 3 IPs and wait until the changes have been replicated
  community.aws.route53:
    state: present
    zone: foo.com
    record: new.foo.com
    type: A
    ttl: 7200
    value:
      - 1.1.1.1
      - 2.2.2.2
      - 3.3.3.3
    wait: yes
- name: Retrieve the details for new.foo.com
  community.aws.route53:
    state: get
    zone: foo.com
    record: new.foo.com
    type: A
  register: rec
- name: Delete new.foo.com A record using the results from the get command
  community.aws.route53:
    state: absent
    zone: foo.com
    record: "{{ rec.set.record }}"
    ttl: "{{ rec.set.ttl }}"
    type: "{{ rec.set.type }}"
    value: "{{ rec.set.value }}"
# Add an AAAA record.  Note that because there are colons in the value
# that the IPv6 address must be quoted. Also shows using the old form command=create.
- name: Add an AAAA record
  community.aws.route53:
    command: create
    zone: foo.com
    record: localhost.foo.com
    type: AAAA
    ttl: 7200
    value: "::1"
# For more information on SRV records see:
# https://en.wikipedia.org/wiki/SRV_record
- name: Add a SRV record with multiple fields for a service on port 22222
  community.aws.route53:
    state: present
    zone: foo.com
    record: "_example-service._tcp.foo.com"
    type: SRV
    value: "0 0 22222 host1.foo.com,0 0 22222 host2.foo.com"
# Note that TXT and SPF records must be surrounded
# by quotes when sent to Route 53:
- name: Add a TXT record.
  community.aws.route53:
    state: present
    zone: foo.com
    record: localhost.foo.com
    type: TXT
    ttl: 7200
    value: '"bar"'
- name: Add an alias record that points to an Amazon ELB
  community.aws.route53:
    state: present
    zone: foo.com
    record: elb.foo.com
    type: A
    value: "{{ elb_dns_name }}"
    alias: True
    alias_hosted_zone_id: "{{ elb_zone_id }}"
- name: Retrieve the details for elb.foo.com
  community.aws.route53:
    state: get
    zone: foo.com
    record: elb.foo.com
    type: A
  register: rec
- name: Delete an alias record using the results from the get command
  community.aws.route53:
    state: absent
    zone: foo.com
    record: "{{ rec.set.record }}"
    ttl: "{{ rec.set.ttl }}"
    type: "{{ rec.set.type }}"
    value: "{{ rec.set.value }}"
    alias: True
    alias_hosted_zone_id: "{{ rec.set.alias_hosted_zone_id }}"
- name: Add an alias record that points to an Amazon ELB and evaluates it health
  community.aws.route53:
    state: present
    zone: foo.com
    record: elb.foo.com
    type: A
    value: "{{ elb_dns_name }}"
    alias: True
    alias_hosted_zone_id: "{{ elb_zone_id }}"
    alias_evaluate_target_health: True
- name: Add an AAAA record with Hosted Zone ID
  community.aws.route53:
    state: present
    zone: foo.com
    hosted_zone_id: Z2AABBCCDDEEFF
    record: localhost.foo.com
    type: AAAA
    ttl: 7200
    value: "::1"
- name: Use a routing policy to distribute traffic
  community.aws.route53:
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
  community.aws.route53:
    state: present
    zone: example.com
    record: example.com
    type: CAA
    value:
      - 0 issue "ca.example.net"
      - 0 issuewild ";"
      - 0 iodef "mailto:security@example.com"
- name: Create a record with geo_location - country_code
  community.aws.route53:
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
  community.aws.route53:
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
| **nameservers**  list / elements=string | Nameservers associated with the zone.  Returned: when state is ‘get’  Sample: `["ns-1036.awsdns-00.org.", "ns-516.awsdns-00.net.", "ns-1504.awsdns-00.co.uk.", "ns-1.awsdns-00.com."]` |
| **set**  complex | Info specific to the resource record.  Returned: when state is ‘get’ |
| **alias**  boolean | Whether this is an alias.  Returned: always  Sample: `false` |
| **failover**  string | Whether this is the primary or secondary resource record set.  Returned: always  Sample: `"PRIMARY"` |
| **geo_location**  dictionary  added in community.aws 3.3.0 | geograpic location based on which Route53 resonds to DNS queries.  Returned: when configured  Sample: `{"continent_code": "NA", "country_code": "US", "subdivision_code": "CA"}` |
| **health_check**  string | health_check associated with this record.  Returned: always |
| **identifier**  string | An identifier that differentiates among multiple resource record sets that have the same combination of DNS name and type.  Returned: always |
| **record**  string | Domain name for the record set.  Returned: always  Sample: `"new.foo.com."` |
| **region**  string | Which region this should be associated with for latency-based routing.  Returned: always  Sample: `"us-west-2"` |
| **ttl**  string | Resource record cache TTL.  Returned: always  Sample: `"3600"` |
| **type**  string | Resource record set type.  Returned: always  Sample: `"A"` |
| **value**  string | Record value.  Returned: always  Sample: `"52.43.18.27"` |
| **values**  list / elements=string | Record Values.  Returned: always  Sample: `["52.43.18.27"]` |
| **weight**  string | Weight of the record.  Returned: always  Sample: `"3"` |
| **zone**  string | Zone this record set belongs to.  Returned: always  Sample: `"foo.bar.com."` |

### Authors

- Bruce Pennypacker (@bpennypacker)
- Mike Buzzetti (@jimbydamonk)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
