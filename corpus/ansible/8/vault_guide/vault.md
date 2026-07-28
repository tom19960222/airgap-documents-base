---
collection: ansible
version: "8"
title: "Ansible Vault"
source_url: https://docs.ansible.com/projects/ansible/8/vault_guide/vault.html
fetched_at: 2026-07-28T00:58:35+00:00
---
# Ansible Vault

Ansible Vault encrypts variables and files so you can protect sensitive content such as passwords or keys rather than leaving it visible as plaintext in playbooks or roles.
To use Ansible Vault you need one or more passwords to encrypt and decrypt content.
If you store your vault passwords in a third-party tool such as a secret manager, you need a script to access them.
Use the passwords with the [ansible-vault](../cli/ansible-vault.md#ansible-vault) command-line tool to create and view encrypted variables, create encrypted files, encrypt existing files, or edit, re-key, or decrypt files.
You can then place encrypted content under source control and share it more safely.

> **Warning:**
>
> - Encryption with Ansible Vault ONLY protects ‘data at rest’.
>   Once the content is decrypted (‘data in use’), play and plugin authors are responsible for avoiding any secret disclosure, see [no_log](../reference_appendices/faq.md#keep-secret-data) for details on hiding output and [Steps to secure your editor](vault_encrypting_content.md#vault-securing-editor) for security considerations on editors you use with Ansible Vault.

You can use encrypted variables and files in ad hoc commands and playbooks by supplying the passwords you used to encrypt them.
You can modify your `ansible.cfg` file to specify the location of a password file or to always prompt for the password.
