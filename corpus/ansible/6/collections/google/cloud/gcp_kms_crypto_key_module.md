---
collection: ansible
version: "6"
title: "google.cloud.gcp_kms_crypto_key module – Creates a GCP CryptoKey"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_kms_crypto_key_module.html
fetched_at: 2026-07-27T17:49:06+00:00
---
# google.cloud.gcp_kms_crypto_key module – Creates a GCP CryptoKey

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/google/cloud) (version 1.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_kms_crypto_key_module.md#ansible-collections-google-cloud-gcp-kms-crypto-key-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_kms_crypto_key`.

- [Synopsis](gcp_kms_crypto_key_module.md#synopsis)
- [Requirements](gcp_kms_crypto_key_module.md#requirements)
- [Parameters](gcp_kms_crypto_key_module.md#parameters)
- [Notes](gcp_kms_crypto_key_module.md#notes)
- [Examples](gcp_kms_crypto_key_module.md#examples)
- [Return Values](gcp_kms_crypto_key_module.md#return-values)

## [Synopsis](gcp_kms_crypto_key_module.md#id1)

- A `CryptoKey` represents a logical key that can be used for cryptographic operations.

## [Requirements](gcp_kms_crypto_key_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_kms_crypto_key_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **key_ring**  string / required | The KeyRing that this key belongs to.  Format: `’projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}’`. |
| **labels**  dictionary | Labels with user-defined metadata to apply to this resource. |
| **name**  string / required | The resource name for the CryptoKey. |
| **project**  string | The Google Cloud Platform project to use. |
| **purpose**  string | Immutable purpose of CryptoKey. See <https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose> for inputs.  Some valid choices include: “ENCRYPT_DECRYPT”, “ASYMMETRIC_SIGN”, “ASYMMETRIC_DECRYPT”  Default: `"ENCRYPT_DECRYPT"` |
| **rotation_period**  string | Every time this period passes, generate a new CryptoKeyVersion and set it as the primary.  The first rotation will take place after the specified period. The rotation period has the format of a decimal number with up to 9 fractional digits, followed by the letter `s` (seconds). It must be greater than a day (ie, 86400). |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **skip_initial_version_creation**  boolean | If set to true, the request will create a CryptoKey without any CryptoKeyVersions. You must use the `google_kms_key_ring_import_job` resource to import the CryptoKeyVersion.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |
| **version_template**  dictionary | A template describing settings for new crypto key versions. |
| **algorithm**  string / required | The algorithm to use when creating a version based on this template.  See the [algorithm reference](<https://cloud.google.com/kms/docs/reference/rest/v1/CryptoKeyVersionAlgorithm>) for possible inputs. |
| **protection_level**  string | The protection level to use when creating a version based on this template.  Some valid choices include: “SOFTWARE”, “HSM” |

## [Notes](gcp_kms_crypto_key_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys>
> - Creating a key: <https://cloud.google.com/kms/docs/creating-keys#create_a_key>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_kms_crypto_key_module.md#id5)

```yaml+jinja
- name: create a key ring
  google.cloud.gcp_kms_key_ring:
    name: key-key-ring
    location: us-central1
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: keyring

- name: create a crypto key
  google.cloud.gcp_kms_crypto_key:
    name: test_object
    key_ring: projects/{{ gcp_project }}/locations/us-central1/keyRings/key-key-ring
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_kms_crypto_key_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **createTime**  string | The time that this resource was created on the server.  This is in RFC3339 text format.  Returned: success |
| **keyRing**  string | The KeyRing that this key belongs to.  Format: `’projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}’`.  Returned: success |
| **labels**  dictionary | Labels with user-defined metadata to apply to this resource.  Returned: success |
| **name**  string | The resource name for the CryptoKey.  Returned: success |
| **nextRotationTime**  string | The time when KMS will create a new version of this Crypto Key.  Returned: success |
| **purpose**  string | Immutable purpose of CryptoKey. See <https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose> for inputs.  Returned: success |
| **rotationPeriod**  string | Every time this period passes, generate a new CryptoKeyVersion and set it as the primary.  The first rotation will take place after the specified period. The rotation period has the format of a decimal number with up to 9 fractional digits, followed by the letter `s` (seconds). It must be greater than a day (ie, 86400).  Returned: success |
| **skipInitialVersionCreation**  boolean | If set to true, the request will create a CryptoKey without any CryptoKeyVersions. You must use the `google_kms_key_ring_import_job` resource to import the CryptoKeyVersion.  Returned: success |
| **versionTemplate**  complex | A template describing settings for new crypto key versions.  Returned: success |
| **algorithm**  string | The algorithm to use when creating a version based on this template.  See the [algorithm reference](<https://cloud.google.com/kms/docs/reference/rest/v1/CryptoKeyVersionAlgorithm>) for possible inputs.  Returned: success |
| **protectionLevel**  string | The protection level to use when creating a version based on this template.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
