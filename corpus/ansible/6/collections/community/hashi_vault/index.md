---
collection: ansible
version: "6"
title: "Community.Hashi_Vault"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/hashi_vault/
fetched_at: 2026-07-28T00:24:59+00:00
---
# Community.Hashi_Vault

Collection version 3.4.0

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Changelog](index.md#changelog)
- [Guides](index.md#guides)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Plugins related to HashiCorp Vault

**Authors:**

- Julie Davila (@juliedavila) <julie(at)davila.io>
- Brian Scholer (@briantist)

**Supported ansible-core versions:**

- 2.11.0 or newer

[Issue Tracker](https://github.com/ansible-collections/community.hashi_vault/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.hashi_vault)
[Discussion, Q&A, troubleshooting](https://github.com/ansible-collections/community.hashi_vault/discussions)

## [Communication](index.md#id2)

- Matrix room `#users:ansible.im`: [General usage and support questions](https://matrix.to/#/#users:ansible.im).
- IRC channel `#ansible` (Libera network):
  [General usage and support questions](https://web.libera.chat/?channel=#ansible).

## [Changelog](index.md#id3)

- [community.hashi_vault Release Notes](docsite/CHANGELOG.md)

## [Guides](index.md#id4)

- [Filter guide](docsite/filter_guide.md)
- [User guide](docsite/user_guide.md)
- [Migrating from the `hashi_vault` lookup](docsite/migration_hashi_vault_lookup.md)
- [About the `hashi_vault` lookup](docsite/about_hashi_vault_lookup.md)
- [Lookup guide](docsite/lookup_guide.md)
- [Contributor guide](docsite/contributor_guide.md)
- [localenv developer guide](docsite/localenv_developer_guide.md)

## [Plugin Index](index.md#id5)

These are the plugins in the community.hashi_vault collection:

### Modules

- [vault_kv1_get module](vault_kv1_get_module.md#ansible-collections-community-hashi-vault-vault-kv1-get-module) – Get a secret from HashiCorp Vault’s KV version 1 secret store
- [vault_kv2_delete module](vault_kv2_delete_module.md#ansible-collections-community-hashi-vault-vault-kv2-delete-module) – Delete one or more versions of a secret from HashiCorp Vault’s KV version 2 secret store
- [vault_kv2_get module](vault_kv2_get_module.md#ansible-collections-community-hashi-vault-vault-kv2-get-module) – Get a secret from HashiCorp Vault’s KV version 2 secret store
- [vault_login module](vault_login_module.md#ansible-collections-community-hashi-vault-vault-login-module) – Perform a login operation against HashiCorp Vault
- [vault_pki_generate_certificate module](vault_pki_generate_certificate_module.md#ansible-collections-community-hashi-vault-vault-pki-generate-certificate-module) – Generates a new set of credentials (private key and certificate) using HashiCorp Vault PKI
- [vault_read module](vault_read_module.md#ansible-collections-community-hashi-vault-vault-read-module) – Perform a read operation against HashiCorp Vault
- [vault_token_create module](vault_token_create_module.md#ansible-collections-community-hashi-vault-vault-token-create-module) – Create a HashiCorp Vault token
- [vault_write module](vault_write_module.md#ansible-collections-community-hashi-vault-vault-write-module) – Perform a write operation against HashiCorp Vault

### Lookup Plugins

- [hashi_vault lookup](hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup) – Retrieve secrets from HashiCorp’s Vault
- [vault_ansible_settings lookup](vault_ansible_settings_lookup.md#ansible-collections-community-hashi-vault-vault-ansible-settings-lookup) – Returns plugin settings (options)
- [vault_kv1_get lookup](vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup) – Get a secret from HashiCorp Vault’s KV version 1 secret store
- [vault_kv2_get lookup](vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup) – Get a secret from HashiCorp Vault’s KV version 2 secret store
- [vault_login lookup](vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup) – Perform a login operation against HashiCorp Vault
- [vault_read lookup](vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup) – Perform a read operation against HashiCorp Vault
- [vault_token_create lookup](vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup) – Create a HashiCorp Vault token
- [vault_write lookup](vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup) – Perform a write operation against HashiCorp Vault

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
