---
collection: ansible
version: "6"
title: "community.crypto.ecs_domain module – Request validation of a domain with the Entrust Certificate Services (ECS) API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/crypto/ecs_domain_module.html
fetched_at: 2026-07-27T17:06:16+00:00
---
# community.crypto.ecs_domain module – Request validation of a domain with the Entrust Certificate Services (ECS) API

> **Note:**
>
> This module is part of the [community.crypto collection](https://galaxy.ansible.com/community/crypto) (version 2.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.crypto`.
> You need further requirements to be able to use this module,
> see [Requirements](ecs_domain_module.md#ansible-collections-community-crypto-ecs-domain-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.ecs_domain`.

New in community.crypto 1.0.0

- [Synopsis](ecs_domain_module.md#synopsis)
- [Requirements](ecs_domain_module.md#requirements)
- [Parameters](ecs_domain_module.md#parameters)
- [Attributes](ecs_domain_module.md#attributes)
- [Notes](ecs_domain_module.md#notes)
- [See Also](ecs_domain_module.md#see-also)
- [Examples](ecs_domain_module.md#examples)
- [Return Values](ecs_domain_module.md#return-values)

## [Synopsis](ecs_domain_module.md#id1)

- Request validation or re-validation of a domain with the Entrust Certificate Services (ECS) API.
- Requires credentials for the [Entrust Certificate Services](https://www.entrustdatacard.com/products/categories/ssl-certificates) (ECS) API.
- If the domain is already in the validation process, no new validation will be requested, but the validation data (if applicable) will be returned.
- If the domain is already in the validation process but the *verification_method* specified is different than the current *verification_method*, the *verification_method* will be updated and validation data (if applicable) will be returned.
- If the domain is an active, validated domain, the return value of *changed* will be false, unless `domain_status=EXPIRED`, in which case a re-validation will be performed.
- If `verification_method=dns`, details about the required DNS entry will be specified in the return parameters *dns_contents*, *dns_location*, and *dns_resource_type*.
- If `verification_method=web_server`, details about the required file details will be specified in the return parameters *file_contents* and *file_location*.
- If `verification_method=email`, the email address(es) that the validation email(s) were sent to will be in the return parameter *emails*. This is purely informational. For domains requested using this module, this will always be a list of size 1.

## [Requirements](ecs_domain_module.md#id2)

The below requirements are needed on the host that executes this module.

- PyYAML >= 3.11

## [Parameters](ecs_domain_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **client_id**  integer | The client ID to request the domain be associated with.  If no client ID is specified, the domain will be added under the primary client with ID of 1.  Default: `1` |
| **domain_name**  string / required | The domain name to be verified or reverified. |
| **entrust_api_client_cert_key_path**  path / required | The path to the key for the client certificate used to authenticate to the Entrust Certificate Services (ECS) API. |
| **entrust_api_client_cert_path**  path / required | The path to the client certificate used to authenticate to the Entrust Certificate Services (ECS) API. |
| **entrust_api_key**  string / required | The key (password) for authentication to the Entrust Certificate Services (ECS) API. |
| **entrust_api_specification_path**  path | The path to the specification file defining the Entrust Certificate Services (ECS) API configuration.  You can use this to keep a local copy of the specification to avoid downloading it every time the module is used.  Default: `"https://cloud.entrust.net/EntrustCloud/documentation/cms-api-2.1.0.yaml"` |
| **entrust_api_user**  string / required | The username for authentication to the Entrust Certificate Services (ECS) API. |
| **verification_email**  string | Email address to be used to verify domain ownership.  Email address must be either an email address present in the WHOIS data for *domain_name*, or one of the following constructed emails: admin@*domain_name*, administrator@*domain_name*, webmaster@*domain_name*, hostmaster@*domain_name*, postmaster@*domain_name*.  Note that if *domain_name* includes subdomains, the top level domain should be used. For example, if requesting validation of example1.ansible.com, or test.example2.ansible.com, and you want to use the “admin” preconstructed name, the email address should be [admin@ansible.com](mailto:admin%40ansible.com).  If using the email values from the WHOIS data for the domain or its top level namespace, they must be exact matches.  If `verification_method=email` but *verification_email* is not provided, the first email address found in WHOIS data for the domain will be used.  To verify domain ownership, domain owner must follow the instructions in the email they receive.  Only allowed if `verification_method=email` |
| **verification_method**  string / required | The verification method to be used to prove control of the domain.  If `verification_method=email` and the value *verification_email* is specified, that value is used for the email validation. If *verification_email* is not provided, the first value present in WHOIS data will be used. An email will be sent to the address in *verification_email* with instructions on how to verify control of the domain.  If `verification_method=dns`, the value *dns_contents* must be stored in location *dns_location*, with a DNS record type of *verification_dns_record_type*. To prove domain ownership, update your DNS records so the text string returned by *dns_contents* is available at *dns_location*.  If `verification_method=web_server`, the contents of return value *file_contents* must be made available on a web server accessible at location *file_location*.  If `verification_method=manual`, the domain will be validated with a manual process. This is not recommended.  Choices:   - `"dns"` - `"email"` - `"manual"` - `"web_server"` |

## [Attributes](ecs_domain_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: none | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](ecs_domain_module.md#id5)

> **Note:**
>
> - There is a small delay (typically about 5 seconds, but can be as long as 60 seconds) before obtaining the random values when requesting a validation while `verification_method=dns` or `verification_method=web_server`. Be aware of that if doing many domain validation requests.

## [See Also](ecs_domain_module.md#id6)

> **See also:**
>
> [community.crypto.x509_certificate](x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module)
> :   Can be used to request certificates from ECS, with `provider=entrust`.
>
> [community.crypto.ecs_certificate](ecs_certificate_module.md#ansible-collections-community-crypto-ecs-certificate-module)
> :   Can be used to request a Certificate from ECS using a verified domain.

## [Examples](ecs_domain_module.md#id7)

```yaml+jinja
- name: Request domain validation using email validation for client ID of 2.
  community.crypto.ecs_domain:
    domain_name: ansible.com
    client_id: 2
    verification_method: email
    verification_email: admin@ansible.com
    entrust_api_user: apiusername
    entrust_api_key: a^lv*32!cd9LnT
    entrust_api_client_cert_path: /etc/ssl/entrust/ecs-client.crt
    entrust_api_client_cert_key_path: /etc/ssl/entrust/ecs-client.key

- name: Request domain validation using DNS. If domain is already valid,
        request revalidation if expires within 90 days
  community.crypto.ecs_domain:
    domain_name: ansible.com
    verification_method: dns
    entrust_api_user: apiusername
    entrust_api_key: a^lv*32!cd9LnT
    entrust_api_client_cert_path: /etc/ssl/entrust/ecs-client.crt
    entrust_api_client_cert_key_path: /etc/ssl/entrust/ecs-client.key

- name: Request domain validation using web server validation, and revalidate
        if fewer than 60 days remaining of EV eligibility.
  community.crypto.ecs_domain:
    domain_name: ansible.com
    verification_method: web_server
    entrust_api_user: apiusername
    entrust_api_key: a^lv*32!cd9LnT
    entrust_api_client_cert_path: /etc/ssl/entrust/ecs-client.crt
    entrust_api_client_cert_key_path: /etc/ssl/entrust/ecs-client.key

- name: Request domain validation using manual validation.
  community.crypto.ecs_domain:
    domain_name: ansible.com
    verification_method: manual
    entrust_api_user: apiusername
    entrust_api_key: a^lv*32!cd9LnT
    entrust_api_client_cert_path: /etc/ssl/entrust/ecs-client.crt
    entrust_api_client_cert_key_path: /etc/ssl/entrust/ecs-client.key
```

## [Return Values](ecs_domain_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **client_id**  integer | Client ID that the domain belongs to. If the input value *client_id* is specified, this will always be the same as *client_id*  Returned: changed or success  Sample: `1` |
| **dns_contents**  string | The value that ECS will be expecting to find in the DNS record located at *dns_location*.  Returned: changed and if *verification_method* is `dns`  Sample: `"AB23CD41432522FF2526920393982FAB"` |
| **dns_location**  string | The location that ECS will be expecting to be able to find the DNS entry for domain verification, containing the contents of *dns_contents*.  Returned: changed and if *verification_method* is `dns`  Sample: `"_pki-validation.ansible.com"` |
| **dns_resource_type**  string | The type of resource record that ECS will be expecting for the DNS record located at *dns_location*.  Returned: changed and if *verification_method* is `dns`  Sample: `"TXT"` |
| **domain_status**  string | Status of the current domain. Will be one of `APPROVED`, `DECLINED`, `CANCELLED`, `INITIAL_VERIFICATION`, `DECLINED`, `CANCELLED`, `RE_VERIFICATION`, `EXPIRED`, `EXPIRING`  Returned: changed or success  Sample: `"APPROVED"` |
| **emails**  list / elements=string | The list of emails used to request validation of this domain.  Domains requested using this module will only have a list of size 1.  Returned: *verification_method* is `email`  Sample: `["admin@ansible.com", "administrator@ansible.com"]` |
| **ev_days_remaining**  integer | The number of days the domain remains eligible for submission of “EV” certificates. Will never be greater than the value of *ov_days_remaining*  Returned: success and *ev_eligible* is `true` and *domain_status* is `APPROVED`, `RE_VERIFICATION` or `EXPIRING`.  Sample: `94` |
| **ev_eligible**  boolean | Whether the domain is eligible for submission of “EV” certificates. Will never be `true` if *ov_eligible* is `false`  Returned: success and *domain_status* is `APPROVED`, `RE_VERIFICATION` or `EXPIRING`, or `EXPIRED`.  Sample: `true` |
| **file_contents**  string | The contents of the file that ECS will be expecting to find at `file_location`.  Returned: *verification_method* is `web_server`  Sample: `"AB23CD41432522FF2526920393982FAB"` |
| **file_location**  string | The location that ECS will be expecting to be able to find the file for domain verification, containing the contents of *file_contents*.  Returned: *verification_method* is `web_server`  Sample: `"http://ansible.com/.well-known/pki-validation/abcd.txt"` |
| **ov_days_remaining**  integer | The number of days the domain remains eligible for submission of “OV” certificates. Will never be less than the value of *ev_days_remaining*  Returned: success and *ov_eligible* is `true` and *domain_status* is `APPROVED`, `RE_VERIFICATION` or `EXPIRING`.  Sample: `129` |
| **ov_eligible**  boolean | Whether the domain is eligible for submission of “OV” certificates. Will never be `false` if *ov_eligible* is `true`  Returned: success and *domain_status* is `APPROVED`, `RE_VERIFICATION`, `EXPIRING`, or `EXPIRED`.  Sample: `true` |
| **verification_method**  string | Verification method used to request the domain validation. If `changed` will be the same as *verification_method* input parameter.  Returned: changed or success  Sample: `"dns"` |

### Authors

- Chris Trufan (@ctrufan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.crypto)
[Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-crypto)
