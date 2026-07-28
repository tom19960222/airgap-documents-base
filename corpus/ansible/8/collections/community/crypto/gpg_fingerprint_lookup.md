---
collection: ansible
version: "8"
title: "community.crypto.gpg_fingerprint lookup – Retrieve a GPG fingerprint from a GPG public or private key file"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/gpg_fingerprint_lookup.html
fetched_at: 2026-07-28T01:42:49+00:00
---
# community.crypto.gpg_fingerprint lookup – Retrieve a GPG fingerprint from a GPG public or private key file

> **Note:**
>
> This lookup plugin is part of the [community.crypto collection](https://galaxy.ansible.com/ui/repo/published/community/crypto/) (version 2.16.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.crypto`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](gpg_fingerprint_lookup.md#ansible-collections-community-crypto-gpg-fingerprint-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.gpg_fingerprint`.

New in community.crypto 2.15.0

- [Synopsis](gpg_fingerprint_lookup.md#synopsis)
- [Requirements](gpg_fingerprint_lookup.md#requirements)
- [Terms](gpg_fingerprint_lookup.md#terms)
- [See Also](gpg_fingerprint_lookup.md#see-also)
- [Examples](gpg_fingerprint_lookup.md#examples)
- [Return Value](gpg_fingerprint_lookup.md#return-value)

## [Synopsis](gpg_fingerprint_lookup.md#id1)

- Takes a list of filenames pointing to GPG public or private key files. Returns the fingerprints for each of these keys.

## [Requirements](gpg_fingerprint_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- GnuPG (`gpg` executable)

## [Terms](gpg_fingerprint_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=path / required | A path to a GPG public or private key. |

## [See Also](gpg_fingerprint_lookup.md#id4)

> **See also:**
>
> [community.crypto.gpg_fingerprint](gpg_fingerprint_filter.md#ansible-collections-community-crypto-gpg-fingerprint-filter) filter plugin
> :   Retrieve a GPG fingerprint from a GPG public or private key.

## [Examples](gpg_fingerprint_lookup.md#id5)

```yaml+jinja
- name: Show fingerprint of GPG public key
  ansible.builtin.debug:
    msg: "{{ lookup('community.crypto.gpg_fingerprint', '/path/to/public_key.gpg') }}"
```

## [Return Value](gpg_fingerprint_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | The fingerprints of the provided public or private GPG keys.  The list has one entry for every path provided.  **Returned:** success |

### Authors

- Felix Fontein (@felixfontein)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
