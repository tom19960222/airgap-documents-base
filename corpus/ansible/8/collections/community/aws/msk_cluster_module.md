---
collection: ansible
version: "8"
title: "community.aws.msk_cluster module – Manage Amazon MSK clusters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/msk_cluster_module.html
fetched_at: 2026-07-28T01:41:35+00:00
---
# community.aws.msk_cluster module – Manage Amazon MSK clusters

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
> see [Requirements](msk_cluster_module.md#ansible-collections-community-aws-msk-cluster-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.msk_cluster`.

New in community.aws 2.0.0

- [Synopsis](msk_cluster_module.md#synopsis)
- [Requirements](msk_cluster_module.md#requirements)
- [Parameters](msk_cluster_module.md#parameters)
- [Notes](msk_cluster_module.md#notes)
- [Examples](msk_cluster_module.md#examples)
- [Return Values](msk_cluster_module.md#return-values)

## [Synopsis](msk_cluster_module.md#id1)

- Create, delete and modify Amazon MSK (Managed Streaming for Apache Kafka) clusters.
- Prior to release 5.0.0 this module was called `community.aws.aws_msk_cluster`. The usage did not change.

Aliases: aws_msk_cluster

## [Requirements](msk_cluster_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](msk_cluster_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **authentication**  dictionary | Includes all client authentication related information.  Effective only for new cluster and can not be updated. |
| **sasl_iam**  boolean  *added in community.aws 5.5.0* | IAM authentication is enabled or not.  **Choices:**   - `false` - `true` |
| **sasl_scram**  boolean | SASL/SCRAM authentication is enabled or not.  **Choices:**   - `false` - `true` |
| **tls_ca_arn**  list / elements=string | List of ACM Certificate Authority ARNs. |
| **unauthenticated**  boolean  *added in community.aws 5.5.0* | Option to explicitly turn on or off authentication  **Choices:**   - `false` - `true` ← (default) |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **configuration_arn**  string | ARN of the configuration to use.  This parameter is required when *state=present*. |
| **configuration_revision**  integer | The revision of the configuration to use.  This parameter is required when *state=present*. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **ebs_volume_size**  integer | The size in GiB of the EBS volume for the data drive on each broker node.  **Default:** `100` |
| **encryption**  dictionary | Includes all encryption-related information.  Effective only for new cluster and can not be updated. |
| **in_transit**  dictionary | The details for encryption in transit. |
| **client_broker**  string | Indicates the encryption setting for data in transit between clients and brokers. The following are the possible values. TLS means that client-broker communication is enabled with TLS only. TLS_PLAINTEXT means that client-broker communication is enabled for both TLS-encrypted, as well as plaintext data. PLAINTEXT means that client-broker communication is enabled in plaintext only.  **Choices:**   - `"TLS"` ← (default) - `"TLS_PLAINTEXT"` - `"PLAINTEXT"` |
| **in_cluster**  boolean | When set to true, it indicates that data communication among the broker nodes of the cluster is encrypted. When set to false, the communication happens in plaintext.  **Choices:**   - `false` - `true` ← (default) |
| **kms_key_id**  string | The ARN of the AWS KMS key for encrypting data at rest. If you don’t specify a KMS key, MSK creates one for you and uses it. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **enhanced_monitoring**  string | Specifies the level of monitoring for the MSK cluster.  **Choices:**   - `"DEFAULT"` ← (default) - `"PER_BROKER"` - `"PER_TOPIC_PER_BROKER"` - `"PER_TOPIC_PER_PARTITION"` |
| **instance_type**  string | The type of Amazon EC2 instances to use for Kafka brokers.  **Choices:**   - `"kafka.t3.small"` ← (default) - `"kafka.m5.large"` - `"kafka.m5.xlarge"` - `"kafka.m5.2xlarge"` - `"kafka.m5.4xlarge"` |
| **logging**  dictionary | Logging configuration. |
| **cloudwatch**  dictionary | Details of the CloudWatch Logs destination for broker logs. |
| **enabled**  boolean | Specifies whether broker logs get sent to the specified CloudWatch Logs destination.  **Choices:**   - `false` ← (default) - `true` |
| **log_group**  string | The CloudWatch log group that is the destination for broker logs. |
| **firehose**  dictionary | Details of the Kinesis Data Firehose delivery stream that is the destination for broker logs. |
| **delivery_stream**  string | The Kinesis Data Firehose delivery stream that is the destination for broker logs. |
| **enabled**  boolean | Specifies whether broker logs get send to the specified Kinesis Data Firehose delivery stream.  **Choices:**   - `false` ← (default) - `true` |
| **s3**  dictionary | Details of the Amazon S3 destination for broker logs. |
| **bucket**  string | The name of the S3 bucket that is the destination for broker logs. |
| **enabled**  boolean | Specifies whether broker logs get sent to the specified Amazon S3 destination.  **Choices:**   - `false` ← (default) - `true` |
| **prefix**  string | The S3 prefix that is the destination for broker logs. |
| **name**  string / required | The name of the cluster. |
| **nodes**  integer | The number of broker nodes in the cluster. Should be greater or equal to two.  **Default:** `3` |
| **open_monitoring**  dictionary | The settings for open monitoring. |
| **jmx_exporter**  boolean | Indicates whether you want to enable or disable the JMX Exporter.  **Choices:**   - `false` ← (default) - `true` |
| **node_exporter**  boolean | Indicates whether you want to enable or disable the Node Exporter.  **Choices:**   - `false` ← (default) - `true` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **security_groups**  list / elements=string | The AWS security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster. If you don’t specify a security group, Amazon MSK uses the default security group associated with the VPC. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create (`present`) or delete (`absent`) cluster.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnets**  list / elements=string | The list of subnets to connect to in the client virtual private cloud (VPC). AWS creates elastic network interfaces inside these subnets. Client applications use elastic network interfaces to produce and consume data.  Client subnets can’t be in Availability Zone us-east-1e.  This parameter is required when *state=present*. |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **version**  string | The version of Apache Kafka.  This version should exist in given configuration.  This parameter is required when *state=present*. |
| **wait**  boolean | Whether to wait for the cluster to be available or deleted.  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How many seconds to wait. Cluster creation can take up to 20-30 minutes.  **Default:** `3600` |

## [Notes](msk_cluster_module.md#id4)

> **Note:**
>
> - All operations are time consuming, for example create takes 20-30 minutes, update kafka version – more than one hour, update configuration – 10-15 minutes;
> - Cluster’s brokers get evenly distributed over a number of availability zones that’s equal to the number of subnets.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](msk_cluster_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- community.aws.msk_cluster:
    name: kafka-cluster
    state: present
    version: 2.6.1
    nodes: 6
    ebs_volume_size: "{{ aws_msk_options.ebs_volume_size }}"
    subnets:
      - subnet-e3b48ce7c25861eeb
      - subnet-2990c8b25b07ddd43
      - subnet-d9fbeaf46c54bfab6
    wait: true
    wait_timeout: 1800
    configuration_arn: arn:aws:kafka:us-east-1:123456789012:configuration/kafka-cluster-configuration/aaaaaaaa-bbbb-4444-3333-ccccccccc-1
    configuration_revision: 1

- community.aws.msk_cluster:
    name: kafka-cluster
    state: absent
```

## [Return Values](msk_cluster_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **bootstrap_broker_string**  complex | A list of brokers that a client application can use to bootstrap.  **Returned:** *state=present* and cluster state is *ACTIVE* |
| **plain**  string | A string containing one or more hostname:port pairs.  **Returned:** success |
| **tls**  string | A string containing one or more DNS names (or IP) and TLS port pairs.  **Returned:** success |
| **cluster_info**  dictionary | Description of the MSK cluster.  **Returned:** *state=present* |
| **response**  dictionary | The response from actual API call.  **Returned:** always  **Sample:** `{}` |

### Authors

- Daniil Kupchenko (@oukooveu)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
