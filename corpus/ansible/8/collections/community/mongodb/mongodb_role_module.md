---
collection: ansible
version: "8"
title: "community.mongodb.mongodb_role module – Adds or removes a role from a MongoDB database"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/mongodb/mongodb_role_module.html
fetched_at: 2026-07-28T01:54:00+00:00
---
# community.mongodb.mongodb_role module – Adds or removes a role from a MongoDB database

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
> see [Requirements](mongodb_role_module.md#ansible-collections-community-mongodb-mongodb-role-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mongodb.mongodb_role`.

New in community.mongodb 1.5.0

- [Synopsis](mongodb_role_module.md#synopsis)
- [Requirements](mongodb_role_module.md#requirements)
- [Parameters](mongodb_role_module.md#parameters)
- [Notes](mongodb_role_module.md#notes)
- [Examples](mongodb_role_module.md#examples)
- [Return Values](mongodb_role_module.md#return-values)

## [Synopsis](mongodb_role_module.md#id1)

- Adds or removes a role from a MongoDB database.
- For further information on the required format for the privileges, authenticationRestriction or roles parameters, see the MongoDB Documentation <https://www.mongodb.com/docs/manual/reference/command/createRole/>

## [Requirements](mongodb_role_module.md#id2)

The below requirements are needed on the host that executes this module.

- pymongo

## [Parameters](mongodb_role_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **atlas_auth**  boolean | Authentication path intended for MongoDB Atlas Instances  **Choices:**   - `false` ← (default) - `true` |
| **auth_mechanism**  string | Authentication type.  **Choices:**   - `"SCRAM-SHA-256"` - `"SCRAM-SHA-1"` - `"MONGODB-X509"` - `"GSSAPI"` - `"PLAIN"` |
| **authenticationRestrictions**  list / elements=any | The authentication restrictions the server enforces on the role. Specifies a list of IP addresses and CIDR ranges users granted this role are allowed to connect to and/or which they can connect from. Provide a list of dictionaries with the following fields: clientSource (list), serverAddress (list). Provide an empty list if you don’t want to use the field.  **Default:** `[]` |
| **connection_options**  list / elements=any | Additional connection options.  Supply as a list of dicts or strings containing key value pairs seperated with ‘=’. |
| **database**  aliases: db  string / required | The name of the database to add/remove the role from. |
| **debug**  boolean | Enable extra debugging output.  **Choices:**   - `false` ← (default) - `true` |
| **login_database**  string | The database where login credentials are stored.  **Default:** `"admin"` |
| **login_host**  string | The host running MongoDB instance to login to.  **Default:** `"localhost"` |
| **login_password**  string | The password used to authenticate with.  Required when *login_user* is specified. |
| **login_port**  integer | The MongoDB server port to login to.  **Default:** `27017` |
| **login_user**  string | The MongoDB user to login with.  Required when *login_password* is specified. |
| **name**  aliases: user  string / required | The name of the role to add or remove. |
| **privileges**  list / elements=any | The privileges to grant the role. A privilege consists of a resource and permitted actions.  **Default:** `[]` |
| **replica_set**  string | Replica set to connect to (automatically connects to primary for writes). |
| **roles**  list / elements=any | The database user roles should be provided as a dictionary with the db and role keys.  **Default:** `[]` |
| **ssl**  aliases: tls  boolean | Whether to use an SSL connection when connecting to the database.  **Choices:**   - `false` ← (default) - `true` |
| **ssl_ca_certs**  aliases: tlsCAFile  string | The ssl_ca_certs option takes a path to a CA file. |
| **ssl_cert_reqs**  aliases: tlsAllowInvalidCertificates  string | Specifies whether a certificate is required from the other side of the connection, and whether it will be validated if provided.  **Choices:**   - `"CERT_NONE"` - `"CERT_OPTIONAL"` - `"CERT_REQUIRED"` ← (default) |
| **ssl_certfile**  aliases: tlsCertificateKeyFile  string | Present a client certificate using the ssl_certfile option. |
| **ssl_crlfile**  string | The ssl_crlfile option takes a path to a CRL file. |
| **ssl_keyfile**  string | Private key for the client certificate. |
| **ssl_pem_passphrase**  aliases: tlsCertificateKeyFilePassword  string | Passphrase to decrypt encrypted private keys. |
| **state**  string | The database user state.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **strict_compatibility**  boolean | Enforce strict requirements for pymongo and MongoDB software versions  **Choices:**   - `false` - `true` ← (default) |

## [Notes](mongodb_role_module.md#id4)

> **Note:**
>
> - Requires the pymongo Python package on the remote host, version 2.4.2+. This can be installed using pip or the OS package manager. Newer mongo server versions require newer pymongo versions. @see <http://api.mongodb.org/python/current/installation.html>

## [Examples](mongodb_role_module.md#id5)

```yaml+jinja
- name: Create sales role
  community.mongodb.mongodb_role:
    name: sales
    database: salesdb
    privileges:
      - resource:
          db: salesdb
          collection: ""
        actions:
          - find
    state: present

- name: Create ClusterAdmin Role
  community.mongodb.mongodb_role:
    name: myClusterwideAdmin
    database: admin
    privileges:
      - resource:
          cluster: true
        actions:
          - addShard
      - resource:
          db: config
          collection: ""
        actions:
          - find
          - update
          - insert
          - remove
      - resource:
          db: "users"
          collection: "usersCollection"
        actions:
          - update
          - insert
          - remove
      - resource:
          db: ""
          collection: ""
        actions:
          - find
    roles:
      - role: "read"
        db: "admin"
    state: present

- name: Create ClusterAdmin Role with a login only from 127.0.0.1 restriction
  community.mongodb.mongodb_role:
    name: myClusterwideAdmin
    database: admin
    privileges:
      - resource:
          cluster: true
        actions:
          - addShard
      - resource:
          db: config
          collection: ""
        actions:
          - find
          - update
          - insert
      - resource:
          db: "users"
          collection: "usersCollection"
        actions:
          - update
          - insert
          - remove
      - resource:
          db: ""
          collection: ""
        actions:
          - find
    roles:
      - role: "read"
        db: "admin"
      - role: "read"
        db: "mynewdb"
    authenticationRestrictions:
      - clientSource:
          - "127.0.0.1"
        serverAddress: []
    state: present

- name: Delete sales role
  community.mongodb.mongodb_role:
    name: sales
    database: "salesdb"
    state: absent

- name: Delete myClusterwideAdmin role
  community.mongodb.mongodb_role:
    name: myClusterwideAdmin
    database: admin
    state: absent
```

## [Return Values](mongodb_role_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **user**  string | The name of the role to add or remove.  **Returned:** success |

### Authors

- Rhys Campbell (@rhysmeister)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.mongodb)
- [Repository (Sources)](https://github.com/ansible-collections/community.mongodb)
