---
collection: ansible
version: "6"
title: "community.mongodb.mongodb_oplog module – Resizes the MongoDB oplog."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/mongodb/mongodb_oplog_module.html
fetched_at: 2026-07-27T17:16:05+00:00
---
# community.mongodb.mongodb_oplog module – Resizes the MongoDB oplog.

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
> see [Requirements](mongodb_oplog_module.md#ansible-collections-community-mongodb-mongodb-oplog-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mongodb.mongodb_oplog`.

New in community.mongodb 1.0.0

- [Synopsis](mongodb_oplog_module.md#synopsis)
- [Requirements](mongodb_oplog_module.md#requirements)
- [Parameters](mongodb_oplog_module.md#parameters)
- [Notes](mongodb_oplog_module.md#notes)
- [Examples](mongodb_oplog_module.md#examples)
- [Return Values](mongodb_oplog_module.md#return-values)

## [Synopsis](mongodb_oplog_module.md#id1)

- Resizes the MongoDB oplog.
- This module should only be used with MongoDB 3.6 and above.
- Old MongoDB versions should use an alternative method.
- Consult <https://docs.mongodb.com/manual/tutorial/change-oplog-size> for further info.

## [Requirements](mongodb_oplog_module.md#id2)

The below requirements are needed on the host that executes this module.

- pymongo

## [Parameters](mongodb_oplog_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_mechanism**  string | Authentication type.  Choices:   - `"SCRAM-SHA-256"` - `"SCRAM-SHA-1"` - `"MONGODB-X509"` - `"GSSAPI"` - `"PLAIN"` |
| **compact**  boolean | Runs compact against the oplog.rs collection in the local database to reclaim disk space.  Performs no actions against PRIMARY members.  The MongoDB user must have the compact role on the local database for this feature to work.  Choices:   - `false` ← (default) - `true` |
| **connection_options**  list / elements=any | Additional connection options.  Supply as a list of dicts or strings containing key value pairs seperated with ‘=’. |
| **login_database**  string | The database where login credentials are stored.  Default: `"admin"` |
| **login_host**  string | The host running MongoDB instance to login to.  Default: `"localhost"` |
| **login_password**  string | The password used to authenticate with.  Required when *login_user* is specified. |
| **login_port**  integer | The MongoDB server port to login to.  Default: `27017` |
| **login_user**  string | The MongoDB user to login with.  Required when *login_password* is specified. |
| **oplog_size_mb**  integer / required | New size of the oplog in MB. |
| **ssl**  aliases: tls  boolean | Whether to use an SSL connection when connecting to the database.  Choices:   - `false` ← (default) - `true` |
| **ssl_ca_certs**  aliases: tlsCAFile  string | The ssl_ca_certs option takes a path to a CA file. |
| **ssl_cert_reqs**  aliases: tlsAllowInvalidCertificates  string | Specifies whether a certificate is required from the other side of the connection, and whether it will be validated if provided.  Choices:   - `"CERT_NONE"` - `"CERT_OPTIONAL"` - `"CERT_REQUIRED"` ← (default) |
| **ssl_certfile**  aliases: tlsCertificateKeyFile  string | Present a client certificate using the ssl_certfile option. |
| **ssl_crlfile**  string | The ssl_crlfile option takes a path to a CRL file. |
| **ssl_keyfile**  string | Private key for the client certificate. |
| **ssl_pem_passphrase**  aliases: tlsCertificateKeyFilePassword  string | Passphrase to decrypt encrypted private keys. |
| **strict_compatibility**  boolean | Enforce strict requirements for pymongo and MongoDB software versions  Choices:   - `false` - `true` ← (default) |

## [Notes](mongodb_oplog_module.md#id4)

> **Note:**
>
> - Requires the pymongo Python package on the remote host, version 2.4.2+. This can be installed using pip or the OS package manager. @see <http://api.mongodb.org/python/current/installation.html>

## [Examples](mongodb_oplog_module.md#id5)

```yaml+jinja
- name: Resize oplog to 16 gigabytes, or 16000 megabytes
  community.mongodb.mongodb_oplog:
    oplog_size_mb: 16000

- name: Resize oplog to 8 gigabytes and compact secondaries to reclaim space
  community.mongodb.mongodb_oplog:
    oplog_size_mb: 8000
    compact: true
```

## [Return Values](mongodb_oplog_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether the member oplog was modified.  Returned: success |
| **compacted**  boolean | Whether the member oplog was compacted.  Returned: success |
| **failed**  boolean | If something went wrong  Returned: failed |
| **msg**  string | A short description of what happened.  Returned: success |

### Authors

- Rhys Campbell (@rhysmeister)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.mongodb)
[Repository (Sources)](https://github.com/ansible-collections/community.mongodb)
