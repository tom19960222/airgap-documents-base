---
collection: ansible
version: "6"
title: "Ansible.Posix"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/posix/index.html
fetched_at: 2026-07-27T16:41:33+00:00
---
# Ansible.Posix

Collection version 1.4.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible Collection targeting POSIX and POSIX-ish platforms.

**Author:**

- Ansible (github.com/ansible)

**Supported ansible-core versions:**

- 2.9 or newer

[Issue Tracker](https://github.com/ansible-collections/ansible.posix)
[Repository (Sources)](https://github.com/ansible-collections/ansible.posix)

## [Plugin Index](index.md#id2)

These are the plugins in the ansible.posix collection:

### Modules

- [acl module](acl_module.md#ansible-collections-ansible-posix-acl-module) – Set and retrieve file ACL information.
- [at module](at_module.md#ansible-collections-ansible-posix-at-module) – Schedule the execution of a command or script file via the at command
- [authorized_key module](authorized_key_module.md#ansible-collections-ansible-posix-authorized-key-module) – Adds or removes an SSH authorized key
- [firewalld module](firewalld_module.md#ansible-collections-ansible-posix-firewalld-module) – Manage arbitrary ports/services with firewalld
- [firewalld_info module](firewalld_info_module.md#ansible-collections-ansible-posix-firewalld-info-module) – Gather information about firewalld
- [mount module](mount_module.md#ansible-collections-ansible-posix-mount-module) – Control active and configured mount points
- [patch module](patch_module.md#ansible-collections-ansible-posix-patch-module) – Apply patch files using the GNU patch tool
- [seboolean module](seboolean_module.md#ansible-collections-ansible-posix-seboolean-module) – Toggles SELinux booleans
- [selinux module](selinux_module.md#ansible-collections-ansible-posix-selinux-module) – Change policy and state of SELinux
- [synchronize module](synchronize_module.md#ansible-collections-ansible-posix-synchronize-module) – A wrapper around rsync to make common tasks in your playbooks quick and easy
- [sysctl module](sysctl_module.md#ansible-collections-ansible-posix-sysctl-module) – Manage entries in sysctl.conf.

### Callback Plugins

- [cgroup_perf_recap callback](cgroup_perf_recap_callback.md#ansible-collections-ansible-posix-cgroup-perf-recap-callback) – Profiles system activity of tasks and full execution using cgroups
- [debug callback](debug_callback.md#ansible-collections-ansible-posix-debug-callback) – formatted stdout/stderr display
- [json callback](json_callback.md#ansible-collections-ansible-posix-json-callback) – Ansible screen output as JSON
- [profile_roles callback](profile_roles_callback.md#ansible-collections-ansible-posix-profile-roles-callback) – adds timing information to roles
- [profile_tasks callback](profile_tasks_callback.md#ansible-collections-ansible-posix-profile-tasks-callback) – adds time information to tasks
- [skippy callback](skippy_callback.md#ansible-collections-ansible-posix-skippy-callback) – Ansible screen output that ignores skipped status
- [timer callback](timer_callback.md#ansible-collections-ansible-posix-timer-callback) – Adds time to play stats

### Shell Plugins

- [csh shell](csh_shell.md#ansible-collections-ansible-posix-csh-shell) – C shell (/bin/csh)
- [fish shell](fish_shell.md#ansible-collections-ansible-posix-fish-shell) – fish shell (/bin/fish)

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
