---
collection: ansible
version: "8"
title: "community.general.lxd_profile module – Manage LXD profiles"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/lxd_profile_module.html
fetched_at: 2026-07-28T01:47:42+00:00
---
# community.general.lxd_profile module – Manage LXD profiles

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
> To use it in a playbook, specify: `community.general.lxd_profile`.

- [Synopsis](lxd_profile_module.md#synopsis)
- [Parameters](lxd_profile_module.md#parameters)
- [Attributes](lxd_profile_module.md#attributes)
- [Notes](lxd_profile_module.md#notes)
- [Examples](lxd_profile_module.md#examples)
- [Return Values](lxd_profile_module.md#return-values)

## [Synopsis](lxd_profile_module.md#id1)

- Management of LXD profiles

Aliases: cloud.lxd.lxd_profile

## [Parameters](lxd_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_cert**  aliases: cert_file  path | The client certificate file path.  If not specified, it defaults to `$HOME/.config/lxc/client.crt`. |
| **client_key**  aliases: key_file  path | The client certificate key file path.  If not specified, it defaults to `$HOME/.config/lxc/client.key`. |
| **config**  dictionary | The config for the instance (e.g. {“limits.memory”: “4GB”}). See <https://documentation.ubuntu.com/lxd/en/latest/api/#/profiles/profile_get>.  If the profile already exists and its “config” value in metadata obtained from GET /1.0/profiles/<name> <https://documentation.ubuntu.com/lxd/en/latest/api/#/profiles/profile_get> are different, then this module tries to apply the configurations <https://documentation.ubuntu.com/lxd/en/latest/api/#/profiles/profile_put>.  Not all config values are supported to apply the existing profile. Maybe you need to delete and recreate a profile. |
| **description**  string | Description of the profile. |
| **devices**  dictionary | The devices for the profile (e.g. {“rootfs”: {“path”: “/dev/kvm”, “type”: “unix-char”}). See <https://documentation.ubuntu.com/lxd/en/latest/api/#/profiles/profile_get>. |
| **merge_profile**  boolean  *added in community.general 2.1.0* | Merge the configuration of the present profile with the new desired configuration, instead of replacing it.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Name of a profile. |
| **new_name**  string | A new name of a profile.  If this parameter is specified a profile will be renamed to this name. See <https://documentation.ubuntu.com/lxd/en/latest/api/#/profiles/profile_post>. |
| **project**  string  *added in community.general 4.8.0* | Project of a profile. See <https://documentation.ubuntu.com/lxd/en/latest/projects/>. |
| **snap_url**  string | The unix domain socket path when LXD is installed by snap package manager.  **Default:** `"unix:/var/snap/lxd/common/lxd/unix.socket"` |
| **state**  string | Define the state of a profile.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **trust_password**  string | The client trusted password.  You need to set this password on the LXD server before running this module using the following command. lxc config set core.trust_password <some random password> See <https://www.stgraber.org/2016/04/18/lxd-api-direct-interaction/>  If trust_password is set, this module send a request for authentication before sending any requests. |
| **url**  string | The unix domain socket path or the https URL for the LXD server.  **Default:** `"unix:/var/lib/lxd/unix.socket"` |

## [Attributes](lxd_profile_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](lxd_profile_module.md#id4)

> **Note:**
>
> - Profiles must have a unique name. If you attempt to create a profile with a name that already existed in the users namespace the module will simply return as “unchanged”.

## [Examples](lxd_profile_module.md#id5)

```yaml+jinja
# An example for creating a profile
- hosts: localhost
  connection: local
  tasks:
    - name: Create a profile
      community.general.lxd_profile:
        name: macvlan
        state: present
        config: {}
        description: my macvlan profile
        devices:
          eth0:
            nictype: macvlan
            parent: br0
            type: nic

# An example for creating a profile in project mytestproject
- hosts: localhost
  connection: local
  tasks:
    - name: Create a profile
      community.general.lxd_profile:
        name: testprofile
        project: mytestproject
        state: present
        config: {}
        description: test profile in project mytestproject
        devices: {}

# An example for creating a profile via http connection
- hosts: localhost
  connection: local
  tasks:
  - name: Create macvlan profile
    community.general.lxd_profile:
      url: https://127.0.0.1:8443
      # These client_cert and client_key values are equal to the default values.
      #client_cert: "{{ lookup('env', 'HOME') }}/.config/lxc/client.crt"
      #client_key: "{{ lookup('env', 'HOME') }}/.config/lxc/client.key"
      trust_password: mypassword
      name: macvlan
      state: present
      config: {}
      description: my macvlan profile
      devices:
        eth0:
          nictype: macvlan
          parent: br0
          type: nic

# An example for modify/merge a profile
- hosts: localhost
  connection: local
  tasks:
    - name: Merge a profile
      community.general.lxd_profile:
        merge_profile: true
        name: macvlan
        state: present
        config: {}
        description: my macvlan profile
        devices:
          eth0:
            nictype: macvlan
            parent: br0
            type: nic

# An example for deleting a profile
- hosts: localhost
  connection: local
  tasks:
    - name: Delete a profile
      community.general.lxd_profile:
        name: macvlan
        state: absent

# An example for renaming a profile
- hosts: localhost
  connection: local
  tasks:
    - name: Rename a profile
      community.general.lxd_profile:
        name: macvlan
        new_name: macvlan2
        state: present
```

## [Return Values](lxd_profile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **actions**  list / elements=string | List of actions performed for the profile.  **Returned:** success  **Sample:** `["create"]` |
| **logs**  list / elements=string | The logs of requests and responses.  **Returned:** when ansible-playbook is invoked with -vvvv.  **Sample:** `["(too long to be placed here)"]` |
| **old_state**  string | The old state of the profile  **Returned:** success  **Sample:** `"absent"` |

### Authors

- Hiroaki Nakamura (@hnakamur)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
