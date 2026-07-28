---
collection: ansible
version: "6"
title: "community.windows.win_credential module – Manages Windows Credentials in the Credential Manager"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_credential_module.html
fetched_at: 2026-07-27T17:23:12+00:00
---
# community.windows.win_credential module – Manages Windows Credentials in the Credential Manager

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_credential`.

- [Synopsis](win_credential_module.md#synopsis)
- [Parameters](win_credential_module.md#parameters)
- [Notes](win_credential_module.md#notes)
- [See Also](win_credential_module.md#see-also)
- [Examples](win_credential_module.md#examples)

## [Synopsis](win_credential_module.md#id1)

- Used to create and remove Windows Credentials in the Credential Manager.
- This module can manage both standard username/password credentials as well as certificate credentials.

## [Parameters](win_credential_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **alias**  string | Adds an alias for the credential.  Typically this is the NetBIOS name of a host if *name* is set to the DNS name. |
| **attributes**  list / elements=dictionary | A list of dicts that set application specific attributes for a credential.  When set, existing attributes will be compared to the list as a whole, any differences means all attributes will be replaced. |
| **data**  string | The value for the attribute. |
| **data_format**  string | Controls the input type for *data*.  If `text`, *data* is a text string that is UTF-16LE encoded to bytes.  If `base64`, *data* is a base64 string that is base64 decoded to bytes.  Choices:   - `"base64"` - `"text"` ← (default) |
| **name**  string / required | The key for the attribute.  This is not a unique identifier as multiple attributes can have the same key. |
| **comment**  string | A user defined comment for the credential. |
| **name**  string / required | The target that identifies the server or servers that the credential is to be used for.  If the value can be a NetBIOS name, DNS server name, DNS host name suffix with a wildcard character (`*`), a NetBIOS of DNS domain name that contains a wildcard character sequence, or an asterisk.  See `TargetName` in <https://docs.microsoft.com/en-us/windows/win32/api/wincred/ns-wincred-credentiala> for more details on what this value can be.  This is used with *type* to produce a unique credential. |
| **persistence**  string | Defines the persistence of the credential.  If `local`, the credential will persist for all logons of the same user on the same host.  `enterprise` is the same as `local` but the credential is visible to the same domain user when running on other hosts and not just localhost.  Choices:   - `"enterprise"` - `"local"` ← (default) |
| **secret**  string | The secret for the credential.  When omitted, then no secret is used for the credential if a new credentials is created.  When *type* is a password type, this is the password for *username*.  When *type* is a certificate type, this is the pin for the certificate. |
| **secret_format**  string | Controls the input type for *secret*.  If `text`, *secret* is a text string that is UTF-16LE encoded to bytes.  If `base64`, *secret* is a base64 string that is base64 decoded to bytes.  Choices:   - `"base64"` - `"text"` ← (default) |
| **state**  string | When `absent`, the credential specified by *name* and *type* is removed.  When `present`, the credential specified by *name* and *type* is removed.  Choices:   - `"absent"` - `"present"` ← (default) |
| **type**  string / required | The type of credential to store.  This is used with *name* to produce a unique credential.  When the type is a `domain` type, the credential is used by Microsoft authentication packages like Negotiate.  When the type is a `generic` type, the credential is not used by any particular authentication package.  It is recommended to use a `domain` type as only authentication providers can access the secret.  Choices:   - `"domain_certificate"` - `"domain_password"` - `"generic_certificate"` - `"generic_password"` |
| **update_secret**  string | When `always`, the secret will always be updated if they differ.  When `on_create`, the secret will only be checked/updated when it is first created.  If the secret cannot be retrieved and this is set to `always`, the module will always result in a change.  Choices:   - `"always"` ← (default) - `"on_create"` |
| **username**  string | When *type* is a password type, then this is the username to store for the credential.  When *type* is a credential type, then this is the thumbprint as a hex string of the certificate to use.  When `type=domain_password`, this should be in the form of a Netlogon (DOMAIN\Username) or a UPN ([username@DOMAIN](mailto:username%40DOMAIN)).  If using a certificate thumbprint, the certificate must exist in the `CurrentUser\My` certificate store for the executing user. |

## [Notes](win_credential_module.md#id3)

> **Note:**
>
> - This module requires to be run with `become` so it can access the user’s credential store.
> - There can only be one credential per host and type. if a second credential is defined that uses the same host and type, then the original credential is overwritten.

## [See Also](win_credential_module.md#id4)

> **See also:**
>
> [ansible.windows.win_user_right](../../ansible/windows/win_user_right_module.md#ansible-collections-ansible-windows-win-user-right-module)
> :   Manage Windows User Rights.
>
> [ansible.windows.win_whoami](../../ansible/windows/win_whoami_module.md#ansible-collections-ansible-windows-win-whoami-module)
> :   Get information about the current user and process.

## [Examples](win_credential_module.md#id5)

```yaml+jinja
- name: Create a local only credential
  community.windows.win_credential:
    name: server.domain.com
    type: domain_password
    username: DOMAIN\username
    secret: Password01
    state: present

- name: Remove a credential
  community.windows.win_credential:
    name: server.domain.com
    type: domain_password
    state: absent

- name: Create a credential with full values
  community.windows.win_credential:
    name: server.domain.com
    type: domain_password
    alias: server
    username: username@DOMAIN.COM
    secret: Password01
    comment: Credential for server.domain.com
    persistence: enterprise
    attributes:
    - name: Source
      data: Ansible
    - name: Unique Identifier
      data: Y3VzdG9tIGF0dHJpYnV0ZQ==
      data_format: base64

- name: Create a certificate credential
  community.windows.win_credential:
    name: '*.domain.com'
    type: domain_certificate
    username: 0074CC4F200D27DC3877C24A92BA8EA21E6C7AF4
    state: present

- name: Create a generic credential
  community.windows.win_credential:
    name: smbhost
    type: generic_password
    username: smbuser
    secret: smbuser
    state: present

- name: Remove a generic credential
  community.windows.win_credential:
    name: smbhost
    type: generic_password
    state: absent
```

### Authors

- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
