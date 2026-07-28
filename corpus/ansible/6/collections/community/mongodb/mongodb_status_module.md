---
collection: ansible
version: "6"
title: "community.mongodb.mongodb_status module – Validates the status of the replicaset."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/mongodb/mongodb_status_module.html
fetched_at: 2026-07-27T17:16:11+00:00
---
# community.mongodb.mongodb_status module – Validates the status of the replicaset.

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
> see [Requirements](mongodb_status_module.md#ansible-collections-community-mongodb-mongodb-status-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mongodb.mongodb_status`.

New in community.mongodb 1.0.0

- [Synopsis](mongodb_status_module.md#synopsis)
- [Requirements](mongodb_status_module.md#requirements)
- [Parameters](mongodb_status_module.md#parameters)
- [Notes](mongodb_status_module.md#notes)
- [Examples](mongodb_status_module.md#examples)
- [Return Values](mongodb_status_module.md#return-values)

## [Synopsis](mongodb_status_module.md#id1)

- Validates the status of the replicaset.
- The module expects all replicaset nodes to be PRIMARY, SECONDARY or ARBITER.
- Will wait until a timeout for the replicaset state to converge if required.
- Can also be used to lookup the current PRIMARY member (see examples).

## [Requirements](mongodb_status_module.md#id2)

The below requirements are needed on the host that executes this module.

- pymongo

## [Parameters](mongodb_status_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_mechanism**  string | Authentication type.  Choices:   - `"SCRAM-SHA-256"` - `"SCRAM-SHA-1"` - `"MONGODB-X509"` - `"GSSAPI"` - `"PLAIN"` |
| **connection_options**  list / elements=any | Additional connection options.  Supply as a list of dicts or strings containing key value pairs seperated with ‘=’. |
| **interval**  integer | The number of seconds to wait between polling executions.  Default: `30` |
| **login_database**  string | The database where login credentials are stored.  Default: `"admin"` |
| **login_host**  string | The host running MongoDB instance to login to.  Default: `"localhost"` |
| **login_password**  string | The password used to authenticate with.  Required when *login_user* is specified. |
| **login_port**  integer | The MongoDB server port to login to.  Default: `27017` |
| **login_user**  string | The MongoDB user to login with.  Required when *login_password* is specified. |
| **poll**  integer | The maximum number of times to query for the replicaset status before the set converges or we fail.  Default: `1` |
| **replica_set**  string | Replicaset name.  Default: `"rs0"` |
| **ssl**  aliases: tls  boolean | Whether to use an SSL connection when connecting to the database.  Choices:   - `false` ← (default) - `true` |
| **ssl_ca_certs**  aliases: tlsCAFile  string | The ssl_ca_certs option takes a path to a CA file. |
| **ssl_cert_reqs**  aliases: tlsAllowInvalidCertificates  string | Specifies whether a certificate is required from the other side of the connection, and whether it will be validated if provided.  Choices:   - `"CERT_NONE"` - `"CERT_OPTIONAL"` - `"CERT_REQUIRED"` ← (default) |
| **ssl_certfile**  aliases: tlsCertificateKeyFile  string | Present a client certificate using the ssl_certfile option. |
| **ssl_crlfile**  string | The ssl_crlfile option takes a path to a CRL file. |
| **ssl_keyfile**  string | Private key for the client certificate. |
| **ssl_pem_passphrase**  aliases: tlsCertificateKeyFilePassword  string | Passphrase to decrypt encrypted private keys. |
| **strict_compatibility**  boolean | Enforce strict requirements for pymongo and MongoDB software versions  Choices:   - `false` - `true` ← (default) |
| **validate**  string | The type of validate to perform on the replicaset.  default, Suitable for most purposes. Validate that there are an odd number of servers and one is PRIMARY and the remainder are in a SECONDARY or ARBITER state.  votes, Check the number of votes is odd and one is a PRIMARY and the remainder are in a SECONDARY or ARBITER state. Authentication is required here to get the replicaset configuration.  minimal, Just checks that one server is in a PRIMARY state with the remainder being SECONDARY or ARBITER.  Choices:   - `"default"` ← (default) - `"votes"` - `"minimal"` |

## [Notes](mongodb_status_module.md#id4)

> **Note:**
>
> - Requires the pymongo Python package on the remote host, version 2.4.2+. This can be installed using pip or the OS package manager. @see <http://api.mongodb.org/python/current/installation.html>

## [Examples](mongodb_status_module.md#id5)

```yaml+jinja
- name: Check replicaset is healthy, fail if not after first attempt
  community.mongodb.mongodb_status:
    replica_set: rs0
  when: ansible_hostname == "mongodb1"

- name: Wait for the replicaset rs0 to converge, check 5 times, 10 second interval between checks
  community.mongodb.mongodb_status:
    replica_set: rs0
    poll: 5
    interval: 10
  when: ansible_hostname == "mongodb1"

# Get the replicaset status and then lookup the primary's hostname and save to a variable
- name: Ensure replicaset is stable before beginning
  community.mongodb.mongodb_status:
    login_user: "{{ admin_user }}"
    login_password: "{{ admin_user_password }}"
    poll: 3
    interval: 10
  register: rs

- name: Lookup PRIMARY replicaset member
  set_fact:
    primary: "{{ item.key.split('.')[0] }}"
  loop: "{{ lookup('dict', rs.replicaset) }}"
  when: "'PRIMARY' in item.value"
```

## [Return Values](mongodb_status_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed**  boolean | If the module has failed or not.  Returned: always |
| **iterations**  integer | Number of times the module has queried the replicaset status.  Returned: always |
| **msg**  string | Status message.  Returned: always |
| **replicaset**  dictionary | The last queried status of all the members of the replicaset if obtainable.  Returned: always |

### Authors

- Rhys Campbell (@rhysmeister)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.mongodb)
[Repository (Sources)](https://github.com/ansible-collections/community.mongodb)
