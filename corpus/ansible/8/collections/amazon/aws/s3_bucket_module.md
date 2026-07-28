---
collection: ansible
version: "8"
title: "amazon.aws.s3_bucket module – Manage S3 buckets in AWS, DigitalOcean, Ceph, Walrus, FakeS3 and StorageGRID"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/s3_bucket_module.html
fetched_at: 2026-07-28T01:07:14+00:00
---
# amazon.aws.s3_bucket module – Manage S3 buckets in AWS, DigitalOcean, Ceph, Walrus, FakeS3 and StorageGRID

> **Note:**
>
> This module is part of the [amazon.aws collection](https://galaxy.ansible.com/ui/repo/published/amazon/aws/) (version 6.5.0).
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

- Manage S3 buckets.
- Compatible with AWS, DigitalOcean, Ceph, Walrus, FakeS3 and StorageGRID.
- When using non-AWS services, *endpoint_url* should be specified.

## [Requirements](s3_bucket_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](s3_bucket_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **acl**  string  *added in amazon.aws 3.1.0* | The canned ACL to apply to the bucket.  If your bucket uses the bucket owner enforced setting for S3 Object Ownership, ACLs are disabled and no longer affect permissions.  **Choices:**   - `"private"` - `"public-read"` - `"public-read-write"` - `"authenticated-read"` |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **bucket_key_enabled**  boolean  *added in amazon.aws 4.1.0* | Enable S3 Bucket Keys for SSE-KMS on new objects.  See the AWS documentation for more information <https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html>.  Bucket Key encryption is only supported if *encryption=aws:kms*.  **Choices:**   - `false` - `true` |
| **ceph**  aliases: rgw  boolean | Enable API compatibility with Ceph RGW.  It takes into account the S3 API subset working with Ceph in order to provide the same module behaviour where possible.  Requires *endpoint_url* if *ceph=true*.  **Choices:**   - `false` ← (default) - `true` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **delete_object_ownership**  boolean  *added in amazon.aws 2.0.0* | Delete bucket’s ownership controls.  This option cannot be used together with a *object_ownership* definition.  **Choices:**   - `false` ← (default) - `true` |
| **delete_public_access**  boolean  *added in amazon.aws 1.3.0* | Delete public access block configuration from bucket.  This option cannot be used together with a *public_access* definition.  **Choices:**   - `false` ← (default) - `true` |
| **dualstack**  boolean  *added in amazon.aws 6.0.0* | Enables Amazon S3 Dual-Stack Endpoints, allowing S3 communications using both IPv4 and IPv6.  Mutually exclusive with *endpoint_url*.  **Choices:**   - `false` ← (default) - `true` |
| **encryption**  string | Describes the default server-side encryption to apply to new objects in the bucket. In order to remove the server-side encryption, the encryption needs to be set to ‘none’ explicitly.  Note: Since January 2023 Amazon S3 doesn’t support disabling encryption on S3 buckets.  **Choices:**   - `"none"` - `"AES256"` - `"aws:kms"` |
| **encryption_key_id**  string | KMS master key ID to use for the default encryption.  If not specified then it will default to the AWS provided KMS key.  This parameter is only supported if *encryption* is `aws:kms`. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **force**  boolean | When trying to delete a bucket, delete all keys (including versions and delete markers) in the bucket first (an S3 bucket must be empty for a successful deletion).  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Name of the S3 bucket. |
| **object_lock_enabled**  boolean  *added in amazon.aws 5.3.0* | Whether S3 Object Lock to be enabled.  Defaults to `False` when creating a new bucket.  **Choices:**   - `false` - `true` |
| **object_ownership**  string  *added in amazon.aws 2.0.0* | Allow bucket’s ownership controls.  `BucketOwnerEnforced` - ACLs are disabled and no longer affect access permissions to your bucket. Requests to set or update ACLs fail. However, requests to read ACLs are supported. Bucket owner has full ownership and control. Object writer no longer has full ownership and control.  `BucketOwnerPreferred` - Objects uploaded to the bucket change ownership to the bucket owner if the objects are uploaded with the bucket-owner-full-control canned ACL.  `ObjectWriter` - The uploading account will own the object if the object is uploaded with the bucket-owner-full-control canned ACL.  This option cannot be used together with a *delete_object_ownership* definition.  `BucketOwnerEnforced` has been added in version 3.2.0.  Note: At the end of April 2023 Amazon updated the default setting to `BucketOwnerEnforced`.  **Choices:**   - `"BucketOwnerEnforced"` - `"BucketOwnerPreferred"` - `"ObjectWriter"` |
| **policy**  json | The JSON policy as a string. Set to the string `"null"` to force the absence of a policy. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **public_access**  dictionary  *added in amazon.aws 1.3.0* | Configure public access block for S3 bucket.  This option cannot be used together with *delete_public_access*.  Note: At the end of April 2023 Amazon updated the default settings to block public access by  default. While the defaults for this module remain unchanged, it is necessary to explicitly pass the *public_access* parameter to enable public access ACLs. |
| **block_public_acls**  boolean | Sets BlockPublicAcls value.  **Choices:**   - `false` ← (default) - `true` |
| **block_public_policy**  boolean | Sets BlockPublicPolicy value.  **Choices:**   - `false` ← (default) - `true` |
| **ignore_public_acls**  boolean | Sets IgnorePublicAcls value.  **Choices:**   - `false` ← (default) - `true` |
| **restrict_public_buckets**  boolean | Sets RestrictPublicAcls value.  **Choices:**   - `false` ← (default) - `true` |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **requester_pays**  boolean | With Requester Pays buckets, the requester instead of the bucket owner pays the cost of the request and the data download from the bucket.  **Choices:**   - `false` - `true` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create or remove the S3 bucket.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_bucket_name**  boolean  *added in amazon.aws 3.1.0* | Whether the bucket name should be validated to conform to AWS S3 naming rules.  On by default, this may be disabled for S3 backends that do not enforce these rules.  See <https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html>  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **versioning**  boolean | Whether versioning is enabled or disabled (note that once versioning is enabled, it can only be suspended).  **Choices:**   - `false` - `true` |

## [Notes](s3_bucket_module.md#id4)

> **Note:**
>
> - If `requestPayment`, `policy`, `tagging` or `versioning` operations/API aren’t implemented by the endpoint, module doesn’t fail if each parameter satisfies the following condition. *requester_pays* is `False`, *policy*, *tags*, and *versioning* are `None`.
> - In release 5.0.0 the *s3_url* parameter was merged into the *endpoint_url* parameter, *s3_url* remains as an alias for *endpoint_url*.
> - For Walrus *endpoint_url* should be set to the FQDN of the endpoint with neither scheme nor path.
> - Support for the `S3_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01, please use the *endpoint_url* parameter or the `AWS_URL` environment variable.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

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
    endpoint_url: http://your-ceph-rados-gateway-server.xxx
    ceph: true

# Remove an S3 bucket and any keys it contains
- amazon.aws.s3_bucket:
    name: mys3bucket
    state: absent
    force: true

# Create a bucket, add a policy from a file, enable requester pays, enable versioning and tag
- amazon.aws.s3_bucket:
    name: mys3bucket
    policy: "{{ lookup('file','policy.json') }}"
    requester_pays: true
    versioning: true
    tags:
      example: tag1
      another: tag2

# Create a simple DigitalOcean Spaces bucket using their provided regional endpoint
- amazon.aws.s3_bucket:
    name: mydobucket
    endpoint_url: 'https://nyc3.digitaloceanspaces.com'

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

# Create a bucket with aws:kms encryption, Bucket key
- amazon.aws.s3_bucket:
    name: mys3bucket
    bucket_key_enabled: true
    encryption: "aws:kms"

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
| **acl**  dictionary | S3 bucket’s canned ACL.  **Returned:** *state=present*  **Sample:** `"public-read"` |
| **encryption**  string | Server-side encryption of the objects in the S3 bucket.  **Returned:** *state=present*  **Sample:** `""` |
| **name**  string | Name of the S3 bucket.  **Returned:** *state=present*  **Sample:** `"2d3ce10a8210d36d6b4d23b822892074complex"` |
| **object_ownership**  string | S3 bucket’s ownership controls.  **Returned:** *state=present*  **Sample:** `"BucketOwnerPreferred"` |
| **policy**  dictionary | S3 bucket’s policy.  **Returned:** *state=present*  **Sample:** `{"Statement": [{"Action": "s3:GetObject", "Effect": "Allow", "Principal": "*", "Resource": "arn:aws:s3:::2d3ce10a8210d36d6b4d23b822892074complex/*", "Sid": "AddPerm"}], "Version": "2012-10-17"}` |
| **requester_pays**  string | Indicates that the requester was successfully charged for the request.  **Returned:** *state=present*  **Sample:** `""` |
| **tags**  dictionary | S3 bucket’s tags.  **Returned:** *state=present*  **Sample:** `{"Tag1": "tag1", "Tag2": "tag2"}` |
| **versioning**  dictionary | S3 bucket’s versioning configuration.  **Returned:** *state=present*  **Sample:** `{"MfaDelete": "Disabled", "Versioning": "Enabled"}` |

### Authors

- Rob White (@wimnat)
- Aubin Bikouo (@abikouo)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
