---
collection: ansible
version: "8"
title: "Protecting sensitive data with Ansible vault"
source_url: https://docs.ansible.com/projects/ansible/8/vault_guide/index.html
fetched_at: 2026-07-28T00:57:43+00:00
---
# Protecting sensitive data with Ansible vault

> **Note:**
>
> **Making Open Source More Inclusive**
>
> Red Hat is committed to replacing problematic language in our code, documentation, and web properties. We are beginning with these four terms: master, slave, blacklist, and whitelist. We ask that you open an issue or pull request if you come upon a term that we have missed. For more details, see [our CTO Chris Wright’s message](https://www.redhat.com/en/blog/making-open-source-more-inclusive-eradicating-problematic-language).

Welcome to the Ansible vault documentation.
Ansible vault provides a way to encrypt and manage sensitive data such as passwords.
This guide introduces you to Ansible vault and covers the following topics:

- Managing vault passwords.
- Encrypting content and files with Ansible vault.
- Using encrypted variables and files.

- [Ansible Vault](vault.md)
- [Managing vault passwords](vault_managing_passwords.md)
  - [Choosing between a single password and multiple passwords](vault_managing_passwords.md#choosing-between-a-single-password-and-multiple-passwords)
  - [Managing multiple passwords with vault IDs](vault_managing_passwords.md#managing-multiple-passwords-with-vault-ids)
  - [Storing and accessing vault passwords](vault_managing_passwords.md#storing-and-accessing-vault-passwords)
- [Encrypting content with Ansible Vault](vault_encrypting_content.md)
  - [Encrypting individual variables with Ansible Vault](vault_encrypting_content.md#encrypting-individual-variables-with-ansible-vault)
  - [Encrypting files with Ansible Vault](vault_encrypting_content.md#encrypting-files-with-ansible-vault)
- [Using encrypted variables and files](vault_using_encrypted_content.md)
  - [Passing a single password](vault_using_encrypted_content.md#passing-a-single-password)
  - [Passing vault IDs](vault_using_encrypted_content.md#passing-vault-ids)
  - [Passing multiple vault passwords](vault_using_encrypted_content.md#passing-multiple-vault-passwords)
  - [Using `--vault-id` without a vault ID](vault_using_encrypted_content.md#using-vault-id-without-a-vault-id)
- [Configuring defaults for using encrypted content](vault_using_encrypted_content.md#configuring-defaults-for-using-encrypted-content)
  - [Setting a default vault ID](vault_using_encrypted_content.md#setting-a-default-vault-id)
  - [Setting a default password source](vault_using_encrypted_content.md#setting-a-default-password-source)
- [When are encrypted files made visible?](vault_using_encrypted_content.md#when-are-encrypted-files-made-visible)
- [Format of files encrypted with Ansible Vault](vault_using_encrypted_content.md#format-of-files-encrypted-with-ansible-vault)
  - [Ansible Vault payload format 1.1 - 1.2](vault_using_encrypted_content.md#ansible-vault-payload-format-1-1-1-2)
