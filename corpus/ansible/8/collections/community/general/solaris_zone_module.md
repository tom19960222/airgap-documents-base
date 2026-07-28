---
collection: ansible
version: "8"
title: "community.general.solaris_zone module – Manage Solaris zones"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/solaris_zone_module.html
fetched_at: 2026-07-28T01:50:42+00:00
---
# community.general.solaris_zone module – Manage Solaris zones

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
> see [Requirements](solaris_zone_module.md#ansible-collections-community-general-solaris-zone-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.solaris_zone`.

- [Synopsis](solaris_zone_module.md#synopsis)
- [Requirements](solaris_zone_module.md#requirements)
- [Parameters](solaris_zone_module.md#parameters)
- [Attributes](solaris_zone_module.md#attributes)
- [Examples](solaris_zone_module.md#examples)

## [Synopsis](solaris_zone_module.md#id1)

- Create, start, stop and delete Solaris zones.
- This module does not currently allow changing of options for a zone that is already been created.

Aliases: system.solaris_zone

## [Requirements](solaris_zone_module.md#id2)

The below requirements are needed on the host that executes this module.

- Solaris 10 or 11

## [Parameters](solaris_zone_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attach_options**  string | Extra options to the zoneadm attach command. For example, this can be used to specify whether a minimum or full update of packages is required and if any packages need to be deleted. For valid values, see zoneadm(1M)  **Default:** `""` |
| **config**  string | The zonecfg configuration commands for this zone. See zonecfg(1M) for the valid options and syntax. Typically this is a list of options separated by semi-colons or new lines, e.g. “set auto-boot=true;add net;set physical=bge0;set address=10.1.1.1;end”  **Default:** `""` |
| **create_options**  string | Extra options to the zonecfg(1M) create command.  **Default:** `""` |
| **install_options**  string | Extra options to the zoneadm(1M) install command. To automate Solaris 11 zone creation, use this to specify the profile XML file, e.g. install_options=”-c sc_profile.xml”  **Default:** `""` |
| **name**  string / required | Zone name.  A zone name must be unique name.  A zone name must begin with an alphanumeric character.  The name can contain alphanumeric characters, underscores `_`, hyphens `-`, and periods `.`.  The name cannot be longer than 64 characters. |
| **path**  string | The path where the zone will be created. This is required when the zone is created, but not used otherwise. |
| **root_password**  string | The password hash for the root account. If not specified, the zone’s root account will not have a password. |
| **sparse**  boolean | Whether to create a sparse (`true`) or whole root (`false`) zone.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | `present`, configure and install the zone.  `installed`, synonym for `present`.  `running`, if the zone already exists, boot it, otherwise, configure and install the zone first, then boot it.  `started`, synonym for `running`.  `stopped`, shutdown a zone.  `absent`, destroy the zone.  `configured`, configure the ready so that it’s to be attached.  `attached`, attach a zone, but do not boot it.  `detached`, shutdown and detach a zone  **Choices:**   - `"absent"` - `"attached"` - `"configured"` - `"detached"` - `"installed"` - `"present"` ← (default) - `"running"` - `"started"` - `"stopped"` |
| **timeout**  integer | Timeout, in seconds, for zone to boot.  **Default:** `600` |

## [Attributes](solaris_zone_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](solaris_zone_module.md#id5)

```yaml+jinja
- name: Create and install a zone, but don't boot it
  community.general.solaris_zone:
    name: zone1
    state: present
    path: /zones/zone1
    sparse: true
    root_password: Be9oX7OSwWoU.
    config: 'set autoboot=true; add net; set physical=bge0; set address=10.1.1.1; end'

- name: Create and install a zone and boot it
  community.general.solaris_zone:
    name: zone1
    state: running
    path: /zones/zone1
    root_password: Be9oX7OSwWoU.
    config: 'set autoboot=true; add net; set physical=bge0; set address=10.1.1.1; end'

- name: Boot an already installed zone
  community.general.solaris_zone:
    name: zone1
    state: running

- name: Stop a zone
  community.general.solaris_zone:
    name: zone1
    state: stopped

- name: Destroy a zone
  community.general.solaris_zone:
    name: zone1
    state: absent

- name: Detach a zone
  community.general.solaris_zone:
    name: zone1
    state: detached

- name: Configure a zone, ready to be attached
  community.general.solaris_zone:
    name: zone1
    state: configured
    path: /zones/zone1
    root_password: Be9oX7OSwWoU.
    config: 'set autoboot=true; add net; set physical=bge0; set address=10.1.1.1; end'

- name: Attach zone1
  community.general.solaris_zone:
    name: zone1
    state: attached
    attach_options: -u
```

### Authors

- Paul Markham (@pmarkham)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
