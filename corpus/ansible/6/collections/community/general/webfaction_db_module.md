---
collection: ansible
version: "6"
title: "community.general.webfaction_db module – Add or remove a database on Webfaction"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/webfaction_db_module.html
fetched_at: 2026-07-27T17:14:00+00:00
---
# community.general.webfaction_db module – Add or remove a database on Webfaction

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
> To use it in a playbook, specify: `community.general.webfaction_db`.

- [Synopsis](webfaction_db_module.md#synopsis)
- [Parameters](webfaction_db_module.md#parameters)
- [Notes](webfaction_db_module.md#notes)
- [Examples](webfaction_db_module.md#examples)

## [Synopsis](webfaction_db_module.md#id1)

- Add or remove a database on a Webfaction host. Further documentation at <https://github.com/quentinsf/ansible-webfaction>.

## [Parameters](webfaction_db_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **login_name**  string / required | The webfaction account to use |
| **login_password**  string / required | The webfaction password to use |
| **machine**  string | The machine name to use (optional for accounts with only one machine) |
| **name**  string / required | The name of the database |
| **password**  string | The password for the new database user. |
| **state**  string | Whether the database should exist  Choices:   - `"present"` ← (default) - `"absent"` |
| **type**  string / required | The type of database to create.  Choices:   - `"mysql"` - `"postgresql"` |

## [Notes](webfaction_db_module.md#id3)

> **Note:**
>
> - You can run playbooks that use this on a local machine, or on a Webfaction host, or elsewhere, since the scripts use the remote webfaction API. The location is not important. However, running them on multiple hosts *simultaneously* is best avoided. If you don’t specify *localhost* as your host, you may want to add `serial: 1` to the plays.
> - See `the webfaction API <<https://docs.webfaction.com/xmlrpc-api/>>`_ for more info.

## [Examples](webfaction_db_module.md#id4)

```yaml+jinja
# This will also create a default DB user with the same
# name as the database, and the specified password.

- name: Create a database
  community.general.webfaction_db:
    name: "{{webfaction_user}}_db1"
    password: mytestsql
    type: mysql
    login_name: "{{webfaction_user}}"
    login_password: "{{webfaction_passwd}}"
    machine: "{{webfaction_machine}}"

# Note that, for symmetry's sake, deleting a database using
# 'state: absent' will also delete the matching user.
```

### Authors

- Quentin Stafford-Fraser (@quentinsf)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
