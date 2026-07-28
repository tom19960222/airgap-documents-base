---
collection: ansible
version: "6"
title: "community.proxysql.proxysql_query_rules module – Modifies query rules using the proxysql admin interface"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/proxysql/proxysql_query_rules_module.html
fetched_at: 2026-07-27T17:20:36+00:00
---
# community.proxysql.proxysql_query_rules module – Modifies query rules using the proxysql admin interface

> **Note:**
>
> This module is part of the [community.proxysql collection](https://galaxy.ansible.com/community/proxysql) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.proxysql`.
> You need further requirements to be able to use this module,
> see [Requirements](proxysql_query_rules_module.md#ansible-collections-community-proxysql-proxysql-query-rules-module-requirements) for details.
>
> To use it in a playbook, specify: `community.proxysql.proxysql_query_rules`.

- [Synopsis](proxysql_query_rules_module.md#synopsis)
- [Requirements](proxysql_query_rules_module.md#requirements)
- [Parameters](proxysql_query_rules_module.md#parameters)
- [Notes](proxysql_query_rules_module.md#notes)
- [Examples](proxysql_query_rules_module.md#examples)
- [Return Values](proxysql_query_rules_module.md#return-values)

## [Synopsis](proxysql_query_rules_module.md#id1)

- The [community.proxysql.proxysql_query_rules](proxysql_query_rules_module.md#ansible-collections-community-proxysql-proxysql-query-rules-module) module modifies query rules using the proxysql admin interface.

## [Requirements](proxysql_query_rules_module.md#id2)

The below requirements are needed on the host that executes this module.

- PyMySQL
- mysqlclient

## [Parameters](proxysql_query_rules_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | A rule with *active* set to `False` will be tracked in the database, but will be never loaded in the in-memory data structures.  Choices:   - `false` - `true` |
| **apply**  boolean | Used in combination with *flagIN* and *flagOUT* to create chains of rules. Setting apply to True signifies the last rule to be applied.  Choices:   - `false` - `true` |
| **cache_empty_result**  boolean  added in community.proxysql 1.1.0 | Controls if resultset without rows will be cached or not.  Choices:   - `false` - `true` |
| **cache_ttl**  integer | The number of milliseconds for which to cache the result of the query. Note in ProxySQL 1.1 *cache_ttl* was in seconds. |
| **client_addr**  string | Match traffic from a specific source. |
| **comment**  string | Free form text field, usable for a descriptive comment of the query rule. |
| **config_file**  path | Specify a config file from which *login_user* and *login_password* are to be read.  Default: `""` |
| **delay**  integer | Number of milliseconds to delay the execution of the query. This is essentially a throttling mechanism and QoS, and allows a way to give priority to queries over others. This value is added to the mysql-default_query_delay global variable that applies to all queries. |
| **destination_hostgroup**  integer | Route matched queries to this hostgroup. This happens unless there is a started transaction and the logged in user has *transaction_persistent* set to `True` (see [community.proxysql.proxysql_mysql_users](proxysql_mysql_users_module.md#ansible-collections-community-proxysql-proxysql-mysql-users-module)). |
| **digest**  string | Match queries with a specific digest, as returned by stats_mysql_query_digest.digest. |
| **error_msg**  string | Query will be blocked, and the specified error_msg will be returned to the client. |
| **flagIN**  integer | Used in combination with *flagOUT* and *apply* to create chains of rules. |
| **flagOUT**  integer | Used in combination with *flagIN* and apply to create chains of rules. When set, *flagOUT* signifies the *flagIN* to be used in the next chain of rules. |
| **force_delete**  boolean | By default we avoid deleting more than one schedule in a single batch, however if you need this behaviour and you are not concerned about the schedules deleted, you can set *force_delete* to `True`.  Choices:   - `false` ← (default) - `true` |
| **load_to_runtime**  boolean | Dynamically load config to runtime memory.  Choices:   - `false` - `true` ← (default) |
| **log**  boolean | Query will be logged.  Choices:   - `false` - `true` |
| **login_host**  string | The host used to connect to ProxySQL admin interface.  Default: `"127.0.0.1"` |
| **login_password**  string | The password used to authenticate to ProxySQL admin interface. |
| **login_port**  integer | The port used to connect to ProxySQL admin interface.  Default: `6032` |
| **login_unix_socket**  string | The socket used to connect to ProxySQL admin interface. |
| **login_user**  string | The username used to authenticate to ProxySQL admin interface. |
| **match_digest**  string | Regular expression that matches the query digest. The dialect of regular expressions used is that of re2 - <https://github.com/google/re2>. |
| **match_pattern**  string | Regular expression that matches the query text. The dialect of regular expressions used is that of re2 - <https://github.com/google/re2>. |
| **mirror_flagOUT**  integer | Enables query mirroring. If set *mirror_flagOUT* can be used to evaluates the mirrored query against the specified chain of rules. |
| **mirror_hostgroup**  integer | Enables query mirroring. If set *mirror_hostgroup* can be used to mirror queries to the same or different hostgroup. |
| **multiplex**  integer  added in community.proxysql 1.1.0 | If `0`, multiplex will be disabled.  If `1`, try to enable multiplex. There can be other conditions preventing this (for example, user variables or transactions).  If `2`, multiplexing is not disabled for just the current query.  By default, does not change multiplexing policies.  Choices:   - `0` - `1` - `2` |
| **negate_match_pattern**  boolean | If *negate_match_pattern* is set to `True`, only queries not matching the query text will be considered as a match. This acts as a NOT operator in front of the regular expression matching against match_pattern.  Choices:   - `false` - `true` |
| **next_query_flagIN**  integer  added in community.proxysql 1.3.0 | When is set, its value will become the *flagIN* value for the next queries. |
| **OK_msg**  string  added in community.proxysql 1.1.0 | The specified message will be returned for a query that uses the defined rule. |
| **proxy_addr**  string | Match incoming traffic on a specific local IP. |
| **proxy_port**  integer | Match incoming traffic on a specific local port. |
| **re_modifiers**  string  added in community.proxysql 1.3.0 | Comma separated list of options to modify the behavior of the RE engine. With `CASELESS` the match is case insensitive. With `GLOBAL` the replace is global (replaces all matches and not just the first). For backward compatibility, only `CASELESS` is the enabled by default. |
| **replace_pattern**  string | This is the pattern with which to replace the matched pattern. Note that this is optional, and when omitted, the query processor will only cache, route, or set other parameters without rewriting. |
| **retries**  integer | The maximum number of times a query needs to be re-executed in case of detected failure during the execution of the query. If retries is not specified, the global variable mysql-query_retries_on_failure applies. |
| **rule_id**  integer | The unique id of the rule. Rules are processed in rule_id order. |
| **save_to_disk**  boolean | Save config to sqlite db on disk to persist the configuration.  Choices:   - `false` - `true` ← (default) |
| **schemaname**  string | Filtering criteria matching schemaname. If *schemaname* is non-NULL, a query will match only if the connection uses schemaname as its default schema. |
| **state**  string | When `present` - adds the rule, when `absent` - removes the rule.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The maximum timeout in milliseconds with which the matched or rewritten query should be executed. If a query run for longer than the specific threshold, the query is automatically killed. If timeout is not specified, the global variable mysql-default_query_timeout applies. |
| **username**  string | Filtering criteria matching username. If *username* is non-NULL, a query will match only if the connection is made with the correct username. |

## [Notes](proxysql_query_rules_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.

## [Examples](proxysql_query_rules_module.md#id5)

```yaml+jinja
---
# This example adds a rule to redirect queries from a specific user to another
# hostgroup, it saves the mysql query rule config to disk, but avoids loading
# the mysql query config config to runtime (this might be because several
# rules are being added and the user wants to push the config to runtime in a
# single batch using the community.general.proxysql_manage_config module). It
# uses supplied credentials to connect to the proxysql admin interface.

- name: Add a rule
  community.proxysql.proxysql_query_rules:
    login_user: admin
    login_password: admin
    username: 'guest_ro'
    match_pattern: "^SELECT.*"
    destination_hostgroup: 1
    active: 1
    retries: 3
    state: present
    load_to_runtime: False

# This example demonstrates the situation, if your application tries to set a
# variable that will disable multiplexing, and you think it can be filtered out,
# you can create a filter that returns OK without executing the request.

- name: Add a filter rule
  community.proxysql.proxysql_query_rules:
    login_user: admin
    login_password: admin
    match_digest: '^SET @@wait_timeout = ?'
    active: 1
    OK_msg: 'The wait_timeout variable is ignored'

# This example adds a caching rule for a query that matches the digest.
# The query digest can be obtained from the `stats_mysql_query_digest`
# table. `cache_ttl` is specified in milliseconds. Empty responses are
# not cached.

- name: Add a cache rule
  community.proxysql.proxysql_query_rules:
    login_user: admin
    login_password: admin
    rule_id: 1
    digest: 0xECA450EA500A9A55
    cache_ttl: 30000
    cache_empty_result: no
    destination_hostgroup: 1
    active: yes
    state: present
    save_to_disk: yes
    load_to_runtime: yes

# This example demonstrates how to prevent disabling multiplexing for
# situations where a request contains @.

- name: Add a rule with multiplex
  community.proxysql.proxysql_query_rules:
    login_user: admin
    login_password: admin
    rule_id: 1
    active: 1
    match_digest: '^SELECT @@max_allowed_packet'
    multiplex: 2

# This example demonstrates how to use next_query_flagIN argument. It allows
# ProxySQL query rules to be chained. The examples shows how you can have SELECTS
# immediately follow INSERT/UPDATE/DELETE statements to query the primary hostgroup
# and avoid replication lag

- name: Add insert query rule
  proxysql_query_rules:
    match_digest: "^INSERT"
    destination_hostgroup: 1,
    next_query_flagIN: 1

- name: Add update query rule
  proxysql_query_rules:
    match_digest: "^UPDATE"
    destination_hostgroup: 1,
    next_query_flagIN: 1

- name: Add delete query rules
  proxysql_query_rules:
    match_digest: "^DELETE"
    destination_hostgroup: 1,
    next_query_flagIN: 1

- name: Add insert query rules
  proxysql_query_rules:
    match_digest: ".*"
    destination_hostgroup: 1,
    next_query_flagIN: 1
    comment: Match every queries after an INSERT/UPDATE/DELETE query

# This example removes all rules that use the username 'guest_ro', saves the
# mysql query rule config to disk, and dynamically loads the mysql query rule
# config to runtime.  It uses credentials in a supplied config file to connect
# to the proxysql admin interface.

- name: Remove rules
  community.proxysql.proxysql_query_rules:
    config_file: '~/proxysql.cnf'
    username: 'guest_ro'
    state: absent
    force_delete: true
```

## [Return Values](proxysql_query_rules_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **stdout**  dictionary | The mysql user modified or removed from proxysql.  Returned: On create/update will return the newly modified rule, in all other cases will return a list of rules that match the supplied criteria.  Sample: `{"changed": true, "msg": "Added rule to mysql_query_rules", "rules": [{"OK_msg": null, "active": "0", "apply": "0", "cache_empty_result": null, "cache_ttl": null, "client_addr": null, "comment": null, "delay": null, "destination_hostgroup": 1, "digest": null, "error_msg": null, "flagIN": "0", "flagOUT": null, "log": null, "match_digest": null, "match_pattern": null, "mirror_flagOUT": null, "mirror_hostgroup": null, "multiplex": null, "negate_match_pattern": "0", "proxy_addr": null, "proxy_port": null, "reconnect": null, "replace_pattern": null, "retries": null, "rule_id": "1", "schemaname": null, "timeout": null, "username": "guest_ro"}], "state": "present"}` |

### Authors

- Ben Mildren (@bmildren)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.proxysql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.proxysql)
