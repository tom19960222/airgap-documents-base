---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_sv_manage_security module – This module manages security options on IBM Storage Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_sv_manage_security_module.html
fetched_at: 2026-07-28T02:35:17+00:00
---
# ibm.storage_virtualize.ibm_sv_manage_security module – This module manages security options on IBM Storage Virtualize family storage systems

> **Note:**
>
> This module is part of the [ibm.storage_virtualize collection](https://galaxy.ansible.com/ui/repo/published/ibm/storage_virtualize/) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.storage_virtualize`.
>
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_sv_manage_security`.

New in ibm.storage_virtualize 2.1.0

- [Synopsis](ibm_sv_manage_security_module.md#synopsis)
- [Parameters](ibm_sv_manage_security_module.md#parameters)
- [Notes](ibm_sv_manage_security_module.md#notes)
- [Examples](ibm_sv_manage_security_module.md#examples)

## [Synopsis](ibm_sv_manage_security_module.md#id1)

- Ansible interface to manage ‘chsecurity’ command.

## [Parameters](ibm_sv_manage_security_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **checkpasswordhistory**  string | Specifies whether the system prevents the user from reusing a previous password.  **Choices:**   - `"yes"` - `"no"` |
| **clitimeout**  integer | Specifies the amount of time (in minutes) in range 5 - 240 before a session expires and the user is logged out of the CLI for inactivity. |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize storage system. |
| **disablesuperusercim**  string | Specifies whether CIMOM access must be disabled for the superuser.  **Choices:**   - `"yes"` - `"no"` |
| **disablesuperusergui**  string | Specifies whether GUI access must be disabled for the superuser.  **Choices:**   - `"yes"` - `"no"` |
| **disablesuperuserrest**  string | Specifies whether REST API access must be disabled for the superuser.  **Choices:**   - `"yes"` - `"no"` |
| **domain**  string | Domain for the Storage Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **expirywarning**  integer | Specifies the number of days in range 0 -30 before a password expires to raise a warning. The warning is displayed on every CLI login until the password is changed. A value of 0 means that the feature is disabled and warnings are not displayed. |
| **guitimeout**  integer | Specifies the amount of time (in minutes) in range 5 - 240 before a session expires and the user is logged out of the GUI for inactivity. |
| **lockoutperiod**  integer | Specifies the number of minutes in range 0 - 10080 that a user is locked out for if the max failed logins value is reached. A value of 0 implies the user is indefinitely locked out when the max failed login attempts are reached. |
| **log_path**  string | Path of debug log file. |
| **maxfailedlogins**  integer | Specifies the number of failed login attempts in range 0 -10 before the user account is locked for the amount of time that is specified in lockout period. A value of 0 means that the feature is disabled and accounts are not locked out after failed login attempts. |
| **maxpasswordhistory**  integer | Specifies the number of previous passwords in range 0 - 10 to compare with if checkpasswordhistory is enabled. A value of 0 means that the new password is compared with the current password only. |
| **minpasswordage**  integer | Specifies the minimum number of days between password changes in range 0 -365. This setting is enforced if checkpasswordhistory is enabled. This restriction is ignored if the password is expired. The setting does nothing if the value is greater than the passwordexpiry value. |
| **minpasswordlength**  integer | Specifies the minimum length requirement in range 6 -64 for user account passwords on the system. |
| **password**  string | REST API password for the Storage Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **passworddigits**  integer | Specifies mimimum number of digits in range 0 -3 required in passwords for local users. |
| **passwordexpiry**  integer | Specifies the number of days in range 0 - 365 before a password expires. A value of 0 means the feature is disabled and passwords do not expire. |
| **passwordlowercase**  integer | Specifies number of minimum lowercase characters in range 0 - 3 required in passwords for local users. |
| **passwordspecialchars**  integer | Specifies number of minimum required special characters in range 0 - 3 in passwords for local users. |
| **passworduppercase**  integer | Specifies number of minimum uppercase characters in range 0 - 3 in passwords for local users. |
| **resetsshprotocol**  boolean | Resets the SSH protocol security level to the default value 3 and configures the system to automatically follow the suggested level.  **Choices:**   - `false` - `true` |
| **restapitimeout**  integer | Specifies token expiry time in minutes in the range 10 - 120. |
| **sshgracetime**  integer | Specifies the duration of time in seconds in range 15-1800, a user has to enter login factors per SSH connection before the connection is terminated. |
| **sshmaxtries**  integer | Specifies the amount of allowed login attempts (in range 1-10) per a single SSH connection. |
| **sshprotocol**  integer | Specifies the numeric value for the SSH security level setting in range 1 - 3.  The level 1 Allows the following key exchange methods curve25519-sha256 [curve25519-sha256@libssh.org](mailto:curve25519-sha256%40libssh.org) ecdh-sha2-nistp256 ecdh-sha2-nistp384 ecdh-sha2-nistp521 diffie-hellman-group-exchange-sha256 diffie-hellman-group16-sha512 diffie-hellman-group18-sha512 diffie-hellman-group14-sha256 diffie-hellman-group14-sha1 diffie-hellman-group1-sha1 diffie-hellman-group-exchange-sha1  The level 2 Allows the following key exchange methods curve25519-sha256 [curve25519-sha256@libssh.org](mailto:curve25519-sha256%40libssh.org) ecdh-sha2-nistp256 ecdh-sha2-nistp384 ecdh-sha2-nistp521 diffie-hellman-group-exchange-sha256 diffie-hellman-group16-sha512 diffie-hellman-group18-sha512 diffie-hellman-group14-sha256 diffie-hellman-group14-sha1  The level 3 Allows the following key exchange methods curve25519-sha256 [curve25519-sha256@libssh.org](mailto:curve25519-sha256%40libssh.org) ecdh-sha2-nistp256 ecdh-sha2-nistp384 ecdh-sha2-nistp521 diffie-hellman-group-exchange-sha256 diffie-hellman-group16-sha512 diffie-hellman-group18-sha512 diffie-hellman-group14-sha256 |
| **superuserlocking**  string | Specifies whether the locking policy configured on the system also applies to the superuser. The value is either enable or disable. This parameter is only supported on systems with a dedicated technician port.  **Choices:**   - `"enable"` - `"disable"` |
| **superusermultifactor**  string | Specifies whether the superuser should be prompted for multifactor authentication.  **Choices:**   - `"yes"` - `"no"` |
| **superuserpasswordkeyrequired**  string | Specifies whether the superuser must provide both a password and SSH key for authentication.  **Choices:**   - `"yes"` - `"no"` |
| **token**  string | The authentication token to verify a user on the Storage Virtualize storage system.  To generate a token, use the ibm_svc_auth module. |
| **username**  string | REST API username for the Storage Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_sv_manage_security_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_sv_manage_security_module.md#id4)

```yaml+jinja
- name: Change max failed login limit
  ibm.storage_virtualize.ibm_sv_manage_security:
   clustername: "{{cluster}}"
   username: "{{username}}"
   password: "{{password}}"
   log_path: /tmp/playbook.debug
   maxfailedlogins: 5

- name: Change SSH protocol level
  ibm.storage_virtualize.ibm_sv_manage_security:
   clustername: "{{cluster}}"
   username: "{{username}}"
   password: "{{password}}"
   log_path: /tmp/playbook.debug
   sshprotocol: 2
```

### Authors

- Sumit Kumar Gupta (@sumitguptaibm)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
