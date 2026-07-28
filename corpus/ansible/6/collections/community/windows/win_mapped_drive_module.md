---
collection: ansible
version: "6"
title: "community.windows.win_mapped_drive module – Map network drives for users"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_mapped_drive_module.html
fetched_at: 2026-07-27T17:23:36+00:00
---
# community.windows.win_mapped_drive module – Map network drives for users

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
> To use it in a playbook, specify: `community.windows.win_mapped_drive`.

- [Synopsis](win_mapped_drive_module.md#synopsis)
- [Parameters](win_mapped_drive_module.md#parameters)
- [Notes](win_mapped_drive_module.md#notes)
- [See Also](win_mapped_drive_module.md#see-also)
- [Examples](win_mapped_drive_module.md#examples)

## [Synopsis](win_mapped_drive_module.md#id1)

- Allows you to modify mapped network drives for individual users.
- Also support WebDAV endpoints in the UNC form.

## [Parameters](win_mapped_drive_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **letter**  string / required | The letter of the network path to map to.  This letter must not already be in use with Windows. |
| **password**  string | The password for `username` that is used when testing the initial connection.  This is never saved with a mapped drive, use the [community.windows.win_credential](win_credential_module.md#ansible-collections-community-windows-win-credential-module) module to persist a username and password for a host. |
| **path**  path | The UNC path to map the drive to.  If pointing to a WebDAV location this must still be in a UNC path in the format `\\hostname\path` and not a URL, see examples for more details.  To specify a `https` WebDAV path, add `@SSL` after the hostname. To specify a custom WebDAV port add `@<port num>` after the `@SSL` or hostname portion of the UNC path, e.g. `\\server@SSL@1234` or `\\server@1234`.  This is required if `state=present`.  If `state=absent` and *path* is not set, the module will delete the mapped drive regardless of the target.  If `state=absent` and the *path* is set, the module will throw an error if path does not match the target of the mapped drive. |
| **state**  string | If `present` will ensure the mapped drive exists.  If `absent` will ensure the mapped drive does not exist.  Choices:   - `"absent"` - `"present"` ← (default) |
| **username**  string | The username that is used when testing the initial connection.  This is never saved with a mapped drive, the [community.windows.win_credential](win_credential_module.md#ansible-collections-community-windows-win-credential-module) module to persist a username and password for a host.  This is required if the mapped drive requires authentication with custom credentials and become, or CredSSP cannot be used.  If become or CredSSP is used, any credentials saved with [community.windows.win_credential](win_credential_module.md#ansible-collections-community-windows-win-credential-module) will automatically be used instead. |

## [Notes](win_mapped_drive_module.md#id3)

> **Note:**
>
> - You cannot use this module to access a mapped drive in another Ansible task, drives mapped with this module are only accessible when logging in interactively with the user through the console or RDP.
> - It is recommend to run this module with become or CredSSP when the remote path requires authentication.
> - When using become or CredSSP, the task will have access to any local credentials stored in the user’s vault.
> - If become or CredSSP is not available, the *username* and *password* options can be used for the initial authentication but these are not persisted.
> - WebDAV paths must have the WebDAV client feature installed for this module to map those paths. This is installed by default on desktop Windows editions but Windows Server hosts need to install the `WebDAV-Redirector` feature using [ansible.windows.win_feature](../../ansible/windows/win_feature_module.md#ansible-collections-ansible-windows-win-feature-module).

## [See Also](win_mapped_drive_module.md#id4)

> **See also:**
>
> [community.windows.win_credential](win_credential_module.md#ansible-collections-community-windows-win-credential-module)
> :   Manages Windows Credentials in the Credential Manager.

## [Examples](win_mapped_drive_module.md#id5)

```yaml+jinja
- name: Create a mapped drive under Z
  community.windows.win_mapped_drive:
    letter: Z
    path: \\domain\appdata\accounting

- name: Delete any mapped drives under Z
  community.windows.win_mapped_drive:
    letter: Z
    state: absent

- name: Only delete the mapped drive Z if the paths match (error is thrown otherwise)
  community.windows.win_mapped_drive:
    letter: Z
    path: \\domain\appdata\accounting
    state: absent

- name: Create mapped drive with credentials and save the username and password
  block:
  - name: Save the network credentials required for the mapped drive
    community.windows.win_credential:
      name: server
      type: domain_password
      username: username@DOMAIN
      secret: Password01
      state: present

  - name: Create a mapped drive that requires authentication
    community.windows.win_mapped_drive:
      letter: M
      path: \\SERVER\C$
      state: present
  vars:
    # become is required to save and retrieve the credentials in the tasks
    ansible_become: yes
    ansible_become_method: runas
    ansible_become_user: '{{ ansible_user }}'
    ansible_become_pass: '{{ ansible_password }}'

- name: Create mapped drive with credentials that do not persist on the next logon
  community.windows.win_mapped_drive:
    letter: M
    path: \\SERVER\C$
    state: present
    username: '{{ ansible_user }}'
    password: '{{ ansible_password }}'

# This should only be required for Windows Server OS'
- name: Ensure WebDAV client feature is installed
  ansible.windows.win_feature:
    name: WebDAV-Redirector
    state: present
  register: webdav_feature

- name: Reboot after installing WebDAV client feature
  ansible.windows.win_reboot:
  when: webdav_feature.reboot_required

- name: Map the HTTPS WebDAV location
  community.windows.win_mapped_drive:
    letter: W
    path: \\live.sysinternals.com@SSL\tools  # https://live.sysinternals.com/tools
    state: present
```

### Authors

- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
