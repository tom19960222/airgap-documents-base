---
collection: ansible
version: "6"
title: "ansible.builtin.cron module – Manage cron.d and crontab entries"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/cron_module.html
fetched_at: 2026-07-27T16:43:58+00:00
---
# ansible.builtin.cron module – Manage cron.d and crontab entries

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `cron` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](cron_module.md#synopsis)
- [Requirements](cron_module.md#requirements)
- [Parameters](cron_module.md#parameters)
- [Attributes](cron_module.md#attributes)
- [Examples](cron_module.md#examples)

## [Synopsis](cron_module.md#id1)

- Use this module to manage crontab and environment variables entries. This module allows you to create environment variables and named crontab entries, update, or delete them.
- When crontab jobs are managed: the module includes one line with the description of the crontab entry `"#Ansible: <name>"` corresponding to the “name” passed to the module, which is used by future ansible/module calls to find/check the state. The “name” parameter should be unique, and changing the “name” value will result in a new cron task being created (or a different one being removed).
- When environment variables are managed, no comment line is added, but, when the module needs to find/check the state, it uses the “name” parameter to find the environment variable definition line.
- When using symbols such as %, they must be properly escaped.

## [Requirements](cron_module.md#id2)

The below requirements are needed on the host that executes this module.

- cron (any ‘vixie cron’ conformant variant, like cronie)

## [Parameters](cron_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **backup**  boolean | If set, create a backup of the crontab before it is modified. The location of the backup is returned in the `backup_file` variable by this module.  Choices:   - `false` ← (default) - `true` |
| **cron_file**  path | If specified, uses this file instead of an individual user’s crontab. The assumption is that this file is exclusively managed by the module, do not use if the file contains multiple entries, NEVER use for /etc/crontab.  If this is a relative path, it is interpreted with respect to */etc/cron.d*.  Many linux distros expect (and some require) the filename portion to consist solely of upper- and lower-case letters, digits, underscores, and hyphens.  Using this parameter requires you to specify the *user* as well, unless *state* is not *present*.  Either this parameter or *name* is required |
| **day**  aliases: dom  string | Day of the month the job should run (`1-31`, `*`, `*/2`, and so on).  Default: `"*"` |
| **disabled**  boolean | If the job should be disabled (commented out) in the crontab.  Only has effect if *state=present*.  Choices:   - `false` ← (default) - `true` |
| **env**  boolean | If set, manages a crontab’s environment variable.  New variables are added on top of crontab.  *name* and *value* parameters are the name and the value of environment variable.  Choices:   - `false` ← (default) - `true` |
| **hour**  string | Hour when the job should run (`0-23`, `*`, `*/2`, and so on).  Default: `"*"` |
| **insertafter**  string | Used with *state=present* and *env*.  If specified, the environment variable will be inserted after the declaration of specified environment variable. |
| **insertbefore**  string | Used with *state=present* and *env*.  If specified, the environment variable will be inserted before the declaration of specified environment variable. |
| **job**  aliases: value  string | The command to execute or, if env is set, the value of environment variable.  The command should not contain line breaks.  Required if *state=present*. |
| **minute**  string | Minute when the job should run (`0-59`, `*`, `*/2`, and so on).  Default: `"*"` |
| **month**  string | Month of the year the job should run (`1-12`, `*`, `*/2`, and so on).  Default: `"*"` |
| **name**  string / required | Description of a crontab entry or, if env is set, the name of environment variable.  This parameter is always required as of ansible-core 2.12. |
| **special_time**  string | Special time specification nickname.  Choices:   - `"annually"` - `"daily"` - `"hourly"` - `"monthly"` - `"reboot"` - `"weekly"` - `"yearly"` |
| **state**  string | Whether to ensure the job or environment variable is present or absent.  Choices:   - `"absent"` - `"present"` ← (default) |
| **user**  string | The specific user whose crontab should be modified.  When unset, this parameter defaults to the current user. |
| **weekday**  aliases: dow  string | Day of the week that the job should run (`0-6` for Sunday-Saturday, `*`, and so on).  Default: `"*"` |

## [Attributes](cron_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | Platform: posix | Target OS/families that can be operated against |

## [Examples](cron_module.md#id5)

```yaml+jinja
- name: Ensure a job that runs at 2 and 5 exists. Creates an entry like "0 5,2 * * ls -alh > /dev/null"
  ansible.builtin.cron:
    name: "check dirs"
    minute: "0"
    hour: "5,2"
    job: "ls -alh > /dev/null"

- name: 'Ensure an old job is no longer present. Removes any job that is prefixed by "#Ansible: an old job" from the crontab'
  ansible.builtin.cron:
    name: "an old job"
    state: absent

- name: Creates an entry like "@reboot /some/job.sh"
  ansible.builtin.cron:
    name: "a job for reboot"
    special_time: reboot
    job: "/some/job.sh"

- name: Creates an entry like "PATH=/opt/bin" on top of crontab
  ansible.builtin.cron:
    name: PATH
    env: yes
    job: /opt/bin

- name: Creates an entry like "APP_HOME=/srv/app" and insert it after PATH declaration
  ansible.builtin.cron:
    name: APP_HOME
    env: yes
    job: /srv/app
    insertafter: PATH

- name: Creates a cron file under /etc/cron.d
  ansible.builtin.cron:
    name: yum autoupdate
    weekday: "2"
    minute: "0"
    hour: "12"
    user: root
    job: "YUMINTERACTIVE=0 /usr/sbin/yum-autoupdate"
    cron_file: ansible_yum-autoupdate

- name: Removes a cron file from under /etc/cron.d
  ansible.builtin.cron:
    name: "yum autoupdate"
    cron_file: ansible_yum-autoupdate
    state: absent

- name: Removes "APP_HOME" environment variable from crontab
  ansible.builtin.cron:
    name: APP_HOME
    env: yes
    state: absent
```

### Authors

- Dane Summers (@dsummersl)
- Mike Grozak (@rhaido)
- Patrick Callahan (@dirtyharrycallahan)
- Evan Kaufman (@EvanK)
- Luca Berruti (@lberruti)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
