---
collection: ansible
version: "8"
title: "community.mongodb.mongodb_shard module – Add or remove shards from a MongoDB Cluster"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/mongodb/mongodb_shard_module.html
fetched_at: 2026-07-28T01:54:01+00:00
---
# community.mongodb.mongodb_shard module – Add or remove shards from a MongoDB Cluster

> **Note:**
>
> This module is part of the [community.mongodb collection](https://galaxy.ansible.com/ui/repo/published/community/mongodb/) (version 1.6.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.mongodb`.
> You need further requirements to be able to use this module,
> see [Requirements](mongodb_shard_module.md#ansible-collections-community-mongodb-mongodb-shard-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mongodb.mongodb_shard`.

New in community.mongodb 1.0.0

- [Synopsis](mongodb_shard_module.md#synopsis)
- [Requirements](mongodb_shard_module.md#requirements)
- [Parameters](mongodb_shard_module.md#parameters)
- [Notes](mongodb_shard_module.md#notes)
- [Examples](mongodb_shard_module.md#examples)
- [Return Values](mongodb_shard_module.md#return-values)

## [Synopsis](mongodb_shard_module.md#id1)

- Add or remove shards from a MongoDB Cluster.

## [Requirements](mongodb_shard_module.md#id2)

The below requirements are needed on the host that executes this module.

- pymongo

## [Parameters](mongodb_shard_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **atlas_auth**  boolean | Authentication path intended for MongoDB Atlas Instances  **Choices:**   - `false` ← (default) - `true` |
| **auth_mechanism**  string | Authentication type.  **Choices:**   - `"SCRAM-SHA-256"` - `"SCRAM-SHA-1"` - `"MONGODB-X509"` - `"GSSAPI"` - `"PLAIN"` |
| **connection_options**  list / elements=any | Additional connection options.  Supply as a list of dicts or strings containing key value pairs seperated with ‘=’. |
| **login_database**  string | The database where login credentials are stored.  **Default:** `"admin"` |
| **login_host**  string | The host running MongoDB instance to login to.  **Default:** `"localhost"` |
| **login_password**  string | The password used to authenticate with.  Required when *login_user* is specified. |
| **login_port**  integer | The MongoDB server port to login to.  **Default:** `27017` |
| **login_user**  string | The MongoDB user to login with.  Required when *login_password* is specified. |
| **mongos_process**  string | Provide a custom name for the mongos process you are connecting to.  Most users can ignore this setting.  **Default:** `"mongos"` |
| **shard**  string / required | The shard connection string.  Should be supplied in the form <replicaset>/host:port as detailed in https://docs.mongodb.com/manual/tutorial/add-shards-to-shard-cluster/.  For example rs0/example1.mongodb.com:27017. |
| **sharded_databases**  any | Enable sharding on the listed database.  Can be supplied as a string or a list of strings.  Sharding cannot be disabled on a database.  Starting in MongoDB 6.0, the enableSharding command is no longer required to shard a collection and this parameter is ignored. |
| **ssl**  aliases: tls  boolean | Whether to use an SSL connection when connecting to the database.  **Choices:**   - `false` ← (default) - `true` |
| **ssl_ca_certs**  aliases: tlsCAFile  string | The ssl_ca_certs option takes a path to a CA file. |
| **ssl_cert_reqs**  aliases: tlsAllowInvalidCertificates  string | Specifies whether a certificate is required from the other side of the connection, and whether it will be validated if provided.  **Choices:**   - `"CERT_NONE"` - `"CERT_OPTIONAL"` - `"CERT_REQUIRED"` ← (default) |
| **ssl_certfile**  aliases: tlsCertificateKeyFile  string | Present a client certificate using the ssl_certfile option. |
| **ssl_crlfile**  string | The ssl_crlfile option takes a path to a CRL file. |
| **ssl_keyfile**  string | Private key for the client certificate. |
| **ssl_pem_passphrase**  aliases: tlsCertificateKeyFilePassword  string | Passphrase to decrypt encrypted private keys. |
| **state**  string | Whether the shard should be present or absent from the Cluster.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **strict_compatibility**  boolean | Enforce strict requirements for pymongo and MongoDB software versions  **Choices:**   - `false` - `true` ← (default) |

## [Notes](mongodb_shard_module.md#id4)

> **Note:**
>
> - Requires the pymongo Python package on the remote host, version 2.4.2+.

## [Examples](mongodb_shard_module.md#id5)

```yaml+jinja
- name: Add a replicaset shard named rs1 with a member running on port 27018 on mongodb0.example.net
  community.mongodb.mongodb_shard:
    login_user: admin
    login_password: admin
    shard: "rs1/mongodb0.example.net:27018"
    state: present

- name: Add a standalone mongod shard running on port 27018 of mongodb0.example.net
  community.mongodb.mongodb_shard:
    login_user: admin
    login_password: admin
    shard: "mongodb0.example.net:27018"
    state: present

- name: To remove a shard called 'rs1'
  community.mongodb.mongodb_shard:
    login_user: admin
    login_password: admin
    shard: rs1
    state: absent

# Single node shard running on localhost
- name: Ensure shard rs0 exists
  community.mongodb.mongodb_shard:
    login_user: admin
    login_password: secret
    shard: "rs0/localhost:3001"
    state: present

# Single node shard running on localhost
- name: Ensure shard rs1 exists
  community.mongodb.mongodb_shard:
    login_user: admin
    login_password: secret
    shard: "rs1/localhost:3002"
    state: present

# Enable sharding on a few databases when creating the shard
- name: To remove a shard called 'rs1'
  community.mongodb.mongodb_shard:
    login_user: admin
    login_password: admin
    shard: rs1
    sharded_databases:
      - db1
      - db2
    state: present
```

## [Return Values](mongodb_shard_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **mongodb_shard**  string | The name of the shard to create.  **Returned:** success |
| **sharded_enabled**  list / elements=string | Databases that have had sharding enabled during module execution.  **Returned:** success when sharding is enabled |

### Authors

- Rhys Campbell (@rhysmeister)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.mongodb)
- [Repository (Sources)](https://github.com/ansible-collections/community.mongodb)
