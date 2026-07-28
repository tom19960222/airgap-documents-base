---
collection: ansible
version: "8"
title: "community.general.cpanm module – Manages Perl library dependencies"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/cpanm_module.html
fetched_at: 2026-07-28T01:45:15+00:00
---
# community.general.cpanm module – Manages Perl library dependencies

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
> To use it in a playbook, specify: `community.general.cpanm`.

- [Synopsis](cpanm_module.md#synopsis)
- [Parameters](cpanm_module.md#parameters)
- [Attributes](cpanm_module.md#attributes)
- [Notes](cpanm_module.md#notes)
- [Examples](cpanm_module.md#examples)

## [Synopsis](cpanm_module.md#id1)

- Manage Perl library dependencies using cpanminus.

Aliases: packaging.language.cpanm

## [Parameters](cpanm_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **executable**  path | Override the path to the cpanm executable. |
| **from_path**  path | The local directory or `tar.gz` file to install from. |
| **installdeps**  boolean | Only install dependencies.  **Choices:**   - `false` ← (default) - `true` |
| **locallib**  path | Specify the install base to install modules. |
| **mirror**  string | Specifies the base URL for the CPAN mirror to use. |
| **mirror_only**  boolean | Use the mirror’s index file instead of the CPAN Meta DB.  **Choices:**   - `false` ← (default) - `true` |
| **mode**  string  *added in community.general 3.0.0* | Controls the module behavior. See notes below for more details.  Default is `compatibility` but that behavior is deprecated and will be changed to `new` in community.general 9.0.0.  **Choices:**   - `"compatibility"` - `"new"` |
| **name**  aliases: pkg  string | The Perl library to install. Valid values change according to the `mode`, see notes for more details.  Note that for installing from a local path the parameter `from_path` should be used. |
| **name_check**  string  *added in community.general 3.0.0* | When `mode=new`, this parameter can be used to check if there is a module `name` installed (at `version`, when specified). |
| **notest**  boolean | Do not run unit tests.  **Choices:**   - `false` ← (default) - `true` |
| **version**  string | Version specification for the perl module. When `mode` is `new`, `cpanm` version operators are accepted. |

## [Attributes](cpanm_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](cpanm_module.md#id4)

> **Note:**
>
> - Please note that <http://search.cpan.org/dist/App-cpanminus/bin/cpanm,%20cpanm> must be installed on the remote host.
> - This module now comes with a choice of execution `mode`: `compatibility` or `new`.
> - `mode=compatibility`: When using `compatibility` mode, the module will keep backward compatibility. This is the default mode. `name` must be either a module name or a distribution file. If the perl module given by `name` is installed (at the exact `version` when specified), then nothing happens. Otherwise, it will be installed using the `cpanm` executable. `name` cannot be an URL, or a git URL. `cpanm` version specifiers do not work in this mode.
> - `mode=new`: When using `new` mode, the module will behave differently. The `name` parameter may refer to a module name, a distribution file, a HTTP URL or a git repository URL as described in `cpanminus` documentation. `cpanm` version specifiers are recognized.

## [Examples](cpanm_module.md#id5)

```yaml+jinja
- name: Install Dancer perl package
  community.general.cpanm:
    name: Dancer

- name: Install version 0.99_05 of the Plack perl package
  community.general.cpanm:
    name: MIYAGAWA/Plack-0.99_05.tar.gz

- name: Install Dancer into the specified locallib
  community.general.cpanm:
    name: Dancer
    locallib: /srv/webapps/my_app/extlib

- name: Install perl dependencies from local directory
  community.general.cpanm:
    from_path: /srv/webapps/my_app/src/

- name: Install Dancer perl package without running the unit tests in indicated locallib
  community.general.cpanm:
    name: Dancer
    notest: true
    locallib: /srv/webapps/my_app/extlib

- name: Install Dancer perl package from a specific mirror
  community.general.cpanm:
    name: Dancer
    mirror: 'http://cpan.cpantesters.org/'

- name: Install Dancer perl package into the system root path
  become: true
  community.general.cpanm:
    name: Dancer

- name: Install Dancer if it is not already installed OR the installed version is older than version 1.0
  community.general.cpanm:
    name: Dancer
    version: '1.0'
```

### Authors

- Franck Cuny (@fcuny)
- Alexei Znamensky (@russoz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
