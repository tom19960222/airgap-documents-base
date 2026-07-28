---
collection: ansible
version: "6"
title: "amazon.aws.aws_s3 module – manage objects in S3."
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/aws_s3_module.html
fetched_at: 2026-07-27T16:43:40+00:00
---
# amazon.aws.aws_s3 module – manage objects in S3.

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
> see [Requirements](aws_s3_module.md#ansible-collections-amazon-aws-aws-s3-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.aws_s3`.

New in amazon.aws 1.0.0

- [Synopsis](aws_s3_module.md#synopsis)
- [Requirements](aws_s3_module.md#requirements)
- [Parameters](aws_s3_module.md#parameters)
- [Notes](aws_s3_module.md#notes)
- [Examples](aws_s3_module.md#examples)
- [Return Values](aws_s3_module.md#return-values)

## [Synopsis](aws_s3_module.md#id1)

- This module allows the user to manage S3 buckets and the objects within them. Includes support for creating and deleting both objects and buckets, retrieving objects as files or strings, generating download links and copy of an object that is already stored in Amazon S3.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](aws_s3_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_s3_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **bucket**  string / required | Bucket name. |
| **content**  string  added in amazon.aws 1.3.0 | The content to `PUT` into an object.  The parameter value will be treated as a string and converted to UTF-8 before sending it to S3. To send binary data, use the *content_base64* parameter instead.  Either *content*, *content_base64* or *src* must be specified for a `PUT` operation. Ignored otherwise. |
| **content_base64**  string  added in amazon.aws 1.3.0 | The base64-encoded binary data to `PUT` into an object.  Use this if you need to put raw binary data, and don’t forget to encode in base64.  Either *content*, *content_base64* or *src* must be specified for a `PUT` operation. Ignored otherwise. |
| **copy_src**  dictionary  added in amazon.aws 2.0.0 | The source details of the object to copy.  Required if *mode* is `copy`. |
| **bucket**  string / required | The name of the source bucket. |
| **object**  string / required | key name of the source object. |
| **version_id**  string | version ID of the source object. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **dest**  path | The destination file path when downloading an object/key with a `GET` operation. |
| **dualstack**  boolean | Enables Amazon S3 Dual-Stack Endpoints, allowing S3 communications using both IPv4 and IPv6.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **encrypt**  boolean | When set for PUT/COPY mode, asks for server-side encryption.  Choices:   - `false` - `true` ← (default) |
| **encryption_kms_key_id**  string | KMS key id to use when encrypting objects using *encrypting=aws:kms*. Ignored if *encryption* is not `aws:kms`. |
| **encryption_mode**  string | What encryption mode to use if *encrypt=true*.  Choices:   - `"AES256"` ← (default) - `"aws:kms"` |
| **expiry**  aliases: expiration  integer | Time limit (in seconds) for the URL generated and returned by S3/Walrus when performing a *mode=put* or *mode=geturl* operation.  Default: `600` |
| **headers**  dictionary | Custom headers for `PUT` operation, as a dictionary of `key=value` and `key=value,key=value`. |
| **ignore_nonexistent_bucket**  boolean | Overrides initial bucket lookups in case bucket or iam policies are restrictive. Example: a user may have the `GetObject` permission but no other permissions. In this case using the option mode: get will fail without specifying *ignore_nonexistent_bucket=true*.  Choices:   - `false` ← (default) - `true` |
| **marker**  string | Specifies the key to start with when using list mode. Object keys are returned in alphabetical order, starting with key after the marker in order. |
| **max_keys**  integer | Max number of results to return in list mode, set this if you want to retrieve fewer than the default 1000 keys.  Default: `1000` |
| **metadata**  dictionary | Metadata for PUT/COPY operation, as a dictionary of `key=value` and `key=value,key=value`. |
| **mode**  string / required | Switches the module behaviour between  `PUT`: upload  `GET`: download  `geturl`: return download URL  `getstr`: download object as string  `list`: list keys  `create`: create bucket  `delete`: delete bucket  `delobj`: delete object  `copy`: copy object that is already stored in another bucket  Choices:   - `"get"` - `"put"` - `"delete"` - `"create"` - `"geturl"` - `"getstr"` - `"delobj"` - `"list"` - `"copy"` |
| **object**  string | Keyname of the object inside the bucket. Can be used to create “virtual directories”, see examples. |
| **overwrite**  aliases: force  string | Force overwrite either locally on the filesystem or remotely with the object/key. Used with `PUT` and `GET` operations.  Must be a Boolean, `always`, `never`, `different` or `latest`.  `true` is the same as `always`.  `false` is equal to `never`.  When this is set to `different` the MD5 sum of the local file is compared with the ‘ETag’ of the object/key in S3. The ETag may or may not be an MD5 digest of the object data. See the ETag response header here <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonResponseHeaders.html>.  (`GET` mode only) When this is set to `latest` the last modified timestamp of local file is compared with the ‘LastModified’ of the object/key in S3.  Default: `"always"` |
| **permission**  list / elements=string | This option lets the user set the canned permissions on the object/bucket that are created. The permissions that can be set are `private`, `public-read`, `public-read-write`, `authenticated-read` for a bucket or `private`, `public-read`, `public-read-write`, `aws-exec-read`, `authenticated-read`, `bucket-owner-read`, `bucket-owner-full-control` for an object. Multiple permissions can be specified as a list; although only the first one will be used during the initial upload of the file  Default: `["private"]` |
| **prefix**  string | Limits the response to keys that begin with the specified prefix for list mode.  Default: `""` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean  added in amazon.aws 2.0.0 | Whether or not to remove tags assigned to the S3 object if not specified in the playbook.  To remove all tags set *tags* to an empty dictionary in conjunction with this.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **retries**  aliases: retry  integer | On recoverable failure, how many times to retry before actually failing.  Default: `0` |
| **rgw**  boolean | Enable Ceph RGW S3 support. This option requires an explicit url via *s3_url*.  Choices:   - `false` ← (default) - `true` |
| **s3_url**  aliases: S3_URL  string | S3 URL endpoint for usage with Ceph, Eucalyptus and fakes3 etc. Otherwise assumes AWS. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **src**  path | The source file path when performing a `PUT` operation.  Either *content*, *content_base64* or *src* must be specified for a `PUT` operation. Ignored otherwise. |
| **tags**  dictionary  added in amazon.aws 2.0.0 | Tags dict to apply to the S3 object. |
| **validate_bucket_name**  boolean  added in amazon.aws 3.1.0 | Whether the bucket name should be validated to conform to AWS S3 naming rules.  On by default, this may be disabled for S3 backends that do not enforce these rules.  See <https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html>  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **version**  string | Version ID of the object inside the bucket. Can be used to get a specific version of a file if versioning is enabled in the target bucket. |

## [Notes](aws_s3_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_s3_module.md#id5)

```yaml+jinja
- name: Simple PUT operation
  amazon.aws.aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    src: /usr/local/myfile.txt
    mode: put

- name: PUT operation from a rendered template
  amazon.aws.aws_s3:
    bucket: mybucket
    object: /object.yaml
    content: "{{ lookup('template', 'templates/object.yaml.j2') }}"
    mode: put

- name: Simple PUT operation in Ceph RGW S3
  amazon.aws.aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    src: /usr/local/myfile.txt
    mode: put
    rgw: true
    s3_url: "http://localhost:8000"

- name: Simple GET operation
  amazon.aws.aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    dest: /usr/local/myfile.txt
    mode: get

- name: Get a specific version of an object.
  amazon.aws.aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    version: 48c9ee5131af7a716edc22df9772aa6f
    dest: /usr/local/myfile.txt
    mode: get

- name: PUT/upload with metadata
  amazon.aws.aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    src: /usr/local/myfile.txt
    mode: put
    metadata: 'Content-Encoding=gzip,Cache-Control=no-cache'

- name: PUT/upload with custom headers
  amazon.aws.aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    src: /usr/local/myfile.txt
    mode: put
    headers: 'x-amz-grant-full-control=emailAddress=owner@example.com'

- name: List keys simple
  amazon.aws.aws_s3:
    bucket: mybucket
    mode: list

- name: List keys all options
  amazon.aws.aws_s3:
    bucket: mybucket
    mode: list
    prefix: /my/desired/
    marker: /my/desired/0023.txt
    max_keys: 472

- name: Create an empty bucket
  amazon.aws.aws_s3:
    bucket: mybucket
    mode: create
    permission: public-read

- name: Create a bucket with key as directory, in the EU region
  amazon.aws.aws_s3:
    bucket: mybucket
    object: /my/directory/path
    mode: create
    region: eu-west-1

- name: Delete a bucket and all contents
  amazon.aws.aws_s3:
    bucket: mybucket
    mode: delete

- name: GET an object but don't download if the file checksums match. New in 2.0
  amazon.aws.aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    dest: /usr/local/myfile.txt
    mode: get
    overwrite: different

- name: Delete an object from a bucket
  amazon.aws.aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    mode: delobj

- name: Copy an object already stored in another bucket
  amazon.aws.aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    mode: copy
    copy_src:
        bucket: srcbucket
        object: /source/key.txt
```

## [Return Values](aws_s3_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **contents**  string | Contents of the object as string.  Returned: (for getstr operation)  Sample: `"Hello, world!"` |
| **expiry**  integer | Number of seconds the presigned url is valid for.  Returned: (for geturl operation)  Sample: `600` |
| **msg**  string | Message indicating the status of the operation.  Returned: always  Sample: `"PUT operation complete"` |
| **s3_keys**  list / elements=string | List of object keys.  Returned: (for list operation)  Sample: `["prefix1/", "prefix1/key1", "prefix1/key2"]` |
| **url**  string | URL of the object.  Returned: (for put and geturl operations)  Sample: `"https://my-bucket.s3.amazonaws.com/my-key.txt?AWSAccessKeyId=<access-key>&Expires=1506888865&Signature=<signature>"` |

### Authors

- Lester Wade (@lwade)
- Sloane Hertel (@s-hertel)
- Alina Buzachis (@linabuzachis)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
