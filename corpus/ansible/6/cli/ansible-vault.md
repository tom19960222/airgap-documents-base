---
collection: ansible
version: "6"
title: "ansible-vault"
source_url: https://docs.ansible.com/projects/ansible/6/cli/ansible-vault.html
fetched_at: 2026-07-27T16:40:37+00:00
---
# ansible-vault

**encryption/decryption utility for Ansible data files**

- [Synopsis](ansible-vault.md#synopsis)
- [Description](ansible-vault.md#description)
- [Common Options](ansible-vault.md#common-options)
- [Actions](ansible-vault.md#actions)

  - [create](ansible-vault.md#create)
  - [decrypt](ansible-vault.md#decrypt)
  - [edit](ansible-vault.md#edit)
  - [view](ansible-vault.md#view)
  - [encrypt](ansible-vault.md#encrypt)
  - [encrypt_string](ansible-vault.md#encrypt-string)
  - [rekey](ansible-vault.md#rekey)
- [Environment](ansible-vault.md#environment)
- [Files](ansible-vault.md#files)
- [Author](ansible-vault.md#author)
- [License](ansible-vault.md#license)
- [See also](ansible-vault.md#see-also)

## [Synopsis](ansible-vault.md#id2)

```bash
usage: ansible-vault [-h] [--version] [-v]
                  {create,decrypt,edit,view,encrypt,encrypt_string,rekey}
                  ...
```

## [Description](ansible-vault.md#id3)

can encrypt any structured data file used by Ansible.
This can include *group_vars/* or *host_vars/* inventory variables,
variables loaded by *include_vars* or *vars_files*, or variable files
passed on the ansible-playbook command line with *-e @file.yml* or *-e @file.json*.
Role variables and defaults are also included!

Because Ansible tasks, handlers, and other objects are data, these can also be encrypted with vault.
If you’d like to not expose what variables you are using, you can keep an individual task file entirely encrypted.

## [Common Options](ansible-vault.md#id4)

--version
:   show program’s version number, config file location, configured module search path, module location, executable location and exit

-h, --help
:   show this help message and exit

-v, --verbose
:   Causes Ansible to print more debug messages. Adding multiple -v will increase the verbosity, the builtin plugins currently evaluate up to -vvvvvv. A reasonable level to start is -vvv, connection debugging might require -vvvv.

## [Actions](ansible-vault.md#id5)

### [create](ansible-vault.md#id6)

create and open a file in an editor that will be encrypted with the provided vault secret when closed

--ask-vault-password, --ask-vault-pass
:   ask for vault password

--encrypt-vault-id  <ENCRYPT_VAULT_ID>
:   the vault id used to encrypt (required if more than one vault-id is provided)

--vault-id
:   the vault identity to use

--vault-password-file, --vault-pass-file
:   vault password file

### [decrypt](ansible-vault.md#id7)

decrypt the supplied file using the provided vault secret

--ask-vault-password, --ask-vault-pass
:   ask for vault password

--output  <OUTPUT_FILE>
:   output file name for encrypt or decrypt; use - for stdout

--vault-id
:   the vault identity to use

--vault-password-file, --vault-pass-file
:   vault password file

### [edit](ansible-vault.md#id8)

open and decrypt an existing vaulted file in an editor, that will be encrypted again when closed

--ask-vault-password, --ask-vault-pass
:   ask for vault password

--encrypt-vault-id  <ENCRYPT_VAULT_ID>
:   the vault id used to encrypt (required if more than one vault-id is provided)

--vault-id
:   the vault identity to use

--vault-password-file, --vault-pass-file
:   vault password file

### [view](ansible-vault.md#id9)

open, decrypt and view an existing vaulted file using a pager using the supplied vault secret

--ask-vault-password, --ask-vault-pass
:   ask for vault password

--vault-id
:   the vault identity to use

--vault-password-file, --vault-pass-file
:   vault password file

### [encrypt](ansible-vault.md#id10)

encrypt the supplied file using the provided vault secret

--ask-vault-password, --ask-vault-pass
:   ask for vault password

--encrypt-vault-id  <ENCRYPT_VAULT_ID>
:   the vault id used to encrypt (required if more than one vault-id is provided)

--output  <OUTPUT_FILE>
:   output file name for encrypt or decrypt; use - for stdout

--vault-id
:   the vault identity to use

--vault-password-file, --vault-pass-file
:   vault password file

### [encrypt_string](ansible-vault.md#id11)

encrypt the supplied string using the provided vault secret

--ask-vault-password, --ask-vault-pass
:   ask for vault password

--encrypt-vault-id  <ENCRYPT_VAULT_ID>
:   the vault id used to encrypt (required if more than one vault-id is provided)

--output  <OUTPUT_FILE>
:   output file name for encrypt or decrypt; use - for stdout

--show-input
:   Do not hide input when prompted for the string to encrypt

--stdin-name  <ENCRYPT_STRING_STDIN_NAME>
:   Specify the variable name for stdin

--vault-id
:   the vault identity to use

--vault-password-file, --vault-pass-file
:   vault password file

-n, --name
:   Specify the variable name

-p, --prompt
:   Prompt for the string to encrypt

### [rekey](ansible-vault.md#id12)

re-encrypt a vaulted file with a new secret, the previous secret is required

--ask-vault-password, --ask-vault-pass
:   ask for vault password

--encrypt-vault-id  <ENCRYPT_VAULT_ID>
:   the vault id used to encrypt (required if more than one vault-id is provided)

--new-vault-id  <NEW_VAULT_ID>
:   the new vault identity to use for rekey

--new-vault-password-file  <NEW_VAULT_PASSWORD_FILE>
:   new vault password file for rekey

--vault-id
:   the vault identity to use

--vault-password-file, --vault-pass-file
:   vault password file

## [Environment](ansible-vault.md#id13)

The following environment variables may be specified.

[`ANSIBLE_CONFIG`](../reference_appendices/config.md#envvar-ANSIBLE_CONFIG) – Override the default ansible config file

Many more are available for most options in ansible.cfg

## [Files](ansible-vault.md#id14)

`/etc/ansible/ansible.cfg` – Config file, used if present

`~/.ansible.cfg` – User config file, overrides the default config if present

## [Author](ansible-vault.md#id15)

Ansible was originally written by Michael DeHaan.

See the AUTHORS file for a complete list of contributors.

## [License](ansible-vault.md#id16)

Ansible is released under the terms of the GPLv3+ License.

## [See also](ansible-vault.md#id17)

*ansible(1)*, *ansible-config(1)*, *ansible-console(1)*, *ansible-doc(1)*, *ansible-galaxy(1)*, *ansible-inventory(1)*, *ansible-playbook(1)*, *ansible-pull(1)*, *ansible-vault(1)*,
