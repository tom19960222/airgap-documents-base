---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.credential module – Configures a credential on a SQL server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/credential_module.html
fetched_at: 2026-07-28T02:40:29+00:00
---
# lowlydba.sqlserver.credential module – Configures a credential on a SQL server

> **Note:**
>
> This module is part of the [lowlydba.sqlserver collection](https://galaxy.ansible.com/ui/repo/published/lowlydba/sqlserver/) (version 2.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install lowlydba.sqlserver`.
> You need further requirements to be able to use this module,
> see [Requirements](credential_module.md#ansible-collections-lowlydba-sqlserver-credential-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.credential`.

New in lowlydba.sqlserver 1.3.0

- [Synopsis](credential_module.md#synopsis)
- [Requirements](credential_module.md#requirements)
- [Parameters](credential_module.md#parameters)
- [Attributes](credential_module.md#attributes)
- [Examples](credential_module.md#examples)
- [Return Values](credential_module.md#return-values)

## [Synopsis](credential_module.md#id1)

- Creates, replaces, or removes a credential on a SQL server.

## [Requirements](credential_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](credential_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | If this switch is enabled, the existing credential will be dropped and recreated.  **Choices:**   - `false` ← (default) - `true` |
| **identity**  string / required | The Credential Identity. |
| **mapped_class_type**  string | Sets the class associated with the credential.  **Choices:**   - `"CryptographicProvider"` - `"None"` |
| **name**  string | The Credential name. |
| **password**  string | Password used to authenticate the Credential Identity. |
| **provider_name**  string | Specifies the cryptographic provider name for the Enterprise Key Management Provider. |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |
| **state**  string | Whether or not the object should be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Attributes](credential_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Examples](credential_module.md#id5)

```yaml+jinja
- name: Create a credential with a password
  lowlydba.sqlserver.credential:
    sql_instance: sql-01.myco.io
    identity: ad\\user
    name: MyCredential
    password : <Password>

- name: Replace an existing credential
  lowlydba.sqlserver.credential:
    sql_instance: sql-01.myco.io
    identity: MyIdentity
    force: true

- name: Create a credential using a SAS token for a backup URL
  lowlydba.sqlserver.credential:
    sql_instance: sql-01.myco.io
    identity: SHARED ACCESS SIGNATURE
    name: https://<azure storage account name>.blob.core.windows.net/<blob container>
    password : <Shared Access Token>

- name: Remove a credential
  lowlydba.sqlserver.credential:
    sql_instance: sql-01.myco.io
    identity: MyIdentity
    state: absent
```

## [Return Values](credential_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `New-DbaDbCredential`, `Get-DbaDbCredential`, or `Remove-DbaDbCredential` function.  **Returned:** success, but not in check_mode. |

### Authors

- Joe Krilov (@Joey40)
- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
