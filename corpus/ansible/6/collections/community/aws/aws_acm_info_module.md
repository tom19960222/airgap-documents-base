---
collection: ansible
version: "6"
title: "community.aws.aws_acm_info module – Retrieve certificate information from AWS Certificate Manager service"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_acm_info_module.html
fetched_at: 2026-07-27T17:03:10+00:00
---
# community.aws.aws_acm_info module – Retrieve certificate information from AWS Certificate Manager service

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
> see [Requirements](aws_acm_info_module.md#ansible-collections-community-aws-aws-acm-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_acm_info`.

New in community.aws 1.0.0

- [Synopsis](aws_acm_info_module.md#synopsis)
- [Requirements](aws_acm_info_module.md#requirements)
- [Parameters](aws_acm_info_module.md#parameters)
- [Notes](aws_acm_info_module.md#notes)
- [Examples](aws_acm_info_module.md#examples)
- [Return Values](aws_acm_info_module.md#return-values)

## [Synopsis](aws_acm_info_module.md#id1)

- Retrieve information for ACM certificates
- Note that this will not return information about uploaded keys of size 4096 bits, due to a limitation of the ACM API.

## [Requirements](aws_acm_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_acm_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **certificate_arn**  aliases: arn  string | If provided, the results will be filtered to show only the certificate with this ARN.  If no certificate with this ARN exists, this task will fail.  If a certificate with this ARN exists in a different region, this task will fail |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **domain_name**  aliases: name  string | The domain name of an ACM certificate to limit the search to |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **statuses**  list / elements=string | Status to filter the certificate results  Choices:   - `"PENDING_VALIDATION"` - `"ISSUED"` - `"INACTIVE"` - `"EXPIRED"` - `"VALIDATION_TIMED_OUT"` - `"REVOKED"` - `"FAILED"` |
| **tags**  dictionary | Filter results to show only certificates with tags that match all the tags specified here. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](aws_acm_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_acm_info_module.md#id5)

```yaml+jinja
- name: obtain all ACM certificates
  community.aws.aws_acm_info:

- name: obtain all information for a single ACM certificate
  community.aws.aws_acm_info:
    domain_name: "*.example_com"

- name: obtain all certificates pending validation
  community.aws.aws_acm_info:
    statuses:
    - PENDING_VALIDATION

- name: obtain all certificates with tag Name=foo and myTag=bar
  community.aws.aws_acm_info:
    tags:
      Name: foo
      myTag: bar

# The output is still a list of certificates, just one item long.
- name: obtain information about a certificate with a particular ARN
  community.aws.aws_acm_info:
    certificate_arn:  "arn:aws:acm:ap-southeast-2:123456789876:certificate/abcdeabc-abcd-1234-4321-abcdeabcde12"
```

## [Return Values](aws_acm_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **certificates**  complex | A list of certificates  Returned: always |
| **certificate**  string | The ACM Certificate body  Returned: when certificate creation is complete  Sample: `"-----BEGIN CERTIFICATE-----\\\\nMII.....-----END CERTIFICATE-----\\\\n"` |
| **certificate_arn**  string | Certificate ARN  Returned: always  Sample: `"arn:aws:acm:ap-southeast-2:123456789012:certificate/abcd1234-abcd-1234-abcd-123456789abc"` |
| **certificate_chain**  string | Full certificate chain for the certificate  Returned: when certificate creation is complete  Sample: `"-----BEGIN CERTIFICATE-----\\\\nMII...\\\\n-----END CERTIFICATE-----\\\\n-----BEGIN CERTIFICATE-----\\\\n..."` |
| **created_at**  string | Date certificate was created  Returned: always  Sample: `"2017-08-15T10:31:19+10:00"` |
| **domain_name**  string | Domain name for the certificate  Returned: always  Sample: `"*.example.com"` |
| **domain_validation_options**  complex | Options used by ACM to validate the certificate  Returned: when certificate type is AMAZON_ISSUED |
| **domain_name**  string | Fully qualified domain name of the certificate  Returned: always  Sample: `"example.com"` |
| **validation_domain**  string | The domain name ACM used to send validation emails  Returned: always  Sample: `"example.com"` |
| **validation_emails**  list / elements=string | A list of email addresses that ACM used to send domain validation emails  Returned: always  Sample: `["admin@example.com", "postmaster@example.com"]` |
| **validation_status**  string | Validation status of the domain  Returned: always  Sample: `"SUCCESS"` |
| **failure_reason**  string | Reason certificate request failed  Returned: only when certificate issuing failed  Sample: `"NO_AVAILABLE_CONTACTS"` |
| **in_use_by**  list / elements=string | A list of ARNs for the AWS resources that are using the certificate.  Returned: always  Sample: `[]` |
| **issued_at**  string | Date certificate was issued  Returned: always  Sample: `"2017-01-01T00:00:00+10:00"` |
| **issuer**  string | Issuer of the certificate  Returned: always  Sample: `"Amazon"` |
| **key_algorithm**  string | Algorithm used to generate the certificate  Returned: always  Sample: `"RSA-2048"` |
| **not_after**  string | Date after which the certificate is not valid  Returned: always  Sample: `"2019-01-01T00:00:00+10:00"` |
| **not_before**  string | Date before which the certificate is not valid  Returned: always  Sample: `"2017-01-01T00:00:00+10:00"` |
| **renewal_summary**  complex | Information about managed renewal process  Returned: when certificate is issued by Amazon and a renewal has been started |
| **domain_validation_options**  complex | Options used by ACM to validate the certificate  Returned: when certificate type is AMAZON_ISSUED |
| **domain_name**  string | Fully qualified domain name of the certificate  Returned: always  Sample: `"example.com"` |
| **validation_domain**  string | The domain name ACM used to send validation emails  Returned: always  Sample: `"example.com"` |
| **validation_emails**  list / elements=string | A list of email addresses that ACM used to send domain validation emails  Returned: always  Sample: `["admin@example.com", "postmaster@example.com"]` |
| **validation_status**  string | Validation status of the domain  Returned: always  Sample: `"SUCCESS"` |
| **renewal_status**  string | Status of the domain renewal  Returned: always  Sample: `"PENDING_AUTO_RENEWAL"` |
| **revocation_reason**  string | Reason for certificate revocation  Returned: when the certificate has been revoked  Sample: `"SUPERCEDED"` |
| **revoked_at**  string | Date certificate was revoked  Returned: when the certificate has been revoked  Sample: `"2017-09-01T10:00:00+10:00"` |
| **serial**  string | The serial number of the certificate  Returned: always  Sample: `"00:01:02:03:04:05:06:07:08:09:0a:0b:0c:0d:0e:0f"` |
| **signature_algorithm**  string | Algorithm used to sign the certificate  Returned: always  Sample: `"SHA256WITHRSA"` |
| **status**  string | Status of the certificate in ACM  Returned: always  Sample: `"ISSUED"` |
| **subject**  string | The name of the entity that is associated with the public key contained in the certificate  Returned: always  Sample: `"CN=*.example.com"` |
| **subject_alternative_names**  list / elements=string | Subject Alternative Names for the certificate  Returned: always  Sample: `["*.example.com"]` |
| **tags**  dictionary | Tags associated with the certificate  Returned: always  Sample: `{"Application": "helloworld", "Environment": "test"}` |
| **type**  string | The source of the certificate  Returned: always  Sample: `"AMAZON_ISSUED"` |

### Authors

- Will Thames (@willthames)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
