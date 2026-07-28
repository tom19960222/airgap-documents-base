---
collection: ansible
version: "6"
title: "community.mongodb.mongodb_info module – Gather information about MongoDB instance."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/mongodb/mongodb_info_module.html
fetched_at: 2026-07-27T17:16:03+00:00
---
# community.mongodb.mongodb_info module – Gather information about MongoDB instance.

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
> see [Requirements](mongodb_info_module.md#ansible-collections-community-mongodb-mongodb-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mongodb.mongodb_info`.

New in community.mongodb 1.0.0

- [Synopsis](mongodb_info_module.md#synopsis)
- [Requirements](mongodb_info_module.md#requirements)
- [Parameters](mongodb_info_module.md#parameters)
- [Notes](mongodb_info_module.md#notes)
- [Examples](mongodb_info_module.md#examples)
- [Return Values](mongodb_info_module.md#return-values)

## [Synopsis](mongodb_info_module.md#id1)

- Gather information about MongoDB instance.

## [Requirements](mongodb_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- pymongo

## [Parameters](mongodb_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_mechanism**  string | Authentication type.  Choices:   - `"SCRAM-SHA-256"` - `"SCRAM-SHA-1"` - `"MONGODB-X509"` - `"GSSAPI"` - `"PLAIN"` |
| **connection_options**  list / elements=any | Additional connection options.  Supply as a list of dicts or strings containing key value pairs seperated with ‘=’. |
| **filter**  list / elements=string | Limit the collected information by comma separated string or YAML list.  Allowable values are `general`, `databases`, `total_size`, `parameters`, `users`, `roles`.  By default, collects all subsets.  You can use ‘!’ before value (for example, `!users`) to exclude it from the information.  If you pass including and excluding values to the filter, for example, *filter=!general,users*, the excluding values, `!general` in this case, will be ignored. |
| **login_database**  string | The database where login credentials are stored.  Default: `"admin"` |
| **login_host**  string | The host running MongoDB instance to login to.  Default: `"localhost"` |
| **login_password**  string | The password used to authenticate with.  Required when *login_user* is specified. |
| **login_port**  integer | The MongoDB server port to login to.  Default: `27017` |
| **login_user**  string | The MongoDB user to login with.  Required when *login_password* is specified. |
| **ssl**  aliases: tls  boolean | Whether to use an SSL connection when connecting to the database.  Choices:   - `false` ← (default) - `true` |
| **ssl_ca_certs**  aliases: tlsCAFile  string | The ssl_ca_certs option takes a path to a CA file. |
| **ssl_cert_reqs**  aliases: tlsAllowInvalidCertificates  string | Specifies whether a certificate is required from the other side of the connection, and whether it will be validated if provided.  Choices:   - `"CERT_NONE"` - `"CERT_OPTIONAL"` - `"CERT_REQUIRED"` ← (default) |
| **ssl_certfile**  aliases: tlsCertificateKeyFile  string | Present a client certificate using the ssl_certfile option. |
| **ssl_crlfile**  string | The ssl_crlfile option takes a path to a CRL file. |
| **ssl_keyfile**  string | Private key for the client certificate. |
| **ssl_pem_passphrase**  aliases: tlsCertificateKeyFilePassword  string | Passphrase to decrypt encrypted private keys. |
| **strict_compatibility**  boolean | Enforce strict requirements for pymongo and MongoDB software versions  Choices:   - `false` - `true` ← (default) |

## [Notes](mongodb_info_module.md#id4)

> **Note:**
>
> - Requires the pymongo Python package on the remote host, version 2.4.2+.

## [Examples](mongodb_info_module.md#id5)

```yaml+jinja
- name: Gather all supported information
  community.mongodb.mongodb_info:
    login_user: admin
    login_password: secret
  register: result

- name: Show gathered info
  debug:
    msg: '{{ result }}'

- name: Gather only information about databases and their total size
  community.mongodb.mongodb_info:
    login_user: admin
    login_password: secret
    filter: databases, total_size

- name: Gather all information except parameters
  community.mongodb.mongodb_info:
    login_user: admin
    login_password: secret
    filter: '!parameters'
```

## [Return Values](mongodb_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **databases**  dictionary | Database information.  Returned: always  Sample: `{"admin": {"empty": false, "sizeOnDisk": 245760}, "config": {"empty": false, "sizeOnDisk": 110592}}` |
| **general**  dictionary | General instance information.  Returned: always  Sample: `{"allocator": "tcmalloc", "bits": 64, "maxBsonObjectSize": 16777216, "storageEngines": ["biggie"], "version": "4.2.3"}` |
| **parameters**  dictionary | Server parameters information.  Returned: always  Sample: `{"maxOplogTruncationPointsAfterStartup": 100, "maxOplogTruncationPointsDuringStartup": 100, "maxSessions": 1000000}` |
| **roles**  dictionary | Role information.  Returned: always  Sample: `{"db": {"restore": {"inheritedRoles": [], "isBuiltin": true, "roles": []}}}` |
| **total_size**  integer | Total size of all databases in bytes.  Returned: always  Sample: `397312` |
| **users**  dictionary | User information.  Returned: always  Sample: `{"db": {"new_user": {"_id": "config.new_user", "mechanisms": ["SCRAM-SHA-1", "SCRAM-SHA-256"], "roles": []}}}` |

### Authors

- Andrew Klychkov (@Andersson007)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.mongodb)
[Repository (Sources)](https://github.com/ansible-collections/community.mongodb)
