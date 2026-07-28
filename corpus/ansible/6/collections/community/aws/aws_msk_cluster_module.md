---
collection: ansible
version: "6"
title: "community.aws.aws_msk_cluster module – Manage Amazon MSK clusters."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_msk_cluster_module.html
fetched_at: 2026-07-27T17:03:29+00:00
---
# community.aws.aws_msk_cluster module – Manage Amazon MSK clusters.

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
> see [Requirements](aws_msk_cluster_module.md#ansible-collections-community-aws-aws-msk-cluster-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_msk_cluster`.

New in community.aws 2.0.0

- [Synopsis](aws_msk_cluster_module.md#synopsis)
- [Requirements](aws_msk_cluster_module.md#requirements)
- [Parameters](aws_msk_cluster_module.md#parameters)
- [Notes](aws_msk_cluster_module.md#notes)
- [Examples](aws_msk_cluster_module.md#examples)
- [Return Values](aws_msk_cluster_module.md#return-values)

## [Synopsis](aws_msk_cluster_module.md#id1)

- Create, delete and modify Amazon MSK (Managed Streaming for Apache Kafka) clusters.

## [Requirements](aws_msk_cluster_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_msk_cluster_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **authentication**  dictionary | Includes all client authentication related information.  Effective only for new cluster and can not be updated. |
| **sasl_scram**  boolean | SASL/SCRAM authentication is enabled or not.  Choices:   - `false` ← (default) - `true` |
| **tls_ca_arn**  list / elements=string | List of ACM Certificate Authority ARNs. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **configuration_arn**  string | ARN of the configuration to use.  This parameter is required when *state=present*. |
| **configuration_revision**  integer | The revision of the configuration to use.  This parameter is required when *state=present*. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ebs_volume_size**  integer | The size in GiB of the EBS volume for the data drive on each broker node.  Default: `100` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **encryption**  dictionary | Includes all encryption-related information.  Effective only for new cluster and can not be updated. |
| **in_transit**  dictionary | The details for encryption in transit. |
| **client_broker**  string | Indicates the encryption setting for data in transit between clients and brokers. The following are the possible values. TLS means that client-broker communication is enabled with TLS only. TLS_PLAINTEXT means that client-broker communication is enabled for both TLS-encrypted, as well as plaintext data. PLAINTEXT means that client-broker communication is enabled in plaintext only.  Choices:   - `"TLS"` ← (default) - `"TLS_PLAINTEXT"` - `"PLAINTEXT"` |
| **in_cluster**  boolean | When set to true, it indicates that data communication among the broker nodes of the cluster is encrypted. When set to false, the communication happens in plaintext.  Choices:   - `false` - `true` ← (default) |
| **kms_key_id**  string | The ARN of the AWS KMS key for encrypting data at rest. If you don’t specify a KMS key, MSK creates one for you and uses it. |
| **enhanced_monitoring**  string | Specifies the level of monitoring for the MSK cluster.  Choices:   - `"DEFAULT"` ← (default) - `"PER_BROKER"` - `"PER_TOPIC_PER_BROKER"` - `"PER_TOPIC_PER_PARTITION"` |
| **instance_type**  string | The type of Amazon EC2 instances to use for Kafka brokers.  Update operation requires botocore version >= 1.19.58.  Choices:   - `"kafka.t3.small"` ← (default) - `"kafka.m5.large"` - `"kafka.m5.xlarge"` - `"kafka.m5.2xlarge"` - `"kafka.m5.4xlarge"` |
| **logging**  dictionary | Logging configuration. |
| **cloudwatch**  dictionary | Details of the CloudWatch Logs destination for broker logs. |
| **enabled**  boolean | Specifies whether broker logs get sent to the specified CloudWatch Logs destination.  Choices:   - `false` ← (default) - `true` |
| **log_group**  string | The CloudWatch log group that is the destination for broker logs. |
| **firehose**  dictionary | Details of the Kinesis Data Firehose delivery stream that is the destination for broker logs. |
| **delivery_stream**  string | The Kinesis Data Firehose delivery stream that is the destination for broker logs. |
| **enabled**  boolean | Specifies whether broker logs get send to the specified Kinesis Data Firehose delivery stream.  Choices:   - `false` ← (default) - `true` |
| **s3**  dictionary | Details of the Amazon S3 destination for broker logs. |
| **bucket**  string | The name of the S3 bucket that is the destination for broker logs. |
| **enabled**  boolean | Specifies whether broker logs get sent to the specified Amazon S3 destination.  Choices:   - `false` ← (default) - `true` |
| **prefix**  string | The S3 prefix that is the destination for broker logs. |
| **name**  string / required | The name of the cluster. |
| **nodes**  integer | The number of broker nodes in the cluster. Should be greater or equal to two.  Default: `3` |
| **open_monitoring**  dictionary | The settings for open monitoring. |
| **jmx_exporter**  boolean | Indicates whether you want to enable or disable the JMX Exporter.  Choices:   - `false` ← (default) - `true` |
| **node_exporter**  boolean | Indicates whether you want to enable or disable the Node Exporter.  Choices:   - `false` ← (default) - `true` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean | Remove tags not listed in *tags* when tags is specified.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_groups**  list / elements=string | The AWS security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster. If you don’t specify a security group, Amazon MSK uses the default security group associated with the VPC. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Create (`present`) or delete (`absent`) cluster.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnets**  list / elements=string | The list of subnets to connect to in the client virtual private cloud (VPC). AWS creates elastic network interfaces inside these subnets. Client applications use elastic network interfaces to produce and consume data.  Client subnets can’t be in Availability Zone us-east-1e.  This parameter is required when *state=present*. |
| **tags**  dictionary | Tag dictionary to apply to the cluster. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **version**  string | The version of Apache Kafka.  This version should exist in given configuration.  This parameter is required when *state=present*.  Update operation requires botocore version >= 1.16.19. |
| **wait**  boolean | Whether to wait for the cluster to be available or deleted.  Choices:   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How many seconds to wait. Cluster creation can take up to 20-30 minutes.  Default: `3600` |

## [Notes](aws_msk_cluster_module.md#id4)

> **Note:**
>
> - All operations are time consuming, for example create takes 20-30 minutes, update kafka version – more than one hour, update configuration – 10-15 minutes;
> - Cluster’s brokers get evenly distributed over a number of availability zones that’s equal to the number of subnets.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_msk_cluster_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- aws_msk_cluster:
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
    configuration_arn: arn:aws:kafka:us-east-1:000000000001:configuration/kafka-cluster-configuration/aaaaaaaa-bbbb-4444-3333-ccccccccc-1
    configuration_revision: 1

- aws_msk_cluster:
    name: kafka-cluster
    state: absent
```

## [Return Values](aws_msk_cluster_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **bootstrap_broker_string**  complex | A list of brokers that a client application can use to bootstrap.  Returned: *state=present* and cluster state is *ACTIVE* |
| **plain**  string | A string containing one or more hostname:port pairs.  Returned: success |
| **tls**  string | A string containing one or more DNS names (or IP) and TLS port pairs.  Returned: success |
| **cluster_info**  dictionary | Description of the MSK cluster.  Returned: *state=present* |
| **response**  dictionary | The response from actual API call.  Returned: always  Sample: `{}` |

### Authors

- Daniil Kupchenko (@oukooveu)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
