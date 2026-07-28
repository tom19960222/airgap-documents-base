---
collection: ansible
version: "8"
title: "community.general.snap module – Manages snaps"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/snap_module.html
fetched_at: 2026-07-28T01:50:40+00:00
---
# community.general.snap module – Manages snaps

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
> To use it in a playbook, specify: `community.general.snap`.

- [Synopsis](snap_module.md#synopsis)
- [Parameters](snap_module.md#parameters)
- [Attributes](snap_module.md#attributes)
- [See Also](snap_module.md#see-also)
- [Examples](snap_module.md#examples)
- [Return Values](snap_module.md#return-values)

## [Synopsis](snap_module.md#id1)

- Manages snaps packages.

Aliases: packaging.os.snap

## [Parameters](snap_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **channel**  string | Define which release of a snap is installed and tracked for updates. This option can only be specified if there is a single snap in the task.  If not passed, the `snap` command will default to `stable`.  If the value passed does not contain the `track`, it will default to `latest`. For example, if `edge` is passed, the module will assume the channel to be `latest/edge`.  See <https://snapcraft.io/docs/channels> for more details about snap channels. |
| **classic**  boolean | Confinement policy. The classic confinement allows a snap to have the same level of access to the system as “classic” packages, like those managed by APT. This option corresponds to the `--classic` argument. This option can only be specified if there is a single snap in the task.  **Choices:**   - `false` ← (default) - `true` |
| **dangerous**  boolean  *added in community.general 7.2.0* | Install the given snap file even if there are no pre-acknowledged signatures for it, meaning it was not verified and could be dangerous.  **Choices:**   - `false` ← (default) - `true` |
| **name**  list / elements=string / required | Name of the snaps to be installed.  Any named snap accepted by the `snap` command is valid.  Notice that snap files might require `dangerous=true` to ignore the error “cannot find signatures with metadata for snap”. |
| **options**  list / elements=string  *added in community.general 4.4.0* | Set options with pattern `key=value` or `snap:key=value`. If a snap name is given, the option will be applied to that snap only. If the snap name is omitted, the options will be applied to all snaps listed in `name`. Options will only be applied to active snaps. |
| **state**  string | Desired state of the package.  When `state=present` the module will use `snap install` if the snap is not installed, and `snap refresh` if it is installed but from a different channel.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"enabled"` - `"disabled"` |

## [Attributes](snap_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](snap_module.md#id4)

> **See also:**
>
> [community.general.snap_alias](snap_alias_module.md#ansible-collections-community-general-snap-alias-module)
> :   Manages snap aliases.

## [Examples](snap_module.md#id5)

```yaml+jinja
# Install "foo" and "bar" snap
- name: Install foo
  community.general.snap:
    name:
      - foo
      - bar

# Install "foo" snap with options par1=A and par2=B
- name: Install "foo" with options
  community.general.snap:
    name:
      - foo
    options:
      - par1=A
      - par2=B

# Install "foo" and "bar" snaps with common option com=A and specific options fooPar=X and barPar=Y
- name: Install "foo" and "bar" with options
  community.general.snap:
    name:
      - foo
      - bar
    options:
      - com=A
      - foo:fooPar=X
      - bar:barPar=Y

# Remove "foo" snap
- name: Remove foo
  community.general.snap:
    name: foo
    state: absent

# Install a snap with classic confinement
- name: Install "foo" with option --classic
  community.general.snap:
    name: foo
    classic: true

# Install a snap with from a specific channel
- name: Install "foo" with option --channel=latest/edge
  community.general.snap:
    name: foo
    channel: latest/edge
```

## [Return Values](snap_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **channel**  string | The channel the snaps were installed from  **Returned:** When snaps are installed |
| **classic**  boolean | Whether or not the snaps were installed with the classic confinement  **Returned:** When snaps are installed |
| **cmd**  string | The command that was executed on the host  **Returned:** When changed is true |
| **options_changed**  list / elements=string  *added in community.general 4.4.0* | The list of options set/changed in format `snap:key=value`.  **Returned:** When any options have been changed/set |
| **snaps_installed**  list / elements=string | The list of actually installed snaps  **Returned:** When any snaps have been installed |
| **snaps_removed**  list / elements=string | The list of actually removed snaps  **Returned:** When any snaps have been removed |

### Authors

- Victor Carceler (@vcarceler)
- Stanislas Lange (@angristan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
