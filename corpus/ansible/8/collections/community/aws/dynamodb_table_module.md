---
collection: ansible
version: "8"
title: "community.aws.dynamodb_table module – Create, update or delete AWS Dynamo DB tables"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/dynamodb_table_module.html
fetched_at: 2026-07-28T01:40:36+00:00
---
# community.aws.dynamodb_table module – Create, update or delete AWS Dynamo DB tables

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
> see [Requirements](dynamodb_table_module.md#ansible-collections-community-aws-dynamodb-table-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.dynamodb_table`.

New in community.aws 1.0.0

- [Synopsis](dynamodb_table_module.md#synopsis)
- [Requirements](dynamodb_table_module.md#requirements)
- [Parameters](dynamodb_table_module.md#parameters)
- [Notes](dynamodb_table_module.md#notes)
- [Examples](dynamodb_table_module.md#examples)
- [Return Values](dynamodb_table_module.md#return-values)

## [Synopsis](dynamodb_table_module.md#id1)

- Create or delete AWS Dynamo DB tables.
- Can update the provisioned throughput on existing tables.
- Returns the status of the specified table.

## [Requirements](dynamodb_table_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](dynamodb_table_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **billing_mode**  string | Controls whether provisoned pr on-demand tables are created.  **Choices:**   - `"PROVISIONED"` - `"PAY_PER_REQUEST"` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **hash_key_name**  string | Name of the hash key.  Required when *state=present* and table doesn’t exist. |
| **hash_key_type**  string | Type of the hash key.  Defaults to `'STRING'` when creating a new table.  **Choices:**   - `"STRING"` - `"NUMBER"` - `"BINARY"` |
| **indexes**  list / elements=dictionary | list of dictionaries describing indexes to add to the table. global indexes can be updated. local indexes don’t support updates or have throughput.  required options: [‘name’, ‘type’, ‘hash_key_name’]  other options: [‘hash_key_type’, ‘range_key_name’, ‘range_key_type’, ‘includes’, ‘read_capacity’, ‘write_capacity’]  **Default:** `[]` |
| **hash_key_name**  string | The name of the hash-based key.  Required if index doesn’t already exist.  Can not be modified once the index has been created. |
| **hash_key_type**  string | The type of the hash-based key.  Defaults to `'STRING'` when creating a new index.  Can not be modified once the index has been created.  **Choices:**   - `"STRING"` - `"NUMBER"` - `"BINARY"` |
| **includes**  list / elements=string | A list of fields to include when using `global_include` or `include` indexes. |
| **name**  string / required | The name of the index. |
| **range_key_name**  string | The name of the range-based key.  Can not be modified once the index has been created. |
| **range_key_type**  string | The type of the range-based key.  Defaults to `'STRING'` when creating a new index.  Can not be modified once the index has been created.  **Choices:**   - `"STRING"` - `"NUMBER"` - `"BINARY"` |
| **read_capacity**  integer | Read throughput capacity (units) to provision for the index. |
| **type**  string / required | The type of index.  **Choices:**   - `"all"` - `"global_all"` - `"global_include"` - `"global_keys_only"` - `"include"` - `"keys_only"` |
| **write_capacity**  integer | Write throughput capacity (units) to provision for the index. |
| **name**  string / required | Name of the table. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **range_key_name**  string | Name of the range key. |
| **range_key_type**  string | Type of the range key.  Defaults to `'STRING'` when creating a new range key.  **Choices:**   - `"STRING"` - `"NUMBER"` - `"BINARY"` |
| **read_capacity**  integer | Read throughput capacity (units) to provision.  Defaults to `1` when creating a new table. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create or delete the table.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **table_class**  string  *added in community.aws 3.1.0* | The class of the table.  Requires at least botocore version 1.23.18.  **Choices:**   - `"STANDARD"` - `"STANDARD_INFREQUENT_ACCESS"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | When *wait=True* the module will wait for up to *wait_timeout* seconds for index updates, table creation or deletion to complete before returning.  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  aliases: wait_for_active_timeout  integer | How long (in seconds) to wait for creation / update / deletion to complete.  AWS only allows secondary indexies to be updated one at a time, this module will automatically update them in serial, and the timeout will be separately applied for each index.  **Default:** `900` |
| **write_capacity**  integer | Write throughput capacity (units) to provision.  Defaults to `1` when creating a new table. |

## [Notes](dynamodb_table_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](dynamodb_table_module.md#id5)

```yaml+jinja
- name: Create dynamo table with hash and range primary key
  community.aws.dynamodb_table:
    name: my-table
    region: us-east-1
    hash_key_name: id
    hash_key_type: STRING
    range_key_name: create_time
    range_key_type: NUMBER
    read_capacity: 2
    write_capacity: 2
    tags:
      tag_name: tag_value

- name: Update capacity on existing dynamo table
  community.aws.dynamodb_table:
    name: my-table
    region: us-east-1
    read_capacity: 10
    write_capacity: 10

- name: Create pay-per-request table
  community.aws.dynamodb_table:
    name: my-table
    region: us-east-1
    hash_key_name: id
    hash_key_type: STRING
    billing_mode: PAY_PER_REQUEST

- name: set index on existing dynamo table
  community.aws.dynamodb_table:
    name: my-table
    region: us-east-1
    indexes:
      - name: NamedIndex
        type: global_include
        hash_key_name: id
        range_key_name: create_time
        includes:
          - other_field
          - other_field2
        read_capacity: 10
        write_capacity: 10

- name: Delete dynamo table
  community.aws.dynamodb_table:
    name: my-table
    region: us-east-1
    state: absent
```

## [Return Values](dynamodb_table_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **table**  complex | The returned table params from the describe API call.  **Returned:** success  **Sample:** `{"arn": "arn:aws:dynamodb:us-east-1:721066863947:table/ansible-test-table", "attribute_definitions": [{"attribute_name": "id", "attribute_type": "N"}], "billing_mode": "PROVISIONED", "creation_date_time": "2022-02-04T13:36:01.578000+00:00", "id": "533b45fe-0870-4b66-9b00-d2afcfe96f19", "item_count": 0, "key_schema": [{"attribute_name": "id", "key_type": "HASH"}], "name": "ansible-test-14482047-alinas-mbp", "provisioned_throughput": {"number_of_decreases_today": 0, "read_capacity_units": 1, "write_capacity_units": 1}, "size": 0, "status": "ACTIVE", "table_arn": "arn:aws:dynamodb:us-east-1:721066863947:table/ansible-test-table", "table_id": "533b45fe-0870-4b66-9b00-d2afcfe96f19", "table_name": "ansible-test-table", "table_size_bytes": 0, "table_status": "ACTIVE", "tags": {}}` |
| **table_status**  string | The current status of the table.  **Returned:** success  **Sample:** `"ACTIVE"` |

### Authors

- Alan Loi (@loia)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
