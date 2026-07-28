---
collection: ansible
version: "6"
title: "community.mongodb.mongodb lookup – lookup info from MongoDB"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/mongodb/mongodb_lookup.html
fetched_at: 2026-07-27T17:16:14+00:00
---
# community.mongodb.mongodb lookup – lookup info from MongoDB

> **Note:**
>
> This lookup plugin is part of the [community.mongodb collection](https://galaxy.ansible.com/community/mongodb) (version 1.4.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.mongodb`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](mongodb_lookup.md#ansible-collections-community-mongodb-mongodb-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.mongodb.mongodb`.

New in community.mongodb 1.0.0

- [Synopsis](mongodb_lookup.md#synopsis)
- [Requirements](mongodb_lookup.md#requirements)
- [Keyword parameters](mongodb_lookup.md#keyword-parameters)
- [Notes](mongodb_lookup.md#notes)
- [Examples](mongodb_lookup.md#examples)
- [Return Value](mongodb_lookup.md#return-value)

## [Synopsis](mongodb_lookup.md#id1)

- The ``MongoDB`` lookup runs the \*find()\* command on a given \*collection\* on a given \*MongoDB\* server.
- The result is a list of jsons, so slightly different from what PyMongo returns. In particular, \*timestamps\* are converted to epoch integers.

## [Requirements](mongodb_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- pymongo >= 2.4 (python library)

## [Keyword parameters](mongodb_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.mongodb.mongodb', key1=value1, key2=value2, ...)` and `query('community.mongodb.mongodb', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **collection**  string / required | Name of the collection which the query will be made |
| **connect_string**  string | Can be any valid MongoDB connection string, supporting authentication, replica sets, etc.  More info at <https://docs.mongodb.org/manual/reference/connection-string/>  Default: `"mongodb://localhost/"` |
| **database**  string / required | Name of the database which the query will be made |
| **extra_connection_parameters**  dictionary | Extra connection parameters that to be sent to pymongo.MongoClient  Check the example to see how to connect to mongo using an SSL certificate.  All possible parameters are here: <https://api.mongodb.com/python/current/api/pymongo/mongo_client.html#pymongo.mongo_client.MongoClient>  Default: `{}` |
| **filter**  dictionary | Criteria of the output  Default: `{}` |
| **limit**  integer | How many results should be shown |
| **projection**  dictionary | Fields you want returned  Default: `{}` |
| **skip**  integer | How many results should be skipped |
| **sort**  list / elements=list | Sorting rules.  Please use the strings `ASCENDING` and `DESCENDING` to set the order.  Check the example for more information.  Default: `[]` |

## [Notes](mongodb_lookup.md#id4)

> **Note:**
>
> - Please check <https://api.mongodb.org/python/current/api/pymongo/collection.html?highlight=find#pymongo.collection.Collection.find> for more details.

## [Examples](mongodb_lookup.md#id5)

```yaml+jinja
- hosts: localhost
  gather_facts: false
  vars:
    mongodb_parameters:
      #mandatory parameters
      database: 'local'
      collection: "startup_log"
      #optional
      connection_string: "mongodb://localhost/"
      # connection_string: "mongodb://username:password@my.server.com:27017/"
      # extra_connection_parameters: { "ssl" : True , "ssl_certfile": /etc/self_signed_certificate.pem" }
      #optional query  parameters, we accept any parameter from the normal mongodb query.
      # filter:  { "hostname": "u18" }
      projection: { "pid": True    , "_id" : False , "hostname" : True }
      skip: 0
      limit: 1
      sort:  [ [ "startTime" , "ASCENDING" ] , [ "age", "DESCENDING" ] ]
  tasks:
    - debug: msg="The PID from MongoDB is {{ lookup('mongodb', mongodb_parameters ).pid }}"

    - debug: msg="The HostName from the MongoDB server is {{ lookup('mongodb', mongodb_parameters ).hostname }}"

    - debug: msg="Mongo DB is stored at {{ lookup('mongodb', mongodb_parameters_inline )}}"
      vars:
        mongodb_parameters_inline:
          database: 'local'
          collection: "startup_log"
          connection_string: "mongodb://localhost/"
          limit: 1
          projection: { "cmdline.storage": True }

      # lookup syntax, does the same as below
    - debug: msg="The hostname is {{ item.hostname }} and the pid is {{ item.pid }}"
      loop: "{{ lookup('mongodb', mongodb_parameters, wantlist=True) }}"

      # query syntax, does the same as above
    - debug: msg="The hostname is {{ item.hostname }} and the pid is {{ item.pid }}"
      loop: "{{ query('mongodb', mongodb_parameters) }}"

    - name: "Raw output from the mongodb lookup (a json with pid and hostname )"
      debug: msg="{{ lookup('mongodb', mongodb_parameters) }}"

    - name: "Yet another mongodb query, now with the parameters on the task itself"
      debug: msg="pid={{item.pid}} hostname={{item.hostname}} version={{ item.buildinfo.version }}"
      with_mongodb:
        - database: 'local'
          collection: "startup_log"
          connection_string: "mongodb://localhost/"
          limit: 1
          projection: { "pid": True    , "hostname": True , "buildinfo.version": True }

    # Please notice this specific query may result more than one result. This is expected
    - name: "Shows the whole output from mongodb"
      debug: msg="{{ item }}"
      with_mongodb:
        - database: 'local'
          collection: "startup_log"
          connection_string: "mongodb://localhost/"
```

## [Return Value](mongodb_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | a list of JSONs with the results of the MongoDB query.  Returned: success |

### Authors

- Marcos Diez (@marcosdiez)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.mongodb)
[Repository (Sources)](https://github.com/ansible-collections/community.mongodb)
