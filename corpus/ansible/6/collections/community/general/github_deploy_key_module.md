---
collection: ansible
version: "6"
title: "community.general.github_deploy_key module – Manages deploy keys for GitHub repositories"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/github_deploy_key_module.html
fetched_at: 2026-07-27T17:09:01+00:00
---
# community.general.github_deploy_key module – Manages deploy keys for GitHub repositories

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
> To use it in a playbook, specify: `community.general.github_deploy_key`.

- [Synopsis](github_deploy_key_module.md#synopsis)
- [Parameters](github_deploy_key_module.md#parameters)
- [Notes](github_deploy_key_module.md#notes)
- [Examples](github_deploy_key_module.md#examples)
- [Return Values](github_deploy_key_module.md#return-values)

## [Synopsis](github_deploy_key_module.md#id1)

- Adds or removes deploy keys for GitHub repositories. Supports authentication using username and password, username and password and 2-factor authentication code (OTP), OAuth2 token, or personal access token. Admin rights on the repository are required.

## [Parameters](github_deploy_key_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | If `true`, forcefully adds the deploy key by deleting any existing deploy key with the same public key or title.  Choices:   - `false` ← (default) - `true` |
| **github_url**  string  added in community.general 0.2.0 | The base URL of the GitHub API  Default: `"https://api.github.com"` |
| **key**  string / required | The SSH public key to add to the repository as a deploy key. |
| **name**  aliases: title, label  string / required | The name for the deploy key. |
| **otp**  integer | The 6 digit One Time Password for 2-Factor Authentication. Required together with *username* and *password*. |
| **owner**  aliases: account, organization  string / required | The name of the individual account or organization that owns the GitHub repository. |
| **password**  string | The password to authenticate with. Alternatively, a personal access token can be used instead of *username* and *password* combination. |
| **read_only**  boolean | If `true`, the deploy key will only be able to read repository contents. Otherwise, the deploy key will be able to read and write.  Choices:   - `false` - `true` ← (default) |
| **repo**  aliases: repository  string / required | The name of the GitHub repository. |
| **state**  string | The state of the deploy key.  Choices:   - `"present"` ← (default) - `"absent"` |
| **token**  string | The OAuth2 token or personal access token to authenticate with. Mutually exclusive with *password*. |
| **username**  string | The username to authenticate with. Should not be set when using personal access token |

## [Notes](github_deploy_key_module.md#id3)

> **Note:**
>
> - Refer to GitHub’s API documentation here: <https://developer.github.com/v3/repos/keys/>.

## [Examples](github_deploy_key_module.md#id4)

```yaml+jinja
- name: Add a new read-only deploy key to a GitHub repository using basic authentication
  community.general.github_deploy_key:
    owner: "johndoe"
    repo: "example"
    name: "new-deploy-key"
    key: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAwXxn7kIMNWzcDfou..."
    read_only: true
    username: "johndoe"
    password: "supersecretpassword"

- name: Remove an existing deploy key from a GitHub repository
  community.general.github_deploy_key:
    owner: "johndoe"
    repository: "example"
    name: "new-deploy-key"
    key: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAwXxn7kIMNWzcDfou..."
    force: true
    username: "johndoe"
    password: "supersecretpassword"
    state: absent

- name: Add a new deploy key to a GitHub repository, replace an existing key, use an OAuth2 token to authenticate
  community.general.github_deploy_key:
    owner: "johndoe"
    repository: "example"
    name: "new-deploy-key"
    key: "{{ lookup('file', '~/.ssh/github.pub') }}"
    force: true
    token: "ABAQDAwXxn7kIMNWzcDfo..."

- name: Re-add a deploy key to a GitHub repository but with a different name
  community.general.github_deploy_key:
    owner: "johndoe"
    repository: "example"
    name: "replace-deploy-key"
    key: "{{ lookup('file', '~/.ssh/github.pub') }}"
    username: "johndoe"
    password: "supersecretpassword"

- name: Add a new deploy key to a GitHub repository using 2FA
  community.general.github_deploy_key:
    owner: "johndoe"
    repo: "example"
    name: "new-deploy-key-2"
    key: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAwXxn7kIMNWzcDfou..."
    username: "johndoe"
    password: "supersecretpassword"
    otp: 123456

- name: Add a read-only deploy key to a repository hosted on GitHub Enterprise
  community.general.github_deploy_key:
    github_url: "https://api.example.com"
    owner: "janedoe"
    repo: "example"
    name: "new-deploy-key"
    key: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAwXxn7kIMNWzcDfou..."
    read_only: true
    username: "janedoe"
    password: "supersecretpassword"
```

## [Return Values](github_deploy_key_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error**  string | the error message returned by the GitHub API  Returned: failed  Sample: `"key is already in use"` |
| **http_status_code**  integer | the HTTP status code returned by the GitHub API  Returned: failed  Sample: `400` |
| **id**  integer | the key identifier assigned by GitHub for the deploy key  Returned: changed  Sample: `24381901` |
| **msg**  string | the status message describing what occurred  Returned: always  Sample: `"Deploy key added successfully"` |

### Authors

- Ali (@bincyber)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
