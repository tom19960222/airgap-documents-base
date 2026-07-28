---
collection: ansible
version: "6"
title: "ansible.windows.win_whoami module – Get information about the current user and process"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_whoami_module.html
fetched_at: 2026-07-27T16:43:21+00:00
---
# ansible.windows.win_whoami module – Get information about the current user and process

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ansible/windows) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_whoami`.

- [Synopsis](win_whoami_module.md#synopsis)
- [Notes](win_whoami_module.md#notes)
- [See Also](win_whoami_module.md#see-also)
- [Examples](win_whoami_module.md#examples)
- [Return Values](win_whoami_module.md#return-values)

## [Synopsis](win_whoami_module.md#id1)

- Designed to return the same information as the `whoami /all` command.
- Also includes information missing from `whoami` such as logon metadata like logon rights, id, type.

## [Notes](win_whoami_module.md#id2)

> **Note:**
>
> - If running this module with a non admin user, the logon rights will be an empty list as Administrator rights are required to query LSA for the information.

## [See Also](win_whoami_module.md#id3)

> **See also:**
>
> [community.windows.win_credential](../../community/windows/win_credential_module.md#ansible-collections-community-windows-win-credential-module)
> :   Manages Windows Credentials in the Credential Manager.
>
> [ansible.windows.win_group_membership](win_group_membership_module.md#ansible-collections-ansible-windows-win-group-membership-module)
> :   Manage Windows local group membership.
>
> [ansible.windows.win_user_right](win_user_right_module.md#ansible-collections-ansible-windows-win-user-right-module)
> :   Manage Windows User Rights.

## [Examples](win_whoami_module.md#id4)

```yaml+jinja
- name: Get whoami information
  ansible.windows.win_whoami:
```

## [Return Values](win_whoami_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  complex | The running account SID details.  Returned: success |
| **account_name**  string | The account name of the account SID.  Returned: success  Sample: `"Administrator"` |
| **domain_name**  string | The domain name of the account SID.  Returned: success  Sample: `"DOMAIN"` |
| **sid**  string | The SID in string form.  Returned: success  Sample: `"S-1-5-21-1654078763-769949647-2968445802-500"` |
| **type**  string | The type of SID.  Returned: success  Sample: `"User"` |
| **authentication_package**  string | The name of the authentication package used to authenticate the user in the session.  Returned: success  Sample: `"Negotiate"` |
| **dns_domain_name**  string | The DNS name of the logon session, this is an empty string if this is not set.  Returned: success  Sample: `"DOMAIN.COM"` |
| **groups**  list / elements=string | A list of groups and attributes that the user is a member of.  Returned: success  Sample: `[{"account_name": "Domain Users", "attributes": ["Mandatory", "Enabled by default", "Enabled"], "domain_name": "DOMAIN", "sid": "S-1-5-21-1654078763-769949647-2968445802-513", "type": "Group"}, {"account_name": "Administrators", "attributes": ["Mandatory", "Enabled by default", "Enabled", "Owner"], "domain_name": "BUILTIN", "sid": "S-1-5-32-544", "type": "Alias"}]` |
| **impersonation_level**  string | The impersonation level of the token, only valid if `token_type` is `TokenImpersonation`, see <https://msdn.microsoft.com/en-us/library/windows/desktop/aa379572.aspx>.  Returned: success  Sample: `"SecurityAnonymous"` |
| **label**  complex | The mandatory label set to the logon session.  Returned: success |
| **account_name**  string | The account name of the label SID.  Returned: success  Sample: `"High Mandatory Level"` |
| **domain_name**  string | The domain name of the label SID.  Returned: success  Sample: `"Mandatory Label"` |
| **sid**  string | The SID in string form.  Returned: success  Sample: `"S-1-16-12288"` |
| **type**  string | The type of SID.  Returned: success  Sample: `"Label"` |
| **login_domain**  string | The name of the domain used to authenticate the owner of the session.  Returned: success  Sample: `"DOMAIN"` |
| **login_time**  string | The logon time in ISO 8601 format  Returned: success  Sample: `"2017-11-27T06:24:14.3321665+10:00"` |
| **logon_id**  integer | The unique identifier of the logon session.  Returned: success  Sample: `20470143` |
| **logon_server**  string | The name of the server used to authenticate the owner of the logon session.  Returned: success  Sample: `"DC01"` |
| **logon_type**  string | The logon type that identifies the logon method, see <https://msdn.microsoft.com/en-us/library/windows/desktop/aa380129.aspx>.  Returned: success  Sample: `"Network"` |
| **privileges**  dictionary | A dictionary of privileges and their state on the logon token.  Returned: success  Sample: `{"SeChangeNotifyPrivileges": "enabled-by-default", "SeDebugPrivilege": "enabled", "SeRemoteShutdownPrivilege": "disabled"}` |
| **rights**  list / elements=string | A list of logon rights assigned to the logon.  Returned: success and running user is a member of the local Administrators group  Sample: `["SeNetworkLogonRight", "SeInteractiveLogonRight", "SeBatchLogonRight", "SeRemoteInteractiveLogonRight"]` |
| **token_type**  string | The token type to indicate whether it is a primary or impersonation token.  Returned: success  Sample: `"TokenPrimary"` |
| **upn**  string | The user principal name of the current user.  Returned: success  Sample: `"Administrator@DOMAIN.COM"` |
| **user_flags**  string | The user flags for the logon session, see UserFlags in <https://msdn.microsoft.com/en-us/library/windows/desktop/aa380128>.  Returned: success  Sample: `"Winlogon"` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
