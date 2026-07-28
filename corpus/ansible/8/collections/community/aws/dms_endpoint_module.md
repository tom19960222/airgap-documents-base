---
collection: ansible
version: "8"
title: "community.aws.dms_endpoint module – Creates or destroys a data migration services endpoint"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/dms_endpoint_module.html
fetched_at: 2026-07-28T01:40:34+00:00
---
# community.aws.dms_endpoint module – Creates or destroys a data migration services endpoint

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
> see [Requirements](dms_endpoint_module.md#ansible-collections-community-aws-dms-endpoint-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.dms_endpoint`.

New in community.aws 1.0.0

- [Synopsis](dms_endpoint_module.md#synopsis)
- [Requirements](dms_endpoint_module.md#requirements)
- [Parameters](dms_endpoint_module.md#parameters)
- [Notes](dms_endpoint_module.md#notes)
- [Examples](dms_endpoint_module.md#examples)
- [Return Values](dms_endpoint_module.md#return-values)

## [Synopsis](dms_endpoint_module.md#id1)

- Creates or destroys a data migration services endpoint, that can be used to replicate data.

## [Requirements](dms_endpoint_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](dms_endpoint_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **certificatearn**  string | Amazon Resource Name (ARN) for the certificate. |
| **databasename**  string | Name for the database on the origin or target side. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **dmstransfersettings**  dictionary | The settings in JSON format for the DMS transfer type of source endpoint. |
| **dynamodbsettings**  dictionary | Settings in JSON format for the target Amazon DynamoDB endpoint if source or target is dynamodb. |
| **elasticsearchsettings**  dictionary | Settings in JSON format for the target Elasticsearch endpoint. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **endpointidentifier**  string / required | An identifier name for the endpoint. |
| **endpointtype**  string | Type of endpoint we want to manage.  Required when *state=present*.  **Choices:**   - `"source"` - `"target"` |
| **enginename**  string | Database engine that we want to use, please refer to the AWS DMS for more information on the supported engines and their limitations.  Required when *state=present*.  **Choices:**   - `"mysql"` - `"oracle"` - `"postgres"` - `"mariadb"` - `"aurora"` - `"redshift"` - `"s3"` - `"db2"` - `"azuredb"` - `"sybase"` - `"dynamodb"` - `"mongodb"` - `"sqlserver"` |
| **externaltabledefinition**  string | The external table definition. |
| **extraconnectionattributes**  string | Extra attributes for the database connection, the AWS documentation states ” For more information about extra connection attributes, see the documentation section for your data store.” |
| **kinesissettings**  dictionary | Settings in JSON format for the target Amazon Kinesis Data Streams endpoint. |
| **kmskeyid**  string | Encryption key to use to encrypt replication storage and connection information. |
| **mongodbsettings**  dictionary | Settings in JSON format for the source MongoDB endpoint. |
| **password**  string | Password used to connect to the database this attribute can only be written the AWS API does not return this parameter. |
| **port**  integer | TCP port for access to the database. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **retries**  integer | number of times we should retry when deleting a resource  Required when *wait=true*. |
| **s3settings**  dictionary | S3 buckets settings for the target Amazon S3 endpoint. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **servername**  string | Servername that the endpoint will connect to. |
| **serviceaccessrolearn**  string | Amazon Resource Name (ARN) for the service access role that you want to use to create the endpoint. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **sslmode**  string | Mode used for the SSL connection.  **Choices:**   - `"none"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **state**  string | State of the endpoint.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A list of tags to add to the endpoint. |
| **timeout**  integer | Time in seconds we should wait for when deleting a resource.  Required when *wait=true*. |
| **username**  string | Username our endpoint will use to connect to the database. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Whether Ansible should wait for the object to be deleted when *state=absent*.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](dms_endpoint_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](dms_endpoint_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details
- name: Endpoint Creation
  community.aws.dms_endpoint:
    state: absent
    endpointidentifier: 'testsource'
    endpointtype: source
    enginename: aurora
    username: testing1
    password: testint1234
    servername: testing.domain.com
    port: 3306
    databasename: 'testdb'
    sslmode: none
    wait: false
```

## [Return Values](dms_endpoint_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **endpoint**  dictionary | A description of the DMS endpoint.  **Returned:** success |
| **database_name**  string | The name of the database at the endpoint.  **Returned:** success  **Sample:** `"exampledb"` |
| **dms_transfer_settings**  dictionary | Additional transfer related settings.  **Returned:** when additional DMS Transfer settings have been configured. |
| **doc_db_settings**  dictionary | Additional settings for DocumentDB endpoints.  **Returned:** when the *endpoint_type* is `documentdb` |
| **elasticsearch_settings**  dictionary | Additional settings for Elasticsearch endpoints.  **Returned:** when the *endpoint_type* is `elasticsearch` |
| **endpoint_arn**  string | The ARN that uniquely identifies the endpoint.  **Returned:** success  **Sample:** `"arn:aws:dms:us-east-1:123456789012:endpoint:1234556789ABCDEFGHIJKLMNOPQRSTUVWXYZ012"` |
| **endpoint_identifier**  string | The database endpoint identifier.  **Returned:** success  **Sample:** `"ansible-test-12345678-dms"` |
| **endpoint_type**  string | The type of endpoint. Valid values are `SOURCE` and `TARGET`.  **Returned:** success  **Sample:** `"SOURCE"` |
| **engine_display_name**  string | The expanded name for the engine name.  **Returned:** success  **Sample:** `"Amazon Aurora MySQL"` |
| **engine_name**  string | The database engine name.  **Returned:** success  **Sample:** `"aurora"` |
| **i_b_m_db_settings**  dictionary | Additional settings for IBM DB2 endpoints.  **Returned:** when the *endpoint_type* is `db2` |
| **kafka_settings**  dictionary | Additional settings for Kafka endpoints.  **Returned:** when the *endpoint_type* is `kafka` |
| **kinesis_settings**  dictionary | Additional settings for Kinesis endpoints.  **Returned:** when the *endpoint_type* is `kinesis` |
| **kms_key_id**  string | An KMS key ID that is used to encrypt the connection parameters for the endpoint.  **Returned:** success  **Sample:** `"arn:aws:kms:us-east-1:123456789012:key/01234567-abcd-12ab-98fe-123456789abc"` |
| **microsoft_sql_server_settings**  dictionary | Additional settings for Microsoft SQL Server endpoints.  **Returned:** when the *endpoint_type* is `sqlserver` |
| **mongo_db_settings**  dictionary | Additional settings for MongoDB endpoints.  **Returned:** when the *endpoint_type* is `mongodb` |
| **my_sql_settings**  dictionary | Additional settings for MySQL endpoints.  **Returned:** when the *endpoint_type* is `mysql` |
| **neptune_settings**  dictionary | Additional settings for Amazon Neptune endpoints.  **Returned:** when the *endpoint_type* is `neptune` |
| **oracle_settings**  dictionary | Additional settings for Oracle endpoints.  **Returned:** when the *endpoint_type* is `oracle` |
| **port**  string | The port used to access the endpoint.  **Returned:** success  **Sample:** `"3306"` |
| **postgre_sql_settings**  dictionary | Additional settings for PostgrSQL endpoints.  **Returned:** when the *endpoint_type* is `postgres` |
| **redis_settings**  dictionary | Additional settings for Redis endpoints.  **Returned:** when the *endpoint_type* is `redshift` |
| **redshift_settings**  dictionary | Additional settings for Redshift endpoints.  **Returned:** when the *endpoint_type* is `redshift` |
| **s3_settings**  dictionary | Additional settings for S3 endpoints.  **Returned:** when the *endpoint_type* is `s3` |
| **server_name**  string | The name of the server at the endpoint.  **Returned:** success  **Sample:** `"ansible-test-123456789.example.com"` |
| **ssl_mode**  string | The SSL mode used to connect to the endpoint.  **Returned:** success  **Sample:** `"none"` |
| **sybase_settings**  dictionary | Additional settings for Sybase endpoints.  **Returned:** when the *endpoint_type* is `sybase` |
| **tags**  dictionary | A dictionary representing the tags attached to the endpoint.  **Returned:** success  **Sample:** `{"MyTagKey": "MyTagValue"}` |
| **username**  string | The user name used to connect to the endpoint.  **Returned:** success  **Sample:** `"example-username"` |

### Authors

- Rui Moreira (@ruimoreira)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
