---
collection: ansible
version: "8"
title: "community.aws.acm_certificate module – Upload and delete certificates in the AWS Certificate Manager service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/acm_certificate_module.html
fetched_at: 2026-07-28T01:40:03+00:00
---
# community.aws.acm_certificate module – Upload and delete certificates in the AWS Certificate Manager service

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
> see [Requirements](acm_certificate_module.md#ansible-collections-community-aws-acm-certificate-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.acm_certificate`.

New in community.aws 1.0.0

- [Synopsis](acm_certificate_module.md#synopsis)
- [Requirements](acm_certificate_module.md#requirements)
- [Parameters](acm_certificate_module.md#parameters)
- [Notes](acm_certificate_module.md#notes)
- [Examples](acm_certificate_module.md#examples)
- [Return Values](acm_certificate_module.md#return-values)

## [Synopsis](acm_certificate_module.md#id1)

- Import and delete certificates in Amazon Web Service’s Certificate Manager (AWS ACM).
- This module does not currently interact with AWS-provided certificates. It currently only manages certificates provided to AWS by the user.
- The ACM API allows users to upload multiple certificates for the same domain name, and even multiple identical certificates. This module attempts to restrict such freedoms, to be idempotent, as per the Ansible philosophy. It does this through applying AWS resource “Name” tags to ACM certificates.
- When *state=present*, if there is one certificate in ACM with a `Name` tag equal to the *name_tag* parameter, and an identical body and chain, this task will succeed without effect.
- When *state=present*, if there is one certificate in ACM a *Name* tag equal to the *name_tag* parameter, and a different body, this task will overwrite that certificate.
- When *state=present*, if there are multiple certificates in ACM with a *Name* tag equal to the *name_tag* parameter, this task will fail.
- When *state=absent* and *certificate_arn* is defined, this module will delete the ACM resource with that ARN if it exists in this region, and succeed without effect if it doesn’t exist.
- When *state=absent* and *domain_name* is defined, this module will delete all ACM resources in this AWS region with a corresponding domain name. If there are none, it will succeed without effect.
- When *state=absent* and *certificate_arn* is not defined, and *domain_name* is not defined, this module will delete all ACM resources in this AWS region with a corresponding *Name* tag. If there are none, it will succeed without effect.
- Note that this may not work properly with keys of size 4096 bits, due to a limitation of the ACM API.
- Prior to release 5.0.0 this module was called `community.aws.aws_acm`. The usage did not change.

Aliases: aws_acm

## [Requirements](acm_certificate_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](acm_certificate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **certificate**  string | The body of the PEM encoded public certificate.  Required when *state* is not `absent` and the certificate does not exist.  If your certificate is in a file, use `lookup('file', 'path/to/cert.pem'`). |
| **certificate_arn**  aliases: arn  string | The ARN of a certificate in ACM to modify or delete.  If *state=present*, the certificate with the specified ARN can be updated. For example, this can be used to add/remove tags to an existing certificate.  If *state=absent*, you must provide one of *certificate_arn*, *domain_name* or *name_tag*.  If *state=absent* and no resource exists with this ARN in this region, the task will succeed with no effect.  If *state=absent* and the corresponding resource exists in a different region, this task may report success without deleting that resource. |
| **certificate_chain**  string | The body of the PEM encoded chain for your certificate.  If your certificate chain is in a file, use `lookup('file', 'path/to/chain.pem'`).  Ignored when *state=absent* |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **domain_name**  aliases: domain  string | The domain name of the certificate.  If *state=absent* and *domain_name* is specified, this task will delete all ACM certificates with this domain.  Exactly one of *domain_name*, *name_tag* and *certificate_arn* must be provided.  If *state=present* this must not be specified. (Since the domain name is encoded within the public certificate’s body.) |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **name_tag**  aliases: name  string | The unique identifier for tagging resources using AWS tags, with key *Name*.  This can be any set of characters accepted by AWS for tag values.  This is to ensure Ansible can treat certificates idempotently, even though the ACM API allows duplicate certificates.  If *state=preset*, this must be specified.  If *state=absent* and *name_tag* is specified, this task will delete all ACM certificates with this Name tag.  If *state=absent*, you must provide exactly one of *certificate_arn*, *domain_name* or *name_tag*.  If both *name_tag* and the ‘Name’ tag in *tags* are set, the values must be the same.  If the ‘Name’ tag in *tags* is not set and *name_tag* is set, the *name_tag* value is copied to *tags*. |
| **private_key**  string | The body of the PEM encoded private key.  Required when *state=present* and the certificate does not exist.  Ignored when *state=absent*.  If your private key is in a file, use `lookup('file', 'path/to/key.pem'`). |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | If *state=present*, the specified public certificate and private key will be uploaded, with *Name* tag equal to *name_tag*.  If *state=absent*, any certificates in this region with a corresponding *domain_name*, *name_tag* or *certificate_arn* will be deleted.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](acm_certificate_module.md#id4)

> **Note:**
>
> - Support for *tags* and *purge_tags* was added in release 3.2.0
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](acm_certificate_module.md#id5)

```yaml+jinja
- name: upload a self-signed certificate
  community.aws.acm_certificate:
    certificate: "{{ lookup('file', 'cert.pem' ) }}"
    privateKey: "{{ lookup('file', 'key.pem' ) }}"
    name_tag: my_cert # to be applied through an AWS tag as  "Name":"my_cert"
    region: ap-southeast-2 # AWS region

- name: create/update a certificate with a chain
  community.aws.acm_certificate:
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
  community.aws.acm_certificate:
    name_tag: my_cert
    state: absent
    region: ap-southeast-2

- name: delete a certificate with a particular ARN
  community.aws.acm_certificate:
    certificate_arn: "arn:aws:acm:ap-southeast-2:123456789012:certificate/01234567-abcd-abcd-abcd-012345678901"
    state: absent
    region: ap-southeast-2

- name: delete all certificates with a particular domain name
  community.aws.acm_certificate:
    domain_name: acm.ansible.com
    state: absent
    region: ap-southeast-2

- name: add tags to an existing certificate with a particular ARN
  community.aws.acm_certificate:
    certificate_arn: "arn:aws:acm:ap-southeast-2:123456789012:certificate/01234567-abcd-abcd-abcd-012345678901"
    tags:
      Name: my_certificate
      Application: search
      Environment: development
    purge_tags: true
```

## [Return Values](acm_certificate_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **arns**  list / elements=string | A list of the ARNs of the certificates in ACM which were deleted  **Returned:** when *state=absent*  **Sample:** `["arn:aws:acm:ap-southeast-2:123456789012:certificate/01234567-abcd-abcd-abcd-012345678901"]` |
| **certificate**  complex | Information about the certificate which was uploaded  **Returned:** when *state=present* |
| **arn**  string | The ARN of the certificate in ACM  **Returned:** when *state=present* and not in check mode  **Sample:** `"arn:aws:acm:ap-southeast-2:123456789012:certificate/01234567-abcd-abcd-abcd-012345678901"` |
| **domain_name**  string | The domain name encoded within the public certificate  **Returned:** when *state=present*  **Sample:** `"acm.ansible.com"` |

### Authors

- Matthew Davis (@matt-telstra) on behalf of Telstra Corporation Limited

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
