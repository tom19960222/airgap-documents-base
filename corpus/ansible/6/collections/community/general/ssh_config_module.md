---
collection: ansible
version: "6"
title: "community.general.ssh_config module – Manage SSH config for user"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ssh_config_module.html
fetched_at: 2026-07-27T17:13:23+00:00
---
# community.general.ssh_config module – Manage SSH config for user

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](ssh_config_module.md#ansible-collections-community-general-ssh-config-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ssh_config`.

New in community.general 2.0.0

- [Synopsis](ssh_config_module.md#synopsis)
- [Requirements](ssh_config_module.md#requirements)
- [Parameters](ssh_config_module.md#parameters)
- [Notes](ssh_config_module.md#notes)
- [Examples](ssh_config_module.md#examples)
- [Return Values](ssh_config_module.md#return-values)

## [Synopsis](ssh_config_module.md#id1)

- Configures SSH hosts with special `IdentityFile`s and hostnames.

## [Requirements](ssh_config_module.md#id2)

The below requirements are needed on the host that executes this module.

- StormSSH

## [Parameters](ssh_config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **forward_agent**  boolean  added in community.general 4.0.0 | Sets the `ForwardAgent` option.  Choices:   - `false` - `true` |
| **group**  string | Which group this configuration file belongs to.  If none given, *user* is used. |
| **host**  string / required | The endpoint this configuration is valid for.  Can be an actual address on the internet or an alias that will connect to the value of *hostname*. |
| **hostname**  string | The actual host to connect to when connecting to the host defined. |
| **identity_file**  path | The path to an identity file (SSH private key) that will be used when connecting to this host.  File need to exist and have mode `0600` to be valid. |
| **port**  string | The actual port to connect to when connecting to the host defined. |
| **proxycommand**  string | Sets the `ProxyCommand` option. |
| **remote_user**  string | Specifies the user to log in as. |
| **ssh_config_file**  path | SSH config file.  If *user* and this option are not specified, `/etc/ssh/ssh_config` is used.  Mutually exclusive with *user*. |
| **state**  string | Whether a host entry should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **strict_host_key_checking**  string | Whether to strictly check the host key when doing connections to the remote host.  Choices:   - `"yes"` - `"no"` - `"ask"` |
| **user**  string | Which user account this configuration file belongs to.  If none given and *ssh_config_file* is not specified, `/etc/ssh/ssh_config` is used.  If a user is given, `~/.ssh/config` is used.  Mutually exclusive with *ssh_config_file*. |
| **user_known_hosts_file**  string | Sets the user known hosts file option. |

## [Notes](ssh_config_module.md#id4)

> **Note:**
>
> - Supports check mode.

## [Examples](ssh_config_module.md#id5)

```yaml+jinja
- name: Add a host in the configuration
  community.general.ssh_config:
    user: akasurde
    host: "example.com"
    hostname: "github.com"
    identity_file: "/home/akasurde/.ssh/id_rsa"
    port: '2223'
    state: present

- name: Delete a host from the configuration
  community.general.ssh_config:
    ssh_config_file: "{{ ssh_config_test }}"
    host: "example.com"
    state: absent
```

## [Return Values](ssh_config_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hosts_added**  list / elements=string | A list of host added.  Returned: success  Sample: `["example.com"]` |
| **hosts_change_diff**  list / elements=string | A list of host diff changes.  Returned: on change  Sample: `[{"example.com": {"new": {"hostname": "github.com", "identityfile": ["/tmp/test_ssh_config/fake_id_rsa"], "port": "2224"}, "old": {"hostname": "github.com", "identityfile": ["/tmp/test_ssh_config/fake_id_rsa"], "port": "2224"}}}]` |
| **hosts_changed**  list / elements=string | A list of host changed.  Returned: success  Sample: `["example.com"]` |
| **hosts_removed**  list / elements=string | A list of host removed.  Returned: success  Sample: `["example.com"]` |

### Authors

- Björn Andersson (@gaqzi)
- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
