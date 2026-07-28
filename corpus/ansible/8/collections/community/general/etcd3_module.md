---
collection: ansible
version: "8"
title: "community.general.etcd3 module – Set or delete key value pairs from an etcd3 cluster"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/etcd3_module.html
fetched_at: 2026-07-28T01:45:31+00:00
---
# community.general.etcd3 module – Set or delete key value pairs from an etcd3 cluster

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
> see [Requirements](etcd3_module.md#ansible-collections-community-general-etcd3-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.etcd3`.

- [Synopsis](etcd3_module.md#synopsis)
- [Requirements](etcd3_module.md#requirements)
- [Parameters](etcd3_module.md#parameters)
- [Attributes](etcd3_module.md#attributes)
- [Examples](etcd3_module.md#examples)
- [Return Values](etcd3_module.md#return-values)

## [Synopsis](etcd3_module.md#id1)

- Sets or deletes values in etcd3 cluster using its v3 api.
- Needs python etcd3 lib to work

Aliases: clustering.etcd3

## [Requirements](etcd3_module.md#id2)

The below requirements are needed on the host that executes this module.

- etcd3

## [Parameters](etcd3_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  path | The Certificate Authority to use to verify the etcd host.  Required if `client_cert` and `client_key` are defined. |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  Required if `client_key` is defined. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  Required if `client_cert` is defined. |
| **host**  string | the IP address of the cluster  **Default:** `"localhost"` |
| **key**  string / required | the key where the information is stored in the cluster |
| **password**  string | The password to use for authentication.  Required if `user` is defined. |
| **port**  integer | the port number used to connect to the cluster  **Default:** `2379` |
| **state**  string / required | the state of the value for the key.  can be present or absent  **Choices:**   - `"present"` - `"absent"` |
| **timeout**  integer | The socket level timeout in seconds. |
| **user**  string | The etcd user to authenticate with. |
| **value**  string / required | the information stored |

## [Attributes](etcd3_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](etcd3_module.md#id5)

```yaml+jinja
- name: Store a value "bar" under the key "foo" for a cluster located "http://localhost:2379"
  community.general.etcd3:
    key: "foo"
    value: "baz3"
    host: "localhost"
    port: 2379
    state: "present"

- name: Authenticate using user/password combination with a timeout of 10 seconds
  community.general.etcd3:
    key: "foo"
    value: "baz3"
    state: "present"
    user: "someone"
    password: "password123"
    timeout: 10

- name: Authenticate using TLS certificates
  community.general.etcd3:
    key: "foo"
    value: "baz3"
    state: "present"
    ca_cert: "/etc/ssl/certs/CA_CERT.pem"
    client_cert: "/etc/ssl/certs/cert.crt"
    client_key: "/etc/ssl/private/key.pem"
```

## [Return Values](etcd3_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **key**  string | The key that was queried  **Returned:** always |
| **old_value**  string | The previous value in the cluster  **Returned:** always |

### Authors

- Jean-Philippe Evrard (@evrardjp)
- Victor Fauth (@vfauth)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
