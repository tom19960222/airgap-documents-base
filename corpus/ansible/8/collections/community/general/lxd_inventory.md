---
collection: ansible
version: "8"
title: "community.general.lxd inventory – Returns Ansible inventory from lxd host"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/lxd_inventory.html
fetched_at: 2026-07-28T01:52:33+00:00
---
# community.general.lxd inventory – Returns Ansible inventory from lxd host

> **Note:**
>
> This inventory plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](lxd_inventory.md#ansible-collections-community-general-lxd-inventory-requirements) for details.
>
> To use it in a playbook, specify: `community.general.lxd`.

New in community.general 3.0.0

- [Synopsis](lxd_inventory.md#synopsis)
- [Requirements](lxd_inventory.md#requirements)
- [Parameters](lxd_inventory.md#parameters)
- [Examples](lxd_inventory.md#examples)

## [Synopsis](lxd_inventory.md#id1)

- Get inventory from the lxd.
- Uses a YAML configuration file that ends with ‘lxd.(yml|yaml)’.

## [Requirements](lxd_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- ipaddress
- lxd >= 4.0

## [Parameters](lxd_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **client_cert**  aliases: cert_file  path | The client certificate file path.  **Default:** `"$HOME/.config/lxc/client.crt"` |
| **client_key**  aliases: key_file  path | The client certificate key file path.  **Default:** `"$HOME/.config/lxc/client.key"` |
| **groupby**  dictionary | Create groups by the following keywords `location`, `network_range`, `os`, `pattern`, `profile`, `release`, `type`, `vlanid`.  See example for syntax. |
| **plugin**  string / required | Token that ensures this is a source file for the ‘lxd’ plugin.  **Choices:**   - `"community.general.lxd"` |
| **prefered_instance_network_family**  string | If an instance has multiple network interfaces, which one is the preferred by family.  Specify `inet` for IPv4 and `inet6` for IPv6.  **Choices:**   - `"inet"` ← (default) - `"inet6"` |
| **prefered_instance_network_interface**  aliases: prefered_container_network_interface  string | If an instance has multiple network interfaces, select which one is the preferred as pattern.  Combined with the first number that can be found e.g. ‘eth’ + 0.  The option has been renamed from `prefered_container_network_interface` to `prefered_instance_network_interface` in community.general 3.8.0. The old name still works as an alias.  **Default:** `"eth"` |
| **project**  string  *added in community.general 6.2.0* | Filter the instance according to the given project.  **Default:** `"default"` |
| **state**  string | Filter the instance according to the current status.  **Choices:**   - `"STOPPED"` - `"STARTING"` - `"RUNNING"` - `"none"` ← (default) |
| **trust_password**  string | The client trusted password.  You need to set this password on the lxd server before running this module using the following command `lxc config set core.trust_password <some random password>` See <https://documentation.ubuntu.com/lxd/en/latest/authentication/#adding-client-certificates-using-a-trust-password>.  If `trust_password` is set, this module send a request for authentication before sending any requests. |
| **type_filter**  string  *added in community.general 4.2.0* | Filter the instances by type `virtual-machine`, `container` or `both`.  The first version of the inventory only supported containers.  **Choices:**   - `"virtual-machine"` - `"container"` ← (default) - `"both"` |
| **url**  string | The unix domain socket path or the https URL for the lxd server.  Sockets in filesystem have to start with `unix:`.  Mostly `unix:/var/lib/lxd/unix.socket` or `unix:/var/snap/lxd/common/lxd/unix.socket`.  **Default:** `"unix:/var/snap/lxd/common/lxd/unix.socket"` |

## [Examples](lxd_inventory.md#id4)

```yaml+jinja
# simple lxd.yml
plugin: community.general.lxd
url: unix:/var/snap/lxd/common/lxd/unix.socket

# simple lxd.yml including filter
plugin: community.general.lxd
url: unix:/var/snap/lxd/common/lxd/unix.socket
state: RUNNING

# simple lxd.yml including virtual machines and containers
plugin: community.general.lxd
url: unix:/var/snap/lxd/common/lxd/unix.socket
type_filter: both

# grouping lxd.yml
groupby:
  locationBerlin:
    type: location
    attribute: Berlin
  netRangeIPv4:
    type: network_range
    attribute: 10.98.143.0/24
  netRangeIPv6:
    type: network_range
    attribute: fd42:bd00:7b11:2167:216:3eff::/24
  osUbuntu:
    type: os
    attribute: ubuntu
  testpattern:
    type: pattern
    attribute: test
  profileDefault:
    type: profile
    attribute: default
  profileX11:
    type: profile
    attribute: x11
  releaseFocal:
    type: release
    attribute: focal
  releaseBionic:
    type: release
    attribute: bionic
  typeVM:
    type: type
    attribute: virtual-machine
  typeContainer:
    type: type
    attribute: container
  vlan666:
    type: vlanid
    attribute: 666
  projectInternals:
    type: project
    attribute: internals
```

### Authors

- Frank Dornheim (@conloos)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
