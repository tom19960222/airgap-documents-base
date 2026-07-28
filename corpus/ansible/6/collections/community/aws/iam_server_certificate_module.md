---
collection: ansible
version: "6"
title: "community.aws.iam_server_certificate module – Manage server certificates for use on ELBs and CloudFront"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/iam_server_certificate_module.html
fetched_at: 2026-07-27T17:04:41+00:00
---
# community.aws.iam_server_certificate module – Manage server certificates for use on ELBs and CloudFront

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
> see [Requirements](iam_server_certificate_module.md#ansible-collections-community-aws-iam-server-certificate-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.iam_server_certificate`.

New in community.aws 1.0.0

- [Synopsis](iam_server_certificate_module.md#synopsis)
- [Requirements](iam_server_certificate_module.md#requirements)
- [Parameters](iam_server_certificate_module.md#parameters)
- [Notes](iam_server_certificate_module.md#notes)
- [Examples](iam_server_certificate_module.md#examples)

## [Synopsis](iam_server_certificate_module.md#id1)

- Allows for the management of server certificates.

## [Requirements](iam_server_certificate_module.md#id2)

The below requirements are needed on the host that executes this module.

- boto >= 2.49.0
- boto3 >= 1.16.0
- botocore >= 1.19.0
- python >= 3.6

## [Parameters](iam_server_certificate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **cert**  string | The path to, or content of the certificate body in PEM encoded format.  If the parameter is not a file, it is assumed to be content.  Passing a file name is deprecated, and support will be dropped in version 5.0.0 of this collection. |
| **cert_chain**  string | The path to, or content of, the CA certificate chain in PEM encoded format.  If the parameter is not a file, it is assumed to be content.  Passing a file name is deprecated, and support will be dropped in version 5.0.0 of this collection. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **dup_ok**  boolean | By default the module will not upload a certificate that is already uploaded into AWS.  If *dup_ok=True*, it will upload the certificate as long as the name is unique.  Currently defaults to `false`, this will default to `true` in release 5.0.0.  Choices:   - `false` - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **key**  string | The path to, or content of the private key in PEM encoded format. If the parameter is not a file, it is assumed to be content.  Passing a file name is deprecated, and support will be dropped in version 5.0.0 of this collection. |
| **name**  string / required | Name of certificate to add, update or remove. |
| **new_name**  string | When *state=present*, this will update the name of the cert.  The *cert*, *key* and *cert_chain* parameters will be ignored if this is defined. |
| **new_path**  string | When *state=present*, this will update the path of the cert.  The *cert*, *key* and *cert_chain* parameters will be ignored if this is defined. |
| **path**  string | When creating or updating, specify the desired path of the certificate.  Default: `"/"` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string / required | Whether to create (or update) or delete the certificate.  If *new_path* or *new_name* is defined, specifying present will attempt to make an update these.  Choices:   - `"present"` - `"absent"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](iam_server_certificate_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](iam_server_certificate_module.md#id5)

```yaml+jinja
- name: Basic server certificate upload from local file
  community.aws.iam_server_certificate:
    name: very_ssl
    state: present
    cert: "{{ lookup('file', 'path/to/cert') }}"
    key: "{{ lookup('file', 'path/to/key') }}"
    cert_chain: "{{ lookup('file', 'path/to/certchain') }}"

- name: Basic server certificate upload
  community.aws.iam_server_certificate:
    name: very_ssl
    state: present
    cert: path/to/cert
    key: path/to/key
    cert_chain: path/to/certchain

- name: Server certificate upload using key string
  community.aws.iam_server_certificate:
    name: very_ssl
    state: present
    path: "/a/cert/path/"
    cert: body_of_somecert
    key: vault_body_of_privcertkey
    cert_chain: body_of_myverytrustedchain

- name: Basic rename of existing certificate
  community.aws.iam_server_certificate:
    name: very_ssl
    new_name: new_very_ssl
    state: present
```

### Authors

- Jonathan I. Davila (@defionscode)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
