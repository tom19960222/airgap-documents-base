---
collection: ansible
version: "8"
title: "ansible.builtin.rpm_key module – Adds or removes a gpg key from the rpm db"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/rpm_key_module.html
fetched_at: 2026-07-28T01:07:40+00:00
---
# ansible.builtin.rpm_key module – Adds or removes a gpg key from the rpm db

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `rpm_key` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.rpm_key` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](rpm_key_module.md#synopsis)
- [Parameters](rpm_key_module.md#parameters)
- [Attributes](rpm_key_module.md#attributes)
- [Examples](rpm_key_module.md#examples)

## [Synopsis](rpm_key_module.md#id1)

- Adds or removes (rpm –import) a gpg key to your rpm database.

## [Parameters](rpm_key_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **fingerprint**  string  *added in Ansible 2.9* | The long-form fingerprint of the key being imported.  This will be used to verify the specified key. |
| **key**  string / required | Key that will be modified. Can be a url, a file on the managed node, or a keyid if the key already exists in the database. |
| **state**  string | If the key will be imported or removed from the rpm db.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **validate_certs**  boolean | If `false` and the `key` is a url starting with https, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](rpm_key_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **rhel** | Target OS/families that can be operated against |

## [Examples](rpm_key_module.md#id4)

```yaml+jinja
- name: Import a key from a url
  ansible.builtin.rpm_key:
    state: present
    key: http://apt.sw.be/RPM-GPG-KEY.dag.txt

- name: Import a key from a file
  ansible.builtin.rpm_key:
    state: present
    key: /path/to/key.gpg

- name: Ensure a key is not present in the db
  ansible.builtin.rpm_key:
    state: absent
    key: DEADB33F

- name: Verify the key, using a fingerprint, before import
  ansible.builtin.rpm_key:
    key: /path/to/RPM-GPG-KEY.dag.txt
    fingerprint: EBC6 E12C 62B1 C734 026B  2122 A20E 5214 6B8D 79E6
```

### Authors

- Hector Acosta (@hacosta)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
