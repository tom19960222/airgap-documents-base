---
collection: ansible
version: "8"
title: "community.general.npm module – Manage node.js packages with npm"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/npm_module.html
fetched_at: 2026-07-28T01:48:12+00:00
---
# community.general.npm module – Manage node.js packages with npm

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
> see [Requirements](npm_module.md#ansible-collections-community-general-npm-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.npm`.

- [Synopsis](npm_module.md#synopsis)
- [Requirements](npm_module.md#requirements)
- [Parameters](npm_module.md#parameters)
- [Attributes](npm_module.md#attributes)
- [Examples](npm_module.md#examples)

## [Synopsis](npm_module.md#id1)

- Manage node.js packages with Node Package Manager (npm).

Aliases: packaging.language.npm

## [Requirements](npm_module.md#id2)

The below requirements are needed on the host that executes this module.

- npm installed in bin path (recommended /usr/local/bin)

## [Parameters](npm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ci**  boolean | Install packages based on package-lock file, same as running `npm ci`.  **Choices:**   - `false` ← (default) - `true` |
| **executable**  path | The executable location for npm.  This is useful if you are using a version manager, such as nvm. |
| **global**  boolean | Install the node.js library globally.  **Choices:**   - `false` ← (default) - `true` |
| **ignore_scripts**  boolean | Use the `--ignore-scripts` flag when installing.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | The name of a node.js library to install. |
| **no_bin_links**  boolean  *added in community.general 2.5.0* | Use the `--no-bin-links` flag when installing.  **Choices:**   - `false` ← (default) - `true` |
| **no_optional**  boolean  *added in community.general 2.0.0* | Use the `--no-optional` flag when installing.  **Choices:**   - `false` ← (default) - `true` |
| **path**  path | The base path where to install the node.js libraries. |
| **production**  boolean | Install dependencies in production mode, excluding devDependencies.  **Choices:**   - `false` ← (default) - `true` |
| **registry**  string | The registry to install modules from. |
| **state**  string | The state of the node.js library.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"latest"` |
| **unsafe_perm**  boolean | Use the `--unsafe-perm` flag when installing.  **Choices:**   - `false` ← (default) - `true` |
| **version**  string | The version to be installed. |

## [Attributes](npm_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](npm_module.md#id5)

```yaml+jinja
- name: Install "coffee-script" node.js package.
  community.general.npm:
    name: coffee-script
    path: /app/location

- name: Install "coffee-script" node.js package on version 1.6.1.
  community.general.npm:
    name: coffee-script
    version: '1.6.1'
    path: /app/location

- name: Install "coffee-script" node.js package globally.
  community.general.npm:
    name: coffee-script
    global: true

- name: Remove the globally package "coffee-script".
  community.general.npm:
    name: coffee-script
    global: true
    state: absent

- name: Install "coffee-script" node.js package from custom registry.
  community.general.npm:
    name: coffee-script
    registry: 'http://registry.mysite.com'

- name: Install packages based on package.json.
  community.general.npm:
    path: /app/location

- name: Update packages based on package.json to their latest version.
  community.general.npm:
    path: /app/location
    state: latest

- name: Install packages based on package.json using the npm installed with nvm v0.10.1.
  community.general.npm:
    path: /app/location
    executable: /opt/nvm/v0.10.1/bin/npm
    state: present
```

### Authors

- Chris Hoffman (@chrishoffman)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
