---
collection: ansible
version: "8"
title: "community.general.sefcontext module – Manages SELinux file context mapping definitions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/sefcontext_module.html
fetched_at: 2026-07-28T01:50:27+00:00
---
# community.general.sefcontext module – Manages SELinux file context mapping definitions

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
> see [Requirements](sefcontext_module.md#ansible-collections-community-general-sefcontext-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.sefcontext`.

- [Synopsis](sefcontext_module.md#synopsis)
- [Requirements](sefcontext_module.md#requirements)
- [Parameters](sefcontext_module.md#parameters)
- [Attributes](sefcontext_module.md#attributes)
- [Notes](sefcontext_module.md#notes)
- [Examples](sefcontext_module.md#examples)

## [Synopsis](sefcontext_module.md#id1)

- Manages SELinux file context mapping definitions.
- Similar to the `semanage fcontext` command.

Aliases: system.sefcontext

## [Requirements](sefcontext_module.md#id2)

The below requirements are needed on the host that executes this module.

- libselinux-python
- policycoreutils-python

## [Parameters](sefcontext_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ftype**  string | The file type that should have SELinux contexts applied.  The following file type options are available:  `a` for all files,  `b` for block devices,  `c` for character devices,  `d` for directories,  `f` for regular files,  `l` for symbolic links,  `p` for named pipes,  `s` for socket files.  **Choices:**   - `"a"` ← (default) - `"b"` - `"c"` - `"d"` - `"f"` - `"l"` - `"p"` - `"s"` |
| **ignore_selinux_state**  boolean | Useful for scenarios (chrooted environment) that you can’t get the real SELinux state.  **Choices:**   - `false` ← (default) - `true` |
| **reload**  boolean | Reload SELinux policy after commit.  Note that this does not apply SELinux file contexts to existing files.  **Choices:**   - `false` - `true` ← (default) |
| **selevel**  aliases: serange  string | SELinux range for the specified `target`.  Defaults to `s0` for new file contexts and to existing value when modifying file contexts. |
| **setype**  string | SELinux type for the specified `target`. |
| **seuser**  string | SELinux user for the specified `target`.  Defaults to `system_u` for new file contexts and to existing value when modifying file contexts. |
| **state**  string | Whether the SELinux file context must be `absent` or `present`.  Specifying `absent` without either `setype` or `substitute` deletes both SELinux type or path substitution mappings that match `target`.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **substitute**  aliases: equal  string  *added in community.general 6.4.0* | Path to use to substitute file context(s) for the specified `target`. The context labeling for the `target` subtree is made equivalent to this path.  This is also referred to as SELinux file context equivalence and it implements the `equal` functionality of the SELinux management tools. |
| **target**  aliases: path  string / required | Target path (expression). |

## [Attributes](sefcontext_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **platform** | **Platform:** **linux** | Target OS/families that can be operated against. |

## [Notes](sefcontext_module.md#id5)

> **Note:**
>
> - The changes are persistent across reboots.
> - `setype` and `substitute` are mutually exclusive.
> - If `state=present` then one of `setype` or `substitute` is mandatory.
> - The [community.general.sefcontext](sefcontext_module.md#ansible-collections-community-general-sefcontext-module) module does not modify existing files to the new SELinux context(s), so it is advisable to first create the SELinux file contexts before creating files, or run `restorecon` manually for the existing files that require the new SELinux file contexts.
> - Not applying SELinux fcontexts to existing files is a deliberate decision as it would be unclear what reported changes would entail to, and there’s no guarantee that applying SELinux fcontext does not pick up other unrelated prior changes.

## [Examples](sefcontext_module.md#id6)

```yaml+jinja
- name: Allow apache to modify files in /srv/git_repos
  community.general.sefcontext:
    target: '/srv/git_repos(/.*)?'
    setype: httpd_sys_rw_content_t
    state: present

- name: Substitute file contexts for path /srv/containers with /var/lib/containers
  community.general.sefcontext:
    target: /srv/containers
    substitute: /var/lib/containers
    state: present

- name: Delete file context path substitution for /srv/containers
  community.general.sefcontext:
    target: /srv/containers
    substitute: /var/lib/containers
    state: absent

- name: Delete any file context mappings for path /srv/git
  community.general.sefcontext:
    target: /srv/git
    state: absent

- name: Apply new SELinux file context to filesystem
  ansible.builtin.command: restorecon -irv /srv/git_repos
```

### Authors

- Dag Wieers (@dagwieers)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
