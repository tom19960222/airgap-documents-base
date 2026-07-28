---
collection: ansible
version: "8"
title: "ansible.builtin.apt_repository module – Add and remove APT repositories"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/apt_repository_module.html
fetched_at: 2026-07-28T01:07:22+00:00
---
# ansible.builtin.apt_repository module – Add and remove APT repositories

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `apt_repository` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.apt_repository` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](apt_repository_module.md#synopsis)
- [Requirements](apt_repository_module.md#requirements)
- [Parameters](apt_repository_module.md#parameters)
- [Attributes](apt_repository_module.md#attributes)
- [Notes](apt_repository_module.md#notes)
- [See Also](apt_repository_module.md#see-also)
- [Examples](apt_repository_module.md#examples)
- [Return Values](apt_repository_module.md#return-values)

## [Synopsis](apt_repository_module.md#id2)

- Add or remove an APT repositories in Ubuntu and Debian.

## [Requirements](apt_repository_module.md#id3)

The below requirements are needed on the host that executes this module.

- python-apt (python 2)
- python3-apt (python 3)
- apt-key or gpg

## [Parameters](apt_repository_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **codename**  string | Override the distribution codename to use for PPA repositories. Should usually only be set when working with a PPA on a non-Ubuntu target (for example, Debian or Mint). |
| **filename**  string | Sets the name of the source list file in sources.list.d. Defaults to a file name based on the repository source url. The .list extension will be automatically added. |
| **install_python_apt**  boolean | Whether to automatically try to install the Python apt library or not, if it is not already installed. Without this library, the module does not work.  Runs `apt-get install python-apt` for Python 2, and `apt-get install python3-apt` for Python 3.  Only works with the system Python 2 or Python 3. If you are using a Python on the remote that is not the system Python, set *install_python_apt=false* and ensure that the Python apt library for your Python version is installed some other way.  **Choices:**   - `false` - `true` ← (default) |
| **mode**  any | The octal mode for newly created files in sources.list.d.  Default is what system uses (probably 0644). |
| **repo**  string / required | A source string for the repository. |
| **state**  string | A source string state.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **update_cache**  aliases: update-cache  boolean | Run the equivalent of `apt-get update` when a change occurs. Cache updates are run after making changes.  **Choices:**   - `false` - `true` ← (default) |
| **update_cache_retries**  integer  *added in ansible-base 2.10* | Amount of retries if the cache update fails. Also see *update_cache_retry_max_delay*.  **Default:** `5` |
| **update_cache_retry_max_delay**  integer  *added in ansible-base 2.10* | Use an exponential backoff delay for each retry (see *update_cache_retries*) up to this max delay in seconds.  **Default:** `12` |
| **validate_certs**  boolean | If `false`, SSL certificates for the target repo will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](apt_repository_module.md#id5)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **debian** | Target OS/families that can be operated against |

## [Notes](apt_repository_module.md#id6)

> **Note:**
>
> - This module supports Debian Squeeze (version 6) as well as its successors and derivatives.

## [See Also](apt_repository_module.md#id7)

> **See also:**
>
> [ansible.builtin.deb822_repository](deb822_repository_module.md#ansible-collections-ansible-builtin-deb822-repository-module)
> :   Add and remove deb822 formatted repositories.

## [Examples](apt_repository_module.md#id8)

```yaml+jinja
- name: Add specified repository into sources list
  ansible.builtin.apt_repository:
    repo: deb http://archive.canonical.com/ubuntu hardy partner
    state: present

- name: Add specified repository into sources list using specified filename
  ansible.builtin.apt_repository:
    repo: deb http://dl.google.com/linux/chrome/deb/ stable main
    state: present
    filename: google-chrome

- name: Add source repository into sources list
  ansible.builtin.apt_repository:
    repo: deb-src http://archive.canonical.com/ubuntu hardy partner
    state: present

- name: Remove specified repository from sources list
  ansible.builtin.apt_repository:
    repo: deb http://archive.canonical.com/ubuntu hardy partner
    state: absent

- name: Add nginx stable repository from PPA and install its signing key on Ubuntu target
  ansible.builtin.apt_repository:
    repo: ppa:nginx/stable

- name: Add nginx stable repository from PPA and install its signing key on Debian target
  ansible.builtin.apt_repository:
    repo: 'ppa:nginx/stable'
    codename: trusty

- name: One way to avoid apt_key once it is removed from your distro
  block:
    - name: somerepo |no apt key
      ansible.builtin.get_url:
        url: https://download.example.com/linux/ubuntu/gpg
        dest: /etc/apt/keyrings/somerepo.asc

    - name: somerepo | apt source
      ansible.builtin.apt_repository:
        repo: "deb [arch=amd64 signed-by=/etc/apt/keyrings/myrepo.asc] https://download.example.com/linux/ubuntu {{ ansible_distribution_release }} stable"
        state: present
```

## [Return Values](apt_repository_module.md#id9)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **repo**  string | A source string for the repository  **Returned:** always  **Sample:** `"deb https://artifacts.elastic.co/packages/6.x/apt stable main"` |
| **sources_added**  list / elements=string  *added in ansible-core 2.15* | List of sources added  **Returned:** success, sources were added  **Sample:** `["/etc/apt/sources.list.d/artifacts_elastic_co_packages_6_x_apt.list"]` |
| **sources_removed**  list / elements=string  *added in ansible-core 2.15* | List of sources removed  **Returned:** success, sources were removed  **Sample:** `["/etc/apt/sources.list.d/artifacts_elastic_co_packages_6_x_apt.list"]` |

### Authors

- Alexander Saltanov (@sashka)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
