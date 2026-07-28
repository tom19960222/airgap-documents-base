---
collection: ansible
version: "6"
title: "community.aws.s3_sync module – Efficiently upload multiple files to S3"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/s3_sync_module.html
fetched_at: 2026-07-27T17:05:04+00:00
---
# community.aws.s3_sync module – Efficiently upload multiple files to S3

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
> see [Requirements](s3_sync_module.md#ansible-collections-community-aws-s3-sync-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.s3_sync`.

New in community.aws 1.0.0

- [Synopsis](s3_sync_module.md#synopsis)
- [Requirements](s3_sync_module.md#requirements)
- [Parameters](s3_sync_module.md#parameters)
- [Notes](s3_sync_module.md#notes)
- [Examples](s3_sync_module.md#examples)
- [Return Values](s3_sync_module.md#return-values)

## [Synopsis](s3_sync_module.md#id1)

- The S3 module is great, but it is very slow for a large volume of files- even a dozen will be noticeable. In addition to speed, it handles globbing, inclusions/exclusions, mime types, expiration mapping, recursion, cache control and smart directory mapping.

## [Requirements](s3_sync_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](s3_sync_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **bucket**  string / required | Bucket name. |
| **cache_control**  string | Cache-Control header set on uploaded objects.  Directives are separated by commas. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **delete**  boolean | Remove remote files that exist in bucket but are not present in the file root.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **exclude**  string | Shell pattern-style file matching.  Used after include to remove files (for instance, skip `"*.txt"`)  For multiple patterns, comma-separate them.  Default: `".*"` |
| **file_change_strategy**  string | Difference determination method to allow changes-only syncing. Unlike rsync, files are not patched- they are fully skipped or fully uploaded.  date_size will upload if file sizes don’t match or if local file modified date is newer than s3’s version  checksum will compare etag values based on s3’s implementation of chunked md5s.  force will always upload all files.  Choices:   - `"force"` - `"checksum"` - `"date_size"` ← (default) |
| **file_root**  path / required | File/directory path for synchronization. This is a local path.  This root path is scrubbed from the key name, so subdirectories will remain as keys. |
| **include**  string | Shell pattern-style file matching.  Used before exclude to determine eligible files (for instance, only `"*.gif"`)  For multiple patterns, comma-separate them.  Default: `"*"` |
| **key_prefix**  string | In addition to file path, prepend s3 path with this prefix. Module will add slash at end of prefix if necessary. |
| **mime_map**  dictionary | Dict entry from extension to MIME type. This will override any default/sniffed MIME type. For example `{".txt": "application/text", ".yml": "application/text"}` |
| **mode**  string | sync direction.  Choices:   - `"push"` ← (default) |
| **permission**  string | Canned ACL to apply to synced files.  Changing this ACL only changes newly synced files, it does not trigger a full reupload.  Choices:   - `"private"` - `"public-read"` - `"public-read-write"` - `"authenticated-read"` - `"aws-exec-read"` - `"bucket-owner-read"` - `"bucket-owner-full-control"` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **retries**  string | The *retries* option does nothing and will be removed after 2022-06-01 |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **storage_class**  string  added in community.aws 1.5.0 | Storage class to be associated to each object added to the S3 bucket.  Choices:   - `"STANDARD"` ← (default) - `"REDUCED_REDUNDANCY"` - `"STANDARD_IA"` - `"ONEZONE_IA"` - `"INTELLIGENT_TIERING"` - `"GLACIER"` - `"DEEP_ARCHIVE"` - `"OUTPOSTS"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](s3_sync_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](s3_sync_module.md#id5)

```yaml+jinja
- name: basic upload
  community.aws.s3_sync:
    bucket: tedder
    file_root: roles/s3/files/

- name: basic upload using the glacier storage class
  community.aws.s3_sync:
    bucket: tedder
    file_root: roles/s3/files/
    storage_class: GLACIER

- name: basic individual file upload
  community.aws.s3_sync:
    bucket: tedder
    file_root: roles/s3/files/file_name

- name: all the options
  community.aws.s3_sync:
    bucket: tedder
    file_root: roles/s3/files
    mime_map:
      .yml: application/text
      .json: application/text
    key_prefix: config_files/web
    file_change_strategy: force
    permission: public-read
    cache_control: "public, max-age=31536000"
    storage_class: "GLACIER"
    include: "*"
    exclude: "*.txt,.*"
```

## [Return Values](s3_sync_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **filelist_actionable**  list / elements=string | file listing (dicts) of files that will be uploaded after the strategy decision  Returned: always  Sample: `[{"bytes": 151, "chopped_path": "policy.json", "fullpath": "roles/cf/files/policy.json", "mime_type": "application/json", "modified_epoch": 1477931256, "s3_path": "s3sync/policy.json", "whysize": "151 / 151", "whytime": "1477931256 / 1477929260"}]` |
| **filelist_initial**  list / elements=string | file listing (dicts) from initial globbing  Returned: always  Sample: `[{"bytes": 151, "chopped_path": "policy.json", "fullpath": "roles/cf/files/policy.json", "modified_epoch": 1477416706}]` |
| **filelist_local_etag**  list / elements=string | file listing (dicts) including calculated local etag  Returned: always  Sample: `[{"bytes": 151, "chopped_path": "policy.json", "fullpath": "roles/cf/files/policy.json", "mime_type": "application/json", "modified_epoch": 1477416706, "s3_path": "s3sync/policy.json"}]` |
| **filelist_s3**  list / elements=string | file listing (dicts) including information about previously-uploaded versions  Returned: always  Sample: `[{"bytes": 151, "chopped_path": "policy.json", "fullpath": "roles/cf/files/policy.json", "mime_type": "application/json", "modified_epoch": 1477416706, "s3_path": "s3sync/policy.json"}]` |
| **filelist_typed**  list / elements=string | file listing (dicts) with calculated or overridden mime types  Returned: always  Sample: `[{"bytes": 151, "chopped_path": "policy.json", "fullpath": "roles/cf/files/policy.json", "mime_type": "application/json", "modified_epoch": 1477416706}]` |
| **uploads**  list / elements=string | file listing (dicts) of files that were actually uploaded  Returned: always  Sample: `[{"bytes": 151, "chopped_path": "policy.json", "fullpath": "roles/cf/files/policy.json", "s3_path": "s3sync/policy.json", "whysize": "151 / 151", "whytime": "1477931637 / 1477931489"}]` |

### Authors

- Ted Timmons (@tedder)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
