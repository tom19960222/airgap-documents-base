---
collection: ansible
version: "8"
title: "microsoft.ad.user module – Manage Active Directory users"
source_url: https://docs.ansible.com/projects/ansible/8/collections/microsoft/ad/user_module.html
fetched_at: 2026-07-28T02:40:55+00:00
---
# microsoft.ad.user module – Manage Active Directory users

> **Note:**
>
> This module is part of the [microsoft.ad collection](https://galaxy.ansible.com/ui/repo/published/microsoft/ad/) (version 1.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install microsoft.ad`.
> You need further requirements to be able to use this module,
> see [Requirements](user_module.md#ansible-collections-microsoft-ad-user-module-requirements) for details.
>
> To use it in a playbook, specify: `microsoft.ad.user`.

- [Synopsis](user_module.md#synopsis)
- [Requirements](user_module.md#requirements)
- [Parameters](user_module.md#parameters)
- [Attributes](user_module.md#attributes)
- [Notes](user_module.md#notes)
- [See Also](user_module.md#see-also)
- [Examples](user_module.md#examples)
- [Return Values](user_module.md#return-values)

## [Synopsis](user_module.md#id1)

- Manages Active Directory users and their attributes.

## [Requirements](user_module.md#id2)

The below requirements are needed on the host that executes this module.

- `ActiveDirectory` PowerShell module

## [Parameters](user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_locked**  boolean | `no` will unlock the user account if locked.  Note that there is not a way to lock an account as an administrator.  Accounts are locked due to user actions; as an admin, you may only unlock a locked account.  If you wish to administratively disable an account, set *enabled* to `no`.  **Choices:**   - `false` - `true` |
| **attributes**  dictionary | The attributes to either add, remove, or set on the AD object.  The value of each attribute option should be a dictionary where the key is the LDAP attribute, e.g. `firstName`, `comment` and the value is the value, or list of values, to set for that attribute.  The attribute value(s) can either be the raw string, integer, or bool value to add, remove, or set on the attribute in question.  The value can also be a dictionary with the *type* key set to `bytes`, `date_time`, `security_descriptor`, or `raw` and the value for this entry under the *value* key.  The `bytes` type has a value that is a base64 encoded string of the raw bytes to set.  The `date_time` type has a value that is the ISO 8601 DateTime string of the DateTime to set. The DateTime will be set as the Microsoft FILETIME integer value which is the number of 100 nanoseconds since 1601-01-01 in UTC.  The `security_descriptor` type has a value that is the Security Descriptor SDDL string used for the `nTSecurityDescriptor` attribute.  The `raw` type is the int, string, or boolean value to set.  String attribute values are compared using a case sensitive match on the AD object being managed.  See [LDAP attributes help](docsite/guide_attributes.md#ansible-collections-microsoft-ad-docsite-guide-attributes) for more information.  **Default:** `{}` |
| **add**  dictionary | A dictionary of all the attributes and their value(s) to add to the AD object being managed if they are not already present.  This is used for attributes that can contain multiple values, if the attribute only allows a single value, use *set* instead.  **Default:** `{}` |
| **remove**  dictionary | A dictionary of all the attributes and their value(s) to remove from the AD object being managed if they are present.  This is used for attributes that can contain multiple values, if the attribute only allows a single value, use *set* instead.  **Default:** `{}` |
| **set**  dictionary | A dictionary of all attributes and their value(s) to set on the AD object being managed.  This will replace any existing values if they do not match the ones being requested.  The order of attribute values are not checked only, only that the values requested are the only values on the object attribute.  Set this to null or an empty list to clear any values for the attribute.  **Default:** `{}` |
| **city**  string | Configures the user’s city.  This is the value set on the `l` LDAP attribute. |
| **company**  string | Configures the user’s company name.  This is the value set on the `company` LDAP attribute. |
| **country**  string | Configures the user’s country code.  Note that this is a two-character ISO 3166 code.  This is the value set on the `c` LDAP attribute. |
| **delegates**  aliases: principals_allowed_to_delegate  dictionary | The principal objects that the current AD object can trust for delegation to either add, remove or set.  The values for each sub option must be specified as a distinguished name `CN=shenetworks,CN=Users,DC=ansible,DC=test`  This is the value set on the `msDS-AllowedToActOnBehalfOfOtherIdentity` LDAP attribute.  This is a highly sensitive attribute as it allows the principals specified to impersonate any account when authenticating with the AD computer object being managed.  To clear all principals, use *set* with an empty list.  See [Setting list option values](docsite/guide_list_values.md#ansible-collections-microsoft-ad-docsite-guide-list-values) for more information on how to add/remove/set list options. |
| **add**  list / elements=string | The AD objects by their `DistinguishedName` to add as a principal allowed to delegate.  Any existing principals not specified by *add* will be untouched unless specified by *remove* or not in *set*. |
| **remove**  list / elements=string | The AD objects by their `DistinguishedName` to remove as a principal allowed to delegate.  Any existing principals not specified by *remove* will be untouched unless *set* is defined. |
| **set**  list / elements=string | The AD objects by their `DistinguishedName` to set as the only principals allowed to delegate.  This will remove any existing principals if not specified in this list.  Specify an empty list to remove all principals allowed to delegate. |
| **description**  string | The description of the AD object to set.  This is the value set on the `description` LDAP attribute. |
| **display_name**  string | The display name of the AD object to set.  This is the value of the `displayName` LDAP attribute. |
| **domain_password**  string | The password for *domain_username*. |
| **domain_server**  string | Specified the Active Directory Domain Services instance to connect to.  Can be in the form of an FQDN or NetBIOS name.  If not specified then the value is based on the default domain of the computer running PowerShell. |
| **domain_username**  string | The username to use when interacting with AD.  If this is not set then the user that is used for authentication will be the connection user.  Ansible will be unable to use the connection user unless auth is Kerberos with credential delegation or CredSSP, or become is used on the task. |
| **email**  string | Configures the user’s email address.  This is a record in AD and does not do anything to configure any email servers or systems.  This is the value set on the `mail` LDAP attribute. |
| **enabled**  boolean | `yes` will enable the user account.  `no` will disable the account.  The default when creating a new is `yes` if *password* is specified. If no *password* is specified then the user will not be enabled.  **Choices:**   - `false` - `true` |
| **firstname**  string | Configures the user’s first name (given name).  This is the value set on the `givenName` LDAP attribute. |
| **groups**  dictionary | Specifies the group membership the user is added, removed, or set to.  To clear all group memberships, use *set* with an empty list.  Note that users cannot be removed from their principal group (for example, “Domain Users”). Attempting to do so will display a warning.  See [Setting list option values](docsite/guide_list_values.md#ansible-collections-microsoft-ad-docsite-guide-list-values) for more information on how to add/remove/set list options. |
| **add**  list / elements=string | The groups to add the user to. |
| **missing_behaviour**  string | Controls what happens when a group specified by `groups` is an invalid group name.  `fail` is the default and will return an error any groups do not exist.  `ignore` will ignore any groups that does not exist.  `warn` will display a warning for any groups that do not exist but will continue without failing.  **Choices:**   - `"fail"` ← (default) - `"ignore"` - `"warn"` |
| **remove**  list / elements=string | The groups to remove the user from. |
| **set**  list / elements=string | The only groups the user is a member of.  This will clear out any existing groups if not in the specified list.  Set to an empty list to clear all group membership of the user. |
| **identity**  string | The identity of the AD object used to find the AD object to manage.  Must be specified if *name* is not set, when trying to rename the object with a new *name*, or when trying to move the object into a different *path*.  The identity can be in the form of a GUID representing the `objectGUID` value, the `userPrincipalName`, `sAMAccountName`, `objectSid`, or `distinguishedName`.  If omitted, the AD object to managed is selected by the `distinguishedName` using the format `CN={{ name }},{{ path }}`. If *path* is not defined, the `defaultNamingContext` is used instead. |
| **name**  string | The `name` of the AD object to manage.  If *identity* is specified, and the name of the object it found does not match this value, the object will be renamed.  This if *identity* must be set to find the object to manage.  This is not always going to be the same as the `sAMAccountName` for user objects. It is strictly the `name` of the object in the path specified. Use *identity* to select an object to manage by `sAMAccountName`. |
| **password**  string | Optionally set the user’s password to this (plain text) value.  To enable an account - *enabled* - a password must already be configured on the account, or you must provide a password here.  Use the *update_password* option to control how a password is checked for idempotency. |
| **password_expired**  boolean | `yes` will require the user to change their password at next login.  `no` will clear the expired password flag.  This is mutually exclusive with *password_never_expires*.  **Choices:**   - `false` - `true` |
| **password_never_expires**  boolean | `yes` will set the password to never expire.  `no` will allow the password to expire.  This is mutually exclusive with *password_expired*.  **Choices:**   - `false` - `true` |
| **path**  string | The path of the OU or the container where the new object should exist in.  If creating a new object, the new object will be created at the path specified. If no path is specified then the `defaultNamingContext` of the domain will be used as the path for most object types.  If managing an existing object found by *identity*, the path of the found object will be moved to the one specified by this option. If no path is specified, the object will not be moved.  The modules [microsoft.ad.computer](computer_module.md#ansible-collections-microsoft-ad-computer-module), [microsoft.ad.user](user_module.md#ansible-collections-microsoft-ad-user-module), and [microsoft.ad.group](group_module.md#ansible-collections-microsoft-ad-group-module) have their own default path that is configured on the Active Directory domain controller.  This can be set to `microsoft.ad.default_path` which will equal the default value used when creating a new object. |
| **postal_code**  string | Configures the user’s postal code / zip code.  This is the value set on the `postalcode` LDAP attribute. |
| **protect_from_deletion**  boolean | Marks the object as protected from accidental deletion.  This applies a deny access right from deleting the object normally and the protection needs to be removed before the object can be deleted through the GUI or any other tool outside Ansible.  Using *state=absent* will still delete the AD object even if it is marked as protected from deletion.  **Choices:**   - `false` - `true` |
| **sam_account_name**  string | The `sAMAccountName` value to set for the user.  If omitted, the *name* value is used when creating a new user. |
| **spn**  aliases: spns  dictionary | Specifies the service principal name(s) for the account to add, remove or set.  This is the value set on the `servicePrincipalName` LDAP attribute.  To clear all service principal names, use *set* with an empty list.  See [Setting list option values](docsite/guide_list_values.md#ansible-collections-microsoft-ad-docsite-guide-list-values) for more information on how to add/remove/set list options. |
| **add**  list / elements=string | The SPNs to add to `servicePrincipalName`. |
| **remove**  list / elements=string | The SPNs to remove from `servicePrincipalName`. |
| **set**  list / elements=string | The SPNs to set as the only values in `servicePrincipalName`.  This will clear out any existing SPNs if not in the specified list.  Set to an empty list to clear all SPNs on the AD object. |
| **state**  string | Set to `present` to ensure the AD object exists.  Set to `absent` to remove the AD object if it exists.  The option *name* must be set when *state=present*.  Using `absent` will recursively remove the AD object and any child objects if it’s a container. It will also remove the AD object even if the object is marked as protected from accidental deletion.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **state_province**  string | Configures the user’s state.  This is the value set on the `state` LDAP attribute. |
| **street**  string | Configures the user’s street address.  This is the value set on the `streetaddress` LDAP attribute. |
| **surname**  aliases: lastname  string | Configures the user’s last name (surname).  This is the value set on the `sn` LDAP attribute. |
| **update_password**  string | `always` will always update passwords.  `on_create` will only set the password for newly created users.  `when_changed` will only set the password when changed.  Using `when_changed` will not work if the account is not enabled or is expired.  **Choices:**   - `"always"` ← (default) - `"on_create"` - `"when_changed"` |
| **upn**  string | Configures the User Principal Name (UPN) for the account.  This is not required, but is best practice to configure for modern versions of Active Directory.  The format is `<username>@<domain>`.  This is the value set on the `userPrincipalName` LDAP attribute. |
| **user_cannot_change_password**  boolean | `yes` will prevent the user from changing their password.  `no` will allow the user to change their password.  **Choices:**   - `false` - `true` |

## [Attributes](user_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **windows** | Target OS/families that can be operated against |

## [Notes](user_module.md#id5)

> **Note:**
>
> - See [win_domain_user migration](docsite/guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain-user) for help on migrating from [community.windows.win_domain_user](../../community/windows/win_domain_user_module.md#ansible-collections-community-windows-win-domain-user-module) to this module.
> - Some LDAP attributes can have only a single value set while others can have multiple. Some attributes are also read only and cannot be changed. It is recommended to look at the schema metadata for an attribute where `System-Only` are read only values and `Is-Single-Value` are attributes with only 1 value.
> - Attempting to set multiple values to a `Is-Single-Value` attribute results in undefined behaviour.
> - If running on a server that is not a Domain Controller, credential delegation through CredSSP or Kerberos with delegation must be used or the *domain_username*, *domain_password* must be set.

## [See Also](user_module.md#id6)

> **See also:**
>
> [microsoft.ad.domain](domain_module.md#ansible-collections-microsoft-ad-domain-module)
> :   Ensures the existence of a Windows domain.
>
> [microsoft.ad.domain_controller](domain_controller_module.md#ansible-collections-microsoft-ad-domain-controller-module)
> :   Manage domain controller/member server state for a Windows host.
>
> [microsoft.ad.group](group_module.md#ansible-collections-microsoft-ad-group-module)
> :   Manage Active Directory group objects.
>
> [microsoft.ad.object](object_module.md#ansible-collections-microsoft-ad-object-module)
> :   Manage Active Directory objects.
>
> [microsoft.ad.object_info](object_info_module.md#ansible-collections-microsoft-ad-object-info-module)
> :   Gather information an Active Directory object.
>
> [microsoft.ad.computer](computer_module.md#ansible-collections-microsoft-ad-computer-module)
> :   Manage Active Directory computer objects.
>
> [Migration guide](docsite/guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain-user)
> :   This module replaces `community.windows.win_domain_user`. See the migration guide for details.
>
> [community.windows.win_domain_user](../../community/windows/win_domain_user_module.md#ansible-collections-community-windows-win-domain-user-module)
> :   Manages Windows Active Directory user accounts.

## [Examples](user_module.md#id7)

```yaml+jinja
- name: Ensure user bob is present with address information
  microsoft.ad.user:
    name: bob
    firstname: Bob
    surname: Smith
    company: BobCo
    password: B0bP4ssw0rd
    state: present
    groups:
      set:
      - Domain Admins
    street: 123 4th St.
    city: Sometown
    state_province: IN
    postal_code: 12345
    country: US
    attributes:
      set:
        telephoneNumber: 555-123456

- name: Ensure user bob is created and use custom credentials to create the user
  microsoft.ad.user:
    name: bob
    firstname: Bob
    surname: Smith
    password: B0bP4ssw0rd
    state: present
    domain_username: DOMAIN\admin-account
    domain_password: SomePas2w0rd
    domain_server: domain@DOMAIN.COM

- name: Ensure user bob is present in OU ou=test,dc=domain,dc=local
  microsoft.ad.user:
    name: bob
    password: B0bP4ssw0rd
    state: present
    path: ou=test,dc=domain,dc=local
    groups:
      set:
      - Domain Admins
      - Domain Users

- name: Ensure user bob is absent
  microsoft.ad.user:
    name: bob
    state: absent

- name: Ensure user has only these spn's defined
  microsoft.ad.user:
    name: liz.kenyon
    spn:
      set:
      - MSSQLSvc/us99db-svr95:1433
      - MSSQLSvc/us99db-svr95.vmware.com:1433

- name: Ensure user has spn added
  microsoft.ad.user:
    name: liz.kenyon
    spn:
      add:
      - MSSQLSvc/us99db-svr95:2433

- name: Ensure user is created with delegates and spn's defined
  microsoft.ad.user:
    name: shmemmmy
    password: The3rubberducki33!
    state: present
    groups:
      set:
      - Domain Admins
      - Domain Users
      - Enterprise Admins
    delegates:
      set:
      - CN=shenetworks,CN=Users,DC=ansible,DC=test
      - CN=mk.ai,CN=Users,DC=ansible,DC=test
      - CN=jessiedotjs,CN=Users,DC=ansible,DC=test
    spn:
      set:
      - MSSQLSvc/us99db-svr95:2433

# The name option is the name of the AD object as seen in dsa.msc and not the
# sAMAccountName. For example, this will change the sAMAccountName of the user
# CN=existing_user,CN=Users,DC=domain,DC=com to 'new_sam_name'.
# E.g. This will change
- name: Change the user's sAMAccountName
  microsoft.ad.user:
    name: existing_user
    sam_account_name: new_sam_name
    state: present

# This will rename the AD object that is specified by identity to 'new_name'.
# The identity value can be the object's GUID, SecurityIdentifier, or
# sAMAccountName. It is important to use the identity value when renaming or
# moving a user object to ensure the object is moved/renamed rather than a new
# one being created.
- name: Rename user LDAP name
  microsoft.ad.user:
    name: new_name
    identity: '{{ user_obj.object_guid }}'
    state: present

# Like changing the name example above, the identity option is needed to ensure
# the existing user object specified is moved rather than a new one created at
# the path specified.
- name: Move user object to different OU
  microsoft.ad.user:
    name: user
    path: OU=Admins,DC=domain,DC=com
    identity: '{{ user_obj.sid }}'
    state: present
```

## [Return Values](user_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **distinguished_name**  string | The `distinguishedName` of the AD object that was created, removed, or edited.  **Returned:** always  **Sample:** `"CN=TestUser,CN=Users,DC=domain,DC=test"` |
| **object_guid**  string | The `objectGUID` of the AD object that was created, removed, or edited.  If a new object was created in check mode, a GUID of 0s will be returned.  **Returned:** always  **Sample:** `"d84a141f-2b99-4f08-9da0-ed2d26864ba1"` |
| **sid**  string | The Security Identifier (SID) of the account managed.  If a new user was created in check mode, the SID will be `S-1-5-0000`.  **Returned:** always  **Sample:** `"S-1-5-21-4151808797-3430561092-2843464588-1104"` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/microsoft.ad/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/microsoft.ad)
- [Report an issue](https://github.com/ansible-collections/microsoft.ad/issues/new/choose)
- [Communication](index.md#communication-for-microsoft-ad)
