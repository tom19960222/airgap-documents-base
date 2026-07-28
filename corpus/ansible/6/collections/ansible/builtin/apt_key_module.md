---
collection: ansible
version: "6"
title: "ansible.builtin.apt_key module – Add or remove an apt key"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/apt_key_module.html
fetched_at: 2026-07-27T16:43:57+00:00
---
# ansible.builtin.apt_key module – Add or remove an apt key

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `apt_key` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](apt_key_module.md#synopsis)
- [Requirements](apt_key_module.md#requirements)
- [Parameters](apt_key_module.md#parameters)
- [Attributes](apt_key_module.md#attributes)
- [Notes](apt_key_module.md#notes)
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
| **state**  string | Ensures that the key is present (added) or absent (revoked).  Choices:   - `"absent"` - `"present"` ← (default) |
| **url**  string | The URL to retrieve key from. |
| **validate_certs**  boolean | If `no`, SSL certificates for the target url will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Attributes](apt_key_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | Platform: debian | Target OS/families that can be operated against |

## [Notes](apt_key_module.md#id5)

> **Note:**
>
> - The apt-key command has been deprecated and suggests to ‘manage keyring files in trusted.gpg.d instead’. See the Debian wiki for details. This module is kept for backwards compatiblity for systems that still use apt-key as the main way to manage apt repository keys.
> - As a sanity check, downloaded key id must match the one specified.
> - Use full fingerprint (40 characters) key ids to avoid key collisions. To generate a full-fingerprint imported key: `apt-key adv --list-public-keys --with-fingerprint --with-colons`.
> - If you specify both the key id and the URL with `state=present`, the task can verify or add the key as needed.
> - Adding a new key requires an apt cache update (e.g. using the [ansible.builtin.apt](apt_module.md#ansible-collections-ansible-builtin-apt-module) module’s update_cache option).

## [Examples](apt_key_module.md#id6)

```yaml+jinja
- name: One way to avoid apt_key once it is removed from your distro
  block:
    - name: somerepo |no apt key
      ansible.builtin.get_url:
        url: https://download.example.com/linux/ubuntu/gpg
        dest: /etc/apt/trusted.gpg.d/somerepo.asc

    - name: somerepo | apt source
      ansible.builtin.apt_repository:
      repo: "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/somerepo.asc] https://download.example.com/linux/ubuntu {{ ansible_distribution_release }} stable"
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

## [Return Values](apt_key_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | List of apt key ids or fingerprints after any modification  Returned: on change  Sample: `["D8576A8BA88D21E9", "3B4FE6ACC0B21F32", "D94AA3F0EFE21092", "871920D1991BC93C"]` |
| **before**  list / elements=string | List of apt key ids or fingprints before any modifications  Returned: always  Sample: `["3B4FE6ACC0B21F32", "D94AA3F0EFE21092", "871920D1991BC93C"]` |
| **fp**  string | Fingerprint of the key to import  Returned: always  Sample: `"D8576A8BA88D21E9"` |
| **id**  string | key id from source  Returned: always  Sample: `"36A1D7869245C8950F966E92D8576A8BA88D21E9"` |
| **key_id**  string | calculated key id, it should be same as ‘id’, but can be different  Returned: always  Sample: `"36A1D7869245C8950F966E92D8576A8BA88D21E9"` |
| **short_id**  string | caclulated short key id  Returned: always  Sample: `"A88D21E9"` |

### Authors

- Jayson Vantuyl (@jvantuyl)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
