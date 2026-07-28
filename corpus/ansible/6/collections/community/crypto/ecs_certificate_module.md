---
collection: ansible
version: "6"
title: "community.crypto.ecs_certificate module – Request SSL/TLS certificates with the Entrust Certificate Services (ECS) API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/crypto/ecs_certificate_module.html
fetched_at: 2026-07-27T17:06:15+00:00
---
# community.crypto.ecs_certificate module – Request SSL/TLS certificates with the Entrust Certificate Services (ECS) API

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
> see [Requirements](ecs_certificate_module.md#ansible-collections-community-crypto-ecs-certificate-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.ecs_certificate`.

- [Synopsis](ecs_certificate_module.md#synopsis)
- [Requirements](ecs_certificate_module.md#requirements)
- [Parameters](ecs_certificate_module.md#parameters)
- [Attributes](ecs_certificate_module.md#attributes)
- [Notes](ecs_certificate_module.md#notes)
- [See Also](ecs_certificate_module.md#see-also)
- [Examples](ecs_certificate_module.md#examples)
- [Return Values](ecs_certificate_module.md#return-values)

## [Synopsis](ecs_certificate_module.md#id1)

- Create, reissue, and renew certificates with the Entrust Certificate Services (ECS) API.
- Requires credentials for the [Entrust Certificate Services](https://www.entrustdatacard.com/products/categories/ssl-certificates) (ECS) API.
- In order to request a certificate, the domain and organization used in the certificate signing request must be already validated in the ECS system. It is *not* the responsibility of this module to perform those steps.

## [Requirements](ecs_certificate_module.md#id2)

The below requirements are needed on the host that executes this module.

- PyYAML >= 3.11
- cryptography >= 1.6

## [Parameters](ecs_certificate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **additional_emails**  list / elements=string | A list of additional email addresses to receive the delivery notice and expiry notification for the certificate. |
| **backup**  boolean | Whether a backup should be made for the certificate in *path*.  Choices:   - `false` ← (default) - `true` |
| **cert_expiry**  string | The date the certificate should be set to expire, in RFC3339 compliant date or date-time format. For example, `2020-02-23`, `2020-02-23T15:00:00.05Z`.  *cert_expiry* is only supported for requests of `request_type=new` or `request_type=renew`. If `request_type=reissue`, *cert_expiry* will be used for the first certificate issuance, but subsequent issuances will have the same expiry as the initial certificate.  A reissued certificate will always have the same expiry as the original certificate.  Note that only the date (day, month, year) is supported for specifying the expiry date. If you choose to specify an expiry time with the expiry date, the time will be adjusted to Eastern Standard Time (EST). This could have the unintended effect of moving your expiry date to the previous day.  Applies only to accounts with a pooling inventory model.  Only one of *cert_expiry* or *cert_lifetime* may be specified. |
| **cert_lifetime**  string | The lifetime of the certificate.  Applies to all certificates for accounts with a non-pooling inventory model.  *cert_lifetime* is only supported for requests of `request_type=new` or `request_type=renew`. If `request_type=reissue`, *cert_lifetime* will be used for the first certificate issuance, but subsequent issuances will have the same expiry as the initial certificate.  Applies to certificates of *cert_type*=`CDS_INDIVIDUAL, CDS_GROUP, CDS_ENT_LITE, CDS_ENT_PRO, SMIME_ENT` for accounts with a pooling inventory model.  `P1Y` is a certificate with a 1 year lifetime.  `P2Y` is a certificate with a 2 year lifetime.  `P3Y` is a certificate with a 3 year lifetime.  Only one of *cert_expiry* or *cert_lifetime* may be specified.  Choices:   - `"P1Y"` - `"P2Y"` - `"P3Y"` |
| **cert_type**  string | Specify the type of certificate requested.  If a certificate is being reissued or renewed, this parameter is ignored, and the `cert_type` of the initial certificate is used.  Choices:   - `"STANDARD_SSL"` - `"ADVANTAGE_SSL"` - `"UC_SSL"` - `"EV_SSL"` - `"WILDCARD_SSL"` - `"PRIVATE_SSL"` - `"PD_SSL"` - `"CODE_SIGNING"` - `"EV_CODE_SIGNING"` - `"CDS_INDIVIDUAL"` - `"CDS_GROUP"` - `"CDS_ENT_LITE"` - `"CDS_ENT_PRO"` - `"SMIME_ENT"` |
| **client_id**  integer | The client ID to submit the Certificate Signing Request under.  If no client ID is specified, the certificate will be submitted under the primary client with ID of 1.  When using a client other than the primary client, the *org* parameter cannot be specified.  The issued certificate will have an organization value in the subject distinguished name represented by the client.  Default: `1` |
| **csr**  string | Base-64 encoded Certificate Signing Request (CSR). *csr* is accepted with or without PEM formatting around the Base-64 string.  If no *csr* is provided when `request_type=reissue` or `request_type=renew`, the certificate will be generated with the same public key as the certificate being renewed or reissued.  If *subject_alt_name* is specified, it will override the subject alternate names in the CSR.  If *eku* is specified, it will override the extended key usage in the CSR.  If *ou* is specified, it will override the organizational units “ou=” present in the subject distinguished name of the CSR, if any.  The organization “O=” field from the CSR will not be used. It will be replaced in the issued certificate by *org* if present, and if not present, the organization tied to *client_id*. |
| **ct_log**  boolean | In compliance with browser requirements, this certificate may be posted to the Certificate Transparency (CT) logs. This is a best practice technique that helps domain owners monitor certificates issued to their domains. Note that not all certificates are eligible for CT logging.  If *ct_log* is not specified, the certificate uses the account default.  If *ct_log* is specified and the account settings allow it, *ct_log* overrides the account default.  If *ct_log* is set to `false`, but the account settings are set to “always log”, the certificate generation will fail.  Choices:   - `false` - `true` |
| **custom_fields**  dictionary | Mapping of custom fields to associate with the certificate request and certificate.  Only supported if custom fields are enabled for your account.  Each custom field specified must be a custom field you have defined for your account. |
| **date1**  string | Custom date field. |
| **date2**  string | Custom date field. |
| **date3**  string | Custom date field. |
| **date4**  string | Custom date field. |
| **date5**  string | Custom date field. |
| **dropdown1**  string | Custom dropdown field. |
| **dropdown2**  string | Custom dropdown field. |
| **dropdown3**  string | Custom dropdown field. |
| **dropdown4**  string | Custom dropdown field. |
| **dropdown5**  string | Custom dropdown field. |
| **email1**  string | Custom email field. |
| **email2**  string | Custom email field. |
| **email3**  string | Custom email field. |
| **email4**  string | Custom email field. |
| **email5**  string | Custom email field. |
| **number1**  float | Custom number field. |
| **number2**  float | Custom number field. |
| **number3**  float | Custom number field. |
| **number4**  float | Custom number field. |
| **number5**  float | Custom number field. |
| **text1**  string | Custom text field (maximum 500 characters) |
| **text10**  string | Custom text field (maximum 500 characters) |
| **text11**  string | Custom text field (maximum 500 characters) |
| **text12**  string | Custom text field (maximum 500 characters) |
| **text13**  string | Custom text field (maximum 500 characters) |
| **text14**  string | Custom text field (maximum 500 characters) |
| **text15**  string | Custom text field (maximum 500 characters) |
| **text2**  string | Custom text field (maximum 500 characters) |
| **text3**  string | Custom text field (maximum 500 characters) |
| **text4**  string | Custom text field (maximum 500 characters) |
| **text5**  string | Custom text field (maximum 500 characters) |
| **text6**  string | Custom text field (maximum 500 characters) |
| **text7**  string | Custom text field (maximum 500 characters) |
| **text8**  string | Custom text field (maximum 500 characters) |
| **text9**  string | Custom text field (maximum 500 characters) |
| **eku**  string | If specified, overrides the key usage in the *csr*.  Choices:   - `"SERVER_AUTH"` - `"CLIENT_AUTH"` - `"SERVER_AND_CLIENT_AUTH"` |
| **end_user_key_storage_agreement**  boolean | The end user of the Code Signing certificate must generate and store the private key for this request on cryptographically secure hardware to be compliant with the Entrust CSP and Subscription agreement. If requesting a certificate of type `CODE_SIGNING` or `EV_CODE_SIGNING`, you must set *end_user_key_storage_agreement* to true if and only if you acknowledge that you will inform the user of this requirement.  Applicable only to *cert_type* of values `CODE_SIGNING` and `EV_CODE_SIGNING`.  Choices:   - `false` - `true` |
| **entrust_api_client_cert_key_path**  path / required | The path to the key for the client certificate used to authenticate to the Entrust Certificate Services (ECS) API. |
| **entrust_api_client_cert_path**  path / required | The path to the client certificate used to authenticate to the Entrust Certificate Services (ECS) API. |
| **entrust_api_key**  string / required | The key (password) for authentication to the Entrust Certificate Services (ECS) API. |
| **entrust_api_specification_path**  path | The path to the specification file defining the Entrust Certificate Services (ECS) API configuration.  You can use this to keep a local copy of the specification to avoid downloading it every time the module is used.  Default: `"https://cloud.entrust.net/EntrustCloud/documentation/cms-api-2.1.0.yaml"` |
| **entrust_api_user**  string / required | The username for authentication to the Entrust Certificate Services (ECS) API. |
| **force**  boolean | If force is used, a certificate is requested regardless of whether *path* points to an existing valid certificate.  If `request_type=renew`, a forced renew will fail if the certificate being renewed has been issued within the past 30 days, regardless of the value of *remaining_days* or the return value of *cert_days* - the ECS API does not support the “renew” operation for certificates that are not at least 30 days old.  Choices:   - `false` ← (default) - `true` |
| **full_chain_path**  path | The destination path for the full certificate chain of the certificate, intermediates, and roots. |
| **org**  string | Organization “O=” to include in the certificate.  If *org* is not specified, the organization from the client represented by *client_id* is used.  Unless the *cert_type* is `PD_SSL`, this field may not be specified if the value of *client_id* is not “1” (the primary client). non-primary clients, certificates may only be issued with the organization of that client. |
| **ou**  list / elements=string | Organizational unit “OU=” to include in the certificate.  *ou* behavior is dependent on whether organizational units are enabled for your account. If organizational unit support is disabled for your account, organizational units from the *csr* and the *ou* parameter are ignored.  If both *csr* and *ou* are specified, the value in *ou* will override the OU fields present in the subject distinguished name in the *csr*  If neither *csr* nor *ou* are specified for a renew or reissue operation, the OU fields in the initial certificate are reused.  An invalid OU from *csr* is ignored, but any invalid organizational units in *ou* will result in an error indicating “Unapproved OU”. The *ou* parameter can be used to force failure if an unapproved organizational unit is provided.  A maximum of one OU may be specified for current products. Multiple OUs are reserved for future products. |
| **path**  path / required | The destination path for the generated certificate as a PEM encoded cert.  If the certificate at this location is not an Entrust issued certificate, a new certificate will always be requested even if the current certificate is technically valid.  If there is already an Entrust certificate at this location, whether it is replaced is depends on the *remaining_days* calculation.  If an existing certificate is being replaced (see *remaining_days*, *force*, and *tracking_id*), whether a new certificate is requested or the existing certificate is renewed or reissued is based on *request_type*. |
| **remaining_days**  integer | The number of days the certificate must have left being valid. If `cert_days < remaining_days` then a new certificate will be obtained using *request_type*.  If `request_type=renew`, a renewal will fail if the certificate being renewed has been issued within the past 30 days, so do not set a *remaining_days* value that is within 30 days of the full lifetime of the certificate being acted upon.  For exmaple, if you are requesting Certificates with a 90 day lifetime, do not set *remaining_days* to a value `60` or higher).  The *force* option may be used to ensure that a new certificate is always obtained.  Default: `30` |
| **request_type**  string | The operation performed if *tracking_id* references a valid certificate to reissue, or there is already a certificate present in *path* but either *force* is specified or `cert_days < remaining_days`.  Specifying `request_type=validate_only` means the request will be validated against the ECS API, but no certificate will be issued.  Specifying `request_type=new` means a certificate request will always be submitted and a new certificate issued.  Specifying `request_type=renew` means that an existing certificate (specified by *tracking_id* if present, otherwise *path*) will be renewed. If there is no certificate to renew, a new certificate is requested.  Specifying `request_type=reissue` means that an existing certificate (specified by *tracking_id* if present, otherwise *path*) will be reissued. If there is no certificate to reissue, a new certificate is requested.  If a certificate was issued within the past 30 days, the `renew` operation is not a valid operation and will fail.  Note that `reissue` is an operation that will result in the revocation of the certificate that is reissued, be cautious with its use.  *check_mode* is only supported if `request_type=new`  For example, setting `request_type=renew` and `remaining_days=30` and pointing to the same certificate on multiple playbook runs means that on the first run new certificate will be requested. It will then be left along on future runs until it is within 30 days of expiry, then the ECS “renew” operation will be performed.  Choices:   - `"new"` ← (default) - `"renew"` - `"reissue"` - `"validate_only"` |
| **requester_email**  string / required | The requester email to associate with certificate tracking information and receive delivery and expiry notices for the certificate. |
| **requester_name**  string / required | The requester name to associate with certificate tracking information. |
| **requester_phone**  string / required | The requester phone number to associate with certificate tracking information. |
| **subject_alt_name**  list / elements=string | The subject alternative name identifiers, as an array of values (applies to *cert_type* with a value of `STANDARD_SSL`, `ADVANTAGE_SSL`, `UC_SSL`, `EV_SSL`, `WILDCARD_SSL`, `PRIVATE_SSL`, and `PD_SSL`).  If you are requesting a new SSL certificate, and you pass a *subject_alt_name* parameter, any SAN names in the CSR are ignored. If no subjectAltName parameter is passed, the SAN names in the CSR are used.  See *request_type* to understand more about SANs during reissues and renewals.  In the case of certificates of type `STANDARD_SSL` certificates, if the CN of the certificate is <domain>.<tld> only the www.<domain>.<tld> value is accepted. If the CN of the certificate is www.<domain>.<tld> only the <domain>.<tld> value is accepted. |
| **tracking_id**  integer | The tracking ID of the certificate to reissue or renew.  *tracking_id* is invalid if `request_type=new` or `request_type=validate_only`.  If there is a certificate present in *path* and it is an ECS certificate, *tracking_id* will be ignored.  If there is no certificate present in *path* or there is but it is from another provider, the certificate represented by *tracking_id* will be renewed or reissued and saved to *path*.  If there is no certificate present in *path* and the *force* and *remaining_days* parameters do not indicate a new certificate is needed, the certificate referenced by *tracking_id* certificate will be saved to *path*.  This can be used when a known certificate is not currently present on a server, but you want to renew or reissue it to be managed by an ansible playbook. For example, if you specify `request_type=renew`, *tracking_id* of an issued certificate, and *path* to a file that does not exist, the first run of a task will download the certificate specified by *tracking_id* (assuming it is still valid). Future runs of the task will (if applicable - see *force* and *remaining_days*) renew the certificate now present in *path*. |
| **tracking_info**  string | Free form tracking information to attach to the record for the certificate. |

## [Attributes](ecs_certificate_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: partial  Check mode is only supported if *request_type=new*. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **safe_file_operations** | Support: full | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption. |

## [Notes](ecs_certificate_module.md#id5)

> **Note:**
>
> - `path` must be specified as the output location of the certificate.

## [See Also](ecs_certificate_module.md#id6)

> **See also:**
>
> [community.crypto.openssl_privatekey](openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module)
> :   Can be used to create private keys (both for certificates and accounts).
>
> [community.crypto.openssl_csr](openssl_csr_module.md#ansible-collections-community-crypto-openssl-csr-module)
> :   Can be used to create a Certificate Signing Request (CSR).

## [Examples](ecs_certificate_module.md#id7)

```yaml+jinja
- name: Request a new certificate from Entrust with bare minimum parameters.
        Will request a new certificate if current one is valid but within 30
        days of expiry. If replacing an existing file in path, will back it up.
  community.crypto.ecs_certificate:
    backup: true
    path: /etc/ssl/crt/ansible.com.crt
    full_chain_path: /etc/ssl/crt/ansible.com.chain.crt
    csr: /etc/ssl/csr/ansible.com.csr
    cert_type: EV_SSL
    requester_name: Jo Doe
    requester_email: jdoe@ansible.com
    requester_phone: 555-555-5555
    entrust_api_user: apiusername
    entrust_api_key: a^lv*32!cd9LnT
    entrust_api_client_cert_path: /etc/ssl/entrust/ecs-client.crt
    entrust_api_client_cert_key_path: /etc/ssl/entrust/ecs-client.key

- name: If there is no certificate present in path, request a new certificate
        of type EV_SSL. Otherwise, if there is an Entrust managed certificate
        in path and it is within 63 days of expiration, request a renew of that
        certificate.
  community.crypto.ecs_certificate:
    path: /etc/ssl/crt/ansible.com.crt
    csr: /etc/ssl/csr/ansible.com.csr
    cert_type: EV_SSL
    cert_expiry: '2020-08-20'
    request_type: renew
    remaining_days: 63
    requester_name: Jo Doe
    requester_email: jdoe@ansible.com
    requester_phone: 555-555-5555
    entrust_api_user: apiusername
    entrust_api_key: a^lv*32!cd9LnT
    entrust_api_client_cert_path: /etc/ssl/entrust/ecs-client.crt
    entrust_api_client_cert_key_path: /etc/ssl/entrust/ecs-client.key

- name: If there is no certificate present in path, download certificate
        specified by tracking_id if it is still valid. Otherwise, if the
        certificate is within 79 days of expiration, request a renew of that
        certificate and save it in path. This can be used to "migrate" a
        certificate to be Ansible managed.
  community.crypto.ecs_certificate:
    path: /etc/ssl/crt/ansible.com.crt
    csr: /etc/ssl/csr/ansible.com.csr
    tracking_id: 2378915
    request_type: renew
    remaining_days: 79
    entrust_api_user: apiusername
    entrust_api_key: a^lv*32!cd9LnT
    entrust_api_client_cert_path: /etc/ssl/entrust/ecs-client.crt
    entrust_api_client_cert_key_path: /etc/ssl/entrust/ecs-client.key

- name: Force a reissue of the certificate specified by tracking_id.
  community.crypto.ecs_certificate:
    path: /etc/ssl/crt/ansible.com.crt
    force: true
    tracking_id: 2378915
    request_type: reissue
    entrust_api_user: apiusername
    entrust_api_key: a^lv*32!cd9LnT
    entrust_api_client_cert_path: /etc/ssl/entrust/ecs-client.crt
    entrust_api_client_cert_key_path: /etc/ssl/entrust/ecs-client.key

- name: Request a new certificate with an alternative client. Note that the
        issued certificate will have it's Subject Distinguished Name use the
        organization details associated with that client, rather than what is
        in the CSR.
  community.crypto.ecs_certificate:
    path: /etc/ssl/crt/ansible.com.crt
    csr: /etc/ssl/csr/ansible.com.csr
    client_id: 2
    requester_name: Jo Doe
    requester_email: jdoe@ansible.com
    requester_phone: 555-555-5555
    entrust_api_user: apiusername
    entrust_api_key: a^lv*32!cd9LnT
    entrust_api_client_cert_path: /etc/ssl/entrust/ecs-client.crt
    entrust_api_client_cert_key_path: /etc/ssl/entrust/ecs-client.key

- name: Request a new certificate with a number of CSR parameters overridden
        and tracking information
  community.crypto.ecs_certificate:
    path: /etc/ssl/crt/ansible.com.crt
    full_chain_path: /etc/ssl/crt/ansible.com.chain.crt
    csr: /etc/ssl/csr/ansible.com.csr
    subject_alt_name:
      - ansible.testcertificates.com
      - www.testcertificates.com
    eku: SERVER_AND_CLIENT_AUTH
    ct_log: true
    org: Test Organization Inc.
    ou:
      - Administration
    tracking_info: "Submitted via Ansible"
    additional_emails:
      - itsupport@testcertificates.com
      - jsmith@ansible.com
    custom_fields:
      text1: Admin
      text2: Invoice 25
      number1: 342
      date1: '2018-01-01'
      email1: sales@ansible.testcertificates.com
      dropdown1: red
    cert_expiry: '2020-08-15'
    requester_name: Jo Doe
    requester_email: jdoe@ansible.com
    requester_phone: 555-555-5555
    entrust_api_user: apiusername
    entrust_api_key: a^lv*32!cd9LnT
    entrust_api_client_cert_path: /etc/ssl/entrust/ecs-client.crt
    entrust_api_client_cert_key_path: /etc/ssl/entrust/ecs-client.key
```

## [Return Values](ecs_certificate_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_file**  string | Name of backup file created for the certificate.  Returned: changed and if *backup* is `true`  Sample: `"/path/to/www.ansible.com.crt.2019-03-09@11:22~"` |
| **backup_full_chain_file**  string | Name of the backup file created for the certificate chain.  Returned: changed and if *backup* is `true` and *full_chain_path* is set.  Sample: `"/path/to/ca.chain.crt.2019-03-09@11:22~"` |
| **cert_days**  integer | The number of days the certificate remains valid.  Returned: success  Sample: `253` |
| **cert_details**  dictionary | The full response JSON from the Get Certificate call of the ECS API.  While the response contents are guaranteed to be forwards compatible with new ECS API releases, Entrust recommends that you do not make any playbooks take actions based on the content of this field. However it may be useful for debugging, logging, or auditing purposes.  Returned: success |
| **cert_status**  string | The certificate status in ECS.  Current possible values (which may be expanded in the future) are: `ACTIVE`, `APPROVED`, `DEACTIVATED`, `DECLINED`, `EXPIRED`, `NA`, `PENDING`, `PENDING_QUORUM`, `READY`, `REISSUED`, `REISSUING`, `RENEWED`, `RENEWING`, `REVOKED`, `SUSPENDED`  Returned: success  Sample: `"ACTIVE"` |
| **filename**  string | The destination path for the generated certificate.  Returned: changed or success  Sample: `"/etc/ssl/crt/www.ansible.com.crt"` |
| **serial_number**  integer | The serial number of the issued certificate.  Returned: success  Sample: `1235262234164342` |
| **tracking_id**  integer | The tracking ID to reference and track the certificate in ECS.  Returned: success  Sample: `380079` |

### Authors

- Chris Trufan (@ctrufan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.crypto)
[Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-crypto)
