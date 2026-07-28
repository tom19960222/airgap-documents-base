---
collection: ansible
version: "8"
title: "community.aws.s3_bucket_info module – Lists S3 buckets in AWS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/s3_bucket_info_module.html
fetched_at: 2026-07-28T01:41:46+00:00
---
# community.aws.s3_bucket_info module – Lists S3 buckets in AWS

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
> see [Requirements](s3_bucket_info_module.md#ansible-collections-community-aws-s3-bucket-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.s3_bucket_info`.

New in community.aws 1.0.0

- [Synopsis](s3_bucket_info_module.md#synopsis)
- [Requirements](s3_bucket_info_module.md#requirements)
- [Parameters](s3_bucket_info_module.md#parameters)
- [Notes](s3_bucket_info_module.md#notes)
- [Examples](s3_bucket_info_module.md#examples)
- [Return Values](s3_bucket_info_module.md#return-values)

## [Synopsis](s3_bucket_info_module.md#id1)

- Lists S3 buckets and details about those buckets.
- Prior to release 5.0.0 this module was called `community.aws.aws_s3_bucket_info`. The usage did not change.

Aliases: aws_s3_bucket_info

## [Requirements](s3_bucket_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](s3_bucket_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **bucket_facts**  dictionary  *added in community.aws 1.4.0* | Retrieve requested S3 bucket detailed information.  Each bucket_X option executes one API call, hence many options being set to `true` will cause slower module execution.  You can limit buckets by using the *name* or *name_filter* option. |
| **bucket_accelerate_configuration**  boolean | Retrive S3 accelerate configuration.  **Choices:**   - `false` ← (default) - `true` |
| **bucket_acl**  boolean | Retrive S3 bucket ACLs.  **Choices:**   - `false` ← (default) - `true` |
| **bucket_cors**  boolean | Retrive S3 bucket CORS configuration.  **Choices:**   - `false` ← (default) - `true` |
| **bucket_encryption**  boolean | Retrive S3 bucket encryption.  **Choices:**   - `false` ← (default) - `true` |
| **bucket_lifecycle_configuration**  boolean | Retrive S3 bucket lifecycle configuration.  **Choices:**   - `false` ← (default) - `true` |
| **bucket_location**  boolean | Retrive S3 bucket location.  **Choices:**   - `false` ← (default) - `true` |
| **bucket_logging**  boolean | Retrive S3 bucket logging.  **Choices:**   - `false` ← (default) - `true` |
| **bucket_notification_configuration**  boolean | Retrive S3 bucket notification configuration.  **Choices:**   - `false` ← (default) - `true` |
| **bucket_ownership_controls**  boolean | Retrive S3 ownership controls.  **Choices:**   - `false` ← (default) - `true` |
| **bucket_policy**  boolean | Retrive S3 bucket policy.  **Choices:**   - `false` ← (default) - `true` |
| **bucket_policy_status**  boolean | Retrive S3 bucket policy status.  **Choices:**   - `false` ← (default) - `true` |
| **bucket_replication**  boolean | Retrive S3 bucket replication.  **Choices:**   - `false` ← (default) - `true` |
| **bucket_request_payment**  boolean | Retrive S3 bucket request payment.  **Choices:**   - `false` ← (default) - `true` |
| **bucket_tagging**  boolean | Retrive S3 bucket tagging.  **Choices:**   - `false` ← (default) - `true` |
| **bucket_website**  boolean | Retrive S3 bucket website.  **Choices:**   - `false` ← (default) - `true` |
| **public_access_block**  boolean | Retrive S3 bucket public access block.  **Choices:**   - `false` ← (default) - `true` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **name**  string  *added in community.aws 1.4.0* | Name of bucket to query.  **Default:** `""` |
| **name_filter**  string  *added in community.aws 1.4.0* | Limits buckets to only buckets who’s name contain the string in *name_filter*.  **Default:** `""` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **transform_location**  boolean  *added in community.aws 1.4.0* | S3 bucket location for default us-east-1 is normally reported as `null`.  Setting this option to `true` will return `us-east-1` instead.  Affects only queries with *bucket_facts=true* and *bucket_location=true*.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](s3_bucket_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](s3_bucket_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Note: Only AWS S3 is currently supported

# Lists all S3 buckets
- community.aws.s3_bucket_info:
  register: result

# Retrieve detailed bucket information
- community.aws.s3_bucket_info:
    # Show only buckets with name matching
    name_filter: your.testing
    # Choose facts to retrieve
    bucket_facts:
      # bucket_accelerate_configuration: true
      bucket_acl: true
      bucket_cors: true
      bucket_encryption: true
      # bucket_lifecycle_configuration: true
      bucket_location: true
      # bucket_logging: true
      # bucket_notification_configuration: true
      # bucket_ownership_controls: true
      # bucket_policy: true
      # bucket_policy_status: true
      # bucket_replication: true
      # bucket_request_payment: true
      # bucket_tagging: true
      # bucket_website: true
      # public_access_block: true
    transform_location: true
    register: result

# Print out result
- name: List buckets
  ansible.builtin.debug:
    msg: "{{ result['buckets'] }}"
```

## [Return Values](s3_bucket_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **bucket_list**  complex | List of buckets  **Returned:** always |
| **bucket_acl**  complex | Bucket ACL configuration.  **Returned:** when *bucket_facts=true* and *bucket_acl=true* |
| **Grants**  list / elements=string | List of ACL grants.  **Returned:** success  **Sample:** `[]` |
| **Owner**  complex | Bucket owner information.  **Returned:** success |
| **DisplayName**  string | Bucket owner user display name.  **Returned:** always  **Sample:** `"username"` |
| **ID**  string | Bucket owner user ID.  **Returned:** always  **Sample:** `"123894e509349etc"` |
| **bucket_cors**  complex | Bucket CORS configuration.  **Returned:** when *bucket_facts=true* and *bucket_cors=true* |
| **CORSRules**  list / elements=string | Bucket CORS configuration.  **Returned:** when CORS rules are defined for the bucket  **Sample:** `[]` |
| **bucket_encryption**  complex | Bucket encryption configuration.  **Returned:** when *bucket_facts=true* and *bucket_encryption=true* |
| **ServerSideEncryptionConfiguration**  complex | ServerSideEncryptionConfiguration configuration.  **Returned:** when encryption is enabled on the bucket |
| **Rules**  list / elements=string | List of applied encryptio rules.  **Returned:** when encryption is enabled on the bucket  **Sample:** `{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}, "BucketKeyEnabled": false}` |
| **bucket_lifecycle_configuration**  complex | Bucket lifecycle configuration settings.  **Returned:** when *bucket_facts=true* and *bucket_lifecycle_configuration=true* |
| **Rules**  list / elements=string | List of lifecycle management rules.  **Returned:** when lifecycle configuration is present  **Sample:** `[{"ID": "example-rule", "Status": "Enabled"}]` |
| **bucket_location**  complex | Bucket location.  **Returned:** when *bucket_facts=true* and *bucket_location=true* |
| **LocationConstraint**  string | AWS region.  **Returned:** always  **Sample:** `"us-east-2"` |
| **bucket_logging**  complex | Server access logging configuration.  **Returned:** when *bucket_facts=true* and *bucket_logging=true* |
| **LoggingEnabled**  complex | Server access logging configuration.  **Returned:** when server access logging is defined for the bucket |
| **TargetBucket**  string | Target bucket name.  **Returned:** always  **Sample:** `"logging-bucket-name"` |
| **TargetPrefix**  string | Prefix in target bucket.  **Returned:** always  **Sample:** `""` |
| **bucket_name_filter**  string | String used to limit buckets. See *name_filter*.  **Returned:** when *name_filter* is defined  **Sample:** `"filter-by-this-string"` |
| **bucket_notification_configuration**  complex | Bucket notification settings.  **Returned:** when *bucket_facts=true* and *bucket_notification_configuration=true* |
| **TopicConfigurations**  list / elements=string | List of notification events configurations.  **Returned:** when at least one notification is configured  **Sample:** `[]` |
| **bucket_ownership_controls**  complex | Preffered object ownership settings.  **Returned:** when *bucket_facts=true* and *bucket_ownership_controls=true* |
| **OwnershipControls**  complex | Object ownership settings.  **Returned:** when ownership controls are defined for the bucket |
| **Rules**  list / elements=string | List of ownership rules.  **Returned:** when ownership rule is defined  **Sample:** `[{"ObjectOwnership:": "ObjectWriter"}]` |
| **bucket_policy**  string | Bucket policy contents.  **Returned:** when *bucket_facts=true* and *bucket_policy=true*  **Sample:** `"{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"AddCannedAcl\",\"Effect\":\"Allow\",..}}]}"` |
| **bucket_policy_status**  complex | Status of bucket policy.  **Returned:** when *bucket_facts=true* and *bucket_policy_status=true* |
| **PolicyStatus**  complex | Status of bucket policy.  **Returned:** when bucket policy is present |
| **IsPublic**  boolean | Report bucket policy public status.  **Returned:** when bucket policy is present  **Sample:** `true` |
| **bucket_replication**  complex | Replication configuration settings.  **Returned:** when *bucket_facts=true* and *bucket_replication=true* |
| **Role**  string | IAM role used for replication.  **Returned:** when replication rule is defined  **Sample:** `"arn:aws:iam::123:role/example-role"` |
| **Rules**  list / elements=string | List of replication rules.  **Returned:** when replication rule is defined  **Sample:** `[{"Filter": "{}", "ID": "rule-1"}]` |
| **bucket_request_payment**  complex | Requester pays setting.  **Returned:** when *bucket_facts=true* and *bucket_request_payment=true* |
| **Payer**  string | Current payer.  **Returned:** always  **Sample:** `"BucketOwner"` |
| **bucket_tagging**  dictionary | Bucket tags.  **Returned:** when *bucket_facts=true* and *bucket_tagging=true*  **Sample:** `{"Tag1": "Value1", "Tag2": "Value2"}` |
| **bucket_website**  complex | Static website hosting.  **Returned:** when *bucket_facts=true* and *bucket_website=true* |
| **ErrorDocument**  dictionary | Object serving as HTTP error page.  **Returned:** when static website hosting is enabled  **Sample:** `{"Key": "error.html"}` |
| **IndexDocument**  dictionary | Object serving as HTTP index page.  **Returned:** when static website hosting is enabled  **Sample:** `{"Suffix": "error.html"}` |
| **RedirectAllRequestsTo**  complex | Website redict settings.  **Returned:** when redirect requests is configured |
| **HostName**  string | Hostname to redirect.  **Returned:** always  **Sample:** `"www.example.com"` |
| **Protocol**  string | Protocol used for redirect.  **Returned:** always  **Sample:** `"https"` |
| **creation_date**  string | Bucket creation date timestamp.  **Returned:** always  **Sample:** `"2021-01-21T12:44:10+00:00"` |
| **name**  string | Bucket name.  **Returned:** always  **Sample:** `"a-testing-bucket-name"` |
| **public_access_block**  complex | Bucket public access block configuration.  **Returned:** when *bucket_facts=true* and *public_access_block=true* |
| **PublicAccessBlockConfiguration**  complex | PublicAccessBlockConfiguration data.  **Returned:** when PublicAccessBlockConfiguration is defined for the bucket |
| **BlockPublicAcls**  boolean | BlockPublicAcls setting value.  **Returned:** success  **Sample:** `true` |
| **BlockPublicPolicy**  boolean | BlockPublicPolicy setting value.  **Returned:** success  **Sample:** `true` |
| **IgnorePublicAcls**  boolean | IgnorePublicAcls setting value.  **Returned:** success  **Sample:** `true` |
| **RestrictPublicBuckets**  boolean | RestrictPublicBuckets setting value.  **Returned:** success  **Sample:** `true` |

### Authors

- Gerben Geijteman (@hyperized)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
