---
collection: ansible
version: "6"
title: "community.general.sefcontext module – Manages SELinux file context mapping definitions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/sefcontext_module.html
fetched_at: 2026-07-27T17:13:06+00:00
---
# community.general.sefcontext module – Manages SELinux file context mapping definitions

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
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
- [Notes](sefcontext_module.md#notes)
- [Examples](sefcontext_module.md#examples)

## [Synopsis](sefcontext_module.md#id1)

- Manages SELinux file context mapping definitions.
- Similar to the `semanage fcontext` command.

## [Requirements](sefcontext_module.md#id2)

The below requirements are needed on the host that executes this module.

- libselinux-python
- policycoreutils-python

## [Parameters](sefcontext_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ftype**  string | The file type that should have SELinux contexts applied.  The following file type options are available:  `a` for all files,  `b` for block devices,  `c` for character devices,  `d` for directories,  `f` for regular files,  `l` for symbolic links,  `p` for named pipes,  `s` for socket files.  Choices:   - `"a"` ← (default) - `"b"` - `"c"` - `"d"` - `"f"` - `"l"` - `"p"` - `"s"` |
| **ignore_selinux_state**  boolean | Useful for scenarios (chrooted environment) that you can’t get the real SELinux state.  Choices:   - `false` ← (default) - `true` |
| **reload**  boolean | Reload SELinux policy after commit.  Note that this does not apply SELinux file contexts to existing files.  Choices:   - `false` - `true` ← (default) |
| **selevel**  aliases: serange  string | SELinux range for the specified target. |
| **setype**  string / required | SELinux type for the specified target. |
| **seuser**  string | SELinux user for the specified target. |
| **state**  string | Whether the SELinux file context must be `absent` or `present`.  Choices:   - `"absent"` - `"present"` ← (default) |
| **target**  aliases: path  string / required | Target path (expression). |

## [Notes](sefcontext_module.md#id4)

> **Note:**
>
> - The changes are persistent across reboots.
> - The [community.general.sefcontext](sefcontext_module.md#ansible-collections-community-general-sefcontext-module) module does not modify existing files to the new SELinux context(s), so it is advisable to first create the SELinux file contexts before creating files, or run `restorecon` manually for the existing files that require the new SELinux file contexts.
> - Not applying SELinux fcontexts to existing files is a deliberate decision as it would be unclear what reported changes would entail to, and there’s no guarantee that applying SELinux fcontext does not pick up other unrelated prior changes.

## [Examples](sefcontext_module.md#id5)

```yaml+jinja
- name: Allow apache to modify files in /srv/git_repos
  community.general.sefcontext:
    target: '/srv/git_repos(/.*)?'
    setype: httpd_git_rw_content_t
    state: present

- name: Apply new SELinux file context to filesystem
  ansible.builtin.command: restorecon -irv /srv/git_repos
```

### Authors

- Dag Wieers (@dagwieers)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
