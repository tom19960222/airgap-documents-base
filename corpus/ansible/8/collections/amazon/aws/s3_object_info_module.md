---
collection: ansible
version: "8"
title: "amazon.aws.s3_object_info module – Gather information about objects in S3"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/s3_object_info_module.html
fetched_at: 2026-07-28T01:07:16+00:00
---
# amazon.aws.s3_object_info module – Gather information about objects in S3

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
> see [Requirements](s3_object_info_module.md#ansible-collections-amazon-aws-s3-object-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.s3_object_info`.

New in amazon.aws 5.0.0

- [Synopsis](s3_object_info_module.md#synopsis)
- [Requirements](s3_object_info_module.md#requirements)
- [Parameters](s3_object_info_module.md#parameters)
- [Notes](s3_object_info_module.md#notes)
- [Examples](s3_object_info_module.md#examples)
- [Return Values](s3_object_info_module.md#return-values)

## [Synopsis](s3_object_info_module.md#id1)

- Describes objects in S3.
- Compatible with AWS, DigitalOcean, Ceph, Walrus, FakeS3 and StorageGRID (only supports list_keys currently).
- When using non-AWS services, *endpoint_url* should be specified.

## [Requirements](s3_object_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](s3_object_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **bucket_name**  string / required | The name of the bucket that contains the object. |
| **ceph**  aliases: rgw  boolean | Enable API compatibility with Ceph RGW.  It takes into account the S3 API subset working with Ceph in order to provide the same module behaviour where possible.  Requires *endpoint_url* if *ceph=true*.  **Choices:**   - `false` ← (default) - `true` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **dualstack**  boolean | Enables Amazon S3 Dual-Stack Endpoints, allowing S3 communications using both IPv4 and IPv6.  Support for passing *dualstack* and *endpoint_url* at the same time has been deprecated, the dualstack endpoints are automatically configured using the configured *region*. Support will be removed in a release after 2024-12-01.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | S3 URL endpoint for usage with Ceph, Eucalyptus and fakes3 etc. Otherwise assumes AWS. |
| **object_details**  dictionary | Retrieve requested S3 object detailed information. |
| **attributes_list**  list / elements=string | The fields/details that should be returned.  Required when *object_attributes* is `true` in *object_details*.  **Choices:**   - `"ETag"` - `"Checksum"` - `"ObjectParts"` - `"StorageClass"` - `"ObjectSize"` |
| **object_acl**  boolean | Retreive S3 object ACL.  **Choices:**   - `false` ← (default) - `true` |
| **object_attributes**  boolean | Retreive S3 object attributes.  **Choices:**   - `false` ← (default) - `true` |
| **object_legal_hold**  boolean | Retreive S3 object legal_hold.  **Choices:**   - `false` ← (default) - `true` |
| **object_lock_configuration**  boolean | Retreive S3 object lock_configuration.  **Choices:**   - `false` ← (default) - `true` |
| **object_retention**  boolean | Retreive S3 object retention.  **Choices:**   - `false` ← (default) - `true` |
| **object_tagging**  boolean | Retreive S3 object Tags.  **Choices:**   - `false` ← (default) - `true` |
| **object_name**  string | The name of the object.  If not specified, a list of all objects in the specified bucket will be returned. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](s3_object_info_module.md#id4)

> **Note:**
>
> - Support for the `S3_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01, please use the *endpoint_url* parameter or the `AWS_URL` environment variable.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](s3_object_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Retrieve a list of objects in S3 bucket
  amazon.aws.s3_object_info:
    bucket_name: MyTestBucket

- name: Retrieve a list of objects in Ceph RGW S3
  amazon.aws.s3_object_info:
    bucket_name: MyTestBucket
    ceph: true
    endpoint_url: "http://localhost:8000"

- name: Retrieve object metadata without object itself
  amazon.aws.s3_object_info:
    bucket_name: MyTestBucket
    object_name: MyTestObjectKey

- name: Retrieve detailed S3 information for all objects in the bucket
  amazon.aws.s3_object_info:
    bucket_name: MyTestBucket
    object_details:
      object_acl: true
      object_attributes: true
      attributes_list:
        - ETag
        - ObjectSize
        - StorageClass

- name: Retrieve detailed S3 object information
  amazon.aws.s3_object_info:
    bucket_name: MyTestBucket
    object_name: MyTestObjectKey
    object_details:
      object_acl: true
      object_tagging: true
      object_legal_hold: true
      object_attributes: true
      attributes_list:
        - ETag
        - ObjectSize
```

## [Return Values](s3_object_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object_info**  list / elements=dictionary | S3 object details.  **Returned:** when *bucket_name* and *object_name* are specified. |
| **object_acl**  complex | Access control list (ACL) of an object.  **Returned:** when *object_acl* is set to *true*. |
| **grants**  complex | A list of grants.  **Returned:** always |
| **grantee**  complex | The entity being granted permissions.  **Returned:** always |
| **id**  string | The canonical user ID of the grantee.  **Returned:** always  **Sample:** `"xxxxxxxxxxxxxxxxxxx"` |
| **type**  string | type of grantee.  **Returned:** always  **Sample:** `"CanonicalUser"` |
| **permission**  string | Specifies the permission given to the grantee.  **Returned:** always  **Sample:** `"FULL CONTROL"` |
| **owner**  complex | Bucket owner’s display ID and name.  **Returned:** always |
| **display_name**  string | Bucket owner’s display name.  **Returned:** always  **Sample:** `"abcd"` |
| **id**  string | Bucket owner’s ID.  **Returned:** always  **Sample:** `"xxxxxxxxxxxxxxxxxxxxx"` |
| **object_attributes**  complex | Object attributes.  **Returned:** when *object_attributes* is set to *true*. |
| **checksum**  complex | The checksum or digest of the object.  **Returned:** always |
| **checksum_crc32**  string | The base64-encoded, 32-bit CRC32 checksum of the object.  **Returned:** if it was upload with the object.  **Sample:** `"xxxxxxxxxxxx"` |
| **checksum_crc32c**  string | The base64-encoded, 32-bit CRC32C checksum of the object.  **Returned:** if it was upload with the object.  **Sample:** `"xxxxxxxxxxxx"` |
| **checksum_sha1**  string | The base64-encoded, 160-bit SHA-1 digest of the object.  **Returned:** if it was upload with the object.  **Sample:** `"xxxxxxxxxxxx"` |
| **checksum_sha256**  string | The base64-encoded, 256-bit SHA-256 digest of the object.  **Returned:** if it was upload with the object.  **Sample:** `"xxxxxxxxxxxx"` |
| **etag**  string | An ETag is an opaque identifier assigned by a web server to a specific version of a resource found at a URL.  **Returned:** always  **Sample:** `"8fa34xxxxxxxxxxxxxxxxxxxxx35c6f3b"` |
| **last_modified**  string | The creation date of the object.  **Returned:** always  **Sample:** `"2022-08-10T01:11:03+00:00"` |
| **object_parts**  complex | A collection of parts associated with a multipart upload.  **Returned:** always |
| **is_truncated**  boolean | Indicates whether the returned list of parts is truncated.  **Returned:** always |
| **max_parts**  integer | The maximum number of parts allowed in the response.  **Returned:** always |
| **next_part_number_marker**  integer | When a list is truncated, this element specifies the last part in the list  As well as the value to use for the PartNumberMarker request parameter in a subsequent request.  **Returned:** always |
| **part_number_marker**  integer | The marker for the current part.  **Returned:** always |
| **total_parts_count**  integer | The total number of parts.  **Returned:** always |
| **object_size**  integer | The size of the object in bytes.  **Returned:** alwayS  **Sample:** `819` |
| **parts**  complex | A container for elements related to an individual part.  **Returned:** always |
| **checksum_crc32**  string | The base64-encoded, 32-bit CRC32 checksum of the object.  **Returned:** if it was upload with the object.  **Sample:** `"xxxxxxxxxxxx"` |
| **checksum_crc32c**  string | The base64-encoded, 32-bit CRC32C checksum of the object.  **Returned:** if it was upload with the object.  **Sample:** `"xxxxxxxxxxxx"` |
| **checksum_sha1**  string | The base64-encoded, 160-bit SHA-1 digest of the object.  **Returned:** if it was upload with the object.  **Sample:** `"xxxxxxxxxxxx"` |
| **checksum_sha256**  string | The base64-encoded, 256-bit SHA-256 digest of the object.  **Returned:** if it was upload with the object.  **Sample:** `"xxxxxxxxxxxx"` |
| **part_number**  integer | The part number identifying the part. This value is a positive integer between 1 and 10,000.  **Returned:** always |
| **size**  integer | The size of the uploaded part in bytes.  **Returned:** always |
| **storage_class**  string | The storage class information of the object.  **Returned:** always  **Sample:** `"STANDARD"` |
| **object_data**  dictionary | A dict containing the metadata of S3 object.  **Returned:** when *bucket_name* and *object_name* are specified but *object_details* is not specified. |
| **accept_ranges**  string | Indicates that a range of bytes was specified.  **Returned:** always |
| **content_length**  integer | Size of the body (object data) in bytes.  **Returned:** always |
| **content_type**  string | A standard MIME type describing the format of the object data.  **Returned:** always |
| **e_tag**  string | A opaque identifier assigned by a web server to a specific version of a resource found at a URL.  **Returned:** always |
| **last_modified**  string | Creation date of the object.  **Returned:** always |
| **metadata**  dictionary | A map of metadata to store with the object in S3.  **Returned:** always |
| **server_side_encryption**  string | The server-side encryption algorithm used when storing this object in Amazon S3.  **Returned:** always |
| **tag_count**  integer | The number of tags, if any, on the object.  **Returned:** always |
| **object_legal_hold**  complex | Object’s current legal hold status  **Returned:** when *object_legal_hold* is set to *true* and object legal hold is set on the bucket. |
| **legal_hold**  complex | The current legal hold status for the specified object.  **Returned:** always |
| **status**  string | Indicates whether the specified object has a legal hold in place.  **Returned:** always  **Sample:** `"ON"` |
| **object_lock_configuration**  complex | Object Lock configuration for a bucket.  **Returned:** when *object_lock_configuration* is set to *true* and object lock configuration is set on the bucket. |
| **object_lock_enabled**  string | Indicates whether this bucket has an Object Lock configuration enabled.  **Returned:** always |
| **rule**  complex | Specifies the Object Lock rule for the specified object.  **Returned:** always |
| **default_retention**  complex | The default Object Lock retention mode and period that you want to apply to new objects placed in the specified bucket.  **Returned:** always |
| **days**  integer | The number of days that you want to specify for the default retention period.  **Returned:** always |
| **mode**  string | The default Object Lock retention mode you want to apply to new objects placed in the specified bucket.  Must be used with either Days or Years.  **Returned:** always |
| **years**  integer | The number of years that you want to specify for the default retention period.  **Returned:** always |
| **object_retention**  complex | Object’s retention settings.  **Returned:** when *object_retention* is set to *true* and object retention is set on the bucket. |
| **retention**  complex | The container element for an object’s retention settings.  **Returned:** always |
| **mode**  string | Indicates the Retention mode for the specified object.  **Returned:** always |
| **retain_until_date**  string | The date on which this Object Lock Retention will expire.  **Returned:** always |
| **object_tagging**  dictionary | The tag-set of an object  **Returned:** when *object_tagging* is set to *true*. |
| **s3_keys**  list / elements=string | List of object keys.  **Returned:** when only *bucket_name* is specified and *object_name*, *object_details* are not specified.  **Sample:** `["prefix1/", "prefix1/key1", "prefix1/key2"]` |

### Authors

- Mandar Vijay Kulkarni (@mandar242)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
