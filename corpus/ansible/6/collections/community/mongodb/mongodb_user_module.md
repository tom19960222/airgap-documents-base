---
collection: ansible
version: "6"
title: "community.mongodb.mongodb_user module – Adds or removes a user from a MongoDB database"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/mongodb/mongodb_user_module.html
fetched_at: 2026-07-27T17:16:13+00:00
---
# community.mongodb.mongodb_user module – Adds or removes a user from a MongoDB database

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
> see [Requirements](mongodb_user_module.md#ansible-collections-community-mongodb-mongodb-user-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mongodb.mongodb_user`.

New in community.mongodb 1.0.0

- [Synopsis](mongodb_user_module.md#synopsis)
- [Requirements](mongodb_user_module.md#requirements)
- [Parameters](mongodb_user_module.md#parameters)
- [Notes](mongodb_user_module.md#notes)
- [Examples](mongodb_user_module.md#examples)
- [Return Values](mongodb_user_module.md#return-values)

## [Synopsis](mongodb_user_module.md#id1)

- Adds or removes a user from a MongoDB database.

## [Requirements](mongodb_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- pymongo

## [Parameters](mongodb_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_mechanism**  string | Authentication type.  Choices:   - `"SCRAM-SHA-256"` - `"SCRAM-SHA-1"` - `"MONGODB-X509"` - `"GSSAPI"` - `"PLAIN"` |
| **connection_options**  list / elements=any | Additional connection options.  Supply as a list of dicts or strings containing key value pairs seperated with ‘=’. |
| **create_for_localhost_exception**  path | This is parmeter is only useful for handling special treatment around the localhost exception.  If `login_user` is defined, then the localhost exception is not active and this parameter has no effect.  If this file is NOT present (and `login_user` is not defined), then touch this file after successfully adding the user.  If this file is present (and `login_user` is not defined), then skip this task. |
| **database**  aliases: db  string / required | The name of the database to add/remove the user from. |
| **login_database**  string | The database where login credentials are stored.  Default: `"admin"` |
| **login_host**  string | The host running MongoDB instance to login to.  Default: `"localhost"` |
| **login_password**  string | The password used to authenticate with.  Required when *login_user* is specified. |
| **login_port**  integer | The MongoDB server port to login to.  Default: `27017` |
| **login_user**  string | The MongoDB user to login with.  Required when *login_password* is specified. |
| **name**  aliases: user  string / required | The name of the user to add or remove. |
| **password**  aliases: pass  string | The password to use for the user. |
| **replica_set**  string | Replica set to connect to (automatically connects to primary for writes). |
| **roles**  list / elements=any | The database user roles valid values could either be one or more of the following strings: ‘read’, ‘readWrite’, ‘dbAdmin’, ‘userAdmin’, ‘clusterAdmin’, ‘readAnyDatabase’, ‘readWriteAnyDatabase’, ‘userAdminAnyDatabase’, ‘dbAdminAnyDatabase’  Or the following dictionary ‘{ db: DATABASE_NAME, role: ROLE_NAME }’.  This param requires pymongo 2.5+. If it is a string, mongodb 2.4+ is also required. If it is a dictionary, mongo 2.6+ is required. |
| **ssl**  aliases: tls  boolean | Whether to use an SSL connection when connecting to the database.  Choices:   - `false` ← (default) - `true` |
| **ssl_ca_certs**  aliases: tlsCAFile  string | The ssl_ca_certs option takes a path to a CA file. |
| **ssl_cert_reqs**  aliases: tlsAllowInvalidCertificates  string | Specifies whether a certificate is required from the other side of the connection, and whether it will be validated if provided.  Choices:   - `"CERT_NONE"` - `"CERT_OPTIONAL"` - `"CERT_REQUIRED"` ← (default) |
| **ssl_certfile**  aliases: tlsCertificateKeyFile  string | Present a client certificate using the ssl_certfile option. |
| **ssl_crlfile**  string | The ssl_crlfile option takes a path to a CRL file. |
| **ssl_keyfile**  string | Private key for the client certificate. |
| **ssl_pem_passphrase**  aliases: tlsCertificateKeyFilePassword  string | Passphrase to decrypt encrypted private keys. |
| **state**  string | The database user state.  Choices:   - `"absent"` - `"present"` ← (default) |
| **strict_compatibility**  boolean | Enforce strict requirements for pymongo and MongoDB software versions  Choices:   - `false` - `true` ← (default) |
| **update_password**  string | `always` will always update passwords and cause the module to return changed.  `on_create` will only set the password for newly created users.  This must be `always` to use the localhost exception when adding the first admin user.  This option is effectively ignored when using x.509 certs. It is defaulted to ‘on_create’ to maintain a a specific module behaviour when the login_database is ‘$external’.  Choices:   - `"always"` ← (default) - `"on_create"` |

## [Notes](mongodb_user_module.md#id4)

> **Note:**
>
> - Requires the pymongo Python package on the remote host, version 2.4.2+. This can be installed using pip or the OS package manager. Newer mongo server versions require newer pymongo versions. @see <http://api.mongodb.org/python/current/installation.html>

## [Examples](mongodb_user_module.md#id5)

```yaml+jinja
- name: Create 'burgers' database user with name 'bob' and password '12345'.
  community.mongodb.mongodb_user:
    database: burgers
    name: bob
    password: 12345
    state: present

- name: Create a database user via SSL (MongoDB must be compiled with the SSL option and configured properly)
  community.mongodb.mongodb_user:
    database: burgers
    name: bob
    password: 12345
    state: present
    ssl: True

- name: Delete 'burgers' database user with name 'bob'.
  community.mongodb.mongodb_user:
    database: burgers
    name: bob
    state: absent

- name: Define more users with various specific roles (if not defined, no roles is assigned, and the user will be added via pre mongo 2.2 style)
  community.mongodb.mongodb_user:
    database: burgers
    name: ben
    password: 12345
    roles: read
    state: present

- name: Define roles
  community.mongodb.mongodb_user:
    database: burgers
    name: jim
    password: 12345
    roles: readWrite,dbAdmin,userAdmin
    state: present

- name: Define roles
  community.mongodb.mongodb_user:
    database: burgers
    name: joe
    password: 12345
    roles: readWriteAnyDatabase
    state: present

- name: Add a user to database in a replica set, the primary server is automatically discovered and written to
  community.mongodb.mongodb_user:
    database: burgers
    name: bob
    replica_set: belcher
    password: 12345
    roles: readWriteAnyDatabase
    state: present

# add a user 'oplog_reader' with read only access to the 'local' database on the replica_set 'belcher'. This is useful for oplog access (MONGO_OPLOG_URL).
# please notice the credentials must be added to the 'admin' database because the 'local' database is not synchronized and can't receive user credentials
# To login with such user, the connection string should be MONGO_OPLOG_URL="mongodb://oplog_reader:oplog_reader_password@server1,server2/local?authSource=admin"
# This syntax requires mongodb 2.6+ and pymongo 2.5+
- name: Roles as a dictionary
  community.mongodb.mongodb_user:
    login_user: root
    login_password: root_password
    database: admin
    user: oplog_reader
    password: oplog_reader_password
    state: present
    replica_set: belcher
    roles:
      - db: local
        role: read

- name: Adding a user with X.509 Member Authentication
  community.mongodb.mongodb_user:
    login_host: "mongodb-host.test"
    login_port: 27001
    login_database: "$external"
    database: "admin"
    name: "admin"
    password: "test"
    roles:
    - dbAdminAnyDatabase
    ssl: true
    ssl_ca_certs: "/tmp/ca.crt"
    ssl_certfile: "/tmp/tls.key" #cert and key in one file
    state: present
    auth_mechanism: "MONGODB-X509"
    connection_options:
     - "tlsAllowInvalidHostnames=true"
```

## [Return Values](mongodb_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **user**  string | The name of the user to add or remove.  Returned: success |

### Authors

- Elliott Foster (@elliotttf)
- Julien Thebault (@Lujeni)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.mongodb)
[Repository (Sources)](https://github.com/ansible-collections/community.mongodb)
