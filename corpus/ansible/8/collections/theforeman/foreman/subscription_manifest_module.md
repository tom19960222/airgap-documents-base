---
collection: ansible
version: "8"
title: "theforeman.foreman.subscription_manifest module – Manage Subscription Manifests"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/subscription_manifest_module.html
fetched_at: 2026-07-28T02:56:45+00:00
---
# theforeman.foreman.subscription_manifest module – Manage Subscription Manifests

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](subscription_manifest_module.md#ansible-collections-theforeman-foreman-subscription-manifest-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.subscription_manifest`.

New in theforeman.foreman 1.0.0

- [Synopsis](subscription_manifest_module.md#synopsis)
- [Requirements](subscription_manifest_module.md#requirements)
- [Parameters](subscription_manifest_module.md#parameters)
- [Attributes](subscription_manifest_module.md#attributes)
- [Examples](subscription_manifest_module.md#examples)

## [Synopsis](subscription_manifest_module.md#id1)

- Upload, refresh and delete Subscription Manifests

Aliases: katello_manifest

## [Requirements](subscription_manifest_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](subscription_manifest_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **manifest_path**  path | Path to the manifest zip file  This parameter will be ignored if *state=absent* or *state=refreshed* |
| **organization**  string / required | Organization that the entity is in |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **repository_url**  aliases: redhat_repository_url  string | URL to retrieve content from |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | The state of the manifest  **Choices:**   - `"absent"` - `"present"` ← (default) - `"refreshed"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](subscription_manifest_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **partial** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](subscription_manifest_module.md#id5)

```yaml+jinja
- name: "Upload the RHEL developer edition manifest"
  theforeman.foreman.subscription_manifest:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    state: present
    manifest_path: "/tmp/manifest.zip"
```

### Authors

- Andrew Kofink (@akofink)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
