---
collection: ansible
version: "6"
title: "community.aws.aws_acm module – Upload and delete certificates in the AWS Certificate Manager service"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_acm_module.html
fetched_at: 2026-07-27T17:03:09+00:00
---
# community.aws.aws_acm module – Upload and delete certificates in the AWS Certificate Manager service

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
> see [Requirements](aws_acm_module.md#ansible-collections-community-aws-aws-acm-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_acm`.

New in community.aws 1.0.0

- [Synopsis](aws_acm_module.md#synopsis)
- [Requirements](aws_acm_module.md#requirements)
- [Parameters](aws_acm_module.md#parameters)
- [Notes](aws_acm_module.md#notes)
- [Examples](aws_acm_module.md#examples)
- [Return Values](aws_acm_module.md#return-values)

## [Synopsis](aws_acm_module.md#id1)

- Import and delete certificates in Amazon Web Service’s Certificate Manager (AWS ACM).
- This module does not currently interact with AWS-provided certificates. It currently only manages certificates provided to AWS by the user.
- The ACM API allows users to upload multiple certificates for the same domain name, and even multiple identical certificates. This module attempts to restrict such freedoms, to be idempotent, as per the Ansible philosophy. It does this through applying AWS resource “Name” tags to ACM certificates.
- When *state=present*, if there is one certificate in ACM with a `Name` tag equal to the `name_tag` parameter, and an identical body and chain, this task will succeed without effect.
- When *state=present*, if there is one certificate in ACM a *Name* tag equal to the *name_tag* parameter, and a different body, this task will overwrite that certificate.
- When *state=present*, if there are multiple certificates in ACM with a *Name* tag equal to the *name_tag* parameter, this task will fail.
- When *state=absent* and *certificate_arn* is defined, this module will delete the ACM resource with that ARN if it exists in this region, and succeed without effect if it doesn’t exist.
- When *state=absent* and *domain_name* is defined, this module will delete all ACM resources in this AWS region with a corresponding domain name. If there are none, it will succeed without effect.
- When *state=absent* and *certificate_arn* is not defined, and *domain_name* is not defined, this module will delete all ACM resources in this AWS region with a corresponding *Name* tag. If there are none, it will succeed without effect.
- Note that this may not work properly with keys of size 4096 bits, due to a limitation of the ACM API.

## [Requirements](aws_acm_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_acm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **certificate**  string | The body of the PEM encoded public certificate.  Required when *state* is not `absent` and the certificate does not exist.  If your certificate is in a file, use `lookup('file', 'path/to/cert.pem'`). |
| **certificate_arn**  aliases: arn  string | The ARN of a certificate in ACM to modify or delete.  If *state=present*, the certificate with the specified ARN can be updated. For example, this can be used to add/remove tags to an existing certificate.  If *state=absent*, you must provide one of *certificate_arn*, *domain_name* or *name_tag*.  If *state=absent* and no resource exists with this ARN in this region, the task will succeed with no effect.  If *state=absent* and the corresponding resource exists in a different region, this task may report success without deleting that resource. |
| **certificate_chain**  string | The body of the PEM encoded chain for your certificate.  If your certificate chain is in a file, use `lookup('file', 'path/to/chain.pem'`).  Ignored when *state=absent* |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **domain_name**  aliases: domain  string | The domain name of the certificate.  If *state=absent* and *domain_name* is specified, this task will delete all ACM certificates with this domain.  Exactly one of *domain_name*, *name_tag* and *certificate_arn* must be provided.  If *state=present* this must not be specified. (Since the domain name is encoded within the public certificate’s body.) |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **name_tag**  aliases: name  string | The unique identifier for tagging resources using AWS tags, with key *Name*.  This can be any set of characters accepted by AWS for tag values.  This is to ensure Ansible can treat certificates idempotently, even though the ACM API allows duplicate certificates.  If *state=preset*, this must be specified.  If *state=absent* and *name_tag* is specified, this task will delete all ACM certificates with this Name tag.  If *state=absent*, you must provide exactly one of *certificate_arn*, *domain_name* or *name_tag*. |
| **private_key**  string | The body of the PEM encoded private key.  Required when *state=present* and the certificate does not exist.  Ignored when *state=absent*.  If your private key is in a file, use `lookup('file', 'path/to/key.pem'`). |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean  added in community.aws 3.2.0 | whether to remove tags not present in the `tags` parameter.  Choices:   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | If *state=present*, the specified public certificate and private key will be uploaded, with *Name* tag equal to *name_tag*.  If *state=absent*, any certificates in this region with a corresponding *domain_name*, *name_tag* or *certificate_arn* will be deleted.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary  added in community.aws 3.2.0 | Tags to apply to certificates imported in ACM.  If both *name_tag* and the ‘Name’ tag in *tags* are set, the values must be the same.  If the ‘Name’ tag in *tags* is not set and *name_tag* is set, the *name_tag* value is copied to *tags*. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](aws_acm_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_acm_module.md#id5)

```yaml+jinja
- name: upload a self-signed certificate
  community.aws.aws_acm:
    certificate: "{{ lookup('file', 'cert.pem' ) }}"
    privateKey: "{{ lookup('file', 'key.pem' ) }}"
    name_tag: my_cert # to be applied through an AWS tag as  "Name":"my_cert"
    region: ap-southeast-2 # AWS region

- name: create/update a certificate with a chain
  community.aws.aws_acm:
    certificate: "{{ lookup('file', 'cert.pem' ) }}"
    private_key: "{{ lookup('file', 'key.pem' ) }}"
    name_tag: my_cert
    certificate_chain: "{{ lookup('file', 'chain.pem' ) }}"
    state: present
    region: ap-southeast-2
  register: cert_create

- name: print ARN of cert we just created
  ansible.builtin.debug:
    var: cert_create.certificate.arn

- name: delete the cert we just created
  community.aws.aws_acm:
    name_tag: my_cert
    state: absent
    region: ap-southeast-2

- name: delete a certificate with a particular ARN
  community.aws.aws_acm:
    certificate_arn: "arn:aws:acm:ap-southeast-2:123456789012:certificate/01234567-abcd-abcd-abcd-012345678901"
    state: absent
    region: ap-southeast-2

- name: delete all certificates with a particular domain name
  community.aws.aws_acm:
    domain_name: acm.ansible.com
    state: absent
    region: ap-southeast-2

- name: add tags to an existing certificate with a particular ARN
  community.aws.aws_acm:
    certificate_arn: "arn:aws:acm:ap-southeast-2:123456789012:certificate/01234567-abcd-abcd-abcd-012345678901"
    tags:
      Name: my_certificate
      Application: search
      Environment: development
    purge_tags: true
```

## [Return Values](aws_acm_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **arns**  list / elements=string | A list of the ARNs of the certificates in ACM which were deleted  Returned: when *state=absent*  Sample: `["arn:aws:acm:ap-southeast-2:123456789012:certificate/01234567-abcd-abcd-abcd-012345678901"]` |
| **certificate**  complex | Information about the certificate which was uploaded  Returned: when *state=present* |
| **arn**  string | The ARN of the certificate in ACM  Returned: when *state=present* and not in check mode  Sample: `"arn:aws:acm:ap-southeast-2:123456789012:certificate/01234567-abcd-abcd-abcd-012345678901"` |
| **domain_name**  string | The domain name encoded within the public certificate  Returned: when *state=present*  Sample: `"acm.ansible.com"` |

### Authors

- Matthew Davis (@matt-telstra) on behalf of Telstra Corporation Limited

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
