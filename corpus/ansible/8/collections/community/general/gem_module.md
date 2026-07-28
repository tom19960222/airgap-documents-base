---
collection: ansible
version: "8"
title: "community.general.gem module – Manage Ruby gems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/gem_module.html
fetched_at: 2026-07-28T01:45:38+00:00
---
# community.general.gem module – Manage Ruby gems

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.gem`.

- [Synopsis](gem_module.md#synopsis)
- [Parameters](gem_module.md#parameters)
- [Attributes](gem_module.md#attributes)
- [Examples](gem_module.md#examples)

## [Synopsis](gem_module.md#id1)

- Manage installation and uninstallation of Ruby gems.

Aliases: packaging.language.gem

## [Parameters](gem_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bindir**  path  *added in community.general 3.3.0* | Install executables into a specific directory. |
| **build_flags**  string | Allow adding build flags for gem compilation |
| **env_shebang**  boolean | Rewrite the shebang line on installed scripts to use /usr/bin/env.  **Choices:**   - `false` ← (default) - `true` |
| **executable**  path | Override the path to the gem executable |
| **force**  boolean | Force gem to (un-)install, bypassing dependency checks.  **Choices:**   - `false` ← (default) - `true` |
| **gem_source**  path | The path to a local gem used as installation source. |
| **include_dependencies**  boolean | Whether to include dependencies or not.  **Choices:**   - `false` - `true` ← (default) |
| **include_doc**  boolean | Install with or without docs.  **Choices:**   - `false` ← (default) - `true` |
| **install_dir**  path | Install the gems into a specific directory. These gems will be independent from the global installed ones. Specifying this requires user_install to be false. |
| **name**  string / required | The name of the gem to be managed. |
| **norc**  boolean  *added in community.general 3.3.0* | Avoid loading any `.gemrc` file. Ignored for RubyGems prior to 2.5.2.  The default changed from `false` to `true` in community.general 6.0.0.  **Choices:**   - `false` - `true` ← (default) |
| **pre_release**  boolean | Allow installation of pre-release versions of the gem.  **Choices:**   - `false` ← (default) - `true` |
| **repository**  aliases: source  string | The repository from which the gem will be installed |
| **state**  string | The desired state of the gem. `latest` ensures that the latest version is installed.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"latest"` |
| **user_install**  boolean | Install gem in user’s local gems cache or for all users  **Choices:**   - `false` - `true` ← (default) |
| **version**  string | Version of the gem to be installed/removed. |

## [Attributes](gem_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](gem_module.md#id4)

```yaml+jinja
- name: Install version 1.0 of vagrant
  community.general.gem:
    name: vagrant
    version: 1.0
    state: present

- name: Install latest available version of rake
  community.general.gem:
    name: rake
    state: latest

- name: Install rake version 1.0 from a local gem on disk
  community.general.gem:
    name: rake
    gem_source: /path/to/gems/rake-1.0.gem
    state: present
```

### Authors

- Ansible Core Team
- Johan Wiren (@johanwiren)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
