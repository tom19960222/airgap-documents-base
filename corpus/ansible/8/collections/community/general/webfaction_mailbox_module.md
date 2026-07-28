---
collection: ansible
version: "8"
title: "community.general.webfaction_mailbox module – Add or remove mailboxes on Webfaction"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/webfaction_mailbox_module.html
fetched_at: 2026-07-28T01:51:26+00:00
---
# community.general.webfaction_mailbox module – Add or remove mailboxes on Webfaction

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.webfaction_mailbox`.

- [DEPRECATED](webfaction_mailbox_module.md#deprecated)
- [Synopsis](webfaction_mailbox_module.md#synopsis)
- [Parameters](webfaction_mailbox_module.md#parameters)
- [Attributes](webfaction_mailbox_module.md#attributes)
- [Notes](webfaction_mailbox_module.md#notes)
- [Examples](webfaction_mailbox_module.md#examples)
- [Status](webfaction_mailbox_module.md#status)

## [DEPRECATED](webfaction_mailbox_module.md#id1)

Removed in:
:   version 9.0.0

Why:
:   the endpoints this module relies on do not exist any more and do not resolve to IPs in DNS.

Alternative:
:   no known alternative at this point

## [Synopsis](webfaction_mailbox_module.md#id2)

- Add or remove mailboxes on a Webfaction account. Further documentation at <https://github.com/quentinsf/ansible-webfaction>.

Aliases: cloud.webfaction.webfaction_mailbox

## [Parameters](webfaction_mailbox_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **login_name**  string / required | The webfaction account to use |
| **login_password**  string / required | The webfaction password to use |
| **mailbox_name**  string / required | The name of the mailbox |
| **mailbox_password**  string / required | The password for the mailbox |
| **state**  string | Whether the mailbox should exist  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Attributes](webfaction_mailbox_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](webfaction_mailbox_module.md#id5)

> **Note:**
>
> - You can run playbooks that use this on a local machine, or on a Webfaction host, or elsewhere, since the scripts use the remote webfaction API. The location is not important. However, running them on multiple hosts *simultaneously* is best avoided. If you do not specify `localhost` as your host, you may want to add `serial=1` to the plays.
> - See [the webfaction API](https://docs.webfaction.com/xmlrpc-api/) for more info.

## [Examples](webfaction_mailbox_module.md#id6)

```yaml+jinja
- name: Create a mailbox
  community.general.webfaction_mailbox:
    mailbox_name="mybox"
    mailbox_password="myboxpw"
    state=present
    login_name={{webfaction_user}}
    login_password={{webfaction_passwd}}
```

## [Status](webfaction_mailbox_module.md#id7)

- This module will be removed in version 9.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](webfaction_mailbox_module.md#deprecated).

### Authors

- Quentin Stafford-Fraser (@quentinsf)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
