---
collection: ansible
version: "6"
title: "community.mongodb.mongodb_index module – Creates or drops indexes on MongoDB collections."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/mongodb/mongodb_index_module.html
fetched_at: 2026-07-27T17:16:02+00:00
---
# community.mongodb.mongodb_index module – Creates or drops indexes on MongoDB collections.

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
> see [Requirements](mongodb_index_module.md#ansible-collections-community-mongodb-mongodb-index-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mongodb.mongodb_index`.

New in community.mongodb 1.0.0

- [Synopsis](mongodb_index_module.md#synopsis)
- [Requirements](mongodb_index_module.md#requirements)
- [Parameters](mongodb_index_module.md#parameters)
- [Notes](mongodb_index_module.md#notes)
- [Examples](mongodb_index_module.md#examples)
- [Return Values](mongodb_index_module.md#return-values)

## [Synopsis](mongodb_index_module.md#id1)

- Creates or drops indexes on MongoDB collections.
- Supports multiple index options, i.e. unique, sparse and partial.
- Validates existence of indexes by name only.

## [Requirements](mongodb_index_module.md#id2)

The below requirements are needed on the host that executes this module.

- pymongo

## [Parameters](mongodb_index_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_mechanism**  string | Authentication type.  Choices:   - `"SCRAM-SHA-256"` - `"SCRAM-SHA-1"` - `"MONGODB-X509"` - `"GSSAPI"` - `"PLAIN"` |
| **connection_options**  list / elements=any | Additional connection options.  Supply as a list of dicts or strings containing key value pairs seperated with ‘=’. |
| **indexes**  list / elements=any / required | List of indexes to create or drop |
| **login_database**  string | The database where login credentials are stored.  Default: `"admin"` |
| **login_host**  string | The host running MongoDB instance to login to.  Default: `"localhost"` |
| **login_password**  string | The password used to authenticate with.  Required when *login_user* is specified. |
| **login_port**  integer | The MongoDB server port to login to.  Default: `27017` |
| **login_user**  string | The MongoDB user to login with.  Required when *login_password* is specified. |
| **replica_set**  string | Replica set to connect to (automatically connects to primary for writes). |
| **ssl**  aliases: tls  boolean | Whether to use an SSL connection when connecting to the database.  Choices:   - `false` ← (default) - `true` |
| **ssl_ca_certs**  aliases: tlsCAFile  string | The ssl_ca_certs option takes a path to a CA file. |
| **ssl_cert_reqs**  aliases: tlsAllowInvalidCertificates  string | Specifies whether a certificate is required from the other side of the connection, and whether it will be validated if provided.  Choices:   - `"CERT_NONE"` - `"CERT_OPTIONAL"` - `"CERT_REQUIRED"` ← (default) |
| **ssl_certfile**  aliases: tlsCertificateKeyFile  string | Present a client certificate using the ssl_certfile option. |
| **ssl_crlfile**  string | The ssl_crlfile option takes a path to a CRL file. |
| **ssl_keyfile**  string | Private key for the client certificate. |
| **ssl_pem_passphrase**  aliases: tlsCertificateKeyFilePassword  string | Passphrase to decrypt encrypted private keys. |
| **strict_compatibility**  boolean | Enforce strict requirements for pymongo and MongoDB software versions  Choices:   - `false` - `true` ← (default) |

## [Notes](mongodb_index_module.md#id4)

> **Note:**
>
> - Requires the pymongo Python package on the remote host, version 2.4.2+.

## [Examples](mongodb_index_module.md#id5)

```yaml+jinja
- name: Create a single index on a collection
  community.mongodb.mongodb_index:
    login_user: admin
    login_password: secret
    indexes:
      - database: mydb
        collection: test
        keys:
          - username: 1
            last_login: -1
        options:
          name: myindex
        state: present

- name: Drop an index on a collection
  community.mongodb.mongodb_index:
    login_user: admin
    login_password: secret
    indexes:
      - database: mydb
        collection: test
        options:
          name: myindex
        state: absent

- name: Create multiple indexes
  community.mongodb.mongodb_index:
    login_user: admin
    login_password: secret
    indexes:
      - database: mydb
        collection: test
        keys:
          - username: 1
            last_login: -1
        options:
          name: myindex
        state: present
      - database: mydb
        collection: test
        keys:
          - email: 1
            last_login: -1
        options:
          name: myindex2
        state: present

- name: Add a unique index
  community.mongodb.mongodb_index:
    login_port: 27017
    login_user: admin
    login_password: secret
    login_database: "admin"
    indexes:
      - database: "test"
        collection: "rhys"
        keys:
          username: 1
        options:
          name: myuniqueindex
          unique: true
        state: present

- name: Add a ttl index
  community.mongodb.mongodb_index:
    login_port: 27017
    login_user: admin
    login_password: secret
    login_database: "admin"
    indexes:
      - database: "test"
        collection: "rhys"
        keys:
          created: 1
        options:
          name: myttlindex
          expireAfterSeconds: 3600
        state: present

- name: Add a sparse index
  community.mongodb.mongodb_index:
    login_port: 27017
    login_user: admin
    login_password: secret
    login_database: "admin"
    indexes:
      - database: "test"
        collection: "rhys"
        keys:
          last_login: -1
        options:
          name: mysparseindex
          sparse: true
        state: present

- name: Add a partial index
  community.mongodb.mongodb_index:
    login_port: 27017
    login_user: admin
    login_password: secret
    login_database: "admin"
    indexes:
      - database: "test"
        collection: "rhys"
        keys:
          last_login: -1
        options:
          name: mypartialindex
          partialFilterExpression:
            rating:
              $gt: 5
        state: present

- name: Add a index in the background (background option is deprecated from 4.2+)
  community.mongodb.mongodb_index:
    login_port: 27017
    login_user: admin
    login_password: secret
    login_database: "admin"
    indexes:
      - database: "test"
        collection: "rhys"
        options:
          name: idxbackground
        keys:
          username: -1
        backgroud: true
        state: present

- name: Check creating 5 index all with multiple options specified
  community.mongodb.mongodb_index:
    login_port: 27017
    login_user: admin
    login_password: secret
    login_database: "admin"
    indexes:
      - database: "test"
        collection: "indextest"
        options:
          name: "idx_unq_username"
          unique: true
        keys:
          username: -1
        state: present
      - database: "test"
        collection: "indextest"
        options:
          name: "idx_last_login"
          sparse: true
        keys:
          last_login: -1
        state: present
      - database: "test"
        collection: "indextest"
        options:
          name: "myindex"
        keys:
          first_name: 1
          last_name: -1
          city: 1
        state: present
      - database: "test"
        collection: partialtest
        options:
          name: "idx_partialtest"
          partialFilterExpression:
            rating:
              $gt: 5
        keys:
          rating: -1
          title: 1
        state: present
      - database: "test"
        collection: "wideindex"
        options:
          name: "mywideindex"
        keys:
          email: -1
          username: 1
          first_name: 1
          last_name: 1
          dob: -1
          city: 1
          last_login: -1
          review_count: 1
          rating_count: 1
          last_post: -1
        state: present
```

## [Return Values](mongodb_index_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Indicates the module has changed something.  Returned: When the module has changed something. |
| **failed**  boolean | Indicates the module has failed.  Returned: When the module has encountered an error. |
| **indexes_created**  list / elements=string | List of indexes created.  Returned: always  Sample: `["myindex", "myindex2"]` |
| **indexes_dropped**  list / elements=string | List of indexes dropped.  Returned: always  Sample: `["myindex", "myindex2"]` |

### Authors

- Rhys Campbell (@rhysmeister)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.mongodb)
[Repository (Sources)](https://github.com/ansible-collections/community.mongodb)
