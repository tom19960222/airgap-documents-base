---
collection: ansible
version: "6"
title: "Community.Mongodb"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/mongodb/index.html
fetched_at: 2026-07-27T16:41:47+00:00
---
# Community.Mongodb

Collection version 1.4.2

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

MongoDB related ansible Roles, Modules, and Plugins

**Authors:**

- Ansible (<https://github.com/ansible>)
- Rhys Campbell (<https://github.com/rhysmeister>)
- Andrew Klychkov (<https://github.com/Andersson007>)
- Marcos Diez (<https://github.com/marcosdiez>)
- Elliott Foster (<http://fourkitchens.com>)
- Loic Blot (<http://www.infopro-digital.com/>)
- Matt Martz (<https://github.com/sivel>)
- Jacob Floyd (<https://github.com/cognifloyd>)

**Supported ansible-core versions:**

- 2.9.10 or newer

[Issue Tracker](https://github.com/ansible-collections/community.mongodb)
[Repository (Sources)](https://github.com/ansible-collections/community.mongodb)

## [Plugin Index](index.md#id2)

These are the plugins in the community.mongodb collection:

### Modules

- [mongodb_balancer module](mongodb_balancer_module.md#ansible-collections-community-mongodb-mongodb-balancer-module) – Manages the MongoDB Sharded Cluster Balancer.
- [mongodb_index module](mongodb_index_module.md#ansible-collections-community-mongodb-mongodb-index-module) – Creates or drops indexes on MongoDB collections.
- [mongodb_info module](mongodb_info_module.md#ansible-collections-community-mongodb-mongodb-info-module) – Gather information about MongoDB instance.
- [mongodb_maintenance module](mongodb_maintenance_module.md#ansible-collections-community-mongodb-mongodb-maintenance-module) – Enables or disables maintenance mode for a secondary member.
- [mongodb_monitoring module](mongodb_monitoring_module.md#ansible-collections-community-mongodb-mongodb-monitoring-module) – Manages the free monitoring feature.
- [mongodb_oplog module](mongodb_oplog_module.md#ansible-collections-community-mongodb-mongodb-oplog-module) – Resizes the MongoDB oplog.
- [mongodb_parameter module](mongodb_parameter_module.md#ansible-collections-community-mongodb-mongodb-parameter-module) – Change an administrative parameter on a MongoDB server
- [mongodb_replicaset module](mongodb_replicaset_module.md#ansible-collections-community-mongodb-mongodb-replicaset-module) – Initialises a MongoDB replicaset.
- [mongodb_schema module](mongodb_schema_module.md#ansible-collections-community-mongodb-mongodb-schema-module) – Manages MongoDB Document Schema Validators.
- [mongodb_shard module](mongodb_shard_module.md#ansible-collections-community-mongodb-mongodb-shard-module) – Add or remove shards from a MongoDB Cluster
- [mongodb_shard_tag module](mongodb_shard_tag_module.md#ansible-collections-community-mongodb-mongodb-shard-tag-module) – Manage Shard Tags.
- [mongodb_shard_zone module](mongodb_shard_zone_module.md#ansible-collections-community-mongodb-mongodb-shard-zone-module) – Manage Shard Zones.
- [mongodb_shell module](mongodb_shell_module.md#ansible-collections-community-mongodb-mongodb-shell-module) – Run commands via the MongoDB shell.
- [mongodb_shutdown module](mongodb_shutdown_module.md#ansible-collections-community-mongodb-mongodb-shutdown-module) – Cleans up all database resources and then terminates the mongod/mongos process.
- [mongodb_status module](mongodb_status_module.md#ansible-collections-community-mongodb-mongodb-status-module) – Validates the status of the replicaset.
- [mongodb_stepdown module](mongodb_stepdown_module.md#ansible-collections-community-mongodb-mongodb-stepdown-module) – Step down the MongoDB node from a PRIMARY state.
- [mongodb_user module](mongodb_user_module.md#ansible-collections-community-mongodb-mongodb-user-module) – Adds or removes a user from a MongoDB database

### Cache Plugins

- [mongodb cache](mongodb_cache.md#ansible-collections-community-mongodb-mongodb-cache) – Use MongoDB for caching

### Lookup Plugins

- [mongodb lookup](mongodb_lookup.md#ansible-collections-community-mongodb-mongodb-lookup) – lookup info from MongoDB

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
