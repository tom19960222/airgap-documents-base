---
collection: ansible
version: "8"
title: "ansible.builtin.dnf module – Manages packages with the dnf package manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/dnf_module.html
fetched_at: 2026-07-28T01:07:25+00:00
---
# ansible.builtin.dnf module – Manages packages with the *dnf* package manager

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `dnf` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.dnf` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](dnf_module.md#synopsis)
- [Requirements](dnf_module.md#requirements)
- [Parameters](dnf_module.md#parameters)
- [Attributes](dnf_module.md#attributes)
- [Notes](dnf_module.md#notes)
- [Examples](dnf_module.md#examples)

## [Synopsis](dnf_module.md#id1)

- Installs, upgrade, removes, and lists packages and groups with the *dnf* package manager.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](dnf_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- python-dnf
- for the autoremove option you need dnf >= 2.0.1”

## [Parameters](dnf_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_downgrade**  boolean  *added in Ansible 2.7* | Specify if the named package and version is allowed to downgrade a maybe already installed higher version of that package. Note that setting allow_downgrade=True can make this module behave in a non-idempotent way. The task could end up with a set of packages that does not match the complete list of specified packages to install (because dependencies between the downgraded package and others can cause changes to the packages which were in the earlier transaction).  **Choices:**   - `false` ← (default) - `true` |
| **allowerasing**  boolean  *added in ansible-base 2.10* | If `true` it allows erasing of installed packages to resolve dependencies.  **Choices:**   - `false` ← (default) - `true` |
| **autoremove**  boolean | If `true`, removes all “leaf” packages from the system that were originally installed as dependencies of user-installed packages but which are no longer required by any such package. Should be used alone or when state is *absent*  **Choices:**   - `false` ← (default) - `true` |
| **bugfix**  boolean  *added in Ansible 2.7* | If set to `true`, and `state=latest` then only installs updates that have been marked bugfix related.  Note that, similar to `dnf upgrade-minimal`, this filter applies to dependencies as well.  **Choices:**   - `false` ← (default) - `true` |
| **cacheonly**  boolean  *added in ansible-core 2.12* | Tells dnf to run entirely from system cache; does not download or update metadata.  **Choices:**   - `false` ← (default) - `true` |
| **conf_file**  string | The remote dnf configuration file to use for the transaction. |
| **disable_excludes**  string  *added in Ansible 2.7* | Disable the excludes defined in DNF config files.  If set to `all`, disables all excludes.  If set to `main`, disable excludes defined in [main] in dnf.conf.  If set to `repoid`, disable excludes defined for given repo id. |
| **disable_gpg_check**  boolean | Whether to disable the GPG checking of signatures of packages being installed. Has an effect only if state is *present* or *latest*.  This setting affects packages installed from a repository as well as “local” packages installed from the filesystem or a URL.  **Choices:**   - `false` ← (default) - `true` |
| **disable_plugin**  list / elements=string  *added in Ansible 2.7* | *Plugin* name to disable for the install/update operation. The disabled plugins will not persist beyond the transaction.  **Default:** `[]` |
| **disablerepo**  list / elements=string | *Repoid* of repositories to disable for the install/update operation. These repos will not persist beyond the transaction. When specifying multiple repos, separate them with a “,”.  **Default:** `[]` |
| **download_dir**  string  *added in Ansible 2.8* | Specifies an alternate directory to store packages.  Has an effect only if *download_only* is specified. |
| **download_only**  boolean  *added in Ansible 2.7* | Only download the packages, do not install them.  **Choices:**   - `false` ← (default) - `true` |
| **enable_plugin**  list / elements=string  *added in Ansible 2.7* | *Plugin* name to enable for the install/update operation. The enabled plugin will not persist beyond the transaction.  **Default:** `[]` |
| **enablerepo**  list / elements=string | *Repoid* of repositories to enable for the install/update operation. These repos will not persist beyond the transaction. When specifying multiple repos, separate them with a “,”.  **Default:** `[]` |
| **exclude**  list / elements=string  *added in Ansible 2.7* | Package name(s) to exclude when state=present, or latest. This can be a list or a comma separated string.  **Default:** `[]` |
| **install_repoquery**  boolean  *added in Ansible 2.7* | This is effectively a no-op in DNF as it is not needed with DNF, but is an accepted parameter for feature parity/compatibility with the *yum* module.  **Choices:**   - `false` - `true` ← (default) |
| **install_weak_deps**  boolean  *added in Ansible 2.8* | Will also install all packages linked by a weak dependency relation.  **Choices:**   - `false` - `true` ← (default) |
| **installroot**  string | Specifies an alternative installroot, relative to which all packages will be installed.  **Default:** `"/"` |
| **list**  string | Various (non-idempotent) commands for usage with `/usr/bin/ansible` and *not* playbooks. Use [ansible.builtin.package_facts](package_facts_module.md#ansible-collections-ansible-builtin-package-facts-module) instead of the `list` argument as a best practice. |
| **lock_timeout**  integer  *added in Ansible 2.8* | Amount of time to wait for the dnf lockfile to be freed.  **Default:** `30` |
| **name**  aliases: pkg  list / elements=string | A package name or package specifier with version, like `name-1.0`. When using state=latest, this can be ‘\*’ which means run: dnf -y update. You can also pass a url or a local path to a rpm file. To operate on several packages this can accept a comma separated string of packages or a list of packages.  Comparison operators for package version are valid here `>`, `<`, `>=`, `<=`. Example - `name >= 1.0`. Spaces around the operator are required.  You can also pass an absolute path for a binary which is provided by the package to install. See examples for more information.  **Default:** `[]` |
| **nobest**  boolean  *added in ansible-core 2.11* | Set best option to False, so that transactions are not limited to best candidates only.  **Choices:**   - `false` ← (default) - `true` |
| **releasever**  string | Specifies an alternative release from which all packages will be installed. |
| **security**  boolean  *added in Ansible 2.7* | If set to `true`, and `state=latest` then only installs updates that have been marked security related.  Note that, similar to `dnf upgrade-minimal`, this filter applies to dependencies as well.  **Choices:**   - `false` ← (default) - `true` |
| **skip_broken**  boolean  *added in Ansible 2.7* | Skip all unavailable packages or packages with broken dependencies without raising an error. Equivalent to passing the –skip-broken option.  **Choices:**   - `false` ← (default) - `true` |
| **sslverify**  boolean  *added in ansible-core 2.13* | Disables SSL validation of the repository server for this transaction.  This should be set to `false` if one of the configured repositories is using an untrusted or self-signed certificate.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | Whether to install (`present`, `latest`), or remove (`absent`) a package.  Default is `None`, however in effect the default action is `present` unless the `autoremove` option is enabled for this module, then `absent` is inferred.  **Choices:**   - `"absent"` - `"present"` - `"installed"` - `"removed"` - `"latest"` |
| **update_cache**  aliases: expire-cache  boolean  *added in Ansible 2.7* | Force dnf to check if cache is out of date and redownload if needed. Has an effect only if state is *present* or *latest*.  **Choices:**   - `false` ← (default) - `true` |
| **update_only**  boolean  *added in Ansible 2.7* | When using latest, only update installed packages. Do not install packages.  Has an effect only if state is *latest*  **Choices:**   - `false` ← (default) - `true` |
| **use_backend**  string  *added in ansible-core 2.15* | By default, this module will select the backend based on the `ansible_pkg_mgr` fact.  **Choices:**   - `"auto"` ← (default) - `"dnf4"` - `"dnf5"` |
| **validate_certs**  boolean  *added in Ansible 2.7* | This only applies if using a https url as the source of the rpm. e.g. for localinstall. If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates as it avoids verifying the source site.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](dnf_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **partial**  In the case of dnf, it has 2 action plugins that use it under the hood, [ansible.builtin.yum](yum_module.md#ansible-collections-ansible-builtin-yum-module) and [ansible.builtin.package](package_module.md#ansible-collections-ansible-builtin-package-module). | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | **Support:** **none** | Supports being used with the `async` keyword |
| **bypass_host_loop** | **Support:** **none** | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **rhel** | Target OS/families that can be operated against |

## [Notes](dnf_module.md#id5)

> **Note:**
>
> - When used with a `loop:` each package will be processed individually, it is much more efficient to pass the list directly to the *name* option.
> - Group removal doesn’t work if the group was installed with Ansible because upstream dnf’s API doesn’t properly mark groups as installed, therefore upon removal the module is unable to detect that the group is installed (<https://bugzilla.redhat.com/show_bug.cgi?id=1620324>)

## [Examples](dnf_module.md#id6)

```yaml+jinja
- name: Install the latest version of Apache
  ansible.builtin.dnf:
    name: httpd
    state: latest

- name: Install Apache >= 2.4
  ansible.builtin.dnf:
    name: httpd >= 2.4
    state: present

- name: Install the latest version of Apache and MariaDB
  ansible.builtin.dnf:
    name:
      - httpd
      - mariadb-server
    state: latest

- name: Remove the Apache package
  ansible.builtin.dnf:
    name: httpd
    state: absent

- name: Install the latest version of Apache from the testing repo
  ansible.builtin.dnf:
    name: httpd
    enablerepo: testing
    state: present

- name: Upgrade all packages
  ansible.builtin.dnf:
    name: "*"
    state: latest

- name: Update the webserver, depending on which is installed on the system. Do not install the other one
  ansible.builtin.dnf:
    name:
      - httpd
      - nginx
    state: latest
    update_only: yes

- name: Install the nginx rpm from a remote repo
  ansible.builtin.dnf:
    name: 'http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm'
    state: present

- name: Install nginx rpm from a local file
  ansible.builtin.dnf:
    name: /usr/local/src/nginx-release-centos-6-0.el6.ngx.noarch.rpm
    state: present

- name: Install Package based upon the file it provides
  ansible.builtin.dnf:
    name: /usr/bin/cowsay
    state: present

- name: Install the 'Development tools' package group
  ansible.builtin.dnf:
    name: '@Development tools'
    state: present

- name: Autoremove unneeded packages installed as dependencies
  ansible.builtin.dnf:
    autoremove: yes

- name: Uninstall httpd but keep its dependencies
  ansible.builtin.dnf:
    name: httpd
    state: absent
    autoremove: no

- name: Install a modularity appstream with defined stream and profile
  ansible.builtin.dnf:
    name: '@postgresql:9.6/client'
    state: present

- name: Install a modularity appstream with defined stream
  ansible.builtin.dnf:
    name: '@postgresql:9.6'
    state: present

- name: Install a modularity appstream with defined profile
  ansible.builtin.dnf:
    name: '@postgresql/client'
    state: present
```

### Authors

- Igor Gnatenko (@ignatenkobrain)
- Cristian van Ee (@DJMuggs) <cristian at cvee.org>
- Berend De Schouwer (@berenddeschouwer)
- Adam Miller (@maxamillion)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
