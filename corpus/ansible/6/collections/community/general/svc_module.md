---
collection: ansible
version: "6"
title: "community.general.svc module – Manage daemontools services"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/svc_module.html
fetched_at: 2026-07-27T17:13:27+00:00
---
# community.general.svc module – Manage daemontools services

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
> To use it in a playbook, specify: `community.general.svc`.

- [Synopsis](svc_module.md#synopsis)
- [Parameters](svc_module.md#parameters)
- [Examples](svc_module.md#examples)

## [Synopsis](svc_module.md#id1)

- Controls daemontools services on remote hosts using the svc utility.

## [Parameters](svc_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **downed**  boolean | Should a ‘down’ file exist or not, if it exists it disables auto startup. Defaults to no. Downed does not imply stopped.  Choices:   - `false` - `true` |
| **enabled**  boolean | Whether the service is enabled or not, if disabled it also implies stopped. Take note that a service can be enabled and downed (no auto restart).  Choices:   - `false` - `true` |
| **name**  string / required | Name of the service to manage. |
| **service_dir**  string | Directory svscan watches for services  Default: `"/service"` |
| **service_src**  string | Directory where services are defined, the source of symlinks to service_dir.  Default: `"/etc/service"` |
| **state**  string | `Started`/`stopped` are idempotent actions that will not run commands unless necessary. `restarted` will always bounce the svc (svc -t) and `killed` will always bounce the svc (svc -k). `reloaded` will send a sigusr1 (svc -1). `once` will run a normally downed svc once (svc -o), not really an idempotent operation.  Choices:   - `"killed"` - `"once"` - `"reloaded"` - `"restarted"` - `"started"` - `"stopped"` |

## [Examples](svc_module.md#id3)

```yaml+jinja
- name: Start svc dnscache, if not running
  community.general.svc:
    name: dnscache
    state: started

- name: Stop svc dnscache, if running
  community.general.svc:
    name: dnscache
    state: stopped

- name: Kill svc dnscache, in all cases
  community.general.svc:
    name: dnscache
    state: killed

- name: Restart svc dnscache, in all cases
  community.general.svc:
    name: dnscache
    state: restarted

- name: Reload svc dnscache, in all cases
  community.general.svc:
    name: dnscache
    state: reloaded

- name: Using alternative svc directory location
  community.general.svc:
    name: dnscache
    state: reloaded
    service_dir: /var/service
```

### Authors

- Brian Coca (@bcoca)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
