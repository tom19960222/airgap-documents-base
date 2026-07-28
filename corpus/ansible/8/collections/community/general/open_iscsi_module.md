---
collection: ansible
version: "8"
title: "community.general.open_iscsi module – Manage iSCSI targets with Open-iSCSI"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/open_iscsi_module.html
fetched_at: 2026-07-28T01:48:41+00:00
---
# community.general.open_iscsi module – Manage iSCSI targets with Open-iSCSI

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](open_iscsi_module.md#ansible-collections-community-general-open-iscsi-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.open_iscsi`.

- [Synopsis](open_iscsi_module.md#synopsis)
- [Requirements](open_iscsi_module.md#requirements)
- [Parameters](open_iscsi_module.md#parameters)
- [Attributes](open_iscsi_module.md#attributes)
- [Examples](open_iscsi_module.md#examples)

## [Synopsis](open_iscsi_module.md#id1)

- Discover targets on given portal, (dis)connect targets, mark targets to manually or auto start, return device nodes of connected targets.

Aliases: system.open_iscsi

## [Requirements](open_iscsi_module.md#id2)

The below requirements are needed on the host that executes this module.

- open_iscsi library and tools (iscsiadm)

## [Parameters](open_iscsi_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auto_node_startup**  aliases: automatic  boolean | Whether the target node should be automatically connected at startup.  **Choices:**   - `false` - `true` |
| **auto_portal_startup**  boolean  *added in community.general 3.2.0* | Whether the target node portal should be automatically connected at startup.  **Choices:**   - `false` - `true` |
| **discover**  boolean | Whether the list of target nodes on the portal should be (re)discovered and added to the persistent iSCSI database.  Keep in mind that `iscsiadm` discovery resets configuration, like `node.startup` to manual, hence combined with `auto_node_startup=true` will always return a changed state.  **Choices:**   - `false` ← (default) - `true` |
| **login**  aliases: state  boolean | Whether the target node should be connected.  **Choices:**   - `false` - `true` |
| **node_auth**  string | The value for `node.session.auth.authmethod`.  **Default:** `"CHAP"` |
| **node_pass**  string | The value for `node.session.auth.password`. |
| **node_pass_in**  string  *added in community.general 3.8.0* | The value for `node.session.auth.password_in`. |
| **node_user**  string | The value for `node.session.auth.username`. |
| **node_user_in**  string  *added in community.general 3.8.0* | The value for `node.session.auth.username_in`. |
| **port**  string | The port on which the iSCSI target process listens.  **Default:** `"3260"` |
| **portal**  aliases: ip  string | The domain name or IP address of the iSCSI target. |
| **rescan**  boolean  *added in community.general 4.1.0* | Rescan an established session for discovering new targets.  When `target` is omitted, will rescan all sessions.  **Choices:**   - `false` ← (default) - `true` |
| **show_nodes**  boolean | Whether the list of nodes in the persistent iSCSI database should be returned by the module.  **Choices:**   - `false` ← (default) - `true` |
| **target**  aliases: name, targetname  string | The iSCSI target name. |

## [Attributes](open_iscsi_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](open_iscsi_module.md#id5)

```yaml+jinja
- name: Perform a discovery on sun.com and show available target nodes
  community.general.open_iscsi:
    show_nodes: true
    discover: true
    portal: sun.com

- name: Perform a discovery on 10.1.2.3 and show available target nodes
  community.general.open_iscsi:
    show_nodes: true
    discover: true
    ip: 10.1.2.3

# NOTE: Only works if exactly one target is exported to the initiator
- name: Discover targets on portal and login to the one available
  community.general.open_iscsi:
    portal: '{{ iscsi_target }}'
    login: true
    discover: true

- name: Connect to the named target, after updating the local persistent database (cache)
  community.general.open_iscsi:
    login: true
    target: iqn.1986-03.com.sun:02:f8c1f9e0-c3ec-ec84-c9c9-8bfb0cd5de3d

- name: Disconnect from the cached named target
  community.general.open_iscsi:
    login: false
    target: iqn.1986-03.com.sun:02:f8c1f9e0-c3ec-ec84-c9c9-8bfb0cd5de3d

- name: Override and disable automatic portal login on specific portal
  community.general.open_iscsi:
    login: false
    portal: 10.1.1.250
    auto_portal_startup: false
    target: iqn.1986-03.com.sun:02:f8c1f9e0-c3ec-ec84-c9c9-8bfb0cd5de3d

- name: Rescan one or all established sessions to discover new targets (omit target for all sessions)
  community.general.open_iscsi:
    rescan: true
    target: iqn.1986-03.com.sun:02:f8c1f9e0-c3ec-ec84-c9c9-8bfb0cd5de3d
```

### Authors

- Serge van Ginderachter (@srvg)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
