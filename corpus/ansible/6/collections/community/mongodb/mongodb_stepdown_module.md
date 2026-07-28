---
collection: ansible
version: "6"
title: "community.mongodb.mongodb_stepdown module – Step down the MongoDB node from a PRIMARY state."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/mongodb/mongodb_stepdown_module.html
fetched_at: 2026-07-27T17:16:12+00:00
---
# community.mongodb.mongodb_stepdown module – Step down the MongoDB node from a PRIMARY state.

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
> see [Requirements](mongodb_stepdown_module.md#ansible-collections-community-mongodb-mongodb-stepdown-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mongodb.mongodb_stepdown`.

New in community.mongodb 1.0.0

- [Synopsis](mongodb_stepdown_module.md#synopsis)
- [Requirements](mongodb_stepdown_module.md#requirements)
- [Parameters](mongodb_stepdown_module.md#parameters)
- [Notes](mongodb_stepdown_module.md#notes)
- [Examples](mongodb_stepdown_module.md#examples)
- [Return Values](mongodb_stepdown_module.md#return-values)

## [Synopsis](mongodb_stepdown_module.md#id1)

- Step down the MongoDB node from the PRIMARY state if it has that status. Returns OK immediately if the member is already in the SECONDARY or ARBITER states. Will wait until a timeout for the member state to reach SECONDARY or PRIMARY, if the member state is currently STARTUP, RECOVERING, STARTUP2 or ROLLBACK, before taking any needed action.

## [Requirements](mongodb_stepdown_module.md#id2)

The below requirements are needed on the host that executes this module.

- pymongo

## [Parameters](mongodb_stepdown_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_mechanism**  string | Authentication type.  Choices:   - `"SCRAM-SHA-256"` - `"SCRAM-SHA-1"` - `"MONGODB-X509"` - `"GSSAPI"` - `"PLAIN"` |
| **connection_options**  list / elements=any | Additional connection options.  Supply as a list of dicts or strings containing key value pairs seperated with ‘=’. |
| **force**  boolean | Optional. A boolean that determines whether the primary steps down if no electable and up-to-date secondary exists within the wait period.  Choices:   - `false` ← (default) - `true` |
| **interval**  integer | The number of seconds to wait between poll executions.  Default: `30` |
| **login_database**  string | The database where login credentials are stored.  Default: `"admin"` |
| **login_host**  string | The host running MongoDB instance to login to.  Default: `"localhost"` |
| **login_password**  string | The password used to authenticate with.  Required when *login_user* is specified. |
| **login_port**  integer | The MongoDB server port to login to.  Default: `27017` |
| **login_user**  string | The MongoDB user to login with.  Required when *login_password* is specified. |
| **poll**  integer | The maximum number of times query for the member status.  Default: `1` |
| **secondary_catch_up**  integer | The secondaryCatchUpPeriodSecs parameter for the stepDown command.  The number of seconds that mongod will wait for an electable secondary to catch up to the primary.  Default: `10` |
| **ssl**  aliases: tls  boolean | Whether to use an SSL connection when connecting to the database.  Choices:   - `false` ← (default) - `true` |
| **ssl_ca_certs**  aliases: tlsCAFile  string | The ssl_ca_certs option takes a path to a CA file. |
| **ssl_cert_reqs**  aliases: tlsAllowInvalidCertificates  string | Specifies whether a certificate is required from the other side of the connection, and whether it will be validated if provided.  Choices:   - `"CERT_NONE"` - `"CERT_OPTIONAL"` - `"CERT_REQUIRED"` ← (default) |
| **ssl_certfile**  aliases: tlsCertificateKeyFile  string | Present a client certificate using the ssl_certfile option. |
| **ssl_crlfile**  string | The ssl_crlfile option takes a path to a CRL file. |
| **ssl_keyfile**  string | Private key for the client certificate. |
| **ssl_pem_passphrase**  aliases: tlsCertificateKeyFilePassword  string | Passphrase to decrypt encrypted private keys. |
| **stepdown_seconds**  integer | The number of seconds to step down the primary, during which time the stepdown member is ineligible for becoming primary.  Default: `60` |
| **strict_compatibility**  boolean | Enforce strict requirements for pymongo and MongoDB software versions  Choices:   - `false` - `true` ← (default) |

## [Notes](mongodb_stepdown_module.md#id4)

> **Note:**
>
> - Requires the pymongo Python package on the remote host, version 2.4.2+. This can be installed using pip or the OS package manager. @see <http://api.mongodb.org/python/current/installation.html>

## [Examples](mongodb_stepdown_module.md#id5)

```yaml+jinja
- name: Step down the current MongoDB member
  community.mongodb.mongodb_stepdown:
    login_user: admin
    login_password: secret

- name: Step down the current MongoDB member, poll a maximum of 5 times if member state is recovering
  community.mongodb.mongodb_stepdown:
    login_user: admin
    login_password: secret
    poll: 5
    interval: 10
```

## [Return Values](mongodb_stepdown_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed**  boolean | If the module had failed or not.  Returned: always |
| **iteration**  integer | Number of times the module has queried the replicaset status.  Returned: always |
| **msg**  string | Status message.  Returned: always |

### Authors

- Rhys Campbell (@rhysmeister)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.mongodb)
[Repository (Sources)](https://github.com/ansible-collections/community.mongodb)
