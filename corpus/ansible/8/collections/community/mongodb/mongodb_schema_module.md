---
collection: ansible
version: "8"
title: "community.mongodb.mongodb_schema module – Manages MongoDB Document Schema Validators."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/mongodb/mongodb_schema_module.html
fetched_at: 2026-07-28T01:54:01+00:00
---
# community.mongodb.mongodb_schema module – Manages MongoDB Document Schema Validators.

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
> see [Requirements](mongodb_schema_module.md#ansible-collections-community-mongodb-mongodb-schema-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mongodb.mongodb_schema`.

New in community.mongodb 1.3.0

- [Synopsis](mongodb_schema_module.md#synopsis)
- [Requirements](mongodb_schema_module.md#requirements)
- [Parameters](mongodb_schema_module.md#parameters)
- [Notes](mongodb_schema_module.md#notes)
- [Examples](mongodb_schema_module.md#examples)
- [Return Values](mongodb_schema_module.md#return-values)

## [Synopsis](mongodb_schema_module.md#id1)

- Manages MongoDB Document Schema Validators.
- Create, update and remove Validators on a collection.
- Supports the entire range of jsonSchema keywords.
- See [jsonSchema Available Keywords](<https://docs.mongodb.com/manual/reference/operator/query/jsonSchema/#available-keywords>) for details.

## [Requirements](mongodb_schema_module.md#id2)

The below requirements are needed on the host that executes this module.

- pymongo

## [Parameters](mongodb_schema_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **action**  string | The validation action for MongoDB to perform when handling invalid documents.  **Choices:**   - `"error"` ← (default) - `"warn"` |
| **atlas_auth**  boolean | Authentication path intended for MongoDB Atlas Instances  **Choices:**   - `false` ← (default) - `true` |
| **auth_mechanism**  string | Authentication type.  **Choices:**   - `"SCRAM-SHA-256"` - `"SCRAM-SHA-1"` - `"MONGODB-X509"` - `"GSSAPI"` - `"PLAIN"` |
| **collection**  string / required | The collection to work with. |
| **connection_options**  list / elements=any | Additional connection options.  Supply as a list of dicts or strings containing key value pairs seperated with ‘=’. |
| **db**  string / required | The database to work with. |
| **debug**  boolean | Enable additional debugging output.  **Choices:**   - `false` ← (default) - `true` |
| **level**  string | The validation level MongoDB should apply when updating existing documents.  **Choices:**   - `"strict"` ← (default) - `"moderate"` |
| **login_database**  string | The database where login credentials are stored.  **Default:** `"admin"` |
| **login_host**  string | The host running MongoDB instance to login to.  **Default:** `"localhost"` |
| **login_password**  string | The password used to authenticate with.  Required when *login_user* is specified. |
| **login_port**  integer | The MongoDB server port to login to.  **Default:** `27017` |
| **login_user**  string | The MongoDB user to login with.  Required when *login_password* is specified. |
| **properties**  dictionary | Individual property specification.  **Default:** `{}` |
| **replica_set**  string | Replicaset name. |
| **required**  list / elements=string | List of fields that are required. |
| **ssl**  aliases: tls  boolean | Whether to use an SSL connection when connecting to the database.  **Choices:**   - `false` ← (default) - `true` |
| **ssl_ca_certs**  aliases: tlsCAFile  string | The ssl_ca_certs option takes a path to a CA file. |
| **ssl_cert_reqs**  aliases: tlsAllowInvalidCertificates  string | Specifies whether a certificate is required from the other side of the connection, and whether it will be validated if provided.  **Choices:**   - `"CERT_NONE"` - `"CERT_OPTIONAL"` - `"CERT_REQUIRED"` ← (default) |
| **ssl_certfile**  aliases: tlsCertificateKeyFile  string | Present a client certificate using the ssl_certfile option. |
| **ssl_crlfile**  string | The ssl_crlfile option takes a path to a CRL file. |
| **ssl_keyfile**  string | Private key for the client certificate. |
| **ssl_pem_passphrase**  aliases: tlsCertificateKeyFilePassword  string | Passphrase to decrypt encrypted private keys. |
| **state**  string | The state of the validator.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **strict_compatibility**  boolean | Enforce strict requirements for pymongo and MongoDB software versions  **Choices:**   - `false` - `true` ← (default) |

## [Notes](mongodb_schema_module.md#id4)

> **Note:**
>
> - Requires the pymongo Python package on the remote host, version 2.4.2+.

## [Examples](mongodb_schema_module.md#id5)

```yaml+jinja
---
- name: Require that an email address field is in every document
  community.mongodb.mongodb_schema:
    collection: contacts
    db: rhys
    required:
      - email

- name: Remove a schema rule
  community.mongodb.mongodb_schema:
    collection: contacts
    db: rhys
    state: absent

- name: More advanced example using properties
  community.mongodb.mongodb_schema:
    collection: contacts
    db: rhys
    properties:
      email:
        maxLength: 150
        minLength: 5
      options:
        bsonType: array
        maxItems: 10
        minItems: 5
        uniqueItems: true
      status:
        bsonType: string
        description: "can only be ACTIVE or DISABLED"
        enum:
          - ACTIVE
          - DISABLED
      year:
        bsonType: int
        description: "must be an integer from 2021 to 3020"
        exclusiveMaximum: false
        maximum: 3020
        minimum: 2021
    required:
      - email
      - first_name
      - last_name
```

## [Return Values](mongodb_schema_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | If the module caused a change.  **Returned:** on success |
| **module_config**  dictionary | The validator document as indicated by the module invocation.  **Returned:** when debug is true |
| **msg**  string | Status message.  **Returned:** always |
| **validator**  dictionary | The validator document as read from the instance.  **Returned:** when debug is true |

### Authors

- Rhys Campbell (@rhysmeister)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.mongodb)
- [Repository (Sources)](https://github.com/ansible-collections/community.mongodb)
