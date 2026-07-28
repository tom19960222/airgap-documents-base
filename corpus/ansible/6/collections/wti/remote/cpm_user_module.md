---
collection: ansible
version: "6"
title: "wti.remote.cpm_user module – Get various status and parameters from WTI OOB and PDU devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/wti/remote/cpm_user_module.html
fetched_at: 2026-07-28T00:23:59+00:00
---
# wti.remote.cpm_user module – Get various status and parameters from WTI OOB and PDU devices

> **Note:**
>
> This module is part of the [wti.remote collection](https://galaxy.ansible.com/wti/remote) (version 1.0.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install wti.remote`.
>
> To use it in a playbook, specify: `wti.remote.cpm_user`.

New in wti.remote 2.7.0

- [Synopsis](cpm_user_module.md#synopsis)
- [Parameters](cpm_user_module.md#parameters)
- [Examples](cpm_user_module.md#examples)
- [Return Values](cpm_user_module.md#return-values)

## [Synopsis](cpm_user_module.md#id1)

- Get/Add/Edit Delete Users from WTI OOB and PDU devices

## [Parameters](cpm_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cpm_action**  string / required | This is the Action to send the module.  Choices:   - `"getuser"` - `"adduser"` - `"edituser"` - `"deleteuser"` |
| **cpm_password**  string / required | This is the Basic Authentication Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Basic Authentication Username of the WTI device to send the module. |
| **use_https**  boolean | Designates to use an https connection or http connection.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  Choices:   - `false` ← (default) - `true` |
| **user_accessapi**  integer | If the user has access to the WTI device via RESTful APIs  0 No , 1 Yes  Choices:   - `0` - `1` |
| **user_accesslevel**  integer | This is the access level that needs to be create/modified/deleted  0 View, 1 User, 2 SuperUser, 3 Administrator  Choices:   - `0` - `1` - `2` - `3` |
| **user_accessmonitor**  integer | If the user has ability to monitor connection sessions  0 No , 1 Yes  Choices:   - `0` - `1` |
| **user_accessoutbound**  integer | If the user has ability to initiate Outbound connection  0 No , 1 Yes  Choices:   - `0` - `1` |
| **user_accessserial**  integer | If the user has access to the WTI device via Serial ports  0 No , 1 Yes  Choices:   - `0` - `1` |
| **user_accessssh**  integer | If the user has access to the WTI device via SSH  0 No , 1 Yes  Choices:   - `0` - `1` |
| **user_accessweb**  integer | If the user has access to the WTI device via Web  0 No , 1 Yes  Choices:   - `0` - `1` |
| **user_callbackphone**  string | This is the Call Back phone number used for POTS modem connections |
| **user_groupaccess**  string | If AccessLevel is lower than Administrator, which Groups the user has access |
| **user_name**  string / required | This is the User Name that needs to be create/modified/deleted |
| **user_pass**  string | This is the User Password that needs to be create/modified/deleted  If the user is being Created this parameter is required |
| **user_plugaccess**  string | If AccessLevel is lower than Administrator, which plugs the user has access |
| **user_portaccess**  string | If AccessLevel is lower than Administrator, which ports the user has access |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](cpm_user_module.md#id3)

```yaml+jinja
# Get User Parameters
- name: Get the User Parameters for the given user of a WTI device
  cpm_user:
    cpm_action: "getuser"
    cpm_url: "rest.wti.com"
    cpm_username: "restuser"
    cpm_password: "restfuluserpass12"
    use_https: true
    validate_certs: true
    user_name: "usernumberone"

# Create User
- name: Create a User on a given WTI device
  cpm_user:
    cpm_action: "adduser"
    cpm_url: "rest.wti.com"
    cpm_username: "restuser"
    cpm_password: "restfuluserpass12"
    use_https: true
    validate_certs: false
    user_name: "usernumberone"
    user_pass: "complicatedpassword"
    user_accesslevel: 2
    user_accessssh: 1
    user_accessserial: 1
    user_accessweb: 0
    user_accessapi: 1
    user_accessmonitor: 0
    user_accessoutbound: 0
    user_portaccess: "10011111"
    user_plugaccess: "00000111"
    user_groupaccess: "00000000"

# Edit User
- name: Edit a User on a given WTI device
  cpm_user:
    cpm_action: "edituser"
    cpm_url: "rest.wti.com"
    cpm_username: "restuser"
    cpm_password: "restfuluserpass12"
    use_https: true
    validate_certs: false
    user_name: "usernumberone"
    user_pass: "newpasswordcomplicatedpassword"

# Delete User
- name: Delete a User from a given WTI device
  cpm_user:
    cpm_action: "deleteuser"
    cpm_url: "rest.wti.com"
    cpm_username: "restuser"
    cpm_password: "restfuluserpass12"
    use_https: true
    validate_certs: true
    user_name: "usernumberone"
```

## [Return Values](cpm_user_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  string | The output JSON returned from the commands sent  Returned: always |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

### Collection links

[Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
[Homepage](https://www.wti.com)
[Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
