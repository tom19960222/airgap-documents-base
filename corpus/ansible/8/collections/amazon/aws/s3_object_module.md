---
collection: ansible
version: "8"
title: "amazon.aws.s3_object module – Manage objects in S3"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/s3_object_module.html
fetched_at: 2026-07-28T01:07:15+00:00
---
# amazon.aws.s3_object module – Manage objects in S3

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
> see [Requirements](s3_object_module.md#ansible-collections-amazon-aws-s3-object-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.s3_object`.

New in amazon.aws 1.0.0

- [Synopsis](s3_object_module.md#synopsis)
- [Requirements](s3_object_module.md#requirements)
- [Parameters](s3_object_module.md#parameters)
- [Notes](s3_object_module.md#notes)
- [Examples](s3_object_module.md#examples)
- [Return Values](s3_object_module.md#return-values)

## [Synopsis](s3_object_module.md#id1)

- This module allows the user to manage the objects and directories within S3 buckets. Includes support for creating and deleting objects and directories, retrieving objects as files or strings, generating download links and copying objects that are already stored in Amazon S3.
- S3 buckets can be created or deleted using the [amazon.aws.s3_bucket](s3_bucket_module.md#ansible-collections-amazon-aws-s3-bucket-module) module.
- Compatible with AWS, DigitalOcean, Ceph, Walrus, FakeS3 and StorageGRID.
- When using non-AWS services, *endpoint_url* should be specified.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: aws_s3

## [Requirements](s3_object_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](s3_object_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **bucket**  string / required | Bucket name. |
| **ceph**  aliases: rgw  boolean | Enable API compatibility with Ceph RGW.  It takes into account the S3 API subset working with Ceph in order to provide the same module behaviour where possible.  Requires *endpoint_url* if *ceph=true*.  **Choices:**   - `false` ← (default) - `true` |
| **content**  string  *added in amazon.aws 1.3.0* | The content to `put` into an object.  The parameter value will be treated as a string and converted to UTF-8 before sending it to S3.  To send binary data, use the *content_base64* parameter instead.  One of *content*, *content_base64* or *src* must be specified when *mode=put* otherwise ignored. |
| **content_base64**  string  *added in amazon.aws 1.3.0* | The base64-encoded binary data to `put` into an object.  Use this if you need to put raw binary data, and don’t forget to encode in base64.  One of *content*, *content_base64* or *src* must be specified when *mode=put* otherwise ignored. |
| **copy_src**  dictionary  *added in amazon.aws 2.0.0* | The source details of the object to copy.  Required if *mode=copy*. |
| **bucket**  string / required | The name of the source bucket. |
| **object**  string / required | key name of the source object. |
| **version_id**  string | version ID of the source object. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **dest**  path | The destination file path when downloading an object/key when *mode=get*.  Ignored when *mode* is not `get`. |
| **dualstack**  boolean | Enables Amazon S3 Dual-Stack Endpoints, allowing S3 communications using both IPv4 and IPv6.  Support for passing *dualstack* and *endpoint_url* at the same time has been deprecated, the dualstack endpoints are automatically configured using the configured *region*. Support will be removed in a release after 2024-12-01.  **Choices:**   - `false` ← (default) - `true` |
| **encrypt**  boolean | Asks for server-side encryption of the objects when *mode=put* or *mode=copy*.  Ignored when *mode* is neither `put` nor `copy`.  **Choices:**   - `false` - `true` ← (default) |
| **encryption_kms_key_id**  string | KMS key id to use when encrypting objects using *encrypting=aws:kms*.  Ignored if *encryption* is not `aws:kms`. |
| **encryption_mode**  string | The encryption mode to use if *encrypt=true*.  **Choices:**   - `"AES256"` ← (default) - `"aws:kms"` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **expiry**  aliases: expiration  integer | Time limit (in seconds) for the URL generated and returned by S3/Walrus when performing a *mode=put* or *mode=geturl* operation.  Ignored when *mode* is neither `put` nor `geturl`.  **Default:** `600` |
| **headers**  dictionary | Custom headers to use when *mode=put* as a dictionary of key value pairs.  Ignored when *mode* is not `put`. |
| **ignore_nonexistent_bucket**  boolean | Overrides initial bucket lookups in case bucket or IAM policies are restrictive.  This can be useful when a user may have the `GetObject` permission but no other permissions. In which case using *mode=get* will fail unless *ignore_nonexistent_bucket=true* is specified.  **Choices:**   - `false` ← (default) - `true` |
| **marker**  string | Specifies the key to start with when using list mode. Object keys are returned in alphabetical order, starting with key after the marker in order.  **Default:** `""` |
| **max_keys**  integer | Max number of results to return when *mode=list*, set this if you want to retrieve fewer than the default 1000 keys.  Ignored when *mode* is not `list`.  **Default:** `1000` |
| **metadata**  dictionary | Metadata to use when *mode=put* or *mode=copy* as a dictionary of key value pairs. |
| **mode**  string / required | Switches the module behaviour between  `put`: upload  `get`: download  `geturl`: return download URL  `getstr`: download object as string  `list`: list keys  `create`: create bucket directories  `delobj`: delete object  `copy`: copy object that is already stored in another bucket  Support for creating and deleting buckets was removed in release 6.0.0. To create and manage the bucket itself please use the [amazon.aws.s3_bucket](s3_bucket_module.md#ansible-collections-amazon-aws-s3-bucket-module) module.  **Choices:**   - `"get"` - `"put"` - `"create"` - `"geturl"` - `"getstr"` - `"delobj"` - `"list"` - `"copy"` |
| **object**  string | Key name of the object inside the bucket.  Can be used to create “virtual directories”, see examples.  Object key names should not include the leading `/`, see <https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html> for more information.  Support for passing the leading `/` has been deprecated and will be removed in a release after 2025-12-01. |
| **overwrite**  aliases: force  string | Force overwrite either locally on the filesystem or remotely with the object/key.  Used when *mode=put* or *mode=get*.  Ignored when when *mode* is neither `put` nor `get`.  Must be a Boolean, `always`, `never`, `different` or `latest`.  `true` is the same as `always`.  `false` is equal to `never`.  When this is set to `different` the MD5 sum of the local file is compared with the ‘ETag’ of the object/key in S3. The ETag may or may not be an MD5 digest of the object data. See the ETag response header here <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonResponseHeaders.html>.  When *mode=get* and *overwrite=latest* the last modified timestamp of local file is compared with the ‘LastModified’ of the object/key in S3.  **Default:** `"different"` |
| **permission**  list / elements=string | This option lets the user set the canned permissions on the object/bucket that are created. The permissions that can be set are `private`, `public-read`, `public-read-write`, `authenticated-read` for a bucket or `private`, `public-read`, `public-read-write`, `aws-exec-read`, `authenticated-read`, `bucket-owner-read`, `bucket-owner-full-control` for an object. Multiple permissions can be specified as a list; although only the first one will be used during the initial upload of the file.  For a full list of permissions see the AWS documentation <https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl>.  **Choices:**   - `"private"` ← (default) - `"public-read"` - `"public-read-write"` - `"aws-exec-read"` - `"authenticated-read"` - `"bucket-owner-read"` - `"bucket-owner-full-control"`   **Default:** `["private"]` |
| **prefix**  string | Limits the response to keys that begin with the specified prefix for list mode.  **Default:** `""` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **retries**  aliases: retry  integer | On recoverable failure, how many times to retry before actually failing.  **Default:** `0` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **sig_v4**  boolean  *added in amazon.aws 5.0.0* | Forces the Boto SDK to use Signature Version 4.  Only applies to get modes, *mode=get*, *mode=getstr*, *mode=geturl*.  **Choices:**   - `false` - `true` ← (default) |
| **src**  path | The source file path when performing a `put` operation.  One of *content*, *content_base64* or *src* must be specified when *mode=put* otherwise ignored. |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_bucket_name**  boolean  *added in amazon.aws 3.1.0* | Whether the bucket name should be validated to conform to AWS S3 naming rules.  On by default, this may be disabled for S3 backends that do not enforce these rules.  See the Amazon documentation for more information about bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html>.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **version**  string | Version ID of the object inside the bucket. Can be used to get a specific version of a file if versioning is enabled in the target bucket. |

## [Notes](s3_object_module.md#id4)

> **Note:**
>
> - Support for *tags* and *purge_tags* was added in release 2.0.0.
> - In release 5.0.0 the *s3_url* parameter was merged into the *endpoint_url* parameter, *s3_url* remains as an alias for *endpoint_url*.
> - For Walrus *endpoint_url* should be set to the FQDN of the endpoint with neither scheme nor path.
> - Support for the `S3_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01, please use the *endpoint_url* parameter or the `AWS_URL` environment variable.
> - Support for creating and deleting buckets was removed in release 6.0.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](s3_object_module.md#id5)

```yaml+jinja
- name: Simple PUT operation
  amazon.aws.s3_object:
    bucket: mybucket
    object: /my/desired/key.txt
    src: /usr/local/myfile.txt
    mode: put

- name: PUT operation from a rendered template
  amazon.aws.s3_object:
    bucket: mybucket
    object: /object.yaml
    content: "{{ lookup('template', 'templates/object.yaml.j2') }}"
    mode: put

- name: Simple PUT operation in Ceph RGW S3
  amazon.aws.s3_object:
    bucket: mybucket
    object: /my/desired/key.txt
    src: /usr/local/myfile.txt
    mode: put
    ceph: true
    endpoint_url: "http://localhost:8000"

- name: Simple GET operation
  amazon.aws.s3_object:
    bucket: mybucket
    object: /my/desired/key.txt
    dest: /usr/local/myfile.txt
    mode: get

- name: Get a specific version of an object.
  amazon.aws.s3_object:
    bucket: mybucket
    object: /my/desired/key.txt
    version: 48c9ee5131af7a716edc22df9772aa6f
    dest: /usr/local/myfile.txt
    mode: get

- name: PUT/upload with metadata
  amazon.aws.s3_object:
    bucket: mybucket
    object: /my/desired/key.txt
    src: /usr/local/myfile.txt
    mode: put
    metadata: 'Content-Encoding=gzip,Cache-Control=no-cache'

- name: PUT/upload with custom headers
  amazon.aws.s3_object:
    bucket: mybucket
    object: /my/desired/key.txt
    src: /usr/local/myfile.txt
    mode: put
    headers: 'x-amz-grant-full-control=emailAddress=owner@example.com'

- name: List keys simple
  amazon.aws.s3_object:
    bucket: mybucket
    mode: list

- name: List keys all options
  amazon.aws.s3_object:
    bucket: mybucket
    mode: list
    prefix: /my/desired/
    marker: /my/desired/0023.txt
    max_keys: 472

- name: Create an empty bucket
  amazon.aws.s3_object:
    bucket: mybucket
    mode: create
    permission: public-read

- name: Create a bucket with key as directory, in the EU region
  amazon.aws.s3_object:
    bucket: mybucket
    object: /my/directory/path
    mode: create
    region: eu-west-1

- name: Delete a bucket and all contents
  amazon.aws.s3_object:
    bucket: mybucket
    mode: delete

- name: GET an object but don't download if the file checksums match. New in 2.0
  amazon.aws.s3_object:
    bucket: mybucket
    object: /my/desired/key.txt
    dest: /usr/local/myfile.txt
    mode: get
    overwrite: different

- name: Delete an object from a bucket
  amazon.aws.s3_object:
    bucket: mybucket
    object: /my/desired/key.txt
    mode: delobj

- name: Copy an object already stored in another bucket
  amazon.aws.s3_object:
    bucket: mybucket
    object: /my/desired/key.txt
    mode: copy
    copy_src:
        bucket: srcbucket
        object: /source/key.txt
```

## [Return Values](s3_object_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **contents**  string | Contents of the object as string.  **Returned:** (for getstr operation)  **Sample:** `"Hello, world!"` |
| **expiry**  integer | Number of seconds the presigned url is valid for.  **Returned:** (for geturl operation)  **Sample:** `600` |
| **msg**  string | Message indicating the status of the operation.  **Returned:** always  **Sample:** `"PUT operation complete"` |
| **s3_keys**  list / elements=string | List of object keys.  **Returned:** (for list operation)  **Sample:** `["prefix1/", "prefix1/key1", "prefix1/key2"]` |
| **url**  string | URL of the object.  **Returned:** (for put and geturl operations)  **Sample:** `"https://my-bucket.s3.amazonaws.com/my-key.txt?AWSAccessKeyId=<access-key>&Expires=1506888865&Signature=<signature>"` |

### Authors

- Lester Wade (@lwade)
- Sloane Hertel (@s-hertel)
- Alina Buzachis (@alinabuzachis)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
