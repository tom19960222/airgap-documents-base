---
collection: ansible
version: "6"
title: "community.general.sudoers module – Manage sudoers files"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/sudoers_module.html
fetched_at: 2026-07-27T17:13:26+00:00
---
# community.general.sudoers module – Manage sudoers files

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
> To use it in a playbook, specify: `community.general.sudoers`.

New in community.general 4.3.0

- [Synopsis](sudoers_module.md#synopsis)
- [Parameters](sudoers_module.md#parameters)
- [Examples](sudoers_module.md#examples)

## [Synopsis](sudoers_module.md#id1)

- This module allows for the manipulation of sudoers files.

## [Parameters](sudoers_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=string | The commands allowed by the sudoers rule.  Multiple can be added by passing a list of commands.  Use `ALL` for all commands. |
| **group**  string | The name of the group for the sudoers rule.  This option cannot be used in conjunction with *user*. |
| **name**  string / required | The name of the sudoers rule.  This will be used for the filename for the sudoers file managed by this rule. |
| **nopassword**  boolean | Whether a password will be required to run the sudo’d command.  Choices:   - `false` - `true` ← (default) |
| **runas**  string  added in community.general 4.7.0 | Specify the target user the command(s) will run as. |
| **state**  string | Whether the rule should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **sudoers_path**  string | The path which sudoers config files will be managed in.  Default: `"/etc/sudoers.d"` |
| **user**  string | The name of the user for the sudoers rule.  This option cannot be used in conjunction with *group*. |
| **validation**  string  added in community.general 5.2.0 | If `absent`, the sudoers rule will be added without validation.  If `detect` and visudo is available, then the sudoers rule will be validated by visudo.  If `required`, visudo must be available to validate the sudoers rule.  Choices:   - `"absent"` - `"detect"` ← (default) - `"required"` |

## [Examples](sudoers_module.md#id3)

```yaml+jinja
- name: Allow the backup user to sudo /usr/local/bin/backup
  community.general.sudoers:
    name: allow-backup
    state: present
    user: backup
    commands: /usr/local/bin/backup

- name: Allow the bob user to run any commands as alice with sudo -u alice
  community.general.sudoers:
    name: bob-do-as-alice
    state: present
    user: bob
    runas: alice
    commands: ALL

- name: >-
    Allow the monitoring group to run sudo /usr/local/bin/gather-app-metrics
    without requiring a password
  community.general.sudoers:
    name: monitor-app
    group: monitoring
    commands: /usr/local/bin/gather-app-metrics

- name: >-
    Allow the alice user to run sudo /bin/systemctl restart my-service or
    sudo /bin/systemctl reload my-service, but a password is required
  community.general.sudoers:
    name: alice-service
    user: alice
    commands:
      - /bin/systemctl restart my-service
      - /bin/systemctl reload my-service
    nopassword: false

- name: Revoke the previous sudo grants given to the alice user
  community.general.sudoers:
    name: alice-service
    state: absent
```

### Authors

- Jon Ellis (@JonEllis)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
