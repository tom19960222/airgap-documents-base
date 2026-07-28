---
collection: ansible
version: "8"
title: "community.aws.acm_certificate_info module – Retrieve certificate information from AWS Certificate Manager service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/acm_certificate_info_module.html
fetched_at: 2026-07-28T01:40:04+00:00
---
# community.aws.acm_certificate_info module – Retrieve certificate information from AWS Certificate Manager service

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
> see [Requirements](acm_certificate_info_module.md#ansible-collections-community-aws-acm-certificate-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.acm_certificate_info`.

New in community.aws 1.0.0

- [Synopsis](acm_certificate_info_module.md#synopsis)
- [Requirements](acm_certificate_info_module.md#requirements)
- [Parameters](acm_certificate_info_module.md#parameters)
- [Notes](acm_certificate_info_module.md#notes)
- [Examples](acm_certificate_info_module.md#examples)
- [Return Values](acm_certificate_info_module.md#return-values)

## [Synopsis](acm_certificate_info_module.md#id1)

- Retrieve information for ACM certificates.
- Note that this will not return information about uploaded keys of size 4096 bits, due to a limitation of the ACM API.
- Prior to release 5.0.0 this module was called `community.aws.aws_acm_info`. The usage did not change.

Aliases: aws_acm_info

## [Requirements](acm_certificate_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](acm_certificate_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **certificate_arn**  aliases: arn  string | If provided, the results will be filtered to show only the certificate with this ARN.  If no certificate with this ARN exists, this task will fail.  If a certificate with this ARN exists in a different region, this task will fail. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **domain_name**  aliases: name  string | The domain name of an ACM certificate to limit the search to. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **statuses**  list / elements=string | Status to filter the certificate results.  **Choices:**   - `"PENDING_VALIDATION"` - `"ISSUED"` - `"INACTIVE"` - `"EXPIRED"` - `"VALIDATION_TIMED_OUT"` - `"REVOKED"` - `"FAILED"` |
| **tags**  dictionary | Filter results to show only certificates with tags that match all the tags specified here. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](acm_certificate_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](acm_certificate_info_module.md#id5)

```yaml+jinja
- name: obtain all ACM certificates
  community.aws.acm_certificate_info:

- name: obtain all information for a single ACM certificate
  community.aws.acm_certificate_info:
    domain_name: "*.example_com"

- name: obtain all certificates pending validation
  community.aws.acm_certificate_info:
    statuses:
    - PENDING_VALIDATION

- name: obtain all certificates with tag Name=foo and myTag=bar
  community.aws.acm_certificate_info:
    tags:
      Name: foo
      myTag: bar

# The output is still a list of certificates, just one item long.
- name: obtain information about a certificate with a particular ARN
  community.aws.acm_certificate_info:
    certificate_arn:  "arn:aws:acm:ap-southeast-2:123456789012:certificate/abcdeabc-abcd-1234-4321-abcdeabcde12"
```

## [Return Values](acm_certificate_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **certificates**  complex | A list of certificates  **Returned:** always |
| **certificate**  string | The ACM Certificate body  **Returned:** when certificate creation is complete  **Sample:** `"-----BEGIN CERTIFICATE-----\\\\nMII.....-----END CERTIFICATE-----\\\\n"` |
| **certificate_arn**  string | Certificate ARN  **Returned:** always  **Sample:** `"arn:aws:acm:ap-southeast-2:123456789012:certificate/abcd1234-abcd-1234-abcd-123456789abc"` |
| **certificate_chain**  string | Full certificate chain for the certificate  **Returned:** when certificate creation is complete  **Sample:** `"-----BEGIN CERTIFICATE-----\\\\nMII...\\\\n-----END CERTIFICATE-----\\\\n-----BEGIN CERTIFICATE-----\\\\n..."` |
| **created_at**  string | Date certificate was created  **Returned:** always  **Sample:** `"2017-08-15T10:31:19+10:00"` |
| **domain_name**  string | Domain name for the certificate  **Returned:** always  **Sample:** `"*.example.com"` |
| **domain_validation_options**  complex | Options used by ACM to validate the certificate  **Returned:** when certificate type is AMAZON_ISSUED |
| **domain_name**  string | Fully qualified domain name of the certificate  **Returned:** always  **Sample:** `"example.com"` |
| **validation_domain**  string | The domain name ACM used to send validation emails  **Returned:** always  **Sample:** `"example.com"` |
| **validation_emails**  list / elements=string | A list of email addresses that ACM used to send domain validation emails  **Returned:** always  **Sample:** `["admin@example.com", "postmaster@example.com"]` |
| **validation_status**  string | Validation status of the domain  **Returned:** always  **Sample:** `"SUCCESS"` |
| **failure_reason**  string | Reason certificate request failed  **Returned:** only when certificate issuing failed  **Sample:** `"NO_AVAILABLE_CONTACTS"` |
| **in_use_by**  list / elements=string | A list of ARNs for the AWS resources that are using the certificate.  **Returned:** always  **Sample:** `[]` |
| **issued_at**  string | Date certificate was issued  **Returned:** always  **Sample:** `"2017-01-01T00:00:00+10:00"` |
| **issuer**  string | Issuer of the certificate  **Returned:** always  **Sample:** `"Amazon"` |
| **key_algorithm**  string | Algorithm used to generate the certificate  **Returned:** always  **Sample:** `"RSA-2048"` |
| **not_after**  string | Date after which the certificate is not valid  **Returned:** always  **Sample:** `"2019-01-01T00:00:00+10:00"` |
| **not_before**  string | Date before which the certificate is not valid  **Returned:** always  **Sample:** `"2017-01-01T00:00:00+10:00"` |
| **renewal_summary**  complex | Information about managed renewal process  **Returned:** when certificate is issued by Amazon and a renewal has been started |
| **domain_validation_options**  complex | Options used by ACM to validate the certificate  **Returned:** when certificate type is AMAZON_ISSUED |
| **domain_name**  string | Fully qualified domain name of the certificate  **Returned:** always  **Sample:** `"example.com"` |
| **validation_domain**  string | The domain name ACM used to send validation emails  **Returned:** always  **Sample:** `"example.com"` |
| **validation_emails**  list / elements=string | A list of email addresses that ACM used to send domain validation emails  **Returned:** always  **Sample:** `["admin@example.com", "postmaster@example.com"]` |
| **validation_status**  string | Validation status of the domain  **Returned:** always  **Sample:** `"SUCCESS"` |
| **renewal_status**  string | Status of the domain renewal  **Returned:** always  **Sample:** `"PENDING_AUTO_RENEWAL"` |
| **revocation_reason**  string | Reason for certificate revocation  **Returned:** when the certificate has been revoked  **Sample:** `"SUPERCEDED"` |
| **revoked_at**  string | Date certificate was revoked  **Returned:** when the certificate has been revoked  **Sample:** `"2017-09-01T10:00:00+10:00"` |
| **serial**  string | The serial number of the certificate  **Returned:** always  **Sample:** `"00:01:02:03:04:05:06:07:08:09:0a:0b:0c:0d:0e:0f"` |
| **signature_algorithm**  string | Algorithm used to sign the certificate  **Returned:** always  **Sample:** `"SHA256WITHRSA"` |
| **status**  string | Status of the certificate in ACM  **Returned:** always  **Sample:** `"ISSUED"` |
| **subject**  string | The name of the entity that is associated with the public key contained in the certificate  **Returned:** always  **Sample:** `"CN=*.example.com"` |
| **subject_alternative_names**  list / elements=string | Subject Alternative Names for the certificate  **Returned:** always  **Sample:** `["*.example.com"]` |
| **tags**  dictionary | Tags associated with the certificate  **Returned:** always  **Sample:** `{"Application": "helloworld", "Environment": "test"}` |
| **type**  string | The source of the certificate  **Returned:** always  **Sample:** `"AMAZON_ISSUED"` |

### Authors

- Will Thames (@willthames)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
