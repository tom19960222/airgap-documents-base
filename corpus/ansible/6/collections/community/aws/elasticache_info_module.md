---
collection: ansible
version: "6"
title: "community.aws.elasticache_info module – Retrieve information for AWS ElastiCache clusters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/elasticache_info_module.html
fetched_at: 2026-07-27T17:04:25+00:00
---
# community.aws.elasticache_info module – Retrieve information for AWS ElastiCache clusters

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
> see [Requirements](elasticache_info_module.md#ansible-collections-community-aws-elasticache-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.elasticache_info`.

New in community.aws 1.0.0

- [Synopsis](elasticache_info_module.md#synopsis)
- [Requirements](elasticache_info_module.md#requirements)
- [Parameters](elasticache_info_module.md#parameters)
- [Notes](elasticache_info_module.md#notes)
- [Examples](elasticache_info_module.md#examples)
- [Return Values](elasticache_info_module.md#return-values)

## [Synopsis](elasticache_info_module.md#id1)

- Retrieve information from AWS ElastiCache clusters

## [Requirements](elasticache_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](elasticache_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **name**  string | The name of an ElastiCache cluster. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](elasticache_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](elasticache_info_module.md#id5)

```yaml+jinja
- name: obtain all ElastiCache information
  community.aws.elasticache_info:

- name: obtain all information for a single ElastiCache cluster
  community.aws.elasticache_info:
    name: test_elasticache
```

## [Return Values](elasticache_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **elasticache_clusters**  complex | List of ElastiCache clusters  Returned: always |
| **auto_minor_version_upgrade**  boolean | Whether to automatically upgrade to minor versions  Returned: always  Sample: `true` |
| **cache_cluster_create_time**  string | Date and time cluster was created  Returned: always  Sample: `"2017-09-15T05:43:46.038000+00:00"` |
| **cache_cluster_id**  string | ID of the cache cluster  Returned: always  Sample: `"abcd-1234-001"` |
| **cache_cluster_status**  string | Status of ElastiCache cluster  Returned: always  Sample: `"available"` |
| **cache_node_type**  string | Instance type of ElastiCache nodes  Returned: always  Sample: `"cache.t2.micro"` |
| **cache_nodes**  complex | List of ElastiCache nodes in the cluster  Returned: always |
| **cache_node_create_time**  string | Date and time node was created  Returned: always  Sample: `"2017-09-15T05:43:46.038000+00:00"` |
| **cache_node_id**  string | ID of the cache node  Returned: always  Sample: `"0001"` |
| **cache_node_status**  string | Status of the cache node  Returned: always  Sample: `"available"` |
| **customer_availability_zone**  string | Availability Zone in which the cache node was created  Returned: always  Sample: `"ap-southeast-2b"` |
| **endpoint**  complex | Connection details for the cache node  Returned: always |
| **address**  string | URL of the cache node endpoint  Returned: always  Sample: `"abcd-1234-001.bgiz2p.0001.apse2.cache.amazonaws.com"` |
| **port**  integer | Port of the cache node endpoint  Returned: always  Sample: `6379` |
| **parameter_group_status**  string | Status of the Cache Parameter Group  Returned: always  Sample: `"in-sync"` |
| **cache_parameter_group**  complex | Contents of the Cache Parameter Group  Returned: always |
| **cache_node_ids_to_reboot**  list / elements=string | Cache nodes which need to be rebooted for parameter changes to be applied  Returned: always  Sample: `[]` |
| **cache_parameter_group_name**  string | Name of the cache parameter group  Returned: always  Sample: `"default.redis3.2"` |
| **parameter_apply_status**  string | Status of parameter updates  Returned: always  Sample: `"in-sync"` |
| **cache_security_groups**  list / elements=string | Security Groups used by the cache  Returned: always  Sample: `["sg-abcd1234"]` |
| **cache_subnet_group_name**  string | ElastiCache Subnet Group used by the cache  Returned: always  Sample: `"abcd-subnet-group"` |
| **client_download_landing_page**  string | URL of client download web page  Returned: always  Sample: `"https://console.aws.amazon.com/elasticache/home#client-download:"` |
| **engine**  string | Engine used by ElastiCache  Returned: always  Sample: `"redis"` |
| **engine_version**  string | Version of ElastiCache engine  Returned: always  Sample: `"3.2.4"` |
| **notification_configuration**  complex | Configuration of notifications  Returned: if notifications are enabled |
| **topic_arn**  string | ARN of notification destination topic  Returned: if notifications are enabled  Sample: `"arn:aws:sns:*:123456789012:my_topic"` |
| **topic_name**  string | Name of notification destination topic  Returned: if notifications are enabled  Sample: `"MyTopic"` |
| **num_cache_nodes**  integer | Number of Cache Nodes  Returned: always  Sample: `1` |
| **pending_modified_values**  complex | Values that are pending modification  Returned: always |
| **preferred_availability_zone**  string | Preferred Availability Zone  Returned: always  Sample: `"ap-southeast-2b"` |
| **preferred_maintenance_window**  string | Time slot for preferred maintenance window  Returned: always  Sample: `"sat:12:00-sat:13:00"` |
| **replication_group_id**  string | Replication Group Id  Returned: always  Sample: `"replication-001"` |
| **security_groups**  complex | List of Security Groups associated with ElastiCache  Returned: always |
| **security_group_id**  string | Security Group ID  Returned: always  Sample: `"sg-abcd1234"` |
| **status**  string | Status of Security Group  Returned: always  Sample: `"active"` |
| **tags**  complex | Tags applied to the ElastiCache cluster  Returned: always  Sample: `{"Application": "web", "Environment": "test"}` |

### Authors

- Will Thames (@willthames)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
