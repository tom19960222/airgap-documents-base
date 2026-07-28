---
collection: ansible
version: "6"
title: "community.mongodb.mongodb_shell module – Run commands via the MongoDB shell."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/mongodb/mongodb_shell_module.html
fetched_at: 2026-07-27T17:16:10+00:00
---
# community.mongodb.mongodb_shell module – Run commands via the MongoDB shell.

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
> see [Requirements](mongodb_shell_module.md#ansible-collections-community-mongodb-mongodb-shell-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mongodb.mongodb_shell`.

New in community.mongodb 1.1.0

- [Synopsis](mongodb_shell_module.md#synopsis)
- [Requirements](mongodb_shell_module.md#requirements)
- [Parameters](mongodb_shell_module.md#parameters)
- [Examples](mongodb_shell_module.md#examples)
- [Return Values](mongodb_shell_module.md#return-values)

## [Synopsis](mongodb_shell_module.md#id1)

- Run commands via the MongoDB shell.
- Commands provided with the eval parameter or included in a Javascript file.
- Attempts to parse returned data into a format that Ansible can use.
- Module currently uses the mongo shell by default. This will change to mongosh in an upcoming version and support for mongo will be dropped

## [Requirements](mongodb_shell_module.md#id2)

The below requirements are needed on the host that executes this module.

- mongo or mongosh

## [Parameters](mongodb_shell_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **additional_args**  any | Additional arguments to supply to the mongo command.  Supply as key-value pairs.  If the parameter is a valueless flag supply an empty string as the value. |
| **db**  string | The database to run commands against  Default: `"test"` |
| **debug**  boolean | show additional debug info.  Choices:   - `false` ← (default) - `true` |
| **eval**  string | A MongoDB command to run. |
| **file**  string | Path to a file containing MongoDB commands. |
| **idempotent**  boolean | Provides a form of pseudo-idempotency to the module.  We perform a hash calculation on the contents of the eval key or the file name provided in the file key.  When the command is first execute a filed called <hash>.success will be created.  The module will not rerun the command if this file exists and idempotent is set to true.  Choices:   - `false` ← (default) - `true` |
| **login_database**  string | The database where login credentials are stored.  Default: `"admin"` |
| **login_host**  string | The host running MongoDB instance to login to.  Default: `"localhost"` |
| **login_password**  string | The password used to authenticate with.  Required when *login_user* is specified. |
| **login_port**  integer | The MongoDB server port to login to.  Default: `27017` |
| **login_user**  string | The MongoDB user to login with.  Required when *login_password* is specified. |
| **mongo_cmd**  string | The MongoDB shell command.  Default: `"mongo"` |
| **nodb**  boolean | Specify a non-default encoding for output.  Choices:   - `false` ← (default) - `true` |
| **norc**  boolean | Prevents the shell from sourcing and evaluating ~/.mongorc.js on start up.  Choices:   - `false` ← (default) - `true` |
| **omit**  list / elements=string | Parameter to omit from the command line.  This should match the parameter name that the MongoDB shell accepts not the module name.  Default: `[]` |
| **quiet**  boolean | Silences output from the shell during the connection process..  Choices:   - `false` - `true` ← (default) |
| **split_char**  string | Used by the split action in the transform stage.  Default: `" "` |
| **strict_compatibility**  boolean | Enforce strict requirements for pymongo and MongoDB software versions  Choices:   - `false` - `true` ← (default) |
| **stringify**  boolean | Wraps the command in eval in JSON.stringify(<js cmd>) (mongo) or EJSON.stringify(<js cmd>) (mongosh).  Useful for escaping documents that are returned in Extended JSON format.  Automatically set to false when using mongo.  Automatically set to true when using mongosh.  Set explicitly to override automatic selection.  Choices:   - `false` - `true` |
| **transform**  string | Transform the output returned to the user.  auto - Attempt to automatically decide the best tranformation.  split - Split output on a character.  json - parse as json.  raw - Return the raw output.  Choices:   - `"auto"` ← (default) - `"split"` - `"json"` - `"raw"` |

## [Examples](mongodb_shell_module.md#id4)

```yaml+jinja
- name: Run the listDatabases command
  community.mongodb.mongodb_shell:
    login_user: user
    login_password: secret
    eval: "db.adminCommand('listDatabases')"

- name: List collections and stringify the output
  community.mongodb.mongodb_shell:
    login_user: user
    login_password: secret
    eval: "db.adminCommand('listCollections')"
    stringify: yes

- name: Run the showBuiltinRoles command
  community.mongodb.mongodb_shell:
    login_user: user
    login_password: secret
    eval: "db.getRoles({showBuiltinRoles: true})"

- name: Run a js file containing MongoDB commands with pseudo-idempotency
  community.mongodb.mongodb_shell:
    login_user: user
    login_password: secret
    file: "/path/to/mongo/file.js"
    idempotent: yes

- name: Provide a couple of additional cmd args
  community.mongodb.mongodb_shell:
    login_user: user
    login_password: secret
    eval: "db.adminCommand('listDatabases')"
    additional_args:
      verbose: True
      networkMessageCompressors: "snappy"
```

## [Return Values](mongodb_shell_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Change status.  Returned: always |
| **err**  string | Raw stderr from mongo.  Returned: when debug is set to true |
| **failed**  boolean | Something went wrong.  Returned: on failure |
| **file**  string | JS file that was executed successfully.  Returned: When a js file is used. |
| **msg**  string | A message indicating what has happened.  Returned: always |
| **out**  string | Raw stdout from mongo.  Returned: when debug is set to true |
| **rc**  integer | Return code from mongo.  Returned: when debug is set to true |
| **transformed_output**  list / elements=string | Output from the mongo command. We attempt to parse this into a list or json where possible.  Returned: on success |

### Authors

- Rhys Campbell (@rhysmeister)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.mongodb)
[Repository (Sources)](https://github.com/ansible-collections/community.mongodb)
