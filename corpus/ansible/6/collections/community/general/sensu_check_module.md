---
collection: ansible
version: "6"
title: "community.general.sensu_check module – Manage Sensu checks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/sensu_check_module.html
fetched_at: 2026-07-27T17:13:09+00:00
---
# community.general.sensu_check module – Manage Sensu checks

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.sensu_check`.

- [Synopsis](sensu_check_module.md#synopsis)
- [Parameters](sensu_check_module.md#parameters)
- [Examples](sensu_check_module.md#examples)

## [Synopsis](sensu_check_module.md#id1)

- Manage the checks that should be run on a machine by *Sensu*.
- Most options do not have a default and will not be added to the check definition unless specified.
- All defaults except *path*, *state*, *backup* and *metric* are not managed by this module,
- they are simply specified for your convenience.

## [Parameters](sensu_check_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  boolean | Classifies the check as an aggregate check,  making it available via the aggregate API  Default is `false`.  Choices:   - `false` - `true` |
| **backup**  boolean | Create a backup file (if yes), including the timestamp information so  you can get the original file back if you somehow clobbered it incorrectly.  Choices:   - `false` ← (default) - `true` |
| **command**  string | Path to the sensu check to run (not required when *state=absent*) |
| **custom**  dictionary | A hash/dictionary of custom parameters for mixing to the configuration.  You can’t rewrite others module parameters using this |
| **dependencies**  list / elements=string | Other checks this check depends on, if dependencies fail handling of this check will be disabled |
| **handle**  boolean | Whether the check should be handled or not  Default is `false`.  Choices:   - `false` - `true` |
| **handlers**  list / elements=string | List of handlers to notify when the check fails |
| **high_flap_threshold**  integer | The high threshold for flap detection |
| **interval**  integer | Check interval in seconds |
| **low_flap_threshold**  integer | The low threshold for flap detection |
| **metric**  boolean | Whether the check is a metric  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | The name of the check  This is the key that is used to determine whether a check exists |
| **occurrences**  integer | Number of event occurrences before the handler should take action  If not specified, defaults to 1. |
| **path**  string | Path to the json file of the check to be added/removed.  Will be created if it does not exist (unless *state=absent*).  The parent folders need to exist when *state=present*, otherwise an error will be thrown  Default: `"/etc/sensu/conf.d/checks.json"` |
| **publish**  boolean | Whether the check should be scheduled at all.  You can still issue it via the sensu api  Default is `false`.  Choices:   - `false` - `true` |
| **refresh**  integer | Number of seconds handlers should wait before taking second action |
| **source**  string | The check source, used to create a JIT Sensu client for an external resource (e.g. a network switch). |
| **standalone**  boolean | Whether the check should be scheduled by the sensu client or server  This option obviates the need for specifying the *subscribers* option  Default is `false`.  Choices:   - `false` - `true` |
| **state**  string | Whether the check should be present or not  Choices:   - `"present"` ← (default) - `"absent"` |
| **subdue_begin**  string | When to disable handling of check failures |
| **subdue_end**  string | When to enable handling of check failures |
| **subscribers**  list / elements=string | List of subscribers/channels this check should run for  See sensu_subscribers to subscribe a machine to a channel |
| **timeout**  integer | Timeout for the check  If not specified, it defaults to 10. |
| **ttl**  integer | Time to live in seconds until the check is considered stale |

## [Examples](sensu_check_module.md#id3)

```yaml+jinja
# Fetch metrics about the CPU load every 60 seconds,
# the sensu server has a handler called 'relay' which forwards stats to graphite
- name: Get cpu metrics
  community.general.sensu_check:
    name: cpu_load
    command: /etc/sensu/plugins/system/cpu-mpstat-metrics.rb
    metric: true
    handlers: relay
    subscribers: common
    interval: 60

# Check whether nginx is running
- name: Check nginx process
  community.general.sensu_check:
    name: nginx_running
    command: /etc/sensu/plugins/processes/check-procs.rb -f /var/run/nginx.pid
    handlers: default
    subscribers: nginx
    interval: 60

# Stop monitoring the disk capacity.
# Note that the check will still show up in the sensu dashboard,
# to remove it completely you need to issue a DELETE request to the sensu api.
- name: Check disk
  community.general.sensu_check:
    name: check_disk_capacity
    state: absent
```

### Authors

- Anders Ingemann (@andsens)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
