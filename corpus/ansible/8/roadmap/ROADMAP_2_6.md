---
collection: ansible
version: "8"
title: "Ansible 2.6"
source_url: https://docs.ansible.com/projects/ansible/8/roadmap/ROADMAP_2_6.html
fetched_at: 2026-07-28T01:04:41+00:00
---
# [Ansible 2.6](ROADMAP_2_6.md#id1)

Topics

- [Ansible 2.6](ROADMAP_2_6.md#ansible-2-6)

  - [Release Schedule](ROADMAP_2_6.md#release-schedule)

    - [Actual](ROADMAP_2_6.md#actual)
  - [Release Manager](ROADMAP_2_6.md#release-manager)
  - [Engine improvements](ROADMAP_2_6.md#engine-improvements)
  - [Core Modules](ROADMAP_2_6.md#core-modules)
  - [Cloud Modules](ROADMAP_2_6.md#cloud-modules)
  - [Network](ROADMAP_2_6.md#network)

    - [Connection work](ROADMAP_2_6.md#connection-work)
    - [Modules](ROADMAP_2_6.md#modules)
    - [Other Features](ROADMAP_2_6.md#other-features)
  - [Windows](ROADMAP_2_6.md#windows)

## [Release Schedule](ROADMAP_2_6.md#id2)

### [Actual](ROADMAP_2_6.md#id3)

- 2018-05-17 Core Freeze (Engine and Core Modules/Plugins)
- 2018-05-21 Alpha Release 1
- 2018-05-25 Community Freeze (Non-Core Modules/Plugins)
- 2018-05-25 Branch stable-2.6
- 2018-05-30 Alpha Release 2
- 2018-06-05 Release Candidate 1
- 2018-06-08 Release Candidate 2
- 2018-06-18 Release Candidate 3
- 2018-06-25 Release Candidate 4
- 2018-06-26 Release Candidate 5
- 2018-06-28 Final Release

## [Release Manager](ROADMAP_2_6.md#id4)

- 2.6.0-2.6.12 Matt Clay (IRC/GitHub: @mattclay)
- 2.6.13+ Toshio Kuratomi (IRC: abadger1999; GitHub: @abadger)

## [Engine improvements](ROADMAP_2_6.md#id5)

- Version 2.6 is largely going to be a stabilization release for Core code.
- Some of the items covered in this release, but are not limited to are the following:

  - `ansible-inventory`
  - `import_*`
  - `include_*`
  - Test coverage
  - Performance Testing

## [Core Modules](ROADMAP_2_6.md#id6)

- Adopt-a-module Campaign

  - Review current status of all Core Modules
  - Reduce backlog of open issues against these modules

## [Cloud Modules](ROADMAP_2_6.md#id7)

## [Network](ROADMAP_2_6.md#id8)

### [Connection work](ROADMAP_2_6.md#id9)

- New connection plugin: eAPI [proposal#102](https://github.com/ansible/proposals/issues/102)
- New connection plugin: NX-API
- Support for configurable options for network_cli & netconf

### [Modules](ROADMAP_2_6.md#id10)

- New `net_get` - platform independent module for pulling configuration with SCP/SFTP over network_cli
- New `net_put` - platform independent module for pushing configuration with SCP/SFTP over network_cli
- New `netconf_get` - Netconf module to fetch configuration and state data [proposal#104](https://github.com/ansible/proposals/issues/104)

### [Other Features](ROADMAP_2_6.md#id11)

- Stretch & tech preview: Configuration caching for network_cli. Opt-in feature to avoid `show running` performance hit

## [Windows](ROADMAP_2_6.md#id12)
