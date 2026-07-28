---
collection: ansible
version: "6"
title: "amazon.aws.s3_bucket module – Manage S3 buckets in AWS, DigitalOcean, Ceph, Walrus, FakeS3 and StorageGRID"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/s3_bucket_module.html
fetched_at: 2026-07-27T16:43:54+00:00
---
# amazon.aws.s3_bucket module – Manage S3 buckets in AWS, DigitalOcean, Ceph, Walrus, FakeS3 and StorageGRID

> **Note:**
>
> This module is part of the [amazon.aws collection](https://galaxy.ansible.com/amazon/aws) (version 3.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](s3_bucket_module.md#ansible-collections-amazon-aws-s3-bucket-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.s3_bucket`.

New in amazon.aws 1.0.0

- [Synopsis](s3_bucket_module.md#synopsis)
- [Requirements](s3_bucket_module.md#requirements)
- [Parameters](s3_bucket_module.md#parameters)
- [Notes](s3_bucket_module.md#notes)
- [Examples](s3_bucket_module.md#examples)
- [Return Values](s3_bucket_module.md#return-values)

## [Synopsis](s3_bucket_module.md#id1)

- Manage S3 buckets in AWS, DigitalOcean, Ceph, Walrus, FakeS3 and StorageGRID.

## [Requirements](s3_bucket_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](s3_bucket_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **acl**  string  added in amazon.aws 3.1.0 | The canned ACL to apply to the bucket.  If your bucket uses the bucket owner enforced setting for S3 Object Ownership, ACLs are disabled and no longer affect permissions.  Choices:   - `"private"` - `"public-read"` - `"public-read-write"` - `"authenticated-read"` |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **ceph**  boolean | Enable API compatibility with Ceph. It takes into account the S3 API subset working with Ceph in order to provide the same module behaviour where possible.  Choices:   - `false` ← (default) - `true` |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **delete_object_ownership**  boolean  added in amazon.aws 2.0.0 | Delete bucket’s ownership controls.  This option cannot be used together with a *object_ownership* definition.  Choices:   - `false` ← (default) - `true` |
| **delete_public_access**  boolean  added in amazon.aws 1.3.0 | Delete public access block configuration from bucket.  This option cannot be used together with a *public_access* definition.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **encryption**  string | Describes the default server-side encryption to apply to new objects in the bucket. In order to remove the server-side encryption, the encryption needs to be set to ‘none’ explicitly.  Choices:   - `"none"` - `"AES256"` - `"aws:kms"` |
| **encryption_key_id**  string | KMS master key ID to use for the default encryption. This parameter is allowed if *encryption* is `aws:kms`. If not specified then it will default to the AWS provided KMS key. |
| **force**  boolean | When trying to delete a bucket, delete all keys (including versions and delete markers) in the bucket first (an S3 bucket must be empty for a successful deletion).  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | Name of the S3 bucket. |
| **object_ownership**  string  added in amazon.aws 2.0.0 | Allow bucket’s ownership controls.  `BucketOwnerEnforced` - ACLs are disabled and no longer affect access permissions to your bucket. Requests to set or update ACLs fail. However, requests to read ACLs are supported. Bucket owner has full ownership and control. Object writer no longer has full ownership and control.  `BucketOwnerPreferred` - Objects uploaded to the bucket change ownership to the bucket owner if the objects are uploaded with the bucket-owner-full-control canned ACL.  `ObjectWriter` - The uploading account will own the object if the object is uploaded with the bucket-owner-full-control canned ACL.  This option cannot be used together with a *delete_object_ownership* definition.  `BucketOwnerEnforced` has been added in version 3.2.0.  Choices:   - `"BucketOwnerEnforced"` - `"BucketOwnerPreferred"` - `"ObjectWriter"` |
| **policy**  json | The JSON policy as a string. Set to the string `"null"` to force the absence of a policy. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **public_access**  dictionary  added in amazon.aws 1.3.0 | Configure public access block for S3 bucket.  This option cannot be used together with *delete_public_access*. |
| **block_public_acls**  boolean | Sets BlockPublicAcls value.  Choices:   - `false` ← (default) - `true` |
| **block_public_policy**  boolean | Sets BlockPublicPolicy value.  Choices:   - `false` ← (default) - `true` |
| **ignore_public_acls**  boolean | Sets IgnorePublicAcls value.  Choices:   - `false` ← (default) - `true` |
| **restrict_public_buckets**  boolean | Sets RestrictPublicAcls value.  Choices:   - `false` ← (default) - `true` |
| **purge_tags**  boolean | Whether to remove tags that aren’t present in the *tags* parameter.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **requester_pays**  boolean | With Requester Pays buckets, the requester instead of the bucket owner pays the cost of the request and the data download from the bucket.  Choices:   - `false` - `true` |
| **s3_url**  aliases: S3_URL  string | S3 URL endpoint for usage with DigitalOcean, Ceph, Eucalyptus and FakeS3 etc.  Assumes AWS if not specified.  For Walrus, use FQDN of the endpoint without scheme nor path. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Create or remove the S3 bucket.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Tags dict to apply to bucket. |
| **validate_bucket_name**  boolean  added in amazon.aws 3.1.0 | Whether the bucket name should be validated to conform to AWS S3 naming rules.  On by default, this may be disabled for S3 backends that do not enforce these rules.  See <https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html>  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **versioning**  boolean | Whether versioning is enabled or disabled (note that once versioning is enabled, it can only be suspended).  Choices:   - `false` - `true` |

## [Notes](s3_bucket_module.md#id4)

> **Note:**
>
> - If `requestPayment`, `policy`, `tagging` or `versioning` operations/API aren’t implemented by the endpoint, module doesn’t fail if each parameter satisfies the following condition. *requester_pays* is `False`, *policy*, *tags*, and *versioning* are `None`.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](s3_bucket_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create a simple S3 bucket
- amazon.aws.s3_bucket:
    name: mys3bucket
    state: present

# Create a simple S3 bucket on Ceph Rados Gateway
- amazon.aws.s3_bucket:
    name: mys3bucket
    s3_url: http://your-ceph-rados-gateway-server.xxx
    ceph: true

# Remove an S3 bucket and any keys it contains
- amazon.aws.s3_bucket:
    name: mys3bucket
    state: absent
    force: yes

# Create a bucket, add a policy from a file, enable requester pays, enable versioning and tag
- amazon.aws.s3_bucket:
    name: mys3bucket
    policy: "{{ lookup('file','policy.json') }}"
    requester_pays: yes
    versioning: yes
    tags:
      example: tag1
      another: tag2

# Create a simple DigitalOcean Spaces bucket using their provided regional endpoint
- amazon.aws.s3_bucket:
    name: mydobucket
    s3_url: 'https://nyc3.digitaloceanspaces.com'

# Create a bucket with AES256 encryption
- amazon.aws.s3_bucket:
    name: mys3bucket
    state: present
    encryption: "AES256"

# Create a bucket with aws:kms encryption, KMS key
- amazon.aws.s3_bucket:
    name: mys3bucket
    state: present
    encryption: "aws:kms"
    encryption_key_id: "arn:aws:kms:us-east-1:1234/5678example"

# Create a bucket with aws:kms encryption, default key
- amazon.aws.s3_bucket:
    name: mys3bucket
    state: present
    encryption: "aws:kms"

# Create a bucket with public policy block configuration
- amazon.aws.s3_bucket:
    name: mys3bucket
    state: present
    public_access:
        block_public_acls: true
        ignore_public_acls: true
        ## keys == 'false' can be omitted, undefined keys defaults to 'false'
        # block_public_policy: false
        # restrict_public_buckets: false

# Delete public policy block from bucket
- amazon.aws.s3_bucket:
    name: mys3bucket
    state: present
    delete_public_access: true

# Create a bucket with object ownership controls set to ObjectWriter
- amazon.aws.s3_bucket:
    name: mys3bucket
    state: present
    object_ownership: ObjectWriter

# Delete onwership controls from bucket
- amazon.aws.s3_bucket:
    name: mys3bucket
    state: present
    delete_object_ownership: true

# Delete a bucket policy from bucket
- amazon.aws.s3_bucket:
    name: mys3bucket
    state: present
    policy: "null"

# This example grants public-read to everyone on bucket using ACL
- amazon.aws.s3_bucket:
    name: mys3bucket
    state: present
    acl: public-read
```

## [Return Values](s3_bucket_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **acl**  dictionary | S3 bucket’s canned ACL.  Returned: *state=present*  Sample: `"public-read"` |
| **encryption**  string | Server-side encryption of the objects in the S3 bucket.  Returned: *state=present*  Sample: `""` |
| **name**  string | Name of the S3 bucket.  Returned: *state=present*  Sample: `"2d3ce10a8210d36d6b4d23b822892074complex"` |
| **object_ownership**  string | S3 bucket’s ownership controls.  Returned: *state=present*  Sample: `"BucketOwnerPreferred"` |
| **policy**  dictionary | S3 bucket’s policy.  Returned: *state=present*  Sample: `{"Statement": [{"Action": "s3:GetObject", "Effect": "Allow", "Principal": "*", "Resource": "arn:aws:s3:::2d3ce10a8210d36d6b4d23b822892074complex/*", "Sid": "AddPerm"}], "Version": "2012-10-17"}` |
| **requester_pays**  string | Indicates that the requester was successfully charged for the request.  Returned: *state=present*  Sample: `""` |
| **tags**  dictionary | S3 bucket’s tags.  Returned: *state=present*  Sample: `{"Tag1": "tag1", "Tag2": "tag2"}` |
| **versioning**  dictionary | S3 bucket’s versioning configuration.  Returned: *state=present*  Sample: `{"MfaDelete": "Disabled", "Versioning": "Enabled"}` |

### Authors

- Rob White (@wimnat)
- Aubin Bikouo (@abikouo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
