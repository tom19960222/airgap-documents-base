---
collection: ansible
version: "8"
title: "community.general.pnpm module – Manage node.js packages with pnpm"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pnpm_module.html
fetched_at: 2026-07-28T01:49:07+00:00
---
# community.general.pnpm module – Manage node.js packages with pnpm

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
> see [Requirements](pnpm_module.md#ansible-collections-community-general-pnpm-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.pnpm`.

New in community.general 7.4.0

- [Synopsis](pnpm_module.md#synopsis)
- [Requirements](pnpm_module.md#requirements)
- [Parameters](pnpm_module.md#parameters)
- [Attributes](pnpm_module.md#attributes)
- [Examples](pnpm_module.md#examples)

## [Synopsis](pnpm_module.md#id1)

- Manage node.js packages with the [pnpm package manager](https://pnpm.io/).

## [Requirements](pnpm_module.md#id2)

The below requirements are needed on the host that executes this module.

- Pnpm executable present in `PATH`.

## [Parameters](pnpm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alias**  string | Alias of the node.js library. |
| **dev**  boolean | Install dependencies in development mode.  Pnpm will ignore any regular dependencies in `package.json`.  **Choices:**   - `false` ← (default) - `true` |
| **executable**  path | The executable location for pnpm.  The default location it searches for is `PATH`, fails if not set. |
| **global**  boolean | Install the node.js library globally.  **Choices:**   - `false` ← (default) - `true` |
| **ignore_scripts**  boolean | Use the `--ignore-scripts` flag when installing.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | The name of a node.js library to install.  All packages in package.json are installed if not provided. |
| **no_optional**  boolean | Do not install optional packages, equivalent to `--no-optional`.  **Choices:**   - `false` ← (default) - `true` |
| **optional**  boolean | Install dependencies in optional mode.  **Choices:**   - `false` ← (default) - `true` |
| **path**  path | The base path to install the node.js libraries. |
| **production**  boolean | Install dependencies in production mode.  Pnpm will ignore any dependencies under `devDependencies` in package.json.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Installation state of the named node.js library.  If `absent` is selected, a name option must be provided.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"latest"` |
| **version**  string | The version of the library to be installed, in semver format. |

## [Attributes](pnpm_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](pnpm_module.md#id5)

```yaml+jinja
- name: Install "tailwindcss" node.js package.
  community.general.pnpm:
    name: tailwindcss
    path: /app/location

- name: Install "tailwindcss" node.js package on version 3.3.2
  community.general.pnpm:
    name: tailwindcss
    version: 3.3.2
    path: /app/location

- name: Install "tailwindcss" node.js package globally.
  community.general.pnpm:
    name: tailwindcss
    global: true

- name: Install "tailwindcss" node.js package as dev dependency.
  community.general.pnpm:
    name: tailwindcss
    path: /app/location
    dev: true

- name: Install "tailwindcss" node.js package as optional dependency.
  community.general.pnpm:
    name: tailwindcss
    path: /app/location
    optional: true

- name: Install "tailwindcss" node.js package version 0.1.3 as tailwind-1
  community.general.pnpm:
    name: tailwindcss
    alias: tailwind-1
    version: 0.1.3
    path: /app/location

- name: Remove the globally-installed package "tailwindcss".
  community.general.pnpm:
    name: tailwindcss
    global: true
    state: absent

- name: Install packages based on package.json.
  community.general.pnpm:
    path: /app/location

- name: Update all packages in package.json to their latest version.
  community.general.pnpm:
    path: /app/location
    state: latest
```

### Authors

- Aritra Sen (@aretrosen)
- Chris Hoffman (@chrishoffman), creator of NPM Ansible module

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
