---
collection: ansible
version: "6"
title: "ansible.builtin.user module – Manage user accounts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/user_module.html
fetched_at: 2026-07-27T16:43:03+00:00
---
# ansible.builtin.user module – Manage user accounts

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `user` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](user_module.md#synopsis)
- [Parameters](user_module.md#parameters)
- [Attributes](user_module.md#attributes)
- [Notes](user_module.md#notes)
- [See Also](user_module.md#see-also)
- [Examples](user_module.md#examples)
- [Return Values](user_module.md#return-values)

## [Synopsis](user_module.md#id1)

- Manage user accounts and user attributes.
- For Windows targets, use the [ansible.windows.win_user](../windows/win_user_module.md#ansible-collections-ansible-windows-win-user-module) module instead.

## [Parameters](user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **append**  boolean | If `yes`, add the user to the groups specified in `groups`.  If `no`, user will only be added to the groups specified in `groups`, removing them from all other groups.  Choices:   - `false` ← (default) - `true` |
| **authorization**  string  added in Ansible 2.8 | Sets the authorization of the user.  Does nothing when used with other platforms.  Can set multiple authorizations using comma separation.  To delete all authorizations, use `authorization=''`.  Currently supported on Illumos/Solaris. |
| **comment**  string | Optionally sets the description (aka *GECOS*) of user account. |
| **create_home**  aliases: createhome  boolean | Unless set to `no`, a home directory will be made for the user when the account is created or if the home directory does not exist.  Changed from `createhome` to `create_home` in Ansible 2.5.  Choices:   - `false` - `true` ← (default) |
| **expires**  float | An expiry time for the user in epoch, it will be ignored on platforms that do not support this.  Currently supported on GNU/Linux, FreeBSD, and DragonFlyBSD.  Since Ansible 2.6 you can remove the expiry time by specifying a negative value. Currently supported on GNU/Linux and FreeBSD. |
| **force**  boolean | This only affects `state=absent`, it forces removal of the user and associated directories on supported platforms.  The behavior is the same as `userdel --force`, check the man page for `userdel` on your system for details and support.  When used with `generate_ssh_key=yes` this forces an existing key to be overwritten.  Choices:   - `false` ← (default) - `true` |
| **generate_ssh_key**  boolean | Whether to generate a SSH key for the user in question.  This will **not** overwrite an existing SSH key unless used with `force=yes`.  Choices:   - `false` ← (default) - `true` |
| **group**  string | Optionally sets the user’s primary group (takes a group name). |
| **groups**  list / elements=string | List of groups user will be added to.  By default, the user is removed from all other groups. Configure `append` to modify this.  When set to an empty string `''`, the user is removed from all groups except the primary group.  Before Ansible 2.3, the only input format allowed was a comma separated string. |
| **hidden**  boolean | macOS only, optionally hide the user from the login window and system preferences.  The default will be `yes` if the *system* option is used.  Choices:   - `false` - `true` |
| **home**  path | Optionally set the user’s home directory. |
| **local**  boolean | Forces the use of “local” command alternatives on platforms that implement it.  This is useful in environments that use centralized authentication when you want to manipulate the local users (in other words, it uses `luseradd` instead of `useradd`).  This will check `/etc/passwd` for an existing account before invoking commands. If the local account database exists somewhere other than `/etc/passwd`, this setting will not work properly.  This requires that the above commands as well as `/etc/passwd` must exist on the target host, otherwise it will be a fatal error.  Choices:   - `false` ← (default) - `true` |
| **login_class**  string | Optionally sets the user’s login class, a feature of most BSD OSs. |
| **move_home**  boolean | If set to `yes` when used with `home:` , attempt to move the user’s old home directory to the specified directory if it isn’t there already and the old home exists.  Choices:   - `false` ← (default) - `true` |
| **name**  aliases: user  string / required | Name of the user to create, remove or modify. |
| **non_unique**  boolean | Optionally when used with the -u option, this option allows to change the user ID to a non-unique value.  Choices:   - `false` ← (default) - `true` |
| **password**  string | Optionally set the user’s password to this crypted value.  On macOS systems, this value has to be cleartext. Beware of security issues.  To create a an account with a locked/disabled password on Linux systems, set this to `'!'` or `'*'`.  To create a an account with a locked/disabled password on OpenBSD, set this to `'*************'`.  See [FAQ entry](https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#how-do-i-generate-encrypted-passwords-for-the-user-module) for details on various ways to generate these password values. |
| **password_expire_max**  integer  added in ansible-core 2.11 | Maximum number of days between password change.  Supported on Linux only. |
| **password_expire_min**  integer  added in ansible-core 2.11 | Minimum number of days between password change.  Supported on Linux only. |
| **password_lock**  boolean | Lock the password (`usermod -L`, `usermod -U`, `pw lock`).  Implementation differs by platform. This option does not always mean the user cannot login using other methods.  This option does not disable the user, only lock the password.  This must be set to `False` in order to unlock a currently locked password. The absence of this parameter will not unlock a password.  Currently supported on Linux, FreeBSD, DragonFlyBSD, NetBSD, OpenBSD.  Choices:   - `false` - `true` |
| **profile**  string  added in Ansible 2.8 | Sets the profile of the user.  Does nothing when used with other platforms.  Can set multiple profiles using comma separation.  To delete all the profiles, use `profile=''`.  Currently supported on Illumos/Solaris. |
| **remove**  boolean | This only affects `state=absent`, it attempts to remove directories associated with the user.  The behavior is the same as `userdel --remove`, check the man page for details and support.  Choices:   - `false` ← (default) - `true` |
| **role**  string  added in Ansible 2.8 | Sets the role of the user.  Does nothing when used with other platforms.  Can set multiple roles using comma separation.  To delete all roles, use `role=''`.  Currently supported on Illumos/Solaris. |
| **seuser**  string | Optionally sets the seuser type (user_u) on selinux enabled systems. |
| **shell**  string | Optionally set the user’s shell.  On macOS, before Ansible 2.5, the default shell for non-system users was `/usr/bin/false`. Since Ansible 2.5, the default shell for non-system users on macOS is `/bin/bash`.  See notes for details on how other operating systems determine the default shell by the underlying tool. |
| **skeleton**  string | Optionally set a home skeleton directory.  Requires `create_home` option! |
| **ssh_key_bits**  integer | Optionally specify number of bits in SSH key to create.  The default value depends on ssh-keygen. |
| **ssh_key_comment**  string | Optionally define the comment for the SSH key.  Default: `"ansible-generated on $HOSTNAME"` |
| **ssh_key_file**  path | Optionally specify the SSH key filename.  If this is a relative filename then it will be relative to the user’s home directory.  This parameter defaults to *.ssh/id_rsa*. |
| **ssh_key_passphrase**  string | Set a passphrase for the SSH key.  If no passphrase is provided, the SSH key will default to having no passphrase. |
| **ssh_key_type**  string | Optionally specify the type of SSH key to generate.  Available SSH key types will depend on implementation present on target host.  Default: `"rsa"` |
| **state**  string | Whether the account should exist or not, taking action if the state is different from what is stated.  Choices:   - `"absent"` - `"present"` ← (default) |
| **system**  boolean | When creating an account `state=present`, setting this to `yes` makes the user a system account.  This setting cannot be changed on existing users.  Choices:   - `false` ← (default) - `true` |
| **uid**  integer | Optionally sets the *UID* of the user. |
| **umask**  string  added in ansible-core 2.12 | Sets the umask of the user.  Does nothing when used with other platforms.  Currently supported on Linux.  Requires `local` is omitted or False. |
| **update_password**  string | `always` will update passwords if they differ.  `on_create` will only set the password for newly created users.  Choices:   - `"always"` ← (default) - `"on_create"` |

## [Attributes](user_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | Platform: posix | Target OS/families that can be operated against |

## [Notes](user_module.md#id4)

> **Note:**
>
> - There are specific requirements per platform on user management utilities. However they generally come pre-installed with the system and Ansible will require they are present at runtime. If they are not, a descriptive error message will be shown.
> - On SunOS platforms, the shadow file is backed up automatically since this module edits it directly. On other platforms, the shadow file is backed up by the underlying tools used by this module.
> - On macOS, this module uses `dscl` to create, modify, and delete accounts. `dseditgroup` is used to modify group membership. Accounts are hidden from the login window by modifying `/Library/Preferences/com.apple.loginwindow.plist`.
> - On FreeBSD, this module uses `pw useradd` and `chpass` to create, `pw usermod` and `chpass` to modify, `pw userdel` remove, `pw lock` to lock, and `pw unlock` to unlock accounts.
> - On all other platforms, this module uses `useradd` to create, `usermod` to modify, and `userdel` to remove accounts.

## [See Also](user_module.md#id5)

> **See also:**
>
> [ansible.posix.authorized_key](../posix/authorized_key_module.md#ansible-collections-ansible-posix-authorized-key-module)
> :   Adds or removes an SSH authorized key.
>
> [ansible.builtin.group](group_module.md#ansible-collections-ansible-builtin-group-module)
> :   Add or remove groups.
>
> [ansible.windows.win_user](../windows/win_user_module.md#ansible-collections-ansible-windows-win-user-module)
> :   Manages local Windows user accounts.

## [Examples](user_module.md#id6)

```yaml+jinja
- name: Add the user 'johnd' with a specific uid and a primary group of 'admin'
  ansible.builtin.user:
    name: johnd
    comment: John Doe
    uid: 1040
    group: admin

- name: Add the user 'james' with a bash shell, appending the group 'admins' and 'developers' to the user's groups
  ansible.builtin.user:
    name: james
    shell: /bin/bash
    groups: admins,developers
    append: yes

- name: Remove the user 'johnd'
  ansible.builtin.user:
    name: johnd
    state: absent
    remove: yes

- name: Create a 2048-bit SSH key for user jsmith in ~jsmith/.ssh/id_rsa
  ansible.builtin.user:
    name: jsmith
    generate_ssh_key: yes
    ssh_key_bits: 2048
    ssh_key_file: .ssh/id_rsa

- name: Added a consultant whose account you want to expire
  ansible.builtin.user:
    name: james18
    shell: /bin/zsh
    groups: developers
    expires: 1422403387

- name: Starting at Ansible 2.6, modify user, remove expiry time
  ansible.builtin.user:
    name: james18
    expires: -1

- name: Set maximum expiration date for password
  ansible.builtin.user:
    name: ram19
    password_expire_max: 10

- name: Set minimum expiration date for password
  ansible.builtin.user:
    name: pushkar15
    password_expire_min: 5
```

## [Return Values](user_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **append**  boolean | Whether or not to append the user to groups.  Returned: When state is `present` and the user exists  Sample: `true` |
| **comment**  string | Comment section from passwd file, usually the user name.  Returned: When user exists  Sample: `"Agent Smith"` |
| **create_home**  boolean | Whether or not to create the home directory.  Returned: When user does not exist and not check mode  Sample: `true` |
| **force**  boolean | Whether or not a user account was forcibly deleted.  Returned: When *state* is `absent` and user exists  Sample: `false` |
| **group**  integer | Primary user group ID  Returned: When user exists  Sample: `1001` |
| **groups**  string | List of groups of which the user is a member.  Returned: When *groups* is not empty and *state* is `present`  Sample: `"chrony,apache"` |
| **home**  string | Path to user’s home directory.  Returned: When *state* is `present`  Sample: `"/home/asmith"` |
| **move_home**  boolean | Whether or not to move an existing home directory.  Returned: When *state* is `present` and user exists  Sample: `false` |
| **name**  string | User account name.  Returned: always  Sample: `"asmith"` |
| **password**  string | Masked value of the password.  Returned: When *state* is `present` and *password* is not empty  Sample: `"NOT_LOGGING_PASSWORD"` |
| **password_expire_max**  integer | Maximum number of days during which a password is valid.  Returned: When user exists  Sample: `20` |
| **password_expire_min**  integer | Minimum number of days between password change  Returned: When user exists  Sample: `20` |
| **remove**  boolean | Whether or not to remove the user account.  Returned: When *state* is `absent` and user exists  Sample: `true` |
| **shell**  string | User login shell.  Returned: When *state* is `present`  Sample: `"/bin/bash"` |
| **ssh_fingerprint**  string | Fingerprint of generated SSH key.  Returned: When *generate_ssh_key* is `True`  Sample: `"2048 SHA256:aYNHYcyVm87Igh0IMEDMbvW0QDlRQfE0aJugp684ko8 ansible-generated on host (RSA)"` |
| **ssh_key_file**  string | Path to generated SSH private key file.  Returned: When *generate_ssh_key* is `True`  Sample: `"/home/asmith/.ssh/id_rsa"` |
| **ssh_public_key**  string | Generated SSH public key file.  Returned: When *generate_ssh_key* is `True`  Sample: `"'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC95opt4SPEC06tOYsJQJIuN23BbLMGmYo8ysVZQc4h2DZE9ugbjWWGS1/pweUGjVstgzMkBEeBCByaEf/RJKNecKRPeGd2Bw9DCj/bn5Z6rGfNENKBmo 618mUJBvdlEgea96QGjOwSB7/gmonduC7gsWDMNcOdSE3wJMTim4lddiBx4RgC9yXsJ6Tkz9BHD73MXPpT5ETnse+A3fw3IGVSjaueVnlUyUmOBf7fzmZbhlFVXf2Zi2rFTXqvbdGHKkzpw1U8eB8xFPP7y d5u1u0e6Acju/8aZ/l17IDFiLke5IzlqIMRTEbDwLNeO84YQKWTm9fODHzhYe0yvxqLiK07 ansible-generated on host'\n"` |
| **stderr**  string | Standard error from running commands.  Returned: When stderr is returned by a command that is run  Sample: `"Group wheels does not exist"` |
| **stdout**  string | Standard output from running commands.  Returned: When standard output is returned by the command that is run |
| **system**  boolean | Whether or not the account is a system account.  Returned: When *system* is passed to the module and the account does not exist  Sample: `true` |
| **uid**  integer | User ID of the user account.  Returned: When *uid* is passed to the module  Sample: `1044` |

### Authors

- Stephen Fromm (@sfromm)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
