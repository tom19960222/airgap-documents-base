---
collection: ansible
version: "6"
title: "community.aws.dms_endpoint module – Creates or destroys a data migration services endpoint"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/dms_endpoint_module.html
fetched_at: 2026-07-27T17:03:49+00:00
---
# community.aws.dms_endpoint module – Creates or destroys a data migration services endpoint

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
> see [Requirements](dms_endpoint_module.md#ansible-collections-community-aws-dms-endpoint-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.dms_endpoint`.

New in community.aws 1.0.0

- [Synopsis](dms_endpoint_module.md#synopsis)
- [Requirements](dms_endpoint_module.md#requirements)
- [Parameters](dms_endpoint_module.md#parameters)
- [Notes](dms_endpoint_module.md#notes)
- [Examples](dms_endpoint_module.md#examples)

## [Synopsis](dms_endpoint_module.md#id1)

- Creates or destroys a data migration services endpoint, that can be used to replicate data.

## [Requirements](dms_endpoint_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](dms_endpoint_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **certificatearn**  string | Amazon Resource Name (ARN) for the certificate. |
| **databasename**  string | Name for the database on the origin or target side. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **dmstransfersettings**  dictionary | The settings in JSON format for the DMS transfer type of source endpoint. |
| **dynamodbsettings**  dictionary | Settings in JSON format for the target Amazon DynamoDB endpoint if source or target is dynamodb. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **elasticsearchsettings**  dictionary | Settings in JSON format for the target Elasticsearch endpoint. |
| **endpointidentifier**  string / required | An identifier name for the endpoint. |
| **endpointtype**  string / required | Type of endpoint we want to manage.  Choices:   - `"source"` - `"target"` |
| **enginename**  string / required | Database engine that we want to use, please refer to the AWS DMS for more information on the supported engines and their limitations.  Choices:   - `"mysql"` - `"oracle"` - `"postgres"` - `"mariadb"` - `"aurora"` - `"redshift"` - `"s3"` - `"db2"` - `"azuredb"` - `"sybase"` - `"dynamodb"` - `"mongodb"` - `"sqlserver"` |
| **externaltabledefinition**  string | The external table definition. |
| **extraconnectionattributes**  string | Extra attributes for the database connection, the AWS documentation states ” For more information about extra connection attributes, see the documentation section for your data store.” |
| **kinesissettings**  dictionary | Settings in JSON format for the target Amazon Kinesis Data Streams endpoint. |
| **kmskeyid**  string | Encryption key to use to encrypt replication storage and connection information. |
| **mongodbsettings**  dictionary | Settings in JSON format for the source MongoDB endpoint. |
| **password**  string | Password used to connect to the database this attribute can only be written the AWS API does not return this parameter. |
| **port**  integer | TCP port for access to the database. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **retries**  integer | number of times we should retry when deleting a resource  Required when *wait=true*. |
| **s3settings**  dictionary | S3 buckets settings for the target Amazon S3 endpoint. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **servername**  string | Servername that the endpoint will connect to. |
| **serviceaccessrolearn**  string | Amazon Resource Name (ARN) for the service access role that you want to use to create the endpoint. |
| **sslmode**  string | Mode used for the SSL connection.  Choices:   - `"none"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **state**  string | State of the endpoint.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | A list of tags to add to the endpoint. |
| **timeout**  integer | Time in seconds we should wait for when deleting a resource.  Required when *wait=true*. |
| **username**  string | Username our endpoint will use to connect to the database. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **wait**  boolean | Whether Ansible should wait for the object to be deleted when *state=absent*.  Choices:   - `false` ← (default) - `true` |

## [Notes](dms_endpoint_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

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

### Authors

- Rui Moreira (@ruimoreira)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
