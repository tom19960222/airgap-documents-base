---
collection: ansible
version: "6"
title: "community.general.homectl module – Manage user accounts with systemd-homed"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/homectl_module.html
fetched_at: 2026-07-27T17:09:20+00:00
---
# community.general.homectl module – Manage user accounts with systemd-homed

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.homectl`.

New in community.general 4.4.0

- [Synopsis](homectl_module.md#synopsis)
- [Parameters](homectl_module.md#parameters)
- [Examples](homectl_module.md#examples)
- [Return Values](homectl_module.md#return-values)

## [Synopsis](homectl_module.md#id1)

- Manages a user’s home directory managed by systemd-homed.

## [Parameters](homectl_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **disksize**  string | The intended home directory disk space.  Human readable value such as `10G`, `10M`, or `10B`. |
| **email**  string | The email address of the user. |
| **environment**  aliases: setenv  string | String separated by comma each containing an environment variable and its value to set for the user’s login session, in a format compatible with ``putenv()``.  Any environment variable listed here is automatically set by pam_systemd for all login sessions of the user. |
| **gid**  integer | Sets the gid of the user.  If using *uid* homed requires the value to be the same.  Only used when a user is first created. |
| **homedir**  path | Path to use as home directory for the user.  This is the directory the user’s home directory is mounted to while the user is logged in.  This is not where the user’s data is actually stored, see *imagepath* for that.  Only used when a user is first created. |
| **iconname**  string | The name of an icon picked by the user, for example for the purpose of an avatar.  Should follow the semantics defined in the Icon Naming Specification.  See <https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html> for specifics. |
| **imagepath**  path | Path to place the user’s home directory.  See [https://www.freedesktop.org/software/systemd/man/homectl.html#–image-path%3DPATH](https://www.freedesktop.org/software/systemd/man/homectl.html#--image-path%3DPATH) for more information.  Only used when a user is first created. |
| **language**  string | The preferred language/locale for the user.  This should be in a format compatible with the `$LANG` environment variable. |
| **location**  string | A free-form location string describing the location of the user. |
| **locked**  boolean | Whether the user account should be locked or not.  Choices:   - `false` - `true` |
| **memberof**  aliases: groups  string | String separated by comma each indicating a UNIX group this user shall be a member of.  Groups the user should be a member of should be supplied as comma separated list. |
| **mountopts**  string | String separated by comma each indicating mount options for a users home directory.  Valid options are `nosuid`, `nodev` or `noexec`.  Homed by default uses `nodev` and `nosuid` while `noexec` is off. |
| **name**  aliases: user, username  string / required | The user name to create, remove, or update. |
| **notafter**  integer | A time since the UNIX epoch after which the record should be considered invalid for the purpose of logging in. |
| **notbefore**  integer | A time since the UNIX epoch before which the record should be considered invalid for the purpose of logging in. |
| **password**  string | Set the user’s password to this.  Homed requires this value to be in cleartext on user creation and updating a user.  The module takes the password and generates a password hash in SHA-512 with 10000 rounds of salt generation using crypt.  See <https://systemd.io/USER_RECORD/>.  This is required for *state=present*. When an existing user is updated this is checked against the stored hash in homed. |
| **passwordhint**  string | Password hint for the given user. |
| **realm**  string | The ‘realm’ a user is defined in. |
| **realname**  aliases: comment  string | The user’s real (‘human’) name.  This can also be used to add a comment to maintain compatibility with `useradd`. |
| **resize**  boolean | When used with *disksize* this will attempt to resize the home directory immediately.  Choices:   - `false` ← (default) - `true` |
| **shell**  string | Shell binary to use for terminal logins of given user.  If not specified homed by default uses `/bin/bash`. |
| **skeleton**  aliases: skel  path | The absolute path to the skeleton directory to populate a new home directory from.  This is only used when a home directory is first created.  If not specified homed by default uses `/etc/skel`. |
| **sshkeys**  string | String separated by comma each listing a SSH public key that is authorized to access the account.  The keys should follow the same format as the lines in a traditional `~/.ssh/authorized_key` file. |
| **state**  string | The operation to take on the user.  Choices:   - `"absent"` - `"present"` ← (default) |
| **storage**  string | Indicates the storage mechanism for the user’s home directory.  If the storage type is not specified, ``homed.conf(5)`` defines which default storage to use.  Only used when a user is first created.  Choices:   - `"classic"` - `"luks"` - `"directory"` - `"subvolume"` - `"fscrypt"` - `"cifs"` |
| **timezone**  string | Preferred timezone to use for the user.  Should be a tzdata compatible location string such as `America/New_York`. |
| **uid**  integer | Sets the UID of the user.  If using *gid* homed requires the value to be the same.  Only used when a user is first created. |
| **umask**  integer | Sets the umask for the user’s login sessions  Value from `0000` to `0777`. |

## [Examples](homectl_module.md#id3)

```yaml+jinja
- name: Add the user 'james'
  community.general.homectl:
    name: johnd
    password: myreallysecurepassword1!
    state: present

- name: Add the user 'alice' with a zsh shell, uid of 1000, and gid of 2000
  community.general.homectl:
    name: alice
    password: myreallysecurepassword1!
    state: present
    shell: /bin/zsh
    uid: 1000
    gid: 1000

- name: Modify an existing user 'frank' to have 10G of diskspace and resize usage now
  community.general.homectl:
    name: frank
    password: myreallysecurepassword1!
    state: present
    disksize: 10G
    resize: true

- name: Remove an existing user 'janet'
  community.general.homectl:
    name: janet
    state: absent
```

## [Return Values](homectl_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | A json dictionary returned from `homectl inspect -j`.  Returned: success  Sample: `{"data": {"binding": {"e9ed2a5b0033427286b228e97c1e8343": {"fileSystemType": "btrfs", "fileSystemUuid": "7bd59491-2812-4642-a492-220c3f0c6c0b", "gid": 60268, "imagePath": "/home/james.home", "luksCipher": "aes", "luksCipherMode": "xts-plain64", "luksUuid": "7f05825a-2c38-47b4-90e1-f21540a35a81", "luksVolumeKeySize": 32, "partitionUuid": "5a906126-d3c8-4234-b230-8f6e9b427b2f", "storage": "luks", "uid": 60268}}, "diskSize": 3221225472, "disposition": "regular", "lastChangeUSec": 1641941238208691, "lastPasswordChangeUSec": 1641941238208691, "privileged": {"hashedPassword": ["$6$ov9AKni.trf76inT$tTtfSyHgbPTdUsG0CvSSQZXGqFGdHKQ9Pb6e0BTZhDmlgrL/vA5BxrXduBi8u/PCBiYUffGLIkGhApjKMK3bV."]}, "signature": [{"data": "o6zVFbymcmk4YTVaY6KPQK23YCp+VkXdGEeniZeV1pzIbFzoaZBvVLPkNKMoPAQbodY5BYfBtuy41prNL78qAg==", "key": "-----BEGIN PUBLIC KEY----- MCowBQYDK2VwAyEAbs7ELeiEYBxkUQhxZ+5NGyu6J7gTtZtZ5vmIw3jowcY= -----END PUBLIC KEY----- "}], "status": {"e9ed2a5b0033427286b228e97c1e8343": {"diskCeiling": 21845405696, "diskFloor": 268435456, "diskSize": 3221225472, "service": "io.systemd.Home", "signedLocally": true, "state": "inactive"}}, "userName": "james"}}` |

### Authors

- James Livulpi (@jameslivulpi)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
