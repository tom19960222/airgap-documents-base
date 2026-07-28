---
collection: ansible
version: "6"
title: "community.general.hponcfg module – Configure HP iLO interface using hponcfg"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/hponcfg_module.html
fetched_at: 2026-07-27T17:09:23+00:00
---
# community.general.hponcfg module – Configure HP iLO interface using hponcfg

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
> see [Requirements](hponcfg_module.md#ansible-collections-community-general-hponcfg-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hponcfg`.

- [Synopsis](hponcfg_module.md#synopsis)
- [Requirements](hponcfg_module.md#requirements)
- [Parameters](hponcfg_module.md#parameters)
- [Notes](hponcfg_module.md#notes)
- [Examples](hponcfg_module.md#examples)

## [Synopsis](hponcfg_module.md#id1)

- This modules configures the HP iLO interface using hponcfg.

## [Requirements](hponcfg_module.md#id2)

The below requirements are needed on the host that executes this module.

- hponcfg tool

## [Parameters](hponcfg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **executable**  string | Path to the hponcfg executable (`hponcfg` which uses $PATH).  Default: `"hponcfg"` |
| **minfw**  string | The minimum firmware level needed. |
| **path**  aliases: src  path / required | The XML file as accepted by hponcfg. |
| **verbose**  boolean | Run hponcfg in verbose mode (-v).  Choices:   - `false` ← (default) - `true` |

## [Notes](hponcfg_module.md#id4)

> **Note:**
>
> - You need a working hponcfg on the target system.

## [Examples](hponcfg_module.md#id5)

```yaml+jinja
- name: Example hponcfg configuration XML
  ansible.builtin.copy:
    content: |
      <ribcl VERSION="2.0">
        <login USER_LOGIN="user" PASSWORD="password">
          <rib_info MODE="WRITE">
            <mod_global_settings>
              <session_timeout value="0"/>
              <ssh_status value="Y"/>
              <ssh_port value="22"/>
              <serial_cli_status value="3"/>
              <serial_cli_speed value="5"/>
            </mod_global_settings>
          </rib_info>
        </login>
      </ribcl>
    dest: /tmp/enable-ssh.xml

- name: Configure HP iLO using enable-ssh.xml
  community.general.hponcfg:
    src: /tmp/enable-ssh.xml

- name: Configure HP iLO on VMware ESXi hypervisor
  community.general.hponcfg:
    src: /tmp/enable-ssh.xml
    executable: /opt/hp/tools/hponcfg
```

### Authors

- Dag Wieers (@dagwieers)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
