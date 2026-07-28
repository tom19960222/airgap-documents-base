---
collection: ansible
version: "8"
title: "ansible.builtin.deb822_repository module – Add and remove deb822 formatted repositories"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/deb822_repository_module.html
fetched_at: 2026-07-28T01:07:24+00:00
---
# ansible.builtin.deb822_repository module – Add and remove deb822 formatted repositories

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `deb822_repository` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.deb822_repository` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

New in ansible-core 2.15

- [Synopsis](deb822_repository_module.md#synopsis)
- [Requirements](deb822_repository_module.md#requirements)
- [Parameters](deb822_repository_module.md#parameters)
- [Notes](deb822_repository_module.md#notes)
- [Examples](deb822_repository_module.md#examples)
- [Return Values](deb822_repository_module.md#return-values)

## [Synopsis](deb822_repository_module.md#id1)

- Add and remove deb822 formatted repositories in Debian based distributions

## [Requirements](deb822_repository_module.md#id2)

The below requirements are needed on the host that executes this module.

- python3-debian / python-debian

## [Parameters](deb822_repository_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_downgrade_to_insecure**  boolean | Allow downgrading a package that was previously authenticated but is no longer authenticated  **Choices:**   - `false` - `true` |
| **allow_insecure**  boolean | Allow insecure repositories  **Choices:**   - `false` - `true` |
| **allow_weak**  boolean | Allow repositories signed with a key using a weak digest algorithm  **Choices:**   - `false` - `true` |
| **architectures**  list / elements=string | Architectures to search within repository |
| **by_hash**  boolean | Controls if APT should try to acquire indexes via a URI constructed from a hashsum of the expected file instead of using the well-known stable filename of the index.  **Choices:**   - `false` - `true` |
| **check_date**  boolean | Controls if APT should consider the machine’s time correct and hence perform time related checks, such as verifying that a Release file is not from the future.  **Choices:**   - `false` - `true` |
| **check_valid_until**  boolean | Controls if APT should try to detect replay attacks.  **Choices:**   - `false` - `true` |
| **components**  list / elements=string | Components specify different sections of one distribution version present in a Suite. |
| **date_max_future**  integer | Controls how far from the future a repository may be. |
| **enabled**  boolean | Tells APT whether the source is enabled or not.  **Choices:**   - `false` - `true` |
| **inrelease_path**  string | Determines the path to the InRelease file, relative to the normal position of an InRelease file. |
| **languages**  list / elements=string | Defines which languages information such as translated package descriptions should be downloaded. |
| **mode**  any | The octal mode for newly created files in sources.list.d.  **Default:** `"0644"` |
| **name**  string / required | Name of the repo. Specifically used for `X-Repolib-Name` and in naming the repository and signing key files. |
| **pdiffs**  boolean | Controls if APT should try to use PDiffs to update old indexes instead of downloading the new indexes entirely  **Choices:**   - `false` - `true` |
| **signed_by**  string | Either a URL to a GPG key, absolute path to a keyring file, one or more fingerprints of keys either in the `trusted.gpg` keyring or in the keyrings in the `trusted.gpg.d/` directory, or an ASCII armored GPG public key block. |
| **state**  string | A source string state.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **suites**  list / elements=string | Suite can specify an exact path in relation to the URI(s) provided, in which case the Components: must be omitted and suite must end with a slash  `/` . Alternatively, it may take the form of a distribution version (e.g. a version codename like disco or artful). If the suite does not specify a path, at least one component must be present. |
| **targets**  list / elements=string | Defines which download targets apt will try to acquire from this source. |
| **trusted**  boolean | Decides if a source is considered trusted or if warnings should be raised before e.g. packages are installed from this source.  **Choices:**   - `false` - `true` |
| **types**  list / elements=string | Which types of packages to look for from a given source; either binary `deb` or source code `deb-src`  **Choices:**   - `"deb"` ← (default) - `"deb-src"`   **Default:** `["deb"]` |
| **uris**  list / elements=string | The URIs must specify the base of the Debian distribution archive, from which APT finds the information it needs. |

## [Notes](deb822_repository_module.md#id4)

> **Note:**
>
> - This module will not automatically update caches, call the apt module based on the changed state.

## [Examples](deb822_repository_module.md#id5)

```yaml+jinja
- name: Add debian repo
  deb822_repository:
    name: debian
    types: deb
    uris: http://deb.debian.org/debian
    suites: stretch
    components:
      - main
      - contrib
      - non-free

- name: Add debian repo with key
  deb822_repository:
    name: debian
    types: deb
    uris: https://deb.debian.org
    suites: stable
    components:
      - main
      - contrib
      - non-free
    signed_by: |-
      -----BEGIN PGP PUBLIC KEY BLOCK-----

      mDMEYCQjIxYJKwYBBAHaRw8BAQdAD/P5Nvvnvk66SxBBHDbhRml9ORg1WV5CvzKY
      CuMfoIS0BmFiY2RlZoiQBBMWCgA4FiEErCIG1VhKWMWo2yfAREZd5NfO31cFAmAk
      IyMCGyMFCwkIBwMFFQoJCAsFFgIDAQACHgECF4AACgkQREZd5NfO31fbOwD6ArzS
      dM0Dkd5h2Ujy1b6KcAaVW9FOa5UNfJ9FFBtjLQEBAJ7UyWD3dZzhvlaAwunsk7DG
      3bHcln8DMpIJVXht78sL
      =IE0r
      -----END PGP PUBLIC KEY BLOCK-----

- name: Add repo using key from URL
  deb822_repository:
    name: example
    types: deb
    uris: https://download.example.com/linux/ubuntu
    suites: '{{ ansible_distribution_release }}'
    components: stable
    architectures: amd64
    signed_by: https://download.example.com/linux/ubuntu/gpg
```

## [Return Values](deb822_repository_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dest**  string | Path to the repository file  **Returned:** always  **Sample:** `"/etc/apt/sources.list.d/focal-archive.sources"` |
| **key_filename**  string | Path to the signed_by key file  **Returned:** always  **Sample:** `"/etc/apt/keyrings/debian.gpg"` |
| **repo**  string | A source string for the repository  **Returned:** always  **Sample:** `"X-Repolib-Name: debian\nTypes: deb\nURIs: https://deb.debian.org\nSuites: stable\nComponents: main contrib non-free\nSigned-By:\n    -----BEGIN PGP PUBLIC KEY BLOCK-----\n    .\n    mDMEYCQjIxYJKwYBBAHaRw8BAQdAD/P5Nvvnvk66SxBBHDbhRml9ORg1WV5CvzKY\n    CuMfoIS0BmFiY2RlZoiQBBMWCgA4FiEErCIG1VhKWMWo2yfAREZd5NfO31cFAmAk\n    IyMCGyMFCwkIBwMFFQoJCAsFFgIDAQACHgECF4AACgkQREZd5NfO31fbOwD6ArzS\n    dM0Dkd5h2Ujy1b6KcAaVW9FOa5UNfJ9FFBtjLQEBAJ7UyWD3dZzhvlaAwunsk7DG\n    3bHcln8DMpIJVXht78sL\n    =IE0r\n    -----END PGP PUBLIC KEY BLOCK-----\n"` |

### Authors

- Ansible Core Team (@ansible)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
