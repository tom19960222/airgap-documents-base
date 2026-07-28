---
collection: ansible
version: "8"
title: "community.aws.elasticache module – Manage cache clusters in Amazon ElastiCache"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/elasticache_module.html
fetched_at: 2026-07-28T01:41:07+00:00
---
# community.aws.elasticache module – Manage cache clusters in Amazon ElastiCache

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
> see [Requirements](elasticache_module.md#ansible-collections-community-aws-elasticache-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.elasticache`.

New in community.aws 1.0.0

- [Synopsis](elasticache_module.md#synopsis)
- [Requirements](elasticache_module.md#requirements)
- [Parameters](elasticache_module.md#parameters)
- [Notes](elasticache_module.md#notes)
- [Examples](elasticache_module.md#examples)

## [Synopsis](elasticache_module.md#id1)

- Manage cache clusters in Amazon ElastiCache.
- Returns information about the specified cache cluster.

## [Requirements](elasticache_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](elasticache_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **cache_engine_version**  string | The version number of the cache engine.  **Default:** `""` |
| **cache_parameter_group**  aliases: parameter_group  string | The name of the cache parameter group to associate with this cache cluster. If this argument is omitted, the default cache parameter group for the specified engine will be used.  **Default:** `""` |
| **cache_port**  integer | The port number on which each of the cache nodes will accept connections. |
| **cache_security_groups**  list / elements=string | A list of cache security group names to associate with this cache cluster.  Don’t use if your Cache is inside a VPC. In that case use *security_group_ids* instead!  **Default:** `[]` |
| **cache_subnet_group**  string | The subnet group name to associate with. Only use if inside a VPC.  Required if inside a VPC.  **Default:** `""` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **engine**  string | Name of the cache engine to be used.  Supported values are `redis` and `memcached`.  **Default:** `"memcached"` |
| **hard_modify**  boolean | Whether to destroy and recreate an existing cache cluster if necessary in order to modify its state.  Defaults to `false`.  **Choices:**   - `false` - `true` |
| **name**  string / required | The cache cluster identifier. |
| **node_type**  string | The compute and memory capacity of the nodes in the cache cluster.  **Default:** `"cache.t2.small"` |
| **num_nodes**  integer | The initial number of cache nodes that the cache cluster will have.  Required when *state=present*.  **Default:** `1` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **security_group_ids**  list / elements=string | A list of VPC security group IDs to associate with this cache cluster. Only use if inside a VPC.  **Default:** `[]` |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string / required | `absent` or `present` are idempotent actions that will create or destroy a cache cluster as needed.  `rebooted` will reboot the cluster, resulting in a momentary outage.  **Choices:**   - `"present"` - `"absent"` - `"rebooted"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Wait for cache cluster result before returning.  **Choices:**   - `false` - `true` ← (default) |
| **zone**  string | The EC2 Availability Zone in which the cache cluster will be created. |

## [Notes](elasticache_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](elasticache_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Basic example
  community.aws.elasticache:
    name: "test-please-delete"
    state: present
    engine: memcached
    cache_engine_version: 1.4.14
    node_type: cache.m3.small
    num_nodes: 1
    cache_port: 11211
    cache_security_groups:
      - default
    zone: us-east-1d

- name: Ensure cache cluster is gone
  community.aws.elasticache:
    name: "test-please-delete"
    state: absent

- name: Reboot cache cluster
  community.aws.elasticache:
    name: "test-please-delete"
    state: rebooted
```

### Authors

- Jim Dalton (@jsdalton)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
