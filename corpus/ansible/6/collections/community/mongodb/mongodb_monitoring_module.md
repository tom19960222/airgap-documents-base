---
collection: ansible
version: "6"
title: "community.mongodb.mongodb_monitoring module – Manages the free monitoring feature."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/mongodb/mongodb_monitoring_module.html
fetched_at: 2026-07-27T17:16:04+00:00
---
# community.mongodb.mongodb_monitoring module – Manages the free monitoring feature.

> **Note:**
>
> This module is part of the [community.mongodb collection](https://galaxy.ansible.com/community/mongodb) (version 1.4.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.mongodb`.
> You need further requirements to be able to use this module,
> see [Requirements](mongodb_monitoring_module.md#ansible-collections-community-mongodb-mongodb-monitoring-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mongodb.mongodb_monitoring`.

New in community.mongodb 1.3.0

- [Synopsis](mongodb_monitoring_module.md#synopsis)
- [Requirements](mongodb_monitoring_module.md#requirements)
- [Parameters](mongodb_monitoring_module.md#parameters)
- [Notes](mongodb_monitoring_module.md#notes)
- [Examples](mongodb_monitoring_module.md#examples)
- [Return Values](mongodb_monitoring_module.md#return-values)

## [Synopsis](mongodb_monitoring_module.md#id1)

- Manages the free monitoring feature.
- Optionally return the monitoring url.

## [Requirements](mongodb_monitoring_module.md#id2)

The below requirements are needed on the host that executes this module.

- pymongo

## [Parameters](mongodb_monitoring_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_mechanism**  string | Authentication type.  Choices:   - `"SCRAM-SHA-256"` - `"SCRAM-SHA-1"` - `"MONGODB-X509"` - `"GSSAPI"` - `"PLAIN"` |
| **connection_options**  list / elements=any | Additional connection options.  Supply as a list of dicts or strings containing key value pairs seperated with ‘=’. |
| **login_database**  string | The database where login credentials are stored.  Default: `"admin"` |
| **login_host**  string | The host running MongoDB instance to login to.  Default: `"localhost"` |
| **login_password**  string | The password used to authenticate with.  Required when *login_user* is specified. |
| **login_port**  integer | The MongoDB server port to login to.  Default: `27017` |
| **login_user**  string | The MongoDB user to login with.  Required when *login_password* is specified. |
| **return_url**  boolean | When true return the monitoring url if available.  Choices:   - `false` ← (default) - `true` |
| **ssl**  aliases: tls  boolean | Whether to use an SSL connection when connecting to the database.  Choices:   - `false` ← (default) - `true` |
| **ssl_ca_certs**  aliases: tlsCAFile  string | The ssl_ca_certs option takes a path to a CA file. |
| **ssl_cert_reqs**  aliases: tlsAllowInvalidCertificates  string | Specifies whether a certificate is required from the other side of the connection, and whether it will be validated if provided.  Choices:   - `"CERT_NONE"` - `"CERT_OPTIONAL"` - `"CERT_REQUIRED"` ← (default) |
| **ssl_certfile**  aliases: tlsCertificateKeyFile  string | Present a client certificate using the ssl_certfile option. |
| **ssl_crlfile**  string | The ssl_crlfile option takes a path to a CRL file. |
| **ssl_keyfile**  string | Private key for the client certificate. |
| **ssl_pem_passphrase**  aliases: tlsCertificateKeyFilePassword  string | Passphrase to decrypt encrypted private keys. |
| **state**  string | Manage the free monitoring feature.  Choices:   - `"started"` ← (default) - `"stopped"` |
| **strict_compatibility**  boolean | Enforce strict requirements for pymongo and MongoDB software versions  Choices:   - `false` - `true` ← (default) |

## [Notes](mongodb_monitoring_module.md#id4)

> **Note:**
>
> - Requires the pymongo Python package on the remote host, version 2.4.2+. This can be installed using pip or the OS package manager. @see <http://api.mongodb.org/python/current/installation.html>

## [Examples](mongodb_monitoring_module.md#id5)

```yaml+jinja
- name: Enable monitoring
  community.mongodb.mongodb_monitoring:
    state: "started"

- name: Disable monitoring
  community.mongodb.mongodb_monitoring:
    state: "stopped"

- name: Enable monitoring and return the monitoring url
  community.mongodb_monitoring:
    state: "started"
    return_url: "yes"
```

## [Return Values](mongodb_monitoring_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether the monitoring status changed.  Returned: success |
| **failed**  boolean | If something went wrong  Returned: failed |
| **msg**  string | A short description of what happened.  Returned: success |
| **url**  string | The MongoDB instance Monitoring url.  Returned: When requested and available. |

### Authors

- Rhys Campbell (@rhysmeister)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.mongodb)
[Repository (Sources)](https://github.com/ansible-collections/community.mongodb)
