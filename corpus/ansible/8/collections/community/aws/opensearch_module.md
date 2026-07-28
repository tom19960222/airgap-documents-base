---
collection: ansible
version: "8"
title: "community.aws.opensearch module – Creates OpenSearch or ElasticSearch domain"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/opensearch_module.html
fetched_at: 2026-07-28T01:41:41+00:00
---
# community.aws.opensearch module – Creates OpenSearch or ElasticSearch domain

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
> see [Requirements](opensearch_module.md#ansible-collections-community-aws-opensearch-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.opensearch`.

New in community.aws 4.0.0

- [Synopsis](opensearch_module.md#synopsis)
- [Requirements](opensearch_module.md#requirements)
- [Parameters](opensearch_module.md#parameters)
- [Notes](opensearch_module.md#notes)
- [Examples](opensearch_module.md#examples)

## [Synopsis](opensearch_module.md#id1)

- Creates or modify a Amazon OpenSearch Service domain.

## [Requirements](opensearch_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](opensearch_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **access_policies**  dictionary | IAM access policy as a JSON-formatted string. |
| **advanced_security_options**  dictionary | Specifies advanced security options. |
| **enabled**  boolean | True if advanced security is enabled.  You must enable node-to-node encryption to use advanced security options.  **Choices:**   - `false` - `true` |
| **internal_user_database_enabled**  boolean | True if the internal user database is enabled.  **Choices:**   - `false` - `true` |
| **master_user_options**  dictionary | Credentials for the master user, username and password, ARN, or both. |
| **master_user_arn**  string | ARN for the master user (if IAM is enabled). |
| **master_user_name**  string | The username of the master user, which is stored in the Amazon OpenSearch Service domain internal database. |
| **master_user_password**  string | The password of the master user, which is stored in the Amazon OpenSearch Service domain internal database. |
| **saml_options**  dictionary | The SAML application configuration for the domain. |
| **enabled**  boolean | True if SAML is enabled.  To use SAML authentication, you must enable fine-grained access control.  You can only enable SAML authentication for OpenSearch Dashboards on existing domains, not during the creation of new ones.  Domains only support one Dashboards authentication method at a time. If you have Amazon Cognito authentication for OpenSearch Dashboards enabled, you must disable it before you can enable SAML.  **Choices:**   - `false` - `true` |
| **idp**  dictionary | The SAML Identity Provider’s information. |
| **entity_id**  string | The unique entity ID of the application in SAML identity provider. |
| **metadata_content**  string | The metadata of the SAML application in XML format. |
| **master_backend_role**  string | The backend role that the SAML master user is mapped to. |
| **master_user_name**  string | The SAML master username, which is stored in the Amazon OpenSearch Service domain internal database. |
| **roles_key**  string | Element of the SAML assertion to use for backend roles. Default is roles. |
| **session_timeout_minutes**  integer | The duration, in minutes, after which a user session becomes inactive. Acceptable values are between 1 and 1440, and the default value is 60. |
| **subject_key**  string | Element of the SAML assertion to use for username. Default is NameID. |
| **allow_intermediate_upgrades**  boolean | If true, allow OpenSearch domain to be upgraded through one or more intermediate versions.  If false, do not allow OpenSearch domain to be upgraded through intermediate versions. The upgrade operation fails if it’s not possible to ugrade to *engine_version* directly.  **Choices:**   - `false` - `true` ← (default) |
| **auto_tune_options**  dictionary | Specifies Auto-Tune options. |
| **desired_state**  string | The Auto-Tune desired state. Valid values are ENABLED and DISABLED.  **Choices:**   - `"ENABLED"` - `"DISABLED"` |
| **maintenance_schedules**  list / elements=dictionary | A list of maintenance schedules. |
| **cron_expression_for_recurrence**  string | A cron expression for a recurring maintenance schedule. |
| **duration**  dictionary | Specifies maintenance schedule duration, duration value and duration unit. |
| **unit**  string | The unit of a maintenance schedule duration. Valid value is HOURS.  **Choices:**   - `"HOURS"` |
| **value**  integer | Integer to specify the value of a maintenance schedule duration. |
| **start_at**  string | The timestamp at which the Auto-Tune maintenance schedule starts. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **cluster_config**  dictionary | Parameters for the cluster configuration of an OpenSearch Service domain. |
| **availability_zone_count**  integer | An integer value to indicate the number of availability zones for a domain when zone awareness is enabled. This should be equal to number of subnets if VPC endpoints is enabled. |
| **cold_storage_options**  dictionary | Specifies the ColdStorageOptions config for a Domain. |
| **enabled**  boolean | True to enable cold storage. Supported on Elasticsearch 7.9 or above.  **Choices:**   - `false` - `true` |
| **dedicated_master**  boolean | A boolean value to indicate whether a dedicated master node is enabled.  **Choices:**   - `false` - `true` |
| **dedicated_master_instance_count**  integer | Total number of dedicated master nodes, active and on standby, for the domain. |
| **dedicated_master_instance_type**  string | The instance type for a dedicated master node. |
| **instance_count**  integer | Number of instances for the domain. |
| **instance_type**  string | Type of the instances to use for the domain. |
| **warm_count**  integer | The number of UltraWarm nodes in the domain. |
| **warm_enabled**  boolean | True to enable UltraWarm storage.  **Choices:**   - `false` - `true` |
| **warm_type**  string | The instance type for the OpenSearch domain’s warm nodes. |
| **zone_awareness**  boolean | A boolean value to indicate whether zone awareness is enabled.  **Choices:**   - `false` - `true` |
| **cognito_options**  dictionary | Parameters to configure OpenSearch Service to use Amazon Cognito authentication for OpenSearch Dashboards. |
| **enabled**  boolean | The option to enable Cognito for OpenSearch Dashboards authentication.  **Choices:**   - `false` - `true` |
| **identity_pool_id**  string | The Cognito identity pool ID for OpenSearch Dashboards authentication. |
| **role_arn**  string | The role ARN that provides OpenSearch permissions for accessing Cognito resources. |
| **user_pool_id**  string | The Cognito user pool ID for OpenSearch Dashboards authentication. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **domain_endpoint_options**  dictionary | Options to specify configuration that will be applied to the domain endpoint. |
| **custom_endpoint**  string | The fully qualified domain for your custom endpoint. |
| **custom_endpoint_certificate_arn**  string | The ACM certificate ARN for your custom endpoint. |
| **custom_endpoint_enabled**  boolean | Whether to enable a custom endpoint for the domain.  **Choices:**   - `false` - `true` |
| **enforce_https**  boolean | Whether only HTTPS endpoint should be enabled for the domain.  **Choices:**   - `false` - `true` |
| **tls_security_policy**  string | Specify the TLS security policy to apply to the HTTPS endpoint of the domain. |
| **domain_name**  string / required | The name of the Amazon OpenSearch/ElasticSearch Service domain.  Domain names are unique across the domains owned by an account within an AWS region. |
| **ebs_options**  dictionary | Parameters to configure EBS-based storage for an OpenSearch Service domain. |
| **ebs_enabled**  boolean | Specifies whether EBS-based storage is enabled.  **Choices:**   - `false` - `true` |
| **iops**  integer | The IOPD for a Provisioned IOPS EBS volume (SSD). |
| **volume_size**  integer | Integer to specify the size of an EBS volume. |
| **volume_type**  string | Specifies the volume type for EBS-based storage. “standard”|”gp2”|”io1” |
| **encryption_at_rest_options**  dictionary | Parameters to enable encryption at rest. |
| **enabled**  boolean | Should data be encrypted while at rest.  **Choices:**   - `false` - `true` |
| **kms_key_id**  string | If encryption at rest enabled, this identifies the encryption key to use.  The value should be a KMS key ARN. It can also be the KMS key id. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **engine_version**  string | -> The engine version to use. For example, ‘ElasticSearch_7.10’ or ‘OpenSearch_1.1’. -> If the currently running version is not equal to *engine_version*, a cluster upgrade is triggered. -> It may not be possible to upgrade directly from the currently running version to *engine_version*. In that case, the upgrade is performed incrementally by upgrading to the highest compatible version, then repeat the operation until the cluster is running at the target version. -> The upgrade operation fails if there is no path from current version to *engine_version*. -> See OpenSearch documentation for upgrade compatibility. |
| **node_to_node_encryption_options**  dictionary | Node-to-node encryption options. |
| **enabled**  boolean | True to enable node-to-node encryption.  **Choices:**   - `false` - `true` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **snapshot_options**  dictionary | Option to set time, in UTC format, of the daily automated snapshot. |
| **automated_snapshot_start_hour**  integer | Integer value from 0 to 23 specifying when the service takes a daily automated snapshot of the specified Elasticsearch domain. |
| **state**  string | Creates or modifies an existing OpenSearch domain.  Deletes an OpenSearch domain.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **vpc_options**  dictionary | Options to specify the subnets and security groups for a VPC endpoint. |
| **security_groups**  list / elements=string | Specifies the security group ids for VPC endpoint. |
| **subnets**  list / elements=string | Specifies the subnet ids for VPC endpoint. |
| **wait**  boolean | Whether or not to wait for completion of OpenSearch creation, modification or deletion.  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | how long before wait gives up, in seconds.  **Default:** `300` |

## [Notes](opensearch_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](opensearch_module.md#id5)

```yaml+jinja
- name: Create OpenSearch domain for dev environment, no zone awareness, no dedicated masters
  community.aws.opensearch:
    domain_name: "dev-cluster"
    engine_version: Elasticsearch_1.1
    cluster_config:
      instance_type: "t2.small.search"
      instance_count: 2
      zone_awareness: false
      dedicated_master: false
    ebs_options:
      ebs_enabled: true
      volume_type: "gp2"
      volume_size: 10
    access_policies: "{{ lookup('file', 'policy.json') | from_json }}"

- name: Create OpenSearch domain with dedicated masters
  community.aws.opensearch:
    domain_name: "my-domain"
    engine_version: OpenSearch_1.1
    cluster_config:
      instance_type: "t2.small.search"
      instance_count: 12
      dedicated_master: true
      zone_awareness: true
      availability_zone_count: 2
      dedicated_master_instance_type: "t2.small.search"
      dedicated_master_instance_count: 3
      warm_enabled: true
      warm_type: "ultrawarm1.medium.search"
      warm_count: 1
      cold_storage_options:
        enabled: false
    ebs_options:
      ebs_enabled: true
      volume_type: "io1"
      volume_size: 10
      iops: 1000
    vpc_options:
      subnets:
        - "subnet-e537d64a"
        - "subnet-e537d64b"
      security_groups:
        - "sg-dd2f13cb"
        - "sg-dd2f13cc"
    snapshot_options:
      automated_snapshot_start_hour: 13
    access_policies: "{{ lookup('file', 'policy.json') | from_json }}"
    encryption_at_rest_options:
      enabled: false
    node_to_node_encryption_options:
      enabled: false
    auto_tune_options:
      enabled: true
      maintenance_schedules:
      - start_at: "2025-01-12"
        duration:
          value: 1
          unit: "HOURS"
        cron_expression_for_recurrence: "cron(0 12 * * ? *)"
      - start_at: "2032-01-12"
        duration:
          value: 2
          unit: "HOURS"
        cron_expression_for_recurrence: "cron(0 12 * * ? *)"
    tags:
      Environment: Development
      Application: Search
    wait: true

- name: Increase size of EBS volumes for existing cluster
  community.aws.opensearch:
    domain_name: "my-domain"
    ebs_options:
      volume_size: 5
    wait: true

- name: Increase instance count for existing cluster
  community.aws.opensearch:
    domain_name: "my-domain"
    cluster_config:
      instance_count: 40
    wait: true
```

### Authors

- Sebastien Rosset (@sebastien-rosset)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
