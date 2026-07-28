---
collection: ansible
version: "8"
title: "community.aws.elasticache_info module – Retrieve information for AWS ElastiCache clusters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/elasticache_info_module.html
fetched_at: 2026-07-28T01:41:07+00:00
---
# community.aws.elasticache_info module – Retrieve information for AWS ElastiCache clusters

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

- Retrieve information from AWS ElastiCache clusters.

## [Requirements](elasticache_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](elasticache_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **name**  string | The name of an ElastiCache cluster. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](elasticache_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

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
| **elasticache_clusters**  list / elements=dictionary | List of ElastiCache clusters.  **Returned:** always |
| **arn**  string | ARN of the cache cluster.  **Returned:** always  **Sample:** `"arn:aws:elasticache:us-east-1:123456789012:cluster:ansible-test"` |
| **auto_minor_version_upgrade**  boolean | Whether to automatically upgrade to minor versions.  **Returned:** always  **Sample:** `true` |
| **cache_cluster_create_time**  string | Date and time cluster was created.  **Returned:** always  **Sample:** `"2017-09-15T05:43:46.038000+00:00"` |
| **cache_cluster_id**  string | ID of the cache cluster.  **Returned:** always  **Sample:** `"abcd-1234-001"` |
| **cache_cluster_status**  string | Status of ElastiCache cluster.  **Returned:** always  **Sample:** `"available"` |
| **cache_node_type**  string | Instance type of ElastiCache nodes.  **Returned:** always  **Sample:** `"cache.t2.micro"` |
| **cache_nodes**  list / elements=dictionary | List of ElastiCache nodes in the cluster.  **Returned:** always |
| **cache_node_create_time**  string | Date and time node was created.  **Returned:** always  **Sample:** `"2017-09-15T05:43:46.038000+00:00"` |
| **cache_node_id**  string | ID of the cache node.  **Returned:** always  **Sample:** `"0001"` |
| **cache_node_status**  string | Status of the cache node.  **Returned:** always  **Sample:** `"available"` |
| **customer_availability_zone**  string | Availability Zone in which the cache node was created.  **Returned:** always  **Sample:** `"ap-southeast-2b"` |
| **endpoint**  dictionary | Connection details for the cache node.  **Returned:** always |
| **address**  string | URL of the cache node endpoint.  **Returned:** always  **Sample:** `"abcd-1234-001.bgiz2p.0001.apse2.cache.amazonaws.com"` |
| **port**  integer | Port of the cache node endpoint.  **Returned:** always  **Sample:** `6379` |
| **parameter_group_status**  string | Status of the Cache Parameter Group.  **Returned:** always  **Sample:** `"in-sync"` |
| **cache_parameter_group**  dictionary | Contents of the Cache Parameter Group.  **Returned:** always |
| **cache_node_ids_to_reboot**  list / elements=string | Cache nodes which need to be rebooted for parameter changes to be applied.  **Returned:** always  **Sample:** `[]` |
| **cache_parameter_group_name**  string | Name of the cache parameter group.  **Returned:** always  **Sample:** `"default.redis3.2"` |
| **parameter_apply_status**  string | Status of parameter updates.  **Returned:** always  **Sample:** `"in-sync"` |
| **cache_security_groups**  list / elements=string | Security Groups used by the cache.  **Returned:** always  **Sample:** `["sg-abcd1234"]` |
| **cache_subnet_group_name**  string | ElastiCache Subnet Group used by the cache.  **Returned:** always  **Sample:** `"abcd-subnet-group"` |
| **client_download_landing_page**  string | URL of client download web page.  **Returned:** always  **Sample:** `"https://console.aws.amazon.com/elasticache/home#client-download:"` |
| **engine**  string | Engine used by ElastiCache.  **Returned:** always  **Sample:** `"redis"` |
| **engine_version**  string | Version of ElastiCache engine.  **Returned:** always  **Sample:** `"3.2.4"` |
| **notification_configuration**  dictionary | Configuration of notifications.  **Returned:** if notifications are enabled |
| **topic_arn**  string | ARN of notification destination topic.  **Returned:** if notifications are enabled  **Sample:** `"arn:aws:sns:*:123456789012:my_topic"` |
| **topic_name**  string | Name of notification destination topic.  **Returned:** if notifications are enabled  **Sample:** `"MyTopic"` |
| **num_cache_nodes**  integer | Number of Cache Nodes.  **Returned:** always  **Sample:** `1` |
| **pending_modified_values**  dictionary | Values that are pending modification.  **Returned:** always |
| **preferred_availability_zone**  string | Preferred Availability Zone.  **Returned:** always  **Sample:** `"ap-southeast-2b"` |
| **preferred_maintenance_window**  string | Time slot for preferred maintenance window.  **Returned:** always  **Sample:** `"sat:12:00-sat:13:00"` |
| **replication_group**  dictionary  *added in community.aws 4.1.0* | Informations about the associated replication group.  **Returned:** if replication is enabled |
| **arn**  string | The ARN (Amazon Resource Name) of the replication group.  **Returned:** always |
| **at_rest_encryption_enabled**  boolean | A flag that enables encryption at-rest when set to true.  **Returned:** always |
| **auth_token_enabled**  boolean | A flag that enables using an AuthToken (password) when issuing Redis commands.  **Returned:** always |
| **automatic_failover**  string | Indicates the status of automatic failover for this Redis replication group.  **Returned:** always  **Sample:** `"enabled"` |
| **cache_node_type**  string | The name of the compute and memory capacity node type for each node in the replication group.  **Returned:** always  **Sample:** `"cache.t3.medium"` |
| **cluster_enabled**  boolean | A flag indicating whether or not this replication group is cluster enabled.  **Returned:** always |
| **description**  string | The user supplied description of the replication group.  **Returned:** always |
| **global_replication_group_info**  dictionary | The name of the Global datastore and role of this replication group in the Global datastore.  **Returned:** always |
| **global_replication_group_id**  string | The name of the Global datastore.  **Returned:** always |
| **global_replication_group_member_role**  string | The role of the replication group in a Global datastore. Can be primary or secondary.  **Returned:** always |
| **kms_key_id**  string | The ID of the KMS key used to encrypt the disk in the cluster.  **Returned:** always |
| **member_clusters**  list / elements=string | The names of all the cache clusters that are part of this replication group.  **Returned:** always |
| **multi_az**  string | A flag indicating if you have Multi-AZ enabled to enhance fault tolerance.  **Returned:** always  **Sample:** `"enabled"` |
| **node_groups**  list / elements=dictionary | A list of node groups in this replication group.  **Returned:** always |
| **node_group_id**  string | The identifier for the node group (shard).  **Returned:** always |
| **node_group_members**  list / elements=dictionary | A list containing information about individual nodes within the node group (shard).  **Returned:** always |
| **cache_cluster_id**  string | The ID of the cluster to which the node belongs.  **Returned:** always |
| **cache_node_id**  string | The ID of the node within its cluster.  **Returned:** always |
| **current_role**  string | The role that is currently assigned to the node - primary or replica.  **Returned:** always  **Sample:** `"primary"` |
| **preferred_availability_zone**  string | The name of the Availability Zone in which the node is located.  **Returned:** always |
| **read_endpoint**  list / elements=dictionary | The information required for client programs to connect to a node for read operations.  **Returned:** always |
| **address**  string | The DNS hostname of the cache node.  **Returned:** always |
| **port**  integer | The port number that the cache engine is listening on.  **Returned:** always  **Sample:** `6379` |
| **primary_endpoint**  list / elements=dictionary | The endpoint of the primary node in this node group (shard).  **Returned:** always |
| **address**  string | The DNS hostname of the cache node.  **Returned:** always |
| **port**  integer | The port number that the cache engine is listening on.  **Returned:** always  **Sample:** `6379` |
| **reader_endpoint**  dictionary | The endpoint of the cache node.  **Returned:** always |
| **address**  string | The DNS hostname of the cache node.  **Returned:** always |
| **port**  integer | The port number that the cache engine is listening on.  **Returned:** always  **Sample:** `6379` |
| **status**  string | The current state of this replication group - `creating`, `available`, `modifying`, `deleting`.  **Returned:** always  **Sample:** `"available"` |
| **pending_modified_values**  dictionary | A group of settings to be applied to the replication group, either immediately or during the next maintenance window.  **Returned:** always |
| **replication_group_id**  string | Replication Group Id.  **Returned:** always  **Sample:** `"replication-001"` |
| **snapshot_retention_limit**  integer | The number of days for which ElastiCache retains automatic cluster snapshots before deleting them.  **Returned:** always |
| **snapshot_window**  string | The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).  **Returned:** always  **Sample:** `"07:00-09:00"` |
| **snapshotting_cluster_id**  string | The cluster ID that is used as the daily snapshot source for the replication group.  **Returned:** always |
| **status**  string | The current state of this replication group - `creating`, `available`, `modifying`, `deleting`, `create-failed`, `snapshotting`  **Returned:** always |
| **transit_encryption_enabled**  boolean | A flag that enables in-transit encryption when set to `true`.  **Returned:** always |
| **replication_group_id**  string | Replication Group Id.  **Returned:** if replication is enabled  **Sample:** `"replication-001"` |
| **security_groups**  list / elements=dictionary | List of Security Groups associated with ElastiCache.  **Returned:** always |
| **security_group_id**  string | Security Group ID  **Returned:** always  **Sample:** `"sg-abcd1234"` |
| **status**  string | Status of Security Group  **Returned:** always  **Sample:** `"active"` |
| **tags**  dictionary | Tags applied to the ElastiCache cluster  **Returned:** always  **Sample:** `{"Application": "web", "Environment": "test"}` |

### Authors

- Will Thames (@willthames)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
