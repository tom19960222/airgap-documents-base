---
collection: ansible
version: "6"
title: "cyberark.pas.cyberark_authentication module – CyberArk Authentication using PAS Web Services SDK."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cyberark/pas/cyberark_authentication_module.html
fetched_at: 2026-07-27T17:24:44+00:00
---
# cyberark.pas.cyberark_authentication module – CyberArk Authentication using PAS Web Services SDK.

> **Note:**
>
> This module is part of the [cyberark.pas collection](https://galaxy.ansible.com/cyberark/pas) (version 1.0.14).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cyberark.pas`.
>
> To use it in a playbook, specify: `cyberark.pas.cyberark_authentication`.

New in cyberark.pas 2.4

- [Synopsis](cyberark_authentication_module.md#synopsis)
- [Parameters](cyberark_authentication_module.md#parameters)
- [Examples](cyberark_authentication_module.md#examples)
- [Return Values](cyberark_authentication_module.md#return-values)

## [Synopsis](cyberark_authentication_module.md#id1)

- Authenticates to CyberArk Vault using Privileged Account Security Web Services SDK and creates a session fact that can be used by other modules. It returns an Ansible fact called *cyberark_session*. Every module can use this fact as `cyberark_session` parameter.

## [Parameters](cyberark_authentication_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_base_url**  string | A string containing the base URL of the server hosting CyberArk’s Privileged Account Security Web Services SDK. |
| **connection_number**  integer | To support multiple connections for same user specify  different value for this parameter. |
| **cyberark_session**  dictionary | Dictionary set by a CyberArk authentication containing the different values to perform actions on a logged-on CyberArk session. |
| **new_password**  string | The new password of the user. This parameter is optional, and enables you to change a password. |
| **password**  string | The password of the user. |
| **state**  string | Specifies if an authentication logon/logoff and a cyberark_session should be added/removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_cyberark_authentication**  boolean | Whether or not LDAP will be used.  Choices:   - `false` ← (default) - `true` |
| **use_ldap_authentication**  boolean | Whether or not LDAP will be used.  Choices:   - `false` ← (default) - `true` |
| **use_radius_authentication**  boolean | Whether or not users will be authenticated via a RADIUS server. Valid values are true/false.  Choices:   - `false` ← (default) - `true` |
| **use_windows_authentication**  boolean | Whether or not Windows will be used.  Choices:   - `false` ← (default) - `true` |
| **username**  string | The name of the user who will logon to the Vault. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only set to `false` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](cyberark_authentication_module.md#id3)

```yaml+jinja
- name: Logon - use_shared_logon_authentication
  cyberark_authentication:
    api_base_url: "{{ web_services_base_url }}"
    use_shared_logon_authentication: yes

- name: Logon - Not use_shared_logon_authentication
  cyberark_authentication:
    api_base_url: "{{ web_services_base_url }}"
    username: "{{ password_object.password }}"
    password: "{{ password_object.passprops.username }}"
    use_shared_logon_authentication: no

- name: Logoff from CyberArk Vault
  cyberark_authentication:
    state: absent
    cyberark_session: "{{ cyberark_session }}"
```

## [Return Values](cyberark_authentication_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cyberark_session**  complex | Authentication facts.  Returned: success |
| **api_base_url**  string | Base URL for API calls. Returned in the cyberark_session, so it can be used in subsequent calls.  Returned: always |
| **token**  string | The token that identifies the session, encoded in BASE 64.  Returned: always |
| **use_shared_logon_authentication**  boolean | Whether or not Shared Logon Authentication was used to establish the session.  Returned: always |
| **validate_certs**  boolean | Whether or not SSL certificates should be validated.  Returned: always |

### Authors

- Edward Nunez (@enunez-cyberark) CyberArk BizDev
- Cyberark Bizdev (@cyberark-bizdev)
- Edgar Mota

### Collection links

[Issue Tracker](https://github.com/cyberark/ansible-security-automation-collection/issues)
[Repository (Sources)](https://github.com/cyberark/ansible-security-automation-collection)
