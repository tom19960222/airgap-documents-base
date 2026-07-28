---
collection: ansible
version: "8"
title: "community.general.bundler module – Manage Ruby Gem dependencies with Bundler"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/bundler_module.html
fetched_at: 2026-07-28T01:44:53+00:00
---
# community.general.bundler module – Manage Ruby Gem dependencies with Bundler

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
> To use it in a playbook, specify: `community.general.bundler`.

- [Synopsis](bundler_module.md#synopsis)
- [Parameters](bundler_module.md#parameters)
- [Attributes](bundler_module.md#attributes)
- [Examples](bundler_module.md#examples)

## [Synopsis](bundler_module.md#id1)

- Manage installation and Gem version dependencies for Ruby using the Bundler gem

Aliases: packaging.language.bundler

## [Parameters](bundler_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **binstub_directory**  path | Only applies if `state=present`. Specifies the directory to install any gem bins files to. When executed the bin files will run within the context of the Gemfile and fail if any required gem dependencies are not installed. If `chdir` is set then this path is relative to `chdir` |
| **chdir**  path | The directory to execute the bundler commands from. This directory needs to contain a valid Gemfile or .bundle/ directory  If not specified, it will default to the temporary working directory |
| **clean**  boolean | Only applies if `state=present`. If set removes any gems on the target host that are not in the gemfile  **Choices:**   - `false` ← (default) - `true` |
| **deployment_mode**  boolean | Only applies if `state=present`. If set it will install gems in ./vendor/bundle instead of the default location. Requires a Gemfile.lock file to have been created prior  **Choices:**   - `false` ← (default) - `true` |
| **exclude_groups**  list / elements=string | A list of Gemfile groups to exclude during operations. This only applies when `state=present`. Bundler considers this a ‘remembered’ property for the Gemfile and will automatically exclude groups in future operations even if `exclude_groups` is not set |
| **executable**  string | The path to the bundler executable |
| **extra_args**  string | A space separated string of additional commands that can be applied to the Bundler command. Refer to the Bundler documentation for more information |
| **gem_path**  path | Only applies if `state=present`. Specifies the directory to install the gems into. If `chdir` is set then this path is relative to `chdir`  If not specified the default RubyGems gem paths will be used. |
| **gemfile**  path | Only applies if `state=present`. The path to the gemfile to use to install gems.  If not specified it will default to the Gemfile in current directory |
| **local**  boolean | If set only installs gems from the cache on the target host  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | The desired state of the Gem bundle. `latest` updates gems to the most recent, acceptable version  **Choices:**   - `"present"` ← (default) - `"latest"` |
| **user_install**  boolean | Only applies if `state=present`. Installs gems in the local user’s cache or for all users  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](bundler_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](bundler_module.md#id4)

```yaml+jinja
- name: Install gems from a Gemfile in the current directory
  community.general.bundler:
    state: present
    executable: ~/.rvm/gems/2.1.5/bin/bundle

- name: Exclude the production group from installing
  community.general.bundler:
    state: present
    exclude_groups: production

- name: Install gems into ./vendor/bundle
  community.general.bundler:
    state: present
    deployment_mode: true

- name: Install gems using a Gemfile in another directory
  community.general.bundler:
    state: present
    gemfile: ../rails_project/Gemfile

- name: Update Gemfile in another directory
  community.general.bundler:
    state: latest
    chdir: ~/rails_project
```

### Authors

- Tim Hoiberg (@thoiberg)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
