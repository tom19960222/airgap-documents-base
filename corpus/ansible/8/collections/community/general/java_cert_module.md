---
collection: ansible
version: "8"
title: "community.general.java_cert module – Uses keytool to import/remove certificate to/from java keystore (cacerts)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/java_cert_module.html
fetched_at: 2026-07-28T01:46:57+00:00
---
# community.general.java_cert module – Uses keytool to import/remove certificate to/from java keystore (cacerts)

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](java_cert_module.md#ansible-collections-community-general-java-cert-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.java_cert`.

- [Synopsis](java_cert_module.md#synopsis)
- [Requirements](java_cert_module.md#requirements)
- [Parameters](java_cert_module.md#parameters)
- [Attributes](java_cert_module.md#attributes)
- [Examples](java_cert_module.md#examples)
- [Return Values](java_cert_module.md#return-values)

## [Synopsis](java_cert_module.md#id1)

- This is a wrapper module around keytool, which can be used to import certificates and optionally private keys to a given java keystore, or remove them from it.

Aliases: system.java_cert

## [Requirements](java_cert_module.md#id2)

The below requirements are needed on the host that executes this module.

- openssl
- keytool

## [Parameters](java_cert_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_alias**  string | Imported certificate alias.  The alias is used when checking for the presence of a certificate in the keystore. |
| **cert_path**  path | Local path to load certificate from.  Exactly one of `cert_url`, `cert_path`, or `pkcs12_path` is required to load certificate. |
| **cert_port**  integer | Port to connect to URL.  This will be used to create server URL:PORT.  **Default:** `443` |
| **cert_url**  string | Basic URL to fetch SSL certificate from.  Exactly one of `cert_url`, `cert_path`, or `pkcs12_path` is required to load certificate. |
| **executable**  string | Path to keytool binary if not used we search in PATH for it.  **Default:** `"keytool"` |
| **keystore_create**  boolean | Create keystore if it does not exist.  **Choices:**   - `false` ← (default) - `true` |
| **keystore_pass**  string / required | Keystore password. |
| **keystore_path**  path | Path to keystore. |
| **keystore_type**  string | Keystore type (JCEKS, JKS). |
| **pkcs12_alias**  string | Alias in the PKCS12 keystore. |
| **pkcs12_password**  string | Password for importing from PKCS12 keystore. |
| **pkcs12_path**  path | Local path to load PKCS12 keystore from.  Unlike `cert_url` and `cert_path`, the PKCS12 keystore embeds the private key matching the certificate, and is used to import both the certificate and its private key into the java keystore.  Exactly one of `cert_url`, `cert_path`, or `pkcs12_path` is required to load certificate. |
| **state**  string | Defines action which can be either certificate import or removal.  When state is present, the certificate will always idempotently be inserted into the keystore, even if there already exists a cert alias that is different.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **trust_cacert**  boolean  *added in community.general 0.2.0* | Trust imported cert as CAcert.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](java_cert_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](java_cert_module.md#id5)

```yaml+jinja
- name: Import SSL certificate from google.com to a given cacerts keystore
  community.general.java_cert:
    cert_url: google.com
    cert_port: 443
    keystore_path: /usr/lib/jvm/jre7/lib/security/cacerts
    keystore_pass: changeit
    state: present

- name: Remove certificate with given alias from a keystore
  community.general.java_cert:
    cert_url: google.com
    keystore_path: /usr/lib/jvm/jre7/lib/security/cacerts
    keystore_pass: changeit
    executable: /usr/lib/jvm/jre7/bin/keytool
    state: absent

- name: Import trusted CA from SSL certificate
  community.general.java_cert:
    cert_path: /opt/certs/rootca.crt
    keystore_path: /tmp/cacerts
    keystore_pass: changeit
    keystore_create: true
    state: present
    cert_alias: LE_RootCA
    trust_cacert: true

- name: Import SSL certificate from google.com to a keystore, create it if it doesn't exist
  community.general.java_cert:
    cert_url: google.com
    keystore_path: /tmp/cacerts
    keystore_pass: changeit
    keystore_create: true
    state: present

- name: Import a pkcs12 keystore with a specified alias, create it if it doesn't exist
  community.general.java_cert:
    pkcs12_path: "/tmp/importkeystore.p12"
    cert_alias: default
    keystore_path: /opt/wildfly/standalone/configuration/defaultkeystore.jks
    keystore_pass: changeit
    keystore_create: true
    state: present

- name: Import SSL certificate to JCEKS keystore
  community.general.java_cert:
    pkcs12_path: "/tmp/importkeystore.p12"
    pkcs12_alias: default
    pkcs12_password: somepass
    cert_alias: default
    keystore_path: /opt/someapp/security/keystore.jceks
    keystore_type: "JCEKS"
    keystore_pass: changeit
    keystore_create: true
    state: present
```

## [Return Values](java_cert_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cmd**  string | Executed command to get action done.  **Returned:** success  **Sample:** `"keytool -importcert -noprompt -keystore"` |
| **msg**  string | Output from stdout of keytool command after execution of given command.  **Returned:** success  **Sample:** `"Module require existing keystore at keystore_path '/tmp/test/cacerts'"` |
| **rc**  integer | Keytool command execution return value.  **Returned:** success  **Sample:** `0` |

### Authors

- Adam Hamsik (@haad)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
