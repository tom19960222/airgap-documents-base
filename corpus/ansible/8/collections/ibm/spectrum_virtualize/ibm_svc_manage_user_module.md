---
collection: ansible
version: "8"
title: "ibm.spectrum_virtualize.ibm_svc_manage_user module – This module manages user on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/spectrum_virtualize/ibm_svc_manage_user_module.html
fetched_at: 2026-07-28T02:35:04+00:00
---
# ibm.spectrum_virtualize.ibm_svc_manage_user module – This module manages user on IBM Spectrum Virtualize family storage systems

> **Note:**
>
> This module is part of the [ibm.spectrum_virtualize collection](https://galaxy.ansible.com/ui/repo/published/ibm/spectrum_virtualize/) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.spectrum_virtualize`.
>
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_svc_manage_user`.

New in ibm.spectrum_virtualize 1.7.0

- [Synopsis](ibm_svc_manage_user_module.md#synopsis)
- [Parameters](ibm_svc_manage_user_module.md#parameters)
- [Notes](ibm_svc_manage_user_module.md#notes)
- [Examples](ibm_svc_manage_user_module.md#examples)

## [Synopsis](ibm_svc_manage_user_module.md#id1)

- Ansible interface to manage ‘mkuser’, ‘rmuser’, and ‘chuser’ commands.

## [Parameters](ibm_svc_manage_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_type**  string | Specifies whether the user authenticates to the system using a remote authentication service or system authentication methods.  Only supported value is ‘usergrp’.  Required when *state=present*, to create a user.  **Choices:**   - `"usergrp"` |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **forcepasswordchange**  boolean | Specifies that the password is to be changed on next login.  Applies when *state=present*, to modify a user.  **Choices:**   - `false` - `true` |
| **keyfile**  string | Specifies the name of the file containing the Secure Shell (SSH) public key.  Applies when *state=present*. |
| **lock**  boolean | Specifies to lock the account indefinitely. The user cannot log in unless unlocked again with the parameter *unlock*.  Applies when *state=present*, to modify a user.  Parameters *lock* and *unlock* are mutually exclusive.  **Choices:**   - `false` - `true` |
| **log_path**  string | Path of debug log file. |
| **name**  string / required | Specifies the unique username. |
| **nokey**  boolean | Specifies that the user’s SSH key is to be deleted.  Applies when *state=present*, to modify a user.  **Choices:**   - `false` - `true` |
| **nopassword**  boolean | Specifies that the user’s password is to be deleted.  Applies when *state=present*, to modify a user.  **Choices:**   - `false` - `true` |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **state**  string / required | Creates or updates (`present`) or removes (`absent`) a user.  **Choices:**   - `"present"` - `"absent"` |
| **token**  string | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the ibm_svc_auth module. |
| **unlock**  boolean | Specifies to unlock the account so it can be logged in to again.  Applies when *state=present*, to modify a user.  Parameters *lock* and *unlock* are mutually exclusive.  **Choices:**   - `false` - `true` |
| **user_password**  string | Specifies the password associated with the user.  Applies when *state=present*. |
| **usergroup**  string | Specifies the name of the user group with which the local user is to be associated.  Applies when *state=present* and *auth_type=usergrp*. |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_manage_user_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_manage_user_module.md#id4)

```yaml+jinja
- name: Create a user
  ibm.spectrum_virtualize.ibm_svc_manage_user:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    state: present
    name: user-name
    user_password: user-password
    auth_type: usergrp
    usergroup: usergroup-name
- name: Remove a user
  ibm.spectrum_virtualize.ibm_svc_manage_user:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    state: absent
    name: user-name
```

### Authors

- Sreshtant Bohidar(@Sreshtant-Bohidar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
