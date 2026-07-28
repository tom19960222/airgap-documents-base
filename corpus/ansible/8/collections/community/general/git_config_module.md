---
collection: ansible
version: "8"
title: "community.general.git_config module – Read and write git configuration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/git_config_module.html
fetched_at: 2026-07-28T01:45:40+00:00
---
# community.general.git_config module – Read and write git configuration

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](git_config_module.md#ansible-collections-community-general-git-config-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.git_config`.

- [Synopsis](git_config_module.md#synopsis)
- [Requirements](git_config_module.md#requirements)
- [Parameters](git_config_module.md#parameters)
- [Attributes](git_config_module.md#attributes)
- [Examples](git_config_module.md#examples)
- [Return Values](git_config_module.md#return-values)

## [Synopsis](git_config_module.md#id1)

- The [community.general.git_config](git_config_module.md#ansible-collections-community-general-git-config-module) module changes git configuration by invoking ‘git config’. This is needed if you do not want to use [ansible.builtin.template](../../ansible/builtin/template_module.md#ansible-collections-ansible-builtin-template-module) for the entire git config file (for example because you need to change just `user.email` in /etc/.git/config). Solutions involving [ansible.builtin.command](../../ansible/builtin/command_module.md#ansible-collections-ansible-builtin-command-module) are cumbersome or do not work correctly in check mode.

Aliases: source_control.git_config

## [Requirements](git_config_module.md#id2)

The below requirements are needed on the host that executes this module.

- git

## [Parameters](git_config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **file**  path  *added in community.general 2.0.0* | Path to an adhoc git configuration file to be managed using the `file` scope. |
| **list_all**  boolean | List all settings (optionally limited to a given `scope`).  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | The name of the setting. If no value is supplied, the value will be read from the config if it has been set. |
| **repo**  path | Path to a git repository for reading and writing values from a specific repo. |
| **scope**  string | Specify which scope to read/set values from.  This is required when setting config values.  If this is set to `local`, you must also specify the `repo` parameter.  If this is set to `file`, you must also specify the `file` parameter.  It defaults to system only when not using `list_all=true`.  **Choices:**   - `"file"` - `"local"` - `"global"` - `"system"` |
| **state**  string | Indicates the setting should be set/unset. This parameter has higher precedence than `value` parameter: when `state=absent` and `value` is defined, `value` is discarded.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **value**  string | When specifying the name of a single setting, supply a value to set that setting to the given value. |

## [Attributes](git_config_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](git_config_module.md#id5)

```yaml+jinja
- name: Add a setting to ~/.gitconfig
  community.general.git_config:
    name: alias.ci
    scope: global
    value: commit

- name: Add a setting to ~/.gitconfig
  community.general.git_config:
    name: alias.st
    scope: global
    value: status

- name: Remove a setting from ~/.gitconfig
  community.general.git_config:
    name: alias.ci
    scope: global
    state: absent

- name: Add a setting to ~/.gitconfig
  community.general.git_config:
    name: core.editor
    scope: global
    value: vim

- name: Add a setting system-wide
  community.general.git_config:
    name: alias.remotev
    scope: system
    value: remote -v

- name: Add a setting to a system scope (default)
  community.general.git_config:
    name: alias.diffc
    value: diff --cached

- name: Add a setting to a system scope (default)
  community.general.git_config:
    name: color.ui
    value: auto

- name: Make etckeeper not complaining when it is invoked by cron
  community.general.git_config:
    name: user.email
    repo: /etc
    scope: local
    value: 'root@{{ ansible_fqdn }}'

- name: Read individual values from git config
  community.general.git_config:
    name: alias.ci
    scope: global

- name: Scope system is also assumed when reading values, unless list_all=true
  community.general.git_config:
    name: alias.diffc

- name: Read all values from git config
  community.general.git_config:
    list_all: true
    scope: global

- name: When list_all is yes and no scope is specified, you get configuration from all scopes
  community.general.git_config:
    list_all: true

- name: Specify a repository to include local settings
  community.general.git_config:
    list_all: true
    repo: /path/to/repo.git
```

## [Return Values](git_config_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **config_value**  string | When `list_all=false` and value is not set, a string containing the value of the setting in name  **Returned:** success  **Sample:** `"vim"` |
| **config_values**  dictionary | When `list_all=true`, a dict containing key/value pairs of multiple configuration settings  **Returned:** success  **Sample:** `{"alias.diffc": "diff --cached", "alias.remotev": "remote -v", "color.ui": "auto", "core.editor": "vim"}` |

### Authors

- Matthew Gamble (@djmattyg007)
- Marius Gedminas (@mgedmin)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
