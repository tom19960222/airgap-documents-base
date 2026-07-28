---
collection: ansible
version: "6"
title: "google.cloud.gcp_sql_ssl_cert module – Creates a GCP SslCert"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_sql_ssl_cert_module.html
fetched_at: 2026-07-27T17:49:30+00:00
---
# google.cloud.gcp_sql_ssl_cert module – Creates a GCP SslCert

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
> see [Requirements](gcp_sql_ssl_cert_module.md#ansible-collections-google-cloud-gcp-sql-ssl-cert-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_sql_ssl_cert`.

- [Synopsis](gcp_sql_ssl_cert_module.md#synopsis)
- [Requirements](gcp_sql_ssl_cert_module.md#requirements)
- [Parameters](gcp_sql_ssl_cert_module.md#parameters)
- [Examples](gcp_sql_ssl_cert_module.md#examples)
- [Return Values](gcp_sql_ssl_cert_module.md#return-values)

## [Synopsis](gcp_sql_ssl_cert_module.md#id1)

- Represents an SSL certificate created for a Cloud SQL instance. To use the SSL certificate you must have the SSL Client Certificate and the associated SSL Client Key. The Client Key can be downloaded only when the SSL certificate is created with the insert method.

## [Requirements](gcp_sql_ssl_cert_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_sql_ssl_cert_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **cert**  string | PEM representation of the X.509 certificate. |
| **cert_serial_number**  string | Serial number, as extracted from the certificate. |
| **common_name**  string | User supplied name. Constrained to [a-zA-Z.-_ ]+. |
| **create_time**  string | The time when the certificate was created in RFC 3339 format, for example 2012-11-15T16:19:00.094Z. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **expiration_time**  string | The time when the certificate expires in RFC 3339 format, for example 2012-11-15T16:19:00.094Z. |
| **instance**  dictionary / required | The name of the Cloud SQL instance. This does not include the project ID.  This field represents a link to a Instance resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘name’ and value of your resource’s name Alternatively, you can add `register: name-of-resource` to a gcp_sql_instance task and then set this instance field to “{{ name-of-resource }}” |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **sha1_fingerprint**  string / required | The SHA-1 of the certificate. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |

## [Examples](gcp_sql_ssl_cert_module.md#id4)

```yaml+jinja
- name: create a instance
  google.cloud.gcp_sql_instance:
    name: "{{resource_name}}-2"
    settings:
      ip_configuration:
        authorized_networks:
        - name: google dns server
          value: 8.8.8.8/32
      tier: db-n1-standard-1
    region: us-central1
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: instance

- name: create a SSL cert
  google.cloud.gcp_sql_ssl_cert:
    common_name: "{{resource_name}}"
    instance: "{{instance['name'}}"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_sql_ssl_cert_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cert**  string | PEM representation of the X.509 certificate.  Returned: success |
| **certSerialNumber**  string | Serial number, as extracted from the certificate.  Returned: success |
| **commonName**  string | User supplied name. Constrained to [a-zA-Z.-_ ]+.  Returned: success |
| **createTime**  string | The time when the certificate was created in RFC 3339 format, for example 2012-11-15T16:19:00.094Z.  Returned: success |
| **expirationTime**  string | The time when the certificate expires in RFC 3339 format, for example 2012-11-15T16:19:00.094Z.  Returned: success |
| **instance**  dictionary | The name of the Cloud SQL instance. This does not include the project ID.  Returned: success |
| **sha1Fingerprint**  string | The SHA-1 of the certificate.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
