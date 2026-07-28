---
collection: ansible
version: "8"
title: "ansible.builtin.dnf5 module – Manages packages with the dnf5 package manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/dnf5_module.html
fetched_at: 2026-07-28T01:07:26+00:00
---
# ansible.builtin.dnf5 module – Manages packages with the *dnf5* package manager

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `dnf5` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.dnf5` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

New in ansible-core 2.15

- [Synopsis](dnf5_module.md#synopsis)
- [Requirements](dnf5_module.md#requirements)
- [Parameters](dnf5_module.md#parameters)
- [Attributes](dnf5_module.md#attributes)
- [Examples](dnf5_module.md#examples)
- [Return Values](dnf5_module.md#return-values)

## [Synopsis](dnf5_module.md#id1)

- Installs, upgrade, removes, and lists packages and groups with the *dnf5* package manager.
- WARNING: The *dnf5* package manager is still under development and not all features that the existing *dnf* module provides are implemented in *dnf5*, please consult specific options for more information.

## [Requirements](dnf5_module.md#id2)

The below requirements are needed on the host that executes this module.

- python3
- python3-libdnf5

## [Parameters](dnf5_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_downgrade**  boolean | Specify if the named package and version is allowed to downgrade a maybe already installed higher version of that package. Note that setting allow_downgrade=True can make this module behave in a non-idempotent way. The task could end up with a set of packages that does not match the complete list of specified packages to install (because dependencies between the downgraded package and others can cause changes to the packages which were in the earlier transaction).  **Choices:**   - `false` ← (default) - `true` |
| **allowerasing**  boolean | If `true` it allows erasing of installed packages to resolve dependencies.  **Choices:**   - `false` ← (default) - `true` |
| **autoremove**  boolean | If `true`, removes all “leaf” packages from the system that were originally installed as dependencies of user-installed packages but which are no longer required by any such package. Should be used alone or when state is *absent*  **Choices:**   - `false` ← (default) - `true` |
| **bugfix**  boolean | If set to `true`, and `state=latest` then only installs updates that have been marked bugfix related.  Note that, similar to `dnf upgrade-minimal`, this filter applies to dependencies as well.  **Choices:**   - `false` ← (default) - `true` |
| **cacheonly**  boolean | Tells dnf to run entirely from system cache; does not download or update metadata.  **Choices:**   - `false` ← (default) - `true` |
| **conf_file**  string | The remote dnf configuration file to use for the transaction. |
| **disable_excludes**  string | Disable the excludes defined in DNF config files.  If set to `all`, disables all excludes.  If set to `main`, disable excludes defined in [main] in dnf.conf.  If set to `repoid`, disable excludes defined for given repo id. |
| **disable_gpg_check**  boolean | Whether to disable the GPG checking of signatures of packages being installed. Has an effect only if state is *present* or *latest*.  This setting affects packages installed from a repository as well as “local” packages installed from the filesystem or a URL.  **Choices:**   - `false` ← (default) - `true` |
| **disable_plugin**  list / elements=string | This is currently a no-op as dnf5 itself does not implement this feature.  *Plugin* name to disable for the install/update operation. The disabled plugins will not persist beyond the transaction.  **Default:** `[]` |
| **disablerepo**  list / elements=string | *Repoid* of repositories to disable for the install/update operation. These repos will not persist beyond the transaction. When specifying multiple repos, separate them with a “,”.  **Default:** `[]` |
| **download_dir**  string | Specifies an alternate directory to store packages.  Has an effect only if *download_only* is specified. |
| **download_only**  boolean | Only download the packages, do not install them.  **Choices:**   - `false` ← (default) - `true` |
| **enable_plugin**  list / elements=string | This is currently a no-op as dnf5 itself does not implement this feature.  *Plugin* name to enable for the install/update operation. The enabled plugin will not persist beyond the transaction.  **Default:** `[]` |
| **enablerepo**  list / elements=string | *Repoid* of repositories to enable for the install/update operation. These repos will not persist beyond the transaction. When specifying multiple repos, separate them with a “,”.  **Default:** `[]` |
| **exclude**  list / elements=string | Package name(s) to exclude when state=present, or latest. This can be a list or a comma separated string.  **Default:** `[]` |
| **install_repoquery**  boolean | This is effectively a no-op in DNF as it is not needed with DNF, but is an accepted parameter for feature parity/compatibility with the *yum* module.  **Choices:**   - `false` - `true` ← (default) |
| **install_weak_deps**  boolean | Will also install all packages linked by a weak dependency relation.  **Choices:**   - `false` - `true` ← (default) |
| **installroot**  string | Specifies an alternative installroot, relative to which all packages will be installed.  **Default:** `"/"` |
| **list**  string | Various (non-idempotent) commands for usage with `/usr/bin/ansible` and *not* playbooks. Use [ansible.builtin.package_facts](package_facts_module.md#ansible-collections-ansible-builtin-package-facts-module) instead of the `list` argument as a best practice. |
| **lock_timeout**  integer | This is currently a no-op as dnf5 does not provide an option to configure it.  Amount of time to wait for the dnf lockfile to be freed.  **Default:** `30` |
| **name**  aliases: pkg  list / elements=string | A package name or package specifier with version, like `name-1.0`. When using state=latest, this can be ‘\*’ which means run: dnf -y update. You can also pass a url or a local path to a rpm file. To operate on several packages this can accept a comma separated string of packages or a list of packages.  Comparison operators for package version are valid here `>`, `<`, `>=`, `<=`. Example - `name >= 1.0`. Spaces around the operator are required.  You can also pass an absolute path for a binary which is provided by the package to install. See examples for more information.  **Default:** `[]` |
| **nobest**  boolean | Set best option to False, so that transactions are not limited to best candidates only.  **Choices:**   - `false` ← (default) - `true` |
| **releasever**  string | Specifies an alternative release from which all packages will be installed. |
| **security**  boolean | If set to `true`, and `state=latest` then only installs updates that have been marked security related.  Note that, similar to `dnf upgrade-minimal`, this filter applies to dependencies as well.  **Choices:**   - `false` ← (default) - `true` |
| **skip_broken**  boolean | Skip all unavailable packages or packages with broken dependencies without raising an error. Equivalent to passing the –skip-broken option.  **Choices:**   - `false` ← (default) - `true` |
| **sslverify**  boolean | Disables SSL validation of the repository server for this transaction.  This should be set to `false` if one of the configured repositories is using an untrusted or self-signed certificate.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | Whether to install (`present`, `latest`), or remove (`absent`) a package.  Default is `None`, however in effect the default action is `present` unless the `autoremove` option is enabled for this module, then `absent` is inferred.  **Choices:**   - `"absent"` - `"present"` - `"installed"` - `"removed"` - `"latest"` |
| **update_cache**  aliases: expire-cache  boolean | Force dnf to check if cache is out of date and redownload if needed. Has an effect only if state is *present* or *latest*.  **Choices:**   - `false` ← (default) - `true` |
| **update_only**  boolean | When using latest, only update installed packages. Do not install packages.  Has an effect only if state is *latest*  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | This is effectively a no-op in the dnf5 module as dnf5 itself handles downloading a https url as the source of the rpm, but is an accepted parameter for feature parity/compatibility with the *yum* module.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](dnf5_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **partial**  In the case of dnf, it has 2 action plugins that use it under the hood, [ansible.builtin.yum](yum_module.md#ansible-collections-ansible-builtin-yum-module) and [ansible.builtin.package](package_module.md#ansible-collections-ansible-builtin-package-module). | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | **Support:** **none** | Supports being used with the `async` keyword |
| **bypass_host_loop** | **Support:** **none** | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **rhel** | Target OS/families that can be operated against |

## [Examples](dnf5_module.md#id5)

```yaml+jinja
- name: Install the latest version of Apache
  ansible.builtin.dnf5:
    name: httpd
    state: latest

- name: Install Apache >= 2.4
  ansible.builtin.dnf5:
    name: httpd >= 2.4
    state: present

- name: Install the latest version of Apache and MariaDB
  ansible.builtin.dnf5:
    name:
      - httpd
      - mariadb-server
    state: latest

- name: Remove the Apache package
  ansible.builtin.dnf5:
    name: httpd
    state: absent

- name: Install the latest version of Apache from the testing repo
  ansible.builtin.dnf5:
    name: httpd
    enablerepo: testing
    state: present

- name: Upgrade all packages
  ansible.builtin.dnf5:
    name: "*"
    state: latest

- name: Update the webserver, depending on which is installed on the system. Do not install the other one
  ansible.builtin.dnf5:
    name:
      - httpd
      - nginx
    state: latest
    update_only: yes

- name: Install the nginx rpm from a remote repo
  ansible.builtin.dnf5:
    name: 'http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm'
    state: present

- name: Install nginx rpm from a local file
  ansible.builtin.dnf5:
    name: /usr/local/src/nginx-release-centos-6-0.el6.ngx.noarch.rpm
    state: present

- name: Install Package based upon the file it provides
  ansible.builtin.dnf5:
    name: /usr/bin/cowsay
    state: present

- name: Install the 'Development tools' package group
  ansible.builtin.dnf5:
    name: '@Development tools'
    state: present

- name: Autoremove unneeded packages installed as dependencies
  ansible.builtin.dnf5:
    autoremove: yes

- name: Uninstall httpd but keep its dependencies
  ansible.builtin.dnf5:
    name: httpd
    state: absent
    autoremove: no
```

## [Return Values](dnf5_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failures**  list / elements=string | A list of the dnf transaction failures  **Returned:** failure  **Sample:** `["Argument 'lsof' matches only excluded packages."]` |
| **msg**  string | Additional information about the result  **Returned:** always  **Sample:** `"Nothing to do"` |
| **rc**  integer | For compatibility, 0 for success, 1 for failure  **Returned:** always  **Sample:** `0` |
| **results**  list / elements=string | A list of the dnf transaction results  **Returned:** success  **Sample:** `["Installed: lsof-4.94.0-4.fc37.x86_64"]` |

### Authors

- Ansible Core Team

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
