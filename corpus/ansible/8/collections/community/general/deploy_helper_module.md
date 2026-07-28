---
collection: ansible
version: "8"
title: "community.general.deploy_helper module – Manages some of the steps common in deploying projects"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/deploy_helper_module.html
fetched_at: 2026-07-28T01:45:21+00:00
---
# community.general.deploy_helper module – Manages some of the steps common in deploying projects

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
> To use it in a playbook, specify: `community.general.deploy_helper`.

- [Synopsis](deploy_helper_module.md#synopsis)
- [Parameters](deploy_helper_module.md#parameters)
- [Attributes](deploy_helper_module.md#attributes)
- [Notes](deploy_helper_module.md#notes)
- [Examples](deploy_helper_module.md#examples)

## [Synopsis](deploy_helper_module.md#id1)

- The Deploy Helper manages some of the steps common in deploying software. It creates a folder structure, manages a symlink for the current release and cleans up old releases.
- Running it with the `state=query` or `state=present` will return the `deploy_helper` fact. `project_path`, whatever you set in the `path` parameter, `current_path`, the path to the symlink that points to the active release, `releases_path`, the path to the folder to keep releases in, `shared_path`, the path to the folder to keep shared resources in, `unfinished_filename`, the file to check for to recognize unfinished builds, `previous_release`, the release the ‘current’ symlink is pointing to, `previous_release_path`, the full path to the ‘current’ symlink target, `new_release`, either the ‘release’ parameter or a generated timestamp, `new_release_path`, the path to the new release folder (not created by the module).

Aliases: web_infrastructure.deploy_helper

## [Parameters](deploy_helper_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **clean**  boolean | Whether to run the clean procedure in case of `state=finalize`.  **Choices:**   - `false` - `true` ← (default) |
| **current_path**  path | The name of the symlink that is created when the deploy is finalized. Used in `state=finalize` and `state=clean`. Returned in the `deploy_helper.current_path` fact.  **Default:** `"current"` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **keep_releases**  integer | The number of old releases to keep when cleaning. Used in `state=finalize` and `state=clean`. Any unfinished builds will be deleted first, so only correct releases will count. The current version will not count.  **Default:** `5` |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **path**  aliases: dest  path / required | The root path of the project. Returned in the `deploy_helper.project_path` fact. |
| **release**  string | The release version that is being deployed. Defaults to a timestamp format `%Y%m%d%H%M%S` (for example `20141119223359`). This parameter is optional during `state=present`, but needs to be set explicitly for `state=finalize`. You can use the generated fact `release={{ deploy_helper.new_release }}`. |
| **releases_path**  string | The name of the folder that will hold the releases. This can be relative to `path` or absolute. Returned in the `deploy_helper.releases_path` fact.  **Default:** `"releases"` |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **shared_path**  path | The name of the folder that will hold the shared resources. This can be relative to `path` or absolute. If this is set to an empty string, no shared folder will be created. Returned in the `deploy_helper.shared_path` fact.  **Default:** `"shared"` |
| **state**  string | The state of the project.  `query` will only gather facts.  `present` will create the project `root` folder, and in it the `releases` and `shared` folders.  `finalize` will remove the unfinished_filename file, create a symlink to the newly deployed release and optionally clean old releases.  `clean` will remove failed & old releases.  `absent` will remove the project folder (synonymous to the [ansible.builtin.file](../../ansible/builtin/file_module.md#ansible-collections-ansible-builtin-file-module) module with `state=absent`).  **Choices:**   - `"present"` ← (default) - `"finalize"` - `"absent"` - `"clean"` - `"query"` |
| **unfinished_filename**  string | The name of the file that indicates a deploy has not finished. All folders in the `releases_path` that contain this file will be deleted on `state=finalize` with `clean=true`, or `state=clean`. This file is automatically deleted from the `new_release_path` during `state=finalize`.  **Default:** `"DEPLOY_UNFINISHED"` |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](deploy_helper_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](deploy_helper_module.md#id4)

> **Note:**
>
> - Facts are only returned for `state=query` and `state=present`. If you use both, you should pass any overridden parameters to both calls, otherwise the second call will overwrite the facts of the first one.
> - When using `state=clean`, the releases are ordered by *creation date*. You should be able to switch to a new naming strategy without problems.
> - Because of the default behaviour of generating the `new_release` fact, this module will not be idempotent unless you pass your own release name with `release`. Due to the nature of deploying software, this should not be much of a problem.

## [Examples](deploy_helper_module.md#id5)

```yaml+jinja
# General explanation, starting with an example folder structure for a project:

# root:
#     releases:
#         - 20140415234508
#         - 20140415235146
#         - 20140416082818
#
#     shared:
#         - sessions
#         - uploads
#
#     current: releases/20140416082818

# The 'releases' folder holds all the available releases. A release is a complete build of the application being
# deployed. This can be a clone of a repository for example, or a sync of a local folder on your filesystem.
# Having timestamped folders is one way of having distinct releases, but you could choose your own strategy like
# git tags or commit hashes.
#
# During a deploy, a new folder should be created in the releases folder and any build steps required should be
# performed. Once the new build is ready, the deploy procedure is 'finalized' by replacing the 'current' symlink
# with a link to this build.
#
# The 'shared' folder holds any resource that is shared between releases. Examples of this are web-server
# session files, or files uploaded by users of your application. It's quite common to have symlinks from a release
# folder pointing to a shared/subfolder, and creating these links would be automated as part of the build steps.
#
# The 'current' symlink points to one of the releases. Probably the latest one, unless a deploy is in progress.
# The web-server's root for the project will go through this symlink, so the 'downtime' when switching to a new
# release is reduced to the time it takes to switch the link.
#
# To distinguish between successful builds and unfinished ones, a file can be placed in the folder of the release
# that is currently in progress. The existence of this file will mark it as unfinished, and allow an automated
# procedure to remove it during cleanup.

# Typical usage
- name: Initialize the deploy root and gather facts
  community.general.deploy_helper:
    path: /path/to/root
- name: Clone the project to the new release folder
  ansible.builtin.git:
    repo: ansible.builtin.git://foosball.example.org/path/to/repo.git
    dest: '{{ deploy_helper.new_release_path }}'
    version: v1.1.1
- name: Add an unfinished file, to allow cleanup on successful finalize
  ansible.builtin.file:
    path: '{{ deploy_helper.new_release_path }}/{{ deploy_helper.unfinished_filename }}'
    state: touch
- name: Perform some build steps, like running your dependency manager for example
  composer:
    command: install
    working_dir: '{{ deploy_helper.new_release_path }}'
- name: Create some folders in the shared folder
  ansible.builtin.file:
    path: '{{ deploy_helper.shared_path }}/{{ item }}'
    state: directory
  with_items:
    - sessions
    - uploads
- name: Add symlinks from the new release to the shared folder
  ansible.builtin.file:
    path: '{{ deploy_helper.new_release_path }}/{{ item.path }}'
    src: '{{ deploy_helper.shared_path }}/{{ item.src }}'
    state: link
  with_items:
      - path: app/sessions
        src: sessions
      - path: web/uploads
        src: uploads
- name: Finalize the deploy, removing the unfinished file and switching the symlink
  community.general.deploy_helper:
    path: /path/to/root
    release: '{{ deploy_helper.new_release }}'
    state: finalize

# Retrieving facts before running a deploy
- name: Run 'state=query' to gather facts without changing anything
  community.general.deploy_helper:
    path: /path/to/root
    state: query
# Remember to set the 'release' parameter when you actually call 'state=present' later
- name: Initialize the deploy root
  community.general.deploy_helper:
    path: /path/to/root
    release: '{{ deploy_helper.new_release }}'
    state: present

# all paths can be absolute or relative (to the 'path' parameter)
- community.general.deploy_helper:
    path: /path/to/root
    releases_path: /var/www/project/releases
    shared_path: /var/www/shared
    current_path: /var/www/active

# Using your own naming strategy for releases (a version tag in this case):
- community.general.deploy_helper:
    path: /path/to/root
    release: v1.1.1
    state: present
- community.general.deploy_helper:
    path: /path/to/root
    release: '{{ deploy_helper.new_release }}'
    state: finalize

# Using a different unfinished_filename:
- community.general.deploy_helper:
    path: /path/to/root
    unfinished_filename: README.md
    release: '{{ deploy_helper.new_release }}'
    state: finalize

# Postponing the cleanup of older builds:
- community.general.deploy_helper:
    path: /path/to/root
    release: '{{ deploy_helper.new_release }}'
    state: finalize
    clean: false
- community.general.deploy_helper:
    path: /path/to/root
    state: clean
# Or running the cleanup ahead of the new deploy
- community.general.deploy_helper:
    path: /path/to/root
    state: clean
- community.general.deploy_helper:
    path: /path/to/root
    state: present

# Keeping more old releases:
- community.general.deploy_helper:
    path: /path/to/root
    release: '{{ deploy_helper.new_release }}'
    state: finalize
    keep_releases: 10
# Or, if you use 'clean=false' on finalize:
- community.general.deploy_helper:
    path: /path/to/root
    state: clean
    keep_releases: 10

# Removing the entire project root folder
- community.general.deploy_helper:
    path: /path/to/root
    state: absent

# Debugging the facts returned by the module
- community.general.deploy_helper:
    path: /path/to/root
- ansible.builtin.debug:
    var: deploy_helper
```

### Authors

- Ramon de la Fuente (@ramondelafuente)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
