---
collection: ansible
version: "6"
title: "community.mongodb.mongodb_replicaset module – Initialises a MongoDB replicaset."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/mongodb/mongodb_replicaset_module.html
fetched_at: 2026-07-27T17:16:06+00:00
---
# community.mongodb.mongodb_replicaset module – Initialises a MongoDB replicaset.

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
> see [Requirements](mongodb_replicaset_module.md#ansible-collections-community-mongodb-mongodb-replicaset-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mongodb.mongodb_replicaset`.

New in community.mongodb 1.0.0

- [Synopsis](mongodb_replicaset_module.md#synopsis)
- [Requirements](mongodb_replicaset_module.md#requirements)
- [Parameters](mongodb_replicaset_module.md#parameters)
- [Notes](mongodb_replicaset_module.md#notes)
- [Examples](mongodb_replicaset_module.md#examples)
- [Return Values](mongodb_replicaset_module.md#return-values)

## [Synopsis](mongodb_replicaset_module.md#id1)

- Initialises a MongoDB replicaset in a new deployment.
- Validates the replicaset name for existing deployments.
- Advanced replicaset member configuration possible (see examples).

## [Requirements](mongodb_replicaset_module.md#id2)

The below requirements are needed on the host that executes this module.

- pymongo

## [Parameters](mongodb_replicaset_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **arbiter_at_index**  integer | Identifies the position of the member in the array that is an arbiter. |
| **auth_mechanism**  string | Authentication type.  Choices:   - `"SCRAM-SHA-256"` - `"SCRAM-SHA-1"` - `"MONGODB-X509"` - `"GSSAPI"` - `"PLAIN"` |
| **chaining_allowed**  boolean | When *settings.chaining_allowed=true*, the replicaset allows secondary members to replicate from other secondary members.  When *settings.chaining_allowed=false*, secondaries can replicate only from the primary.  Choices:   - `false` - `true` ← (default) |
| **cluster_cmd**  string | Command the module should use to obtain information about the MongoDB node we are connecting to.  Choices:   - `"isMaster"` - `"hello"` ← (default) |
| **connection_options**  list / elements=any | Additional connection options.  Supply as a list of dicts or strings containing key value pairs seperated with ‘=’. |
| **debug**  boolean | Add additonal info for debug.  Choices:   - `false` ← (default) - `true` |
| **election_timeout_millis**  integer | The time limit in milliseconds for detecting when a replicaset’s primary is unreachable.  Default: `10000` |
| **force**  boolean | Only relevant when reconfigure = true.  Specify true to force the available replica set members to accept the new configuration.  Force reconfiguration can result in unexpected or undesired behavior, including rollback of “majority” committed writes.  Choices:   - `false` ← (default) - `true` |
| **heartbeat_timeout_secs**  integer | Number of seconds that the replicaset members wait for a successful heartbeat from each other.  If a member does not respond in time, other members mark the delinquent member as inaccessible.  The setting only applies when using *protocol_version=0*. When using *protocol_version=1* the relevant setting is *settings.election_timeout_millis*.  Default: `10` |
| **login_database**  string | The database where login credentials are stored.  Default: `"admin"` |
| **login_host**  string | The host running MongoDB instance to login to.  Default: `"localhost"` |
| **login_password**  string | The password used to authenticate with.  Required when *login_user* is specified. |
| **login_port**  integer | The MongoDB server port to login to.  Default: `27017` |
| **login_user**  string | The MongoDB user to login with.  Required when *login_password* is specified. |
| **max_time_ms**  integer | Specifies a cumulative time limit in milliseconds for processing the replicaset reconfiguration. |
| **members**  list / elements=any | Yaml list consisting of the replicaset members.  Csv string will also be accepted i.e. mongodb1:27017,mongodb2:27017,mongodb3:27017.  A dictionary can also be used to specify advanced replicaset member options.  If a port number is not provided then 27017 is assumed. |
| **protocol_version**  integer | Version of the replicaset election protocol.  Choices:   - `0` - `1` ← (default) |
| **reconfigure**  boolean | This feature is currently experimental. Please test your scenario thoroughly.  Consult the integration test file for supported scenarios - \ [Integration tests](<https://github.com/ansible-collections/community.mongodb/tree/master/tests/integration/targets/mongodb_replicaset/tasks>). \ See files prefixed with 330.  Whether to perform replicaset reconfiguration actions.  Only relevant when the replicaset already exists.  Only one member should be removed or added per invocation.  Members should be specific as either all strings or all dicts when reconfiguring.  Currently no support for replicaset settings document changes.  Choices:   - `false` ← (default) - `true` |
| **replica_set**  string | Replicaset name.  Default: `"rs0"` |
| **ssl**  aliases: tls  boolean | Whether to use an SSL connection when connecting to the database.  Choices:   - `false` ← (default) - `true` |
| **ssl_ca_certs**  aliases: tlsCAFile  string | The ssl_ca_certs option takes a path to a CA file. |
| **ssl_cert_reqs**  aliases: tlsAllowInvalidCertificates  string | Specifies whether a certificate is required from the other side of the connection, and whether it will be validated if provided.  Choices:   - `"CERT_NONE"` - `"CERT_OPTIONAL"` - `"CERT_REQUIRED"` ← (default) |
| **ssl_certfile**  aliases: tlsCertificateKeyFile  string | Present a client certificate using the ssl_certfile option. |
| **ssl_crlfile**  string | The ssl_crlfile option takes a path to a CRL file. |
| **ssl_keyfile**  string | Private key for the client certificate. |
| **ssl_pem_passphrase**  aliases: tlsCertificateKeyFilePassword  string | Passphrase to decrypt encrypted private keys. |
| **strict_compatibility**  boolean | Enforce strict requirements for pymongo and MongoDB software versions  Choices:   - `false` - `true` ← (default) |
| **validate**  boolean | Performs some basic validation on the provided replicaset config.  Choices:   - `false` - `true` ← (default) |

## [Notes](mongodb_replicaset_module.md#id4)

> **Note:**
>
> - Requires the pymongo Python package on the remote host, version 2.4.2+. This can be installed using pip or the OS package manager. @see <http://api.mongodb.org/python/current/installation.html>

## [Examples](mongodb_replicaset_module.md#id5)

```yaml+jinja
# Create a replicaset called 'rs0' with the 3 provided members
- name: Ensure replicaset rs0 exists
  community.mongodb.mongodb_replicaset:
    login_host: localhost
    login_user: admin
    login_password: admin
    replica_set: rs0
    members:
    - mongodb1:27017
    - mongodb2:27017
    - mongodb3:27017
  when: groups.mongod.index(inventory_hostname) == 0

# Create two single-node replicasets on the localhost for testing
- name: Ensure replicaset rs0 exists
  community.mongodb.mongodb_replicaset:
    login_host: localhost
    login_port: 3001
    login_user: admin
    login_password: secret
    login_database: admin
    replica_set: rs0
    members: localhost:3001
    validate: no

- name: Ensure replicaset rs1 exists
  community.mongodb.mongodb_replicaset:
    login_host: localhost
    login_port: 3002
    login_user: admin
    login_password: secret
    login_database: admin
    replica_set: rs1
    members: localhost:3002
    validate: no

- name: Create a replicaset and use a custom priority for each member
  community.mongodb.mongodb_replicaset:
    login_host: localhost
    login_user: admin
    login_password: admin
    replica_set: rs0
    members:
    - host: "localhost:3001"
      priority: 1
    - host: "localhost:3002"
      priority: 0.5
    - host: "localhost:3003"
      priority: 0.5
  when: groups.mongod.index(inventory_hostname) == 0

- name: Create replicaset rs1 with options and member tags
  community.mongodb.mongodb_replicaset:
    login_host: localhost
    login_port: 3001
    login_database: admin
    replica_set: rs1
    members:
    - host: "localhost:3001"
      priority: 1
      tags:
        dc: "east"
        usage: "production"
    - host: "localhost:3002"
      priority: 1
      tags:
        dc: "east"
        usage: "production"
    - host: "localhost:3003"
      priority: 0
      hidden: true
      slaveDelay: 3600
      tags:
        dc: "west"
        usage: "reporting"

- name: Replicaset with one arbiter node (mongodb3 - index is zero-based)
  community.mongodb.mongodb_replicaset:
    login_user: admin
    login_password: admin
    replica_set: rs0
    members:
      - mongodb1:27017
      - mongodb2:27017
      - mongodb3:27017
    arbiter_at_index: 2
  when: groups.mongod.index(inventory_hostname) == 0

- name: Add a new member to a replicaset - Safe for pre-5.0 consult documentation - https://docs.mongodb.com/manual/tutorial/expand-replica-set/
  block:
    - name: Create replicaset with module - with dicts
      community.mongodb.mongodb_replicaset:
        replica_set: "rs0"
        members:
           - host: localhost:3001
           - host: localhost:3002
           - host: localhost:3003

    - name: Wait for the replicaset to stabilise
      community.mongodb.mongodb_status:
        replica_set: "rs0"
        poll: 5
        interval: 10

    - name: Remove a member from the replicaset
      community.mongodb.mongodb_replicaset:
        replica_set: "rs0"
        reconfigure: yes
        members:
           - host: localhost:3001
           - host: localhost:3002

    - name: Wait for the replicaset to stabilise after member removal
      community.mongodb.mongodb_status:
        replica_set: "rs0"
        validate: minimal
        poll: 5
        interval: 10

    - name: Add a member to the replicaset
      community.mongodb.mongodb_replicaset:
        replica_set: "rs0"
        reconfigure: yes
        members:
           - host: localhost:3001
           - host: localhost:3002
           - host: localhost:3004
             hidden: true
             votes: 0
             priority: 0

    - name: Wait for the replicaset to stabilise after member addition
      community.mongodb.mongodb_status:
        replica_set: "rs0"
        validate: minimal
        poll: 5
        interval: 30

    - name: Reconfigure the replicaset - Make member 3004 a normal voting member
      community.mongodb.mongodb_replicaset:
        replica_set: "rs0"
        reconfigure: yes
        members:
           - host: localhost:3001
           - host: localhost:3002
           - host: localhost:3004
             hidden: false
             votes: 1
             priority: 1

    - name: Wait for the replicaset to stabilise
      community.mongodb.mongodb_status:
        replica_set: "rs0"
        poll: 5
        interval: 30
```

## [Return Values](mongodb_replicaset_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **mongodb_replicaset**  string | The name of the replicaset that has been created.  Returned: success |
| **reconfigure**  boolean | If a replicaset reconfiguration occured.  Returned: On rpelicaset reconfiguration |

### Authors

- Rhys Campbell (@rhysmeister)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.mongodb)
[Repository (Sources)](https://github.com/ansible-collections/community.mongodb)
