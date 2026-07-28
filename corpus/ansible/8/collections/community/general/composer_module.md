---
collection: ansible
version: "8"
title: "community.general.composer module – Dependency Manager for PHP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/composer_module.html
fetched_at: 2026-07-28T01:45:09+00:00
---
# community.general.composer module – Dependency Manager for PHP

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
> see [Requirements](composer_module.md#ansible-collections-community-general-composer-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.composer`.

- [Synopsis](composer_module.md#synopsis)
- [Requirements](composer_module.md#requirements)
- [Parameters](composer_module.md#parameters)
- [Attributes](composer_module.md#attributes)
- [Notes](composer_module.md#notes)
- [Examples](composer_module.md#examples)

## [Synopsis](composer_module.md#id1)

- Composer is a tool for dependency management in PHP. It allows you to declare the dependent libraries your project needs and it will install them in your project for you.

Aliases: packaging.language.composer

## [Requirements](composer_module.md#id2)

The below requirements are needed on the host that executes this module.

- php
- composer installed in bin path (recommended /usr/local/bin) or specified in `composer_executable`

## [Parameters](composer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **apcu_autoloader**  boolean | Uses APCu to cache found/not-found classes  **Choices:**   - `false` ← (default) - `true` |
| **arguments**  string | Composer arguments like required package, version and so on.  **Default:** `""` |
| **classmap_authoritative**  boolean | Autoload classes from classmap only.  Implicitly enable optimize_autoloader.  Recommended especially for production, but can take a bit of time to run.  **Choices:**   - `false` ← (default) - `true` |
| **command**  string | Composer command like “install”, “update” and so on.  **Default:** `"install"` |
| **composer_executable**  path  *added in community.general 3.2.0* | Path to composer executable on the remote host, if composer is not in `PATH` or a custom composer is needed. |
| **executable**  aliases: php_path  path | Path to PHP Executable on the remote host, if PHP is not in PATH. |
| **global_command**  boolean | Runs the specified command globally.  **Choices:**   - `false` ← (default) - `true` |
| **ignore_platform_reqs**  boolean | Ignore php, hhvm, lib-\* and ext-\* requirements and force the installation even if the local machine does not fulfill these.  **Choices:**   - `false` ← (default) - `true` |
| **no_dev**  boolean | Disables installation of require-dev packages (see –no-dev).  **Choices:**   - `false` - `true` ← (default) |
| **no_plugins**  boolean | Disables all plugins (see –no-plugins).  **Choices:**   - `false` ← (default) - `true` |
| **no_scripts**  boolean | Skips the execution of all scripts defined in composer.json (see –no-scripts).  **Choices:**   - `false` ← (default) - `true` |
| **optimize_autoloader**  boolean | Optimize autoloader during autoloader dump (see –optimize-autoloader).  Convert PSR-0/4 autoloading to classmap to get a faster autoloader.  Recommended especially for production, but can take a bit of time to run.  **Choices:**   - `false` - `true` ← (default) |
| **prefer_dist**  boolean | Forces installation from package dist even for dev versions (see –prefer-dist).  **Choices:**   - `false` ← (default) - `true` |
| **prefer_source**  boolean | Forces installation from package sources when possible (see –prefer-source).  **Choices:**   - `false` ← (default) - `true` |
| **working_dir**  path | Directory of your project (see –working-dir). This is required when the command is not run globally.  Will be ignored if `global_command=true`. |

## [Attributes](composer_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](composer_module.md#id5)

> **Note:**
>
> - Default options that are always appended in each execution are –no-ansi, –no-interaction and –no-progress if available.
> - We received reports about issues on macOS if composer was installed by Homebrew. Please use the official install method to avoid issues.

## [Examples](composer_module.md#id6)

```yaml+jinja
- name: Download and installs all libs and dependencies outlined in the /path/to/project/composer.lock
  community.general.composer:
    command: install
    working_dir: /path/to/project

- name: Install a new package
  community.general.composer:
    command: require
    arguments: my/package
    working_dir: /path/to/project

- name: Clone and install a project with all dependencies
  community.general.composer:
    command: create-project
    arguments: package/package /path/to/project ~1.0
    working_dir: /path/to/project
    prefer_dist: true

- name: Install a package globally
  community.general.composer:
    command: require
    global_command: true
    arguments: my/package
```

### Authors

- Dimitrios Tydeas Mengidis (@dmtrs)
- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
