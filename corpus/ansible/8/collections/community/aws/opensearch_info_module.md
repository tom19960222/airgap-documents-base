---
collection: ansible
version: "8"
title: "community.aws.opensearch_info module – obtain information about one or more OpenSearch or ElasticSearch domain"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/opensearch_info_module.html
fetched_at: 2026-07-28T01:41:42+00:00
---
# community.aws.opensearch_info module – obtain information about one or more OpenSearch or ElasticSearch domain

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
> see [Requirements](opensearch_info_module.md#ansible-collections-community-aws-opensearch-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.opensearch_info`.

New in community.aws 4.0.0

- [Synopsis](opensearch_info_module.md#synopsis)
- [Requirements](opensearch_info_module.md#requirements)
- [Parameters](opensearch_info_module.md#parameters)
- [Notes](opensearch_info_module.md#notes)
- [Examples](opensearch_info_module.md#examples)
- [Return Values](opensearch_info_module.md#return-values)

## [Synopsis](opensearch_info_module.md#id1)

- Obtain information about one Amazon OpenSearch Service domain.

## [Requirements](opensearch_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](opensearch_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **domain_name**  string | The name of the Amazon OpenSearch/ElasticSearch Service domain. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **tags**  dictionary | A dict of tags that are used to filter OpenSearch domains that match all tag key, value pairs. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](opensearch_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](opensearch_info_module.md#id5)

```yaml+jinja
- name: Get information about an OpenSearch domain instance
  community.aws.opensearch_info:
    domain_name: my-search-cluster
  register: new_cluster_info

- name: Get all OpenSearch instances
  community.aws.opensearch_info:

- name: Get all OpenSearch instances that have the specified Key, Value tags
  community.aws.opensearch_info:
    tags:
      Applications: search
      Environment: Development
```

## [Return Values](opensearch_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instances**  complex | List of OpenSearch domain instances  **Returned:** always |
| **domain_config**  complex | The OpenSearch domain configuration  **Returned:** always |
| **domain_name**  string | The name of the OpenSearch domain.  **Returned:** always |
| **domain_status**  complex | The current status of the OpenSearch domain.  **Returned:** always |
| **access_policies**  complex | IAM access policy as a JSON-formatted string.  **Returned:** success |
| **advanced_security_options**  complex | Specifies advanced security options.  **Returned:** success |
| **enabled**  boolean | True if advanced security is enabled.  You must enable node-to-node encryption to use advanced security options.  **Returned:** success |
| **internal_user_database_enabled**  boolean | True if the internal user database is enabled.  **Returned:** success |
| **master_user_options**  complex | Credentials for the master user, username and password, ARN, or both.  **Returned:** success |
| **master_user_arn**  string | ARN for the master user (if IAM is enabled).  **Returned:** success |
| **master_user_name**  string | The username of the master user, which is stored in the Amazon OpenSearch Service domain internal database.  **Returned:** success |
| **master_user_password**  string | The password of the master user, which is stored in the Amazon OpenSearch Service domain internal database.  **Returned:** success |
| **saml_options**  complex | The SAML application configuration for the domain.  **Returned:** success |
| **enabled**  boolean | True if SAML is enabled.  **Returned:** success |
| **idp**  complex | The SAML Identity Provider’s information.  **Returned:** success |
| **entity_id**  string | The unique entity ID of the application in SAML identity provider.  **Returned:** success |
| **metadata_content**  string | The metadata of the SAML application in XML format.  **Returned:** success |
| **master_backend_role**  string | The backend role that the SAML master user is mapped to.  **Returned:** success |
| **master_user_name**  string | The SAML master username, which is stored in the Amazon OpenSearch Service domain internal database.  **Returned:** success |
| **roles_key**  string | Element of the SAML assertion to use for backend roles. Default is roles.  **Returned:** success |
| **session_timeout_minutes**  integer | The duration, in minutes, after which a user session becomes inactive. Acceptable values are between 1 and 1440, and the default value is 60.  **Returned:** success |
| **subject_key**  string | Element of the SAML assertion to use for username. Default is NameID.  **Returned:** success |
| **arn**  string | The ARN of the OpenSearch domain.  **Returned:** always |
| **auto_tune_options**  complex | Specifies Auto-Tune options.  **Returned:** success |
| **desired_state**  string | The Auto-Tune desired state. Valid values are ENABLED and DISABLED.  **Returned:** success |
| **maintenance_schedules**  list / elements=dictionary | A list of maintenance schedules.  **Returned:** success |
| **cron_expression_for_recurrence**  string | A cron expression for a recurring maintenance schedule.  **Returned:** success |
| **duration**  complex | Specifies maintenance schedule duration, duration value and duration unit.  **Returned:** success |
| **unit**  string | The unit of a maintenance schedule duration. Valid value is HOURS.  **Returned:** success |
| **value**  integer | Integer to specify the value of a maintenance schedule duration.  **Returned:** success |
| **start_at**  string | The timestamp at which the Auto-Tune maintenance schedule starts.  **Returned:** success |
| **cluster_config**  complex | Parameters for the cluster configuration of an OpenSearch Service domain.  **Returned:** success |
| **availability_zone_count**  integer | An integer value to indicate the number of availability zones for a domain when zone awareness is enabled. This should be equal to number of subnets if VPC endpoints is enabled.  **Returned:** success |
| **cold_storage_options**  complex | Specifies the ColdStorageOptions config for a Domain.  **Returned:** success |
| **enabled**  boolean | True to enable cold storage. Supported on Elasticsearch 7.9 or above.  **Returned:** success |
| **dedicated_master_count**  integer | Total number of dedicated master nodes, active and on standby, for the domain.  **Returned:** success |
| **dedicated_master_enabled**  boolean | A boolean value to indicate whether a dedicated master node is enabled.  **Returned:** success |
| **dedicated_master_type**  string | The instance type for a dedicated master node.  **Returned:** success |
| **instance_count**  integer | Number of instances for the domain.  **Returned:** success |
| **instance_type**  string | Type of the instances to use for the domain.  **Returned:** success |
| **warm_count**  integer | The number of UltraWarm nodes in the domain.  **Returned:** success |
| **warm_enabled**  boolean | True to enable UltraWarm storage.  **Returned:** success |
| **warm_type**  string | The instance type for the OpenSearch domain’s warm nodes.  **Returned:** success |
| **zone_awareness**  boolean | A boolean value to indicate whether zone awareness is enabled.  **Returned:** success |
| **zone_awareness_config**  complex | The zone awareness configuration for a domain when zone awareness is enabled.  **Returned:** success |
| **availability_zone_count**  integer | An integer value to indicate the number of availability zones for a domain when zone awareness is enabled.  **Returned:** success |
| **zone_awareness_enabled**  boolean | A boolean value to indicate whether zone awareness is enabled.  **Returned:** success |
| **cognito_options**  complex | Parameters to configure OpenSearch Service to use Amazon Cognito authentication for OpenSearch Dashboards.  **Returned:** success |
| **enabled**  boolean | The option to enable Cognito for OpenSearch Dashboards authentication.  **Returned:** success |
| **identity_pool_id**  string | The Cognito identity pool ID for OpenSearch Dashboards authentication.  **Returned:** success |
| **role_arn**  string | The role ARN that provides OpenSearch permissions for accessing Cognito resources.  **Returned:** success |
| **user_pool_id**  string | The Cognito user pool ID for OpenSearch Dashboards authentication.  **Returned:** success |
| **created**  boolean | The domain creation status. True if the creation of a domain is complete. False if domain creation is still in progress.  **Returned:** always |
| **deleted**  boolean | The domain deletion status. True if a delete request has been received for the domain but resource cleanup is still in progress. False if the domain has not been deleted. Once domain deletion is complete, the status of the domain is no longer returned.  **Returned:** always |
| **domain_endpoint_options**  complex | Options to specify configuration that will be applied to the domain endpoint.  **Returned:** success |
| **custom_endpoint**  string | The fully qualified domain for your custom endpoint.  **Returned:** success |
| **custom_endpoint_certificate_arn**  string | The ACM certificate ARN for your custom endpoint.  **Returned:** success |
| **custom_endpoint_enabled**  boolean | Whether to enable a custom endpoint for the domain.  **Returned:** success |
| **enforce_https**  boolean | Whether only HTTPS endpoint should be enabled for the domain.  **Returned:** success |
| **tls_security_policy**  string | Specify the TLS security policy to apply to the HTTPS endpoint of the domain.  **Returned:** success |
| **domain_id**  string | The unique identifier for the OpenSearch domain.  **Returned:** always |
| **domain_name**  string | The name of the OpenSearch domain.  **Returned:** always |
| **ebs_options**  complex | Parameters to configure EBS-based storage for an OpenSearch Service domain.  **Returned:** success |
| **ebs_enabled**  boolean | Specifies whether EBS-based storage is enabled.  **Returned:** success |
| **iops**  integer | The IOPD for a Provisioned IOPS EBS volume (SSD).  **Returned:** success |
| **volume_size**  integer | Integer to specify the size of an EBS volume.  **Returned:** success |
| **volume_type**  string | Specifies the volume type for EBS-based storage. “standard”|”gp2”|”io1”  **Returned:** success |
| **encryption_at_rest_options**  complex | Parameters to enable encryption at rest.  **Returned:** success |
| **enabled**  boolean | Should data be encrypted while at rest.  **Returned:** success |
| **kms_key_id**  string | If encryption at rest enabled, this identifies the encryption key to use.  The value should be a KMS key ARN. It can also be the KMS key id.  **Returned:** success |
| **endpoint**  string | The domain endpoint that you use to submit index and search requests.  **Returned:** always |
| **endpoints**  dictionary | Map containing the domain endpoints used to submit index and search requests.  When you create a domain attached to a VPC domain, this propery contains the DNS endpoint to which service requests are submitted.  If you query the opensearch_info immediately after creating the OpenSearch cluster, the VPC endpoint may not be returned. It may take several minutes until the endpoints is available.  **Returned:** success |
| **engine_version**  string | The version of the OpenSearch domain.  **Returned:** always  **Sample:** `"OpenSearch_1.1"` |
| **node_to_node_encryption_options**  complex | Node-to-node encryption options.  **Returned:** success |
| **enabled**  boolean | True to enable node-to-node encryption.  **Returned:** success |
| **processing**  boolean | The status of the domain configuration. True if Amazon OpenSearch Service is processing configuration changes. False if the configuration is active.  **Returned:** always |
| **snapshot_options**  complex | Option to set time, in UTC format, of the daily automated snapshot.  **Returned:** success |
| **automated_snapshot_start_hour**  integer | Integer value from 0 to 23 specifying when the service takes a daily automated snapshot of the specified Elasticsearch domain.  **Returned:** success |
| **upgrade_processing**  boolean | true if a domain upgrade operation is in progress.  **Returned:** always |
| **vpc_options**  complex | Options to specify the subnets and security groups for a VPC endpoint.  **Returned:** success |
| **availability_zones**  list / elements=string | The Availability Zones for the domain..  **Returned:** success |
| **security_group_ids**  list / elements=string | Specifies the security group ids for VPC endpoint.  **Returned:** success |
| **subnet_ids**  list / elements=string | Specifies the subnet ids for VPC endpoint.  **Returned:** success |
| **vpc_id**  string | The VPC ID for the domain.  **Returned:** success |

### Authors

- Sebastien Rosset (@sebastien-rosset)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
