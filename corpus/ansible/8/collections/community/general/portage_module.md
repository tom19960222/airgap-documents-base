---
collection: ansible
version: "8"
title: "community.general.portage module – Package manager for Gentoo"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/portage_module.html
fetched_at: 2026-07-28T01:49:08+00:00
---
# community.general.portage module – Package manager for Gentoo

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
> To use it in a playbook, specify: `community.general.portage`.

- [Synopsis](portage_module.md#synopsis)
- [Parameters](portage_module.md#parameters)
- [Attributes](portage_module.md#attributes)
- [Examples](portage_module.md#examples)

## [Synopsis](portage_module.md#id1)

- Manages Gentoo packages

Aliases: packaging.os.portage

## [Parameters](portage_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backtrack**  integer  *added in community.general 5.8.0* | Set backtrack value (`--backtrack`). |
| **changed_use**  boolean | Include installed packages where USE flags have changed, except when  flags that the user has not enabled are added or removed  (–changed-use)  **Choices:**   - `false` ← (default) - `true` |
| **deep**  boolean | Consider the entire dependency tree of packages (–deep)  **Choices:**   - `false` ← (default) - `true` |
| **depclean**  boolean | Remove packages not needed by explicitly merged packages (–depclean)  If no package is specified, clean up the world’s dependencies  Otherwise, –depclean serves as a dependency aware version of –unmerge  **Choices:**   - `false` ← (default) - `true` |
| **getbinpkg**  boolean | Prefer packages specified at `PORTAGE_BINHOST` in `make.conf`.  **Choices:**   - `false` ← (default) - `true` |
| **getbinpkgonly**  boolean  *added in community.general 1.3.0* | Merge only packages specified at `PORTAGE_BINHOST` in `make.conf`.  **Choices:**   - `false` ← (default) - `true` |
| **jobs**  integer | Specifies the number of packages to build simultaneously.  Since version 2.6: Value of 0 or False resets any previously added  –jobs setting values |
| **keepgoing**  boolean | Continue as much as possible after an error.  **Choices:**   - `false` ← (default) - `true` |
| **loadavg**  float | Specifies that no new builds should be started if there are  other builds running and the load average is at least LOAD  Since version 2.6: Value of 0 or False resets any previously added  –load-average setting values |
| **newuse**  boolean | Include installed packages where USE flags have changed (–newuse)  **Choices:**   - `false` ← (default) - `true` |
| **nodeps**  boolean | Only merge packages but not their dependencies (–nodeps)  **Choices:**   - `false` ← (default) - `true` |
| **noreplace**  boolean | Do not re-emerge installed packages (–noreplace)  **Choices:**   - `false` - `true` ← (default) |
| **oneshot**  boolean | Do not add the packages to the world file (–oneshot)  **Choices:**   - `false` ← (default) - `true` |
| **onlydeps**  boolean | Only merge packages’ dependencies but not the packages (–onlydeps)  **Choices:**   - `false` ← (default) - `true` |
| **package**  aliases: name  list / elements=string | Package atom or set, for example `sys-apps/foo` or `>foo-2.13` or `@world` |
| **quiet**  boolean | Run emerge in quiet mode (–quiet)  **Choices:**   - `false` ← (default) - `true` |
| **quietbuild**  boolean | Redirect all build output to logs alone, and do not display it  on stdout (–quiet-build)  **Choices:**   - `false` ← (default) - `true` |
| **quietfail**  boolean | Suppresses display of the build log on stdout (–quiet-fail)  Only the die message and the path of the build log will be  displayed on stdout.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | State of the package atom  **Choices:**   - `"present"` ← (default) - `"installed"` - `"emerged"` - `"absent"` - `"removed"` - `"unmerged"` - `"latest"` |
| **sync**  string | Sync package repositories first  If `yes`, perform “emerge –sync”  If `web`, perform “emerge-webrsync”  **Choices:**   - `"web"` - `"yes"` - `"no"` |
| **update**  boolean | Update packages to the best version available (–update)  **Choices:**   - `false` ← (default) - `true` |
| **usepkg**  boolean | Tries to use the binary package(s) in the locally available packages directory.  **Choices:**   - `false` ← (default) - `true` |
| **usepkgonly**  boolean | Merge only binaries (no compiling).  **Choices:**   - `false` ← (default) - `true` |
| **verbose**  boolean | Run emerge in verbose mode (–verbose)  **Choices:**   - `false` ← (default) - `true` |
| **withbdeps**  boolean  *added in community.general 5.8.0* | Specifies that build time dependencies should be installed.  **Choices:**   - `false` - `true` |

## [Attributes](portage_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](portage_module.md#id4)

```yaml+jinja
- name: Make sure package foo is installed
  community.general.portage:
    package: foo
    state: present

- name: Make sure package foo is not installed
  community.general.portage:
    package: foo
    state: absent

- name: Update package foo to the latest version (os specific alternative to latest)
  community.general.portage:
    package: foo
    update: true

- name: Install package foo using PORTAGE_BINHOST setup
  community.general.portage:
    package: foo
    getbinpkg: true

- name: Re-install world from binary packages only and do not allow any compiling
  community.general.portage:
    package: '@world'
    usepkgonly: true

- name: Sync repositories and update world
  community.general.portage:
    package: '@world'
    update: true
    deep: true
    sync: true

- name: Remove unneeded packages
  community.general.portage:
    depclean: true

- name: Remove package foo if it is not explicitly needed
  community.general.portage:
    package: foo
    state: absent
    depclean: true
```

### Authors

- William L Thomson Jr (@wltjr)
- Yap Sok Ann (@sayap)
- Andrew Udvare (@Tatsh)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
