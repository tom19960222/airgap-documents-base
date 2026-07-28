---
collection: ansible
version: "8"
title: "community.hashi_vault.vault_pki_generate_certificate module – Generates a new set of credentials (private key and certificate) using HashiCorp Vault PKI"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/hashi_vault/vault_pki_generate_certificate_module.html
fetched_at: 2026-07-28T01:53:31+00:00
---
# community.hashi_vault.vault_pki_generate_certificate module – Generates a new set of credentials (private key and certificate) using HashiCorp Vault PKI

> **Note:**
>
> This module is part of the [community.hashi_vault collection](https://galaxy.ansible.com/ui/repo/published/community/hashi_vault/) (version 5.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.hashi_vault`.
> You need further requirements to be able to use this module,
> see [Requirements](vault_pki_generate_certificate_module.md#ansible-collections-community-hashi-vault-vault-pki-generate-certificate-module-requirements) for details.
>
> To use it in a playbook, specify: `community.hashi_vault.vault_pki_generate_certificate`.

New in community.hashi_vault 2.3.0

- [Synopsis](vault_pki_generate_certificate_module.md#synopsis)
- [Requirements](vault_pki_generate_certificate_module.md#requirements)
- [Parameters](vault_pki_generate_certificate_module.md#parameters)
- [Attributes](vault_pki_generate_certificate_module.md#attributes)
- [See Also](vault_pki_generate_certificate_module.md#see-also)
- [Examples](vault_pki_generate_certificate_module.md#examples)
- [Return Values](vault_pki_generate_certificate_module.md#return-values)

## [Synopsis](vault_pki_generate_certificate_module.md#id1)

- Generates a new set of credentials (private key and certificate) based on a Vault PKI role.

## [Requirements](vault_pki_generate_certificate_module.md#id2)

The below requirements are needed on the host that executes this module.

- `hvac` ([Python library](https://hvac.readthedocs.io/en/stable/changelog.html#may-25th-2019)) version `0.9.1` or higher
- For detailed requirements, see [the collection requirements page](docsite/user_guide.md#ansible-collections-community-hashi-vault-docsite-user-guide-requirements).

## [Parameters](vault_pki_generate_certificate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alt_names**  list / elements=string | Specifies requested Subject Alternative Names.  These can be host names or email addresses; they will be parsed into their respective fields.  If any requested names do not match role policy, the entire request will be denied.  **Default:** `[]` |
| **auth_method**  string | Authentication method to be used.  `none` auth method was added in collection version `1.2.0`.  `cert` auth method was added in collection version `1.4.0`.  `aws_iam_login` was renamed `aws_iam` in collection version `2.1.0` and was removed in `3.0.0`.  `azure` auth method was added in collection version `3.2.0`.  **Choices:**   - `"token"` ← (default) - `"userpass"` - `"ldap"` - `"approle"` - `"aws_iam"` - `"azure"` - `"jwt"` - `"cert"` - `"none"` |
| **aws_access_key**  aliases: aws_access_key_id  string | The AWS access key to use. |
| **aws_iam_server_id**  string  *added in community.hashi_vault 0.2.0* | If specified, sets the value to use for the `X-Vault-AWS-IAM-Server-ID` header as part of `GetCallerIdentity` request. |
| **aws_profile**  aliases: boto_profile  string | The AWS profile |
| **aws_secret_key**  aliases: aws_secret_access_key  string | The AWS secret key that corresponds to the access key. |
| **aws_security_token**  string | The AWS security token if using temporary access and secret keys. |
| **azure_client_id**  string  *added in community.hashi_vault 3.2.0* | The client ID (also known as application ID) of the Azure AD service principal or managed identity. Should be a UUID.  If not specified, will use the system assigned managed identity. |
| **azure_client_secret**  string  *added in community.hashi_vault 3.2.0* | The client secret of the Azure AD service principal. |
| **azure_resource**  string  *added in community.hashi_vault 3.2.0* | The resource URL for the application registered in Azure Active Directory. Usually should not be changed from the default.  **Default:** `"https://management.azure.com/"` |
| **azure_tenant_id**  string  *added in community.hashi_vault 3.2.0* | The Azure Active Directory Tenant ID (also known as the Directory ID) of the service principal. Should be a UUID.  Required when using a service principal to authenticate to Vault, e.g. required when both *azure_client_id* and *azure_client_secret* are specified.  Optional when using managed identity to authenticate to Vault. |
| **ca_cert**  aliases: cacert  string | Path to certificate to use for authentication.  If not specified by any other means, the `VAULT_CACERT` environment variable will be used. |
| **cert_auth_private_key**  path  *added in community.hashi_vault 1.4.0* | For `cert` auth, path to the private key file to authenticate with, in PEM format. |
| **cert_auth_public_key**  path  *added in community.hashi_vault 1.4.0* | For `cert` auth, path to the certificate file to authenticate with, in PEM format. |
| **common_name**  string / required | Specifies the requested CN for the certificate.  If the CN is allowed by role policy, it will be issued. |
| **engine_mount_point**  string | Specify the mount point used by the PKI engine.  Defaults to the default used by `hvac`. |
| **exclude_cn_from_sans**  boolean | If true, the given *common_name* will not be included in DNS or Email Subject Alternate Names (as appropriate).  Useful if the CN is not a hostname or email address, but is instead some human-readable identifier.  **Choices:**   - `false` ← (default) - `true` |
| **format**  string | Specifies the format for returned data.  Can be `pem`, `der`, or `pem_bundle`.  If `der`, the output is base64 encoded.  If `pem_bundle`, the `certificate` field will contain the private key and certificate, concatenated. If the issuing CA is not a Vault-derived self-signed root, this will be included as well.  **Choices:**   - `"pem"` ← (default) - `"der"` - `"pem_bundle"` |
| **ip_sans**  list / elements=string | Specifies requested IP Subject Alternative Names.  Only valid if the role allows IP SANs (which is the default).  **Default:** `[]` |
| **jwt**  string | The JSON Web Token (JWT) to use for JWT authentication to Vault. |
| **mount_point**  string | Vault mount point.  If not specified, the default mount point for a given auth method is used.  Does not apply to token authentication. |
| **namespace**  string | Vault namespace where secrets reside. This option requires HVAC 0.7.0+ and Vault 0.11+.  Optionally, this may be achieved by prefixing the authentication mount point and/or secret path with the namespace (e.g `mynamespace/secret/mysecret`).  If environment variable `VAULT_NAMESPACE` is set, its value will be used last among all ways to specify *namespace*. |
| **other_sans**  list / elements=string | Specifies custom OID/UTF8-string SANs.  These must match values specified on the role in `allowed_other_sans`.  The format is the same as OpenSSL: `<oid>;<type>:<value>` where the only current valid type is `UTF8`.  **Default:** `[]` |
| **password**  string | Authentication password. |
| **private_key_format**  string | Specifies the format for marshaling the private key.  Defaults to `der` which will return either base64-encoded DER or PEM-encoded DER, depending on the value of *format*.  The other option is `pkcs8` which will return the key marshalled as PEM-encoded PKCS8.  **Choices:**   - `"der"` ← (default) - `"pkcs8"` |
| **proxies**  any  *added in community.hashi_vault 1.1.0* | URL(s) to the proxies used to access the Vault service.  It can be a string or a dict.  If it’s a dict, provide the scheme (eg. `http` or `https`) as the key, and the URL as the value.  If it’s a string, provide a single URL that will be used as the proxy for both `http` and `https` schemes.  A string that can be interpreted as a dictionary will be converted to one (see examples).  You can specify a different proxy for HTTP and HTTPS resources.  If not specified, [environment variables from the Requests library](https://requests.readthedocs.io/en/master/user/advanced/#proxies) are used. |
| **region**  string | The AWS region for which to create the connection. |
| **retries**  any  *added in community.hashi_vault 1.3.0* | Allows for retrying on errors, based on the [Retry class in the urllib3 library](https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html#urllib3.util.Retry).  This collection defines recommended defaults for retrying connections to Vault.  This option can be specified as a positive number (integer) or dictionary.  If this option is not specified or the number is `0`, then retries are disabled.  A number sets the total number of retries, and uses collection defaults for the other settings.  A dictionary value is used directly to initialize the `Retry` class, so it can be used to fully customize retries.  For detailed information on retries, see the collection User Guide. |
| **retry_action**  string  *added in community.hashi_vault 1.3.0* | Controls whether and how to show messages on *retries*.  This has no effect if a request is not retried.  **Choices:**   - `"ignore"` - `"warn"` ← (default) |
| **role_id**  string | Vault Role ID or name. Used in `approle`, `aws_iam`, `azure` and `cert` auth methods.  For `cert` auth, if no *role_id* is supplied, the default behavior is to try all certificate roles and return any one that matches.  For `azure` auth, *role_id* is required. |
| **role_name**  string / required | Specifies the name of the role to create the certificate against. |
| **secret_id**  string | Secret ID to be used for Vault AppRole authentication. |
| **timeout**  integer  *added in community.hashi_vault 1.3.0* | Sets the connection timeout in seconds.  If not set, then the `hvac` library’s default is used. |
| **token**  string | Vault token. Token may be specified explicitly, through the listed [env] vars, and also through the `VAULT_TOKEN` env var.  If no token is supplied, explicitly or through env, then the plugin will check for a token file, as determined by *token_path* and *token_file*.  The order of token loading (first found wins) is `token param -> ansible var -> ANSIBLE_HASHI_VAULT_TOKEN -> VAULT_TOKEN -> token file`. |
| **token_file**  string | If no token is specified, will try to read the token from this file in *token_path*.  **Default:** `".vault-token"` |
| **token_path**  string | If no token is specified, will try to read the *token_file* from this path. |
| **token_validate**  boolean  *added in community.hashi_vault 0.2.0* | For token auth, will perform a `lookup-self` operation to determine the token’s validity before using it.  Disable if your token does not have the `lookup-self` capability.  **Choices:**   - `false` ← (default) - `true` |
| **ttl**  string | Specifies requested Time To Live.  Cannot be greater than the role’s `max_ttl` value.  If not provided, the role’s `ttl` value will be used.  Note that the role values default to system values if not explicitly set. |
| **uri_sans**  list / elements=string | Specifies the requested URI Subject Alternative Names.  **Default:** `[]` |
| **url**  string | URL to the Vault service.  If not specified by any other means, the value of the `VAULT_ADDR` environment variable will be used.  If `VAULT_ADDR` is also not defined then an error will be raised. |
| **username**  string | Authentication user name. |
| **validate_certs**  boolean | Controls verification and validation of SSL certificates, mostly you only want to turn off with self signed ones.  Will be populated with the inverse of `VAULT_SKIP_VERIFY` if that is set and *validate_certs* is not explicitly provided.  Will default to `true` if neither *validate_certs* or `VAULT_SKIP_VERIFY` are set.  **Choices:**   - `false` - `true` |

## [Attributes](vault_pki_generate_certificate_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action group:** **community.hashi_vault.vault** | Use `group/community.hashi_vault.vault` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **partial**  In check mode, this module will not contact Vault and will return an empty `data` field and `changed` status. | Can run in `check_mode` and return changed status prediction without modifying target. |

## [See Also](vault_pki_generate_certificate_module.md#id5)

> **See also:**
>
> [HashiCorp Vault PKI Secrets Engine API](https://www.vaultproject.io/api/secret/pki#generate-certificate)
> :   API documentation for the HashiCorp Vault PKI secrets engine.
>
> [HVAC library reference](https://hvac.readthedocs.io/en/stable/usage/secrets_engines/pki.html#generate-certificate)
> :   HVAC library reference about the PKI engine.

## [Examples](vault_pki_generate_certificate_module.md#id6)

```yaml+jinja
- name: Login and use the resulting token
  community.hashi_vault.vault_login:
    url: https://localhost:8200
    auth_method: ldap
    username: "john.doe"
    password: "{{ user_passwd }}"
  register: login_data

- name: Generate a certificate with an existing token
  community.hashi_vault.vault_pki_generate_certificate:
    role_name: test.example.org
    common_name: test.example.org
    ttl: 8760h
    alt_names:
      - test2.example.org
      - test3.example.org
    url: https://vault:8201
    auth_method: token
    token: "{{ login_data.login.auth.client_token }}"
  register: cert_data

- name: Display generated certificate
  debug:
    msg: "{{ cert_data.data.data.certificate }}"
```

## [Return Values](vault_pki_generate_certificate_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about newly generated certificate  **Returned:** success |
| **data**  complex | Payload  **Returned:** success |
| **ca_chain**  list / elements=string | Linked list of CA certificates.  **Returned:** success  **Sample:** `["-----BEGIN CERTIFICATE-----...-----END CERTIFICATE-----"]` |
| **certificate**  string | Generated certificate.  **Returned:** success  **Sample:** `"-----BEGIN CERTIFICATE-----...-----END CERTIFICATE-----"` |
| **issuing_ca**  string | CA certificate.  **Returned:** success  **Sample:** `"-----BEGIN CERTIFICATE-----...-----END CERTIFICATE-----"` |
| **private_key**  string | Private key used to generate certificate.  **Returned:** success  **Sample:** `"-----BEGIN RSA PRIVATE KEY-----...-----END RSA PRIVATE KEY-----"` |
| **private_key_type**  string | Private key algorithm.  **Returned:** success  **Sample:** `"rsa"` |
| **serial_number**  string | Certificate’s serial number.  **Returned:** success  **Sample:** `"39:dd:2e:90:b7:23:1f:8d:d3:7d:31:c5:1b:da:84:d0:5b:65:31:58"` |
| **lease_duration**  integer | Vault lease duration.  **Returned:** success  **Sample:** `21600` |
| **lease_id**  string | Vault lease attached to certificate.  **Returned:** success  **Sample:** `"pki/issue/test/7ad6cfa5-f04f-c62a-d477-f33210475d05"` |
| **renewable**  boolean | True if certificate is renewable.  **Returned:** success  **Sample:** `false` |
| **warning**  string | Warnings returned by Vault during generation.  **Returned:** success |

### Authors

- Florent David (@Ripolin)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.hashi_vault/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.hashi_vault)
- [Discussion, Q&A, troubleshooting](https://github.com/ansible-collections/community.hashi_vault/discussions)
- [Communication](index.md#communication-for-community-hashi-vault)
