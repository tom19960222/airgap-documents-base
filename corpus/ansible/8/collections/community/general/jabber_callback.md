---
collection: ansible
version: "8"
title: "community.general.jabber callback – post task events to a jabber server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/jabber_callback.html
fetched_at: 2026-07-28T01:51:57+00:00
---
# community.general.jabber callback – post task events to a jabber server

> **Note:**
>
> This callback plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this callback plugin,
> see [Requirements](jabber_callback.md#ansible-collections-community-general-jabber-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.jabber`.

- [Callback plugin](jabber_callback.md#callback-plugin)
- [Synopsis](jabber_callback.md#synopsis)
- [Requirements](jabber_callback.md#requirements)
- [Parameters](jabber_callback.md#parameters)

## [Callback plugin](jabber_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](jabber_callback.md#id2)

- The chatty part of ChatOps with a Hipchat server as a target.
- This callback plugin sends status updates to a HipChat channel during playbook execution.

## [Requirements](jabber_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- xmpp (Python library <https://github.com/ArchipelProject/xmpppy>)

## [Parameters](jabber_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **password**  string / required | Password for the user to the jabber server  **Configuration:**   - Environment variable: [`JABBER_PASS`](../../environment_variables.md#envvar-JABBER_PASS) |
| **server**  string / required | connection info to jabber server  **Configuration:**   - Environment variable: [`JABBER_SERV`](../../environment_variables.md#envvar-JABBER_SERV) |
| **to**  string / required | chat identifier that will receive the message  **Configuration:**   - Environment variable: [`JABBER_TO`](../../environment_variables.md#envvar-JABBER_TO) |
| **user**  string / required | Jabber user to authenticate as  **Configuration:**   - Environment variable: [`JABBER_USER`](../../environment_variables.md#envvar-JABBER_USER) |

### Authors

- Unknown

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
