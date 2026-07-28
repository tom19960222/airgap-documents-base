---
collection: ansible
version: "6"
title: "Interactive input: prompts"
source_url: https://docs.ansible.com/projects/ansible/6/user_guide/playbooks_prompts.html
fetched_at: 2026-07-27T16:40:25+00:00
---
# Interactive input: prompts

If you want your playbook to prompt the user for certain input, add a ‘vars_prompt’ section. Prompting the user for variables lets you avoid recording sensitive data like passwords. In addition to security, prompts support flexibility. For example, if you use one playbook across multiple software releases, you could prompt for the particular release version.

- [Hashing values supplied by `vars_prompt`](playbooks_prompts.md#hashing-values-supplied-by-vars-prompt)
- [Allowing special characters in `vars_prompt` values](playbooks_prompts.md#allowing-special-characters-in-vars-prompt-values)

Here is a most basic example:

```yaml
---
- hosts: all
  vars_prompt:

    - name: username
      prompt: What is your username?
      private: no

    - name: password
      prompt: What is your password?

  tasks:

    - name: Print a message
      ansible.builtin.debug:
        msg: 'Logging in as {{ username }}'
```

The user input is hidden by default but it can be made visible by setting `private: no`.

> **Note:**
>
> Prompts for individual `vars_prompt` variables will be skipped for any variable that is already defined through the command line `--extra-vars` option, or when running from a non-interactive session (such as cron or Ansible AWX). See [Defining variables at runtime](playbooks_variables.md#passing-variables-on-the-command-line).

If you have a variable that changes infrequently, you can provide a default value that can be overridden.

```yaml
vars_prompt:

  - name: release_version
    prompt: Product release version
    default: "1.0"
```

## [Hashing values supplied by `vars_prompt`](playbooks_prompts.md#id1)

You can hash the entered value so you can use it, for instance, with the user module to define a password:

```yaml
vars_prompt:

  - name: my_password2
    prompt: Enter password2
    private: yes
    encrypt: sha512_crypt
    confirm: yes
    salt_size: 7
```

If you have [Passlib](https://passlib.readthedocs.io/en/stable/) installed, you can use any crypt scheme the library supports:

- *des_crypt* - DES Crypt
- *bsdi_crypt* - BSDi Crypt
- *bigcrypt* - BigCrypt
- *crypt16* - Crypt16
- *md5_crypt* - MD5 Crypt
- *bcrypt* - BCrypt
- *sha1_crypt* - SHA-1 Crypt
- *sun_md5_crypt* - Sun MD5 Crypt
- *sha256_crypt* - SHA-256 Crypt
- *sha512_crypt* - SHA-512 Crypt
- *apr_md5_crypt* - Apache’s MD5-Crypt variant
- *phpass* - PHPass’ Portable Hash
- *pbkdf2_digest* - Generic PBKDF2 Hashes
- *cta_pbkdf2_sha1* - Cryptacular’s PBKDF2 hash
- *dlitz_pbkdf2_sha1* - Dwayne Litzenberger’s PBKDF2 hash
- *scram* - SCRAM Hash
- *bsd_nthash* - FreeBSD’s MCF-compatible nthash encoding

The only parameters accepted are ‘salt’ or ‘salt_size’. You can use your own salt by defining
‘salt’, or have one generated automatically using ‘salt_size’. By default Ansible generates a salt
of size 8.

New in version 2.7.

If you do not have Passlib installed, Ansible uses the [crypt](https://docs.python.org/3/library/crypt.html) library as a fallback. Ansible supports at most four crypt schemes, depending on your platform at most the following crypt schemes are supported:

- *bcrypt* - BCrypt
- *md5_crypt* - MD5 Crypt
- *sha256_crypt* - SHA-256 Crypt
- *sha512_crypt* - SHA-512 Crypt

New in version 2.8.

## [Allowing special characters in `vars_prompt` values](playbooks_prompts.md#id2)

Some special characters, such as `{` and `%` can create templating errors. If you need to accept special characters, use the `unsafe` option:

```yaml
vars_prompt:
  - name: my_password_with_weird_chars
    prompt: Enter password
    unsafe: yes
    private: yes
```

> **See also:**
>
> [Intro to playbooks](playbooks_intro.md#playbooks-intro)
> :   An introduction to playbooks
>
> [Conditionals](playbooks_conditionals.md#playbooks-conditionals)
> :   Conditional statements in playbooks
>
> [Using Variables](playbooks_variables.md#playbooks-variables)
> :   All about variables
>
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
