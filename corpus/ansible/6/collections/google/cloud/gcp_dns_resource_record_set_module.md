---
collection: ansible
version: "6"
title: "google.cloud.gcp_dns_resource_record_set module – Creates a GCP ResourceRecordSet"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_dns_resource_record_set_module.html
fetched_at: 2026-07-27T17:48:59+00:00
---
# google.cloud.gcp_dns_resource_record_set module – Creates a GCP ResourceRecordSet

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
> see [Requirements](gcp_dns_resource_record_set_module.md#ansible-collections-google-cloud-gcp-dns-resource-record-set-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_dns_resource_record_set`.

- [Synopsis](gcp_dns_resource_record_set_module.md#synopsis)
- [Requirements](gcp_dns_resource_record_set_module.md#requirements)
- [Parameters](gcp_dns_resource_record_set_module.md#parameters)
- [Examples](gcp_dns_resource_record_set_module.md#examples)
- [Return Values](gcp_dns_resource_record_set_module.md#return-values)

## [Synopsis](gcp_dns_resource_record_set_module.md#id1)

- A single DNS record that exists on a domain name (i.e. in a managed zone).
- This record defines the information about the domain and where the domain / subdomains direct to.
- The record will include the domain/subdomain name, a type (i.e. A, AAA, CAA, MX, CNAME, NS, etc) .

## [Requirements](gcp_dns_resource_record_set_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_dns_resource_record_set_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **managed_zone**  dictionary / required | Identifies the managed zone addressed by this request. This must be a dictionary that contains both a ‘name’ key and a ‘dnsName’ key. You can pass in the results of the gcp_dns_managed_zone module, which will contain both. |
| **name**  string / required | For example, www.example.com. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |
| **target**  list / elements=string | As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) . |
| **ttl**  integer | Number of seconds that this ResourceRecordSet can be cached by resolvers. |
| **type**  string / required | One of valid DNS resource types.  Some valid choices include: “A”, “AAAA”, “CAA”, “CNAME”, “MX”, “NAPTR”, “NS”, “PTR”, “SOA”, “SPF”, “SRV”, “TLSA”, “TXT” |

## [Examples](gcp_dns_resource_record_set_module.md#id4)

```yaml+jinja
- name: create a managed zone
  google.cloud.gcp_dns_managed_zone:
    name: managedzone-rrs
    dns_name: testzone-4.com.
    description: test zone
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: managed_zone

- name: create a resource record set
  google.cloud.gcp_dns_resource_record_set:
    name: www.testzone-4.com.
    managed_zone: "{{ managed_zone }}"
    type: A
    ttl: 600
    target:
    - 10.1.2.3
    - 40.5.6.7
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_dns_resource_record_set_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **managed_zone**  dictionary | Identifies the managed zone addressed by this request. This must be a dictionary that contains both a ‘name’ key and a ‘dnsName’ key. You can pass in the results of the gcp_dns_managed_zone module, which will contain both.  Returned: success |
| **name**  string | For example, www.example.com.  Returned: success |
| **target**  list / elements=string | As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) .  Returned: success |
| **ttl**  integer | Number of seconds that this ResourceRecordSet can be cached by resolvers.  Returned: success |
| **type**  string | One of valid DNS resource types.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
