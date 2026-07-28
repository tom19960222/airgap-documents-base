---
collection: ansible
version: "8"
title: "community.general.sorcery module – Package manager for Source Mage GNU/Linux"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/sorcery_module.html
fetched_at: 2026-07-28T01:50:42+00:00
---
# community.general.sorcery module – Package manager for Source Mage GNU/Linux

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
> see [Requirements](sorcery_module.md#ansible-collections-community-general-sorcery-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.sorcery`.

- [Synopsis](sorcery_module.md#synopsis)
- [Requirements](sorcery_module.md#requirements)
- [Parameters](sorcery_module.md#parameters)
- [Attributes](sorcery_module.md#attributes)
- [Notes](sorcery_module.md#notes)
- [Examples](sorcery_module.md#examples)

## [Synopsis](sorcery_module.md#id1)

- Manages “spells” on Source Mage GNU/Linux using *sorcery* toolchain

Aliases: packaging.os.sorcery

## [Requirements](sorcery_module.md#id2)

The below requirements are needed on the host that executes this module.

- bash

## [Parameters](sorcery_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cache_valid_time**  integer | Time in seconds to invalidate grimoire collection on update.  Especially useful for SCM and rsync grimoires.  Makes sense only in pair with `update_cache`.  **Default:** `0` |
| **depends**  string | Comma-separated list of _optional_ dependencies to build a spell (or make sure it is built) with; use `+`/`-` in front of dependency to turn it on/off (`+` is optional though).  This option is ignored if `name` parameter is equal to `*` or contains more than one spell.  Providers must be supplied in the form recognized by Sorcery, for example ‘`openssl(SSL)`‘. |
| **name**  aliases: spell, grimoire  list / elements=string | Name of the spell or grimoire.  Multiple names can be given, separated by commas.  Special value `*` in conjunction with states `latest` or `rebuild` will update or rebuild the whole system respectively  The alias `grimoire` was added in community.general 7.3.0. |
| **repository**  string  *added in community.general 7.3.0* | Repository location.  If specified, `name` represents grimoire(s) instead of spell(s).  Special value `*` will pull grimoire from the official location.  Only single item in `name` in conjunction with `*` can be used.  `state=absent` must be used with a special value `*`. |
| **state**  string | Whether to cast, dispel or rebuild a package.  State `cast` is an equivalent of `present`, not `latest`.  State `rebuild` implies cast of all specified spells, not only those existed before.  **Choices:**   - `"present"` ← (default) - `"latest"` - `"absent"` - `"cast"` - `"dispelled"` - `"rebuild"` |
| **update**  boolean | Whether or not to update sorcery scripts at the very first stage.  **Choices:**   - `false` ← (default) - `true` |
| **update_cache**  aliases: update_codex  boolean | Whether or not to update grimoire collection before casting spells.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](sorcery_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](sorcery_module.md#id5)

> **Note:**
>
> - When all three components are selected, the update goes by the sequence – Sorcery -> Grimoire(s) -> Spell(s); you cannot override it.
> - Grimoire handling is supported since community.general 7.3.0.

## [Examples](sorcery_module.md#id6)

```yaml+jinja
- name: Make sure spell foo is installed
  community.general.sorcery:
    spell: foo
    state: present

- name: Make sure spells foo, bar and baz are removed
  community.general.sorcery:
    spell: foo,bar,baz
    state: absent

- name: Make sure spell foo with dependencies bar and baz is installed
  community.general.sorcery:
    spell: foo
    depends: bar,baz
    state: present

- name: Make sure spell foo with bar and without baz dependencies is installed
  community.general.sorcery:
    spell: foo
    depends: +bar,-baz
    state: present

- name: Make sure spell foo with libressl (providing SSL) dependency is installed
  community.general.sorcery:
    spell: foo
    depends: libressl(SSL)
    state: present

- name: Make sure spells with/without required dependencies (if any) are installed
  community.general.sorcery:
    name: "{{ item.spell }}"
    depends: "{{ item.depends | default(None) }}"
    state: present
  loop:
    - { spell: 'vifm', depends: '+file,-gtk+2' }
    - { spell: 'fwknop', depends: 'gpgme' }
    - { spell: 'pv,tnftp,tor' }

- name: Install the latest version of spell foo using regular glossary
  community.general.sorcery:
    name: foo
    state: latest

- name: Rebuild spell foo
  community.general.sorcery:
    spell: foo
    state: rebuild

- name: Rebuild the whole system, but update Sorcery and Codex first
  community.general.sorcery:
    spell: '*'
    state: rebuild
    update: true
    update_cache: true

- name: Refresh the grimoire collection if it is 1 day old using native sorcerous alias
  community.general.sorcery:
    update_codex: true
    cache_valid_time: 86400

- name: Make sure stable grimoire is present
  community.general.sorcery:
    name: stable
    repository: '*'
    state: present

- name: Make sure binary and stable-rc grimoires are removed
  community.general.sorcery:
    grimoire: binary,stable-rc
    repository: '*'
    state: absent

- name: Make sure games grimoire is pulled from rsync
  community.general.sorcery:
    grimoire: games
    repository: "rsync://download.sourcemage.org::codex/games"
    state: present

- name: Make sure a specific branch of stable grimoire is pulled from git
  community.general.sorcery:
    grimoire: stable.git
    repository: "git://download.sourcemage.org/smgl/grimoire.git:stable.git:stable-0.62"
    state: present

- name: Update only Sorcery itself
  community.general.sorcery:
    update: true
```

### Authors

- Vlad Glagolev (@vaygr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
