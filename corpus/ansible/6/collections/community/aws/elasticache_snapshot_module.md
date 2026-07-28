---
collection: ansible
version: "6"
title: "community.aws.elasticache_snapshot module – Manage cache snapshots in Amazon ElastiCache"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/elasticache_snapshot_module.html
fetched_at: 2026-07-27T17:04:26+00:00
---
# community.aws.elasticache_snapshot module – Manage cache snapshots in Amazon ElastiCache

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
> see [Requirements](elasticache_snapshot_module.md#ansible-collections-community-aws-elasticache-snapshot-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.elasticache_snapshot`.

New in community.aws 1.0.0

- [Synopsis](elasticache_snapshot_module.md#synopsis)
- [Requirements](elasticache_snapshot_module.md#requirements)
- [Parameters](elasticache_snapshot_module.md#parameters)
- [Notes](elasticache_snapshot_module.md#notes)
- [Examples](elasticache_snapshot_module.md#examples)
- [Return Values](elasticache_snapshot_module.md#return-values)

## [Synopsis](elasticache_snapshot_module.md#id1)

- Manage cache snapshots in Amazon ElastiCache.
- Returns information about the specified snapshot.

## [Requirements](elasticache_snapshot_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](elasticache_snapshot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **bucket**  string | The s3 bucket to which the snapshot is exported. |
| **cluster_id**  string | The name of an existing cache cluster in the replication group to make the snapshot. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **name**  string / required | The name of the snapshot we want to create, copy, delete. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **replication_id**  string | The name of the existing replication group to make the snapshot. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string / required | Actions that will create, destroy, or copy a snapshot.  Choices:   - `"present"` - `"absent"` - `"copy"` |
| **target**  string | The name of a snapshot copy. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](elasticache_snapshot_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](elasticache_snapshot_module.md#id5)

```yaml+jinja
# Note: None of these examples set aws_access_key, aws_secret_key, or region.
# It is assumed that their matching environment variables are set.

- name: 'Create a snapshot'
  community.aws.elasticache_snapshot:
    name: 'test-snapshot'
    state: 'present'
    cluster_id: '{{ cluster }}'
    replication_id: '{{ replication }}'
```

## [Return Values](elasticache_snapshot_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | if a snapshot has been created, deleted, or copied  Returned: always  Sample: `{"changed": true}` |
| **response_metadata**  dictionary | response metadata about the snapshot  Returned: always  Sample: `{"http_headers": {"content-length": 1490, "content-type": "text/xml", "date": "Tue, 07 Feb 2017 16:43:04 GMT", "x-amzn-requestid": "7f436dea-ed54-11e6-a04c-ab2372a1f14d"}, "http_status_code": 200, "request_id": "7f436dea-ed54-11e6-a04c-ab2372a1f14d", "retry_attempts": 0}` |
| **snapshot**  dictionary | snapshot data  Returned: always  Sample: `{"auto_minor_version_upgrade": true, "cache_cluster_create_time": "2017-02-01T17:43:58.261000+00:00", "cache_cluster_id": "test-please-delete", "cache_node_type": "cache.m1.small", "cache_parameter_group_name": "default.redis3.2", "cache_subnet_group_name": "default", "engine": "redis", "engine_version": "3.2.4", "node_snapshots": {"cache_node_create_time": "2017-02-01T17:43:58.261000+00:00", "cache_node_id": 1, "cache_size": null}, "num_cache_nodes": 1, "port": 11211, "preferred_availability_zone": "us-east-1d", "preferred_maintenance_window": "wed:03:00-wed:04:00", "snapshot_name": "deletesnapshot", "snapshot_retention_limit": 0, "snapshot_source": "manual", "snapshot_status": "creating", "snapshot_window": "10:00-11:00", "vpc_id": "vpc-c248fda4"}` |

### Authors

- Sloane Hertel (@s-hertel)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
