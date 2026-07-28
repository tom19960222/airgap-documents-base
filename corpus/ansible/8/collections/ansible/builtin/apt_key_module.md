---
collection: ansible
version: "8"
title: "ansible.builtin.apt_key module – Add or remove an apt key"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/apt_key_module.html
fetched_at: 2026-07-28T01:07:21+00:00
---
# ansible.builtin.apt_key module – Add or remove an apt key

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `apt_key` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.apt_key` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](apt_key_module.md#synopsis)
- [Requirements](apt_key_module.md#requirements)
- [Parameters](apt_key_module.md#parameters)
- [Attributes](apt_key_module.md#attributes)
- [Notes](apt_key_module.md#notes)
- [See Also](apt_key_module.md#see-also)
- [Examples](apt_key_module.md#examples)
- [Return Values](apt_key_module.md#return-values)

## [Synopsis](apt_key_module.md#id1)

- Add or remove an *apt* key, optionally downloading it.

## [Requirements](apt_key_module.md#id2)

The below requirements are needed on the host that executes this module.

- gpg

## [Parameters](apt_key_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **data**  string | The keyfile contents to add to the keyring. |
| **file**  path | The path to a keyfile on the remote server to add to the keyring. |
| **id**  string | The identifier of the key.  Including this allows check mode to correctly report the changed state.  If specifying a subkey’s id be aware that apt-key does not understand how to remove keys via a subkey id. Specify the primary key’s id instead.  This parameter is required when `state` is set to `absent`. |
| **keyring**  path | The full path to specific keyring file in `/etc/apt/trusted.gpg.d/`. |
| **keyserver**  string | The keyserver to retrieve key from. |
| **state**  string | Ensures that the key is present (added) or absent (revoked).  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **url**  string | The URL to retrieve key from. |
| **validate_certs**  boolean | If `false`, SSL certificates for the target url will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](apt_key_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **debian** | Target OS/families that can be operated against |

## [Notes](apt_key_module.md#id5)

> **Note:**
>
> - The apt-key command used by this module has been deprecated. See the [Debian wiki](https://wiki.debian.org/DebianRepository/UseThirdParty) for details. This module is kept for backwards compatibility for systems that still use apt-key as the main way to manage apt repository keys.
> - As a sanity check, downloaded key id must match the one specified.
> - Use full fingerprint (40 characters) key ids to avoid key collisions. To generate a full-fingerprint imported key: `apt-key adv --list-public-keys --with-fingerprint --with-colons`.
> - If you specify both the key id and the URL with `state=present`, the task can verify or add the key as needed.
> - Adding a new key requires an apt cache update (e.g. using the [ansible.builtin.apt](apt_module.md#ansible-collections-ansible-builtin-apt-module) module’s update_cache option).

## [See Also](apt_key_module.md#id6)

> **See also:**
>
> [ansible.builtin.deb822_repository](deb822_repository_module.md#ansible-collections-ansible-builtin-deb822-repository-module)
> :   Add and remove deb822 formatted repositories.

## [Examples](apt_key_module.md#id7)

```yaml+jinja
- name: One way to avoid apt_key once it is removed from your distro, armored keys should use .asc extension, binary should use .gpg
  block:
    - name: somerepo | no apt key
      ansible.builtin.get_url:
        url: https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x36a1d7869245c8950f966e92d8576a8ba88d21e9
        dest: /etc/apt/keyrings/myrepo.asc
        checksum: sha256:bb42f0db45d46bab5f9ec619e1a47360b94c27142e57aa71f7050d08672309e0

    - name: somerepo | apt source
      ansible.builtin.apt_repository:
        repo: "deb [arch=amd64 signed-by=/etc/apt/keyrings/myrepo.asc] https://download.example.com/linux/ubuntu {{ ansible_distribution_release }} stable"
        state: present

- name: Add an apt key by id from a keyserver
  ansible.builtin.apt_key:
    keyserver: keyserver.ubuntu.com
    id: 36A1D7869245C8950F966E92D8576A8BA88D21E9

- name: Add an Apt signing key, uses whichever key is at the URL
  ansible.builtin.apt_key:
    url: https://ftp-master.debian.org/keys/archive-key-6.0.asc
    state: present

- name: Add an Apt signing key, will not download if present
  ansible.builtin.apt_key:
    id: 9FED2BCBDCD29CDF762678CBAED4B06F473041FA
    url: https://ftp-master.debian.org/keys/archive-key-6.0.asc
    state: present

- name: Remove a Apt specific signing key, leading 0x is valid
  ansible.builtin.apt_key:
    id: 0x9FED2BCBDCD29CDF762678CBAED4B06F473041FA
    state: absent

# Use armored file since utf-8 string is expected. Must be of "PGP PUBLIC KEY BLOCK" type.
- name: Add a key from a file on the Ansible server
  ansible.builtin.apt_key:
    data: "{{ lookup('ansible.builtin.file', 'apt.asc') }}"
    state: present

- name: Add an Apt signing key to a specific keyring file
  ansible.builtin.apt_key:
    id: 9FED2BCBDCD29CDF762678CBAED4B06F473041FA
    url: https://ftp-master.debian.org/keys/archive-key-6.0.asc
    keyring: /etc/apt/trusted.gpg.d/debian.gpg

- name: Add Apt signing key on remote server to keyring
  ansible.builtin.apt_key:
    id: 9FED2BCBDCD29CDF762678CBAED4B06F473041FA
    file: /tmp/apt.gpg
    state: present
```

## [Return Values](apt_key_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | List of apt key ids or fingerprints after any modification  **Returned:** on change  **Sample:** `["D8576A8BA88D21E9", "3B4FE6ACC0B21F32", "D94AA3F0EFE21092", "871920D1991BC93C"]` |
| **before**  list / elements=string | List of apt key ids or fingprints before any modifications  **Returned:** always  **Sample:** `["3B4FE6ACC0B21F32", "D94AA3F0EFE21092", "871920D1991BC93C"]` |
| **fp**  string | Fingerprint of the key to import  **Returned:** always  **Sample:** `"D8576A8BA88D21E9"` |
| **id**  string | key id from source  **Returned:** always  **Sample:** `"36A1D7869245C8950F966E92D8576A8BA88D21E9"` |
| **key_id**  string | calculated key id, it should be same as ‘id’, but can be different  **Returned:** always  **Sample:** `"36A1D7869245C8950F966E92D8576A8BA88D21E9"` |
| **short_id**  string | calculated short key id  **Returned:** always  **Sample:** `"A88D21E9"` |

### Authors

- Jayson Vantuyl (@jvantuyl)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
