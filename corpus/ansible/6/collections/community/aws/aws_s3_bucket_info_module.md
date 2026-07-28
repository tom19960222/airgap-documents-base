---
collection: ansible
version: "6"
title: "community.aws.aws_s3_bucket_info module – lists S3 buckets in AWS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_s3_bucket_info_module.html
fetched_at: 2026-07-27T17:03:31+00:00
---
# community.aws.aws_s3_bucket_info module – lists S3 buckets in AWS

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
> see [Requirements](aws_s3_bucket_info_module.md#ansible-collections-community-aws-aws-s3-bucket-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_s3_bucket_info`.

New in community.aws 1.0.0

- [Synopsis](aws_s3_bucket_info_module.md#synopsis)
- [Requirements](aws_s3_bucket_info_module.md#requirements)
- [Parameters](aws_s3_bucket_info_module.md#parameters)
- [Notes](aws_s3_bucket_info_module.md#notes)
- [Examples](aws_s3_bucket_info_module.md#examples)
- [Return Values](aws_s3_bucket_info_module.md#return-values)

## [Synopsis](aws_s3_bucket_info_module.md#id1)

- Lists S3 buckets and details about those buckets.

## [Requirements](aws_s3_bucket_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_s3_bucket_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **bucket_facts**  dictionary  added in community.aws 1.4.0 | Retrieve requested S3 bucket detailed information  Each bucket_X option executes one API call, hence many options being set to `true` will cause slower module execution.  You can limit buckets by using the *name* or *name_filter* option. |
| **bucket_accelerate_configuration**  boolean | Retrive S3 accelerate configuration.  Choices:   - `false` ← (default) - `true` |
| **bucket_acl**  boolean | Retrive S3 bucket ACLs.  Choices:   - `false` ← (default) - `true` |
| **bucket_cors**  boolean | Retrive S3 bucket CORS configuration.  Choices:   - `false` ← (default) - `true` |
| **bucket_encryption**  boolean | Retrive S3 bucket encryption.  Choices:   - `false` ← (default) - `true` |
| **bucket_lifecycle_configuration**  boolean | Retrive S3 bucket lifecycle configuration.  Choices:   - `false` ← (default) - `true` |
| **bucket_location**  boolean | Retrive S3 bucket location.  Choices:   - `false` ← (default) - `true` |
| **bucket_logging**  boolean | Retrive S3 bucket logging.  Choices:   - `false` ← (default) - `true` |
| **bucket_notification_configuration**  boolean | Retrive S3 bucket notification configuration.  Choices:   - `false` ← (default) - `true` |
| **bucket_ownership_controls**  boolean | Retrive S3 ownership controls.  Choices:   - `false` ← (default) - `true` |
| **bucket_policy**  boolean | Retrive S3 bucket policy.  Choices:   - `false` ← (default) - `true` |
| **bucket_policy_status**  boolean | Retrive S3 bucket policy status.  Choices:   - `false` ← (default) - `true` |
| **bucket_replication**  boolean | Retrive S3 bucket replication.  Choices:   - `false` ← (default) - `true` |
| **bucket_request_payment**  boolean | Retrive S3 bucket request payment.  Choices:   - `false` ← (default) - `true` |
| **bucket_tagging**  boolean | Retrive S3 bucket tagging.  Choices:   - `false` ← (default) - `true` |
| **bucket_website**  boolean | Retrive S3 bucket website.  Choices:   - `false` ← (default) - `true` |
| **public_access_block**  boolean | Retrive S3 bucket public access block.  Choices:   - `false` ← (default) - `true` |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **name**  string  added in community.aws 1.4.0 | Name of bucket to query.  Default: `""` |
| **name_filter**  string  added in community.aws 1.4.0 | Limits buckets to only buckets who’s name contain the string in *name_filter*.  Default: `""` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **transform_location**  boolean  added in community.aws 1.4.0 | S3 bucket location for default us-east-1 is normally reported as `null`.  Setting this option to `true` will return `us-east-1` instead.  Affects only queries with *bucket_facts=true* and *bucket_location=true*.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](aws_s3_bucket_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_s3_bucket_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Note: Only AWS S3 is currently supported

# Lists all s3 buckets
- community.aws.aws_s3_bucket_info:
  register: result

# Retrieve detailed bucket information
- community.aws.aws_s3_bucket_info:
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

## [Return Values](aws_s3_bucket_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **bucket_list**  complex | List of buckets  Returned: always |
| **bucket_acl**  complex | Bucket ACL configuration.  Returned: when *bucket_facts=true* and *bucket_acl=true* |
| **Grants**  list / elements=string | List of ACL grants.  Returned: success  Sample: `[]` |
| **Owner**  complex | Bucket owner information.  Returned: success |
| **DisplayName**  string | Bucket owner user display name.  Returned: always  Sample: `"username"` |
| **ID**  string | Bucket owner user ID.  Returned: always  Sample: `"123894e509349etc"` |
| **bucket_cors**  complex | Bucket CORS configuration.  Returned: when *bucket_facts=true* and *bucket_cors=true* |
| **CORSRules**  list / elements=string | Bucket CORS configuration.  Returned: when CORS rules are defined for the bucket  Sample: `[]` |
| **bucket_encryption**  complex | Bucket encryption configuration.  Returned: when *bucket_facts=true* and *bucket_encryption=true* |
| **ServerSideEncryptionConfiguration**  complex | ServerSideEncryptionConfiguration configuration.  Returned: when encryption is enabled on the bucket |
| **Rules**  list / elements=string | List of applied encryptio rules.  Returned: when encryption is enabled on the bucket  Sample: `{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}, "BucketKeyEnabled": false}` |
| **bucket_lifecycle_configuration**  complex | Bucket lifecycle configuration settings.  Returned: when *bucket_facts=true* and *bucket_lifecycle_configuration=true* |
| **Rules**  list / elements=string | List of lifecycle management rules.  Returned: when lifecycle configuration is present  Sample: `[{"ID": "example-rule", "Status": "Enabled"}]` |
| **bucket_location**  complex | Bucket location.  Returned: when *bucket_facts=true* and *bucket_location=true* |
| **LocationConstraint**  string | AWS region.  Returned: always  Sample: `"us-east-2"` |
| **bucket_logging**  complex | Server access logging configuration.  Returned: when *bucket_facts=true* and *bucket_logging=true* |
| **LoggingEnabled**  complex | Server access logging configuration.  Returned: when server access logging is defined for the bucket |
| **TargetBucket**  string | Target bucket name.  Returned: always  Sample: `"logging-bucket-name"` |
| **TargetPrefix**  string | Prefix in target bucket.  Returned: always  Sample: `""` |
| **bucket_name_filter**  string | String used to limit buckets. See *name_filter*.  Returned: when *name_filter* is defined  Sample: `"filter-by-this-string"` |
| **bucket_notification_configuration**  complex | Bucket notification settings.  Returned: when *bucket_facts=true* and *bucket_notification_configuration=true* |
| **TopicConfigurations**  list / elements=string | List of notification events configurations.  Returned: when at least one notification is configured  Sample: `[]` |
| **bucket_ownership_controls**  complex | Preffered object ownership settings.  Returned: when *bucket_facts=true* and *bucket_ownership_controls=true* |
| **OwnershipControls**  complex | Object ownership settings.  Returned: when ownership controls are defined for the bucket |
| **Rules**  list / elements=string | List of ownership rules.  Returned: when ownership rule is defined  Sample: `[{"ObjectOwnership:": "ObjectWriter"}]` |
| **bucket_policy**  string | Bucket policy contents.  Returned: when *bucket_facts=true* and *bucket_policy=true*  Sample: `"{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"AddCannedAcl\",\"Effect\":\"Allow\",..}}]}"` |
| **bucket_policy_status**  complex | Status of bucket policy.  Returned: when *bucket_facts=true* and *bucket_policy_status=true* |
| **PolicyStatus**  complex | Status of bucket policy.  Returned: when bucket policy is present |
| **IsPublic**  boolean | Report bucket policy public status.  Returned: when bucket policy is present  Sample: `true` |
| **bucket_replication**  complex | Replication configuration settings.  Returned: when *bucket_facts=true* and *bucket_replication=true* |
| **Role**  string | IAM role used for replication.  Returned: when replication rule is defined  Sample: `"arn:aws:iam::123:role/example-role"` |
| **Rules**  list / elements=string | List of replication rules.  Returned: when replication rule is defined  Sample: `[{"Filter": "{}", "ID": "rule-1"}]` |
| **bucket_request_payment**  complex | Requester pays setting.  Returned: when *bucket_facts=true* and *bucket_request_payment=true* |
| **Payer**  string | Current payer.  Returned: always  Sample: `"BucketOwner"` |
| **bucket_tagging**  dictionary | Bucket tags.  Returned: when *bucket_facts=true* and *bucket_tagging=true*  Sample: `{"Tag1": "Value1", "Tag2": "Value2"}` |
| **bucket_website**  complex | Static website hosting.  Returned: when *bucket_facts=true* and *bucket_website=true* |
| **ErrorDocument**  dictionary | Object serving as HTTP error page.  Returned: when static website hosting is enabled  Sample: `{"Key": "error.html"}` |
| **IndexDocument**  dictionary | Object serving as HTTP index page.  Returned: when static website hosting is enabled  Sample: `{"Suffix": "error.html"}` |
| **RedirectAllRequestsTo**  complex | Website redict settings.  Returned: when redirect requests is configured |
| **HostName**  string | Hostname to redirect.  Returned: always  Sample: `"www.example.com"` |
| **Protocol**  string | Protocol used for redirect.  Returned: always  Sample: `"https"` |
| **creation_date**  string | Bucket creation date timestamp.  Returned: always  Sample: `"2021-01-21T12:44:10+00:00"` |
| **name**  string | Bucket name.  Returned: always  Sample: `"a-testing-bucket-name"` |
| **public_access_block**  complex | Bucket public access block configuration.  Returned: when *bucket_facts=true* and *public_access_block=true* |
| **PublicAccessBlockConfiguration**  complex | PublicAccessBlockConfiguration data.  Returned: when PublicAccessBlockConfiguration is defined for the bucket |
| **BlockPublicAcls**  boolean | BlockPublicAcls setting value.  Returned: success  Sample: `true` |
| **BlockPublicPolicy**  boolean | BlockPublicPolicy setting value.  Returned: success  Sample: `true` |
| **IgnorePublicAcls**  boolean | IgnorePublicAcls setting value.  Returned: success  Sample: `true` |
| **RestrictPublicBuckets**  boolean | RestrictPublicBuckets setting value.  Returned: success  Sample: `true` |

### Authors

- Gerben Geijteman (@hyperized)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
