---
collection: ansible
version: "8"
title: "community.general.rhn_register module – Manage Red Hat Network registration using the rhnreg_ks command"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/rhn_register_module.html
fetched_at: 2026-07-28T01:49:58+00:00
---
# community.general.rhn_register module – Manage Red Hat Network registration using the `rhnreg_ks` command

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
> see [Requirements](rhn_register_module.md#ansible-collections-community-general-rhn-register-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rhn_register`.

- [DEPRECATED](rhn_register_module.md#deprecated)
- [Synopsis](rhn_register_module.md#synopsis)
- [Requirements](rhn_register_module.md#requirements)
- [Parameters](rhn_register_module.md#parameters)
- [Attributes](rhn_register_module.md#attributes)
- [Notes](rhn_register_module.md#notes)
- [Examples](rhn_register_module.md#examples)
- [Status](rhn_register_module.md#status)

## [DEPRECATED](rhn_register_module.md#id1)

Removed in:
:   version 10.0.0

Why:
:   RHN hosted at redhat.com was discontinued years ago, and Spacewalk 5
    (which uses RHN) is EOL since 2020, May 31st; while this module could
    work on Uyuni / SUSE Manager (fork of Spacewalk 5), we have not heard
    about anyone using it in those setups.

Alternative:
:   Contact the community.general maintainers to report the usage of this
    module, and potentially step up to maintain it.

## [Synopsis](rhn_register_module.md#id2)

- Manage registration to the Red Hat Network.

Aliases: packaging.os.rhn_register

## [Requirements](rhn_register_module.md#id3)

The below requirements are needed on the host that executes this module.

- rhnreg_ks
- either libxml2 or lxml

## [Parameters](rhn_register_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **activationkey**  string | Supply an activation key for use with registration. |
| **ca_cert**  aliases: sslcacert  path | Supply a custom ssl CA certificate file for use with registration. |
| **channels**  list / elements=string | Optionally specify a list of channels to subscribe to upon successful registration.  **Default:** `[]` |
| **enable_eus**  boolean | If `false`, extended update support will be requested.  **Choices:**   - `false` ← (default) - `true` |
| **force**  boolean  *added in community.general 2.0.0* | Force registration, even if system is already registered.  **Choices:**   - `false` ← (default) - `true` |
| **nopackages**  boolean | If `true`, the registered node will not upload its installed packages information to Satellite server.  **Choices:**   - `false` ← (default) - `true` |
| **password**  string | Red Hat Network password. |
| **profilename**  string | Supply an profilename for use with registration. |
| **server_url**  string | Specify an alternative Red Hat Network server URL.  The default is the current value of `serverURL` from `/etc/sysconfig/rhn/up2date`. |
| **state**  string | Whether to register (`present`), or unregister (`absent`) a system.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **systemorgid**  string | Supply an organizational id for use with registration. |
| **username**  string | Red Hat Network username. |

## [Attributes](rhn_register_module.md#id5)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](rhn_register_module.md#id6)

> **Note:**
>
> - This is for older Red Hat products. You probably want the [community.general.redhat_subscription](redhat_subscription_module.md#ansible-collections-community-general-redhat-subscription-module) module instead.
> - In order to register a system, `rhnreg_ks` requires either a username and password, or an activationkey.

## [Examples](rhn_register_module.md#id7)

```yaml+jinja
- name: Unregister system from RHN
  community.general.rhn_register:
    state: absent
    username: joe_user
    password: somepass

- name: Register as user with password and auto-subscribe to available content
  community.general.rhn_register:
    state: present
    username: joe_user
    password: somepass

- name: Register with activationkey and enable extended update support
  community.general.rhn_register:
    state: present
    activationkey: 1-222333444
    enable_eus: true

- name: Register with activationkey and set a profilename which may differ from the hostname
  community.general.rhn_register:
    state: present
    activationkey: 1-222333444
    profilename: host.example.com.custom

- name: Register as user with password against a satellite server
  community.general.rhn_register:
    state: present
    username: joe_user
    password: somepass
    server_url: https://xmlrpc.my.satellite/XMLRPC

- name: Register as user with password and enable channels
  community.general.rhn_register:
    state: present
    username: joe_user
    password: somepass
    channels: rhel-x86_64-server-6-foo-1,rhel-x86_64-server-6-bar-1

- name: Force-register as user with password to ensure registration is current on server
  community.general.rhn_register:
    state: present
    username: joe_user
    password: somepass
    server_url: https://xmlrpc.my.satellite/XMLRPC
    force: true
```

## [Status](rhn_register_module.md#id8)

- This module will be removed in version 10.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](rhn_register_module.md#deprecated).

### Authors

- James Laska (@jlaska)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
