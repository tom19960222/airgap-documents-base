---
collection: ansible
version: "6"
title: "community.windows.win_domain_user module – Manages Windows Active Directory user accounts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_domain_user_module.html
fetched_at: 2026-07-27T17:23:21+00:00
---
# community.windows.win_domain_user module – Manages Windows Active Directory user accounts

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
> To use it in a playbook, specify: `community.windows.win_domain_user`.

- [Synopsis](win_domain_user_module.md#synopsis)
- [Parameters](win_domain_user_module.md#parameters)
- [Notes](win_domain_user_module.md#notes)
- [See Also](win_domain_user_module.md#see-also)
- [Examples](win_domain_user_module.md#examples)
- [Return Values](win_domain_user_module.md#return-values)

## [Synopsis](win_domain_user_module.md#id1)

- Manages Windows Active Directory user accounts.

## [Parameters](win_domain_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **account_locked**  boolean | `no` will unlock the user account if locked.  Note that there is not a way to lock an account as an administrator.  Accounts are locked due to user actions; as an admin, you may only unlock a locked account.  If you wish to administratively disable an account, set *enabled* to `no`.  Choices:   - `false` - `true` |
| **attributes**  dictionary | A dict of custom LDAP attributes to set on the user.  This can be used to set custom attributes that are not exposed as module parameters, e.g. `telephoneNumber`.  See the examples on how to format this parameter. |
| **city**  string | Configures the user’s city. |
| **company**  string | Configures the user’s company name. |
| **country**  string | Configures the user’s country code.  Note that this is a two-character ISO 3166 code. |
| **delegates**  aliases: principals_allowed_to_delegate  list / elements=string  added in community.windows 1.10.0 | Specifies an array of principal objects. This parameter sets the msDS-AllowedToActOnBehalfOfOtherIdentity attribute of a computer account object.  Must be specified as a distinguished name `CN=shenetworks,CN=Users,DC=ansible,DC=test` |
| **description**  string | Description of the user |
| **domain_password**  string | The password for *username*. |
| **domain_server**  string | Specifies the Active Directory Domain Services instance to connect to.  Can be in the form of an FQDN or NetBIOS name.  If not specified then the value is based on the domain of the computer running PowerShell. |
| **domain_username**  string | The username to use when interacting with AD.  If this is not set then the user Ansible used to log in with will be used instead when using CredSSP or Kerberos with credential delegation. |
| **email**  string | Configures the user’s email address.  This is a record in AD and does not do anything to configure any email servers or systems. |
| **enabled**  boolean | `yes` will enable the user account.  `no` will disable the account.  Choices:   - `false` - `true` ← (default) |
| **firstname**  string | Configures the user’s first name (given name). |
| **groups**  list / elements=string | Adds or removes the user from this list of groups, depending on the value of *groups_action*.  To remove all but the Principal Group, set `groups=<principal group name>` and *groups_action=replace*.  Note that users cannot be removed from their principal group (for example, “Domain Users”). |
| **groups_action**  string | If `add`, the user is added to each group in *groups* where not already a member.  If `remove`, the user is removed from each group in *groups*.  If `replace`, the user is added as a member of each group in *groups* and removed from any other groups.  Choices:   - `"add"` - `"remove"` - `"replace"` ← (default) |
| **groups_missing_behaviour**  string  added in community.windows 1.10.0 | Controls what happens when a group specified by `groups` is an invalid group name.  `fail` is the default and will return an error any groups do not exist.  `ignore` will ignore any groups that does not exist.  `warn` will display a warning for any groups that do not exist but will continue without failing.  Choices:   - `"fail"` ← (default) - `"ignore"` - `"warn"` |
| **identity**  string | Identity parameter used to find the User in the Active Directory.  This value can be in the forms `Distinguished Name`, `objectGUID`, `objectSid` or `sAMAccountName`.  Default to `name` if not set. |
| **name**  string / required | Name of the user to create, remove or modify. |
| **password**  string | Optionally set the user’s password to this (plain text) value.  To enable an account - *enabled* - a password must already be configured on the account, or you must provide a password here. |
| **password_expired**  boolean | `yes` will require the user to change their password at next login.  `no` will clear the expired password flag.  This is mutually exclusive with *password_never_expires*.  Choices:   - `false` - `true` |
| **password_never_expires**  boolean | `yes` will set the password to never expire.  `no` will allow the password to expire.  This is mutually exclusive with *password_expired*.  Choices:   - `false` - `true` |
| **path**  string | Container or OU for the new user; if you do not specify this, the user will be placed in the default container for users in the domain.  Setting the path is only available when a new user is created; if you specify a path on an existing user, the user’s path will not be updated - you must delete (e.g., `state=absent`) the user and then re-add the user with the appropriate path. |
| **postal_code**  string | Configures the user’s postal code / zip code. |
| **sam_account_name**  string  added in community.windows 1.7.0 | Configures the SAM Account Name (`sAMAccountName`) for the account.  This is allowed to a maximum of 20 characters due to pre-Windows 2000 restrictions.  Default to the `<username>` specified in `upn` or `name` if not set. |
| **spn**  aliases: spns  list / elements=string  added in community.windows 1.10.0 | Specifies the service principal name(s) for the account. This parameter sets the ServicePrincipalNames property of the account. The LDAP display name (ldapDisplayName) for this property is servicePrincipalName. |
| **spn_action**  string  added in community.windows 1.10.0 | If `add`, the SPNs are added to the user.  If `remove`, the SPNs are removed from the user.  If `replace`, the defined set of SPN’s overwrite the current set of SPNs.  Choices:   - `"add"` - `"remove"` - `"replace"` ← (default) |
| **state**  string | When `present`, creates or updates the user account.  When `absent`, removes the user account if it exists.  When `query`, retrieves the user account details without making any changes.  Choices:   - `"absent"` - `"present"` ← (default) - `"query"` |
| **state_province**  string | Configures the user’s state or province. |
| **street**  string | Configures the user’s street address. |
| **surname**  aliases: lastname  string | Configures the user’s last name (surname). |
| **update_password**  string | `always` will always update passwords.  `on_create` will only set the password for newly created users.  `when_changed` will only set the password when changed.  Choices:   - `"always"` ← (default) - `"on_create"` - `"when_changed"` |
| **upn**  string | Configures the User Principal Name (UPN) for the account.  This is not required, but is best practice to configure for modern versions of Active Directory.  The format is `<username>@<domain>`. |
| **user_cannot_change_password**  boolean | `yes` will prevent the user from changing their password.  `no` will allow the user to change their password.  Choices:   - `false` - `true` |

## [Notes](win_domain_user_module.md#id3)

> **Note:**
>
> - Works with Windows 2012R2 and newer.
> - If running on a server that is not a Domain Controller, credential delegation through CredSSP or Kerberos with delegation must be used or the *domain_username*, *domain_password* must be set.
> - Note that some individuals have confirmed successful operation on Windows 2008R2 servers with AD and AD Web Services enabled, but this has not received the same degree of testing as Windows 2012R2.

## [See Also](win_domain_user_module.md#id4)

> **See also:**
>
> [ansible.windows.win_domain](../../ansible/windows/win_domain_module.md#ansible-collections-ansible-windows-win-domain-module)
> :   Ensures the existence of a Windows domain.
>
> [ansible.windows.win_domain_controller](../../ansible/windows/win_domain_controller_module.md#ansible-collections-ansible-windows-win-domain-controller-module)
> :   Manage domain controller/member server state for a Windows host.
>
> [community.windows.win_domain_computer](win_domain_computer_module.md#ansible-collections-community-windows-win-domain-computer-module)
> :   Manage computers in Active Directory.
>
> [community.windows.win_domain_group](win_domain_group_module.md#ansible-collections-community-windows-win-domain-group-module)
> :   Creates, modifies or removes domain groups.
>
> [ansible.windows.win_domain_membership](../../ansible/windows/win_domain_membership_module.md#ansible-collections-ansible-windows-win-domain-membership-module)
> :   Manage domain/workgroup membership for a Windows host.
>
> [ansible.windows.win_user](../../ansible/windows/win_user_module.md#ansible-collections-ansible-windows-win-user-module)
> :   Manages local Windows user accounts.
>
> [community.windows.win_user_profile](win_user_profile_module.md#ansible-collections-community-windows-win-user-profile-module)
> :   Manages the Windows user profiles.

## [Examples](win_domain_user_module.md#id5)

```yaml+jinja
- name: Ensure user bob is present with address information
  community.windows.win_domain_user:
    name: bob
    firstname: Bob
    surname: Smith
    company: BobCo
    password: B0bP4ssw0rd
    state: present
    groups:
      - Domain Admins
    street: 123 4th St.
    city: Sometown
    state_province: IN
    postal_code: 12345
    country: US
    attributes:
      telephoneNumber: 555-123456

- name: Ensure user bob is created and use custom credentials to create the user
  community.windows.win_domain_user:
    name: bob
    firstname: Bob
    surname: Smith
    password: B0bP4ssw0rd
    state: present
    domain_username: DOMAIN\admin-account
    domain_password: SomePas2w0rd
    domain_server: domain@DOMAIN.COM

- name: Ensure user bob is present in OU ou=test,dc=domain,dc=local
  community.windows.win_domain_user:
    name: bob
    password: B0bP4ssw0rd
    state: present
    path: ou=test,dc=domain,dc=local
    groups:
      - Domain Admins

- name: Ensure user bob is absent
  community.windows.win_domain_user:
    name: bob
    state: absent

- name: Ensure user has spn's defined
  community.windows.win_domain_user:
    name: liz.kenyon
    spn:
      - MSSQLSvc/us99db-svr95:1433
      - MSSQLSvc/us99db-svr95.vmware.com:1433

- name: Ensure user has spn added
  community.windows.win_domain_user:
    name: liz.kenyon
    spn_action: add
    spn:
      - MSSQLSvc/us99db-svr95:2433

- name: Ensure user is created with delegates and spn's defined
  community.windows.win_domain_user:
    name: shmemmmy
    password: The3rubberducki33!
    state: present
    groups:
      - Domain Admins
      - Enterprise Admins
    delegates:
      - CN=shenetworks,CN=Users,DC=ansible,DC=test
      - CN=mk.ai,CN=Users,DC=ansible,DC=test
      - CN=jessiedotjs,CN=Users,DC=ansible,DC=test
    spn:
      - MSSQLSvc/us99db-svr95:2433
```

## [Return Values](win_domain_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account_locked**  boolean | true if the account is locked  Returned: always  Sample: `false` |
| **changed**  boolean | true if the account changed during execution  Returned: always  Sample: `false` |
| **city**  string | The user city  Returned: always  Sample: `"Indianapolis"` |
| **company**  string | The user company  Returned: always  Sample: `"RedHat"` |
| **country**  string | The user country  Returned: always  Sample: `"US"` |
| **created**  boolean | Whether a user was created  Returned: always  Sample: `true` |
| **delegates**  list / elements=string  added in community.windows 1.10.0 | Principals allowed to delegate  Returned: always  Sample: `["CN=svc.tech.unicorn,CN=Users,DC=ansible,DC=test", "CN=geoff,CN=Users,DC=ansible,DC=test"]` |
| **description**  string | A description of the account  Returned: always  Sample: `"Server Administrator"` |
| **distinguished_name**  string | DN of the user account  Returned: always  Sample: `"CN=nick,OU=test,DC=domain,DC=local"` |
| **email**  string | The user email address  Returned: always  Sample: `"nick@domain.local"` |
| **enabled**  string | true if the account is enabled and false if disabled  Returned: always  Sample: `"True"` |
| **firstname**  string | The user first name  Returned: always  Sample: `"Nick"` |
| **groups**  list / elements=string | AD Groups to which the account belongs  Returned: always  Sample: `["Domain Admins", "Domain Users"]` |
| **msg**  string | Summary message of whether the user is present or absent  Returned: always  Sample: `"User nick is present"` |
| **name**  string | The username on the account  Returned: always  Sample: `"nick"` |
| **password_expired**  boolean | true if the account password has expired  Returned: always  Sample: `false` |
| **password_updated**  boolean | true if the password changed during this execution  Returned: always  Sample: `true` |
| **postal_code**  string | The user postal code  Returned: always  Sample: `"46033"` |
| **sam_account_name**  string  added in community.windows 1.7.0 | The SAM Account Name of the account  Returned: always  Sample: `"nick"` |
| **sid**  string | The SID of the account  Returned: always  Sample: `"S-1-5-21-2752426336-228313920-2202711348-1175"` |
| **spn**  list / elements=string  added in community.windows 1.10.0 | The service principal names  Returned: always  Sample: `["HTTPSvc/ws1intel-svc1", "HTTPSvc/ws1intel-svc1.vmware.com"]` |
| **state**  string | The state of the user account  Returned: always  Sample: `"present"` |
| **state_province**  string | The user state or province  Returned: always  Sample: `"IN"` |
| **street**  string | The user street address  Returned: always  Sample: `"123 4th St."` |
| **surname**  string | The user last name  Returned: always  Sample: `"Doe"` |
| **upn**  string | The User Principal Name of the account  Returned: always  Sample: `"nick@domain.local"` |
| **user_cannot_change_password**  string | true if the user is not allowed to change password  Returned: always  Sample: `"False"` |

### Authors

- Nick Chandler (@nwchandler)
- Joe Zollo (@zollo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
